# [AS/NZS 1170.2:2021] Building Wind Loads Generator

> **原文：** [\[AS/NZS 1170.2:2021\] Building Wind Load Generator](https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator)
> **原文创建：** 2025-05-15 · **原文最后编辑：** 2026-02-24

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/AS_NZS_1170_22021_Building_Wind_Loads_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 依据 **AS/NZS 1170.2:2021** 标准，自动化封闭式（enclosed）建筑的静力风荷载计算。输入风荷载设计参数后，即时可视化沿高度的风压·风力分布，从而简化风荷载设计过程。

> ⚠️ AS/NZS 1170.2:2021 是澳大利亚·新西兰的共用标准，但本 Plug-in 目前**仅实现了澳大利亚（AS）
> 条款**（原文明确说明）。

## 支持版本

- `MIDAS GEN NX 2026 (v1.1) US`
- 适用标准：AS/NZS 1170.2:2021 (Structural design actions, Part 2: Wind actions)

## 主要功能

- **符合标准：** 遵循最新的 AS/NZS 1170.2:2021 标准（封闭式建筑），支持最新的荷载评估。
- **可视化校验：** 以折线图显示各方向的层力（Story Force）·层剪力（Story Shear）·倾覆力矩（Overturning Moment）分布，结果可即时查看与解读。
- **交互式工作流：** 修改参数时图形即时刷新，减少反复操作时间，提升建模效率。
- **计算书导出与联动：** 计算所得静力风荷载既可直接施加到结构模型，也可导出为 Excel 计算书用于文档存档与进一步利用。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 风荷载设计参数输入 | 默认可对 8 个方位（cardinal direction）分别输入。`Mz,cat`、`Ms`、`Mt` 可按方向逐一指定 |
| Wind Load Input Condition → Input Only Worst-Case Value | 若要对所有方向套用同一组风荷载参数则勾选此项。即向全部方向使用同一组起控制作用（governing）的取值 |
| Calculate Wind Load | 点击后执行计算。Story Force·Story Shear·Overturning Moment 以图形与表格即时可视化（可按 0°、90°、180°、270° 各方向分别查看） |
| Apply | 将计算所得荷载施加到结构模型。依结构朝向按 +X、+Y、-X、-Y 方向施加，并可用切换按钮限定为仅施加到正（+）方向（+X、+Y） |

## 风荷载设计参数（对应原文条款）

| 符号 | 名称 | 依据条款 | 备注 |
| --- | --- | --- | --- |
| V_R | Regional Wind Speed（区域风速，m/s） | Section 3 | 澳大利亚查 Table 3.1(A) 或 Fundamental Basic Wind Velocity Map |
| M_c | Climate change multiplier | Table 3.3 | 依地区通常取 1.0 或 1.05 |
| M_d | Wind Direction Multiplier | Section 3, Table 3.2(A) | 澳大利亚标准下取值 0.75~1.00，随方位而异 |
| M_z,cat | Terrain/Height Multiplier | Section 4.2 | 反映地形粗糙度·高度。Clause 4.2.3 允许在上游地形不止一种时取平均 |
| M_s | Shielding Multiplier | Section 4.3, Table 4.2 | 高度 ≤ 25m 用 Table 4.2。超过 25m 或不施加遮蔽效应时取 1.0 |
| M_t | Topographic Multiplier | Section 4.4 | Region A4（海拔 400m 及以上）用 Eq. 4.4(1)，Region A0 用 Eq. 4.4(2)，其余取 Clause 4.4.1(c)(i)/(ii) 中的较大值 |
| V_des,θ | Orthogonal design wind speed | Section 4 | 取正交方向 ±45° 范围内 site wind speed 经线性插值后的最大值 |
| C_shp | Aerodynamic shape factor | Equation 5.2(1) | 本 Plug-in 假定 K 系数（Ka, Kc,e, Kl, Kp）默认取 1.0，故计算中不显式予以考虑 |
| C_pe | External pressure coefficient | Table 5.2(A)（迎风壁）/5.2(B)（背风壁） | 按 h/d 比值确定 |
| K_a | Area reduction factor | Clause 5.4.2, Table 5.4 | 适用于封闭式建筑的屋面板·墙面板，其余情况默认取 1.0 |
| K_c,e | Action combination factor（外压） | Clause 5.4.3 | 一般取 1.0 |
| K_l | Local pressure factor（围护面板） | Clause 5.4.4 | 一般取 1.0（需施加局部围护面板压力的情形除外） |
| K_p | Porous cladding reduction factor | Clause 5.4.5 | 一般取 1.0，透风围护面板时查 Table 5.8 |
| C_dyn | Dynamic response factor | Section 6 | 一阶固有频率 > 1Hz 时取 1.0。0.2~1.0Hz 时套用 Clause 6.4（顺风向）/6.5（横风向） |
| 建筑平面尺寸（b × d） | — | — | 用于形状系数·风荷载受风面积的计算 |

设计风压（Pa）按 `p = p_air × V_des,θ² × C_shp × C_dyn` 形式的公式计算（参见原文公式图片，p_air = 空气密度 1.2 kg/m³）。

## 参考/限制事项

- 本 Plug-in **不支持柔性高层建筑（flexible tall building）。** 属于该类结构时，需由用户按 Equation 6.2(1) 或 6.3(2) 自行计算 C_dyn。
- 由于 K 系数默认假定为 1.0，若存在局部围护面板压力·透风围护面板等 K 系数不为 1.0 的工况，需另行校核结果。

## 相关 JSON API 端点

Plug-in 中关于“将计算结果直接施加到结构模型”的说明，按性质而言很可能与 `docs/manual` 的静力风荷载端点联动。但相应端点文档是按 KDS 41-12:2022 / User Type 描述的，因此与 AS/NZS 1170.2 规范的确切字段对应关系尚未确认 —— 仅作参考列出链接。

- [`/db/SWIND` — Static Wind Load](../../../manual/zh-cn/06_DB_Static_Loads.md) *(各规范间字段对应关系未确认)*

> ⚠️ 原文的“Conclusion”段落疑似原样照抄了“AS 1170.4:2024 地震作用 Plug-in”的说明而自相矛盾
> （措辞与另一 Plug-in 的文章完全相同），故本文未予搬运。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator)
