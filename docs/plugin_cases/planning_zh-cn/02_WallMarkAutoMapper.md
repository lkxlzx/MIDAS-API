# WallMarkAutoMapper 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/02_WallMarkAutoMapper.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据对视频(`docs/plugin_cases/videos/02_WallMarkAutoMapper.mp4`, 60fps, 3840×2160, 约 300秒)按 10秒
> 间隔抓取帧（共 30张）后的逐帧目视分析 + 视频内字幕（旁白字幕）撰写。
> 已与原文文章(`docs/plugin_cases/articles/02_WallMarkAutoMapper.md`)的四大功能说明交叉确认。

## 1. 概述

**WallMarkAutoMapper** 将从 DXF 结构平面图中提取的墙体名称（Wall Mark）文本与坐标，与 MIDAS GEN
NX 分析模型中已赋予的 Wall ID 的墙体中心坐标自动匹配，从而把图纸上的墙体名称批量赋予并管理为对应
Wall ID 的 Wall Mark 的 Plug-in。匹配结果在 Preview 画面与结果表中复核后，仅将用户选中的项目反映
到模型。

## 2. 问题定义

- GEN NX 默认 UI(`Modify Wall Mark Data`)需用户逐项手工输入 Wall Mark 名称及其所属的 Wall ID
  列表(`WID_LIST`)。
- 在墙体数量众多的剪力墙结构公寓等项目中（以视频示例为准：墙体 102 个，Wall Mark 100 个），重复
  录入时间随之拉长，遗漏·笔误等失误概率也随之升高。
- 即便只是修改已录入的项目，也得边滚动列表边逐个查找，难以将全部项目一眼整体对照。
- 依视频字幕的量化效果：手工操作时以 100 个墙体计约需 50 分钟（按每件约 30 秒估计：查看图纸 +
  确认 Wall ID + 录入）→ 使用 Plug-in 时约 20 分钟（设置 5 分钟 + 结果复核约 13 分钟 + 应用确认
  2 分钟），约**节省 60% 时间**。

## 3. 目标用户

- 同时使用 DXF 结构平面图与 GEN NX 分析模型的结构设计者·建模人员。
- 尤其在墙体数量众多的剪力墙结构（公寓等）项目中，需要反复更新 Wall Mark（设计标注名）的实务人员。

## 4. 核心概念 / 差异化点

- **基于坐标的自动匹配**：并非文本完全一致匹配，而是计算 DXF 中提取的 Wall Mark 插入坐标与 GEN NX
  Wall ID 的中心坐标之间的 XY 直线距离，连接最近的候选。因此图纸上的墙体名称与 GEN NX Wall ID
  名称不同（例：图纸为 "HW5"，模型为 Wall ID 1）时也可按位置匹配。
- **三级可信度分类（容许距离 × 75% 阈值）**：以用户指定的容许距离为基准，将结果自动分为
  OK/需复核/匹配失败三级，从而无需全量复核，只针对例外项目复核。
- **创建 / 修改 双模式**：将初次批量赋予用的"Wall Mark 创建"模式，与对已赋予的 Wall Mark 进行查询·
  修改·删除的"Wall Mark 修改"模式，在 UI 顶部标签上分离。
- **支持 Excel 往返编辑**：结果表可导出为 Excel 进行批量复核·修改，之后再次导入反映（复核人员为
  多人或工作量极大时很有用）。
- **预览确认后选择性反映**："应用预览"窗口中区分新建/修改/无变更/冲突·不可应用项目，仅将选中的
  项目反映到实际模型 — 防止误操作覆盖全部内容的事故。

## 5. 工作流

### Step 0 — 准备 DXF 文件（前置作业，在 GEN NX 之外）

- 将 GEN NX 模型导出为 **AutoCAD DXF File**(`Export > AutoCAD DXF File`)后，由 CAD 程序在该 DXF 上
  布置墙体名称（Wall Mark）文本，并以独立图层（视频示例：`A-WALL_CENTERLINE`）管理。
- ⚠️ 限制：分析模型与图纸的比例必须一致（推荐以 mm 为单位），墙体名称文本需布置在紧邻墙体中心线的
  位置才能提升匹配精度（字幕："需位于墙体中心与墙体名称相邻处，匹配结果的准确度才会提高"）。

### Step 1 — API 连接与数据载入（Wall Mark 创建模式）

左侧面板 3 个分组：

| 分组 | 字段 | 说明 |
| --- | --- | --- |
| API 设置 | 连接按钮 | 输入 Mapi Key，与已打开的 GEN NX 文件建立连接 |
| GEN NX 设置 | Load 楼层（下拉，默认"全部楼层"） | 选择匹配目标的楼层范围 |
| GEN NX 设置 | Wall Type: MEMBRANE / PLATE（切换） | 选择匹配目标的墙体单元类型 |
| GEN NX 设置 | "GEN NX 载入"按钮 | 以所选条件载入模型的墙体 Node/Element 数据 |
| DXF 设置 | 载入 DXF 文件 | 选择目标 DXF 文件（例：`Sample_Wallmark.dxf`） |
| DXF 设置 | Wall Mark 图层（下拉） | 指定墙体名称文本所在的图层（例：`A-WALL_CENTERLINE`） |
| 匹配设置 | 匹配容许距离（mm，默认值 1000） | 划分 OK/需复核/匹配失败的距离基准 |

