# 6x6 General Spring for Pile Foundation (KR)

> **原文：** [Pile Spring](https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring)
> （在“Plug-in Item”清单中记作“6x6 General Spring for Pile Foundation (KR)”，而该文章
> 自身的标题为“Pile Spring”。）
> **原文创建：** 2024-07-29 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/6x6_General_Spring_for_Pile_Foundation_KR.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

桩基础的建模方法之一，是用 **6x6 General Spring** 来考虑桩基础刚度。本 Plug-in 支持采用韩国公路桥涵设计规范（2010）的位移法计算桩基础刚度。

输入桩参数（桩类型、上段·下段桩、加固）并布置桩后，再输入地层信息，即可查看各桩的特征值、轴向弹簧常数（Kv）与垂直轴向刚度（K1~K4），并可经 Excel 计算书查看各方向（Global X、Y）的弹性弹簧矩阵取值。最终将各方向矩阵组合成 6x6 General Spring 完成计算，并以 General Spring 的形式导入 midas Civil。

- 依据桩参数·地层信息的输入，用位移法计算 6x6 刚度矩阵
- 支持永久、地震时、固有周期计算用矩阵
- 支持的桩类型：灌注桩（Cast-in-place）、PHC 桩、SC 桩、钢管桩（Steel Pipe）、水泥土桩（Soil Cement）
- 支持复合桩（上段·下段桩）、群桩、单桩

## 支持版本

- `MIDAS CIVIL NX 2024 (v1.1) KR`
- 适用标准：韩国公路桥涵设计规范（2010）

## 主要功能

桩基础的建模方法包括固定端模型、虚拟固定端（β）模型、p-y 曲线模型、6x6 general spring 模型等。本 Plug-in 计算 6x6 general spring 方式的刚度矩阵，并在 Midas Civil 中自动生成 general spring。它将传统上依赖 Excel 完成的桩特征值、轴向/横向弹簧刚度计算以及最终矩阵组合过程予以自动化，计算所得取值也可通过 Excel 计算书加以校验。

## 使用方法

要计算矩阵，需在 **Pile Information** 选项卡输入桩参数，在 **Ground Information** 选项卡输入地层参数。

| 步骤 | 选项卡 | 说明 |
| --- | --- | --- |
| 1 | Pile Information | 桩参数输入与布置。支持单桩·群桩·加固截面·复合桩（上段/下段）。可选择桩类型（灌注·PHC·SC·钢管·水泥土）与施工方法（锤击沉桩·振动锤·灌注·大孔径钻孔·预钻孔·钢管水泥土·旋转钻进）。桩布置坐标系遵循韩国公路桥涵设计规范（2010）坐标系，导入 Midas Civil 时转换为 Civil 坐标系 |
| 2 | Ground Information | 选择地层参数以及水平地基反力系数折减系数。支持按土层（黏土·砂性土·砾石）选择并依据道路设计手册自动计算剪切波速。提供因液化层·边坡影响·群桩影响而折减水平地基反力系数（KH）的选项 |
| 3 | Import Data | 查看刚度矩阵结果后，将 6x6 general spring 输入 Midas Civil。Type1/Type2 是把 Plug-in 的荷载坐标系与 Midas Civil 坐标系对齐的设置 |

## 参考/限制事项

- 若不以 6x6 General Spring 而改用虚拟固定端模型，可用 Excel 计算书输出的桩特征值（β）
  确定虚拟固定端位置。
- 复合桩的特征值在用 Excel 计算书计算时，通常按上段桩的截面特性（EI）与单一地基反力系数（KH）
  确定；而本 Plug-in 不仅考虑上段·下段桩参数，还考虑加固截面（外包·填充段）直至多层地层的
  地基反力系数，据此计算桩特征值。
- 轴向弹簧常数（Kv）按韩国公路桥涵设计规范（2010）公式计算，外露桩不施加修正系数。工程中
  常见的复合桩（SC+PHC）一般仅考虑 PHC 桩的截面特性进行计算。混合桩按弹簧串联刚度公式计算
  轴向弹簧常数。
- 垂直轴向弹簧常数（K1~K4）在单一地层（水平地基反力系数恒定）·桩截面特性（EI）恒定条件下的
  通用公式即为公路桥涵设计规范公式，而本 Plug-in 对多层地层·复合桩采用框架分析法计算。单层
  地层·单桩情况下，可得到与公路桥涵设计规范通用公式相同的结果。
- 原文提供示例附件（`pile sample.zip`）。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring](https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring)
