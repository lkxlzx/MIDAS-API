# Temperature Gradient Stress Generator

> **原文：** [Temperature Gradient Stress Generator](https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator)
> **原文编写：** 2024-12-03 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Temperature_Gradient_Stress_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

按 **AASHTO-LRFD** 标准计算 PSC、混凝土、钢组合截面在考虑温度梯度（temperature gradient）后的自平衡应力（Self-Equilibrating Stress）的 Plug-in。在桥梁截面施加温度梯度时，无需再手动计算并输入热影响引起的应力。自平衡应力值直接提供在应力汇总表中，尤其适用于包含非对称、组合截面的复杂桥梁几何建模，简化了温度引起的应力的分析与设计过程。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

分析 PSC、混凝土、钢组合截面的温度梯度影响时，传统上必须手动计算自平衡应力，既耗时又易出错。本 Plug-in 将该过程自动化，计算自平衡应力并直接显示在应力汇总表中。无需重复的手工输入或另行计算，从而简化工作流、节省时间并保证准确性。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 点击 **Import Section** 并选择要施加温度梯度的截面（从 Civil 文件读取） |
| 2 | 选择截面后，以 Civil 文件为基准设置 Temperature zone、girder surface、girder materials 选项，并选择应用截面底部显示的 T3 选项 |
| 3 | 随所选材料与选项，计算值显示在表格（⑤）中。自平衡应力也在此处查看。随选项变化，温度梯度（⑥）与自平衡应力（⑦）实时更新 |
| 4 | 向单元添加温度荷载 — 添加 Heating load（①）、Cooling load（②）（选择一个荷载工况时仅可选择其一） |
| 5 | 选择要施加的单元后，可确认已添加温度荷载 |

## 参考/限制事项 — 与既有功能的差异

多数 Civil 用户已熟悉按截面特性施加温度梯度的既有功能（`Load > Temperature > Temperature Loads > Temp. Gradient & Beam Section Temp.`）。

- **既有方式：** 要在 PSC 梁上施加温度梯度，需添加截面温度，输入深度、温度变化位置、温度变化量，并选择单元以使用该荷载。所施加的荷载不显示应力值。
- **Plug-in 方式：** 最大差异在于本 Plug-in 会在应力汇总表中显示自平衡应力。可在右侧查看非线性温度梯度曲线与自平衡应力图表。

> ⚠️ 原文的 "Conclusion" 段落照抄了 "Inertial Forces Controller" 文章的结论（与惯性力方向自动
> 转换相关的内容），与本文（温度梯度应力）无关，属原文自相矛盾。
> 本文未予搬入。

## 相关 JSON API 端点

Plug-in 处理的梁截面温度与 `docs/manual` 的以下端点对应。

- [`/db/BTMP` — Beam Section Temperature](../../../manual/zh-cn/07_DB_Temperature_Prestress.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator](https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator)
