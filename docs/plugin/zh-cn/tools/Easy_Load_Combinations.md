# Easy Load Combinations

> **原文：** [Easy Load Combinations](https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations)
> **原文撰写：** 2025-04-09 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Easy_Load_Combinations.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 简化了在 MIDAS CIVIL NX 中生成荷载组合的过程。仅需几次点击即可引入
荷载工况、施加组合系数，并把组合后的荷载工况直接传递到模型，从而节省时间、减少错误。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- **自动引入：** 依据 MIDAS 模型文件自动引入并更新荷载工况。
- **便捷组合：** 仅需选择荷载工况并施加系数，即可快速生成新的荷载组合。
- **一键应用：** 单击即可将组合后的荷载工况直接传递到模型。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 打开 Plug-in 时，自动导入 MIDAS CIVIL NX 文件中的所有荷载工况 |
| 2 | 在 Plug-in 界面的列表中选择所需的荷载工况，并按设计要求分别输入组合系数 |
| 3 | 点击 **Add** 时，以所输入的参数生成新的荷载组合集；点击 **Update/Overwrite** 时将荷载组合传递至 CIVIL NX |
| 4 | 可在产品的 Result > Load Combination 中确认数据是否更新成功 |

## 参考/限制事项

- 生成荷载组合之前，须确认导入的所有荷载工况与 MIDAS CIVIL NX 模型一致。
- 对于 Eurocode 移动荷载，为避免兼容性问题，须使用 v1.1.0 及以上版本。
- 在应用于模型之前，须再次确认组合系数的准确性。

## 相关 JSON API 端点

Plug-in 所处理的荷载组合与 `docs/manual` 的以下端点相对应。

- [`/db/LCOM-GEN` — Load Combinations (General)](../../../manual/zh-cn/13_DB_Load_Combinations.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations](https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations)
