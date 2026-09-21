# P-Y Curve Generator

> **原文：** [P-Y Curve Generator](https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator)
> **原文撰写：** 2025-11-20 · **原文最后编辑：** 2025-12-18

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/P_Y_Curve_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

基于API RP2A、Matlock(1970)、Reese et al.(1974/1975)等国际通用的公式以及多种岩石模型，
生成桩基础的水平土抗力（P-Y）曲线的Plug-in。与MIDAS Civil NX/Gen无缝联动，
输出随深度变化的非线性弹簧，支持详细的地基-结构相互作用建模。

评估多层地基剖面并自动探测层间过渡，采用严密的岩土工程公式、等效深度修正与按土类的
抗力模型，计算每个桩节点的P-Y曲线。可快速生成、可视化并导出用于结构分析工作流的弹簧数据。

## 支持版本

`MIDAS CIVIL NX 2025 (v2.x)`

## 支持的P-Y模型

| 类别 | 模型 |
| --- | --- |
| 黏土（Clay） | Soft Clay — API RP2A(Matlock 1970) · Stiff Clay — Reese et al.(1975)，无地下水（有地下水的版本尚未实现，仅自动反映重度） |
| 砂（Sand） | API Sand · Reese et al.(1974) Sand |
| 岩石（Rock） | Weak Rock — Reese(1997) · Strong Rock — Tunner(2006)，Vuggy Limestone |

### 支持的桩类型

Pipe, Solid Round, H-Section, Box, Solid Rectangle

## 理论实现要点

- **多层地基与等效深度（Equivalent Depth, Georgiadis Method）：** 当沿桩长存在不同土层时，
  把上覆层的累计抗力转换为下一层的等效起始深度，使各层的P-Y行为从正确的抗力状态开始：
  `∫[0, h_eq,i] p_i(z) dz = f0_i`
- **节点影响区与弹簧组装：** 每个桩节点具有影响区（influence zone），水平反力按
  `P(y) = ∫[z1, z2] p(y,z) dz`计算，以反映土层变化·直径变化·随深度的非线性刚度变化。
  - 首个节点：从地表至中间深度
  - 中间节点：相邻节点之间的中间深度
  - 末尾节点：从前一中间深度至桩端
- **非圆形截面的有效直径：** Reese et al.(1974/1975)、Matlock(1970)、API RP2A等经典公式
  源自圆形桩试验，并以直径D为基准归一化。H型钢·箱形·矩形截面等非圆形截面，转换为与实际
  截面具有相同与土接触周长的等效圆形桩后应用：
  `D_eff = P_shape / π`（P_shape = 实际桩截面周长）
- **群桩与斜桩（Group and Battered Pile）：**
  - **群桩效应（Group Effect）：** 以较小间距将桩成群设置时，各单桩周围的抗力区相互重叠，
    在同一水平位移下承担的荷载小于单桩。p-multiplier受桩间距以及桩在群中位置的影响，
    前排桩通常比后排桩具有更大的p-multiplier。设计实务中常以群桩整体的平均p-multiplier
    作为代表值。Mokwa and Duncan(2001)提出了按桩间距·布置估算p-multiplier的设计图表。
  - **斜桩（Battered Pile）：** 根据Kubo(1965)、Awoshika & Reese(1971)的研究，
    引入倾角（正/负）后发挥的土抗力相对竖直桩增大或减小，该比率以试验观测为依据。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1. 输入土层 | 水中（submerged）重度/有效重度不直接输入 — 在Automatic Groundwater Level模式下，用用户输入的饱和重度减去水的重度，自动反映浮力效应。以地表（Ground Level）为基准，地表以下的深度输入正数、地表以上的高度输入负数（按钻孔数据的惯例）。地下水位高于地表时输入负数 |
| 2. 输入桩形状 | 可在MIDAS产品中选择单元，用"Import from MIDAS Product"直接导入。若模型中桩群的布置相对全局坐标系发生了旋转，则指定旋转角，以正确定义地基反应方向。可用右侧面板的"Group Effect Calculator"自动计算p-multiplier或手工输入（X·Y方向可独立指定，并可像Excel一样通过拖选范围批量输入） |
| 3. Pile-Soil Assignment | 生成P-Y曲线case时，指定先前定义的桩信息·地基剖面·桩shift值。必须单击**"Save and Generate Non-Linear Spring"**才会生成P-Y曲线 |
| 4. 结果审查与建模生成 | 审查生成的边界条件计算结果，单击**"Generate Boundary Condition Modelling"**后，该边界条件将直接在MIDAS产品中生成 |

## 验证（Verification）

原文中包含验证章节，把Plug-in生成的P-Y曲线与外部参考程序的结果以及手算进行了定量比较 —
以由6个土层（Soft Clay → Sand → Sand → Stiff Clay → Weak Rock → Strong Rock）组成的
示例地基剖面、长度15.0m·直径1.20m的圆形桩为基准，详细给出了在含层间过渡的特定节点
（例：Node 8130，桩身深度9.0~10.0m）处，对10个细分点用梯形积分法计算P-Y积分过程，
从而得出`P = -1607.42 kN`（对应位移-1.255879 m）的示例。本仓库文档仅概述方法，
完整数值示例请参见原文。

## 主要功能

- 为多层地基系统生成按深度的P-Y弹簧
- 以等效深度积分准确反映层间过渡
- 支持现代桩基设计所用的大部分主要土抗力模型
- 提供P-Y曲线、地基剖面图与分层汇总
- 与MIDAS Civil/GEN NX非线性边界条件完全兼容
- 支持导出弹簧力-位移表

## 相关JSON API Endpoint

Plug-in说明由"Generate Boundary Condition Modelling"生成的非线性弹簧边界条件，
就其性质而言很可能与`docs/manual`中的下列Endpoint相关。但原文未明确指出究竟使用哪个
Endpoint（General Link还是Point Spring等），因此仅作为参考列出链接。

- [`/db/MLFC` — Force-Deformation Function](../../../manual/zh-cn/05_DB_Boundary.md) *（对应关系未确认）*
- [`/db/NLNK` — General Link](../../../manual/zh-cn/05_DB_Boundary.md) *（对应关系未确认）*

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator](https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator)
