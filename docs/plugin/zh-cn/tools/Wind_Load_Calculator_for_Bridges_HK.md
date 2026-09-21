# Wind Load Calculator for Bridges (HK)

> **原文：** [Wind Load Calculator for bridges (HK)](https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK)
> **原文编写：** 2024-12-02 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Wind_Load_Calculator_for_Bridges_HK.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

按香港路政署（Highways Department）发布的 **STRUCTURES DESIGN MANUAL for Highways and Railways 2013 Edition(SDM 2013)** 3.4 节 Wind Actions，计算作用于桥梁结构物的风荷载的峰值速度压（Peak Velocity Pressure）的 Plug-in。支持计算桥梁风致力的两种方法，并提供设计用详细结果。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- 以均匀风压与风速剖面为基准，快速、准确地分析风作用对桥梁结构物的影响。
- 按 SDM 2013 指南提供准确的风致力。
- 风压计算同时支持 **Simplified Procedure** 与 **Full Procedure**。
- 风压数据与结构分析轻松联动。
- 清晰、详细地可视化风作用对桥梁结构物的影响。
- 按 SDM 2013 标准可处理多样的桥梁几何与地形。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 运行 Plug-in，在荷载组合列表中选择风荷载用的荷载工况名称 |
| 2 | 定义 **Velocity Pressure Case**。若无已定义的工况，可用右侧 `(...)` 按钮添加 Velocity Pressure Case |
| Velocity Pressure Cases Dialog | ① Add（新增工况）② Close（关闭）③ Modify（修改所选工况）④ Delete（删除所选工况） |
| 3 | 点击 Add 时，在 **Simplified Procedure**（Clause 3.4.2）与 **Full Procedure**（Clause 3.4.3）中选择其一并输入新数据。指定 Velocity Pressure Name |
| 4 | 查看所选的 Velocity Pressure Case（单位：kN/m²） |
| 5 | 指定 Force Coefficient。可用右侧 `(...)` 按钮启用按 BS EN 标准的自动计算 |
| 6 | 指定 Structural Factor(CsCd)。规范基准值为 1.0 |
| 7 | 选择对象单元 — 在模型中选择要施加荷载的梁单元后读入 Plug-in |
| 8 | 指定荷载施加方向 |
| 9 | 必要时输入 Restraint Height — 模型中未包含的栏杆（parapet）、防冲护栏（barrier）等的附加高度 |
| Apply | 完成设置后点击即输入荷载 |

## 参考/限制事项

### Procedure 选择依据

| 方法 | 依据条款 | 适用对象 |
| --- | --- | --- |
| Simplified Procedure | Clause 3.4.2 | 适用于以简单要求即能满足的绝大多数道路结构物 |
| Full Procedure | Clause 3.4.3 | 对风致破坏需要更高结构可靠性等级的结构物。**满足下列任一条件时为必填**：① 跨径超过 100m 的桥梁，② 位于战略道路（Strategic Routes）或由 Chief Highway Engineer/Bridges and Structures 指定的桥梁，③ 地面以上高度超过 40m 的桥梁 |

> ⚠️ Clause 3.4.4 定义的 **Dynamic Response Procedure** 不在本 Plug-in 的处理范围内
> （参考：UK NA to BS EN 1991-1-4 Clause NA.2.49）。

选择 Simplified Procedure 时，会按相关标准自动计算并提供峰值风压（Peak Wind Pressure）。

**用户输入·计算：** 用户输入规范表格中的变量并点击 Calculate 按钮后，即计算并施加速度压（Wind Velocity Pressure）。

**用于自动计算的表格：**
- Table 3.6: Wind Velocities
- Table 3.7: Peak Velocity Pressure
- Table 3.8: Exposure to Wind

为简化菜单选择，Simplified Procedure 包含 Section 3.4.1 General 中给出的 Table 3.6 Wind Velocity 值。**Full Procedure** 在计算峰值速度压或平均速度压时需要更详细的输入，且随所选选项卡不同，用于计算的参数也不同。各输入项的工具提示按 SDM2013 标准及各参数在风荷载效应计算中的作用提供。

## 相关 JSON API 端点

Plug-in 应用计算结果的对象，性质上可能与 `docs/manual` 的静力风荷载、静力荷载工况端点联动。但与 SDM 2013（香港）代码的准确字段对应关系尚未确认 — 仅作参考链接。

- [`/db/STLD` — Static Load Cases](../../../manual/zh-cn/06_DB_Static_Loads.md) *（荷载施加对象工况）*
- [`/db/SWIND` — Static Wind Load](../../../manual/zh-cn/06_DB_Static_Loads.md) *（各代码字段对应关系未确认）*

## 结论（原文）

借助本 Plug-in 可清晰理解风作用对桥梁结构物的影响，有助于工程师与设计者将 SDM 2013 指南高效应用于风荷载分析。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK](https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK)
