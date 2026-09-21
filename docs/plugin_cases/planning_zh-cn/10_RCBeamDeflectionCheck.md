# RCBeamDeflectionCheck 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/10_RCBeamDeflectionCheck.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 视频（`docs/plugin_cases/videos/10_RCBeamDeflectionCheck.mp4`，60fps，1920×1080，约 192 秒）按
> 7 秒间隔截帧（共 28 张）后，以逐帧目视分析 + 字幕 + Message Window 日志为依据撰写。与原文文章
> （`docs/plugin_cases/articles/10_RCBeamDeflectionCheck.md`）的 4 大功能说明做了交叉确认。产出物
> "挠度结构验算"报告中完整暴露了 KDS 14 20 30 4.2 的计算全过程（Ie,eff、Icr、Mcr、弹性挠度、长期
> 挠度），是计算逻辑验证依据非常强的案例。

## 1. 概述

**RC Beam Deflection Check** 通过 API 读取 MIDAS GEN NX 模型中 RC 梁的截面·材料·配筋与各荷载工况的
分析弯矩，按 KDS 14 20 30 4.2 规定的有效截面二次矩（Ie，Branson 公式）自动计算短期·长期挠度并与
允许挠度比较，输出 A4 结构计算书（挠度验算书）。

## 2. 问题定义

- 结构设计实务中 RC 梁的挠度验算必不可少，但有效截面二次矩（Ie,eff）的确定、开裂截面二次矩（Icr）
  计算、徐变·干燥收缩引起的长期挠度放大系数（λΔ）取值等多步计算，手工反复完成很繁琐。
- GEN NX 模型中已存在的截面·材料·配筋·弯矩信息，为编制验算书还要再誊写一遍，存在效率浪费。

## 3. 目标用户

- 需按 KDS 14 20 30（混凝土结构使用性设计标准）4.2 条验算 RC 梁挠度的结构设计者。
- 需反复编制简支梁·连续梁·悬臂梁等不同支承条件挠度验算书的工程人员。

## 4. 核心概念 / 差异化点

- **模型数据自动获取**：在 GEN NX 建模画面直接选择待验算的梁（"Select beam load" 按钮），该梁的截面
  （b、h）、材料强度（fck、fy）、配筋（As、各排根数·规格）、构件长度（L）全部自动读取。
- **将荷载工况分组为固定荷载/活荷载**：由用户直接映射多个静力荷载工况（DL_self、DL_finish、LL-1、
  LL-2 等）中哪些属于固定荷载（D）、哪些属于活荷载（L），从而构造挠度计算所需的 M_D·M_L·M_D+L·
  M_sus（持续荷载弯矩）。
- **把计算条件作为细部选项暴露**：支承条件（简支梁/连续梁/悬臂梁等）、梁截面（矩形梁/T 形梁）、翼缘
  宽度·厚度（选择 T 形梁时）、短期/长期允许挠度标准（L/360、L/480 等用户自定义）、持续荷载比例（%）、
  加载持续时间（D）（60 个月以上 λ=2.0 等）、保护层厚度、持续荷载方式（遵循 KDS[14 20 30]）均可精细
  调整。
- **反映 T 形梁有效宽度**：除矩形梁外，选择 T 形梁时可输入翼缘宽度（bf）·翼缘厚度（hf）并反映到有效
  截面计算 —— 也包含以不同截面假定复核同一梁构件的演示。
- **NG 时立即修改配筋 → 反映到 GEN NX → 重新验算的闭环**：验算结果为 NG（长期挠度超限）时，在同一
  窗口内直接修改配筋（各排钢筋根数·规格），点击 "Rebar update" 按钮立即反映到 GEN NX 模型（显示
  `✓ GEN NX 已应用`）后再执行重新验算 —— 编制验算书与配筋加强在一屏内即可完成往复。
- **自动生成 A4 挠度验算书**：把 KDS 14 20 30 4.2 的全部计算过程（荷载及弯矩确定 → 是否开裂判定 →
  开裂截面二次矩 Icr 确定 → 有效截面二次矩 Ie,eff 确定 → 弹性挠度 → 长期挠度 → 挠度验算 OK/NG）连同
  表格·公式打印/保存为 A4 单页报告。

## 5. 工作流

### Step 1 — API 连接

- 在 "RC Beam Deflection Check" 窗口输入 `Base URL`、`MAPI Key` 后连接。

### Step 2 — 荷载工况映射及计算条件设置

- 在固定荷载（DL）列表中新增/选择 `DL_self`、`DL_finish` 等，在活荷载（LL）列表中新增/选择 `LL-1`、
  `LL-2` 等（用"+新增"按钮可组合多个工况，注释："添加多个时会一并执行 [M_D = M_D1 + M_D2 ...]"）。
