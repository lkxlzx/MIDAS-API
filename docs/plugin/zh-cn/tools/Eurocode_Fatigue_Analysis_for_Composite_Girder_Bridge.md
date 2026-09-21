# [Eurocode] Fatigue Analysis for Composite Girder Bridge

> **原文：** [Fatigue Analysis for Composite Girder Bridge \[NTC 2018\]](https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section)
> （"Plug-in Item" 列表中的记法为 "[Eurocode] Fatigue Analysis for Composite Girder Bridge"，
> 而文章本身的标题为 "Fatigue Analysis for Composite Girder Bridge [NTC 2018]"。）
> **原文撰写：** 2025-08-01 · **原文最后编辑：** 2026-01-06

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Eurocode_Fatigue_Analysis_for_Composite_Girder_Bridge.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

本 Plug-in 以 **Eurocode** 标准对组合桥梁（composite bridge）执行疲劳分析，
同时支持意大利国家附录 **NTC 2018**。它与 MIDAS Civil NX 联动，对混凝土、钢筋、
钢主梁（steel girder）进行疲劳评估。支持疲劳参数设置、结构数据导入以及疲劳安全性
审查结果的生成。

## 支持版本

- `MIDAS CIVIL NX 2025 (v2.x)`
- 适用标准：
  - `EN 1991-2:2003` — Eurocode 1, Part 2: Traffic loads on bridges
  - `EN 1992-1-1:2004` — Eurocode 2, Part 1-1: General rules and rules for buildings
  - `EN 1992-2:2005` — Eurocode 2, Part 2: Concrete bridges
  - `EN 1993-1-1:2005` — Eurocode 3, Part 1-1: General rules and rules for buildings
  - `EN 1993-1-9:2005` — Eurocode 3, Part 1-9: Fatigue
  - `EN 1993-2:2006` — Eurocode 3, Part 2: Steel bridges
  - `NTC 2018` (Italy) — Norme Tecniche per le Costruzioni（意大利国家附录）

## 主要功能

- 完全遵循 Eurocode 疲劳设计规定与意大利国家附录（NTC 2018）。
- 支持混凝土、钢筋、钢主梁等多项疲劳审查。
- 提供安全系数图表、应力幅图、修正系数汇总等可视化结果。
- 支持**通过 MIDAS Civil API 的智能数据导入**（原文注明）。
- 通过新增/编辑/复制/删除来管理疲劳工况。
- 为工程文档化导出结果。

### 支持的疲劳工况类型

| 分类 | 类型 |
| --- | --- |
| 通用（铁路·道路） | Concrete Shear（无需补强钢筋） · Concrete Shear（需补强钢筋） · Steel Girder（正应力） · Steel Girder（剪应力） |
| 铁路专用 | Concrete Compression（Damage Equivalent Stress Method） · Reinforcing Steel（Damage Equivalent Stress Method – Railway） |
| 道路专用 | Concrete Compression（Simplified Method） · Reinforcing Steel（Damage Equivalent Stress Method – Road） |

### 支持的截面

`COMPOSITE-I`, `COMPOSITE-T`, `STEEL-I (Type-1)`, `Steel Box Type1`, `Steel I Type1`,
`Steel Tub Type1`, `Steel Box Type2`, `Steel I Type2`, `Steel Tub Type2`

## 使用方法（以 Reinforcing Steel 为例的工作流）

