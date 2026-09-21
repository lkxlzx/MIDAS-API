# MIDAS API Manual Sync

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）

用于将 `docs/manual/`（JSON Manual 节）与 `docs/plugin/`（Plug-in 节）与 MIDAS API 官方在线手册（Zendesk Help Center）定期同步的脚本集合。核心设计：**列表比对不借助 AI，只对确实需要打补丁的条目调用 AI**，从而避开每次重新审阅全文所需的 token 成本。

## 跟踪对象节

已登记在 `common.py` 的 `SECTIONS` 中，可用 `--section manual|plugin` 参数单独指定，也可省略该参数以全部为对象执行。两个节的跟踪**方式（mode）**不同。

| 名称 | mode | 对象文档 | 清单（manifest） |
| --- | --- | --- | --- |
| `manual` | `section` — 用 `sections/{id}/articles.json` 一次性列出 651 篇文章（JSON Manual，`section_id=30087500371097`） | `docs/manual/*.md` — REST 端点 schema 表 | `docs/manual/.sync_manifest.json` |
| `plugin` | `id_list` — 将 `common.PLUGIN_ARTICLE_IDS`（57 个，显式列表）用 `articles/{id}.json` 逐篇查询 | `docs/plugin/**/*.md` — GUI 内建 Plug-in 工具用法 | `docs/plugin/.sync_manifest.json` |

`plugin` 之所以是 `id_list`：Plug-in 的 Zendesk 节（`section_id=35681419399961`）即使调用 `sections/{id}/articles.json` 也**只**返回 "Plug-in Online Manual" 落地页这 **1 篇**。其余 56 篇（指南 4 + 单个工具 52）只是该落地页正文 HTML 里的 `<a href>` 链接，并且各自分散在无法通过 API 查找到的独立 `section_id` 之下。因此把创建 `docs/plugin/INDEX.md` 时抽取出的 57 个 article id 作为固定列表写死在 `common.py` 里，逐篇查询。**新增 Plug-in 时，落地页自身的 `updated_at` 会变化，因此 `changed` 列表里会捕获到该落地页文章（`35639730101529`）**，并把这当作信号去重新抓取落地页、更新 `PLUGIN_ARTICLE_IDS` 与 `INDEX.md`（因为需要修改代码，所以不会自动反映）。

## 组成

| 文件 | 作用 | 是否用 AI |
|---|---|---|
| `common.py` | Zendesk API 调用、节注册表、清单读取/保存、diff 计算等公共逻辑 | ✗ |
| `fetch_manifest.py` | 把当前主页状态按节快照保存到 `.sync_manifest.json`（省略 `--section` 时为全部） | ✗ |
| `check_diff.py` | 按节比较清单与当前主页状态，只抽出 added/removed/changed article（省略 `--section` 时为全部）。对每个 changed 条目**判定是哪个语种发生了变化**，以 `locale_note` 标注（可用 `--no-locales` 省略） | ✗ |
| `validate_manual.py` | 校验 `docs/manual/*.md` + `docs/plugin/**/*.md` 的 JSON 代码块有效性 + TOC 锚点一致性 | ✗ |
| `prompt_sample.md` | 最初由人手撰写手册文档（01~27）时所使用的提示词示例（仅供参考，不是执行脚本） | — |

AI（Claude）不会在 CI 中被自动调用 — **不把 API 密钥登记到 CI 正是有意为之的设计**。作为替代，GitHub Actions 只免费确认是否存在变更并以 GitHub Issue 通知，实际打补丁由人打开 Claude Code 对话窗口亲自触发。

## 工作原理

```
[每周，低成本，免费] GitHub Actions → check_diff.py（manual + plugin 两个节都查）
      │  只查询 Zendesk article 的 id/updated_at，与清单比较
      │  → 纯脚本，不调用 LLM，不需要 API 密钥
      │
      ├─ 无变更 → 结束
      │
      └─ 有变更 → 生成/更新 GitHub Issue（含 diff + 待粘贴的提示词）
             │
             └─ [由人触发] 把 issue 内容粘贴到 Claude Code 对话窗口
                    → 只重新抓取对应条目 → 只打补丁被映射到的节
                    → 用 validate_manual.py 校验 → 用 fetch_manifest.py 更新清单
                    → 提交与推送在用户确认后推进
```

