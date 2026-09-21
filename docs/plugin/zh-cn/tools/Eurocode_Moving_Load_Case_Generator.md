# Eurocode Moving Load Case Generator

> **原文：** [Eurocode Moving Load Case Generator](https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator)
> **原文撰写：** 2026-08-18 · **原文最后编辑：** 2026-08-18

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Eurocode_Moving_Load_Case_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

EN 1991-2 的交通荷载，与其说是工程作业，不如说首先是一项漫长的录入作业。
仅 Load Model 1 就需按每条名义车道取不同值的 tandem system 与 UDL，并各自配合相应的
修正系数；Load Model 2 需另设单轴荷载，Load Model 3 是一组每次仅可同时施加一种的
特殊车辆；此外还不包含 cl 4.6 的疲劳荷载模型与 Section 6 的铁路荷载模型。以上所有荷载
都需在 MIDAS 中先建为车辆（vehicle），再重新连接为具有正确车道、名义车道编号与系数的
移动荷载工况，而且只要有一条车道变化就得全部重新制作。**Eurocode Moving
Load Generator** 代替了这项作业 — 它从打开的模型中读取交通车道，以 Table 4.4a 的交通
荷载群（traffic load group）为出发点，生成由此派生的车辆与移动荷载工况。

## 支持版本

`MIDAS CIVIL NX 2026 (v2.2)` — Plug-in 版本 `1.0.0`

## 主要功能

- **以荷载群作为一级输入：** 将 EN 1991-2 Table 4.4a 的 gr1a·gr1b·gr3·gr4·gr5 作为一级
  选择对象，并按 cl 4.5.1 处理为互斥 — 选定荷载群后，其所包含的荷载模型会一并勾选，
  两者不会出现不一致。
- **覆盖 EN 1991-2 全部范围：** Section 4 的 Load Model 1~4 与人行道荷载、cl 4.6 的
  疲劳荷载模型 FLM1~4、Section 6 的 LM71、SW/0、SW/2、HSLM-A、HSLM-B — 道路、疲劳、铁路
  模型均可一次性生成或分别生成。
- **将国家决定变量（NDP）作为系数处理：** MIDAS 的移动荷载代码只有 EUROCODE 这一个条目
  （并非按国家排列的清单），因此唯一的分支只有 LM3 的特殊车辆组（UK NA SV/SOV 或
  EN Annex A 模型）— 其余修正系数均为普通数值，故任何国家附录都仅通过编辑系数即可表达，
  常见取值则提供预设。
- **可生成 characteristic 与 frequent 两种取值：** 将 EN 1990 Table A2.1 的 ψ 系数写入
  车辆，并按代表值（frequent/characteristic/两者）生成工况 — 属于何种取值会标注在荷载
  工况名称中。
- **名义车道编号仅赋予一次：** 为模型中的每条交通车道指定角色（道路车道/人行道/剩余区域/
  铁路）后，道路车道按 cl 4.2.3 获得名义车道编号，该编号决定 Table 4.2 的行与修正系数 —
  在 Lanes 选项卡中可在记录之前确认结果值。
- **将铁路车道与道路车道分离：** MIDAS 在 Eurocode 下把铁路车道与道路车道以同一对话框
  存入同一清单、无从区分，故以 Track 角色加以区分 — 未指定车道的铁路工况不会被静默地以
  空载记录，而是拒绝生成。
- **连同铁路组合数据一并记录：** 将 cl 6.8.1 Table 6.11 的按荷载轨道数的 ψ1 系数与多重
  加载系数写入 MIDAS Railway Bridge Data（ψ0 因 MIDAS 在生成荷载组合时固定取 0.8，故无
  需另行输入）。
- **明示无法生成的项目：** 对没有标准轴重组合的疲劳荷载模型 5（FLM5），以及本质上是归入
  静力荷载的 cl 4.4 制动力、加速力与离心力的 gr2，不静默省略，而是明示无法生成的原因。
- **写入前预览与 dry run：** 将所有车辆与工况连同相关条文一并列出，并可用 Dry run
  在不触及模型的情况下预先构造实际将传输的 payload。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 CIVIL NX 中打开桥梁模型并运行 Plug-in — 连接信息自动设置 |
| 2 | 在 **Model** 选项卡中执行 Read model — 查看移动荷载代码、交通车道以及已有的车辆与移动荷载工况。若代码不是 Eurocode，需在 MIDAS 的 Load > Moving Load > Moving Load Code 中设置后重新读取 |
| 3 | 在 **Load models** 选项卡中选择适用的 EN 1991-2 条目并勾选交通荷载群 — 荷载群所必需的下属模型显示为锁定状态，其余可解除（例如无人行道荷载的桥梁可仅解除该项）。也提供按单个荷载模型生成工况的选项，但默认关闭 |
| 4 | 在 **Lanes** 选项卡为所有车道赋予角色（道路车道/人行道/剩余区域/铁路），并决定剩余区域是否施加荷载以及是否启用 MIDAS 优化（自动选择加载哪条车道）。在下方表格中确认施加修正系数后各车道的 LM1 取值 |
| 5 | 设置命名规则 — 组合荷载模型、MIDAS 子类型、荷载群、代表值与序号，生成可读的名称，同名已有工况的处理方式也在此决定 |
| 6 | 在 **Factors** 选项卡选择国家附录（NDP）预设后，查看/修改按名义车道的 tandem 与 UDL 修正系数、剩余区域系数、LM2 用 betaQ、LM3 特殊车辆组、ψ 组合系数、铁路 classification factor 以及 Railway Bridge Data。勾选要生成的代表值（frequent/characteristic/两者） |
| 7 | 审阅 Preview — 连同相关的 EN 1991-2 条文确认将要生成的所有车辆与移动荷载工况，问题项目与需确认的项目被加以区分显示 |
| 8 | 在 **Generate** 选项卡中选择 Dry run（不传输、仅构造 payload）或 Write to model（实际记录）。日志会保留全部记录内容，以内置 payload 替代生成的项目另行标示 |

## 参考/限制事项

- 疲劳荷载模型 5（FLM5）因无标准轴重组合而不会生成。
- gr2（制动力、加速力、离心力）归类为静力荷载，不作为移动荷载工况生成。
- 铁路工况必须指定车道（Track 角色），未指定时将被拒绝生成。
- ψ0 由 MIDAS 在生成荷载组合时自动施加 0.8，故 Plug-in 不另行接收输入。
- 对移动荷载代码不是 Eurocode 的模型拒绝写入。

## 相关 JSON API 端点

Plug-in 生成的车辆与移动荷载工况与 `docs/manual` 的以下端点相对应。

- [`/db/MVHL` — Vehicles](../../../manual/zh-cn/08_DB_Moving_Loads.md)
- [`/db/MVLDeu` — Moving Load Cases – Eurocode](../../../manual/zh-cn/08_DB_Moving_Loads.md)

## 结论（原文）

Eurocode Moving Load Generator 消除了 EN 1991-2 评估中缓慢而机械的部分 — 为每个
荷载模型与每种特殊车辆制作车辆，并为各自创建具备车道、名义车道编号、修正系数与代表值
的移动荷载工况 — 留下来的才是工程判断：结构物应承受的交通荷载群、所采用的国家附录取值
以及结果的含义 — 所有将生成的项目，都会在写入模型之前连同依据条文一并以清单形式呈现。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator](https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator)
