# AutoWallRebarData 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/18_AutoWallRebarData.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据视频（`docs/plugin_cases/videos/18_AutoWallRebarData.mp4`，30fps，1910×1006，约169秒）按
> 7秒间隔截帧（共25张）后逐帧目视分析，并以画面下方日志文本为依据撰写。已与原文文章
> （`docs/plugin_cases/articles/18_AutoWallRebarData.md`）的2大功能说明交叉确认。视频中包含直接
> 打开 GEN NX 原生 `Design > Rebar Input > Modify Wall Rebar Data`（Design Input Data）窗口、与
> Plug-in 写入的结果进行比对确认的画面，因此数据究竟对应 GEN NX 的哪一项功能十分明确。

## 1. 概述

**Auto Wall RebarData** 是可以按 Wall Mark 或厚度（Thickness）选择 GEN NX 墙体配筋（Modify
Wall Rebar Data），将竖向钢筋、水平钢筋、端部约束筋、边缘构件钢筋连同保护层与厚度按楼层区间
一次性输入，并把已输入的配筋整理为 Wall Mark 单位的表格导出为 PDF 的 Plug-in。

## 2. 问题定义

- GEN NX 原生 `Modify Wall Rebar Data` 功能按墙体（Wall ID）指定配筋，而属于同一 Wall Mark 的
  多个楼层·多个 Wall ID 往往要反复输入相同配筋，产生大量重复手工操作（原文第1项功能“自动化
  楼层重复手工操作”）。
- 输入结束后，还要另外重新制作按标记整理墙体配筋现状的文档（供设计审查·图册编制使用），颇为
  繁琐。

## 3. 目标用户

- 需要按 KDS 41 20:2022 输入 RC 墙体竖向·水平·端部约束·边缘构件钢筋的结构设计人员。
- 需要把配筋现状按 Wall Mark 整理为表格并用于审查·图册的现场人员。

## 4. 核心概念 / 差异点

- **选择对象可在 Wall Mark 与 Thickness 两种基准之间切换**：在“对象选择”小节可在 Wall Mark
  页签（用复选框逐个/多个选择 CW1、CW2、CW3...）或 Thickness 页签（按厚度批量选择）之间切换。
  也支持直接输入 Wall ID（如 `例: 100-110, 205` 那样范围与单个混合输入）。
- **按楼层区间多重定义配筋**：用“+层区间添加”按钮建立多个楼层范围（例：B7~B1、1F~15F、
  16F~30F），各区间独立指定竖向钢筋/水平钢筋/保护层厚度/端部约束筋/边缘构件规格——实际设计中
  低层部用粗钢筋、上层部改用细钢筋的典型模式得以如实反映。
- **配筋输入字段细分**：竖向钢筋（规格@间距）、水平钢筋（规格@间距）、保护层厚度（内侧 DW/
  外侧 DE，勾选厚度模型值）、端部约束筋（是否使用、规格×数量@间距）、边缘构件数量（间距）、
  边缘构件长度(mm)，完整覆盖 KDS 41 20 墙体配筋标准项目。
- **应用前显示对象·区间进度状态**：以“对象 11个 · 区间 1 · 输入完成/未完成”的形式，用实时
  计数器显示定义了多少个 Wall ID、多少个楼层区间以及输入是否完成。
- **通过日志窗口透明公开执行历史**：各步骤的 API 调用结果原样输出为日志，如“已连接（HTTP
  200）”、“总 N个（未定→选/全部）”、“墙体选择：楼层组 20条”、“配筋应用：完成 N条”、“基准墙体
  配筋（REBAR）加载 N条”等——即使失败也能追踪问题出现在哪一步。
- **按 Wall Mark 单位导出配筋清单 PDF**：“将当前模型的墙体配筋（Wall ID 11个）整理为表格，
  打印 → 保存为 PDF”——各标记的楼层区间·钢筋·保护层·厚度表格即时输出为 PDF。
