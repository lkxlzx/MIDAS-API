# VibrationAnalysisAssistant 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/03_VibrationAnalysisAssistant.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据对视频(`docs/plugin_cases/videos/03_VibrationAnalysisAssistant.mp4`, 30fps, 3840×2160, 约 285秒)按
> 10秒间隔抓取帧（共 29张）后的逐帧目视分析 + 视频内字幕（旁白字幕）撰写。已与原文
> 文章(`docs/plugin_cases/articles/03_VibrationAnalysisAssistant.md`)的四大功能说明交叉确认。

## 1. 概述

**Vibration Analysis Assistant** 是在 MIDAS GEN NX 分析模型中，针对楼板·梁构件的步行荷载振动复核
所需的 Time History Function（时程函数）、Time History Load Case（时程荷载工况）、Dynamic Nodal
Load（动力节点荷载）3 种输入，在单一画面上完成输入·复核·应用的 Plug-in。以图形和表格实时确认荷载
特性后，通过 GEN NX API 反映到模型。

## 2. 问题定义

- 在 GEN NX 默认 UI 中，Time History Function（荷载函数）、Time History Load Case（分析工况）、
  Time History Analysis Data（动力节点荷载）的输入被拆分到各自独立的窗口
  (`Add/Modify/Show Time History Functions`, `Add/Modify Time History Load Cases`,
  `Time History Analysis Data`)，用户需在多个窗口间往返，输入并对照相关变量。
- 即使修改了输入值，也没有途径立即查看其结果（荷载时间函数的形态、峰值等），因此存在错误的
  `Time Step` 或 `Repeat` 值直到实际反映进模型前都不被发现的风险。
- 在多个窗口间往返的过程中，Node 编号、荷载方向、时间间隔等容易出现输入错误。

## 3. 目标用户

- 对楼板/梁构件执行步行荷载（适用性）振动复核的结构工程师。
- 需要把 IABSE（国际桥梁结构工程协会）标准的 Heel Drop-Walking Continuous 步行荷载函数反复以
  各种条件（步行频率、阻尼比、荷载节点等）加以应用的实务人员。

## 4. 核心概念 / 差异化点

- **单一画面集中输入**：将 Time History Function / Damping(Modal) / Dynamic Nodal Loads /
  Time History Load Case 4 个输入分组布置在同一画面，并在其下方附上实时预览图形与表格，使用户
  无需切换上下文即可完成作业。
- **实时荷载函数预览（Walking Load Preview）**：修改 `G`、`Walking Frequency fs`、`Time Step`、
  `Repeat` 等输入值的瞬间，右侧 `Time Function Graph` 与 `Time Function Table` 即同步刷新，可立即
  确认峰值荷载·持续时间(Duration)·重复次数(Steps)。在反映到模型之前提前发现错误是其核心价值。
- **荷载类型固定**：本 Plug-in 将支持范围固定为仅支持 IABSE 步行荷载函数中的
  **Heel Drop-Walking Continuous(IABSE)** 一种，从而把输入项精简为步行荷载复核所需的最小集合。
- **应用后重新查询校验**：通过 API 反映到 GEN NX 后立即重新查询、确认是否正常反映到实际模型的
  步骤，已包含在工作流之中。

## 5. 工作流

### Step 1 — 连接 API

- 点击左上角"API 设置"按钮 → 弹出输入 Base URL 与 MAPI-Key 的模态窗。
- 右上角状态徽章 4 种状态：`GEN NX Disconnected`（未连接，红色）/ `Connection failed`（连接
  失败，需检查 MAPI-Key）/ `Checking...`（连接中）/ `GEN NX Connected`（连接完成，绿色）。

### Step 2 — 填写 4 个输入分组

画面由左侧起 4 个面板构成：

