# CS Report Generator

> **原文：** [CS Report Generator](https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator)
> **原文创建：** 2026-04-10 · **原文最后编辑：** 2026-04-10

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/CS_Report_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

为 MIDAS CIVIL NX 模型生成清晰的逐阶段（stage-wise）施工阶段报告。它汇总施工阶段全过程中结构·边界·荷载组的激活/未激活状态，便于快速校验与文档化。提供基于 Excel 的报告预览与下载。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.1)`

## 主要功能

- **快速概览：** 把各施工阶段的激活/未激活结构组、边界组、荷载组即时汇总为一份统一的 Excel 报告。
- **减少建模错误：** 以表格形式呈现施工阶段设置，有助于发现遗漏或并非本意的激活项。
- **节省时间的工作流：** 无需在 CIVIL NX 中手工逐一查看多个对话框·表格·窗口，全部施工阶段数据自动提取。

## 使用方法

| 按钮 | 说明 |
| --- | --- |
| Generate Report | 提取施工阶段数据，自动生成 Excel 报告并预览 |
| Download Excel Report | 以 `.xlsx` 格式导出报告 |
| Reset | 初始化当前会话并重新生成报告 |

## 参考/限制事项

本 Plug-in **不修改**以下内容 —— 它是只读（read-only）的校验·报告工具。

- 模型数据
- 施工阶段（Construction Stages）
- 激活/未激活设置

## 相关 JSON API 端点

Plug-in 所提取的施工阶段定义，与 `docs/manual` 中的以下端点对应。

- [`/db/STAG` — Define Construction Stage](../../../manual/zh-cn/10_DB_Construction_Stage.md)

## 结论（原文）

Construction Stage Report Generator 简化了在 MIDAS CIVIL NX 中校验施工阶段设置的过程。它给出清晰、结构化且可导出的汇总，使工程师能够快速校验模型、减少错误并提升生产率。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator](https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator)