- **使用与 GEN NX 原生功能完全相同的数据模型**：直接在 GEN NX 原生菜单
  `Design > Rebar Input > Modify Wall Rebar Data` 中打开查看应用结果，Plug-in 输入的按楼层区间
  配筋以 `Wall ID / Wall Mark / Start Story / End Story / Bar` 形式（如 `300-B7`、`300-B6`、
  `300-B5` 这样在 Wall ID 后附楼层区间后缀的 Sub Wall ID 模式）被准确反映，由此确认 Plug-in
  直接沿用了 GEN NX 原生配筋数据结构。

## 5. 工作流

### Step 1 — 确认目标墙体（GEN NX 原生画面）

- 演示开始时，先在 GEN NX `Design > RC Design`（KDS 41 20:2022）画面中确认目标模型（70个楼层，
  Wall 6386个）。
- 在 `Design > Design Input Data > Modify Wall Mark Data` 中确认 CW3 这一 Wall Mark 已分配多个
  Wall ID（300, 301, 302, 303...）——该数据应已由 #2/#15 的 `/db/WMAK` 预先构建。

### Step 2 — 运行 Plug-in 并连接 API

- 运行 `Apps > Plug-in > Auto Wall RebarData`。在运行前的信息面板中确认“对象：Wall Mark 或
  Thickness（厚度）— 自动筛选实际存在的 Wall ID，不存在的 ID 在应用时跳过”、“配筋：竖向钢筋·
  水平钢筋·端部约束筋·边缘构件，保护层厚度，按楼层范围（FROM~TO）输入”、“钢筋规格下拉框、自动
  填充既有配筋、应用后自动重新查询”等说明。
- 输入 Base URL/MAPI-Key → 在 API Settings 弹窗中确认 Connected 状态。

### Step 3 — 对象选择

- 在“对象选择”小节选择 Wall Mark 页签 → 在 CW1(600)、CW2(600)、CW3(300)、CW3(B栋)(300)、
  CW3A(300)... 列表中用复选框选择对象（例：仅选 CW3 → “对象 11个”）。
- 也可用 Wall ID 直接输入字段细化范围（输入 `300to310` 后自动规范化显示为 `300 - 310`）。

### Step 4 — 输入配筋（按楼层区间）

- 勾选楼层范围指定后，可在“应用于全部楼层”与单独指定区间之间选择。
- 第1区间（例 B7~B1）：竖向钢筋 D13@250，水平钢筋 D10@250，保护层厚度 DW30/DE50(mm)，端部约束筋
  使用 D16×4@100，边缘构件数量/边缘构件长度不使用。
- 用“+层区间添加”建立第2区间（例 1F~15F）：改为竖向钢筋 D16@150，水平钢筋 D13@200（或调整为
  D16@200）。
- 第3区间（例 16F~30F）：竖向钢筋 D13@150，水平钢筋 D13@200，按上层部要求缩小。
- 钢筋规格用下拉框选择 D4~D57。

### Step 5 — 应用配筋

- 点击“配筋输入”→ 下方日志按顺序输出进度：“已连接（HTTP 200）”→“总 70个（未定→选）
  B7→Roof”→“墙体映射导入完成 1个”→“墙体选定 楼层组 6386个 → Wall(ID 12个)，厚度组 20种”→
  “基准墙体配筋（REBAR）加载 117个”。
- 最终确认为“对象 11个 · 区间 3 · 输入完成”状态。

### Step 6 — 结果验证（再次确认 GEN NX 原生画面）

- 直接打开 GEN NX `Design > Rebar Input > Modify Wall Rebar Data` 菜单（原生弹窗），确认 Plug-in
  生成的按楼层区间 Sub Wall ID（`300`、`300-B7`、`300-B6`、`300-B5`、`301`、`301-B7`...）已准确
  注册。

### Step 7 — 导出配筋清单 PDF

- 点击“PDF/打印”→ 按“将当前模型的墙体配筋（Wall ID 11个）整理为表格，打印 → 保存为 PDF”的
  说明，将各 Wall Mark 的配筋清单保存为 PDF。

## 6. 关联的 JSON API 端点

日志中未暴露明确的端点名（仅以 HTTP 200 显示 `GET`/`POST` 的成功与否），但已直接确认数据被准确
反映到 GEN NX 原生 `Modify Wall Rebar Data` 窗口所对应的内容：

