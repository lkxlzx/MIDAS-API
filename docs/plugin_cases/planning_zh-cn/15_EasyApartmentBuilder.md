# EasyApartmentBuilder 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/15_EasyApartmentBuilder.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据对视频（`docs/plugin_cases/videos/15_EasyApartmentBuilder.mp4`，60fps，3840×2160，约 313 秒）按 10 秒间隔逐帧截取（共 32 张）后逐帧肉眼分析 + 画面下方字幕编写。已与原文文章（`docs/plugin_cases/articles/15_EasyApartmentBuilder.md`）的 4 大功能说明交叉确认。本件与 #1(WALL STACKER) 的目的·工作流相似，同属"DXF → 公寓剪力墙骨架自动建模"系列 Plug-in，但不同之处在于它专精于 **Wall Mark(用户标注名) → Wall ID(GEN NX 设计单位) 两步分离**与**基准层复制**功能。

## 1. 概述

**Easy Apartment Builder(EAB)** 是基于结构平面图 DXF、通过 Wall Mark/ID 自动化实现简明快捷的公寓分析建模的 Plug-in。它自动生成墙体的标注名(Wall Mark)，为满足 GEN NX 的墙体设计逻辑(按 Wall ID 设计)而自动分配 Wall ID，并可指定基准层，把相同的 Wall Mark/ID 重复应用到多个楼层。

## 2. 问题定义

- 像公寓这样墙体数量众多的剪力墙结构，给 DXF 图纸中的每一片墙命名(Mark)并分配 GEN NX 设计单位 Wall ID 的作业十分重复且耗时。
- Wall Mark(用于图纸标注的名称)与 Wall ID(GEN NX 墙体设计逻辑的实际单位)本是不同的概念，由人手工逐一映射很容易出错。
- 多个楼层(基准层重复等)会重复相同的墙体构成，每一层都从头作业效率很低。

## 3. 目标用户

- 需要把公寓(剪力墙结构)结构平面图 DXF 快速转成 GEN NX 分析模型的结构建模人员。
- 需要边按项目标准整理 Wall Mark·Wall ID 体系边建模的实务人员。

## 4. 核心概念 / 差异化点

- **按 CAD 元素类型自动映射**：把 DXF 的线元素(Line、Poly Line)自动识别·考虑为墙体·梁单元，点元素(Point)自动识别为柱 —— 选择图层时以"Wall / Beam & Column"三分弹窗由用户确认。
- **Wall Mark → Wall ID 两步工作流**：① 在平面中选择墙体，自动或手动分配 Wall Mark(例：W1、CW1)（可把多片墙合并为同一个 Mark）→ ② 用"Wall ID 自动生成"按钮，按 Wall Mark 分配顺序从 1001 号起自动编号赋给 Wall ID。把 Mark(人读的标注)与 ID(GEN NX 设计单位)明确分离，既保持图纸标注惯例又满足 GEN NX 墙体设计逻辑。
- **指定基准层与复制**：为每个 DXF 文件(楼层)指定"基准层"徽标后，就把该层中定义的 Wall Mark/ID/Material/Thickness 原样复制到其它楼层应用 —— 消除了重复输入。视频演示中已确认把基准层(01 1F to 17F.dxf)中制作的 250 余个 Wall Mark 复制到"02 18F to 25F.dxf"楼层的画面（分配数量由 250 个重组为 152 个）。
- **在 Plug-in 界面中直接指定 Material/Thickness**：无需往返于单独的 GEN NX 界面，在选中 Wall Mark 的状态下即可直接指定 Material(C30、C27 等)与 Thickness(T200、T250 等)——与原文第 4 项功能（"可以确认建模将如何落地，即 Material、Properties、Thickness"）一致。
- **Beam/Col 也一并处理**：在单独的"Beam/Col"标签中，为各 DXF 层(01 1F to 17F / 02 18F to 25F / 03 옥탑층)分别指定把 Line 元素映射为 Beam 所需的 Material·Section，不仅墙体，梁、柱也在同一个工作流内一并处理。
- **用户便利功能(快捷键·交互)**：鼠标滚轮(Zoom In/Out)、Ctrl+Z(Undo)、Load/Save As（保存·读取已有作业）、通过点击/左→右拖动/右→左拖动选择平面元素（与 NX 相同的操作体系）、按元素设置 View Active/Inactive、输入 Story Data·Wall 数据时用 Tab/Enter 在输入框间跳转、点击 dxf 层后拖动可一次选择多个楼层、在 Wall 标签中把 Wall Mark 现状里已在平面中选中的 Mark 移到列表最上方等，提供了大量实务便利功能。
- **建模前的最终确认与影响范围摘要**：在"Model Build 确认"模态窗中指定墙体划分(Wall Segment Length)值后，会预先汇总显示待生成的 Element 数量(Wall+Beam/Column)与 Wall Mark/Wall ID/Story 条目数，随后"执行 Build"。

