#语言：简体中文译文 · 原文：[韩文原文](../common.py) · 译文生成：2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）
"""MIDAS API 手册同步脚本的公共辅助函数。这里不调用 AI — 只有纯 HTTP + diff 逻辑。"""
import json
import os
import time
import urllib.request

_DOCS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "docs")

SYNC_LOCALE = "en-us"  # 本仓库所镜像其正文的语种
BASE = f"https://support.midasuser.com/api/v2/help_center/{SYNC_LOCALE}"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

# "Plug-in" 这个 Zendesk 分节（id 35681419399961）不会通过 sections/{id}/articles.json 列出
# 所属文章 —— 该端点恰好只返回 1 篇文章（"Plug-in Online Manual" 落地页）。其余 56 篇只是
# 该落地页正文 HTML 里的 <a href> 链接，每一篇都各自待在一个自动生成的、否则无从发现的
# section_id 下。因此与 "manual"（真正的分节列表）不同，"plugin" 被跟踪为一份显式的
# article-id 白名单，通过 articles/{id}.json 逐篇查询。
# 若落地页自身的 updated_at 发生了变化，那就是重新抓取它的信号，
# 用来检查链接列表（docs/plugin/INDEX.md）本身
# 是否需要更新（工具新增/删除/改名）。
_PLUGIN_LANDING_ID = "35639730101529"  # Plug-in Online Manual（目录页）
_PLUGIN_GUIDE_IDS = [
    "35693347852569",   # Introduction to MIDAS Plug-in
    "35694950947353",   # How to use MIDAS Plug-ins
    "44321576105497",   # Guiding for writing Python Code
    "44321750649369",   # A Guide to Creating Plug-in for Developers
]
_PLUGIN_TOOL_IDS = [
    "35651992652441", "60307252076441", "35679369131289", "40709970824729",
    "35656036758937", "35650468767385", "46935970426905", "46857988729753",
    "52564358801049", "35661003551385", "35845551989401", "45536334603161",
    "60341711486361", "45496104876313", "41509743351193", "56841756166681",
    "60340982021529", "35639906272025", "45543036560921", "35649982873625",
    "49393118303897", "45352026157593", "35681919947673", "56728677543321",
    "45354275911321", "40706127836953", "50959239482393", "60469083421593",
    "35649669387289", "45537498601881", "35651585867801", "47130265330841",
    "45548001795865", "35654598923161", "52596776672537", "60470400396953",
    "35649267067545", "45716286965273", "35651417232025", "35658068066841",
    "45545604010521", "35824220762521", "58178248491161", "60317101122329",
    "52808991968665", "40708129121817", "40663607747737", "45306728128921",
    "60315550956825", "52715682940313", "35655721814937", "40645303004697",
    "60848073556633", "60848423734169",
    "60997850893209", "60998764028185",
    "61258768334233", "61259043302041", "61259174909849", "61259225090329",
    "61259382041369", "61486703401753", "61655350763289",
    # 2026-09-15 定期点检中通过重新抓取落地页发现（新增 2 个，删除 0 个）
    "61971621469849", "62123537156889",
]
# 2026-08-30 已废弃（官方站点已删除，确认返回 404）—— 不再是查询对象。docs/plugin/INDEX.md
# No.53/54（"Floor Load Table Generator"/"Easy Result Table"）以 ⚠️ 已废弃标注，文档予以保留。
#   "49475987573657", "49504449511705",
PLUGIN_ARTICLE_IDS = [_PLUGIN_LANDING_ID] + _PLUGIN_GUIDE_IDS + _PLUGIN_TOOL_IDS  # 70 ids

# 本仓库跟踪的 Zendesk 资源。"manual" = JSON Manual 分节（REST 端点
# schema 参考，docs/manual/*），"plugin" = Plug-in article-id 白名单（内嵌于 GUI 的
# 自动化工具，docs/plugin/*）。
SECTIONS = {
    "manual": {
        "mode": "section",
        "id": "30087500371097",
        "manifest": os.path.join(_DOCS_DIR, "manual", ".sync_manifest.json"),
    },
    "plugin": {
        "mode": "id_list",
        "ids": PLUGIN_ARTICLE_IDS,
        "manifest": os.path.join(_DOCS_DIR, "plugin", ".sync_manifest.json"),
    },
}
DEFAULT_SECTION = "manual"

# 向后兼容别名（旧的单分节脚本/调用方）。
SECTION_ID = SECTIONS[DEFAULT_SECTION]["id"]
MANIFEST_PATH = SECTIONS[DEFAULT_SECTION]["manifest"]


