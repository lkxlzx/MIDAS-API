# Rebar Spacing Converter

> **原文：** [Rebar Spacing Converter](https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter)
> **原文撰写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Rebar_Spacing_Converter.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

以钢筋截面积为基准，可校核不同直径钢筋间距的Plug-in。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

设计实务中经常需要把钢筋直径改为其他规格。此时原有钢筋直径所规定的间距也必须随新直径
相应改变，而按钢筋截面积为基准重新计算，可使重新设计的过程变得简单。

- 按标准快速校核钢筋间距，提高设计与施工效率。
- 内置钢筋数据库，可按相应标准校核间距。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 选择各国钢筋标准（national rebar standard） |
| 2 | 在单选列表中选择输入方法（4种方式） |
| 3 | 选择钢筋规格与间距 |
| 4 | 单击**ADD TO BELOW LIST**后，所选的钢筋规格·间距会被添加到列表中 |

**示例：** 要把按`#4@100`布置的钢筋改为`#3`与`#4`共同使用的布置 — 将钢筋代码设为"ASTM"、
输入方法选为"1=>2"（因为是把单根钢筋`#4`改为两根钢筋`#3+#4`）。把Before rebar size设为"#4"、
before spacing设为"100"、after rebar size设为"#3"、"#4"后，"After Rebar Spacing"会自动计算并
显示为`#3+#4@77.5`。单击**ADD TO BELOW LIST**即可按列表形式查看结果。

**Rebar Spacing Verification：** 按输入的规格·间距布置钢筋，可在保持相同截面积的前提下
校核不同直径钢筋的间距。

## 参考/限制事项

### 支持的钢筋标准

| 代码 | 标准 |
| --- | --- |
| ASTM | American Society for Testing Materials |
| KS | Korean Industrial Standards |
| EN | European Code |
| GB | Chinese National Standard |
| IS | Indian Standards |
| JIS | Japanese Industrial Standards |
| UNI | Italian National Standards |
| AS/NZS | Australian/New Zealand |

### 输入方法

| 方法 | 说明 | 示例 |
| --- | --- | --- |
| Input Method 1 | 输入单一钢筋规格 | 钢筋规格`#4`、间距`100` → `#4`钢筋按100间距布置 |
| Input Method 2 | 输入两种钢筋规格 | 钢筋规格`#4`、`#6`、间距`100` → `#4`、`#6`钢筋按100间距交替布置 |

## 结论（原文）

用Rebar Spacing Converter Plug-in可换算不同直径的钢筋，并以相同截面积为基准校核钢筋间距。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter](https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter)
