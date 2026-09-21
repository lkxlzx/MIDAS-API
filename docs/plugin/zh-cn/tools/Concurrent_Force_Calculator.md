# Concurrent Force Calculator

> **原文：** [Concurrent Force Calculator](https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator)
> **原文撰写：** 2026-07-23 · **原文最后编辑：** 2026-07-23

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Concurrent_Force_Calculator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 用于从所选结构构件中提取并导出同时力（concurrent force）结果。
它以用户所选的构件、荷载组合与力分量为基准，生成整理为表格形式的力数据，从而简化分析
结果的审查过程。通过精简后处理（post-processing）作业，使结构性能评估与工程
报告的编制更加便捷。

## 支持版本

`MIDAS CIVIL NX 2025 (v2.1)`

## 主要功能

- 从所选结构构件快速提取同时内力（internal force）结果。
- 减少手动数据收集与后处理所耗费的时间。
- 可仅关注所需的构件与荷载组合。
- 可选择性地支持以下力分量：`FX`（轴力）、`FY`（剪力）、`FZ`（剪力）、`MX`（扭转力矩）、
  `MY`（弯矩）、`MZ`（弯矩）。
- 可将结果直接导出为 Microsoft Excel，用于进一步分析、汇报与文档化。
- 可选择新建 Excel 工作表或更新已有工作表。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1. 选择结构构件 | 选择需要同时力结果的模型中的结构构件 |
| 2. 选择荷载组合 | 选择一个以上要提取结果的荷载组合 |
| 3. 选择力分量 | 选择输出中包含的力分量（`FX`、`FY`、`FZ`、`MX`、`MY`、`MZ`） |
| 4. 生成结果 | 运行 Plug-in，提取所选构件与所选荷载组合的同时力数据 |
| 5. 导出为 Excel | 导出为新工作表或更新已有工作表。导出的表格已整理妥当，便于审查、筛选与汇报 |

## 参考/限制事项

- 运行 Plug-in 前，结构分析必须已成功完成。
- 仅处理已选择的构件，未选择的构件不包含在输出中。

## 结论（原文）

Concurrent Force Calculator 提供了从结构分析模型中快速、高效地提取、整理
并导出同时力结果的方法。可按构件、荷载组合与力分量进行选择性提取，从而减少
手工作业负担，并提升工程后处理与报告流程的准确性和效率。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator](https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator)
