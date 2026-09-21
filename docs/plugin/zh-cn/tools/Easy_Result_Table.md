# Easy Result Table

> **原文：** [Easy Result Table](https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table)
> **原文撰写：** 2025-08-05 · **原文最后编辑：** 2026-07-27

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Easy_Result_Table.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 无需逐个进入菜单查找结构计算书所用的后处理结果表格（Reaction、Story
Drift 等），而是把所需的表格一次性汇总，批量输出为结构计算书用 PDF。

## 支持版本

`MIDAS GEN NX 2025 (v1.1) KR`

## 主要功能

- 去除了每个项目中重复出现的「按结果表格逐一进入菜单手动确认、保存」的过程 — 结构计算书
  所需的结果表格少则 3 个、多则 10 个以上，重复作业负担很大。
- 把常用的表格配置**预先保存为设置值**，在后续项目中也可调用同一设置自动输出。

## 使用方法

| 区域 | 说明 |
| --- | --- |
| Result Table 列表 | 以树形结构显示可用的结果项（Reaction、Story Drift、Overturning Moment 等）。点击各项右侧的 **Add** 按钮，将其加入当前表格 |
| Settings 面板 | 调整在列表中所选项目的细项（要显示的楼层范围、单位、排序等）后，点击 **Save** 确定 |
| Save / Load | 将重设定信息与结果表格配置保存为本地 `.json` 文件并复用 |
| CREATE TABLE | 反映已 Add 的全部项目与设置，生成最终结果表格 → 通过 **Export to PDF** 输出结构计算书用 PDF |
| 列表管理工具栏 | `+`：自定义项目添加对话框，🗑️：删除所选项目 |

**使用步骤：** 在所需的组中点击 `Add` → 选择已添加的项目（激活 Settings 面板）→ 指定 Load Case
Name、Units（Force、Distance）与 Styles（Style、Decimal Places）→ `Save` → `Create Table` →
在 Table Processing Status 中确认成功（OK）/无法输出（NG）→ `Download PDF`
（`all-table-YYYY-MM-DD.pdf`）。

## 参考/限制事项

本 Plug-in 支持输出的后处理结果表格清单：

- Reaction Force/Moments(Global)
- Vibration Mode Shape(Eigenvalue Mode)
- Story Drift (X, Y)
- Story Displacement (X, Y)
- Story Shear (Response Spectrum Analysis)
- Story Eccentricity
- Story Shear Force Ratio
- Stability Coefficient (X, Y)
- Weight Irregularity Check (X, Y)
- Overturning Moment
- Story Axial Force Sum
- Torsional Amplification Factor (X, Y)
- Stiffness Irregularity Check (Soft Story) (X, Y)
- Capacity Irregularity Check (Weak Story)

## 相关 JSON API 端点

Plug-in 所查询的后处理结果表格与 `docs/manual` 的以下端点相对应。

- [`/post/table` — Reaction](../../../manual/zh-cn/19_POST_AnalysisResult_1.md#1-reaction)
- [`/post/table` — Vibration Mode Shape](../../../manual/zh-cn/20_POST_AnalysisResult_2.md#28-vibration-mode-shape)
- [`/post/table` — Story Drift 等楼层结果表格总览](../../../manual/zh-cn/21_POST_StoryTables.md) *(Story
  Displacement、Story Shear、Story Eccentricity、Overturning Moment 等清单中的大部分属于
  本章)*

## 结论（原文）

本 Plug-in 将重复性的后处理结果输出作业实现自动化，是一款既能节省时间、又可
保持文档一致性的有力工具。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table](https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table)
