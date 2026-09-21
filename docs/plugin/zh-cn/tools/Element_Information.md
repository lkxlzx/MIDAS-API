# Element Information

> **原文：** [Element Information](https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information)
> **原文撰写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Element_Information.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 便于轻松地查看单元（Element）信息，用于快速确认与核查特定单元的详细信息。

- 快速查看单元信息
- 无需输出单元表格，即可在建模过程中提供所需的详细信息

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

以往以表格形式显示所选单元详细信息的做法，对应 Element Table 与 Element Detail Table。

- **Element Table：** 显示全部单元清单，并高亮显示所选单元。
- **Element Detail Table：** 表格中仅显示所选单元。

以往的方式在直观确认所选单元信息上较为繁琐。本 Plug-in 无需切换到 Element
Table 或 Element Detail Table，即可直接查看所选单元的信息。

- 快速查看单元信息，减少错误
- 无需在单元表格之间切换即可在建模过程中提供所需信息，改善工作流程

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在模型中选择单元 |
| 2 | 将光标置于 Plug-in 上以运行 |
| 3 | 可查看所选单元的类型、材料、截面、连接节点编号、长度、面积、体积、单位重量、总重量、Beam End Release 信息 |
| 4 | 启用 **Detail** 开关后，各项单元信息按行排列显示 |

## 显示项目（Element Information）

| 项目 | 说明 |
| --- | --- |
| Elem ID | 单元 ID |
| Node Con | 连接的节点 ID |
| Type | 单元类型 — `BEAM`（一般/变截面梁）、`TRUSS`（桁架）、`TENSTR`（只拉/Hook/拉索）、`COMPTR`（只压/Gap）、`PLATE`（板单元）、`WALL`（墙单元）、`PLSTRS`（平面应力）、`PLSTRN`（平面应变）、`AXISYM`（轴对称）、`SOLID`（实体单元） |
| Material | 分配给单元的材料名称 |
| Section | 分配给单元的截面名称 |
| L/A/V | 长度 / 面积（Plate 时） / 体积（Solid 时） |
| Weight (U) | 单位长度/面积/体积的重量（单位重量） |
| Weight (T) | 单元总重量 |
| BER (Beam End Release) | 显示 I/J 端释放信息。`-`（无释放信息）、`F`（固定，Fixed）、`P`（铰，Pinned） |

## 相关 JSON API 端点

Plug-in 所显示的单元信息与 `docs/manual` 的以下端点相对应。

- [`/db/ELEM` — Element](../../../manual/zh-cn/03_DB_Node_Element.md)

## 结论（原文）

通过本指南，可在结构建模项目中高效地管理单元信息，并借助 Element
Information Plug-in 快速访问所需的信息。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information](https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information)