## 本地运行

```bash
cd scripts/manual_sync

# 首次 1 次，或反映更新之后刷新快照（无参数时为 manual+plugin 全部）
python3 fetch_manifest.py
python3 fetch_manifest.py --section plugin   # 只针对特定节

# 只确认是否有变更（exit 0 = 无变更，exit 1 = 有变更 + 输出 diff）
python3 check_diff.py

# 文档打补丁后必须执行 — 校验 JSON/TOC 完整性（docs/manual + docs/plugin 全部扫描）
python3 validate_manual.py
```

## 语种判定 — 报了 `changed` 但正文原封不动时

Zendesk 的文章级 `updated_at` 是**该文章所有译本 `updated_at` 中的最大值**。
而 `common.py` 的 `BASE`（`SYNC_LOCALE = "en-us"`）**只**拉取英文正文。因此
只有 ko 或 ja 被编辑的情况 → `check_diff.py` 会判定为 changed → 但拉回来的英文正文一个字都
没变。如果把这种情形判成"只更新了时间戳的面子工程"就此跳过，**就会把真实变更整个漏掉。**

`check_diff.py` 对每个 changed 条目调用一次 `articles/{id}/translations.json`
（只挑比上一次快照的 `updated_at` 更新的语种），据此判定为以下三种之一：

| `locale_note` | 意思 | 应对 |
| --- | --- | --- |
| `en-us changed — normal review` | 与平时一样，英文正文发生了变化 | 按既有流程对照 |
| `ko/ja changed but en-us did NOT ...` | **我们所拉取的正文中看不见的变更** | 直接打开该语种页面进行对照 |
| `metadata only — no translation body is newer` | 没有任何译本变新 | 确实是面子工程，可以跳过 |

实测依据（2026-09-06，719 篇全量扫描）：

- 719 篇中 492 篇为 `ko+en-us+ja`，174 篇为 `ko+en-us`。**"存在 ja 译本"这一事实本身，在
  本次扫描之前都未被掌握。**
- `/ope/MEMB`（`49514964272665`）的 `2026-07-30` 更新，既不是 ko 也不是 en-us，而是由 **ja 译本**
  造成的。反倒是 ko 与 en-us 正文自 2025 年起就一直以请求 Key 互不相同的状态被搁置，
  正因为没看到这个分叉，我们向官方提交过**方向相反的错误报告**，随后撤回
  （Jira `MAPI-2484` A-7）。
- SSEIS（`58908676674585`）的 ko 正文污染也属于 en-us 完好、只有 ko 变动的情况，若没有这一判定，
  该事项会被当成面子工程过滤掉。

**若要全量检查各语种正文之间偏离到什么程度**，比较 `translations.json` 里各篇文章的
`updated_at` 与正文长度即可（见 `common.py` 的 `fetch_translations()`）。
2026-09-06 的扫描中，得出了正文长度比例严重错位的 9 篇，以及 **ko 正文按字节完全相同的
文章对 2 对**（SSEIS、Static Wind Load）。

## GitHub Actions（仅检查，不需要 API 密钥）

`.github/workflows/manual-sync.yml` 每周一（UTC 03:17）只执行 `check_diff.py`。检测到变更时：
- 在执行日志中输出 diff
- 把 diff JSON 作为 `manual-diff` 构件（artifact）上传
- 在仓库中创建 "MIDAS API manual 变更检测" issue（若已有打开的 issue 则追加评论）— issue 正文中包含**可直接原样复制、粘贴到 Claude Code 对话窗口的提示词**。

不需要追加登记任何 secret（只使用默认 `GITHUB_TOKEN`）。**手动执行：** Actions 标签页 → "MIDAS API Manual Sync Check" → Run workflow。

## 实际更新怎么做

1. 确认 issue 通知（或直接执行 `python3 check_diff.py` 得到的结果）
2. 把 issue 正文中的提示词原样粘贴到已打开本仓库的 Claude Code 对话窗口
3. Claude 只重新核对 diff 对应的 article，对映射到的节打补丁，并用 `validate_manual.py` 校验
4. 提交与推送一律由 Claude 在取得用户确认后推进（没有自动 push/PR）
