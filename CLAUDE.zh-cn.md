# CLAUDE.md

> **语言：** 简体中文译文  
> **原文：** [韩文原文](./CLAUDE.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](./docs/zh-cn/GLOSSARY.md)）

在本仓库工作时必须遵守的规则与背景。

## 本仓库是什么

这里是关于 **MIDAS NX Open API**（MIDAS Gen NX / Civil NX）由人工直接策展的
**JSON 架构手册**仓库。不是代码库，而是文档仓库。

- `docs/manual/01_DOC.md` ~ `27_Design_SRC_AIKSRC2K.md` — 27 个章节、共约 270 个端点，
  以 MIDAS 官方 Zendesk 在线手册为基准进行文档化。`docs/manual/INDEX.md` 是全量目录/数量索引。
- `docs/plugin/` — MIDAS 插件（用 MIDAS API + Python 制作、内嵌在 GUI 中的成品自动化工具）
  文档。它与 `docs/manual/` 分属不同文件夹的原因以及文档性质的差异，见 `docs/plugin/INDEX.md` 顶部说明。
  `INDEX.md` 既是目录也是进度（已撰写/待撰写）跟踪表——单个工具文档正在逐步补全，
  所以要先确认状态。
- `docs/AUTHENTICATION.md` — 认证、GET/PUT 工作流、防火墙指南等 Quick Tips。
- `examples/` — Python/VBA/JavaScript/curl/其他语言示例。
- `scripts/manual_sync/` — 与官方网站的定期同步工具，`docs/manual`、`docs/plugin` 两者都是
  对象（见下文）。

## 范围：只聚焦本仓库

**兄弟仓库 `MIDAS-API-NX-SDK`（Python SDK）不动。** 本仓库是纯文档，SDK 是独立项目。
除非请求的是 SDK 相关工作，否则不引用、也不修改那个仓库。

## 手册/插件同步工作流（`scripts/manual_sync/`）

目的：把官方 Zendesk Help Center 的两个节与各自的本地文档定期对齐。设计原则是
**列表比较不用 AI，只对确实需要打补丁的条目调用 AI** — 详细流程见
`scripts/manual_sync/README.md`。

| 节名称（`--section`） | Zendesk 目标 | 跟踪方式 | 本地文档 |
| --- | --- | --- | --- |
| `manual` | JSON Manual 节（651 篇文章，`section_id=30087500371097`） | 直接使用节的列表 API | `docs/manual/*.md` |
| `plugin` | Plug-in 节（`section_id=35681419399961`） | ⚠️ 节的列表 API 只返回 1 条落地页，因此对 `common.py` 的 `PLUGIN_ARTICLE_IDS`（70 条固定列表）逐条单独查询 | `docs/plugin/**/*.md` |

```bash
cd scripts/manual_sync
python fetch_manifest.py                  # 刷新快照，无参数时处理 manual+plugin 全部
python fetch_manifest.py --section plugin # 只处理特定节
python check_diff.py                      # 确认是否有变更（exit 0=两者都没有，1=至少有一项）
python validate_manual.py                 # 打完补丁后必须运行——同时校验 docs/manual+docs/plugin
```

**收到“定期核查更新”的请求时：**

