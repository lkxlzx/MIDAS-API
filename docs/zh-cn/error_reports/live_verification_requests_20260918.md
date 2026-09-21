# 实测核验请求清单 (2026-09-18)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../error_reports/live_verification_requests_20260918.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../GLOSSARY.md)）

在提交官方手册（Zendesk）错误上报的过程中，收集了**仅凭文档无法定论的条目**。
您用实际 API 响应确认后，上报的方向与优先级即可确定。

## 为什么需要

本仓库（`MIDAS-API`）是誊录官方文档的文档仓库，因此判断官方文档是否出错时能用的依据
**只有官方页面内部的证据**。当表与示例给出不同的值、或韩文/英文 locale 出现分歧时，
在文档内部无法得出哪一方为正本的结论。

实际上 2026-09-06 处理 `/ope/MEMB` 一案时，只看韩文页面就下了判断，结果**提交了方向相反的
错误上报、随后又撤回**（Jira `MAPI-2484` A-7）。相反，`MAPI-2375` 由负责开发确认了实际动作，
以「表中写的 `SET_STORY_DRIFT_METHOD` 是无效字段，即使输入也会被静默忽略」的结论结案。
实测结果充当文档争论的裁判。

## 核验方法（通用）

1. **基准 payload 原样使用官方 article 的示例**，**一次只改一个字段**。
2. **请勿只凭 HTTP 200 下判定。** 这是最关键的部分。MIDAS API 对不认识的字段不会拒绝，
   而是可能**静默忽略**（`MAPI-2375` 先例）。务必在 POST 之后**用 GET 再读一次，
   确认值是否真的被反映**。
3. 因此各条目的判定分三种：**拒绝（报错）** / **受理·已反映** / **受理但被忽略**。

---

## A. 定论型 — 依结果改变上报方向

### A-1. `/ope/MEMB` — 请求字段名是 `SELETION_TYPE` 还是 `SELECTION_TYPE`