| 功能 | 对应 GEN NX 菜单 | `docs/manual` 覆盖情况 |
| --- | --- | --- |
| 墙体配筋（竖向·水平·端部约束·边缘构件）查询/输入 | `Design > Rebar Input > Modify Wall Rebar Data` | ⚠️ 专用端点未文档化（见下） |
| Wall Mark 列表查询 | `Design > Design Input Data > Modify Wall Mark Data` | [`24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정`](../../manual/zh-cn/24_DB_Design.md#9-dbwmak--modify-wall-mark-design-墙体标记设计修改) (`/db/WMAK`) |
| 按 Wall Mark 的构件钢筋设计基准 | （参考）`DESIGN/RC/KDS-41-20-2022/DCRM-WALL` | [`26_Design_RC_KDS41202022.md`](../../manual/zh-cn/26_Design_RC_KDS41202022.md) (§32 `DCRM-WALL`) |

- ⚠️ **重要发现**：本 Plug-in 所操作的“墙体配筋（Modify Wall Rebar Data）”——按楼层区间指定
  竖向/水平钢筋、端部约束筋、边缘构件、保护层厚度的专用数据——在 `docs/manual` 中并未以专用
  端点文档化。§32 的 `DCRM-WALL`（“墙体构件用钢筋设计基准”）名称相似，但与画面中确认的按楼层
  区间竖向·水平·端部约束·边缘构件输入 UI 是否为完全相同的数据，仅凭本仓库无法断定。与 #5
  （WallStiffnessAuto）发现 `/db/WSSF` 时同样，本 Plug-in 也是暴露 `docs/manual` 手册覆盖空白
  （gap）的案例——准确的端点名需在官方 API 文档中另行确认。
- 配筋清单查询（PDF 输出的依据）从日志中“基准墙体配筋（REBAR）加载 117个”一语判断，推测是以
  GET 重新查询上述同一墙体配筋端点。

## 7. 输入数据规格

- **对象选择**：按 Wall Mark（多选复）或 Thickness（厚度）基准，Wall ID 直接输入（范围/单个
  混合）。
- **按楼层区间配筋**：楼层范围（From~To）、竖向钢筋（规格@间距）、水平钢筋（规格@间距）、保护层
  厚度（内侧/外侧）、端部约束筋（是否使用、规格×数量@间距）、边缘构件数量·边缘构件长度。
- **前置条件**：GEN NX 模型中须已定义 Wall Mark（`/db/WMAK`）（“对象选择”的 Wall Mark 页签基于
  该数据运行）。

## 8. 输出 / 生成结果

- 反映到 GEN NX 模型 `Modify Wall Rebar Data` 的按楼层区间墙体配筋（竖向·水平·端部约束·边缘
  构件·保护层厚度）。
- 以 Wall Mark 为单位整理的墙体配筋清单 PDF。

## 9. 限制事项与局限

- 运行前说明中明确写有“不存在的 ID 在应用时跳过”，因此虽被指定为对象但模型中实际不存在的
  Wall ID 会被悄悄跳过——用户若未另行留意，可能造成部分墙体遗漏。
- `docs/manual` 中未文档化本 Plug-in 使用的墙体配筋专用端点，仅凭本仓库无法确认准确的请求模式
  （Key/Value）。
- 楼层区间互相重叠时（例：同时指定 1F~15F 与 10F~20F）的处理方式在画面中未确认（⚠️ 未确认）。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–21 | GEN NX 原生 RC Design 画面、确认目标模型（70层），通过 Modify Wall Mark Data 确认 CW3 的分配 |
| 21–42 | 运行 Auto Wall RebarData、信息面板（对象/配筋/钢筋规格说明）、API 连接 |
| 42–70 | 对象选择（Wall Mark 页签、勾选 CW3、Wall ID 直接输入） |
| 70–126 | 按楼层区间输入配筋（B7~B1、1F~15F、16F~30F 三个区间）、调整钢筋规格下拉框 |
| 126–140 | 执行“配筋输入”、查看日志 |
| 140–161 | 用 GEN NX 原生 Modify Wall Rebar Data 窗口验证结果（确认 Sub Wall ID 模式） |
| 161–169 | 通过 PDF/打印导出配筋清单 |

---

*下一步：分析 19_AutoSteel 视频并撰写规划文档。*
