# Tunnel Lining Generator

> **原文：** [Tunnel Lining Model](https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model)
> （"Plug-in Item" 列表中标注为 "Tunnel Lining Generator"，而文章本身的标题为 "Tunnel
> Lining Model"。）
> **原文编写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Tunnel_Lining_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

生成隧道衬砌（tunnel lining）分析用 midas Civil 模型的 Plug-in。以从 DXF 文件导入的单元为基准创建新节点，计算地基系数（subgrade modulus）并以只压弹性连接（elastic link, compression only）相连。弹簧系数按混凝土衬砌详细设计规范（韩国道路公社 2016）采用 AFTES 与美国的公式。

- 生成衬砌分析用模型
- 以地基系数与单元尺寸为基准自动计算、生成弹簧

## 支持版本

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 适用标准：Korea Design Standard (KDS)

## 主要功能

隧道衬砌分析中，通常先把 DXF 文件（衬砌中心线）导入 midas Civil，再由地基系数计算弹簧刚度。本 Plug-in 自动在各单元 1m 距离处生成节点，并用考虑泊松比的 AFTES 公式自动计算地基系数。端部边界条件支持 Hinge 与 Spring 模型，其中 Spring 模型考虑单元的截面尺寸计算弹簧刚度。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 导入 DXF | 将包含隧道衬砌中心线的 DXF 文件导入 midas Civil。若单元未指定截面，端部边界条件必须以 Hinge 生成（计算弹簧刚度需要单元宽度） |
| Selected Elements | 在 MIDAS Civil 中选择要生成衬砌模型的单元，然后点击 Plug-in 读入单元 |
| Subgrade Modulus | 输入计算弹簧刚度所需的地基系数、泊松比，用 AFTES 公式计算 Ks |
| End Boundary Condition | Hinge：在端部节点生成 Hinge 边界条件（与是否指定截面无关）。Spring：沿衬砌轴线生成只压弹性连接（弹簧刚度按单元宽度计算） |
| Create | 生成衬砌模型 — 考虑各单元的法线方向向量，在 1m 距离处生成节点，并以只压弹性连接将该节点与原有节点相连 |

## 参考/限制事项

端部弹簧边界条件仅在单元已指定截面时才能计算。

## 相关 JSON API 端点

Plug-in 生成的节点、弹性连接与 `docs/manual` 的以下端点对应。

- [`/db/NODE` — Node](../../../manual/zh-cn/03_DB_Node_Element.md)
- [`/db/ELNK` — Elastic Link](../../../manual/zh-cn/05_DB_Boundary.md)

## 结论（原文）

借助本 Plug-in 可生成包含边界条件的隧道衬砌模型文件。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model](https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model)
