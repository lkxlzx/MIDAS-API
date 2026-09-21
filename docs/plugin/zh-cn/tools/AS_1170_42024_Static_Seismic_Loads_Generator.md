# [AS 1170.4:2024] Static Seismic Loads Generator

> **原文：** [\[AS 1170.4:2024\] Static Seismic Loads Generator](https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator)
> **原文创建：** 2025-05-13 · **原文最后编辑：** 2025-08-13

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/AS_1170_42024_Static_Seismic_Loads_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 依据 **AS 1170.4:2024** 标准，自动化等效静力地震作用的计算。输入抗震设计参数后，即时可视化 X、Y 两个方向的各层水平力分布，从而简化抗震设计工作流。

## 支持版本

- `MIDAS GEN NX 2024 (v1.1) US`
- 适用标准：AS 1170.4:2024 (Structural design actions, Part 4: Earthquake actions in
  Australia)

## 主要功能

- **符合标准：** 遵循最新的 AS 1170.4:2024 标准，支持最新的静力水平荷载计算。
- **可视化校验：** 以双向柱状图（dual bar graph）显示各方向的层力（Story Force）·层剪力（Story Shear）·倾覆力矩（Overturning Moment）分布，结果可即时查看与解读。
- **交互式工作流：** 修改参数时图形即时刷新，减少反复操作时间，提升建模效率。
- **计算书导出与联动：** 计算所得静力地震作用既可直接施加到结构模型，也可导出为 Excel 计算书用于文档存档。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 左侧：抗震设计参数输入 | 输入下表所列参数 |
| 右侧：结果可视化 | Story Force·Story Shear·Overturning Moment 以 X、Y 两个方向的图形与表格即时显示 |
| Load Cases to Apply to Seismic Loads 选项卡 | 选择各方向地震作用所要施加到的静力荷载工况（Static Load Case） |
| Apply Seismic Loads | 点击后将计算所得荷载施加到结构模型 |

## 抗震设计参数（对应原文条款）

| 序号 | 参数 | 依据条款 | 说明 |
| --- | --- | --- | --- |
| ① | Sub-Soil Class | Section 4.1.1 / 4.2 | 从 `Ae, Be, Ce, De, Ee` 中选择 |
| ② | Annual Probability of Exceedance | Table 3.1 | 按超越概率确定概率系数（kp） |
| ③ | Hazard Factor (Z) | Table 3.2, Figures 3.2(A)–3.2(G) | 澳大利亚各地区的 Z 值 |
| ④ | kp × Z | Table 3.3 | 自动计算 kp·Z 的乘积，并与 Table 3.3 的最小值比对校验 |
| ⑤ | Importance Level | NCC / AS/NZS 1170.0 Appendix F | 本 Plug-in 仅支持 Level `2, 3, 4`。不支持 Level 1（无需考虑地震作用）与住宅（domestic）结构 |
| ⑥ | Structure Height (hn) | — | 自基础至参与地震作用的最高质量处的总高度。建模上采用最大层高 |
| ⑦ | Earthquake Design Category (EDC) | Table 2.1 | 见下文“EDC 支持范围” |
| ⑧ | Sp, μ | Table 6.5 | 结构性能系数（Sp）·结构延性系数（μ），X、Y 方向可分别设置 |
| ⑨ | Fundamental Period (T₁) | Equation 6.2(7) | 各方向固有周期（秒）可直接输入，或用 **Period Calculator** 按规范近似式自动计算。X、Y 方向可分别设置 |

### EDC（Earthquake Design Category）支持范围

| EDC | 分析方法 | 依据条款 | 本 Plug-in 是否支持 |
| --- | --- | --- | --- |
| I | Simple Static Method | Clause 5.2, 5.3 | 支持 |
| II | Static Analysis | Clause 5.2, 5.4 | 支持 |
| III | 需要动力分析 | Clause 5.2, 5.5 | **不支持** — 需使用另外的 Plug-in “[AS 1170.4:2024] Response Spectrum Generator” |

### 底部剪力（Base Shear）计算公式

- **EDC I（Simple Static Method, Eq. 5.3, Clause 5.3）：** 采用第 i 层的地震重量 Wi 进行计算。
- **EDC II（Static Analysis, Eq. 6.2(3), Clause 6.2.1）：** 采用 `kp·Z`（概率系数×危险系数）、`Ch(T1)`
  （Clause 6.4 的弹性场地危险谱取值）、`Sp`（结构性能系数，Table 6.5）、`μ`（结构
  延性系数，Table 6.5）、`Wt`（全部楼层 Wi 之和）进行计算。

## 结论（原文）

本 Plug-in 提供了按 AS 1170.4:2024 标准生成静力地震作用的完备且易用的环境。通过规范化的参数输入与动态可视化反馈，保障了抗震设计过程的透明性。工程师可以更清楚地理解场地类别·结构高度·延性等关键输入对各层荷载分布的影响，从而同时提升设计质量与决策效率。从输入到可视化、导出的顺畅工作流大幅减轻了手工操作负担，促成了规范化且可复现的结果。

## 参考/限制事项

- **EDC III（需要动力分析）的结构不能由本 Plug-in 处理** — 必须使用另外的“[AS
  1170.4:2024] Response Spectrum Generator” Plug-in。
- 不支持 Importance Level 1 结构与住宅（domestic housing）结构。

## 相关 JSON API 端点

Plug-in 将计算结果施加到的“Static Load Cases”，与 `docs/manual` 中的以下端点对应。不过与 AS 1170.4 规范本身的确切字段对应关系（是否包含地震作用专用表格）尚未确认 —— 仅作参考列出链接。

- [`/db/STLD` — Static Load Cases](../../../manual/zh-cn/06_DB_Static_Loads.md) *(施加对象的荷载工况)*
- [`/db/SSEIS` — Static Seismic Load (KDS 41-17-00:2019 / User Type)](../../../manual/zh-cn/06_DB_Static_Loads.md) *(各规范间字段对应关系未确认)*

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator)
