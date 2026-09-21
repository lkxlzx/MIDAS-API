# Load Effect for Load Combination

> **原文：** [Load Effect for LC](https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination)
> **原文撰写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Load_Effect_for_Load_Combination.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

提取指定荷载组合（Load Combination）中所含各荷载工况（Load Case）的梁内力（Beam force）
值，从而便于从构件内力角度把握各荷载工况对荷载组合的贡献度。可以快速、准确地分析
各荷载工况对结果的影响。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

产品方面经常收到的咨询：

- 结果仅以Excel风格的表格形式输出。
- 出现意外结果时，用户必须手工核查荷载设置。

本Plug-in管理各个输入值，用过滤系统追踪错误取值，并可在结果标签中快速分析。
它被全球客户列为期望实现的功能，发生错误时能够轻松识别问题所在。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 查看荷载组合列表 | 1. 运行Plug-in，并在荷载组合列表中选择所需的一般荷载组合。2. 确认所选的荷载组合并单击**Select** |
| 确认荷载组合 | 3. 在模型视图中选择要审查的单元。4. 在Plug-in中单击**Import**按钮保存所选单元。5. 设置待输出的梁内力结果的Position、Unit、Style |
| 查看荷载工况列表 | 6. 单击**Create Force**后，该荷载组合的Beam force数据输出到右侧"Force Table"。若包含移动荷载工况，可能同时显示最大值·最小值工况 |
| 结果验证 | 7. 输出Force Table后，例如选取gLBC4(min)的值，确认构成构件内力的load effect。8. 选取时输出构成该荷载组合的各荷载工况及各自的Unfactored Value、Factor、Factored Value。9. 最不利的值以**红色**、影响最小的值以**蓝色**可视化。选择Sort by Absolute或Sort by Max/Min即按该基准排序 |

## 相关JSON API Endpoint

本Plug-in所处理的荷载组合·构件内力结果，与`docs/manual`中的下列Endpoint对应。

- [`/db/LCOM-GEN` — Load Combinations (General)](../../../manual/zh-cn/13_DB_Load_Combinations.md)
- [`POST 8. Beam Force`](../../../manual/zh-cn/19_POST_AnalysisResult_1.md)

## 结论（原文）

通过本指南可以清楚地理解构成最终结果的中间数值，并用Load Effect Analysis Plug-in
高效分析各荷载工况的贡献度。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination](https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination)
