# Concrete Material Set EN1992-1-1

> **原文：** [Concrete Material Set EN1992-1-1](https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1)
> **原文撰写：** 2025-04-09 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Concrete_Material_Set_EN1992_1_1.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

**EN 1992-1-1** 标准下的混凝土材料特性与时间相关行为（徐变、干燥收缩）计算输入
的自动化 Plug-in。提供可校验设计参数的可视化工具，有助于遵循 Eurocode 规范要求。

## 支持版本

- `MIDAS CIVIL NX 2024 (v1.1) US`
- 适用标准：EN 1992-1-1, EN 1992-2-1

## 主要功能

- **符合标准：** 材料特性与时间相关特性的计算完全遵循 EN 1992-1-1。
- **可视化校验：** 以图形显示徐变系数、干燥收缩应变、应力-应变曲线等关键结果，
  可据此检查正确性。
- **高效性：** 免除了抗压/抗拉强度、弹性模量以及时间相关效应的手动计算。

## 使用方法

| 选项卡 | 说明 |
| --- | --- |
| Concrete | 选择混凝土等级（Concrete Grade）并输入分项系数（partial factor）。选择混凝土应力-应变关系并确认图形。通过 **Additional Information** 查看详细信息 |
| Time-Dependent | 输入时间相关特性。选择要显示的项目 — 徐变系数（Creep coefficients）、干燥收缩应变（Shrinkage strain）、平均抗压强度（Mean compressive strength）、平均抗拉强度（Mean tensile strength）、弹性模量（Elastic modulus）。通过 **Additional Info** 按钮查看详细信息 |

## 参考/限制事项

- **EN 1992-2 支持：** 该设计代码仅可作为输入保存而选用，不执行任何计算。
- **与 MIDAS CIVIL NX 联动：** 计算得到的时间相关特性（如徐变系数）**不会**自动反映
  到模型中，需由用户自行将相应值输入模型。
- **输入校验：** 须确认所输入的值（混凝土龄期、湿度等）符合 EN 1992-1-1 的要求。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1](https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1)
