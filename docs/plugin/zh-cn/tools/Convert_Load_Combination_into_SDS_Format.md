# Convert Load Combination into SDS Format

> **原文：** [Convert Load Combination into SDS Format](https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format)
> **原文撰写：** 2025-04-08 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Convert_Load_Combination_into_SDS_Format.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 将荷载组合转换为仅由基本荷载工况构成的组合，使其可用于
**MIDAS SDS**。

## 支持版本

`MIDAS GEN NX 2026 (v1.1) KR`

## 主要功能

进行结构设计时必须建立荷载组合，而该组合随结构物所受荷载状态的不同而不同，施加于
荷载的系数又随设计标准而不同，因此要自动生成满足所有条件的荷载组合是困难的。

用户本想自行编写程序未提供的荷载组合来使用，若这样的荷载组合在与之联动的程序中无法
运行，将会多么不便？为此，本 Plug-in 将原程序中生成的荷载组合加以分解，
转换为 MIDAS SDS 等程序可使用的基本荷载的组合。

- 减少程序切换时不必要的作业，从而缩短设计时间。
- 减少反复修改作业中产生的人为失误。
- 防止自动生成不必要的荷载，可实现更经济的设计。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 运行 Plug-in 后，在 **Select lcb Type** 中选择要引入的 Design Type |
| 2 | 选择 Design Type 后 **Select Active Type** 窗口被激活，仅显示当前存在荷载组合的 Type。选择要转换为 SDS LCB Type 的 Type 并点击 **Create**，即转换为 SDS 格式 |
| 3 | 将结果传递给 SDS 的两种方法：① 保存到剪贴板后直接粘贴到 SDS；② 下载为 Excel 文件（自动保存至操作系统的下载文件夹）后按需修改 |
| 4 | 将复制的荷载组合粘贴到 SDS 的 Load Combinations 电子表格表单第 1 行的活动单元格，即完成 |

## 参考/限制事项

- **SDS 尚无已启用的 API**，荷载组合只能以复制-粘贴的方式传递
  （原文注明）。本 Plug-in 向 SDS 侧传递数据时走的不是 JSON API，而是经由剪贴板/Excel
  文件。

## 结论（原文）

通过本指南，可利用 Plug-in 制作仅面向 CIVIL 或 GEN 某一程序的荷载组合，
从而缩短设计时间、提高准确度。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format](https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format)
