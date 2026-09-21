# Easy Capture Generator

> **原文：** [Easy Capture Generator](https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator)
> （"Plug-in Item" 列表中还把 "Image Capture Generator" 作为同一 URL 的别名
> 一并列出。）
> **原文撰写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Easy_Capture_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 将打印（输出）设置以数据库（DB）形式保存，从而可以轻松地输出。
一个 DB 中可保存多个设置，并可将配置好的内容按多种格式输出。

- 以 DB 形式保存打印设置
- 在一个 DB 中轻松保存与管理多个设置
- 支持多重打印

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

以往每次制作账单（invoice）或报告时都必须重复输入打印设置，一旦建模发生变化或输出
结果不满意，重新作业又要花费大量时间。使用本 Plug-in 后，用户可把配置好的设置
保存起来，即使建模发生变化也无需重新配置即可继续使用。此外还可以把相似的设置归为
一组并应用到多个荷载工况上，从而加快作业速度、统一输出并减少用户失误。

- 尽量减少重复的设置输入，缩短作业时间
- 支持多重输出，节省不必要的打印时间
- 使用预先配置好的输入值，减少用户失误

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 DB 选项卡中选择要保存的 DB。Components 可多选，其余选项仅可单选 |
| 2 | 点击 **Save** 按钮保存，并在 File List Work Tree 中确认输入信息 |
| 3 | 必要时追加选择要保存的 DB |
| 4 | DB 信息保存完成后，切换到 Type of Display 选项卡 |
| 5 | 以与 DB 选项卡相同的方式选择选项 |
| 6 | 点击保存按钮 |
| 7 | 切换到 View 选项卡 |
| 8 | 选择并保存所需的设置。按 Active Type 作如下设置 |
| 9 | **Active All**：输出整个模型 |
| 10 | **Active by Node/Element**：仅输出模型中所选的部分。先在模型中选择要输出的单元，再在 Plug-in 中选择 **Active by Node/Element** |
| 11 | **Active Identity**：输出 Structure Group 中定义的部分。从列表中选择要输出的组 |
| 12 | DB/Type of Display/View 信息保存完成后，可用 **Download** 按钮以 JSON 格式保存 |
| 13 | 切换到 Print 选项卡，在 File List 中确认已保存的 DB |
| 14 | 运行 Plug-in 后，用户最近输入的信息保存在 Current 中。若要使用此前保存的 DB，用 **Add File** 按钮调取文件 |
| 15 | 选择要输出的文件并点击 **Select Load Case** 按钮 |
| 16 | 打开 Load Case 选择窗口后，选择要输出的 Load Case（可多选） |
| 17 | 若要保存所选的 Load Case，用 **Download** 按钮以 JSON 格式保存。把已保存的 DB 调入其他模型时，不存在的 Load Case 名称不会输出 |
| 18 | Load Case 输入完成后，用保存按钮保存 |
| 19 | 在 Plug-in 右侧的 Print File Work Tree 中确认已保存的文件 |
| 20 | 用 **Print Size** 按钮输入输出尺寸（按用户计算机环境以像素为单位进行调整） |
| 21 | 输入尺寸后点击打印（print）按钮 |

## 相关 JSON API 端点

Plug-in 所处理的 View/Type of Display/Active 设置与 `docs/manual` 的以下端点
相对应。

- [`/view/CAPTURE` — Capture](../../../manual/zh-cn/16_VIEW.md)
- [`/view/DISPLAY` — Display](../../../manual/zh-cn/16_VIEW.md)
- [`/view/ACTIVE` — Active](../../../manual/zh-cn/16_VIEW.md)

## 结论（原文）

通过本指南，可在结构建模项目中轻松保存与管理打印相关设置，并快速输出所需的
信息。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator](https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator)
