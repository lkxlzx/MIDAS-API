# GEN NX to Staad Converter

> **原文：** [GEN NX to Staad Converter](https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter)
> **原文撰写：** 2026-04-07 · **原文最后编辑：** 2026-07-27

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/GEN_NX_to_Staad_Converter.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

将MIDAS GEN NX模型转换为STAAD.Pro的`.std`格式的Plug-in。转换过程在几何、材料属性、
荷载条件的全范围内保持数据完整性，从而大幅减少人工重新建模时间。

## 支持版本

`MIDAS GEN NX 2026 (v1.1) US`

## 主要功能

- **节省时间：** 无需在STAAD中手工重写模型，把原本需要数小时的重新建模工作
  缩短到几分钟。
- **透明的转换：** 内置日志明确列出哪些内容已完成转换、哪些条目（若有）不受支持，
  便于工程师快速核对转换内容。
- **易用性：** 界面简洁，选择待转换数据并生成`.STD`文件即可。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 用复选框选择要导出的数据：Geometry、Material Properties、Section Properties、Supports、Loads、Load Combinations |
| 2 | 单击**Generate .STD File**开始转换（以进度条显示处理状态） |
| 3 | 单击**Download .STD File**保存生成的`.std`文件 |
| 4 | 展开**Logs**区域，确认转换消息、映射说明以及不支持/被省略条目的警告 |
| 5 | 用**Reset**初始化当前运行并开始新的转换 |

日志面板详细记录从API连接与数据预取到最终文件生成的全部步骤，
并包含转换过程中发现的不支持功能的明确警告。

## 参考/限制事项 — MIDAS GEN NX → STAAD.Pro 转换映射

### 可转换的数据类别

`UNITS`、`MATERIAL PROPERTIES`、`SECTION PROPERTIES`、`BOUNDARY CONDITION`、
`MEMBER SPECIFICATION`、`RELEASE`、`LOAD`、`LOAD CASE & COMBINATION`（以及`GEOMETRY`）

### NODE（坐标系转换）

两者全局坐标系不同，按下表转换。

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| X | Z |
| Y | X |
| Z | Y |

### ELEMENT

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Beam | Member |
| Truss | Member Truss |
| Plate | Shell Element |
| Wall | Shell Element |

> ⚠️ 目前不支持只拉（Tension-only）·只压（Compression-only）构件。

### MATERIAL

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Isotropic | Isotropic (E, Poisson, Density, Alpha, Damping) |
| Orthotropic | 不支持 |
| SRC | 不支持 |

### SECTION

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| I (I Section) | ISECTION / TABLE ST |
| C (Channel) | GENERAL with Profile Points |
| L (Angle) | GENERAL with Profile Points |
| T (Tee) | TEE |
| B (Box) | TUBE |
| P (Pipe) | PIPE |
| 2L (Double Angle) | DOUBLE ANGLE |
| 2C, 2CB (Double Channel) | GENERAL with Profile Points |
| SB (Solid Rectangle) | PRIS YD ZD |
| SR (Solid Round) | PRIS YD |
| 其他 | 具有圆截面属性的GENERAL（0.1m × 0.1m占位Profile Points） |

> ⚠️ 目前不支持`VALUE`、`SRC`、`COMBINED`、`TAPERED`、`COMPOSITE`截面类型。

### BOUNDARY CONDITION

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Support (Fixed / Pinned / Partial) | FIXED / PINNED / FIXED BUT |
| Point Spring (Linear) | KFX, KFY, KFZ, KMX, KMY, KMZ |
| Rigid Link | SLAVE RIGID MASTER |

> ⚠️ 不支持非线性Point Spring与弹簧阻尼（damping）。

### RELEASE

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| 1D Member Release (Full DOF) | MEMBER RELEASE |
| 1D Member Release (Partial Moment) | MPX / MPY / MPZ |
| 1D Member Release (Spring) | Spring KFX–KMZ |
| 2D Plate Release (J1–J4) | PLATE RELEASE |

### LOAD

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Self Weight | SELFWEIGHT |
| Nodal Load (Force / Moment) | JOINT LOAD |
| Beam Concentrated Force | MEMBER LOAD CON |
| Beam Concentrated Moment | MEMBER LOAD CMON |
| Beam Uniform / Trapezoidal Force | MEMBER LOAD TRAP |
| Beam Uniform Moment | MEMBER LOAD UMON (discretized) |
| Pressure Load (Uniform) | ELEMENT LOAD PRESSURE |
| Pressure Load (Trapezoidal) | ELEMENT LOAD TRAP JT |

> ⚠️ 不支持梁单元荷载的偏心（eccentricity）。楼面荷载（FBLA）必须在运行Plug-in之前
> 先在MIDAS中转换为梁单元荷载。受STAAD自身限制，带投影（projection）的梯形压力荷载
> 不支持。

### LOAD CASE

MIDAS荷载工况代码（`D`、`L`、`W`、`E`、`T`、`S`等）映射为STAAD的`LOADTYPE`关键字（`Dead`、
`Live`、`Wind`、`Seismic-H`、`Temperature`、`Snow`等）。

### LOAD COMBINATION

| MIDAS GEN NX | STAAD.Pro |
| --- | --- |
| Algebraic | ADD |
| Absolute | ABS |
| SRSS | SRSS |

> ⚠️ 不支持Envelope组合（含嵌套的envelope）。

### 其他不支持的功能（需在STAAD.Pro中手动定义）

- Floor Diaphragms
- Beam end offsets
- Section Stiffness Scale Factors
- Load to Masses
- Static Seismic Loads
- Static Wind Loads

## 结论（原文）

GEN NX to STAAD Converter提供了将结构模型从MIDAS GEN NX快速、可靠地迁移到STAAD.Pro的
方法。通过自动传递几何、属性、边界条件、荷载与组合，帮助工程师把时间用于分析与设计，
而不是在不同平台之间重建模型。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter](https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter)
