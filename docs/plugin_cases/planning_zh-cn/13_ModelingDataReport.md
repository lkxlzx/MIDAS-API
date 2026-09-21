# ModelingDataReport 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/13_ModelingDataReport.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据对视频（`docs/plugin_cases/videos/13_ModelingDataReport.mp4`，30fps，1920×1080，约 230 秒）按 8 秒间隔逐帧截取（共 29 张）后逐帧肉眼分析 + 字幕编写。已与原文文章（`docs/plugin_cases/articles/13_ModelingDataReport.md`）的 3 大功能说明交叉确认。在本系列的 20 个案例中，这是产出信息密度最高（PDF 共 31 页、5 个章节）的 Plug-in，其核心在于几乎全量排查建模校核项。

## 1. 概述

**Modeling Data Report** 用 MIDAS API 全量收集 GEN NX 中已打开模型的声明数据（结构形式/楼层/材料/截面/边界条件/荷载/分析选项），自动生成为可直接附入结构计算书附录的"建模审查报告"（PDF、Excel）的 Plug-in。

## 2. 问题定义

- 由资深工程师校核 GEN NX 模型或向其他负责人交接时，需要逐项确认散落在各个菜单中的设置（自重、边界条件、刚度系数等），因为不清楚菜单位置而很容易漏项。
- 层间位移、不规则（错层、偏心等）评估这类抗震相关审查文档必须组合多个结果表格，单独制作文档非常耗时。
- 资深与初级工程师之间的建模确认（评审）过程重复且不标准。

## 3. 目标用户

- 需要校核、交接 GEN NX 模型的资深/初级结构工程师。
- 需要在结构计算书附录中附上建模审查报告的实务人员。

## 4. 核心概念 / 差异化点

- **声明与否（Boolean）全量检查**：把材料、截面、刚度系数、边界条件、分析选项等 GEN NX 的每一个独立输入菜单逐项列为"已声明"/"–"（未声明）的表格，从源头上杜绝用户忘记"这一项到底填没填"的失误（例如 3.1 节"声明现状(Properties)"表中，将 Material Properties/Section Stiffness Scale Factor/Thickness/Wall Stiffness Scale Factor 等 10 余个项一并列为已声明/未声明）。
- **基于节点坐标自动校验自重计算**：由节点坐标自动计算并显示建筑面积、单位面积重力荷载（1.1 模型摘要），并通过按荷载工况的汇总表（2.4 节）使用户能够发现录入错误的荷载。
- **最底层节点-支座声明数量对照自动化**：生成形如"最下层(B1F)标高节点数：257 vs Support 声明节点数：257 → 未声明节点：0（无遗漏）"的自动对照表，自动抓出支承条件遗漏（3.10 节）——不是简单罗列，而是内嵌了实际的一致性校验逻辑。
  ⚠️ 按本文档的惯例，这类自动校验仅限于明确列出的项，因此推测是分别用 API 取得"几个 vs 几个"这两个数字后再作比较，其余各项是否也都有这种一致性校验尚未得到确认。
- **Self Check 复选框**：在每一项旁放置可由用户直接勾选的"Self Check"栏，审查者可逐项标记"我已亲自确认"，可作为检查清单使用。
- **组织为 5 个章节**：General(结构概况·建筑概况校验) → Structure(骨架·荷载·楼层质量) → Properties & Boundary(材料·截面·支座) → Analysis Option(必用分析选项) → Load(荷载·风/地震·层间位移·不规则)，把前处理（建模）与后处理（分析选项·不规则评估）整合为一份文档。
- **Story Drift·不规则评估也自动给出**：自动计算考虑偶然偏心(Accidental Eccentricity)的层间位移、刚度不规则(Soft Story，X/Y 方向)、偏心(Torsional)不规则的判定结果并以 Regular/Irregular 呈现，输出大量表格——与原文第 3 项功能（"层间位移与不规则评估也自动整理完毕，减轻了抗震相关审查文档的编写负担"）完全一致。

## 5. 工作流

### Step 1 — 连接 API 并采集模型

- 在"Modeling Data Report"窗口中输入 `Base URL`、`MAPI-Key`。
- 点击"1. 模型采集" → 按荷载工况的计算进度日志(Calculating Loads for Load Case DL/WX/WY/EX/EY/WX(A)...) → 自动对地下/地上/屋面塔层进行分类（用户必要时可直接修改，用下拉框重新划分地下/地上/屋面塔层）。