- article `49514964272665` ([英文](https://support.midasuser.com/hc/en-us/articles/49514964272665))
- **矛盾：** Specifications 表第 2 行的 Key 是 `"SELETION_TYPE"`（韩文、英文页面各出现 1 次），
  而同一页面的 Input JSON 示例韩文、英文均为 `"SELECTION_TYPE"`。

**步骤** — 必须使用 `ASSIGN_TYPE: "MANUAL"` + 指定选择对象的组合。
`"AUTO"`/`"ALL"` 组合即使该字段被忽略、结果看起来也一样，没有判别力。

```jsonc
// (a) 基准：官方英文示例原样
{ "Argument": { "ASSIGN_TYPE": "MANUAL", "SELECTION_TYPE": "SELECTION",
                "ELEM_LIST": [640, 692], "ALLOW_SINGLE": false } }

// (b) 只把键名换成表中的写法
{ "Argument": { "ASSIGN_TYPE": "MANUAL", "SELETION_TYPE": "SELECTION",
                "ELEM_LIST": [640, 692], "ALLOW_SINGLE": false } }
```

**解读**

| (b) 结果 | 结论 |
| --- | --- |
| 拒绝（报错） | 表存在拼写错误。请求把表更正为 `SELECTION_TYPE` — 当前上报内容正确 |
| 受理 + 选择已反映 | 两个键是别名。表虽是拼写错误但无害 → 优先级下调 |
| 受理但选择未反映 | **静默忽略。** 与 `MAPI-2375` 属同一类型，最为危险 — 优先级上调 |

### A-2. `/db/SSEIS` — `SEIS_CODE` 值冒号后的空格

- article `58908676674585`
- **矛盾：** 韩文页面的**可复制示例**为 `"SEIS_CODE": "KDS(41-17-00: 2019)"`（有空格），
  而英文示例与 JSON Schema 的 `const` 为 `"KDS(41-17-00:2019)"`（无空格）。同一韩文页面的
  Specifications 表也无空格，页面内部自身不一致。
- `SEIS_CODE` 在 schema 上是 `const`，写法不同可能被校验拦下。

**步骤：** 用同一 payload 分别发送两种写法。

```jsonc
"SEIS_CODE": "KDS(41-17-00:2019)"    // (a) 无空格
"SEIS_CODE": "KDS(41-17-00: 2019)"   // (b) 有空格 — 韩文示例原样复制的形态
```

**解读**

| (b) 结果 | 结论 |
| --- | --- |
| 拒绝 | 确凿存在**复制韩文示例就会失败**的真实使用损害 → A-8 的首要依据 |
| 受理 | 服务器对空格做了归一化。降为统一写法的要求级别 |

### A-3. `/db/TDNA` — `RADIUS` 的类型

- article `35954555962137`
- **矛盾：** Specifications 表中同一个 `"RADIUS"` 条目按区间分成三种类型。

| 区间 | 表的写法 | JSON Schema |
| --- | --- | --- |
| `PROFY` (2D Round, x-y) | `Boolean` / 默认值 `false` | `"type": "number"` |
| `PROFZ` (2D Round, x-z) | `Number` / `0` | `"type": "number"` |
| `PROF` (3D Spline) | `Array` / `0` | `"type": "number"` |

schema 三个分支都是 `number`，3D 示例也是标量 `"RADIUS": 0` · `"RADIUS": 20`。

**步骤：** (a) 三个分支都用数字（官方示例原样）→ 基准。(b) `PROFY.RADIUS` 给 `false`。
(c) `PROF.RADIUS` 给数组 `[0, 20]`。

**解读：** 若 (b)·(c) 被拒绝，表中两行即确定为错误，「三行全部为 `Number`」的上报也就确定。
假如 (c) 被**受理**，则意味着只有 3D 分支实际接收数组，那时出错的是 schema 一方，上报方向
就会反过来。**正因为存在这种可能性，才需要确认。**

---

## B. 补强型 — 结论已由文档得出，实测用于强化依据

### B-1. `/db/SSEIS` — 拼错的键 `IINHERENT_TORSION` / `NHERENT_TORSION`

正确的键是 `INHERENT_TORSION`。官方示例中仍残留拼错的形态，请确认原样复制发送后会怎样。
**若是被忽略**，就成为「复制示例会静默丢失该选项」的具体损害，上报的分量也随之不同。

### B-2. 表中缺失的字段是否真的起作用

下列字段**存在于 JSON Schema·示例中，但 Specifications 表里没有对应行。** 请确认它们是否出现
在 GET 响应中、用 POST/PUT 设置时是否被反映，确认后「表缺项」的上报即可定案。

| 端点 | 字段 |
| --- | --- |
| `/db/MATD` | `bSERVCHECK` · `dSHORTTERM` · `dLONGTERM` |
| `/db/SPLC` | `ALONG` |

---

## C. 无法用实测确认的条目（不属于请求范围）

为免白费力气，在此明确。以下是**与服务器行为无关的写法·文句问题**，只能通过文档修订解决。

- `/db/PNLA` 条件标签 `When Element Select Type` ↔ `When Element Type`（说明文句）
- `/ope/GSBG` Component 列表中的 `• -Sbz" 4`（冒号位置出现双引号 — 标点符号）
- `/db/SPLC` `fasle` · `Eccentricitiy`、`/db/DSTL` `maxroperties`（说明文字段的拼写错误）
- `/db/SSEIS` 韩文正文污染（两个 article 的韩文正文变得相同的编辑事故）

---

## 结果回复格式

按条目填写以下内容，即可原样引用到 Jira 上报中。

| 项目 | 改动的字段 | HTTP 状态 | 响应摘要 | GET 再查结果 | 判定 |
| --- | --- | --- | --- | --- | --- |
| A-1 (b) | `SELETION_TYPE` | | | 选择是否被反映？ | 拒绝 / 反映 / 忽略 |

也请一并写明用于核验的产品·构建版本。由于存在官方文档与产品版本错开的情况，
上报时需要以此明确依据的适用范围。