连接后在操作日志（左下）按顺序显示的状态消息：
1. "已确认 GEN NX 连接。载入 STOR 28 个。"
2. "请执行 GEN NX 载入。"
3. "GEN NX 数据载入完成：NODE 7461个，ELEM 7377个，STOR 28个，Load 楼层 全部楼层，Wall 候选
   102个"

中央 Wall Mark Preview 中显示已载入的墙体形状（GEN NX Wall，实线）（Marks 0 | Walls 102）。

### Step 2 — 执行自动匹配

点击"▶ 执行自动匹配"按钮时：

- 从 DXF 的 Wall Mark 图层提取文本/坐标，与 GEN NX 各 Wall ID 的中心坐标比对完成匹配。
- 以匹配容许距离为基准分三级：

| 状态 | 条件 | 含义 |
| --- | --- | --- |
| OK | 距离 ≤ 容许距离 × 75% | 显示为自动匹配成功 |
| 需复核 | 容许距离 × 75% < 距离 ≤ 容许距离 | 在容许范围内，但需用户确认 |
| 匹配失败 | 容许距离内无可用候选 | 不自动分配 Wall ID |

- 执行后日志："在 101호.dxf 中匹配了 Wall Mark 100 个。容许距离 1000.0mm，匹配摘要：
  OK 80 个，需复核 18 个，匹配失败 2 个"
- 底部 Summary Card 即时显示 Wall Mark 总数（100 个）、匹配成功（80 个，80%）、需复核（18 个，18%）、
  匹配失败（2 个，2%）。
- 中央 Preview 默认只高亮显示"需复核""匹配失败"项目，可用鼠标滚轮放大/缩小、拖动平移画面，与图纸
  对照复核。图例：GEN NX Wall（灰色实线）/ 匹配成功（绿色虚线）/ 需复核（橙色虚线）/ 未匹配（红色
  虚线）/ 标记冲突（紫色虚线）。
- 右侧"自动匹配结果"表：列 `适用(复选框) | Wall Mark | Wall ID | 距离 | 状态`。可用筛选·排序只挑出
  需复核项目，也可直接点击单元格对 Wall Mark 名称进行行内修改。

### Step 3 — 应用结果

- 勾选要反映的项目（单独勾选或"全选"）后点击"Wall Mark 应用"按钮 → 打开 **Wall Mark 应用预览**
  模态窗。
- 模态窗内筛选标签：全部 / 新建 / 修改 / 无变更 / 冲突·不可应用。表列：
  `区分 | Wall Mark | 变更前 WID_LIST | 变更后 WID_LIST | 状态/备注`。
- 提示文案（字幕）："只有结果表中选中的 Wall Mark 才会反映到 GEN NX。分析模型中已经应用、但未包含在
  匹配结果中的 Wall Mark 不予变更。" — 即即便执行部分应用，原有未涉及项目仍会被保留的
  non-destructive 反映方式。
- 点击"应用"时完成最终反映，并在日志中记录"Wall Mark 修改履历保存：1件"等。

### Step 4 — Excel 往返编辑（可选）

- "导出 EXCEL" → 生成 `DXF Wall Mark Auto Mapper — Review / Apply Excel Template v1` 形式的工作簿。
  列：`Apply | Story | Wall Mark(도면) | 최종 Wall Mark | Wall ID | Status |
  Dist. | Conf. | Note`。
- 在 Excel 中用 `Apply` 列(Y/N)标注是否反映，`Status` 为 `Review`（容许距离内需复核）或
  `Unmatched`（无候选）的行，其理由会自动写入 `Note` 列（例："容许距离内需复核""无候选"）。
- 将修改后的 Excel 用"导入 EXCEL"重新载入，即反映到结果表，从而可在电子表格中推进批量复核。
- 另提供 PDF 结果表输出按钮（用于报告/记录，细部动作未在视频中显示）。

### Step 5 — Wall Mark 修改模式（查询·修改·删除既有 Wall Mark）

将顶部标签切换为"Wall Mark 修改"后，左侧设置面板与创建模式相同（API/GEN NX 设置），但动作不同：

- 日志："已执行 GET db/WMAK 查询校验" → "切换模式：已初始化作业数据" →
  "修改模式载入完成：Wall 候选 102个，Wall Mark 87个"
- 右侧"Wall Mark 修改"表：列 `选择 | 状态(无变更/变更/删除等) | Wall Mark | WID_LIST |
  变更前 WID_LIST`。将模型中已保存的 Wall Mark 原样载入，以可编辑的表格显示。
- 在表格内右键点击可通过上下文菜单执行"增加行 / 删除行 / 撤销删除行" — 即在此画面也可对特定
  Wall Mark 增加或排除 Wall ID，或删除 Wall Mark 本身。
