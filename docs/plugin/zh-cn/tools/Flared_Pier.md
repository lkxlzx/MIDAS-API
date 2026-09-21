# Flared Pier

> **原文：** [Flared Pier](https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier)
> **原文撰写：** 2025-04-04 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Flared_Pier.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

Flared Pier Creator Plug-in 简化了在 MIDAS CIVIL NX 中生成喇叭形桥墩（flared
pier）的过程。利用 MIDAS CIVIL NX 文件中预定义的截面与材料数据，只需最少的输入即可
高效地生成喇叭形桥墩。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- **易于使用：** 为确定桥墩柱的端部，只需选择最顶端节点的标高（Level）。
- **可定制的设计：** 以局部轴属性为基准生成喇叭形桥墩，确保精确的对位与形状。
- **高效性：** 借助 Refresh 功能，无需重启流程即可快速更新截面与材料数据。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 选择 Structural Group 与 Boundary Group（自文件中导入） |
| 2 | 输入起始节点编号（start node number） |
| 3 | 选择 Reference nodes（支座底部） |
| 4 | 选择 Sections、Materials，并输入各部位的 length（可通过标题右侧的帮助选项确认各部位） |

## 参考/限制事项

- 所选择的所有节点必须共用相同的局部轴 — 若轴不一致，生成桥墩时将发生错误。
- 在开始生成之前，须再次确认所有输入值均大于 0。
- 每当 MIDAS CIVIL NX 中发生变更时，都须通过 Refresh 图标更新截面与材料数据。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier](https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier)
