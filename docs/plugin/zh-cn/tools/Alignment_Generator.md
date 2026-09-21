# Alignment Generator

> **原文：** [Alignment Generator](https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator)
> **原文创建：** 2024-12-03 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Alignment_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 可生成包含圆弧（arc）或缓和曲线（clothoid）·三次抛物线（cubic parabola）在内的复杂线形。它把复杂线形的生成自动化，无需手工计算与输入。以全局坐标系或用户指定角度为基准，将水平惯性力对齐到各桥墩（pier）最接近的方向。

对于曲线桥·匝道这类桥墩与全局坐标系之间方位错开、从而使抗震分析工作流容易变得复杂的复杂桥梁形体建模，本 Plug-in 尤其有用。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

传统上，结构工程师在用 CAD 工具准备整个分析项目时，要经过线形分段、定义跨径长度与支座位置、把文件导出到 MIDAS CIVIL NX 等一系列重复性工作。即使改用 Lisp 或 AutoCAD VBA，这个过程依然耗时很长，而且容易出现人为失误。Alignment Generator Plug-in 在 MIDAS CIVIL NX 内部直接自动化线形生成，从而省去这些繁琐步骤，节省时间、减少错误，并简化整个工作流。

## 使用方法

| 字段 | 说明 | 选项·默认值 |
| --- | --- | --- |
| 添加分段 / 选择线型 | 添加分段（①）并选择线形种类（②），同时指定长度·起始/结束半径（③） | — |
| 分段间距 | 输入所要生成的节点之间的距离（= 单元长度） | — |
| Structure Group / Material / Section ID | 按分段设置结构组·材料·截面 ID（④） | — |
| 预览图 | 底部图形随输入值实时刷新，提供预览（⑤） | — |
| Create | 输入完成后点击，即生成节点·单元·局部轴 | — |
| 帮助图标 | 使用过程中有疑问时，可通过帮助图标查看 Plug-in 信息 | — |

> ⚠️ **注意（原文）：**
> - 分段的个数不必与线形（alignment）的个数相同。
> - 分段的总长度应小于线形长度。
> - 截面（Section）与材料（Material）必须在运行 Plug-in 之前预先创建完成。
> - 基准节点的位置以 GCS 为基准取 (0,0,0)，节点编号沿 X(+) 方向递增。
> - 本 Plug-in 仅在 X-Y 平面内工作。

生成后的线形可以随时方便地更新 —— 只需修改半径（Radius）取值后再次点击 **Create**。

## 参考/限制事项

Plug-in 的内部缓和曲线计算函数支持：**Clothoid**、**Cubic Parabola**。

## 结论（原文）

Alignment Generator Plug-in 能够节省用户在 CAD 作业过程中耗费的时间，并消除人为失误的可能。用户只需输入线形种类、半径、分段间距。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator](https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator)
