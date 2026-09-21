# [MS 1553:2002] Building Wind Loads Generator

> **原文：** [\[MS 1553:2002\] Building Wind Loads Generator](https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator)
> **原文撰写：** 2025-05-20 · **原文最后编辑：** 2025-08-05

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/MS_15532002_Building_Wind_Loads_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

针对马来西亚建筑结构，按**MS 1553:2002**标准自动化静力风荷载计算的Plug-in。
输入风荷载设计参数后，可立即按高度可视化风压与风力分布，简化风荷载评估过程。

## 支持版本

- `MIDAS GEN NX 2024 (v1.1) US`
- 适用标准：MS 1553:2002 (Code of Practice on Wind Loading for Building Structures)

## 主要功能

- **标准符合性：** 完全遵循MS 1553:2002，为位于马来西亚的结构物提供一致且可靠的
  风荷载计算。
- **可视化校核：** 以自动生成的柱状图显示各方向的层力（Story Force）·层剪力
  （Story Shear）·倾覆力矩（Overturning Moment）来确认结果。
- **交互式工作流：** 调整设计参数时图形与计算立即刷新，尽量减少人工重算并加快设计迭代。
- **计算书导出与联动：** 既可直接将荷载施加到结构模型，也可将结果导出为Excel，
  用于文档化及与其他工具联动。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 左侧：输入风荷载设计参数 | 输入结构模型的风荷载设计参数 |
| 右侧：结果可视化 | 以X·Y两个方向的图形与表格即时显示Story Force·Story Shear·Overturning Moment |
| X-Dir / Y-Dir标签 | 在各标签中输入作用于全局坐标系X方向与Y方向的风荷载参数 |
| Apply（主对话框右侧） | 选择按方向施加风荷载的静力荷载工况（Static Load Case） |
| Apply（最终） | 将计算得到的荷载施加到结构模型 |

## 风荷载设计参数（对应原文条款）

| 符号 | 名称 | 依据条款 | 备注 |
| --- | --- | --- | --- |
| V_s | Basic Wind Speed | Figure 3.1 / Fundamental Basic Wind Velocity Map | 以50年重现期为基准，Zone I 33.5 m/s、Zone II 32.5 m/s为推荐值 |
| M_d | Climate change multiplier | — | 取值为1.0 |
| M_z,cat | Terrain/Height Multiplier | Section 4.2, Clause 4.2.3 | 反映地形粗糙度与高度，上游地形不止一种时允许取平均 |
| M_s | Shielding Multiplier | Section 4.3, Table 4.3 | 忽略Shielding效应、不对特定方向施加，或平均仰坡超过0.2时取1.0 |
| M_h | Hill Shape Multiplier | Section 4.4, Figures 4.3–4.4 | 除特定场地地形区（local topographic zone）的特定方位外取1.0 |
| V_des | Building design wind speed | Table 3.2 | 最大site wind speed（V_sit）乘以重要性系数（I） |
| C_fig | Aerodynamic shape factor | Section 5.2(a) | — |
| C_pe | External pressure coefficient | Table 5.2(a)（迎风壁）/5.2(b)（背风壁） | 随h/d比确定 |
| K_a | Area reduction factor | Clause 5.4.2, Table 5.4 | 适用于封闭式建筑的屋面与墙，其他情况默认1.0 |
| K_c | Combination factor（外压） | Clause 5.4.3 | 多个面上的压力共同作用时，可采用小于1.0的系数 |
| K_l | Local pressure factor（覆层） | Clause 5.4.4 | 默认1.0，应用局部覆层压力时除外 |
| K_p | Porous cladding reduction factor | Clause 5.4.5, Table 5.8 | 通常为1.0，采用透气的覆层时参见Table 5.8 |
| C_dyn | Dynamic response factor | Section 6 | 一阶固有频率 > 1Hz时为1.0。0.2~1.0Hz时应用Clause 6.2（along-wind）/6.3（cross-wind） |
| 建筑平面尺寸（b × d） | — | — | 用于计算形状系数与风荷载暴露面积 |
| Importance Factor / Wind Direction | — | Table 3.2 | 按结构物分类在0.87、1.0、1.15、1.15之中选择。主风向决定轴向与荷载分配 |

建筑设计风压（Pa）按`p = 0.5·p_air × V_des² × C_fig × C_dyn`形式的公式计算（参见
原文公式图片，p_air = 空气密度1.225 kg/m³，`0.5·p_air` = 0.613）。

> ⚠️ 原文的参数编号③与④均重复记载为"M_z,cat: Terrain/Height Multiplier" —
> 这看起来是原文自身的编号错误，本文档仅整理为一个条目。

## 参考/限制事项

- 本Plug-in**不支持柔性高层建筑（flexible tall building）。** 属于该情形时，需由用户
  用Equation (10)或(19)自行计算C_dyn。

## 相关JSON API Endpoint

Plug-in说明将计算结果"直接施加到结构模型"的部分，就其性质而言很可能与`docs/manual`的
静力风荷载Endpoint联动。但相应Endpoint文档是按KDS 41-12:2022 / User Type基准撰写的，
与MS 1553:2002代码的确切字段对应关系未能确认 — 仅作为参考列出链接。

- [`/db/SWIND` — Static Wind Load](../../../manual/zh-cn/06_DB_Static_Loads.md) *（各代码间字段对应未确认）*

## 结论（原文）

本Plug-in为基于MS 1553:2002的静力风荷载生成提供了快速、直观的方案。通过对基本风速、
地形类别、shielding、建筑高度等核心风荷载设计参数的引导，提高了风荷载确定的清晰度与
一致性。借助实时可视化与导出功能，工程师可快速评估场地与建筑特性对风荷载的影响。
简化的工作流最大限度减少人工输入，促成标准化且可复现的风荷载设计结果。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator](https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator)
