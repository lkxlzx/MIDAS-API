# Line to Plate Converter

> **原文：** [Line To Plate Converter](https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter)
> **原文撰写：** 2026-07-27 · **原文最后编辑：** 2026-07-29

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Line_to_Plate_Converter.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

在MIDAS CIVIL NX中把选中的梁单元转换为板单元，以获得更详细、更准确的分析。
可灵活控制网格密度、划分方式，以及转换后的板与其余框架模型之间的边界连接性。
按照原截面形状、材料与刚度特性生成Plate截面，从而保持原模型的结构意图。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.1)`

## 主要功能

- **提升分析精度：** 将1D梁单元转换为2D板单元，提供更详细、更准确的分析。
- **灵活的网格控制：** 纵向划分策略可在目标网格尺寸（m）或划分个数之间选择，
  并可用截面网格尺寸参数单独控制横向网格密度。
- **保持结构连接性：** 可选的Rigid Link功能在跨径两端自动生成刚性连接，维持转换后的
  板网格与其余框架模型之间的连接性与边界约束。
- **节省时间：** 自动化了生成板网格、指定厚度、与既有模型连接这些繁琐的手工操作。
  把原本需要数小时的人工建模缩减为几次点击。

## 使用方法

| 字段 | 说明 | 选项·默认值 |
| --- | --- | --- |
| 单元选择 | 在MIDAS CIVIL NX中选择要转换为Plate的梁单元 | — |
| Division Type开关 | OFF: Mesh division（个数） — 输入纵向划分个数，ON: Mesh size(m) — 输入纵向目标网格尺寸（m） | 个数范围2~500（默认5），尺寸范围0.1~10.0m（默认0.50m） |
| Section Mesh size (m) | 将截面划分为板条时所用的横向细分尺寸 | 范围0.1~10.0m，默认0.50m |
| Rigid Link复选框 | 启用时在跨径两端生成刚性连接，保持与原框架模型的连接性 | 默认启用 |
| Convert | 单击后开始转换。处理期间所有输入字段被禁用并显示进度Spinner | — |

## 参考/限制事项

- Plug-in会从模型中**删除**所选的1D单元。若存在关联的荷载·预应力束，将被一并删除，
  必要时需手工重新创建。
- 若所选单元不构成一条连续的链，则只处理从最小单元ID开始的连续区段。
- 对不支持的截面类型会显示"Unsupported Section"错误消息，并初始化界面以便重试。

### 支持的截面（Uniform·Tapered）

| 名称 | Shape Code |
| --- | --- |
| Angle | `L` |
| Channel | `C` |
| H/I-Section | `H` |
| T-Section | `T` |
| Box | `B` |
| Pipe | `P` |
| Solid Rectangle | `SB` |
| PSC 1-Cell | `1-CEL` |
| PSC 2-Cell | `2-CEL` |

## 相关JSON API Endpoint

本Plug-in所处理的单元·刚性连接，与`docs/manual`中的下列Endpoint对应。

- [`/db/ELEM` — Element](../../../manual/zh-cn/03_DB_Node_Element.md)
- [`/db/RIGD` — Rigid Link](../../../manual/zh-cn/05_DB_Boundary.md)

## 结论（原文）

Line to Plate Converter Plug-in帮助工程师轻松地把简单梁模型转换为板单元模型。
自动处理对齐、插值、网格划分、单元生成与刚性连接，减少建模工作量，
并为高级分析提供准确可靠的结果。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter](https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter)
