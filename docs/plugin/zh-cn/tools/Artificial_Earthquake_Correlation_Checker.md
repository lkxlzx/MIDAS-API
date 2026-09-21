# Artificial Earthquake Correlation Checker

> **原文：** [Artificial Earthquake Correlation](https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker)
> **原文创建：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Artificial_Earthquake_Correlation_Checker.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

按 KDS 标准，人工地震波之间的相关系数不得大于 0.16。本 Plug-in 计算 midas Civil 中人工地震波（Time History Function）之间的相关系数。

## 支持版本

- `MIDAS GEN NX 2026 (v1.1)`
- 适用标准：Korean Standard (KDS)

## 主要功能

通常由时间-加速度数据计算相关系数时要借助 Excel。本 Plug-in 只需选择 Time History Function 即可快速复核相关系数，并可以表格形式查看结果。

## 使用方法

| 字段 | 说明 | 选项·默认值 |
| --- | --- | --- |
| Time History Functions | 读取当前已载入的 Time History Function 清单（可用 **Refresh** 按钮刷新）。选择需要复核相关系数的 Time History Function | — |
| Correlation Coefficient Target | 输入相关系数的上限值 | 默认值 `0.16` |
| Calculate | 点击后计算相关系数。结果在右下角表格中查看 | — |

结果表格的颜色/标注判据：

| 标注 | 含义 |
| --- | --- |
| 蓝色取值 | 相关系数小于限值 |
| 红色取值 | 相关系数大于限值 |
| `NG` | 各 Time History Function 的数据个数不一致，无法计算相关系数 |

## 参考/限制事项

人工地震波的相关系数按 KDS 17 10 00（抗震设计 通则）标准计算。

## 相关 JSON API 端点

Plug-in 所针对的 Civil 中的“Time History Functions”，与 `docs/manual` 中的以下端点对应。

- [`/db/THFC` — Time History Functions](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)

## 结论（原文）

由 Time History Function 数据计算相关系数。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker](https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker)
