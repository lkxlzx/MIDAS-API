# ScaffoldModel 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/08_ScaffoldModel.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据视频（`docs/plugin_cases/videos/08_ScaffoldModel.mp4`，60fps，1920×1038，约 262 秒）以 9 秒
> 间隔抓取帧（共 30 张）后逐帧目视分析 + 下方字幕作为依据编写。与原文
> 文章（`docs/plugin_cases/articles/08_ScaffoldModel.md`）的四大功能说明交叉核对过。与 #7
> ScaleUp 同样是 GEN NX "My Work"（Apps）面板中执行的注册型 Plug-in，其特征是在单个对话
> 框内把从建模到荷载·分析·Steel Code Check·图像保存·计算书编写全部处理的
> 一站式（one-stop）结构。

## 1. 概述

**ScaffoldModel（Scaffold-Mddel）** 是在 MIDAS GEN NX 中将单排脚手架与双排脚手架（建设现场临时
脚手架）的模型生成、荷载施加、结构分析、Steel Code Check、结果图像保存及脚手架结构计算书
编写的全过程自动化的实务型工具。

## 2. 问题定义

- 外部脚手架结构审查是实务中反复执行的定型化作业（建模 → 施加荷载 → 分析 →
  Steel Code Check → 保存结果图像 → 编写计算书），但每次都手动推进则耗时很长。
- 尤其是风荷载、隔音墙·防坠落网附加荷载、连墙件条件等脚手架特有的荷载组合，存在每次
  都要重新构成的繁琐。

## 3. 目标用户

- 需编写建设现场单排/双排脚手架结构计算书的结构工程师。
- 需将同一审查流程反复应用于多个现场（项目）的实务人员。

## 4. 核心概念 / 差异化点

- **建模 → 分析 → 计算书在一个对话框中无缝处理**："生成模型 → 执行分析 →
  保存分析图像 → 编写计算书"4 个按钮按顺序配置在同一弹窗底部，不关闭窗口
  即可顺序执行整条流水线。
- **单排/双排脚手架形式切换**：在"脚手架形式"中用单排脚手架/双排脚手架复选框切换形式时，
  输入字段的构成本身随之改变（双排脚手架会额外显示内侧/外侧立杆间距、连杆长度等单排脚手架没有的
  字段）。
- **"在新文件中生成"与"保护现有数据"两种执行模式**：在新文件中生成是以新工程为基准生成脚手架模型的方式，
  保护现有数据是在保留现有模型数据的前提下追加脚手架模型的方式—支持在已有其他结构模型的
  文件上只追加脚手架的场景。以保护现有数据模式重新执行时，
  演示中展示了**新脚手架模型为避免与现有模型重叠而隔开生成**（例：8m 偏移）。
- **附加荷载用复选框切换**：勾选隔音墙设置·防坠落网设置后，相应荷载数值（隔音墙高度/荷载、坠落荷载）
  输入字段出现，且这些数值会反映到自动生成的荷载组合
  （1.0D、1.0D+1.0L、0.8D+0.52W、0.8D-0.52W、ENV_ALLOW）中。
- **自动保存分析图像 + 自动附加到计算书**：用"保存分析图像"按钮按指定路径（例：
  `C:\MIDAS\CaptureTest`）将等轴测图·荷载图（风荷载/防坠落网荷载/构件内力等）
  保存为 PNG，并在"编写计算书"阶段经"是否选择在脚手架计算书中放入的荷载计算表图
  像？"确认后，把已保存的图像自动附加到计算书（HTML）中。

## 5. 工作流

### Step 1 — 在 Apps 中执行

- 在 GEN NX 右侧 `Tree Menu 2 > Works`（My Work 面板）中搜索·选择 "Scaffold-Mddel" 应用 → Run。

### Step 2 — 输入脚手架建模

面板由 5 个分组构成：

| 分组 | 字段 | 备注 |
| --- | --- | --- |
| 数据生成方式 | 在新文件中生成 / 保护现有数据 | 互斥复选框 |
| 脚手架形式 | 单排脚手架建模 / 双排脚手架建模 | 依选择而下方输入字段构成不同 |
| 水平杆与立杆 | 脚手架竖向高度、脚手架横向长度、第一道水平杆高度、立杆间距、水平杆间距（+双排脚手架追加内侧/外侧立杆间距、连杆长度） | mm 单位 |
| 连墙件 | 起始高度、横向设置间距、竖向设置间距、长度 | mm 单位 |
| 荷载 | 风荷载 WL(kN/m²)、隔音墙设置（高度/荷载 DL）、防坠落网设置（荷载 DL）、生成荷载组合 | 用复选框 on/off 附加荷载 |
| 分析图像 | 项目名、图像保存路径 | 用于计算书封面·附加 |