def _get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_translations(article_id, retries=4):
    """获取单篇文章的 {locale: {"updated_at": ..., "len": ...}}。

    分节列表返回的文章级 ``updated_at`` 是所有语种译本的 MAX，因此变动可能来自我们从不读取的
    语种。上面的 ``BASE`` 是 en-us Help Center，意味着只改了 ko 或只改了 ja 的编辑，在
    check_diff.py 里会表现为一篇 "changed" 文章，而其 en-us 正文逐字节完全相同 —— 这会被读成
    表面性的时间戳刷新而被放过。这个端点正是用来区分两者的。

    2026-09-06 实测：719 篇被跟踪的文章以各种组合带有 ko/en-us/ja；
    /ope/MEMB 的 2026-07-30 变动是*日文*译本造成的，而它的 ko 与 en-us 正文在请求 key 上
    互不相同，自 2025 年以来从未被改动过。
    """
    url = f"https://support.midasuser.com/api/v2/help_center/articles/{article_id}/translations.json"
    for attempt in range(retries):
        try:
            data = _get_json(url)
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))  # 轻度并发下 Zendesk 会返回 429
            continue
        return {
            t["locale"]: {
                "updated_at": t["updated_at"],
                "len": len(t.get("body") or ""),
            }
            for t in data.get("translations", [])
        }
    return {}


def locales_changed_since(article_id, old_updated_at):
    """哪些语种的正文在 ``old_updated_at`` 之后发生过变动。

    返回 (changed_locales, all_locales)。``changed_locales`` 为空表示没有任何译本比上一次快照
    更新 —— 即真正的仅元数据变动。``SYNC_LOCALE`` 不在列表里，意味着我们拉到的正文看起来不会
    有变化。
    """
    locales = fetch_translations(article_id)
    changed = sorted(
        loc for loc, meta in locales.items() if meta["updated_at"] > old_updated_at
    )
    return changed, locales


def fetch_all_articles(section_id=SECTION_ID):
    """通过 sections/{id}/articles.json 列表，为给定分节下的每篇文章获取
    {id: {title, updated_at, html_url}}（该方式只对确实通过 API 列出所属文章的分节有效；
    "plugin" 的例外见 PLUGIN_ARTICLE_IDS）。
    """
    articles = {}
    page = 1
    while True:
        data = _get_json(f"{BASE}/sections/{section_id}/articles.json?per_page=100&page={page}")
        for a in data.get("articles", []):
            articles[str(a["id"])] = {
                "title": a["title"],
                "updated_at": a["updated_at"],
                "html_url": a["html_url"],
            }
        if not data.get("next_page"):
            break
        page += 1
    return articles


def fetch_articles_by_ids(ids):
    """通过不区分语种的 articles/{id}.json 端点（不带 /en-us/ 前缀）逐篇获取
    {id: {title, updated_at, html_url}} —— 有些 Plug-in 文章（例如 Python 编码指南）只存在于
    ko 语种下，在 /en-us/ 会返回 404。用于所属文章无法通过分节 API 列出的分节（如 "plugin"）。
    """
    articles = {}
    for aid in ids:
        data = _get_json(
            f"https://support.midasuser.com/api/v2/help_center/articles/{aid}.json"
        )
        a = data["article"]
        articles[str(a["id"])] = {
            "title": a["title"],
            "updated_at": a["updated_at"],
            "html_url": a["html_url"],
        }
    return articles


def fetch_section(name):
    """按 SECTIONS[name]["mode"] 分派到正确的抓取策略。"""
    cfg = SECTIONS[name]
    if cfg["mode"] == "id_list":
        return fetch_articles_by_ids(cfg["ids"])
    return fetch_all_articles(cfg["id"])


def load_manifest(path=MANIFEST_PATH):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("articles", {})


def save_manifest(articles, path=MANIFEST_PATH, section_id=SECTION_ID):
    payload = {"section_id": section_id, "article_count": len(articles), "articles": articles}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write("\n")


def diff_articles(old, new):
    """纯比较，不用 AI。返回含 added/removed/changed id 列表的 dict。"""
    old_ids, new_ids = set(old), set(new)
    added = sorted(new_ids - old_ids)
    removed = sorted(old_ids - new_ids)
    changed = sorted(
        i for i in (old_ids & new_ids) if old[i]["updated_at"] != new[i]["updated_at"]
    )
    return {
        "added": [{"id": i, **new[i]} for i in added],
        "removed": [{"id": i, **old[i]} for i in removed],
        "changed": [
            {"id": i, "title": new[i]["title"], "html_url": new[i]["html_url"],
             "old_updated_at": old[i]["updated_at"], "new_updated_at": new[i]["updated_at"]}
            for i in changed
        ],
    }