| 步骤 | 说明 |
| --- | --- |
| ① 运行 Plug-in | 进入用于疲劳审查与 MIDAS API 联动的仪表板。运行时选择桥梁类型（铁路/道路） |
| ② 连接 MIDAS Civil API | 连接到已打开的 MIDAS Civil NX 模型，自动查询疲劳分析所需的结构数据 |
| ③ 设置全局参数 | 定义部分安全系数（γ）、设计寿命（年数或循环次数） |
| ④ 选择疲劳类型 | 选择审查方法 |
| ⑤ 管理疲劳工况 | 查看已生成的疲劳工况清单，通过编辑/复制/删除管理多种方案 |
| ⑥ 导入 MIDAS Civil NX 结果 | 从 MIDAS Civil 导入按荷载工况、施工阶段为基准的应力、力结果 |
| ⑦ 导入单元 | 从 MIDAS Civil 导入所选择的单元 ID |
| ⑧ 加载数据 | 确认分析对象单元以及相应疲劳条件下的荷载值 |
| ⑨ （可选）输入疲劳专用参数 | 仅在特定疲劳方法中提供的选项卡 |
| ⑩ （可选）计算修正系数 | 按 NTC:2018 计算 λ（lambda）值 |
| ⑪ 执行疲劳分析 | 计算等效应力、损伤指数与疲劳安全性 |
| ⑫ 查看结果 | 依据所选疲劳工况显示应力幅比较、修正系数、疲劳安全系数等 |
| ⑬ 保存结果 | 保存当前分析结果，并导出用于报告与进一步审查 |

## 各疲劳工况的关键输入（摘要）

每种疲劳工况类型都拥有由多个页面（Fatigue Settings → 截面/材料特性 → 修正系数）构成的
专用输入向导。代表性项目：

| 疲劳工况 | 关键输入 | 备注 |
| --- | --- | --- |
| Concrete Compression (Simplified Method) | `fck`、`σc,max`、`σc,min` | σc,max、σc,min 仅压应力（正值）有效 — 若为 0 及以下（拉应力或 0）则不纳入评估 |
| Concrete Shear（无需补强钢筋） | `Vsd,max`、`Vsd,min`（取自含 CB 的混凝土设计荷载组合）、截面特性（`d`、`bw`、`Qn`、`J`、`Vrd,c`） | 仅自动加载存在混凝土受拉区的截面，否则需手动输入（可利用 Section Property Calculator） |
| Concrete Shear（需补强钢筋） | 跨度 `L`、有效高度 `d`、剪力荷载 `Vsd`、抗剪补强钢筋规格、交通条件（道路/铁路各不相同） | 修正系数 λc0~λc4，道路为 `λs = φfat·λs1·λs2·λs3·λs4`，铁路为 `λs = λs1·λs2·λs3·λs4` |
| Steel Girder（正应力） | 跨度 `L`、Detail category（例：160、140、125…）→ 自动设置 `Δσamm`、正应力（从 Civil 导入或手动输入） | 铁路需同时具备 `Δσ1` 与 `Δσ1+2`，道路仅需 `Δσ1` |
| Steel Girder（剪应力） | 跨度 `L`、Detail Category（Shear，默认 100 或 80）→ 自动设置 `Δτamm`、`Δτ1`（仅可导入静力荷载工况） | 移动荷载需预先转换为静力荷载，并需在 MIDAS NX 中启用 "Analysis / Main Control Data / Calculate Equivalent Beam Stresses" 选项 |
| Concrete Compression (Damage Equivalent Stress Method, 铁路) | `fck`、`L`、`σc,max,71`、`σc,perm`（取自 Civil 结果） | 两值均须大于 0 |
| Reinforcing Steel (Damage Equivalent Stress Method – Railway) | `L`、`fck`、钢筋/混凝土弹性模量、有效高度 `d`、开裂状态判定（手动/自动）、钢筋种类、`ΔσRsk`、交通条件 | 开裂自动判定：fb > fctd 时为开裂截面，否则为未开裂截面。未开裂截面需拉应力（Δσ1、Δσ1+2），开裂截面需弯矩 Msd |
| Reinforcing Steel (Damage Equivalent Stress Method – Road) | 与 Railway 版本相似的参数集（跨度、有效高度、材料特性、交通条件等） | 规格相似，采用道路交通条件 |

## 参考/限制事项

- 所有应力/力的输入值都设有有效性校验 — 若不满足相应条件（例如应为压应力的值小于等于
  0），该工况即不纳入评估。
- Steel Girder（剪应力）工况仅可导入静力荷载工况，移动荷载须预先转换为静力荷载。
- 修正系数（λ）虽自动计算，但关闭自动计算后，部分项目可手动重新指定
  （例：Reinforcing Steel – Railway 的 λs1~λs4）。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section](https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section)
