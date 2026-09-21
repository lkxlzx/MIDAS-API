# ScaleUp 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/07_ScaleUp.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据视频（`docs/plugin_cases/videos/07_ScaleUp.mp4`，30fps，3840×2160，约 189 秒）以 8 秒间隔
> 抓取帧（共 24 张）后逐帧目视分析 + 画面上方大字幕（阶段标题）与下方气泡字幕作为
> 依据编写。与原文文章（`docs/plugin_cases/articles/07_ScaleUp.md`）的四大功能说明交叉
> 核对过。与 #4（AutoGenerationCmFactor）的目的（计算 Cm 修正系数）类似，但 ScaleUp 是 MIDAS
> 官方 "Apps"（Structure Analysis 面板 > Apps）平台上注册的完成型向导（Wizard）UI，
> **不止于计算 Cm，而是包含自动生成荷载组合·输出报告在内**的全过程，范围更广。尤其 "GEN NX DATA MAP"
> 画面上以文本形式原样显示了实际调用的 5 种 API，API 映射依据非常强。

## 1. 概述

**ScaleUp（Scale Up SE）** 是按抗震设计基准自动计算反应谱分析的修正系数 Cm，并在 GEN NX 中
自动生成设计用荷载组合的 Plug-in。Cm 计算所需的分析结果与荷载工况信息从 GEN NX 自动读取，
从确认分析结果 → 计算 Cm → 生成设计用荷载组合 → 输出报告以一个连续的 5 步向导流程完成。

## 2. 问题定义

- 按方向比较等效静力分析与反应谱分析的基底剪力来计算修正系数 Cm 的流程，
  是在多张结果表与计算表之间来回的重复作业。
- 即使算出 Cm，之后仍需把套用该系数的设计用荷载组合再次手动输入 GEN NX
  这一额外步骤。

## 3. 目标用户

- 包括首次接触此作业流程的用户—原文四大功能的第 1 项即为"面向首次使用者的分步引导"，
  是明显顾及新用户上手的设计。
- 需在反应谱分析结果上套用 Cm 修正系数以生成设计用荷载组合的结构设计者。

## 4. 核心概念 / 差异化点

- **顶部状态提示栏 + 脉动（pulse）强调效果**：常驻显示 5 步（①输入设计条件 ②确认模型数据 ③算出
  Cm ④生成荷载组合 ⑤报告）的进度状态，并对接下来应输入的字段以蓝色边框脉动强调—
  让初次使用者也不会迷茫"下一步该做什么"。
- **收藏夹（抗侧力体系）管理**：将包含反应修正系数（R）·超强系数（Ω0）·位移放大系数（Cd）等的
  "抗侧力体系"以搜索·收藏方式保存并可重复使用—不必每次翻查代码表填入 R/Ω0/Cd
  数值。
- **实时反应谱可视化**：按输入的设计条件（地震分区、场地等级、重要性等）即时
  按区间（短周期/过渡/长周期）绘制反应谱图线，并可用鼠标查询特定周期（T）处的 Sa 数值。
- **以 GEN NX 数据映射实现来源透明化**：按一下 "读取 GEN NX 数据" 按钮即自动取得 Cm 计算所需的
  5 个条目（层高、RS 工况、特征值结果、有效重量、层剪力），并在"模型数据来源与原表"
  画面中公开**各条目究竟由哪个 API 取得**（例：`GET db/STOR`、
  `GET db/SPLC`、`POST TABLE - EIGENVALUEMODE`）及其原始响应表—防止自动化黑箱化的设计。
- **从计算 Cm 到生成荷载组合无缝衔接的连续流程**：将算出的 Cm 原样传给第 4 步（生成荷载组合），
  按 RC/Steel/SRC 等设计基准在 GEN NX 的 `Load Combinations` 窗口中实际
  生成荷载组合，并可在同一画面选择特殊地震荷载·垂直地震力组合·正交效应考虑等抗震设计附加选项。
- **输出计算依据报告**：将全过程（设计条件、GEN NX 模型数据、Cm 计算过程、设计
  反应谱）汇总为 "Scale Up 计算报告"，即时以 Web/PDF 输出。

## 5. 工作流

### Step 0 — 在 Apps 平台中执行

- 在 MIDAS GEN NX 右侧 `Tree Menu 2 > Apps` 中选择 "Scale Up SE" 应用 → 点击 "Run" → 执行
  插件。
- 执行前确认提示："请在 GEN NX API Settings 中确认 API Connection 状态为 Connect 后再按 Run
  按钮"、"请在已生成反应谱分析与特征值分析结果的模型中执行。"

### Step 1 — 输入设计条件

