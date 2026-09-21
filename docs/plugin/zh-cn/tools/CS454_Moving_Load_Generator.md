# CS454 Moving Load Generator

> **原文：** [CS454 Moving Load Generator](https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator)
> **原文创建：** 2026-08-10 · **原文最后编辑：** 2026-08-10

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/CS454_Moving_Load_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

CS 454 移动荷载评估与其说首先是工程工作，不如说是一大段录入工作。Appendix B 的 Table B.1 针对 5 个评估移动荷载等级（assessment live loading level）定义了 22 种车辆模型，且每种车辆的轴重·轴距分别给定。Clause 5.12.1 要求不仅考虑评估目标等级，还要一并涵盖其下的所有等级；车队（convoy）的数量还要再翻倍；并叠加 ALL model 2·消防车（fire engine）组·特殊车辆（special vehicle）。

这些车辆需分别在 Vehicular Load 对话框中连同系数一并设置生成，之后还要以单独的 Moving Load Case 指定名称·车道分配·极限状态 —— 而且每当等级·车道·系数变化，就得重新生成整套。

**CS 454 Moving Load Generator** Plug-in 把这一过程压缩为一次定义。只要在 MIDAS 中预先定义好交通车道（traffic lane），在本 Plug-in 中仅需选择车辆模型与等级，即可通过一次确认步骤在关联的模型中生成车辆与移动荷载工况。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.0.1)`

## 主要功能

- **完全照搬 Appendix B：** 内置 Table B.1 的全部 22 种车辆模型，按官方轴重·轴距·总重原样生成为 MIDAS 的 ALL MODEL 1 子类型。Table B.2 的消防车组因 MIDAS 无对应子类型，按用户自定义车辆（user-defined vehicle）处理。
- **按 Clause 5.12.1 的等级累加：** 勾选一个评估等级即同时包含其下所有等级 —— 因为该条款要求直至评估目标等级的全部车辆模型，且条款注记指出部分 26T 车辆可能比更重的车辆更为不利。此后可把车辆清单实际收窄为起控制作用的轴重排列。
- **一次处理两个可变荷载模型：** ALL model 1 以 Appendix B 的单车生成，ALL model 2 以 Clause 5.17~5.19 的均布荷载（UDL）+ 集中荷载（KEL）组合生成，其取值由 MIDAS 自加载长度（loaded length）算得。可选择单车·车队·两者皆可，并适用 Clause 5.14 的最小纵向间距 1.0m。
- **车道只分配一次：** 交通车道、并排（straddling）车道对、Clause 5.16 的剩余区域车道只需设置一次，即原样应用于所生成的全部工况。特殊车辆同样使用该交通车道，并按 Appendix C 施加前后各 25m 的间距。
- **所有系数集中一处：** Factors 选项卡包含 Vehicular Load·Moving Load Case 对话框所需的全部取值 —— 用于 Table 5.19c K 系数计算的路面类别·交通流类别、动力放大系数、临界轴与其他轴冲击系数、超载、单元数、车速、极限状态、荷载组合。无需再打开 MIDAS 的那两个对话框。
- **同时处理承载能力与正常使用极限状态：** 两者都勾选时，对每种车辆分别按极限状态生成带 `-ULS`·`-SLS` 后缀的工况。名称·说明在 MIDAS 字段长度限制内自动调整，被缩减的内容在 Preview 中报告。
- **复制已验证的条目来写入：** 新条目通过复制模型中已存在的条目生成，故 MIDAS 所用的字段嵌套结构与 enum 标注得以原样保留，仅重写名称·子类型·车辆·车道字段。若模型中没有可复制的条目，则由内置的 CS 454 模板按字段逐项复现一个经 MIDAS 验证的条目。
- **写入前校验：** Preview 列出将要生成的全部车辆与移动荷载工况，并附轴重数据·车道·状态以及作为依据的 CS 454 条款注释；在 **Generate** 确认之前，模型中不反映任何内容。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 CIVIL NX 中打开目标模型并运行 Plug-in。连接信息自动填入，**Validation Check** 会在其他操作之前先报告 PyScript·base URI·MAPI key |
| 2 | 在 **Model** 选项卡点击 **Read model**。模型中已有的交通车道·车辆·移动荷载工况会一并报告，用作 payload 模板的车辆·荷载工况也在此选择。交通车道必须先在 MIDAS 中定义 —— 本 Plug-in 只分配车道，不创建车道 |
| 3 | 在 **Loading** 中选择正常交通（normal）/特殊交通（abnormal），按需勾选 **ALL model 1**·**ALL model 2**，并勾选评估荷载等级。若非只评估特定等级，请保持等级累加（level stacking）开启。不需要的车辆模型取消勾选，并在单车/车队/两者之间选择 |
| 4 | 在 **Lanes** 中为每个生成工况勾选施加车辆的交通车道，设置 Clause 5.16 所要求的剩余区域车道，并添加并排车道对。属特殊交通时，设置特殊车辆种类与所要生成的名称 |
| 5 | 同样在 **Lanes** 中，用子类型·Table B.1 引用字符·等级·特殊车辆·序号记号构造车辆·荷载工况的名称模式。选择对模型中已存在名称的处理方式（编号后并存/覆盖/跳过） |
| 6 | 在 **Factors** 中设置路面·交通流类别、动力放大系数·轴冲击系数、超载、单元数、车速、设计组合（极限状态、Combination 1/2/3） |
| 7 | 复核 **Preview** — 列出将要生成的所有车辆及其引用名·等级·总重·轴重·轴距，以及所有移动荷载工况及其车辆·特殊车辆·车道·状态。同时显示 CS 454 依据条款；若存在错误，则在解决之前阻止生成 |
| 8 | **Generate** 选项卡 — **Preview payload** 在不写入的情况下生成实际发送的 JSON，**Write to model** 则予以提交。日志中报告写入/跳过/改名结果及其后的模型状态；若有遗漏条目，可在 **Diagnostics** 选项卡查看各 MAPI 端点的响应 |

## 参考/限制事项

- 交通车道必须先在 MIDAS 中定义 —— 本 Plug-in 只分配车道，不创建车道。
- 新条目以复制模型中已存在条目的方式生成；无可复制条目时使用内置的 CS 454 模板。
- 名称·说明超出 MIDAS 字段长度限制时，自动缩减后写入，缩减的内容在 Preview 中报告。

## 相关 JSON API 端点

Plug-in 明确说明会生成车辆与移动荷载工况，二者与 `docs/manual` 中的以下端点对应。

- [`/db/MVHL` — Vehicles](../../../manual/zh-cn/08_DB_Moving_Loads.md)
- [`/db/MVLD` — Moving Load Cases](../../../manual/zh-cn/08_DB_Moving_Loads.md)

## 结论（原文）

CS 454 Moving Load Generator 消除了 DMRB 移动荷载评估中最缓慢·最机械的部分 —— 把 Appendix B 的轴重数据誊写到 Vehicular Load 对话框、逐一顾及 Clause 5.12.1 随评估目标等级一并要求的下级等级、为每种车辆·每个车队·每种极限状态手工创建 Moving Load Case。车道只需定义一次并经 Preview 确认，此后每当等级·车道·系数·范围变化，几秒即可重新生成整套，使工程师的时间用于评估本身，而非数据录入。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator](https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator)
