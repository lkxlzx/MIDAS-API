# PlantFrameBuilder 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/11_PlantFrameBuilder.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 视频（`docs/plugin_cases/videos/11_PlantFrameBuilder.mp4`，30fps，1920×1080，约 165 秒）按 6 秒
> 间隔截帧（共 28 张）后，以逐帧目视分析 + 字幕为依据撰写。与原文文章
> （`docs/plugin_cases/articles/11_PlantFrameBuilder.md`）的 2 大功能说明做了交叉确认。
> "GENERATE READINESS" 检查清单与 "GENERATE COMPLETE MODEL" 进度日志在画面上原样暴露，是可以极为
> 具体地确认生成流水线阶段构成的案例。

## 1. 概述

**Plant Frame Builder** 是仅凭 Bay 间距·层高等输入值，即可自动生成双列多层 Pipe Rack（工厂配管支撑
结构物）初始结构分析用钢框架（Node/Column/Beam/Brace/Support）模型的 GEN NX API Plug-in。

## 2. 问题定义

- 逐个手工绘制数十·数百个 Node 与 Element 的既有方式很繁琐。
- 即便在 CAD 中用 DXF 画出骨架再 Import 到 GEN NX，每当形状变更（Bay 数、层数、间距等）都必须从头
  重复一遍，由此产生往返作业。
- 既有 GEN NX 方式（用 Copy/移动反复堆叠楼层）同样属于重复作业，形状变更时的返工成本很大。

## 3. 目标用户

- 在工厂（石油化工·发电等）项目中需要把配管支撑用 Pipe Rack 骨架快速做成初始结构分析模型的结构
  工程师。
- 需要在初始设计阶段反复比较多种形状方案（Bay 数、层数、斜撑布置等）的工程人员。

## 4. 核心概念 / 差异化点

- **输入参数 → 实时 3D 预览 → 一次点击、数十秒内生成**：无需 CAD，在 GEN NX 内只调整 Bay 数·间距、
  Rack 宽度、Level 数·层高等参数，右侧"结构预览"便即时刷新，最终按一次按钮生成整个模型。
- **复用既有模型的 Material/Section + 同时支持新建定义**：点击"读取数据"后，当前 GEN NX 模型中已定义
  的 Material（#1 Frame）·7 种 Section 会原样填入下拉框供复用，同时可用"+ 新增 Steel Material
  定义"/"+ 新增 DB Section"当场定义新的材料·截面并加入"待生成清单"（并非立即生成，而是在最终执行
  Generate Complete Model 时一并生成）。
- **按构件类别独立指定截面**：Column、Trans.（横）Beam、Long.（纵）Beam、Brace 4 类构件可分别指定
  不同截面。用 X-Brace 开关控制是否使用斜撑，并可像 Brace Bay 那样逐个选择 Bay 1/3/5/7...，直接
  指定布置斜撑的位置。
- **3 种支座条件（Fixed/Pinned/None）**：以节点约束方式选择支承条件。
- **详细设置（原点、基准 Level、ID 分配）**：Origin X/Y、Base Elev. Z、逐个勾选放置斜撑的 Level、
  自动 ID 分配（Node/Element 编号取最大值+1 规则）等细部选项通过"展开详细设置"暴露。
- **VALIDATE & PREVIEW → GENERATE READINESS 两级预校验**：生成之前把全部输入值以摘要表（Unit、
  Material 分配、Section 分配、Column/Beam/Brace 截面等）一次整理呈现，随后连预计生成数量（Node/
  Column/Beam/Brace 个数与准确的 ID 范围，例：Column ID 1~160、Brace ID 391~550）也预先计算显示。
  只有"GENERATE READINESS"检查清单（模型数据读取/Unit 读取/Material 分配/Section 分配/无名称冲突/
  输入校验/模型冲突校验 7 项）全部通过，"确认后生成"按钮才会被激活。
- **明示不支持 Undo**：生成之前明确给出警告文"本插件不支持 Undo/自动 Rollback。生成后若要回退，
  必须在 GEN NX 中直接删除" —— 在让用户清楚认识到这是不可回退的操作之后才继续。
- **分阶段进度日志暴露**：执行生成时，实时显示"前处理进度：重新查询 → 预校验 → Unit → Material →
  Section（任一步失败则其后全部中止）"的顺序及各阶段的成功/跳过状态 —— 属于中途一旦失败即中止后续
  全部阶段的安全串行流水线结构。

## 5. 工作流

### Step 1 — API 连接

