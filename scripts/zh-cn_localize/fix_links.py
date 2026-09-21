"""Rewrite relative links inside the zh-cn mirrors produced by the localisation pass.

Translation agents copy link targets verbatim from the Korean original, so every mirror
sits one directory level deeper than those copies assume. This resolves each relative link
against the *original* file it was copied from, then re-emits it from the mirror's real
location - pointing at the zh-cn mirror when one exists, at the Korean original otherwise.

`path#anchor` links are the hard case: the anchor comes from a heading a different agent
translated. Because translation preserves heading order 1:1, the anchor is resolved by
heading *index* - original anchor -> index of that heading in the Korean file -> anchor
recomputed from the same-index heading in the mirror.

Also substitutes the {{ORIGINAL}} / {{GLOSSARY}} placeholders, and audits each mirror
against its original (heading-count parity, links this script broke, leftover Korean)
instead of silently guessing.

Usage:
    python scripts/zh-cn_localize/fix_links.py            # rewrite in place + report
    python scripts/zh-cn_localize/fix_links.py --check     # report only, write nothing

Exit 0 -> clean. Exit 1 -> reported problems need a human look.
"""
import argparse
import os
import re
import sys

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
GLOSSARY = "docs/zh-cn/GLOSSARY.md"

sys.path.insert(0, os.path.join(REPO, "scripts", "manual_sync"))
from validate_manual import gh_anchor  # noqa: E402  single source of truth for anchors

# group 1 = "[text](" (with leading "!" for images), 2 = link text, 3 = target, 4 = ")"
MD_LINK = re.compile(r"(!?\[[^\]]*\]\()([^)\s]+)(\))")
PLACEHOLDER = re.compile(r"\]\((\{\{ORIGINAL\}\}|\{\{GLOSSARY\}\})\)")
HEAD = re.compile(r"^#{1,6} (.*)$", re.MULTILINE)
HANGUL = re.compile(r"[가-힣]")
FENCE = re.compile(r"```.*?```", re.S)
SKIP = ("http:", "https:", "mailto:", "#", "/", "ftp:")
CODE_EXT = (".md", ".py", ".bas", ".html", ".js")


def norm(p):
    return p.replace("\\", "/")


def is_mirror(rel):
    return "/zh-cn/" in rel or rel.endswith(".zh-cn.md") or "_zh-cn/" in rel


def to_mirror(rel):
    """Korean original path -> its zh-cn mirror path, or None when not mirrored."""
    rel = norm(rel)
    if is_mirror(rel) or rel.startswith("scripts/zh-cn_localize/"):
        return None
    b = rel.rsplit("/", 1)[-1]
    d = rel[: -len(b)].rstrip("/")
    if rel == "docs/AUTHENTICATION.md":
        return "docs/zh-cn/AUTHENTICATION.md"
    if rel in ("README.md", "CLAUDE.md"):
        return rel[:-3] + ".zh-cn.md"
    # examples/<lang>/README.md sits next to runnable code; infix beats another zh-cn/ dir
    if rel.startswith("examples/") and b == "README.md":
        return f"{d}/README.zh-cn.md" if d else "README.zh-cn.md"
    if rel.startswith("docs/manual/"):
        return f"docs/manual/zh-cn/{b}"
    if rel.startswith("docs/plugin/"):
        return "docs/plugin/zh-cn/" + norm(rel)[len("docs/plugin/"):]
    if rel.startswith("docs/plugin_cases/articles/"):
        return f"docs/plugin_cases/articles_zh-cn/{b}"
    if rel.startswith("docs/plugin_cases/planning/"):
        return f"docs/plugin_cases/planning_zh-cn/{b}"
    if rel.startswith("docs/error_reports/"):
        return f"docs/zh-cn/error_reports/{b}"
    if os.path.splitext(b)[1].lower() in CODE_EXT:
        return f"{d}/zh-cn/{b}" if d else f"zh-cn/{b}"
    return None


def exists(rel):
    """Files *and* directories - README/examples link at folder targets too (./python/)."""
    p = os.path.join(REPO, norm(rel).replace("/", os.sep))
    return os.path.isfile(p) or os.path.isdir(p)


def read(rel):
    with open(os.path.join(REPO, norm(rel).replace("/", os.sep)), encoding="utf-8") as f:
        return f.read()


def write(rel, text):
    """Preserve each file's own line endings; a VBA .bas saved as CRLF must stay CRLF."""
    path = os.path.join(REPO, norm(rel).replace("/", os.sep))
    with open(path, "rb") as f:
        crlf = b"\r\n" in f.read()
    with open(path, "w", encoding="utf-8", newline="\r\n" if crlf else "\n") as f:
        f.write(text)


def anchors_of(text):
    """Anchors in document order, with validate_manual's duplicate handling."""
    out, seen = [], {}
    for h in HEAD.findall(text):
        a = gh_anchor(h)
        if a in seen:
            seen[a] += 1
            a = f"{a}-{seen[a]}"
        else:
            seen[a] = 0
        out.append(a)
    return out


_ANCHORS = {}


def anchor_list(rel):
    if rel not in _ANCHORS:
        _ANCHORS[rel] = anchors_of(read(rel)) if exists(rel) else None
    return _ANCHORS[rel]


def rel_from(from_dir, target):
    r = norm(os.path.relpath(target, from_dir or "."))
    return r if r.startswith(".") else "./" + r


