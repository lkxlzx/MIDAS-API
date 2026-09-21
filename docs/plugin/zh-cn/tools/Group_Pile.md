# Group Pile

> **原文：** [Group Pile](https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile)
> **原文撰写：** 2025-04-04 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Group_Pile.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

Group Pile Generator Plug-in在MIDAS CIVIL NX中自动化生成包含桩帽（pile cap）的群桩
（group pile）。直接与现有Civil文件数据联动，减少人工输入并保证桩基设计的一致性。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- **易用性：** 只需选择最顶层节点标高即可定义桩底位置。
- **顺畅的数据联动：** 自动从MIDAS CIVIL NX文件中读取截面与材料数据。
- **性能提升：** 群桩设置一次完成，此后即可高效生成大量桩。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 选择Structural Group、Boundary Group、Pile Material、Pile Section、Pile Cap Material（可选）、Pile Cap Section（可选） |
| 2 | 输入起始节点编号（start node numbers） |
| 3 | 输入Pile array numbers、中心间距（Spacing）、Edge length、Pile Diameter、Length、Cap height（可选）。Length的单位可在`D`（以桩自身尺寸为基准）与`L`（以全局单位为基准）中选择 |
| 4 | 若要同时生成桩帽，勾选复选框并输入Pile Cap（可选）信息 |
| 5 | 生成群桩之前选择桥墩底部节点（bottom of pier node） |

## 参考/限制事项

- **局部轴一致性：** 所选的全部节点必须共享相同的局部轴，桩才能正确对齐。
- **输入校验：** 间距、深度等数值输入必须大于0，否则会出现错误。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile](https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile)
