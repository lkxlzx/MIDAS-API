# Local Axis

> **原文：** [Local Axis](https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis)
> **原文撰写：** 2025-04-09 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Local_Axis.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

利用Plug-in求解切线方向的节点局部轴（tangential Node Local Axis）位置。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

结构设计时需以某一坐标轴为基准进行建模与分析。坐标轴默认使用全局轴（Global Axis），
但当构件具有参数化（parametric）形状时，需以采用局部轴（Local Axis）的输入与结果值
来查看荷载与构件内力。

在既有分析程序中，为从全局轴切换到局部轴，必须求出两轴的旋转值并直接施加。本Plug-in
同时对所有已选择局部轴值的节点进行计算，把旋转后的数值直接输入到运算与程序中。

- 自动化人工局部轴运算，缩短设计时间
- 减少反复修改作业带来的人为失误
- 提供多种切线计算公式选项，支持准确而高效的设计

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 选择Cubic Spline的Type |
| 2 | 选择要应用Local Axis的节点。必须用**Import Node**按钮在CIVIL NX建模中直接选择并导入 |
| 3 | Local Axis应用到建模中 |
| 4 | 可通过图形实时查看Spline形状 |

通过Spline按钮可以直观地查看各Spline之间的差异。

## 参考/限制事项

- Import Node须在CIVIL NX建模中以直接选择的方式导入，且必须通过**Import Node**按钮执行。
  Plug-in仅读取X-Y平面的信息。
- Spline仅沿X轴正（+）方向生成。
- Start Point与End Point用于计算Cubic Spline的起点·终点角度，仅在Clamped Cubic Spline下有效。

## 相关JSON API Endpoint

本Plug-in所应用的节点局部轴，与`docs/manual`中的下列Endpoint对应。

- [`/db/SKEW` — Node Local Axis](../../../manual/zh-cn/03_DB_Node_Element.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis](https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis)