- 在 "GEN NX Plant Frame Builder" 窗口输入 `Base URL`、`MAPI-Key`。明确说明"Key 只在会话内存中使用，
  不会保存在任何地方"。

### Step 2 — 读取数据

- 点击"读取数据" → 自动读取当前 GEN NX 模型的 Unit（例：KN/M/KCAL/C）、Material（Frame #1）、
  Section（7 种）清单。

### Step 3 — 基本设置（形状参数）

| 字段 | 说明 | 示例值 |
| --- | --- | --- |
| Bay 数 | 纵向跨数 | 3 → 15 |
| Bay 间距 | 等间距或按 Bay Custom | 6 (m) |
| Rack 宽度 | 横向宽度 | 8 (m) |
| Level 数 | 层数 | 2 → 5 |
| 层高 | 等层高或 Custom | 4 (m) |

- 改值时左侧"结构预览"3D 等轴测图即时刷新，Bay/Rack/Level/Brace/Support 摘要文本也一并更新。

### Step 4 — 材料·截面·斜撑·支座设置

- Material：复用既有 Frame（#1），或以"+ 新增 Steel Material 定义"（Standard：KS22(S)、DB 钢种：
  SS235 等）新建后"加入待生成清单"。
- Column/Trans. Beam/Long. Beam 截面：各自在下拉框中选择既有 Section，或以"+ 新增 DB Section"
  （Shape：H-Section 等、可直接输入截面名、仅显示 KS21 目录等中确认到的 12 种）新建定义。
- X-Brace 开关打开时指定 Brace 截面，并用独立复选框选择 Brace Bay（例：Bay 1、3、5、7、9、11、13、
  15 —— 每奇数 Bay 布置斜撑）。
- Support：从 Fixed/Pinned/None 中选择（例：改为 Pinned 时，预览中的支座标记立即变为三角形铰符号）。
- 详细设置：Origin X/Y、Base Elev. Z、逐个勾选放置斜撑的 Level（在 Level 1~5 中选择）、自动 ID 分配
  开关（打开时以"Node 1 / Element（当前最大 ID + 1，读取数据结果）"自动编号）。

### Step 5 — 校验与预览

- 在 "VALIDATE & PREVIEW" 区块确认"校验通过 — 可按以下内容进行批量生成"。
- 通过输入值摘要表（当前 Unit、Unit 应用方式、Material 分配/新增 Material、Column/Trans. Beam/
  Long. Beam 截面等）再次确认最终设置。
- 预计生成数量表（PIPE RACK）：Node 192 个（ID 1~192）、Column 160 个、Transverse Beam 80 个、
  Longitudinal Beam 150 个、Brace 160 个、Element 合计 550 个（ID 1~550，Column ID 1~160、
  Transverse Beam ID 161~240、Longitudinal Beam ID 241~390、Brace ID 391~550）、Support 32 个
  （PINNED），并详细显示坐标范围（X 0~90/Y 0~8/Z 0~20）与 Brace 位置清单。

### Step 6 — 确认生成准备状态（GENERATE READINESS）

- 检查清单 7 项：模型数据读取（Base URL/MAPI-Key/读取数据）、Unit 读取、Material 分配、Section
  分配（Column/Trans./Long./Brace）、无名称冲突、输入校验、模型冲突校验 —— 仅当全部为 ✓（成功）时
  才能进入下一步。
- ⚠️ 演示中在把形状改回的瞬间，捕捉到"模型冲突校验"项显示为 ✕（失败）的帧 —— 表明对与上次生成结果
  坐标重叠的情形可事先筛除的校验阶段确实在起作用（重新设置后再次以 ✓ 通过）。

### Step 7 — 生成模型

- "GENERATE COMPLETE MODEL" 区块内的"生成前最终确认"警告框：再次确认所用 Unit、有无新增 Material/
  Section、将生成的 Node/Element/Support 数量、ID 范围、不支持 Undo 的警告，随后点击"确认后生成"
  按钮。
- 进度日志："前处理进度：重新查询 → 预校验（ID·名称冲突）→ Unit 应用 → Material 生成/重新查询校验 →
  Section 生成/重新查询校验 →（Frame 生成顺序）Node → Column → Transverse → Longitudinal → Brace →
  Support"，各阶段按顺序显示成功（●）并执行。
- 完成后确认 GEN NX 模型树中确实生成了 Nodes 192、Elements 550（Truss 160、Beam 390）、Material 1、
  Section 7、Supports 32（Type 1 [111000]），并以 3D 等轴测图旋转检视最终的 Pipe Rack 骨架形状。

## 6. 关联 JSON API 端点

