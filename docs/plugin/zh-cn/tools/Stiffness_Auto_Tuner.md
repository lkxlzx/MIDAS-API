# Stiffness Auto Tuner

> **原文：** [Stiffness Auto Tuner](https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner)
> **原文编写：** 2026-05-22 · **原文最后编辑：** 2026-08-13

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Stiffness_Auto_Tuner.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

Beam/Wall Stiffness Auto Tuner 是支持自动调整所选梁单元 Element Stiffness Factor 与墙单元 Wall Stiffness Factor 的 Plug-in。它以用户定义的条件为基准反复执行分析与设计验算，确认构件验算比（check ratio）是否满足用户设定的目标比后，按定义的刚度折减顺序更新 Stiffness Factor。它减少了修改梁、墙 Stiffness Factor 并重跑分析的重复性手工操作。最终采用的刚度条件可在 MIDAS 模型中直接查看。

## 支持版本

- `MIDAS GEN NX 2026 v2.2`
- 适用标准：KDS 41 20 2022 RC — Beam check 使用 Beam Check 结果，Wall check 使用 Wall Design 结果

## 主要功能

- **梁、墙批量应用：** 可将梁（Beam）与墙（Wall）一次性设为对象，批量完成各构件的 Stiffness Factor 调整与迭代分析（2026-08-13 原文修订新增）。
- **自动迭代（Automatic iteration）：** 反复执行运行分析、查看设计结果、按用户设定的目标比更新 Stiffness Factor。
- **基于模型的单元选择：** 在 MIDAS GEN NX 中选择的目标构件可与 Plug-in 直接同步。
- **Stiffness Factor 顺序控制：** 设置刚度折减步长，并通过添加/删除数值直接编排用于迭代分析的刚度折减顺序。
- **自动分组：** 梁单元在最终分析结束后按刚度自动生成 Element Group（例：`AutoTuner_Beam [0.80] [Node=0; Element=4]`）。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 运行 Plug-in，在上级选项卡中输入梁或墙的条件（2026-08-13 原文修订 — 此前需分别选择 **Beam Stiffness Tuner** / **Wall Stiffness Tuner** 两个 Plug-in，现改为在同一界面中以选项卡切换） |
| 2 | 在 MIDAS 模型中选择目标构件并点击 **Sync from product**。梁刚度调整读取所选梁单元，墙刚度调整按 Wall ID、层信息读取所选墙单元 |
| 3 | 必要时可批量选择分配给特定 Section 或 Wall ID 的构件 |
| 4 | （可选）设置是否考虑梁上已施加的 Section Stiffness Factor。启用后不仅考虑 Element Stiffness Factor，还考虑既有 Section Stiffness Factor，并以更小的值为基准执行分析与设计 |
| 5 | 设置 **Decrement Stiffness Step Value**。按指定步长生成从 100% 向下递减的刚度折减顺序，并显示在 **Stiffness decrement sequence** 中 |
| 6 | 在 **Value to insert** 输入数值即会加入 Stiffness decrement sequence；可用 **Value to delete** 从序列中删除数值 |
| 7 | 输入 **Iteration Number** 与 **Target Ratio**。Target Ratio 是判断是否需要进一步折减刚度的设计比限值 |
| 8 | 在 **Analysis scope** 中设置梁与墙是全部纳入执行阶段还是单独执行（2026-08-13 原文修订新增） |
| 9 | 查看最终结果对话框 — 汇总显示仍超出目标比的构件、达到刚度下限的构件，以及所选单元最终采用的刚度值 |
| 10 | 最后一次迭代结束后，MIDAS 模型中自动生成刚度组，所选单元按最终刚度比分配到该组 |
| Back | 返回主页面 |
| Refresh | 重新打开模型或模型信息发生变更时，以最新信息刷新 Plug-in |

## 结论（原文）

本 Plug-in 提供了基于迭代分析与设计验算结果自动调整梁、墙刚度系数的工作流。它把构件选择、刚度折减顺序设置、目标比输入、自动分组分配串联为一个工作流，减少刚度调整所需的重复手工操作。用户可将生成的刚度值作为设计审查过程的一部分使用，并需验证最终模型行为是否满足项目要求。

## 相关 JSON API 端点

Plug-in 声明调整的梁单元刚度系数与 `docs/manual` 的以下端点对应。墙刚度系数（Wall Stiffness Factor）对应哪个端点原文并未说明，因此未加链接。

- [`/db/ESSF` — Element Stiffness Scale Factor](../../../manual/zh-cn/04_DB_Properties.md) *（仅梁单元，墙对应关系未确认）*

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner](https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner)
