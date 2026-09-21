# [TAIWAN2014] Building Wind Loads Generator

> **原文：** [\[TAIWAN2014\] Building Wind Loads Generator](https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator)
> **原文编写：** 2025-11-27 · **原文最后编辑：** 2025-12-09

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/TAIWAN2014_Building_Wind_Loads_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

针对封闭式建筑，按 **台湾 TAIWAN(2014)** 标准自动化计算静力风荷载的 Plug-in。输入风荷载设计参数后，即可按高度即时可视化风压与风力分布，简化风荷载设计过程。

## 支持版本

- `MIDAS GEN NX 2026 (v1.1) US`
- 适用标准：TAIWAN 2014 — 第二章 建築物設計風力之計算（台湾内政部国土管理署）

## 主要功能

- **符合标准：** 按 TAIWAN 2014 标准（封闭式建筑）支持最新的荷载评估。
- **可视化校验：** 以柱状图显示各方向的设计风压、层力（Story Force）、层剪力（Story Shear）、倾覆力矩（Overturning Moment）分布，可即时查看并解读结果。
- **交互式工作流：** 修改参数时图表即时刷新，减少重复操作时间，提升建模效率。
- **计算书导出与联动：** 可将计算得到的静力风荷载直接施加到结构模型，或为文档化而导出 Excel 计算书。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 左侧：输入风荷载设计参数 | 输入结构模型的风荷载设计参数 |
| 右侧：结果可视化 | 将 Design Wind Pressure、Story Force、Story Shear、Overturning Moment 以 X、Y 两个方向的图表与表格即时显示 |
| Load Cases to Apply to Wind Loads 选项卡 | 按方向选择施加风荷载的静力荷载工况（Static Load Case）。X、Y 方向的荷载工况必须互不相同（防止覆盖） |
| Apply Wind Loads | 点击后将计算得到的荷载施加到结构模型 |

## 风荷载设计参数（对应原文条款）

| 编号 | 参数 | 依据条款 | 说明 |
| --- | --- | --- | --- |
| ① | Basic Wind Speed (V₁₀) | 2.4 基本設計風速 | 以目标场地 10m 高度为基准的 10 分钟平均风速（重现期通常为 50 年）。参考台湾风速地图或地方规定 |
| ② | Exposure Category | 2.3 風速之垂直分布, 表2.2 | Category A（市区，20m 以上建筑占 50% 以上）：α=0.32, Zg=500m, Zmin=18m · Category B（郊外/小城市）：α=0.25, Zg=400m, Zmin=9m · Category C（开阔地/海岸）：α=0.15, Zg=300m, Zmin=4.5m |
| ③ | Importance Factor (I) | 2.5 用途係數 | 按建筑物用途、功能的重要性系数 |
| ④ | Mean Roof Height (hn) | — | 从结构模型的楼层数据自动提取的、超出地面的平均屋顶高度（模型内最大标高）。用于计算 K(z)、阵风影响系数、地形系数 |
| ⑤ | Topographic Factor (Kzt) | 表2.3(a)(b)(c) | 在 "Topographic Settings" 中选择性输入（可选）。反映丘陵/山脊/悬崖引起的风速增大效应。按方向指定 Hill Shape（Ridge/Escarpment/Hill）、Hill Height（H）、Hill Length（Lh）、脊线-建筑距离（x，迎风侧为正/背风侧为负）→ 计算 K1(H/Lh, 表2.3(a))、K2(x/Lh, 表2.3(b))、K3(z/Lh, 表2.3(c))。不考虑地形效应时所有楼层 Kzt=1.0 |
| ⑥ | Structure Type | — | Rigid Structure（自振频率 > 1Hz，低层/多层建筑，阵风影响系数计算简单）或 Flexible Structure（自振频率 ≤ 1Hz，高层/细长建筑，需输入自振频率与阻尼比，考虑更详细的动力响应） |
| ⑦ | Gust Effect Factor (G 或 Gf) | 2.7 陣風反應因子 | 通过 "Gust Effect Factor Calculator" 计算 X、Y 方向。Rigid Structure 输入建筑宽度（B）、长度（L）→ 自动计算湍流强度（Iz）、积分长度尺度（Lz）、背景响应系数（Q）。Flexible Structure 需额外输入 X、Y 方向的自振频率与阻尼比（计入共振响应效应） |
| ⑧ | Building Width and Depth (b × d) | — | 计算形状系数与风荷载有效面积所需的建筑平面尺寸 |
| ⑨ | Load Cases to Apply to Wind Loads | — | 分别指定施加 X、Y 方向风荷载的静力荷载工况（须互不相同） |

## 设计风压计算

- **基本风压 q(z)：** 形如 `q(z) = (单位换算常数) × I × V₁₀² × K(z) × Kzt`（参考原文公式图片，单位 kgf/m² 自动换算为用户单位制）。
- **速度压暴露系数 K(z)：** 以各暴露类别的 Zg（梯度风高度）、α（指数）为基准的高度函数（参考原文公式图片）。⚠️ 当 z ≤ 5m 时，计算中按 z = 5m 处理（原文明确说明）。
- **设计风压：**
  - 迎风面：`p1(z) = q(z) × G(或 Gf) × Cpe,windward − q(h) × GCpi`
  - 背风面：`p2(z) = q(h) × G(或 Gf) × Cpe,leeward − q(h) × GCpi`
  - 沿风向作用的设计风压：`p1(z) − p2(z)`
  - `Cpe,windward = 0.8`（固定值），`Cpe,leeward` 随 L/B 比变化（表2.4 线性插值），内压系数 `GCpi = 0.375`（按封闭式建筑）
- **层风力：** `Story Force = 设计风压 × 楼层暴露高度 × 建筑宽度(LOADED_BX 或 LOADED_BY)`
- **层剪力、倾覆力矩：** 层剪力为该层以上各层层力的累加和，倾覆力矩为层剪力与层高的累加力矩。

### 计算流程小结（原文）

1. 输入参数（基本风速、暴露类别、重要性系数、结构形式）
2. 计算各楼层 K(z)（以标高与暴露类别为基准）
3. 考虑地形效应时计算 Kzt
4. 按建筑尺寸与动力特性计算阵风影响系数（G 或 Gf）
5. 应用迎风面、背风面 Cpe 值
6. 计算各楼层基本风压
7. 应用阵风效应与压力系数得出设计风压
8. 考虑楼层形状计算水平力
9. 累加各力得出层剪力、倾覆力矩
10. 以图表、表格可视化结果
11. 将荷载施加到结构模型，或导出为 Excel 计算书

## 相关 JSON API 端点

原文描述将计算结果 "直接施加到结构模型" 的部分，性质上可能与 `docs/manual` 的静力风荷载端点联动。但相应端点文档按 KDS 41-12:2022 / User Type 编写，与 TAIWAN 2014 代码的准确字段对应关系尚未确认 — 仅作参考链接。

- [`/db/SWIND` — Static Wind Load](../../../manual/zh-cn/06_DB_Static_Loads.md) *（各代码字段对应关系未确认）*

## 结论（原文）

本 Plug-in 提供了按台湾 TAIWAN 2014 建筑法规生成静力风荷载的完善且易用的环境。通过标准化的参数输入与动态可视化反馈，保证了风荷载设计过程的透明度。工程师可更好地理解风速、地形暴露、地形效应、阵风响应等关键输入对各层风压、风力分布的影响，从而同时提升设计质量与决策效率。它同时支持 Rigid 与 Flexible 结构，并将地形效应作为可选功能，是可广泛用于台湾各类建筑类型与场地条件的工具。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator)