画面上未暴露确切的端点名称，但凭"Frame 生成顺序：Node → Column → Transverse → Longitudinal →
Brace → Support"这一明确顺序，以及最终反映到 GEN NX 模型树的数据结构（Nodes/Elements（Truss·
Beam）/Material/Section/Supports）即可完成准确映射：

| 生成顺序 | 对象 | 推测 API | 文档位置 |
| --- | --- | --- | --- |
| 1 | Material（新增 Steel Material） | `POST /db/MATL` | [`04_DB_Properties.md#1-dbmatl`](../../manual/zh-cn/04_DB_Properties.md#1-dbmatl) |
| 2 | Section（新增 DB Section） | `POST /db/SECT` | [`04_DB_Properties.md#12-dbsect`](../../manual/zh-cn/04_DB_Properties.md#12-dbsect) |
| 3 | Node（192 个） | `POST /db/NODE` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode) |
| 4 | Column/Beam（Trans.·Long.） | `POST /db/ELEM`（Beam） | [`03_DB_Node_Element.md#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| 5 | Brace | `POST /db/ELEM`（Truss） | 同上 |
| 6 | Support（32 个，Fixed/Pinned） | `POST /db/CONS` | [`05_DB_Boundary.md#1-dbcons--constraint-support`](../../manual/zh-cn/05_DB_Boundary.md#1-dbcons--constraint-support) |

- ⚠️ 上述映射依据画面显示的"Frame 生成顺序"与最终生成的 GEN NX 模型树条目（被归类为 Truss 160 个 /
  Beam 390 个 —— 推测 Column·Beam 以 Beam 类型生成、Brace 以 Truss 类型生成），而实际请求体与准确的
  调用次数（逐个 POST 重复 vs 批量 POST）未在画面暴露，未获确认。
- 推测 Unit 应用（日志中单独存在"Unit 应用"步骤）调用的是 `/db/UNIT` 系列端点，但在 `docs/manual`
  中尚未确认到该端点（⚠️ 未确认）。

## 7. 输入数据规格

- **形状参数**：Bay 数、Bay 间距（等间距/Custom）、Rack 宽度、Level 数、层高（等层高/Custom）。
- **材料·截面**：Column/Trans. Beam/Long. Beam/Brace 各自的既有或新增 Section、Material。
- **斜撑**：是否使用 X-Brace、斜撑布置的 Bay·Level。
- **支座条件**：Fixed/Pinned/None。
- **详细设置**：Origin X/Y、Base Elev. Z、是否自动 ID 分配。

## 8. 输出 / 生成结果

- GEN NX 模型中生成的 Node·Column·Transverse Beam·Longitudinal Beam·Brace·Support 全部 Pipe Rack
  骨架（用于初始结构分析）。
- 生成前即可确认的预计数量·ID 范围摘要信息。

## 9. 限制事项与局限

- 不支持 Undo/自动 Rollback —— 生成后若要回退，必须由用户在 GEN NX 中直接删除。这是该 Plug-in 自己
  明确警告的局限。
- 生成物是"初始结构分析用"Frame 模型，实际配管荷载·风荷载等荷载施加以及构件验算·设计不包含在该
  Plug-in 的范围内（原文与画面任何位置都未提及荷载施加功能）。
- 模型冲突校验（与既有模型坐标是否重叠）会自动执行，但究竟会进一步自动重排到不重叠的位置，还是仅给
  出失败信号，画面中只确认到失败后重试的镜头，未确认到自动避让逻辑。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–12 | 片头（Plant Frame Builder 概述幻灯片、生成前最终确认 UI 预览） |
| 12–30 | WHY —— 既有手工/DXF Import 方式的繁琐，介绍"无需 CAD、直接在 GEN NX 内"的概念 |
| 30–66 | 实际进入 GEN NX，API 连接（Base URL/MAPI-Key），读取数据 |
| 66–96 | 基本设置（Material/Column/Beam/Brace 截面、新增 Steel Material·DB Section 定义） |
| 96–138 | 随 Bay 数/Level 数/Bay 间距等参数调整的实时预览刷新，X-Brace·Brace Bay·支座条件，详细设置（原点/Brace Level/自动 ID） |
| 138–150 | VALIDATE & PREVIEW 摘要表，GENERATE READINESS 检查清单，确认预计生成数量·ID 范围 |
| 150–162 | 执行"确认后生成" → 分阶段进度日志 → 确认最终 3D 模型生成结果（树条目·旋转检视） |
| 162–165 | 收尾 |

---

*下一步：12_OTChecker 视频分析与规划文档撰写。*
