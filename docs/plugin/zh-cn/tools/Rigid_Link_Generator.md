# Rigid Link Generator

> **原文：** [Rigid link generator](https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator)
> **原文编写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Rigid_Link_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

通过选择主节点（Master Node）与从节点（Slave Node）组，为每个主节点生成到距离最近的从节点的刚性连接（Rigid Link）的 Plug-in。创建非等间距的 Rigid Link 时也无需输入距离（Distance）值 — Rigid Link 会自动生成到主节点最近的从节点。适用于框架单元与板单元以刚性连接相连的上部结构（superstructure）建模。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

在 midas Civil 中创建 Rigid Link 时，必须先选择主节点，再选择与之连接的确切从节点。此外，创建非等间距的 Rigid Link 时，必须通过 'Copy Rigid Link' 功能输入准确的间距。本 Plug-in 只需选择主节点，无需逐个选择从节点，也无需输入非等间距的间距值，即可生成 Rigid Link。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 选择 Master Node | 选择将作为主节点的节点。在 midas Civil 中选择节点后，点击 Plug-in 的 'Select Master Nodes' 字段录入该节点（示例中选择对应主梁的节点） |
| 选择 Slave Node | 选择与主节点连接的从节点。无需选择确切的从节点（示例中选择整个桥面板单元） |
| Link Property | 选择 Rigid Link 的属性（与 midas Civil 相同） |
| Apply | 点击后，从主节点到从节点组中距离最近的节点生成 Rigid Link |

## 结论（原文）

在将主梁建模为梁单元、桥面板建模为板单元等上部结构建模场景中非常有用。Rigid Link 会生成到主节点最近的节点。

## 相关 JSON API 端点

Plug-in 生成的 Rigid Link 与 `docs/manual` 中的以下端点对应。

- [`/db/RIGD` — Rigid Link](../../../manual/zh-cn/05_DB_Boundary.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator](https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator)