## 5. 工作流

### Step 1 — 在 Apps 中运行并读取 DXF

- 在 GEN NX `Apps > My Work` 中运行"EAB" Plug-in → 打开独立的 Web 视图(基于浏览器的 Floor Plan Editor)窗口。
- 按"请从右侧读取 DXF 文件"的提示，先在 Story Data 标签中确认楼层列表(1F~11F 等)（显示 Height/Level 值，可指定 Ground Level）。
- 用"读取"按钮按顺序读入多个 DXF 文件(例：`01 1F to 17F.dxf`、`02 18F to 25F.dxf`、`03 최상층.dxf`) —— 用复选框映射各 DXF 所对应的楼层范围。

### Step 2 — 指定基准层并按 DXF Layer 定义元素

- 为每个已读取的 DXF 文件指定"基准层"徽标(例：把 01 1F to 17F.dxf 设为基准层)。
- 在"选择图层"模态窗中按 DXF 的 Layer 分别指定 Wall / Beam & Column 元素类型。

### Step 3 — 定义 Wall 元素(Wall Mark 自动分配 → 修改·合并)

- 在 Wall 标签中点击"自动分配" → 对未选择的全部墙体自动赋予 W1、W2、W3… 形式的 Wall Mark（在右侧"WALL MARK 现状"表中以 Mark/Wall ID/Material/Thickness 各列列出）。
- 在平面中直接点击/拖动选择墙体 → 在"WALL MARK 分配"输入栏中输入想要的名称(例：CW1、CW2、CW4)并点击"分配" → 可把所选的多片墙合并为一个 Mark。
- Properties 分配：用 Material·Thickness 下拉框为选中的 Mark 指定材料·厚度。

### Step 4 — 自动生成 Wall ID

- 点击"Wall ID 自动生成"按钮 → 显示"将按 Wall Mark 分配顺序对全部对象从 1001 号起依次赋号"的提示后，Wall ID 自动编号(例：CW1→1001、CW2→1002、CW3→1003、CW4→1004、W2→1005...)。

### Step 5 — 复制基准层数据

- 在其他 DXF 层(例：02 18F to 25F.dxf)执行"复制并导入基准层 Data" → 基准层中定义的 Wall Mark/ID/Material/Thickness 原样复制到该层（WALL MARK 现状条目数由 250 个变为 152 个，即按该层实际墙体构成重新应用）。
- 也可以按楼层重新指定不同的 Material/Thickness(例：上部楼层改为 C27)。

### Step 6 — 添加 Beam/Col 元素

- 切换到"Beam/Col"标签 → 按 DXF 层(01 1F to 17F / Beam、02 18F to 25F / Beam、03 최상층 / Beam)分别指定要映射给 Line 元素的 Material·Section。

### Step 7 — Model Build

- 点击右下角"Model Build"按钮 → 在"Model Build 确认"模态窗中确认单位制(m，Plan Editor 模型单位)并输入 Wall Segment Length（墙体划分长度，例 1~1.5m）。
- 自动显示待生成摘要："Wall Element(3837 个，Beam/Column Element 312 个已完成)、Wall Mark(按 Mark 的 Wall ID 分组)、Story 信息登记(27 个)"等 —— 4199 个 Element(Wall 3887 + B/C 312)、Wall 260 个、Story 26 个。
- 点击"执行 Build" → 实际反映到 GEN NX 模型。

### Step 8 — 确认 GEN NX 模型结果

- 在 GEN NX 树菜单中确认已生成 Stories(27)、Nodes(4995)、Elements(4199，Beam 312/Wall 3887)、Material 2 种(C30、C27)、Section 2 种(Col、Beam)、Thickness 4 种(T150/T200/T250/T300)。
- 在平面图中确认自动赋予的 Wall ID(1001、1002...)与 Wall Mark(CW1、CW2、W101...)以标签形式显示在图纸上。
- 在 GEN NX 默认菜单 `Structure > Building > Auto Wall ID Generation`(GEN NX 自身的向导工具)界面中，也再次确认以"Modify Wall Mark Data"呈现的正是 Plug-in 制作的 Wall Mark/ID 数据，原样得到反映 —— 即 Plug-in 的输出与 GEN NX 原生 Wall Mark 体系完全兼容。
- 在 Structure 功能区的 `Story > Story Data` 窗口中，最终确认 Plug-in 登记的楼层数据(Floor Width、Floor Center、Eccentricity 等)已正常反映到 GEN NX。