- 视频示例值：脚手架竖向高度 14000mm、横向长度 6000mm、第一道水平杆高度 300mm、立杆间距
  @600mm、水平杆间距 @1500mm、连墙件起始高度 600mm·横向/竖向设置间距 @3000mm·长度
  500mm、风荷载 WL 0.519kN/m²、隔音墙高度 4m·荷载 DL −0.5kN/m²、坠落荷载 DL −1.5kN。

### Step 3 — 生成模型

- 点击"生成模型" → 下方执行日志："此阶段生成材料、截面、节点、构件..." → 画面上
  生成格构式脚手架 3D 模型（Node/Element/Section/Material）。
- 接续显示"生成荷载工况、荷载组、Floor Load Type、荷载组合" → 树菜单中自动生成 Static
  Load Case 1(DL: Dead Load)/2(LL: Live Load)/3(WL: Wind Load on Structure)，
  各工况中填入 Self Weight、Nodal Loads、Floor Loads。

### Step 4 — 执行分析与 Steel Code Check

- 点击"执行分析" → 进行结构分析。
- 接续显示 "Steel Checking" 进度状态窗（Read or Check Steel Members...）→ 按 KDS 41 30:2022 基准
  Start/End Code Checking 日志，Member Checking 250/250 完成。
- 执行结果汇总自动记载于弹窗底部文本区域："建模报告执行结果汇总 — 建模
  方式：在新文件中生成，脚手架形式：单排脚手架，Steel Code Check → 完成"、"生成模型汇总 — 脚手架
  竖向高度/横向长度/构件生成、节点·单元生成、连墙件 boundary 条件已应用、Steel Code
  Check 已进行"。

### Step 5 — 保存分析图像

- 点击"保存分析图像"按钮 → 在指定路径（`C:\MIDAS\CaptureTest`）自动截图并保存
  `01_iso`、`02_load_wind`、`03_load_fall_protection`、`04_load_sound_barrier`、`06_beam_my`（构件内力图）等多个视点·各类荷载的 PNG 图像。

### Step 6 — 编写计算书

- 点击"编写计算书" → "是否选择在脚手架计算书中放入的荷载计算表图像？"确认模态框
  （确认：选择图像 / 取消：荷载计算表另行审查）→ 选择"确认"时，已截图的图像被自动附加到计算书中。
- 产出物：`비계검토서_00구 00동 00-00_20260728(10).html` — 含封面（"脚 手 架 计 算 书"、项目名、
  编制日期）与审查概要（按脚手架及安全设施物设置（KDS 41 60 10）的审查、竖向荷载·风荷载·
  荷载组合汇总表）的 HTML 报告被保存到下载文件夹，可直接用浏览器查阅。

### Step 7 — （反复演示）保护现有数据模式 + 双排脚手架

- "将以保护现有数据方式执行。"— 把数据生成方式改为"保护现有数据"、
  脚手架形式改为"双排脚手架建模"后重新执行。
- 输入双排脚手架专用字段（内侧立杆间距 @750、外侧立杆间距 @1500、连杆长度（内外排之间）
  @1500）。
- "可确认新的脚手架模型为避免与现有模型重叠而隔开生成"—
  在现有单排脚手架模型旁以 8m 偏移自动布置新的双排脚手架模型（Nodes 476/Elements
  931 增加）。
- "生成模型后由用户确认构件布置或应用条件，修改必要部分，此后利用 GEN NX API
  从脚手架模型生成起...大幅缩短了作业时间"— 强调这是自动生成后可手工修正的半自动工作流，
  并收尾。

## 6. 关联 JSON API 端点

画面上未显示准确的端点文本，但操作对象（生成脚手架构件、执行 Steel Code
Check·结果·图像·报告）明确，可特定 `docs/manual` 中的对应端点：