| 面板 | 字段 | 说明 |
| --- | --- | --- |
| **Time History Function** | Function Name | 时程函数名称 |
| | Scale Factor | 应用于所生成荷载时间函数的倍数 |
| | G (kN) | 计算步行荷载时使用的基准荷载 |
| | Walking Frequency fs (Hz) | 步行频率 |
| | Time Step (sec) | 荷载时间函数的生成间隔 |
| | Repeat | 步行荷载重复次数 |
| **Time History Load Case** | Name | Load Case 名称 |
| | Description | 分析工况说明 |
| | Analysis Type | Linear / Nonlinear |
| | Analysis Method | Modal / Direct Integration |
| | Time History Type | Transient / Periodic |
| | End Time (sec) | 分析结束时间 |
| | Time Increment (sec) | 分析时间间隔 |
| | Step Number Increment for Output | 输出步数倍数 |
| **Damping - Modal** | Damping Ratio | 应用于全部振型的阻尼比 |
| | Table – Mode / Damping Ratio (+/− 按钮) | 增删各振型的阻尼比 |
| **Dynamic Nodal Loads** | Node No. | 施加动力节点荷载的 Node 编号 |
| | THLC Name | 选择施加荷载的 Time History Load Case |
| | Option | ADD / Replace / Delete |
| | Function Name | 选择要应用的 Time History Function |
| | Direction | X / Y / Z |
| | Arrival Time | 动力荷载起始的时间 |
| | Scale Factor | 应用于节点荷载的倍数（输入负数时荷载方向反转） |

### Step 3 — 确认实时预览

- 右下侧的 **Walking Load Preview** 中，`Time Function Graph`（折线）与 `Time Function Table`
  (Time/Load 值列表)始终同步显示。
- 上方显示 `Peak`（最大荷载）、`Duration`（持续时间）、`Steps`（步数）3 个汇总值。
- 视频演示：把 `Repeat` 由 1 改为 10，图形立即由单一波形变为重复 10 次的波形，Duration 由
  0.5秒 → 5.0秒，Steps 由 1.0 → 10.0 同步刷新。此外还将 `Time Step` 由 0.0050 → 0.0010秒、
  `End Time` 由 8秒 → 20秒等，实时调整多个参数加以确认。
- 将 `Scale Factor`（Dynamic Nodal Loads 一侧）由 1.000 改为 −1.000 时，Peak 值的符号由
  +0.908 kN → −0.908 kN 反转，同样实时反映 — 可用于校验荷载施加方向。

### Step 4 — 应用至 GEN NX 并校验

- 复核全部输入后点击"应用于 GEN NX"按钮。
- 底部日志显示应用结果摘要："应用完成 (ADD)：THFC #1, THIS #1, THNL 1 个 node 已反映" — 该日志
  文案原样暴露了实际调用的 API 端点名（THFC/THIS/THNL）。
- 随后切换到实际 GEN NX 程序画面（Tree Menu）重新查询反映结果：确认
  `Time History Analysis > Time History Load Cases`(Case 1: Walking_TH_01)、
  `Time Forcing Functions`(Function 1: Walk-cont(IABSE))、
  `Dynamic Nodal Loads`(Type 1: LoadCase=Walking_TH_01, Function=Walk-cont(IABSE))均已在树中
  生成 — 伴随"确认其是否正常反映"的旁白，重新查询校验步骤被明确纳入工作流。

## 6. 关联 JSON API 端点

片头幻灯片中明确标注为 "GEN NX API: THFC · THIS · THNL"，应用完成日志中也原样显示了同样的 3 个
代码 — 因此这 3 项并非推测，而是在画面上直接确认到的依据。

