# WallStiffnessAuto 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/05_WallStiffnessAuto.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据视频（`docs/plugin_cases/videos/05_WallStiffnessAuto.mp4`，30fps，1920×1080，约 134 秒）以 6 秒
> 间隔抓取帧（共 23 张）后逐帧目视分析 + 视频内字幕（旁白字幕）作为依据
> 编写。与原文文章（`docs/plugin_cases/articles/05_WallStiffnessAuto.md`）的四大功能说明交叉
> 核对过。本视频是演示幻灯片与 GEN NX 实际屏幕录制相结合的演示形式，尤其最后
> "总结·扩展"幻灯片上以文本形式原样展示了实际使用的 API 列表，因此相比其他 Plug-in
> API 映射依据更强。

## 1. 概述

**WallStiffnessAuto** 是通过 GEN NX API 直接查询 RC 墙体设计（KDS-41-20-2022）结果，对超出设计
基准（NG）的墙体，自行逐步降低其刚度增减系数（WSSF，Wall Stiffness Scale Factor），直至全部 NG
消除为止、反复收敛的 Plug-in。程序自动重复"结构分析 → 墙体设计·审查 → 提取 NG →
降低刚度系数"这一 4 步循环，直到 NG 为 0。

## 2. 问题定义

- 在初期建模阶段，刚度较大的墙体其设计应力比常常超出基准（NG），此时
  实务人员会随意调低该墙体的刚度 → 重新分析 → 重新进行设计审查，直到 NG 消失为止
  手动调整数值。
- 这类反复调整作业随墙体数量增多而（视频示例为多高层建筑，NG 5 项 → 起始对象单元 24 个）
  耗时越长，是典型需要人工介入的重复作业。

## 3. 目标用户

- 按 KDS-41-20-2022 基准执行 RC 墙体设计，需通过降低刚度（反映开裂截面等）来消除
  NG 的结构设计者。
- 尤其是墙体数量多、反复调整耗时大的项目（如墙式结构）的实务人员。

## 4. 核心概念 / 差异化点

- **分析→设计→提取→降低 4 步自动循环**：将结构分析（POST doc/ANAL）→ 墙体设计·审查（WD/
  WC-ANAL）→ 提取 NG（WD/WC-TABLE）→ 降低刚度系数（PUT db/WSSF）绑定为一个循环，在 NG 为 0
  之前由程序自动重复。人员只需设置后按下开始按钮。
- **降低条件参数化**：以每次减小量（Step）、系数下限、最大重复次数这 3 个参数
  控制自动重复的范围——为避免无限降低而设置下限，并为重复无法结束的情形预留最大
  次数上限。
- **历史自动记录**：每次重复将 NG·应力比·应用系数自动保存为画面表格与 CSV 文件，
  以便事后追溯·验证。
- **即时还原**：已降低的系数可用一个按钮还原到降低前的数值（1.0），试错
  成本低。
- **通用扩展设计**：演示者本人认识到"墙体（WSSF）与梁（ESSF）的刚度 API 互不相同，需按构件种类分支"，
  并将墙体·梁各自不同的刚度 API·NG 判定单位设计为在同一套自动重复结构上
  运行——实际上在总结幻灯片中明确注明梁刚度自动调节（ESSF）功能将于 2026-08-03 更新追加。

## 5. 工作流

### Step 1 — 连接 API

- 在 Plug-in 窗口输入 `BASE_URL`、`MAPI-KEY`（字幕："① 输入 BASE_URL 与 MAPI-Key"）。
- 从设计基准显示栏自动显示 `KDS-41-20-2022 (RC Wall)` 来看，墙体审查基准已固定于
  该代码。

### Step 2 — 设置降低条件

- ② 设置每次减小量（Step）、系数下限、最大重复次数这 3 个字段。
- 视频示例值：每次减小量 0.1，系数下限 0.3，最大重复次数 10。

### Step 3 — 开始自动重复