## 6. 关联 JSON API 端点

画面上未显示准确的 API 调用日志（在基于浏览器的 UI 中处理），但在最终 GEN NX 结果界面上数据结构清晰可辨，可以建立对应关系：

| 功能 | 推测 API | 文档位置 |
| --- | --- | --- |
| Story Data 登记 | `POST /db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/zh-cn/02_DB_Project_Structure.md#15-dbstor--story-data) |
| 墙体/梁 Node·Element 生成 | `POST /db/NODE`, `POST /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| Material/Section/Thickness 生成 | `POST /db/MATL`, `POST /db/SECT`, `POST /db/THIK` | [`04_DB_Properties.md#1-dbmatl`](../../manual/zh-cn/04_DB_Properties.md#1-dbmatl), [`#12-dbsect`](../../manual/zh-cn/04_DB_Properties.md#12-dbsect) |
| Wall Mark(Mark ↔ Wall ID 映射) | `POST /db/WMAK` | [`24_DB_Design.md#9-dbwmak--modify-wall-mark-design-벽체-마크-설계-수정`](../../manual/zh-cn/24_DB_Design.md#9-dbwmak--modify-wall-mark-design-墙体标记设计修改) |

- 由于已确认 Plug-in 制作的 Wall Mark/Wall ID 数据原样显示在 GEN NX 原生 `Structure > Building > Auto Wall ID Generation`(树菜单"Modify Wall Mark Data")界面上，因此与 #2(WallMarkAutoMapper) 一样，有力地支撑了 `/db/WMAK`(`{"WMAK": {"<ID>": {"MARKNAME": "...", "WID_LIST": [...]}}}`) schema 的使用。
- ⚠️ 在基于浏览器的 Web 视图(Floor Plan Editor)中实时进行的 DXF 解析·Wall Mark 自动分配·基准层复制逻辑本身，看起来并非 GEN NX Open API 调用，而是 Plug-in 自身逻辑(客户端侧)，推测仅在最终"Model Build"阶段才批量调用 GEN NX API（准确的调用时点·是否批处理未在画面上确认）。

## 7. 输入数据规格

- **DXF 文件**：结构平面图，可按楼层上传多个文件。需要区分线(墙体·梁)、点(柱)元素的图层。
- **Story Data**：各层高度(Height)·标高(Level)，指定 Ground Level。
- **Wall Segment Length**：墙体划分长度(m) — 在 Model Build 时指定。

## 8. 输出 / 生成结果

- GEN NX 模型的 Story Data、Node/Element(Wall/Beam/Column)、Material/Section/Thickness、Wall Mark(`/db/WMAK`) 全部数据。

## 9. 限制事项与局限

- 开发者在"今后改进事项"中亲自写明："应用 Beam 元素时最下层会被形成 → 改进为删除"——目前存在最下层(地下/基础标高)会一并生成不必要 Beam 元素的局限，并表明今后将改进为自动删除。
- 由于 Wall Segment Length(划分长度)取值不同会使生成的 Element 数量大幅变化（提示语："例）长度 7.0m 的墙体输入 2.0m 时分为 4 段(约 1.75m)，裂缝节点会自动布置在尽量不重叠的位置"），因此需要针对所选值复核结果。
- Wall Mark 自动分配按墙体布置顺序(选择顺序)编号，因此若与项目标准命名规则不同，可能需要手动重新分配。

## 10. 画面清单

| 时点(秒) | 画面内容 |
| --- | --- |
| 0–10 | 开场（Plug-in Info：昵称 이현파파、Easy Apartment Builder、功能摘要） |
| 10–20 | 考虑事项/便利功能幻灯片（按 CAD dxf 元素特性对应的构件 Type、快捷键、今后改进事项、预期效果） |
| 20–40 | 在 Apps 中运行 EAB、首次进入 Floor Plan Editor Web 视图、确认 Story Data |
| 40–60 | 读取多个 DXF 文件(1F~17F/18F~25F/최상층)、楼层映射 |
| 60–100 | 按 DXF Layer 定义元素(选择图层模态窗)、Wall Mark 自动分配 |
| 100–190 | 修改·合并 Wall Mark、指定 Material/Thickness、自动生成 Wall ID、复制基准层 Data |
| 190–230 | 在 Beam/Col 标签中指定 Material/Section |
| 230–250 | Model Build 确认模态窗(Wall Segment Length、待生成摘要) → 执行 Build |
| 250–313 | 确认 GEN NX 结果(3D 形状、Wall ID/Mark 标签、与原生 Wall Mark 数据·Story Data 窗口对照) |

---

*下一步：16_CRANE_LOADER 视频分析与规划文档撰写。*
