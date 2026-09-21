# Response Spectrum Generator

> **原文：** [Response Spectrum Generator](https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator)
> **原文撰写：** 2025-04-14 · **原文最后编辑：** 2026-07-27

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Response_Spectrum_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

按**NZS 1170.5 (2004)**等各国抗震荷载标准自动化生成设计反应谱（Design Response
Spectrum）数据的Plug-in。为需要高精度地震输入函数进行结构分析的工程师而开发。
支持自定义参数并提供实时图形预览，简化反应谱的生成过程。

## 支持版本

`MIDAS CIVIL NX 2025 (v1.1) US`, `MIDAS GEN NX 2025 (v1.1) US`

## 适用标准（原文列明）

- `NZS 1170.5:2004` — New Zealand Standard for Seismic Actions
- `AS 1170.4:2024` — Australian Standard for Earthquake Actions
- `SBC 301-CR:2018` — Saudi Building Code: Seismic Design Provisions
- `NF EN1998-1:2008` — French National Annex to Eurocode 8
- `UNE EN1998-1:2011` — Spanish National Annex to Eurocode 8
- `SNZ TS 1170.5:2025` — New Zealand Standard for Seismic Actions
- `Peru E.030:2026` — Peru Standard for Seismic design

> ⚠️ 上述"适用标准"列表中列出了7个代码，但原文的"Note"一节明确写有"Currently,
> only NZS 1170.5 (2004) is supported."（目前仅支持NZS 1170.5(2004)），两节内容互相矛盾。
> 该Plug-in实际支持到哪些代码，原文本身即处于不明确状态，因此建议在使用前于最新版本中
> 直接确认所支持的代码。

## 主要功能

- **按代码生成谱值：** 依据所选代码，用自定义抗震参数计算谱加速度值。
- **实时可视化：** 在施加之前预览生成的反应谱图形。
- **可随时联动：** 生成的数据可立即指定给荷载工况或分析函数。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1. Function Name | 输入谱名称（例：RS 01）— 要继续执行的必填项 |
| 2. Design Spectrum Selection | 选择设计标准 |
| 3. Set Parameters | 设置参数 |
| 4. Preview Design Spectrum | 按输入值查看谱图形 |
| 5–6. Apply RS Data | 单击**Update**后，将该谱指定为供分析使用的Response Spectrum Function |

## 参考/限制事项

- 所有输入字段均需为有效的正的小数值。输入有误时会弹出警告模态框。
- （原文Note明确）目前仅支持NZS 1170.5 (2004)，今后若更改设计代码，则必须重新设置
  全部相关抗震参数。
- 其设计目标是提供与所选代码匹配的本地参数设置。
- 适合与需要谱输入的动力分析模块配合使用。

## 相关JSON API Endpoint

本Plug-in生成并指定的反应谱函数，与`docs/manual`中的下列Endpoint对应。

- [`/db/SPFC` — Response Spectrum Functions](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator](https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator)