- Preview 图例也与创建模式不同，由 GEN NX Wall / 变更 / 删除 / NG 四类构成。
- 用"Wall Mark 应用"按钮，以与创建模式相同的方式预览 → 最终反映。

## 6. 关联 JSON API 端点

以视频内操作日志中明确显示的 API 调用/数据对象为准：

| 时点 | 日志文案 | 推测 API | 文档位置 |
| --- | --- | --- | --- |
| 刚连接后 | "载入 STOR 28 个" | `GET /db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/zh-cn/02_DB_Project_Structure.md#15-dbstor--story-data) |
| GEN NX 载入 | "载入了 NODE 7461个、ELEM 7377个…" | `GET /db/NODE`, `GET /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode), [`03_DB_Node_Element.md#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| 进入修改模式 | "已执行 GET db/WMAK 查询校验" | `GET /db/WMAK` | [`24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정`](../../manual/zh-cn/24_DB_Design.md#9-dbwmak--modify-wall-mark-design-墙体标记设计修改) |
| Wall Mark 应用 | "保存 Wall Mark 修改履历" | `POST /db/WMAK`（新建/变更部分），必要时 `PUT`/`DELETE` | 同上 |

- ⚠️ `/db/WMAK` 的正式模式为 `{"WMAK": {"<ID>": {"MARKNAME": "...", "WID_LIST": [...]}}}`
  结构，视频结果表·修改表中显示的 `Wall Mark`/`WID_LIST`/`变更前 WID_LIST` 列名与该模式的
  `MARKNAME`/`WID_LIST` 准确对应 — 与其他 8 个 Plug-in 不同，本项在画面日志中以文本形式露出了
  实际端点名(`db/WMAK`)，因此属于已确认的依据而非推测。
- Wall ID 中心坐标计算所需的墙体单元筛选（Wall Type: MEMBRANE/PLATE）逻辑未在画面上显示，因此
  准确的过滤方式（例：是否利用 `/db/ELEM` 的 `TYPE` 字段）未获确认。

## 7. 输入数据规格

- **DXF 文件**：在 GEN NX 中以 `Export > AutoCAD DXF File` 导出后，将墙体名称文本(TEXT/MTEXT)添加到
  独立图层的文件。前提是与分析模型同一比例（推荐 mm）、原点坐标系一致。
- **Wall Mark 图层**：在 UI 中指定 DXF 内墙体名称文本所在的图层名（例：
  `A-WALL_CENTERLINE`）。
- **匹配容许距离**：mm 单位，由用户直接输入（视频默认值 1000mm）。
- **GEN NX 模型**：必须包含已赋予 Wall ID 的墙体单元（Membrane 或 Plate）。

## 8. 输出 / 生成结果

- 更新 GEN NX 模型的 `/db/WMAK` 数据（Wall Mark ↔ Wall ID 列表映射）。
- Excel 结果表(`.xlsx`) — 用于复核·批准履历管理。
- PDF 结果表 — 用于报告输出。

## 9. 限制事项与局限

- 匹配纯粹以坐标距离为准，因此当墙体名称文本远离墙体中心布置、或多个墙体在容许距离内密集排布时，
  "需复核"/"匹配失败"会增多 — 其设计前提并非完全自动化，而是自动匹配 + 人工复核。
- 分析模型与 DXF 图纸的比例·原点不同时，匹配本身即不成立（前置准备阶段的必要前提）。
- "Wall Mark 应用"采用结果表中未列出的既有 Wall Mark 不受变更的 partial-update 方式，因此需要整体
  重新同步时，可能需在"Wall Mark 修改"模式下另行全量删除后重建等追加作业（视频中未直接提及，
  依 UI 动作推得 — ⚠️ 待确认）。

## 10. 画面清单

| 时点(秒) | 画面内容 |
| --- | --- |
| 0–10 | 片头标题（标题/一句话介绍） |
| 20–50 | 01·WHY — 既有手工方式的 3 处不便（逐项录入、手写 WID_LIST、难以整体比较） |
| 60–100 | 02·SOLUTION — 4 步流程（DXF → GEN NX → MATCH → APPLY）及匹配状态判定标准（75%）说明 |
| 110 | Wall Mark Auto Mapper 实际 UI 首次进入（连接前状态） |
| 120–140 | 左侧设置区结构说明、API 连接（Mapi Key） |
| 140–170 | GEN NX 数据载入完成，DXF 文件生成方式（AutoCAD Export）说明幻灯片 |
| 180–230 | 执行自动匹配 → Summary Card、Preview 筛选、结果表复核 |
| 230–250 | Wall Mark 应用预览模态窗，Excel 导出（Excel 模板画面） |
| 250–280 | Wall Mark 修改模式：载入、表中行内编辑、右键增行/删行、应用 |
| 280–300 | 04·IMPACT — 预期效果汇总（50 分钟 → 20 分钟，约节省 60%） |

---

*下一步：撰写 03_VibrationAnalysisAssistant 的视频分析与规划文档。*
