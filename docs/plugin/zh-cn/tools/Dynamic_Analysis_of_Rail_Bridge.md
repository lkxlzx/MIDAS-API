# Dynamic Analysis of Rail Bridge

> **原文：** [Dynamic Analysis of Rail Bridge](https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge)
> **原文撰写：** 2026-07-23 · **原文最后编辑：** 2026-07-23

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Dynamic_Analysis_of_Rail_Bridge.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

铁路桥梁的动力分析，需要在各种列车荷载与运行速度条件下精确评估结构加速度。
本 Plug-in 将分析模型内大量时程荷载工况的生成自动化，大幅减少了荷载定义、
数据提取与结果分析所需的手工作业。通过提升效率，使桥梁的动力响应得以准确而一致地
进行评估。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.1)`

## 主要功能

- **自动化的效率：** 消除了在不同速度与编组条件下对时程荷载工况进行重复性手动定义的
  工作。
- **标准化与一致性：** 采用依据国际标准（**EN1991-2:2003, Clause 6.4.6.3 (2)**）的基本阻尼值，
  为可靠的分析提供支撑。
- **顺畅的报告与导出：** 即时以图形显示运行速度与最大加速度的关系，并提供用于综合
  报告的动态 Excel 导出功能。

## 使用方法

| 字段 | 说明 |
| --- | --- |
| Train Speed Parameters | 定义 Initial Speed、Final Speed 与 Speed Increment 后，自动生成所需的全部时程荷载工况 |
| Time Step Increment | 设置各时程工况求解器积分所用的时间步长（Δt） |
| Bridge Type for Damping | 选择预置的桥梁类型（应用 EN1991-2 默认值）或直接输入用户自定义的阻尼值 |
| Train Load File | 上传包含列车荷载数据（序列号、轴重、轴距）的 Excel 文件。Plug-in 自动对其进行校验，并在相邻窗口预览设置 |
| Rail Track Nodes | 指定表示动态轴重所行经的轨道路径的结构节点组 |
| Acceleration Output Nodes | 选择用于评估竖向结构加速度响应的结构节点组 |
| Speed vs. Acceleration Plot | 查看所定义速度范围内的绝对最大加速度曲线，并将完整数据集导出为 Excel |

## 参考/限制事项

分析执行前必须确认的关键建模条件（原文注明）：

- **单元网格形状：** 沿轨道路径连续任意两个桥梁单元长度之和（x1 + x2）必须大于任意两
  列车轴之间的最小距离（d_min）— `x1 + x2 > d_min`。
- **数据完整性：** Plug-in 界面对话框中的所有必填输入项，必须在动态求解器运行之前
  填写完毕并通过校验。

## 相关 JSON API 端点

Plug-in 生成的时程荷载工况与 `docs/manual` 的以下端点相对应。

- [`/db/THIS` — Time History Load Cases](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)

## 结论（原文）

Dynamic Analysis of Rail Bridge Plug-in 将复杂的列车-结构物动力相互作用分析
转变为标准化、可靠且高度自动化的流程。通过整合自动荷载工况生成、符合标准的阻尼值
与图形输出，工程师能够以充分的信心、高效地验证高速铁路运行条件下桥梁的动力性能。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge](https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge)