| 功能 | 推测 API | 文档位置 |
| --- | --- | --- |
| 生成模型（材料·截面·节点·构件） | `POST /db/MATL`、`POST /db/SECT`、`POST /db/NODE`、`POST /db/ELEM` | [`04_DB_Properties.md#1-dbmatl`](../../manual/zh-cn/04_DB_Properties.md#1-dbmatl), [`04_DB_Properties.md#12-dbsect`](../../manual/zh-cn/04_DB_Properties.md#12-dbsect), [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| 生成荷载工况·组合 | `POST /db/STLD`（静力荷载工况）、`POST /ope/LCOM-STEEL` | [`15_OPE.md`](../../manual/zh-cn/15_OPE.md)（LCOM-STEEL 系列） |
| 执行结构分析 | `POST /doc/ANAL` | [`01_DOC.md#11-docanal--perform-analysis`](../../manual/zh-cn/01_DOC.md#11-docanal--perform-analysis) |
| 执行 Steel Code Check | `POST DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL` | [`25_Design_Steel_KDS41302022.md#23-designsteelkds-41-30-2022code-anal--steel-code-check-perform-강재-코드-검토-수행`](../../manual/zh-cn/25_Design_Steel_KDS41302022.md#23-designsteelkds-41-30-2022code-anal--steel-code-check-perform-钢结构规范校核执行) |
| Steel Code Check 结果表 | `POST DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE` | [`25_Design_Steel_KDS41302022.md#24-designsteelkds-41-30-2022code-table--steel-code-check-table-강재-코드-검토-표`](../../manual/zh-cn/25_Design_Steel_KDS41302022.md#24-designsteelkds-41-30-2022code-table--steel-code-check-table-钢结构规范校核表) |
| Steel Code Check 结果图像 | `POST DESIGN/STEEL/KDS-41-30-2022/DREULT` | [`25_Design_Steel_KDS41302022.md#26-designsteelkds-41-30-2022dreult--steel-design-result-강재-설계-결과-이미지`](../../manual/zh-cn/25_Design_Steel_KDS41302022.md#26-designsteelkds-41-30-2022dreult--steel-design-result-钢结构设计结果图像) |
| 生成计算书（报告） | `POST DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT` | [`25_Design_Steel_KDS41302022.md#25-designsteelkds-41-30-2022code-report--steel-code-check-report-강재-코드-검토-보고서`](../../manual/zh-cn/25_Design_Steel_KDS41302022.md#25-designsteelkds-41-30-2022code-report--steel-code-check-report-钢结构规范校核报告) |

- ⚠️ 上述映射是基于画面上明示的阶段名（"生成模型"、"执行分析"、"Steel Code Check"、"保存分析
  图像"、"编写计算书"）与 `docs/manual/25_Design_Steel_KDS41302022.md` 的端点
  名称·用途准确对应所作的推测，实际请求体与准确的调用顺序未在画面上
  显示。
- 自动生成荷载组合（`1.0D`、`1.0D+1.0L`、`0.8D+0.52W`、`0.8D-0.52W`、`ENV_ALLOW`）是否准确经过
  `/ope/LCOM-STEEL`，抑或 Plug-in 直接调用 `/db/` 系列荷载组合端点，
  在画面上未能确认。

## 7. 输入数据规格

- **脚手架尺寸**：脚手架竖向高度/横向长度(mm)、第一道水平杆高度、立杆/水平杆间距。
- **连墙件**：起始高度、横向/竖向设置间距、长度。
- **荷载**：风荷载 WL(kN/m²) 必填，隔音墙·防坠落网荷载以复选框选择输入。
- **分析图像保存路径**：本地文件路径（例：`C:\MIDAS\CaptureTest`）。

## 8. 输出 / 生成结果

- 生成到 GEN NX 模型中的单排/双排脚手架结构（Node/Element/Section/Material/Boundary/Load）。
- 分析结果图像（PNG，等轴测图·荷载图·构件内力图 等）。
- "脚手架计算书"HTML 报告（含附加的荷载计算表图像）。

## 9. 限制事项与局限

- "保护现有数据"模式虽会自动隔开布置以避免与现有模型重叠，但用户能否直接指定准确的隔开
  距离（例：8m）在视频中未能确认（⚠️ 看似自动计算，但基准未确认）。
- 自动生成后仍"由用户确认构件布置或应用条件并修改必要部分"—自身亦予以明确，
  并非完全免审查的自动化，而是作为生成初稿的工具设计。
- 原文提到 Steel Code Check 结果只显示 OK/NG，但视频中未捕捉到展示单个构件的
  NG 详细内容（具体哪个构件因何种原因 NG）的画面。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–18 | 在 My Work(Apps) 面板中搜索·执行 "Scaffold-Mddel"，功能概要字幕 |
| 18–45 | 首次显示脚手架建模输入弹窗（数据生成方式、脚手架形式、水平杆·立杆尺寸） |
| 45–99 | 输入连墙件·荷载（风荷载、隔音墙、防坠落网），生成荷载组合预览 |
| 99–135 | 执行"生成模型" → 生成 3D 脚手架模型·材料/截面/节点/构件，确认自动生成荷载工况 |
| 135–162 | "执行分析" → 进行 Steel Code Check(KDS 41 30:2022)，结果汇总日志 |
| 162–189 | "保存分析图像" → 确认截图图像文件夹，"编写计算书" → 确认图像附加模态框 → 查阅 HTML 计算书 |
| 189–216 | 切换为"保护现有数据" + "双排脚手架建模"并重新输入字段 |
| 216–252 | 重新执行 → 确认生成与现有模型隔开的新型双排脚手架模型，效果概要字幕（"大幅缩短了作业时间"） |
| 252–262 | 结束卡片（"感谢观看"） |

---

*下一步：09_RCRebarOptimizer 视频分析与规划文档编写。*
