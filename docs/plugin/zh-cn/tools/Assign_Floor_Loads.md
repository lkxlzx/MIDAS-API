# Assign Floor Loads

> **原文：** [Assign Floor Loads](https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads)
> **原文创建：** 2025-11-19 · **原文最后编辑：** 2025-11-19

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Assign_Floor_Loads.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 用于快速·直观地指定楼面荷载（Floor Load）。不必逐个手工选择节点，也不必依赖基于文本的层高输入，可直接在模型中拖拽选择构件并批量施加荷载。施加成功与失败的区域既可经图形预览查看，也可通过表格信息核对。

## 支持版本

`MIDAS GEN NX 2026 (v1.1) US`

## 主要功能

- **节省时间：** 消除了手工选择节点、多节点文本输入、重复施加荷载等步骤，把原本耗时数小时的工作缩减到几分钟。
- **减少错误：** 即使误点击节点或几何形状复杂，也可通过图形与表格信息校验结果，从而减少人为失误。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 GEN NX 中选择要指定楼面荷载的单元（Elements） |
| 2 | 选择荷载所要施加到的 **Plane Type** |
| 3 | 选择 **Floor Load**、**Select Load Group** 等必要项后点击 **Apply** |
| Refresh | 点击后刷新建筑几何·Floor Load·Select Load Group |
| 结果查看 | 可在 Results 选项卡以图形方式复核荷载施加位置。也可用表格形式查看施加成功/失败区域的节点编号 |

## 参考/限制事项

- 本 Plug-in 始终以 **“Allow Polygon Type Unit Area”** 启用的状态运行。
- 不支持 **“Unmodeled Sub-Beam”** 与 **“Convert to Beam Load types”**。

## 相关 JSON API 端点

Plug-in 所处理的“Floor Load”指定，与 `docs/manual` 中的以下端点对应。

- [`/db/FBLD` — Define Floor Load Type](../../../manual/zh-cn/06_DB_Static_Loads.md)
- [`/db/FBLA` — Assign Floor Loads](../../../manual/zh-cn/06_DB_Static_Loads.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads](https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads)
