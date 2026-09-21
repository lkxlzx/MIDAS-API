# Traffic Lane Generator

> **原文：** [Traffic Lane Generator](https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator)
> **原文编写：** 2026-07-22 · **原文最后编辑：** 2026-07-23

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Traffic_Lane_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

Traffic Lane Generator 是只需一次点击即可生成多条车道（traffic lane）的 Plug-in。

## 支持版本

`MIDAS CIVIL NX 2025 (v2.2)`

## 主要功能

- **高效性：** 一次点击生成多条车道，把传统上高度重复的过程自动化。
- **广泛兼容：** 目前支持 15 个移动荷载代码（moving load code）。
- **直观界面：** Plug-in 输入项与 Civil NX 用户界面一致，降低了老用户的学习成本。
- **即时应用：** 同时生成多条车道，并自动应用到 Civil NX 模型中所选的单元。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 Civil NX 中直接选择车道所依据的基准单元 |
| 2 | 在下拉菜单中选择要施加的移动荷载代码 |
| 3 | 在左侧面板定义轮距（wheel spacing）、车道宽度、跨径长度、冲击系数、车辆荷载分布等通用车道参数 |
| 4 | 在右侧 Lane Configuration 区的表格中添加、删除车道，并指定各车道（L1, L2, L3 等）的偏心（eccentricity） |
| 5 | 点击窗口右下角的 **"Generate Traffic Lanes"** 按钮执行生成 |

## 结论（原文）

Traffic Lane Generator 简化了 Civil NX 中的车道定义过程。它借助 API 联动消除手工重复作业并保证准确性，使工程师能把更多时间投入核心的分析与设计工作。

## 相关 JSON API 端点

Plug-in 生成的车道与 `docs/manual` 的以下端点对应。

- [`/db/LLAN` — Traffic Line Lanes](../../../manual/zh-cn/08_DB_Moving_Loads.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator](https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator)
