# Rebar Auto Generator

> **原文：** [Rebar Auto Generator](https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator)
> **原文撰写：** 2026-07-27 · **原文最后编辑：** 2026-07-29

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Rebar_Auto_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

按澳大利亚RMS标准自动化生成截面的纵向与抗剪钢筋的Plug-in。
可在预定义的标准位置快速、准确地生成钢筋。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.1)`

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 单击**Connect** → 打开Marketplace并运行Rebar Auto Generator Plug-in |
| 2 | 选择Section ID、Type、Name、vBar size、Pitch，然后单击**Generate Rebar** |

## 参考/限制事项

1. Plug-in自动识别PSC-Composite截面并用于钢筋生成。
2. 运行Plug-in时会覆盖所选截面的既有钢筋数据。
3. 目前仅支持`AS-Super-T_RMS_2019`截面。
4. 可用**'Ref .dwg file'**查看图纸形式的钢筋详图。

## 相关JSON API Endpoint

本Plug-in生成的截面钢筋信息，与`docs/manual`中的下列Endpoint对应。

- [`/db/RPSC` — Section Manager (Reinforcements)](../../../manual/zh-cn/04_DB_Properties.md)

## 结论（原文）

Rebar Auto Generator Plug-in简化了MIDAS CIVIL NX，尤其是RMS标准截面中的钢筋建模。
自动化钢筋布置并保证对预定义标准的遵循，减轻人工负担并把错误降到最低。

> ⚠️ 原文的"Benefits of this plugin"段落，看起来是原样复制了与本文章实际功能
> （自动生成截面钢筋）无关的另一Plug-in的内容（与时程荷载工况·EN1991-2:2003阻尼·
> 行车速度-加速度图形相关的内容，与"Dynamic Analysis of Rail Bridge"文句相同）。
> 这属于原文明显的自相矛盾，因此本文档未予收录。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator](https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator)
