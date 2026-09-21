# Tendon Profile

> **原文：** [Tendon Profile](https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile)
> **原文编写：** 2025-04-03 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Tendon_Profile.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

将桥梁结构物的预应力束线形（tendon profile）从相对坐标高效转换为绝对坐标的 Plug-in。把 Element 预应力束线形转换为 Straight 预应力束线形，简化工程师处理 2D、3D 模型的工作。

- **支持条件：** 在 2D/3D、Splice、Element 输入类型下可用。
- **限制：** 在 2D、3D 输入类型下均不支持 Straight Length、Transfer Length。2D 输入类型下 Fix、BOT 功能也在支持范围之外。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- **节省时间：** 消除手动导出 DXF、Excel 处理与手动输入，把原本需要数小时的工作缩短到几分钟。
- **减少错误：** 自动化繁琐过程，最大限度减少坐标转换中的人为失误。
- **可定制参数：** X 轴方向、旋转角、Y/Z 偏移可按具体设计要求调整。
- **易用性：** 仅需选择可转换的预应力束线形并应用转换的简洁界面。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 点击 **"Import Tendon Profile List"** |
| 2 | 选择要转换的预应力束线形 |
| 3 | 点击 **"NEW"** 或 **"Modify"** 按钮，自动应用转换 |

点击 **NEW** 按钮时，会以原预应力束名称 + `"_str"` 生成新的预应力束线形。

## 参考/限制事项

- Straight Length, Transfer Length, Fix, BOT 功能在特定条件下不支持。
- 2D 模型中不支持的功能，可能需要改用 3D 输入的替代工作流。

## 相关 JSON API 端点

Plug-in 转换的预应力束线形与 `docs/manual` 的以下端点对应。

- [`/db/TDNA` — Tendon Profile](../../../manual/zh-cn/07_DB_Temperature_Prestress.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile](https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile)
