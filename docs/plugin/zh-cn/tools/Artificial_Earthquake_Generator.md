# Artificial Earthquake Generator

> **原文：** [Artificial Earthquake Generator](https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator)
> **原文创建：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Artificial_Earthquake_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 按标准生成时程分析用的**反应谱**与**人工地震波**并绘制图形。可利用设计谱生成人工地震波，并将其转换为谱荷载图形。其中包含 ASCE7 谱系列标准，数据取自 USGS Seismic Design Geodatabase。

## 支持版本

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 适用标准：American Standard (ASCE7-22)

## 主要功能

基于 USGS Seismic Design Geodatabase，提供按 ASCE7-22 标准的反应谱数据。可查询指定地区的纬度/经度数据，并提供 4 种 RS 数据类型。

- Two-Period Design Spectrum
- Two-Period MCEr Spectrum
- Multi-Period Design Spectrum
- Multi-Period MCEr Spectrum

在生成的 RS 数据基础上，还可通过谱匹配（spectral matching）按目标谱拟合，生成与之吻合的人工地震动数据。

- 按标准精确生成反应谱·人工地震波
- 利用 USGS 数据获得可靠结果
- 将生成数据以图形可视化，便于分析
- 界面易用，便于选择设计标准与输入数据

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1. 选择 Spectrum Standard | 运行 Plug-in 并选择设计谱标准（ASCE7-22） |
| 2. 输入 Target Address | 输入目标地址并点击 **Search**。可按地址（By Address）或纬度/经度（By Latitude/Longitude）输入 |
| 3. 输入 Seismic Data | 设置 Risk Category、Soil Site Class、Design Spectrum Option |
| 4. Calc. Design Spectrum | 点击后计算反应谱 |
| 5. 设置 Artificial Earthquake Data | 为计算人工地震数据，按地震烈度输入 Rise·Level·Total time·Damping Ratio 等取值 |
| 6. Calc. Artificial Earthquake | 点击后生成时程函数数据 |
| 7. 结果分析 | 将结果图形可视化并加以分析 |
| 8. Update RS Function / Update TimeHistory Function | 点击后把结果数据导入（import）到程序中 |

### 反应谱数据生成方法

检索目标地区后，在 Seismic Data 中输入地震危险系数·地震分区系数，再点击 **Calc. Design Spectrum**，即输出基于 USGS Seismic Design Geodatabase 的反应谱数据。查看可视化与文本结果后，点击 **Update RS Function** 即把数据导入 Civil NX 的 **RS Functions**。

### 时程分析用人工地震波生成方法

在设计谱中选择设计标准，并按待评估的地震烈度输入包络函数数据·最大加速度·阻尼比等函数取值。点击 **Calc. Artificial Earthquake** 即生成人工地震波，并转换为谱或加速度图形。复核结果后点击 **Update TimeHistory Functions**，即把数据导入 Civil NX 的 **TimeHistory Functions**。

生成的人工地震波可用 **Graph Type** 切换为谱·加速度图形的形式查看。

## 相关 JSON API 端点

原文中明确指出结果导入的对象是 Civil NX 的“RS Functions”“TimeHistory Functions”，二者与 `docs/manual` 中的以下端点对应。

- [`/db/SPFC` — Response Spectrum Functions](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)
- [`/db/THFC` — Time History Functions](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)

## 结论（原文）

借助本指南，即可使用基于新标准（ASCE7-22）的 RS 与人工地震波生成 Plug-in，有效地生成并分析时程分析用的反应谱·人工地震波。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator](https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator)