- 输入地震分区、直接输入图谱值 S、场地类型、重要性系数 Ie、抗侧力体系（R/Ω0/Cd 自动显示）。
- 可将常用的抗侧力体系以收藏夹保存·调出（收藏夹管理模态框：搜索、添加、
  移除）。
- 提供近似周期计算公式（例："4. 钢筋混凝土剪力墙结构及其他框架"，Ta = 0.0488·hn^0.75）与 KDS
  41 17 00 4.2.2 (2)·(3) 条款复选框（"基岩深度超过 20m 且 Vs≥360 → Fv×0.8"、"S5 且深度
  不明 → Fa,Fv×1.1"）—与 #4 AutoGenerationCmFactor 共用相同的 KDS 41 17 00 逻辑。
- 随输入实时以表格与图线计算设计反应谱（SDS、SD1、S、To、Ts、R/Ie 等），
  并可通过提示框比较特定周期的 Sa 数值（弹性 Sa 与 ELF 有效值 Cs）。

### Step 2 — 确认模型数据（联动 GEN NX 数据）

- 用 "Gen NX 数据读取" 按钮自动读取 Cm 计算所需的信息（也可手动输入）。
- 读取的条目：楼层列表/hn、RS 工况/基准周期、Td/相应方向 Wx·Wy（有效地震重量）、有效重量
  汇总（质量 API 失败时可改为手动输入）、沉降工况/自动计算。
- 可在 **"模型数据来源与原表"** 弹窗中直接查阅 5 个读取条目各自的来源 API 与原始响应表
  （见 6 节）—需要确认时可验证联动的原始数据。
- 最终在画面上汇总显示 X/Y 方向 RS 工况、Td,x/Td,y、有效地震重量 Wx/Wy、可信范围（1F~地下 5F 等）。

### Step 3 — 算出 Cm

- 点击 "计算 Cm" 按钮 → 执行按方向的基底剪力基准比较（确认静力计算结果 / 计算 Cm）。
- 结果：Cm,x = 1.19（通常需要）、Cm,y = 1.034（通常需要）—以表格同时给出各方向的 Vs（等效静力）·0.85Vs（最小
  基准）·Vt（反应谱）·与基准的比值。
- 提示文字："层间位移不适用 Cm。（KDS 41 17 00 7.3.3.5(2)：EL 频率控制请维持缩放前的值）"（⚠️ 因画面截图
  分辨率而有完全无法判读的部分，但从主旨看应为提示 Cm 不适用于层间位移验算的 KDS 条款）。

### Step 4 — 生成荷载组合

- 选择结构设计分类（例：RC · KDS 41 20 : 2022）及生成方式（例："添加到现有组合"）。
- 添加 Envelope 组合复选框、已自动反映 X/Y 方向各自应用 Factor（Cm,x=1.19、Cm,y=1.034）的
  RX(RS)/RY(RS) 组合预览。
- 抗震设计附加选项：生成特殊地震荷载组合（使用 DCM SDS 时批量生成特殊地震荷载组合）、
  生成垂直地震力组合、考虑正交效应（对所选 RX/RY 工况应用 100:30 或 SRSS 正交效应组合）。
- 点击"确认后 GEN NX ..."按钮 → 确认请求详情（API 请求详情）后执行 "Gen NX 生成荷载组合"
  → 在 GEN NX 的 `Load Combinations` 窗口（含 Steel/Concrete/SRC/Cold Formed Steel/Footing/
  Aluminum Design 选项卡）中实际生成荷载组合。

### Step 5 — 报告

- 输入封面名（项目名、公司名）并以 Web 或 PDF 输出 "Scale Up 计算报告"。
- 报告构成：① 设计条件（荷载、有效地面加速度 S、场地等级/重要性、抗侧力体系、近似周期），
  ② GEN NX 模型数据（X/Y 方向 hn/Ta、等效替代重力荷载 W、各方向周期 Td、基底剪力 Vt、相应方向
  应用），③ 计算过程（X/Y 方向各自 T_use、Cu 基准、Sd1 放大、Cu 下限、Cu 应用、Vs、0.85Vs/Vt、Cm），
  ④ 设计反应谱（图线），⑤ Cm 计算结果（汇总）。

## 6. 关联 JSON API 端点

**"GEN NX DATA MAP" 画面上以文本形式原样显示了 5 个读取条目的来源 API**，可基于
确认到的依据进行映射：

