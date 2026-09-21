# SPACE GASS Converter

> **原文：** [SPACE GASS Converter](https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter)
> **原文编写：** 2024-08-02 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/SPACE_GASS_Converter.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

将 SPACE GASS `.txt` 文件的模型数据高效导入 Civil NX 的 Plug-in。SPACE GASS 文件可直接导入（import）为 Civil NX 模型。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

利用 SPACE GASS 模型文件，将模型数据高效导入 Civil NX。在自动转换材料、截面相关数据，单元、节点等几何数据，以及边界条件、荷载数据的同时，保持原始数据的完整性，实现可靠且准确的模拟。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 点击 **Import** 按钮 |
| 2 | 导入 SPACE GASS `.txt` 文件（仅可导入文本（txt）格式的 SPACE GASS 文件） |
| 3 | 确认已导入的 SPACE GASS 文本文件 |
| 4 | 确认 SPACE GASS 建模信息（只读编辑器） |
| 5 | 点击 **Send** 按钮 |
| 6 | 生成 Civil 模型 |

## 参考/限制事项 — SPACE GASS → midas Civil 转换映射

### 可转换的数据类别

`MATERIAL`, `SECTION`, `NODE`, `ELEMENT`, `BOUNDARY CONDITION`, `LOAD`

### MATERIAL / SECTION

材料、截面信息与 User Defined 方式兼容。

### NODE（坐标系转换）

由于 SPACEGASS 与 midas Civil 的全局坐标系不同，按如下方式转换。

| | SPACE GASS | MIDAS CIVIL NX |
| --- | --- | --- |
| X-DIR | X | X |
| Y-DIR | Y | Z |
| Z-DIR | Z | -Y |

### ELEMENT

| SPACE GASS | MIDAS CIVIL NX |
| --- | --- |
| Normal | General Beam |
| Plate | Plate |
| Tension Only | Tension Only |
| Compression Only | Compression Only |

### BOUNDARY CONDITION

以下数据可转换：`SUPPORT`, `POINT SPRING`, `RIGID LINK / ELASTIC LINK`, `BEAM END RELEASE`

### LOADCASE

| SPACE GASS | MIDAS CIVIL NX |
| --- | --- |
| SELF LOAD | SELF WEIGHT |
| PRESCRIBED DISPLACEMENT | SPECIFIED DISPLACEMENT OF SUPPORT |
| MEMBER CONCENTRATED LOAD | NODAL LOAD |
| MEMBER DISTRIBUTED FORCE | UNIFORM LOAD |
| MEMBER DISTRIBUTED MOMENT | UNIFORM MOMENT |
| PLATE PRESSURE LOAD | PRESSURE LOAD |

## 结论（原文）

通过 SPACE GASS Converter 可将模型信息快速导入 MIDAS CIVIL NX。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter](https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter)