### Step 2 — 输入系数

- 输入建筑重要性、位移放大系数 C_d、超强系数 Ω_0、冗余度系数等——这些系数会反映到层间位移·不规则评估中。

### Step 3 — 生成报告(PDF)

- 点击"2. 生成报告(PDF)" → 生成由 5 个章节构成的报告(共 31 页)：

**Chapter 01. General**（结构概况·建筑概况校验）
- 1. General — 数据采集（从已打开的模型实时采集）、采集时刻、是否已分析。
- 自动截取整体形状(Isometric)·平面(Top)图像。
- 1.1 模型摘要：建筑规模（地下 1 层/地上 20 层+屋面塔 1 层，共 22 层）、建筑宽/进深/高度、建筑重要性（风荷载·地震作用重要性系数）、建模建筑面积（钢框架网格近似）、建筑总重（全部楼层固定荷载之和）、地震有效重量（计算地震作用时采用的 MASS）、代表层单位面积荷载（面积/DL sum/LL sum/单位面积 DL/单位面积 LL）。
- 特征值分析结果表(Mode No/Frequency/Period/TRAN-X/TRAN-Y/ROTN-Z)。
- 风荷载概况（自动/手动计算、适用规范 KDS(41-12:2022)、基本风速、重要性系数 I_w、细长比 λ、计算方法、阵风影响系数、风向横向荷载 Across Wind、Wind Shear）。
- 地震作用概况（适用规范 KDS(41-17-00:2019)、重要性系数 I_E、场地系数 S、场地分类）。

**Chapter 02. Structure**（骨架·荷载·楼层质量）
- 原样截取 Structure Type/Mass Control Parameter/Building Control 弹窗以确认声明状态（3-D/X-Z Plane/Y-Z Plane/X-Y Plane/Constraint RZ、Lumped Mass/Consistent Mass 等）。
- 2.3 Story Data — Wind·Seismic(各层 Floor Width、Center、Eccentricity、Accidental/Inherent Eccentricity、Torsional Amplification Factor X/Y)。
- 2.4.2~2.4.5 按荷载工况的汇总表(DL/LL/WX/WY — Z 方向，Level/Input/Self Weight/Sum)。
- 2.5 Story Mass(Translational Mass X/Y-DIR、Rotational Mass、Center of Mass X/Y-Coord)。

**Chapter 03. Properties & Boundary**（材料·截面·支座）
- 3.1 声明现状(Properties)：Material Properties/Material Design Data/Design Code(Material)/Design Steel Code/Time Dependent Material(Creep·Comp. Strength)/Section Properties/Section Stiffness Scale Factor/Thickness/Wall Stiffness Scale Factor/Plate Stiffness Scale Factor/Element Stiffness Scale Factor/Effective Width Scale Factor — 已声明/未声明表。
- 3.2 Material Properties(ID/Name/Type/Standard/DB/弹性模量/泊松比/线膨胀系数/重度/阻尼比)、3.3 Design Code、3.4 Material Design Data、3.5 Thickness、3.6 Section Properties(全部 30 个)、3.7 Section Stiffness Scale Factor(fArea/fAsy/fAsz/fIxx/fIyy/fIzz/fWgt/适用 Element 数)。
- 3.9 声明现状(Boundary)：Supports/Point Spring/General Spring/Surface Spring/Rigid Link/Elastic Link/General Link Properties/General Link/Beam End Release/Beam End Offsets/Plate End Release/Linear Constraints/Panel Zone Effects/Diaphragm Disconnect/Boundary Group。
- **3.10 Supports — 最下层全量对照**：将最下层(B1F)标高节点数与 Support 声明节点数进行对照，自动算出未声明节点数（无遗漏等）——同时显示约束模式(Dx Dy Dz Rx Ry Rz Rw)。
- 3.11 Elastic Link(Type/数量)、3.12 Beam End Release(按释放自由度的数量)。

