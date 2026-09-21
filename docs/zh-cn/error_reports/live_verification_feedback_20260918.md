# 实测核验反馈 (2026-09-18)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../error_reports/live_verification_feedback_20260918.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../GLOSSARY.md)）

核验产品为 MIDAS Gen NX 2026 v2.1 与 MIDAS Civil NX 2026 v2.2，两款
产品的 Build 均为 09/15/2026。所有核验都在自动保存后、于空白 scratch
文档中进行。判定时不只看 HTTP 状态，而是同时看响应正文与后续 GET。

## 结果概要

| 项目 | 产品 | 改动的字段 | HTTP 状态 | 响应摘要 | GET 再查结果 | 判定 |
| --- | --- | --- | --- | --- | --- | --- |
| A-1 (b) | Gen | `SELETION_TYPE` | 200 | `MEMB.1.AELEM = [2,3]` | `/db/MEMB/1.AELEM = [2,3]` | 受理·已反映 |
| A-1 (b) | Civil | `SELETION_TYPE` | 200 | `MEMB.1.AELEM = [2,3]` | `/db/MEMB/1.AELEM = [2,3]` | 受理·已反映 |
| A-2 (b) | Gen | `SEIS_CODE = "KDS(41-17-00: 2019)"` | 201 | 以无空格的代码响应 | `KDS(41-17-00:2019)` | 受理·已归一化 |
| A-3 (b) | Gen | `PROFY[1].RADIUS = false` | 201 + 错误正文 | `Wrong Field` | `Not Found Key` | 拒绝 |
| A-3 (b) | Civil | `PROFY[1].RADIUS = false` | 201 + 错误正文 | `Wrong Field` | `Not Found Key` | 拒绝 |
| A-3 (c) | Gen | `PROF[1].RADIUS = [0,20]` | 201 + 错误正文 | `Wrong Field` | `Not Found Key` | 拒绝 |
| A-3 (c) | Civil | `PROF[1].RADIUS = [0,20]` | 201 + 错误正文 | `Wrong Field` | `Not Found Key` | 拒绝 |
| B-1 | Gen | `IINHERENT_TORSION = true` | 201 | 拼错的键从响应中消失 | `INHERENT_TORSION = false` | 受理但被忽略 |
| B-1 | Gen | `NHERENT_TORSION = true` | 201 | 拼错的键从响应中消失 | `INHERENT_TORSION = false` | 受理但被忽略 |
| B-2 MATD | Gen | `bSERVCHECK = true` | 200 | 返回请求值 | `true` | 受理·已反映 |
| B-2 MATD | Gen | `dSHORTTERM = 1.25` | 200 | 返回请求值 | `1.25` | 受理·已反映 |
| B-2 MATD | Gen | `dLONGTERM = 1.5` | 200 | 返回请求值 | `1.5` | 受理·已反映 |
| B-2 MATD | Civil | `bSERVCHECK = true` | 200 | 返回请求值 | 无该字段 | 受理但被忽略 |
| B-2 MATD | Civil | `dSHORTTERM = 1.25` | 200 | 返回请求值 | 无该字段 | 受理但被忽略 |
| B-2 MATD | Civil | `dLONGTERM = 1.5` | 200 | 返回请求值 | 无该字段 | 受理但被忽略 |
| B-2 SPLC POST | Gen | `aACCECC_ECCEN_LIST[0].ALONG = 2.5` | 201 | 返回请求值 | `2.5` | 受理·已反映 |
| B-2 SPLC PUT | Gen | `ALONG: 2.5 -> 3.5` | 200 | 返回 `3.5` | 保持原值 `2.5` | 受理但被忽略 |

## A-1 结论

`SELECTION_TYPE` 与表中的拼写错误 `SELETION_TYPE`，目前在两款产品中都是
行为完全相同的别名。因此表中的拼写确实应当更正，但不属于「复制拼写错误
的调用被静默忽略、导致选择消失」的类型。
只把官方示例中该模型专用的单元编号 `640, 692` 替换为 scratch 模型中实际的 beam
单元 `2, 3`。

## A-2 结论

冒号后带空格的 KDS 代码 Gen 同样接受，并把 POST 响应与 GET 存储值
归一化为无空格的标准字符串。复制韩文示例在当前产品中不会失败，因此
属于统一写法的要求级别。

## A-3 结论

以官方在线 article 的 2D Round/Element 与 3D Round/Element 示例原样作为
基准。在各 scratch 文档中制作了与示例相同的 30 m 连续 beam 30 个、Tendon Group、官方
Magura Tendon Property。

- 以 2D 为基准的 `PROFY` 与 `PROFZ` 数字 `RADIUS` 值 `0, 20, 0`，在两款产品中
  都能生成，GET 中也以数字保留。
- 以 3D 为基准的 `PROF` 数字 `RADIUS` 值 `0, 20, 0`，同样在两款产品中
  生成，GET 中也以数字保留。
- `PROFY.RADIUS = false` 与 `PROF.RADIUS = [0,20]` 在两款产品中都被
  判为 `Wrong Field` 而拒绝。该 API 会以 HTTP 201 返回错误正文，
  只看状态码就会误判为成功。

因此两个问题行的实际 wire type 都是 `Number`，2D 的 `Boolean` 及
3D 的 `Array` 写法属于错误。

## B-1 结论

正常的 `INHERENT_TORSION = true` 在 GET 中也存为 `true`。相比之下
`IINHERENT_TORSION` 与 `NHERENT_TORSION` 虽返回 HTTP 201，但拼错的键
从响应中消失，GET 中的正常字段仍是默认值 `false`。两种拼写错误服务器都
静默忽略，因此复制示例的用户可能误以为选项已经生效。

## B-2 结论

### `/db/MATD`

在 Gen 中，分别只加 `bSERVCHECK`、`dSHORTTERM`、`dLONGTERM` 之一的
PUT，以及把三个字段一起发送的 PUT，其结果都在 GET 中保留。因此三个字段在
Gen 中确实起作用，可作为补上 Specifications 表缺项的依据。

在 Civil 中，同样的 PUT 返回 HTTP 200、即时响应里也出现了输入值，
但后续 GET 中三个字段全部不存在。基准 PUT 的其他材料值正常保存，
所以并非整个请求失败。在当前 Build 中，这三个字段看似 Gen 专用行为：
可以传送给 Civil，但不会持续保存。

### `/db/SPLC`

在官方默认反应谱示例后面附加了 Gen NX 专用的偶然偏心块。先
创建了实际的 Story 与 Response Spectrum Function。包含 `ALONG = 2.5` 的
POST 原样存入后续 GET。向同一条记录发送 `ALONG = 3.5` 的
PUT，响应返回了 3.5，但后续 GET 中留下的仍是原来的 2.5。

因此 `ALONG` 在 Gen 的创建路径中是实际存在的 wire field，但当前 Build 的
更新路径会静默忽略变更。只看 PUT 响应就可能误判为已经反映，所以除文档错误上报
之外，还需要确认产品行为。
