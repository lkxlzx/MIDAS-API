# Breakdown Load Combination

> **原文：** [Breakdown Load Combination](https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination)
> **原文创建：** 2024-08-02 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Breakdown_Load_Combination.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

以 MIDAS CIVIL 的基本荷载工况（primary load case）为基准，把复杂的荷载组合（load combination）分解为简单·基础形式的 Plug-in。可分析各种荷载组合的影响，精确把握特定组合对结构的作用。

- 将荷载组合转换为基本荷载工况
- 利用 MIDAS CIVIL 的基本荷载工况，把复杂的荷载组合简化为基础形式

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

MIDAS CIVIL 提供静力（Static）、移动（Moving）、施工阶段（Construction Stage）、温度（Thermal）、反应谱（Response Spectrum）、沉降（Settlement）、推覆（Pushover）共 7 种基本荷载工况。用户以这些基本荷载工况为基础，预估哪一个荷载组合对结构最为不利。

按设计代码的不同，可能需要数百个荷载组合，其中 Eurocode 对荷载组合·变异系数的要求尤其复杂精细。在考虑荷载组合时，用户实际上会先假定并构建一份“荷载组合路线图”：为了得到最终结果，会把基本荷载工况与已生成的荷载组合反复组合起来，问题正出在这种反复组合的方式上 —— 分析完成后，人们总希望依据分析结果找出对某个节段起不利作用的荷载工况，并据此反向追溯每一个荷载组合。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 执行分析并生成荷载组合（Load Combinations） |
| 2 | 在 Civil 中选择单元，点击 **Import Load Combinations** 按钮 |
| 3 | 选择待分解的目标荷载组合、单元端部（element end）、envelope 类型以及相应的力/力矩，点击 **Breakdown data** 按钮（需要时可输入前缀（Prefix）名称） |
| 4 | 生成新分解出的荷载组合 |

## 参考/限制事项

- **须在分析后使用：** 应在 'PostCS' 及 'locked' 状态下使用。
- **单元数量限制：** 可同时分解的单元最多 5 个。
- **荷载组合前缀：** 输入 LCB Prefix 时会体现在所生成荷载组合的名称中；不输入时，以所选荷载组合为依据生成名称。分解后的 LC 字符数限制为 **20 字符**，因此荷载工况名称或 Prefix 名称需与之匹配加以调整。
- **荷载工况基准：** 必须在 Active 列中选择 'Strength/Stress'、'Serviceability'、'Active' 基准之一。
- **荷载工况类型：** 必须在 Type 列中选择 'Add' 或 'Envelope' 类型。
- **规范限制：** 不支持南非（South Africa）·法国（France）的移动荷载。
- **荷载系数符号：** 移动荷载·沉降荷载等非对称荷载工况只允许正的（positive）荷载系数 —— 不允许负的荷载系数。

## 相关 JSON API 端点

Plug-in 所处理的荷载组合与 `docs/manual` 中的以下端点对应。但原文未指明究竟使用哪一个设计类（General/Concrete/Steel 等）端点。

- [`/db/LCOM-GEN` — Load Combinations (General)](../../../manual/zh-cn/13_DB_Load_Combinations.md)

## 结论（原文）

借助本指南，即可利用 MIDAS CIVIL 的基本荷载工况，把复杂的荷载组合有效转换为更易处理的形式。这一必备工具可帮助工程师开展细致·精确的影响分析，提高结构评估的精细度。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination](https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination)
