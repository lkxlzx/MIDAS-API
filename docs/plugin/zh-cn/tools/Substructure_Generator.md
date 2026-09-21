# Substructure Generator

> **原文：** [Substructure Generator](https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator)
> **原文编写：** 2026-07-22 · **原文最后编辑：** 2026-07-27

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Substructure_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 旨在 Civil NX 中顺畅生成下部结构（Substructure）模型并编制详细报告，同时实现几何生成与文档编制的自动化，为工程师提供高效的工作流。

## 支持版本

`MIDAS CIVIL NX 2025 (v2.2)`

## 主要功能

- **完整的模型生成：** 自动生成连边界条件都已定义完备、可直接分析的 3D 下部结构模型。
- **自动文档：** 生成可下载的 `.xlsx` Excel 报告，内含全部输入汇总、计算得到的荷载，以及在 Midas Civil NX 中动态截取的截图（BMD 图、位移云图、截面视图等）。
- **荷载与反应谱一体化：** 将静力、移动、风、地震荷载准确施加为节点荷载，并生成反应谱函数。
- **多样的基础选项：** 同时支持明挖基础（Open Foundation）与桩基础（Pile Foundation）输入。

## 使用方法（9 个选项卡）

| 选项卡 | 说明 |
| --- | --- |
| Initial Data | 起点坐标以及盖梁（Pier Cap）、桥墩（Pier）、基础（Footing）的材料属性设置 |
| Superstructure | 收集主要用于生成 Excel 报告与自动计算风荷载的尺寸，如有效跨径等 |
| Pier & Pier Cap | 定义几何尺寸、形状（圆形/矩形）、单元网格长度 |
| Foundation | 明挖基础或桩基础输入（尺寸、深度、网格大小、SBC 与地基系数等地基属性） |
| Bearing | 设置支座布置（两侧/中央）、距离、垫石高度、弹性连接刚度值 |
| Loading | 输入以节点荷载施加于支座位置的静力荷载（自重、SIDL） |
| Moving Load | 输入以节点荷载施加的移动荷载最大反力（竖向、纵向、横向） |
| Dynamic Load | 定义风荷载参数与地震荷载数据（按 IS 1893 的反应谱） |
| Create Model | 最终执行选项卡 — 生成 Midas Civil NX 模型并下载 Excel 报告 |

**保存/复用输入值：** 在任一选项卡都可用 **Download (.json)** 按钮将当前输入保存为 JSON 文件。该 JSON 包含所有选项卡的数据，因此在任一选项卡下载/上传都会保存、恢复全部输入。若要再次使用已保存的 JSON，先通过 **Upload** 上传，然后点击 **Apply**，所有已保存的值即自动恢复。

## 参考/限制事项

在输入数据前，需进行以下设置，以使图像在报告中正确显示。

1. 在 Civil NX 中进入 **Display Option**（Alt + E）
2. 在 **Draw** 选项卡中打开 **"Hidden Option (Model)"**
3. 在 Thickness Option 中启用 **"Plane Thickness"**

## 相关 JSON API 端点

Plug-in 声明生成的反应谱函数与 `docs/manual` 的以下端点对应。静力/移动/风/地震荷载具体通过哪个 `/db/*` 端点写入，原文未说明，因此未加链接。

- [`/db/SPFC` — Response Spectrum Functions](../../../manual/zh-cn/09_DB_Dynamic_Loads.md) *（仅反应谱函数）*

## 结论（原文）

借助 Sub Structure Generator 可快速构建详细的 3D 下部结构模型，同时生成综合的工程报告。本 Plug-in 大幅减少了手工建模与文档编制的时间。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator](https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator)
