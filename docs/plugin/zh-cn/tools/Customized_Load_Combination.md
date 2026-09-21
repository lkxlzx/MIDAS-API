# Customized Load Combination

> **原文：** [Customized Load Combination](https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination)
> **原文撰写：** 2024-12-23 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Customized_Load_Combination.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 简化了在 midas Civil NX 中生成与管理结构设计用荷载组合的过程。
它提供了定义特定设计场景所需荷载工况、系数与设置的选项，因此与标准设计代码及自定义
设计代码均可兼容。

## 支持版本

`MIDAS CIVIL NX 2025 (v1.1) US`

## 主要功能

产品经常收到的咨询：

- 缺少针对特定国家或某修订版/旧版代码的荷载组合。
- 需要为反映地方自治团体要求、严格的审查流程以及设计者意图而增加的特殊荷载组合。

定义数量众多的荷载组合是一件繁琐的工作，因此本 Plug-in 提供以下功能。

- 以最少的输入生成荷载组合。
- 提供从 Excel 文件引入输入数据的选项。
- 将生成的荷载组合导出为 wizard 文件以便复用 — 可自行构建荷载组合生成输入值
  库，大幅节省时间。
- 自动生成所生成组合的包络（envelope）。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 运行 "Customized Load Combination Auto-Generator" Plug-in |
| 2 | 在荷载组合列表中新增输入项 — A：荷载组合名称，B：Active 状态（见下表），C：Type（见下表） |
| 3 | 添加荷载工况与荷载系数 — A：Load Case 名称（Civil 中已生成的项以下拉框形式导入，Plug-in 中定义的组合也包含在内，例：Static、RS、MVL、TH、Settlement 等），B：Sign（见下表），C：Factor（最多 5 个，由用户直接输入，导入的荷载工况至少需要 1 个 factor，同一荷载组合内序号相同的 factor 同时使用） |
| 4 | 附加输入 — A：Generate Envelope Load Combinations（为生成的组合生成包络），B：Generate Inactive Load Combinations（生成标记为 "Inactive" 的荷载组合），C：Generate Load Combinations In（选择要在其中生成荷载组合的选项卡：Steel Design / Concrete Design / SRC Design / Composite Steel Girder Design） |
| 5 | 点击 **Generate Load Combination** |
| 6 | 确认生成完成的提示 |
| 7 | 在 Results > Load Combination > Steel Design 等路径下查看结果 |
| 8 | Export Load Combination Input（导出 wizard 文件，便于为 TMH·AREMA 等特定代码生成模板，或在出现错误时重新生成）/ Import Load Combination Input（引入已生成的 wizard 文件） |

### B：Active 状态选项

| 选项 | 说明 |
| --- | --- |
| Inactive | 用户选择时可在 Civil 中生成 |
| Local | 仅在 Plug-in 内部显示 |
| Strength | 在 Civil 中生成，按承载能力极限状态（ULS）设计 |
| Service | 在 Civil 中生成，按正常使用极限状态（SLS）设计 |

### C：Type 选项

| 选项 | 说明 |
| --- | --- |
| Add | 将组合内所有工况相加 |
| Either | 仅考虑组合内的某一个工况 |
| Envelope | 生成组合内各工况的包络 |

### B（荷载系数 Sign）选项

| 选项 | 说明 |
| --- | --- |
| `+` | 仅正（positive）的系数值 |
| `-` | 仅负（negative）的系数值 |
| `±` | 正/负系数的排列（permutation） |
| `+, -` | 分别给出仅施加正号的情况与仅施加负号的情况 |

## 相关 JSON API 端点

"Generate Load Combinations In" 中所选择的 4 种选项卡与 `docs/manual` 的以下端点
相对应。

- [`/db/LCOM-STEEL` — Load Combinations (Steel Design)](../../../manual/zh-cn/13_DB_Load_Combinations.md)
- [`/db/LCOM-CONC` — Load Combinations (Concrete Design)](../../../manual/zh-cn/13_DB_Load_Combinations.md)
- [`/db/LCOM-SRC` — Load Combinations (SRC Design)](../../../manual/zh-cn/13_DB_Load_Combinations.md)
- [`/db/LCOM-STLCOMP` — Load Combinations (Composite Steel Girder Design)](../../../manual/zh-cn/13_DB_Load_Combinations.md)

## 结论（原文）

Customized Load Combination Auto-Generator Plug-in 大幅简化了荷载组合的定义
与管理过程，为用户节省时间与精力。通过自动化荷载组合的生成与导出来提升效率，并确保
符合各类设计标准。用户可为今后的项目快速生成、保存并复用荷载组合。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination](https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination)