- 计算条件：支承条件（简支梁），梁截面（矩形梁/T 形梁），翼缘宽度·厚度（mm），短期允许挠度（L/360），
  持续荷载率（%，例 50），长期允许挠度（L/480），加载持续时间（D）（例"60 个月以上（λ×2.0）"），
  保护层厚度（mm，例 40），持续荷载方式（例 KDS[14 20 30]）。

### Step 3 — 选择待验算梁并自动获取数据

- 点击 "Select beam load" → 在建模画面选择梁单元（高亮显示）→ "构件名、截面尺寸、混凝土强度、钢筋
  强度、构件长度将自动读取"，并反映到梁构件列表表格（Ele No., Section, b, h, fck, fy, L 列）。
- 用复选框选择待验算的梁后，同时显示该梁的配筋信息（按位置：End(i)/Middle(m)/End(j)，按排的 As
  Top/Bot、钢筋规格下拉框）与固定荷载·活荷载弯矩（Mu_D、Mu_L）。

### Step 4 — 执行挠度验算

- 点击"执行挠度验算" → 新窗口（弹窗）即时生成"挠度验算结果"摘要（例："OK 0 · NG 1"）及按构件的详细
  报告。
- 报告构成（#1 示例 — 8m 简支梁、矩形 600×800、fck 24MPa、fy 500MPa）：
  1. **荷载及弯矩确定**：按位置（Middle）的 M_DL、M_LL、M_D+L、M_sus（持续荷载比 50%）表。
  2. **是否开裂判定**：f_r(=0.63√fck)、I_g(=bh³/12)、M_cr(+)(=f_r·Ig/yt,pos)。
  3. **开裂截面二次矩（Icr）确定**：换算弹性模量比 n(=Es/Ec)、受压侧·受拉侧钢筋量、kd、I_cr(mm⁴)。
  4. **有效截面二次矩（Ie,eff）确定**：KDS 加权平均 `Ie,eff = Iu·m` 方式，按位置 (D)/(D+L)/(sus) 的
     三列表格。
  5. **弹性挠度**：K(D+L) 系数、δ_D+L、δ_D、δ_L = δ_D+L − δ_D。
  6. **长期挠度**：时间发展系数 ξ（按加载持续时间，60 个月以上=2.0）、受压钢筋配筋率 ρ'、λΔ
     (=ξ/(1+50ρ'))、δ_sus、δ_cp+sh(=λΔ·δ_sus)、δ_cp+sh+δ_L(=长期挠度合计)。
  7. **挠度验算**：短期挠度（例 9.64mm < δa=L/360=22.22mm → OK），长期挠度（例 33.65mm <
     δa=L/480=16.67mm 超限 → **NG**，"可见长期挠度需要加强"）。

### Step 5 — NG 时的配筋加强与重新验算

- 在判定为 NG 的梁的配筋表中直接修改各排钢筋规格/根数（例：下部钢筋 5-D22 → 增至 7-D22）。
- 点击 "Rebar update" → 确认已立即反映到建模画面（`✓ GEN NX 已应用`）。
- 重新执行"执行挠度验算" → 配筋增加后按上部钢筋 7-D22（2,710mm²）、下部钢筋 11-D22（8,516mm²）
  重新计算 → 结果转为 OK 1 · NG 0（短期 3.97mm < 22.22mm、长期 15.24mm < 16.67mm，均为 OK）——
  "确认长期挠度不存在问题。"

### Step 6 — 改为 T 形梁截面条件再次演示

- 对第二根梁（10m、矩形 800×800）："该梁将套用 T 形梁有效翼缘宽度·厚度进行验算" —— 把梁截面切换为
  T 形梁，输入翼缘宽度 2500mm·翼缘厚度 150mm 后重新验算。
- NG（初始结果）→ 修改配筋（上部钢筋 10-D22、下部钢筋 6+11-D22 两排配筋等）→ "Rebar update" →
  重新验算 → 确认结果。

### Step 7 — 结果打印/PDF 保存

- "打印/PDF 保存"按钮 → 选择打印机（例 SINDOH D450 或 Microsoft Print to PDF），连同页面·颜色·双面
  打印选项预览验算结果页面后保存/打印。
- 结束字幕："本次演示以简支梁为基准展示，但可以应用到多种工况" —— 暗示连续梁·悬臂梁等其他支承条件
  也可适用同一逻辑（惟实际演示仅以简支梁进行）。

## 6. 关联 JSON API 端点

画面上未以文本暴露确切的端点名称，但 GEN NX Tables 树（Tree Menu 2）中直接显示了 `Design Tables >
Concrete Design > Modify Beam Rebar Data`，Message Window 中原样输出 `Start Writing RC Beam Design
Result to Table` / `Start Writing RC Beam Checking Result to Table` / `End Code Checking by KDS 41
20 : 2022` 日志，可见与 #9（RCRebarOptimizer）中确认的属于同一 RC 设计 API 系列：

| 功能 | 推测 API | 文档位置 |
| --- | --- | --- |
| 梁配筋信息查询/修改（"Rebar update"） | `DESIGN/RC/KDS-41-20-2022/DCRM-BEAM` | [`26_Design_RC_KDS41202022.md#29-designrckds-41-20-2022dcrm-beam--design-criteria-for-rebars-by-beam-member-보-부재별-철근-설계기준`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#29-designrckds-41-20-2022dcrm-beam--design-criteria-for-rebars-by-beam-member-按梁构件的钢筋设计准则) |
| RC 梁设计执行/结果表（弯矩·配筋查询） | `BD-ANAL` / `BD-TABLE` | [`26_Design_RC_KDS41202022.md#39-designrckds-41-20-2022bd-anal--rc-beam-design-perform-rc-보-설계-수행`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#39-designrckds-41-20-2022bd-anal--rc-beam-design-perform-rc-梁设计执行), [`26_Design_RC_KDS41202022.md#40-designrckds-41-20-2022bd-table--rc-beam-design-table-rc-보-설계-테이블`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#40-designrckds-41-20-2022bd-table--rc-beam-design-table-rc-梁设计表格) |
| 截面/构件信息（b、h、L） | `GET /db/SECT`、`GET /db/ELEM` | [`04_DB_Properties.md#12-dbsect`](../../manual/zh-cn/04_DB_Properties.md#12-dbsect), [`03_DB_Node_Element.md#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| 材料强度（fck、fy） | `GET /db/MATL` | [`04_DB_Properties.md#1-dbmatl`](../../manual/zh-cn/04_DB_Properties.md#1-dbmatl) |
| 各荷载工况分析弯矩 | `POST /post/table`（构件内力系列表格） | [`20_POST_AnalysisResult_2.md`](../../manual/zh-cn/20_POST_AnalysisResult_2.md)（Beam Force 系列） |

- ⚠️ 挠度计算本身（Ie,eff、Icr、λΔ 等 KDS 14 20 30 4.2 算式）并非 GEN NX Open API 直接提供的结果，
  而应是 Plug-in 以 API 取到的截面·材料·配筋·弯矩原始数据为基础**自行实现的计算逻辑** ——
  `docs/manual` 中没有直接计算"挠度（Deflection）"的专用 POST 端点，这暗示了该 Plug-in 的核心附加值
  （仅用 API 取数据，计算自行完成）。

## 7. 输入数据规格

- **荷载工况映射**：固定荷载（DL）·活荷载（LL）各指定 1 个以上。
- **计算条件**：支承条件、梁截面类型（矩形/T 形）、短期·长期允许挠度标准（L/n 形式）、持续荷载比例
  （%）、加载持续时间（λ 系数）、保护层厚度（mm）。
- **待验算梁**：在 GEN NX 建模画面直接选择。

## 8. 输出 / 生成结果

- 挠度验算结果摘要（OK/NG 件数）及按构件的详细计算报告。
- 配筋加强时反映到 GEN NX 模型的修改后配筋数据（`DCRM-BEAM`）。
- A4 挠度结构验算书（打印/PDF）。

## 9. 限制事项与局限

- 实际演示仅以简支梁（Simple Beam）支承条件进行，连续梁·悬臂梁等其他支承条件的计算逻辑差异未在画面
  直接确认（字幕仅提及"可以应用"）。
- 挠度计算本身看起来是 Plug-in 而非 API 的自实现逻辑，因此并不保证与 GEN NX 正式计算结果 100% 一致
  （⚠️ 需 Plug-in 自行验证 —— 原文中也没有关于计算正确性的额外保证文句）。
- 持续荷载比例（%）与加载持续时间（λ 系数）需用户自行输入，这些取值是否符合实际设计条件须由工程师
  判断。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–21 | 片头（User Guide，Plug-in Info：Star Love Fish，RC Beam deflection check[KDS]） |
| 21–35 | 进入 GEN NX 模型（Rebar-Beam 示例），首次显示 RC Beam Deflection Check 窗口，服务器连接 |
| 35–70 | 荷载工况（DL/LL）映射，输入计算条件（支承条件、允许挠度、持续荷载率、加载持续时间、保护层厚度） |
| 70–91 | "Select beam load" → 自动获取梁数据、确认配筋、执行挠度验算 → 首个结果（1 号构件，长期挠度 NG） |
| 91–119 | 配筋加强（增加下部钢筋）→ Rebar update → 重新验算 → 确认 OK，准备切换 T 形梁 |
| 119–161 | 输入 T 形梁有效宽度，执行 2 号构件（10m）验算 → 确认 NG |
| 161–176 | 2 号构件配筋加强 → Rebar update → 重新验算 → OK，确认摘要/详细结果切换 |
| 176–189 | 在打印/PDF 保存对话框中预览结果 |
| 189–192 | 结束字幕（"可应用于多种工况"） |

---

*下一步：11_PlantFrameBuilder 视频分析与规划文档撰写。*
