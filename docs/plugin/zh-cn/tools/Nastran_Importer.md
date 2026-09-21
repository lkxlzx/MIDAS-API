# Nastran Importer

> **原文：** [Nastran Importer](https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer)
> **原文撰写：** 2025-04-09 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Nastran_Importer.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

将**Nastran BDF（Bulk Data Format）**文件平滑导入MIDAS CIVIL NX的Plug-in。
面向处理基于网格模型的工程师设计，在自动化节点/单元数据转换的同时保持几何完整性，
保证仿真的准确性。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- **高效的工作流：** 无需人工数据转换，直接导入Nastran BDF文件。
- **数据完整性：** 导入过程中保留原始网格结构（节点/单元）。
- **节省时间：** 消除把Nastran模型迁移到Civil NX过程中的多余步骤。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 单击Import按钮访问本地文件夹 |
| 2 | 选择要转换的BDF文件 |
| 3 | 确认转换后的几何模型 |

## 参考/限制事项

- 支持的数据为**节点（nodes）**与**单元（elements）**，不支持的数据（例如求解器专用命令）
  将被忽略。
- 对于复杂模型，导入后必须校验网格连续性。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer](https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer)