**Chapter 04. Analysis Option**（必用分析选项）
- 原样截取 Main Control Data(Auto Rotational DOF Constraint、Number of Iterations/Load Case、Convergence Tolerance、Consider Section Stiffness Scale Factor for Stress Calculation 等)与 Eigenvalue Analysis Control(Type of Analysis、Number of Frequencies、Eigenvalue Control Parameters)弹窗。
- P-Delta/Buckling/Nonlinear/Construction Stage/Settlement/Heat of Hydration/Moving Load/Pushover/Inelastic Hinge Control 等其余选项标注为"无已声明项"（透明地表明本示例模型中实际并未使用这些选项）。

**Chapter 05. Load**（荷载·风/地震·层间位移·不规则）
- 5.2 Static Load Cases — 按工况整理（计算区分：直接输入/自动计算、已输入荷载详情、Description）、5.3 Dynamic Load Cases(反应谱 RS、角度、谱函数、模态组合 CQC、偶然偏心 5.00%)。
- 5.1 Gravity Load — 按输入菜单的声明矩阵(Self-Weight/Nodal Body Force/Nodal Loads/Element Beam Load/Define Floor Load Type/Finishing Material Loads × DL/LL)。
- 5.2.3 Across Wind — 振动参数(是否考虑 Across Wind、是否考虑 Torsional/Wind Response、建筑宽度、固有频率、质量 M/Mx/My、质量惯性矩 Mt)、5.2.4 风洞试验对象审查（全部楼层，以细长比 λ = H/√(B·D) 为基准判定是否需做风洞试验，自动归类为 Regular/非对象）、5.2.5/5.2.6 按方向的 Story Force·Story Shear。
- **5.4 Story Drift 及不规则评估**：层间位移·稳定系数·不规则审查·RS 楼层剪力 — 5.4.1 Story Drift(X 方向、Maximum Drift of All Vertical Elements、Allowable Story Drift、Drift at the Center of Mass)、5.4.6~5.4.7 考虑偶然偏心的偏心审查（按 RY(RS)+RY(ES) 等组合判定 Regular/Irregular）、Stiffness Irregularity Check(Soft Story，X 方向) — 按楼层全量列出刚度比与判定结果。

### Step 4 — 确认结果并输出

- 用"保存/打印为 PDF"按钮下载最终报告(31 页)，以 Adobe Acrobat 等工具查看。
- 另外单独支持 Excel 输出("Excel 输出"按钮)（画面上未展示详细演示）。

## 6. 关联 JSON API 端点

画面上未显示准确的请求日志（仅显示荷载计算进度消息），但报告中所含各项与 `docs/manual` 的下列端点存在明确对应关系：

