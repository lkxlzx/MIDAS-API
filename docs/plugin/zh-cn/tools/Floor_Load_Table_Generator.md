# Floor Load Table Generator

> **原文：** [Floor Load Table Generator](https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator)
> **原文撰写：** 2025-08-04 · **原文最后编辑：** 2026-07-27

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Floor_Load_Table_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 以房间（room）与空间为单位，集中管理结构设计所用的重力方向楼面荷载
（Dead Load / Live Load）信息，并同时自动处理结构计算书用的荷载表（PDF）与分析模型
输入。

## 支持版本

`MIDAS GEN NX 2025 (v1.1) KR`

## 主要功能

- 一次设置即可**同时处理 PDF 输出 + 分析模型自动输入**。
- 将荷载条件**保存/读取为配置文件（.json）**，可在各个项目中重复使用。
- 与结构形式无关，可通用适用。
- 消除了按楼层、按空间（装修材料、吊顶、设备条件等）重复进行的手动编写荷载表与重新
  输入的过程，节省工作时间并防止出错。

## 使用方法

| 区域 | 说明 |
| --- | --- |
| Global Setting | 设置项目名、DL/LL Factor（荷载系数）、DL/LL Case（要映射的 Load Case）、公司标志图像等整个项目的公共信息 |
| Category | 输入 Category Name 后用 `+` 按钮创建类别（例：办公室、机房）— 按空间、用途划分的荷载分类单位 |
| Load Group | 在所选择的 Category 内添加细分荷载组。为各组输入面积、DL、LL 等荷载信息 — 结构计算书表格的核心数据 |
| Save / Load | 将设置与荷载表配置保存为本地 `.json` 文件并复用 |
| Export to PDF | 将荷载表输出为结构计算书用 PDF |
| Send to MIDAS | 将输入的 Load Group 信息批量注册到 Gen NX 的 **Define Floor Load** 项目 |

**Load Group 输入项目：**

| 项目 | 说明 |
| --- | --- |
| Name | 材料与构成构件名称（例：混凝土板、普通砂浆） |
| Type | 选择 `thickness`（按厚度计算）或 `load`（直接输入单位面积荷载） |
| Thickness (mm) | 厚度值 — 仅当 Type 为 `thickness` 时激活 |
| Unit Weight (kN/m³) | 材料的单位重量 |
| Load (kN/m²) | Type 为 `thickness` 时按 `Thickness × Unit Weight / 1000` 自动计算，为 `load` 时直接输入 |

## 参考/限制事项

- LL（活荷载）的默认值不会自动计算，通常需手动输入。
- 点击 Export to PDF 时，需在类别选择弹窗中指定输出的对象类别，文件以
  `项目名-YYYY-MM-DD.pdf` 的形式保存。
- 已保存的设置文件会以 `floor-load-settings-YYYY-MM-DD.pdf`（原文标注如此）的名称下载，
  但实际是用于复用的 `.json` 设置文件。

## 相关 JSON API 端点

Plug-in 所引用与记录的数据与 `docs/manual` 的以下端点相对应。

- [`/db/STLD` — Static Load Cases](../../../manual/zh-cn/06_DB_Static_Loads.md) *(DL/LL Case 的映射对象)*
- [`/db/FBLD` — Define Floor Load Type](../../../manual/zh-cn/06_DB_Static_Loads.md#13-dbfbld--define-floor-load-type)
- [`/db/FBLA` — Assign Floor Loads](../../../manual/zh-cn/06_DB_Static_Loads.md#14-dbfbla--assign-floor-loads)

## 结论（原文）

本 Plug-in 是一款面向实际工程应用的 Plug-in，可把结构计算书用荷载表的编写与
产品内的荷载输入整合为单一作业来处理。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator](https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator)
