# Alignment Local Axis for Element

> **原文：** [Alignment Local Axis for Element](https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element)
> **原文创建：** 2024-07-30 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Alignment_Local_Axis_for_Element.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

将板（Plate）单元的局部 z 轴对齐到与基准点（Reference Point）一致的方向。在排列圆柱形结构的局部轴时很有用。

## 支持版本

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 适用标准：General Use（与特定设计规范无关）

## 主要功能

可用于以指定点为基准排列结构的局部轴。

## 使用方法

| 字段 | 说明 | 选项·默认值 |
| --- | --- | --- |
| Select Elements | 在 midas Civil 中选择单元后进入 Plug-in 窗口 | — |
| Reference Point | 输入局部 z 轴所要对齐的基准节点坐标。局部 z 轴将被排向指向该节点的方向 | — |

## 参考/限制事项

Plate 单元局部轴的排列逻辑如下。

1. 沿 Plate 单元的局部方向计算法向向量。
2. 计算由平面中心到 Reference Point 的向量。
3. 两向量夹角小于 90 度时不排列局部轴；超过 90 度时反转 Plate 单元的方向，按相反的轴排列。

## 结论（原文）

可以轻松反转指定单元的轴向。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element](https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element)