- ③ 点击"开始自动重复"按钮 → 将下述 4 步按设定的次数自动重复：
  1. **执行结构分析**（`POST doc/ANAL`）— GEN NX 内显示"Analysis is now completed"进度
     状态窗（Forming Element Stiffness and Load Matrices → Static Analysis → Eigenvalue
     Analysis → Response Spectrum Analysis）。
  2. **墙体设计·审查**（`WD/WC-ANAL`）— "Start Design by KDS 41 20 : 2022"进度状态窗
     （按 Design Relief of Concrete Wall → Check Complete Wall → Converting Design Results →
     Creating design result file 的顺序推进）。
  3. **提取 NG**（`WD/WC-TABLE`）— 将每次重复的 NG 对象墙体列表以表格（楼层、Wall ID、ID、主控应力比、
     最大应力比、重复次数、应用系数）显示。例："第 1 次重复 NG 历史（例：仅墙体对象结果）"表中
     显示 `1F/13`、`2F/22`、`1F/24`、`2F/46`、`1F/72` 等。
  4. **降低刚度系数**（`PUT db/WSSF`）— 以各构件当前刚度系数进度条可视化降低进度。
- 重复日志示例："Create Load Combination : 164"、"End Creating Load Combinations for Design/
  Checking."、"Start Design by KDS 41 20 : 2022"、"End Design by KDS 41 20 : 2022"— 这 4 条
  日志的循环在每次重复中重新出现。

### Step 4 — 确认结果

- ④ 重复结束后，通过"设计完成"提示弹窗确认结果。若 NG 仍然存在，则以"已达到最大重复次数"
  提示另行告知（即两种结束条件：NG=0 达成，或达到最大重复次数）。
- 树菜单中生成了 `Wall Stiffness Scale Factor` 分组，`Type 1 | Group=Default; Shear=0.7;
  Bending=0.7` 这样的按组最终降低系数被保留，可供审查。

### Step 5 — 输出 NG 历史 CSV

- 提供记录每次重复的 NG 构件·应力比·应用系数的 CSV 文件作为产出成果。

## 6. 关联 JSON API 端点

**"总结·以及扩展"幻灯片上以文本形式原样显示**了实际使用的 GEN NX API 列表，
因此对本 Plug-in 的映射并非推测，而是基于画面上直接确认到的依据，属于少见的案例。

