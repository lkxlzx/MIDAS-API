# Floor Transition

> **原文：** [Floor Transition](https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition)
> **原文撰写：** 2024-07-30 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Floor_Transition.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 用于协助把已测定楼层（floor）的形状移动或转换到结构模型内的其他楼层。
在多层建筑中尤为有用。

- 提供在多层建筑中转换楼层的功能
- 以楼层信息或 Z 坐标为基准转换节点与单元的坐标

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

自动调整节点与单元坐标，消除了对手工作业以及 Excel 等辅助程序的依赖。
对于设有墙体箍带（wall belt）的结构物，在竖直移动模型的一部分时尤为有用。

- 自动化节点与单元坐标的调整，大幅节省时间。
- 减少手工作业过程中可能出现的错误，提高模型精度。
- 简化结构模型的修改，支撑高效的项目管理。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在属于 "From Floor" 的底部楼层中选择 1 个基准节点（Criteria Node） |
| 2 | 输入要被移动的楼层（"From Floor"） |
| 3 | 输入要转换到的目标楼层（"To Floor"） |
| 4 | 点击 **Apply** 按钮 |

**示例：** 在 11 层建筑中若要把 2 层的框架移到 5 层，选择属于 2 层的节点编号（例："172"），
在 "From Floor" 中输入 "2"、"To Floor" 中输入 "5"，随后点击 Apply，2 层的框架即移动到
5 层。

## 参考/限制事项

- **存在楼层信息时：** 当结构物的各楼层可由楼层信息（Story Data）明确识别时，以其数据为
  基准运行。例：11 层建筑把 2 层移至 5 层时，在 From Floor 输入 "2"、To Floor 输入 "5"。
- **无楼层信息时：** 若无单独的楼层信息，则以竖直坐标（Z 坐标）为基准运行。例：
  节点组的 Z 坐标为 0、5、10 时，分别视为「1 层」「2 层」「3 层」进行输入 — 即把 Z=0 的节点
  组定义为 "1"、Z=5 定义为 "2"、Z=10 定义为 "3"。

## 相关 JSON API 端点

Plug-in 作为基准使用的楼层信息与 `docs/manual` 的以下端点相对应。

- [`/db/STOR` — Story Data](../../../manual/zh-cn/02_DB_Project_Structure.md)

## 结论（原文）

Floor Transition Plug-in 在结构建模项目中协助完成楼层形状的转换。它自动
调整节点与单元坐标，并有效地管理楼层信息，使建模作业更加精确、快捷。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition](https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition)