1. 用 `check_diff.py` 分别提取两个节中已变更的文章 id 列表。
2. 对被标记的每一篇文章重读原文，并与文档按字段/内容逐条比对——必须区分“只刷新了
   时间戳的表面改动（cosmetic bump）”与“实际内容变更”。不得只看时间戳 diff 就
   假定发生了变更。
   - **先看 `locale_note`。** 文章级别的 `updated_at` 是 ko/en-us/**ja** 各译本时间戳的最大值，
     而本仓库只取回 en-us 正文。所以只编辑了 ko/ja 的情况下，会出现“被判定为 changed，
     但取回的正文没变”的状态；若把这当成表面改动放过，就会把真实变更整块漏掉。
     `check_diff.py` 会针对每个 changed 给出判定，因此出现 `en-us did NOT` 时必须亲自打开对应
     语言版本的页面进行比对。
   - 在 `plugin` 节中，若落地 article（id `35639730101529`，"Plug-in Online Manual"）被判定为变更，
     这可能不是实际内容变更，而是**Plug-in 列表本身被新增/删除/改名的信号**。
     需重新抓取落地页、重新抽取链接列表，并与 `docs/plugin/INDEX.md` 及
     `common.py` 的 `PLUGIN_ARTICLE_IDS` 比对后更新。
3. 只把确有变更的条目反映到对应文档（`docs/manual/*.md` 或 `docs/plugin/**/*.md`），必要时
   同步更新 `INDEX.md`（日期·条目数量·状态）。`docs/plugin` 中“⬜ 待撰写”的条目即使没有 diff
   也当然保持原样——是否已撰写目前还不属于定期巡检的对象。
4. 确认 `validate_manual.py` 通过后，用 `fetch_manifest.py` 对该节重新快照。
5. 再跑一次 `check_diff.py`，确认是 `has_diff: false`。
6. 提交与推送仅在用户明确指示时才进行（无自动 push — 见下文）。

规模较大时（例：同时有 20~30 篇文章被标记）拆成并行子代理会更高效：第一轮专职调研/比对
（原文 vs 手册比较，只判定是否为实际变更），第二轮专职编辑，只拿第一轮确定的事实去应用
实际补丁。给编辑代理时必须具体指定原文文件路径、目标节、精确的字段 diff、要仿照的
样式模板章节。

### 已知环境问题

- **`python3` 在本机指向已损坏的 Windows Store 存根。** 必须使用 `python`（3.13.5）。
- **`check_diff.py` 的 stdout 在 Windows 控制台（cp949）下可能抛出 `UnicodeEncodeError`**
  （`\xa0` 等无法编码的字符）。采用设置 `PYTHONIOENCODING=utf-8` 并把结果重定向到文件再读的
  方式绕开（不依赖直接捕获 stdout）。

### 解析抓取到的原文时

要用程序比对官方文章正文，必须先归一化两件事。
这两点都实际造成过解析失败：

- **空格是 U+00A0（不换行空格）** — 冒号后面与缩进用的不是普通空格。
  不先执行 `text.replace("\xa0", " ")`，正则与 `json.loads` 会悄无声息地错配。
- **示例 JSON 中的非法转义** — 部分文章的 `EXPORT_PATH` 没有对反斜杠转义，形如
  `"D:\00.2023년\..."`，导致那一个块在 `json.loads` 中被弃掉。整块会静默漏掉，
  因此不要忽略解析失败，而要把反斜杠加倍后重试。

### 官方文档错别字与自相矛盾的处理原则

官方文章中错别字和内部矛盾很常见。同一篇文章的 Specifications 表与 Request 示例给出不同
Key 的情况也有。判断基准：

- **示例（Request Examples）优先于表。** 示例是实际可运行的 payload，表是人工誊抄的。
  实际出现的错别字全都只在表里。
- **表与示例不一致时，在套用“示例优先”原则之前，先取回另一语言版本的正文。** 即使是同一篇
  文章 id，`/hc/ko/` 与 `/hc/en-us/` 的正文也可能不同。实际上 `/ope/MEMB` 的英文请求示例为
  `ELEM_LIST`（与表一致），仅韩文请求示例为 `AELEM`，当时只看了韩文版就套用示例优先原则，
  结果向官方提交了一条方向相反的错误报备，造成了事故（2026-09-06，
  Jira `MAPI-2484` A-7 已撤回）。若一侧语言版本内部自洽而只有另一侧自相矛盾，
  则自洽的一侧为正本。
- **与其他记录了同一 enum 的文章交叉核对。** 例：`STORY_DRIFT_METHOD` 的 3 个取值
  在第 10·13·17 节文章中各写错在不同的位置，只有第 17 节完好。
- **若写得与原文不同，就在那一处以 ⚠️ 注释留下依据。** 不留下的话下次同步会以“与原文不同”
  为由把它改回错别字。实际发生过一次这样的事故。
- 反过来说，因写法含糊而暂缓判断的情况也要用注释写明（例：第 20 章 Wall Force 的
  `SECT_POSITION`·`PARTS` 因官方 Specifications 表中没有说明，已注明属于推测）。

### 发给官方负责人的错误报备

把发现的官方文档错误汇总后整理成 Word 文档转交（使用 `python-docx`，本机已安装）。
产出物保存在 `docs/error_reports/`，`*.docx` 已被 `.gitignore` 处理，
不要提交进仓库。最近一次报备：`docs/error_reports/MIDAS_API_Manual_오류제보_20260827.docx`
（2026-08-27，13 件 — A. 错别字 8 件 + B. 表述不一致 5 件，在对 docs/manual 全量复检过程中发现）
— 本次没有用 Word 文档，而是直接登记为 Jira 子任务，在 `MAPI-2008` 之下的 `MAPI-2484`(A)·
`MAPI-2485`(B) 中跟踪。上一次报备（`MIDAS_API_Manual_오류제보_20260725.docx`，20 件）
在 `MAPI-2009`~`MAPI-2013` 中跟踪，实际已终结（详细内容参考会话记忆）。
报备文档中引用字符串要按原文照录，并注明**未验证实际 API 行为**，
把正本判断留给负责人。在提交新条目之前，必须重新抓取最新的官方页面确认仍可复现——
过去复检笔记中留下的发现，
有些在复核时已被修正，或本就有据不足。

## `docs/manual/*.md` 文档惯例

各端点章节按以下顺序：

1. `TABLE_TYPE`（或该端点对应的）enum/规格表
2. `Response HEAD`
3. （适用时）ADDITIONAL 子章节 — 标题格式为 `### ADDITIONAL — <说明> (<日期> 官方已反映)`，
   仅在请求中叠加了 config 对象时才添加
4. `Request / Response JSON`
5. `Python Example`

参数表使用 `| No. | 说明 | Key | 值类型 | 默认值 | 必填 |` 列。嵌套字段在说明前加缩进标记：
一级用 `└`，二级用“两个全角空格 + `└`”。

**表格 markdown 风格：** 新增的表必须使用带空格的分隔符（`| --- | --- |`）。
compact（`|---|---|`）会被 MD060 lint 拦下。**但原本已存在的 compact 风格表不动** — 它本来
就没被拦，而且不属于本次工作范围。

MD024（重复标题）/MD036（把强调当标题使用）告警在 `20_POST_AnalysisResult_2.md`、
`21_POST_StoryTables.md`、`26_Design_RC_KDS41202022.md` 等既有章节整篇范围内已是全文件通用
惯例。新章节沿用同一模式而出现同一告警是正常的 — 不是“需要修的东西”。

**新增 `## N. …` 章节时，必须同时在该章顶部的列表表（例：第 20 章“表的列表”）中补上对应行。**
`validate_manual.py` 只检查 *目录链接 → 标题* 这一个方向，因此目录列表中漏掉的标题
会通过校验。请自行确认章节数量与列表表行数一致。

向某章新增端点时，若该端点归属哪一章判断不清（例：结果表可能横跨多个
POST 章的情况），以官方文章自身的标题与各章文档开头写明的范围（例：“17 个”这类
数量表述）为依据判断。

## `docs/plugin/*.md` 文档惯例

不沿用 `docs/manual` 的 Key/Value 架构表惯例 — 因为 Plug-in 原文不是 REST 端点规格，
而是 GUI 使用方法 walkthrough。单个工具文档（`docs/plugin/tools/*.md`）按以下顺序
（`docs/plugin/INDEX.md` 底部有同一模板）：

1. 概述（Intro）2. 支持版本（Developed with）3. 主要功能（Benefits，如有）4. 使用方法
（按 UI 字段逐条说明，可用表）5. 参考/限制事项（Note）6. *（仅确认过的情况）*相关 JSON API 端点 —
若存在 Plug-in 内部疑似调用的 `docs/manual/*` 端点则相互链接，
不确定就不要凭猜测加入 7. 原文链接。

**52 篇单个工具文档（`tools/*.md`）渐进式撰写** — 不要一次全部填完。
`docs/plugin/INDEX.md` 中“状态”列为 ⬜（待撰写）的条目，在用户请求时（或成批地）
重新抓取原文，按上述模板撰写，并把状态更新为 ✅。规模较大时，直接复用上文
“手册/插件同步工作流”中说明的研究/编辑分离子代理模式。`guide/` 下 4 篇概念·开发指南文档
已全部撰写完成。

文件名不用编号，而用工具名 slug 化（`tools/Alignment_Editor.md` 等）— 因为这是随时会新增
Plug-in 的扁平列表，一旦编号，每次插入都需要重新编号。

## Git 约定

- **提交与推送仅在用户明确指示时执行。** 没有“提交推送”这类明确指示时，
  即使产生了改动也不提交。
- 提交前用 `git status --short` 确认只暂存了预期的文件。
