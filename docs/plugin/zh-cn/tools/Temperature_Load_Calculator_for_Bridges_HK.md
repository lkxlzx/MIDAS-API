# Temperature Load Calculator for Bridges (HK)

> **原文：** [Temperature Load Calculator for bridges (HK)](https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK)
> **原文编写：** 2024-12-02 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Temperature_Load_Calculator_for_Bridges_HK.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

按 **STRUCTURES DESIGN MANUAL for Highways and Railways 2013 Edition(SDM 2013)** 3.5 节 Temperature Effects 计算桥梁结构物温度作用（thermal action）的 Plug-in。同时考虑上部结构内的均匀温度变化（uniform temperature change）与温度梯度（temperature gradient），据此确定最终的温度荷载。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- 快速、准确地分析桥梁结构物因温度变化产生的热影响。
- 按 SDM 2013 标准同时考虑均匀温度变化与温差，准确建立温度作用模型。
- 支持将温度作用快速反映到结构分析中。
- 可视化温度梯度、均匀温度变化对桥梁结构物的影响。
- 保证最终设计中准确反映全部温度贡献分量。

## 使用方法

### Uniform Temperature（均匀温度）

| 步骤 | 说明 |
| --- | --- |
| 1. 按结构类型输入参数 | Superstructure Type（参考 SDM2013 Figure 3.2 分类）、Structure Type（Normal/Minor，参考 Clause 3.5.2(3)）、Deck Surfacing Type（参考 SDM2013 Table 3.18 分类，选择 "Thickness" 时可定义铺装厚度）、Height above Sea Level（参考 Clause 3.5.2(5)） |
| 2. 选择 UNIFORM 选项卡 | 指定均匀温度 |
| 3. Adjustment to Temperature | 两种计算方法 — **Ceiling Method**（使用负的修正值，对计算影响较大）、**Linear Interpolation**（中间修正值的适用方式不同，最终结果与 Ceiling Method 有差异） |
| 4. 热作用参数·计算结果 | 显示均匀桥梁温度、修正值等已计算的热作用参数（供参考） |
| 5. 指定荷载工况 | 为对象单元指定用于均匀温度引起的膨胀、收缩的荷载工况 |
| 6. Apply Uniform Temperature Loads | 对所选单元执行施加均匀温度效应荷载 |

### Temperature Differences（温差）

| 步骤 | 说明 |
| --- | --- |
| 1. 按结构类型输入参数 | 见 Uniform Temperature 一节 |
| 2. 选择 DIFFERENCES 选项卡 | 指定温差 |
| 3. Adjustment to Temperature | 与 Uniform Temperature 一节方式相同 |
| 4. 热作用参数·计算结果 | 显示桥梁构件间温差、修正值等（供参考） |
| 5. 指定荷载工况 | 按计算得到的温差为对象单元指定加热（heating）、冷却（cooling）荷载工况 |
| 6. Apply Temperature Differences Loads | 对所选单元执行施加温差效应荷载 |

## 参考/限制事项

### 通用限制

1. 各荷载工况必须相同（identical load cases）。
2. 施加前，荷载工况必须已在 Load Case Menu 中预先定义。
3. 荷载以 MIDAS Civil 中指定初始温度的相对温度值施加。

### Uniform Bridge Temperature

1. 可应用于所有单元类型。
2. 所选荷载工况中不得指定 MIDAS Civil 的 Element Temperature Load。

### Temperature Differences

1. **仅适用于梁单元**。
2. 支持的截面类型/形状：
   - Type 1(USER)：`H`, `B`
   - Type 2(COMPOSITE)：`B`, `I`, `Tub`, `GB`, `GI`, `GT`
   - Type 3(PSC)：`1CELL`, `2CELL`, `3CELL`, `NCEL`, `NCE2`, `PSCM`, `PSCI`, `PSCH`, `PSCT`, `PSCB`, `VALUE`
3. 截面/桥面板高度值用于示例计算，荷载按所选实际单元截面重新计算并施加。
4. 各上部结构类型的最小适用截面高度：Type 1 — 600mm, Type 2 — 桥面板高度 + 400mm,Type 3 — 135mm 以上

## 相关 JSON API 端点

Plug-in 处理（或参考）的温度荷载与 `docs/manual` 的以下端点对应。

- [`/db/ETMP` — Element Temperature](../../../manual/zh-cn/07_DB_Temperature_Prestress.md) *（Uniform Bridge Temperature 限制条件中明确提及）*
- [`/db/BTMP` — Beam Section Temperature](../../../manual/zh-cn/07_DB_Temperature_Prestress.md) *（推测对应 Temperature Differences）*

## 结论（原文）

借助本 Plug-in 可高效分析作用于桥梁结构物的温度作用，并提供基于 SDM 2013 的准确数据，为有依据的设计过程提供支持。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK](https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK)