| 输入分组 | 端点 | 文档位置 |
| --- | --- | --- |
| Time History Function | `/db/THFC` | [`09_DB_Dynamic_Loads.md#8-dbthfc--time-history-functions`](../../manual/zh-cn/09_DB_Dynamic_Loads.md#8-dbthfc--time-history-functions) |
| Time History Load Case | `/db/THIS` | [`09_DB_Dynamic_Loads.md#6-dbthis--time-history-load-cases`](../../manual/zh-cn/09_DB_Dynamic_Loads.md#6-dbthis--time-history-load-cases) |
| Dynamic Nodal Loads | `/db/THNL` | [`09_DB_Dynamic_Loads.md#10-dbthnl--dynamic-nodal-loads`](../../manual/zh-cn/09_DB_Dynamic_Loads.md#10-dbthnl--dynamic-nodal-loads) |

- ⚠️ 3 个端点均支持 GET/POST/PUT/PUT-with-id/DELETE/DELETE-with-id，Plug-in 的
  `Option`(ADD/Replace/Delete) 字段推测对应这些 CRUD 动作（主要为 POST=ADD、PUT=Replace、
  DELETE=Delete），但画面上未显示实际的 HTTP 方法，因此准确映射仍属推测。
- Modal Damping（阻尼比）的输入究竟是写入 `/db/THIS` 请求体内的阻尼相关字段，还是存在独立端点，
  画面上未获确认。

## 7. 输入数据规格

- **荷载函数类型**：固定为 Heel Drop-Walking Continuous(IABSE) — 本 Plug-in 不支持其他 IABSE
  步行荷载类型（例：Heel Drop 单独）。
- **应用对象**：实际 GEN NX 模型中存在的 Node 编号（Dynamic Nodal Loads 的 Node No.）。
- **必填数值输入**：G(kN)、Walking Frequency(Hz)、Time Step(sec)、Repeat、End Time(sec)、
  Time Increment(sec)、Damping Ratio、Arrival Time(sec)、Scale Factor。

## 8. 输出 / 生成结果

- 在 GEN NX 模型中生成 `/db/THFC`（时程函数）、`/db/THIS`（时程荷载工况）、`/db/THNL`（动力
  节点荷载）数据。
- 画面上以图形·表格形式呈现的荷载函数预览（属于不存入模型的复核用产出物）。

## 9. 限制事项与局限

- 支持的荷载类型固定为 Heel Drop-Walking Continuous(IABSE) 一种，因此要应用其他步行荷载标准
  （例：特定国家标准的独立时间函数）便超出本 Plug-in 的范围。
- 阻尼方面画面上仅显示 Modal（按振型阻尼比）方式，Direct Integration 分析中常用的 Rayleigh 阻尼等
  其他阻尼定义方式未在视频中得到确认。
- 应用推测是以 ADD/Replace/Delete 选项为基准、按 1 个 Node·1 个 Function·1 个 Load Case 为单位
  进行，向多个 Node 批量应用同一条件的批处理功能未在视频中得到确认（⚠️ 未确认）。

## 10. 画面清单

| 时点(秒) | 画面内容 |
| --- | --- |
| 0–10 | 片头标题（标题/一句话介绍，GEN NX API: THFC·THIS·THNL） |
| 20–30 | 01·WHY — 既有 GEN NX 3 个输入窗口（Time History Function/Load Case/Analysis Data）彼此分离的问题 |
| 30–110 | 02·CHALLENGE — Plug-in 整体 UI 概要（左：4 个输入面板，右：Walking Load Preview） |
| 120–170 | 03·UI — API 设置（连接徽章 4 种状态）、THF·THLS 逐字段说明、Damping·Dynamic Nodal Loads 逐字段说明 |
| 180–230 | 实际程序演示：修改 Repeat/Time Step/End Time 值 → 图形·表格实时刷新，Scale Factor 负值反转 |
| 230–240 | 应用于 GEN NX → 日志（THFC #1, THIS #1, THNL 1 个已反映）→ 在 GEN NX 程序中通过 Tree Menu 重新查询校验 |
| 250–285 | 04·IMPACT — 应用预期效果（缩短输入时间·减少错误·提升复核便利性） |

---

*下一步：撰写 04_AutoGenerationCmFactor 的视频分析与规划文档。*
