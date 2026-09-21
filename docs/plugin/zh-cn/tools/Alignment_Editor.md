# Alignment Editor

> **原文：** [Alignment Editor](https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor)
> **原文创建：** 2026-07-22 · **原文最后编辑：** 2026-07-22

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Alignment_Editor.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

Alignment Editor Plug-in 用于修改桥梁模型的线形（alignment）。它把节点几何从初始基准线形转换为新的目标线形，并自动更新竖向单元的角度（beta angle）。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.1)`

## 主要功能

- **线形感知转换（Alignment Aware Transformation）** — 精确地把所有节点的相对距离·垂直偏距·高程搬到新线形上，从而自动重映射模型。
- **节省时间** — 无需手工重排节点，把原本耗时数小时的工作缩减为一次点击。
- **减少错误** — 消除了手工坐标编辑，大幅减少几何与数据处理上的错误。
- **灵活插值（Flexible Interpolation）** — 提供多种插值方案，以契合线形几何意图。
- **方向自动更新** — 更新竖向单元的角度，使局部轴沿新线形保持一致。

## 使用方法

| 字段 | 说明 | 选项·默认值 |
| --- | --- | --- |
| Initial Points | 定义初始线形的表格。可 ① 点击 **Import Coordinates**，从当前 MIDAS CIVIL NX 模型中所选节点自动提取坐标；或 ② 直接输入·修改 X/Y/Z | — |
| Final Points | 定义目标线形的表格。直接输入 X/Y/Z 坐标 | — |
| Interpolation Method | 选择在点之间生成线形曲线的插值方法 | `Cubic` / `Akima` / `Makima` / `PCHIP` |
| Update Alignment | 应用转换。成功时显示 “Alignment modified” 确认信息 | — |

## 参考/限制事项

- **插值方法选择：** 采用不同的插值方法，曲线经过控制点的方式也不同。
  - `Cubic` 生成光滑曲线，但在急剧变化区段附近可能出现过冲·欠冲。
  - `Akima`、`Makima` 可减小过冲。
  - `PCHIP`（Piecewise Cubic Hermite Interpolating Polynomial）保证曲线不会超出相邻点的取值范围。
- **线形点要求：** Initial Points 与 Final Points 表格都必须至少 2 行，且 X 坐标需按升序排列。
- **端点处理（End point Behaviour）：** 位于初始线形 X 范围之外的节点，以最近的线形端点为基准按刚体旋转（rigid rotation）方式映射。
- **参考链接（原文提供）：** `scipy.interpolate.CubicSpline`、`scipy.interpolate.Akima1DInterpolator`、
  `scipy.interpolate.PchipInterpolator`

## 结论（原文）

Alignment Editor 在保持几何关系的前提下，将桥梁模型重排到更新后的线形上。它自动更新节点坐标与单元方向，在 MIDAS Civil NX 之内提供了完整闭环的线形修改工作流。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor](https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor)
