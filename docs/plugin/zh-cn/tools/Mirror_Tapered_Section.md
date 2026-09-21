# Mirror Tapered Section

> **原文：** [Mirror Tapered Section](https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section)
> **原文撰写：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Mirror_Tapered_Section.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

交换既有变截面（Tapered Section）的I端与J端，生成新的变截面。
创建具有相同局部轴的对称镜像变截面。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

若要使coping的局部轴对称，就必须创建I端与J端互换的变截面
（例：coping 1-1 / coping 1-2 — I、J端互换的变截面）。本Plug-in允许在对称形状的
一侧先创建变截面，再交换I、J端形成新的变截面，从而快速生成截面。

## 使用方法

| 字段 | 说明 |
| --- | --- |
| Tapered Section List | 读取当前已输入的变截面列表（可用Refresh按钮刷新）。选择要进行镜像的截面 |
| New Section Name Tag | 输入要附加到新建截面名称上的标签。例：选择A截面时，将以"A_Mirror"为名称生成新的变截面 |
| Generate | 生成新的变截面 |

## 参考/限制事项

Mirror功能仅适用于变截面（Tapered Section）。Tapered Value·User·DB截面均可。

## 相关JSON API Endpoint

本Plug-in生成的变截面，与`docs/manual`中的下列Endpoint对应。

- [`/db/SECT` — Section Properties（含Tapered）](../../../manual/zh-cn/04_DB_Properties.md)

## 结论（原文）

只要是对称形状的变截面，用Mirror Section Plug-in即可轻松创建截面。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section](https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section)