| 界面显示 | 用途（界面显示） | 文档位置 |
| --- | --- | --- |
| `POST doc/ANAL` | 执行结构分析 | [`01_DOC.md#11-docanal--perform-analysis`](../../manual/zh-cn/01_DOC.md#11-docanal--perform-analysis) |
| `POST WD/WC-ANAL` | 墙体设计与配筋审查 | [`26_Design_RC_KDS41202022.md#63-designrckds-41-20-2022wc-anal--rc-wall-check-perform-rc-벽체-검토-수행`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#63-designrckds-41-20-2022wc-anal--rc-wall-check-perform-rc-墙体验算执行) |
| `POST WD/WC-TABLE` | 查询 NG 构件·应力比 | [`26_Design_RC_KDS41202022.md#64-designrckds-41-20-2022wc-table--rc-wall-check-table-rc-벽체-검토-테이블`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#64-designrckds-41-20-2022wc-table--rc-wall-check-table-rc-墙体验算表格) |
| `GET db/ELEM · NODE · STOR` | 单元·楼层映射 | [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode), [`#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem), [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/zh-cn/02_DB_Project_Structure.md#15-dbstor--story-data) |
| `GET / PUT db/WSSF` | 查询·应用刚度增减系数 | ⚠️ 本仓库的 `docs/manual` 中没有 `/db/WSSF` 专用端点文档（见下文） |
| `GET view/SELECT` | 读取所选构件 | [`16_VIEW.md#1-viewselect--select`](../../manual/zh-cn/16_VIEW.md#1-viewselect--select) |

- ⚠️ **关于 `/db/WSSF` 的重要发现**：`docs/manual` 中只文档化了名称相似的 `/db/ESSF`（Element Stiffness
  Scale Factor，[`04_DB_Properties.md#31-dbessf`](../../manual/zh-cn/04_DB_Properties.md#31-dbessf)），
  而它是按单元（Element）单位直接指定 `AREA_SF`/`ASY_SF`/`IYY_SF`/`IZZ_SF` 等的方式。
  另一方面，视频中的 GEN NX 树菜单里另有 `Wall Stiffness Scale Factor` 条目，
  以 `Type N | Group=...; Shear=x; Bending=y` 的形式管理**按组的剪切/弯曲刚度
  系数**——与 `/db/ESSF` 的按单元轴力/扭转/弯曲/剪切/自重 6 种系数结构不同。
  `12_DB_Analysis_Control.md:2384` 的分析控制选项表中存在 `"bWSSF"`（是否使用 Wall Stiffness Scale
  Factor 的 Boolean），`12_DB_Analysis_Control.md:2600` 的缩写表中存在 `"WSSF"` = Wall
  Stiffness Scale Factor，术语本身是有的，但按组 GET/PUT 该值的专用
  端点（`/db/WSSF`）在本仓库中尚未文档化。也就是说，画面上显示的这一 API
  名称看来确实存在（开发者明确写为 "GET / PUT db/WSSF"），但属于本仓库
  手册覆盖范围的空白（gap），需另行确认。

## 7. 输入数据规格

- **前置条件**：RC 墙体已按 KDS-41-20-2022 基准定义完毕，且须已设置反应谱分析
  荷载工况（进度状态窗中包含 Eigenvalue Analysis、Response Spectrum
  Analysis）。
- **降低条件参数**：每次减小量（Step，例 0.1）、系数下限（例 0.3）、最大重复次数
  （例 10）。

## 8. 输出 / 生成结果

- GEN NX 模型中 `Wall Stiffness Scale Factor` 按组的最终刚度系数（Shear/Bending）。
- 每次重复的 NG·应力比·应用系数历史 CSV 文件。
- "设计完成"或"已达到最大重复次数"提示。

## 9. 限制事项与局限

- 总结幻灯片中开发者本人提到的 3 项技术挑战：
  1. 墙体（WSSF）与梁（ESSF）的刚度 API 互不相同，需按构件种类进行分支处理。
  2. NG 结果以"Wall ID + 楼层"为单位输出，因此需要一个通过节点坐标推断楼层并映射到实际单元
     的过程（即 NG 结果本身不会直接落到 element ID 上）。
  3. 需自动判别刚度降低不生效（不收敛）的构件（轴力·弯曲主导），以防止无限重复。
- 当前（视频制作时点）仅完成墙体（WSSF）刚度自动调节，梁（ESSF）刚度自动调节为
  "预定 26.08.03 更新"，当时仍在单独开发中（⚠️ 以视频制作时点为基准—是否实际
  发布需在本文档编写时点重新确认）。
- 即使达到最大重复次数，NG 仍可能残留，此时程序无法自动解决，仅显示"已达到最大重复次数"
  提示—最终判断由工程师负责。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–6 | 片头 — 参赛作品/昵称/功能一句话摘要 |
| 6–12 | THE SOLUTION — 4 步循环（结构分析→墙体设计·审查→提取 NG→降低刚度系数）示意图，点击一次/历史自动记录/即时还原 |
| 12–18 | 自动重复执行 UI 说明（确认 NG 构件·应力比，设置降低条件，NG 消除·系数历史 CSV） |
| 18–132 | 实操演示（完整演示视频，从连接服务器到确认结果）：连接 API → 设置降低条件 → 开始自动重复 → 分析/设计/提取 NG/降低刚度 重复 N 次（大量日志·进度状态窗）→ "设计完成"提示 |
| 132–134 | SUMMARY — 使用的 6 种 GEN NX API、3 项技术挑战、后续更新（梁 ESSF）、通用性说明 |

---

*下一步：06_WallHelper 视频分析与规划文档编写。*