def map_anchor(orig_rel, frag, dest_rel, problems, where):
    """Turn a fragment authored against orig_rel into one valid in dest_rel."""
    dst = anchor_list(dest_rel)
    if dst is not None and frag in dst:
        # Some translators rewrite cross-file anchors themselves instead of copying them.
        # If the fragment already resolves in the destination, trust it over index mapping.
        return frag
    src = anchor_list(orig_rel)
    if src is None or dst is None:
        return frag
    if frag not in src:
        problems.append(f"{where}: anchor not found in original -> {orig_rel}#{frag}")
        return frag
    i = src.index(frag)
    if i >= len(dst):
        problems.append(f"{where}: heading index {i} past end of {dest_rel}")
        return frag
    return dst[i]


def check_cross_anchors(finals):
    """Report path#anchor links whose fragment does not exist in the destination file.

    validate_manual.py only resolves same-page anchors, so the 124 cross-file
    `path#anchor` links in this repo have no other gate covering them. `finals` carries
    the post-rewrite text so this reports on what actually lands, not on stale disk state.
    """
    bad = []
    for rel in sorted(finals):
        if not rel.endswith(".md"):
            continue
        d = rel[: -len(rel.rsplit("/", 1)[-1])].rstrip("/")
        for m in MD_LINK.finditer(finals[rel]):
            raw = m.group(2)
            if raw.startswith(SKIP) or "#" not in raw or "{{" in raw:
                continue
            path, _, frag = raw.partition("#")
            target = norm(os.path.normpath(os.path.join(d, path))) if path else d
            if not exists(target):
                continue  # pre-existing broken link (e.g. gitignored videos/) - not ours
            dst = anchor_list(target)
            if dst is not None and frag not in dst:
                bad.append(f"{rel}: dead cross-file anchor -> {path}#{frag}")
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report without writing")
    args = ap.parse_args()

    tracked = set()
    for root, dirs, names in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__")]
        for n in names:
            tracked.add(norm(os.path.relpath(os.path.join(root, n), REPO)))
    orig_by_mirror = {}
    for rel in tracked:
        m = to_mirror(rel)
        if m and m in tracked:
            orig_by_mirror[m] = rel

    problems, rewritten, finals = [], 0, {}
    for mirror_rel, orig_rel in sorted(orig_by_mirror.items()):
        text = read(mirror_rel)
        before = text
        mdir = mirror_rel[: -len(mirror_rel.rsplit("/", 1)[-1])].rstrip("/")
        odir = orig_rel[: -len(orig_rel.rsplit("/", 1)[-1])].rstrip("/")

        def sub_ph(m, _mdir=mdir, _orig=orig_rel):
            target = _orig if "ORIGINAL" in m.group(1) else GLOSSARY
            return "](" + rel_from(_mdir, target) + ")"

        def sub_link(m, _mdir=mdir, _odir=odir, _where=mirror_rel, _orig=orig_rel):
            raw = m.group(2)
            if raw.startswith(SKIP):
                return m.group(0)
            path, _, frag = raw.partition("#")
            target = None
            # Resolve against the original's dir first; fall back to the mirror's own dir so a
            # second run sees already-rewritten "../" paths instead of mangling them.
            for base in (_odir, _mdir):
                cand = norm(os.path.normpath(os.path.join(base, path))) if path else base
                if exists(cand):
                    target = cand
                    break
            if target is None:
                return m.group(0)
            mir = to_mirror(target)
            dest = mir if (mir in tracked and exists(mir)) else target
            if target == _orig:
                dest = target  # this mirror's own provenance link: must keep pointing at the original
            elif target == _where:
                dest = _orig  # self-link damage from an earlier run: heal back to the original
            if exists(target) and not exists(dest):
                problems.append(f"{_where}: redirected to non-existent {dest}")
            new = map_anchor(target, frag, dest, problems, _where) if frag else ""
            out = rel_from(_mdir, dest)
            if path.endswith("/") and not out.endswith("/"):
                out += "/"  # keep directory links (./python/) as directories
            return m.group(1) + out + (("#" + new) if new else "") + m.group(3)

        text = PLACEHOLDER.sub(sub_ph, text)
        text = MD_LINK.sub(sub_link, text)

        # Heading parity only means something for markdown: "^# " is a Python/VBA/HTML
        # comment marker, and plugin_cases/articles/ originals carry no "##" sections at all
        # while the accepted en / zh-tw mirrors promote them - parity there is convention,
        # not a defect.
        if mirror_rel.endswith(".md") and not mirror_rel.startswith("docs/plugin_cases/"):
            src_n, dst_n = len(anchor_list(orig_rel)), len(anchor_list(mirror_rel))
            if src_n != dst_n:
                problems.append(f"{mirror_rel}: {dst_n} headings vs original {src_n}")
        # JSON blocks stay byte-identical to the original (GLOSSARY S4), so hangul inside
        # fences is correct - only prose counts as untranslated.
        prose = FENCE.sub("```\n```", text)
        orig_prose = FENCE.sub("```\n```", read(orig_rel))
        left, orig_left = len(HANGUL.findall(prose)), len(HANGUL.findall(orig_prose))
        if orig_left and left > orig_left * 0.2 + 40:
            problems.append(f"{mirror_rel}: {left} hangul in prose (original {orig_left})")

        if text != before:
            rewritten += 1
            if not args.check:
                write(mirror_rel, text)
        finals[mirror_rel] = text

    problems.extend(check_cross_anchors(finals))

    print(f"mirrors: {len(orig_by_mirror)}   rewritten: {rewritten}   "
          f"mode: {'check' if args.check else 'write'}")
    for p in problems:
        print("  !", p)
    print("problems:", len(problems))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