| 界面显示（条目编号） | 界面显示文本 | 文档位置 |
| --- | --- | --- |
| 01 层高 | `GET db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/zh-cn/02_DB_Project_Structure.md#15-dbstor--story-data) |
| 02 RS 工况 | `GET db/SPLC`（RS 荷载工况 · 经 GET db/SPLC 下拉框再次确认） | [`09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases`](../../manual/zh-cn/09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases) |
| 03 特征值结果 | `POST TABLE · EIGENVALUEMODE` | [`20_POST_AnalysisResult_2.md#28-vibration-mode-shape`](../../manual/zh-cn/20_POST_AnalysisResult_2.md#28-vibration-mode-shape) |
| 04 有效地震重量 | `NODE · MASS · SUMMARY XY`（下拉框中显示 `Mass Summary X · POST post/TABLE · MASS_SUMMARY_X`、`Mass Summary Y · ...MASS_SUMMARY_Y`） | [`18_POST_PreProcess.md#3-mass-summary-table`](../../manual/zh-cn/18_POST_PreProcess.md#3-mass-summary-table) |
| 05 层剪力 | `POST TABLE · STORY_SHEAR_FOR_RS` | [`21_POST_StoryTables.md#3-story-shear-force-rs-analysis`](../../manual/zh-cn/21_POST_StoryTables.md#3-story-shear-force-rs-analysis) |
| 生成荷载组合请求 | `POST ope/LCOM-*`（按画面上 "RC · KDS 41 20 : 2022" 的选择状态推测为 `LCOM-CONC`） | [`15_OPE.md#16-opelcom-conc--load-combination-concrete--kds-41-202022`](../../manual/zh-cn/15_OPE.md#16-opelcom-conc--load-combination-concrete--kds-41-202022) |

- "GEN NX DATA MAP" 下拉框中除上述 5 项外还显示了 `楼层信息 · GET db/STOR`、`全部固有周期 ·
  POST post/TABLE - EIGENVALUEMODE`、`全部质量参与率 · POST post/TABLE - EIGENVALUEMODE`、
  `节点信息 · GET db/NODE` 等额外候选条目，由此确认这 5 个映射槽位各自可在多张原表中
  选择的构造。
- ⚠️ 生成荷载组合的 API 在画面上显示为 `POST ope/LCOM-*`，尾部被截断（被图标遮挡），
  准确的模式名（LCOM-CONC/LCOM-GEN/LCOM-STEEL/LCOM-SRC 之一）是基于"结构设计分类"
  被选为 RC · KDS 41 20 : 2022 的情形所作的推测。

## 7. 输入数据规格

- **前置条件**：已生成反应谱分析与特征值分析结果的 GEN NX 模型。
- **设计条件**：地震分区、图谱值 S、场地类型、重要性系数 Ie、抗侧力体系（R/Ω0/Cd）、近似周期
  计算公式。

## 8. 输出 / 生成结果

- Cm,x / Cm,y 修正系数数值。
- 在 GEN NX `Load Combinations`（Concrete/Steel/SRC 等）中自动生成套用 Cm 的荷载组合（RX(RS)×Cm,x、
  RY(RS)×Cm,y 等）。
- "Scale Up 计算报告"（Web/PDF）。

## 9. 限制事项与局限

- Cm 计算画面上明示了与 KDS 41 17 00 相关的警告"层间位移不适用 Cm"，
  可见本 Plug-in 生成的荷载组合用于强度设计，层间位移（使用性）验算需另用其他荷载
  工况。
- 与 #4（AutoGenerationCmFactor）有目的重叠之处，但 ScaleUp 运行于 MIDAS 官方 Apps
  平台（注册型向导 UI）并涵盖到生成荷载组合·报告，范围更广—两个 Plug-in 的关系（竞争/补充）
  原文未明示，暂不判断。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–8 | 在 Apps 列表中选择 "Scale Up SE"，执行前确认提示 |
| 8–40 | 执行插件，输入设计条件 UI（地震分区/场地/重要性/抗侧力体系，收藏夹） |
| 40–72 | 反应谱实时图线与按区间的 Sa 查询，进入"下一步：确认模型数据" |
| 72–96 | 读取 GEN NX 数据，"GEN NX DATA MAP"（显示原 API·表 5 种） |
| 96–120 | 模型数据确认画面汇总，执行计算 Cm |
| 120–144 | Cm,x/Cm,y 计算结果、基底剪力比较表、"下一步：生成荷载组合" |
| 144–168 | 生成荷载组合选项（结构设计分类、Envelope、抗震设计附加选项），在 GEN NX Load Combinations 窗口中实际生成 |
| 168–189 | 输入报告封面 → 打印/PDF 输出 → 确认最终计算报告内容 |

---

*下一步：08_ScaffoldModel 视频分析与规划文档编写。*
