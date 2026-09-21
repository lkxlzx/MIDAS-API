# Node Controller

> **原文：** [Node Controller](https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller)
> **原文撰写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Node_Controller.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本Plug-in的目的在于简化**节点坐标修改**过程，选择节点时无需在Node Table与
Node Detail Table之间来回切换。

- 快速执行节点坐标修改作业
- 以表格形式显示修改后的节点坐标信息

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

以往创建或修改节点坐标时，主要使用两种方式。

- 使用Create Nodes或Translate Nodes功能
- 使用Node或Node Detail Table

本Plug-in以简单的操作取代对人工操作或Excel之类辅助程序的依赖。

- 自动化节点坐标修改作业，节省时间
- 减少作业过程中的错误，提高模型精度
- 无需在各节点表之间移动即可提供所需信息，改善工作流

## 使用方法

| 项目 | 说明 |
| --- | --- |
| 选择节点并运行 | 未作选择即运行Plug-in时，从选择节点开始。若已选中节点，则立即加载信息 |
| Create/Translate切换 | **Create**：为消除移动节点过程中需要新增节点时的不便而增加。**Translate**（默认值）：执行节点坐标移动 |
| 显示所选节点数量 | 在括号内显示已选节点的数量。框中显示所选节点编号，可通过改选其他节点进行变更 |
| 输入节点移动距离 | 用X、Y、Z坐标框旁的箭头输入移动距离值。单击箭头即按指定值移动（例：输入1后单击3次则移动3m） |
| 单位换算 | 遵循产品内所选的长度单位（m、mm、cm、in、ft等）。所选多个节点的X/Y/Z值相同时可以修改，不同时显示为"Var."并禁止修改 |
| Apply | 单击后执行处理并变更模型数据 |
| 以表格显示所选节点坐标 | 以表格形式显示所选节点的坐标。节点间坐标值不同时，可直接在表中修改 |

## 相关JSON API Endpoint

本Plug-in所处理的节点坐标，与`docs/manual`中的下列Endpoint对应。

- [`/db/NODE` — Node](../../../manual/zh-cn/03_DB_Node_Element.md)

## 结论（原文）

利用Node Controller Plug-in，可在结构建模项目中高效地管理节点坐标，并快速访问所需信息。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller](https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller)