| 章节 | 项 | 推测 API | 文档位置 |
| --- | --- | --- | --- |
| 01/02 | Story Data | `GET /db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/zh-cn/02_DB_Project_Structure.md#15-dbstor--story-data) |
| 01/02 | Node/Element 数量、坐标 | `GET /db/NODE`, `GET /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| 01 | 特征值分析结果 | `POST /post/table`(`EIGENVALUEMODE`/`PARTICIPATIONVECTORMODE`) | [`20_POST_AnalysisResult_2.md#28-vibration-mode-shape`](../../manual/zh-cn/20_POST_AnalysisResult_2.md#28-vibration-mode-shape) |
| 03 | Material Properties | `GET /db/MATL` | [`04_DB_Properties.md#1-dbmatl`](../../manual/zh-cn/04_DB_Properties.md#1-dbmatl) |
| 03 | Section Properties | `GET /db/SECT` | [`04_DB_Properties.md#12-dbsect`](../../manual/zh-cn/04_DB_Properties.md#12-dbsect) |
| 03 | Thickness | `GET /db/THIK` | [`04_DB_Properties.md`](../../manual/zh-cn/04_DB_Properties.md) (§13 THIK) |
| 03 | Section Stiffness Scale Factor | `GET /db/ESSF`(Element Stiffness Scale Factor) | [`04_DB_Properties.md#31-dbessf`](../../manual/zh-cn/04_DB_Properties.md#31-dbessf) |
| 03 | Supports | `GET /db/CONS` | [`05_DB_Boundary.md#1-dbcons--constraint-support`](../../manual/zh-cn/05_DB_Boundary.md#1-dbcons--constraint-support) |
| 03 | Elastic Link | `GET /db/ELNK` | [`05_DB_Boundary.md#6-dbelnk--elastic-link`](../../manual/zh-cn/05_DB_Boundary.md#6-dbelnk--elastic-link) |
| 04 | Analysis Control(Main/Eigenvalue) | `GET /db/*`(Analysis Control 系列) | [`12_DB_Analysis_Control.md`](../../manual/zh-cn/12_DB_Analysis_Control.md) |
| 05 | Static/Dynamic Load Cases | `GET /db/STLD`, `GET /db/SPLC` | [`06_DB_Static_Loads.md#1-dbstld--static-load-cases`](../../manual/zh-cn/06_DB_Static_Loads.md#1-dbstld--static-load-cases), [`09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases`](../../manual/zh-cn/09_DB_Dynamic_Loads.md#2-dbsplc--response-spectrum-load-cases) |
| 05 | Story Drift、不规则评估 | `POST /post/table`(Story Drift、`STIFFNESS_IRREGULARITY_X/Y`、Eccentricity 系列) | [`21_POST_StoryTables.md#1-story-drift`](../../manual/zh-cn/21_POST_StoryTables.md#1-story-drift), [`21_POST_StoryTables.md#13-stiffness-irregularity-check-soft-story`](../../manual/zh-cn/21_POST_StoryTables.md#13-stiffness-irregularity-check-soft-story) |

- ⚠️ 3.1 节/3.9 节的"Wall Stiffness Scale Factor"·"Plate Stiffness Scale Factor"是否声明这一项，与 #5(WallStiffnessAuto) 文档中已经确认的情况相同，属于在 `docs/manual` 中未另行文档化专用 GET 端点的项（仅存在以 Element 为单位的 `/db/ESSF`）。该 Plug-in 用哪个 API 查询此项是否声明，未得到确认。
- 该 Plug-in 看起来会汇总调用模型中几乎全部 `/db/*` 查询端点与大量 `/post/table` 结果表格，上表仅整理了画面所显示项中可确认的一部分（⚠️ 并非全量清单）。

## 7. 输入数据规格

- **前置条件**：已完成分析（或部分完成）的 GEN NX 模型。
- **系数输入**：建筑重要性、位移放大系数 C_d、超强系数 Ω_0、冗余度系数。
- **楼层分类**：自动分类出的地下/地上/屋面塔层，必要时由用户直接修改。

## 8. 输出 / 生成结果

- "Modeling Data Report" PDF(共 31 页，5 个章节)。
- 同一批数据的 Excel 形式输出（仅确认到按钮，未演示细节）。

## 9. 限制事项与局限

- 本报告始终是自动对照"是否声明"与"数值一致性"的工具，并不会判断这些值在结构上是否正确（例如材料强度是否符合设计意图）——属于检查清单式的校核辅助工具。
- 除 3.10 节"最底层节点-支座对照"这类已明确确认的自动校验逻辑之外，其余各项是否都经过类似的一致性校验未在画面上得到确认（也存在大量简单罗列型表格）。
- P-Delta/Buckling/Pushover 等未使用的分析选项只显示为"无已声明项"，究竟是"正常地未使用"还是"误漏"，需要工程师另行判断。

## 10. 画面清单

| 时点(秒) | 画面内容 |
| --- | --- |
| 0–16 | 开场旁白，进入 GEN NX 示例模型（公寓 22 层） |
| 16–40 | Plug-in 首次执行、荷载计算日志、Base URL/MAPI-Key 连接 |
| 40–72 | 楼层分类（地下/地上/屋面塔层）修改、系数输入（重要性·C_d·Ω_0） |
| 72–104 | Chapter 01 General — 模型摘要、特征值分析结果、风/地震作用概况 |
| 104–136 | Chapter 02 Structure — Structure Type/Building Control、Story Data、按荷载工况汇总表、Story Mass |
| 136–168 | Chapter 03 Properties & Boundary — 声明现状、Material/Section/Stiffness Scale Factor、Supports 对照、Elastic Link/Beam End Release |
| 168–184 | Chapter 04 Analysis Option — 截取 Main Control/Eigenvalue Control 弹窗 |
| 184–216 | Chapter 05 Load — Static/Dynamic Load Cases、Gravity Load 矩阵、Across Wind、Story Drift、不规则评估(Stiffness Irregularity) |
| 216–224 | 确认 PDF 终版(Adobe Acrobat，31 页)、收尾旁白 |
| 224–230 | 结束卡片 |

---

*下一步：14_GenSnap 视频分析与规划文档撰写。*
