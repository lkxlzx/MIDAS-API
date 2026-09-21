# RCRebarOptimizer 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/09_RCRebarOptimizer.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 视频（`docs/plugin_cases/videos/09_RCRebarOptimizer.mp4`，30fps，1920×1080，约 270 秒）按 9 秒
> 间隔截帧（共 31 张）后，以逐帧目视分析 + Message Window 中显示的 GEN NX 分析日志 + 底部字幕为
> 依据撰写。原文文章（`docs/plugin_cases/articles/09_RCRebarOptimizer.md`）中已明确写有
> "RC 设计 API（DCRM·CD/BD-ANAL·设计结果表）"的表述，因此 API 映射依据从一开始就非常强，且
> Plug-in 画面内的"优化工作原理"说明框也直接公开了详细算法，是本次会话中信息密度最高的案例。

## 1. 概述

**RC Rebar Optimizer** 利用 MIDAS GEN NX 的 RC 设计 API（DCRM·CD/BD-ANAL·设计结果表），将 RC
柱·梁的主筋按候选规格（D19~D32）自动遍历设计，输出满足验算比（CHK）的按构件最小用钢配筋，并把
相同截面（柱标记·梁标记）统一为同一标准配筋的 Plug-in。

## 2. 问题定义

- GEN NX 默认的 RC 设计结果只是对每一根构件计算理论上所需的最小钢筋量，实际施工中该从标准规格
  （例：D19、D22、D25、D29）中选哪几种、各配几根，以及相近截面归并为几种标准类型（统一），仍需
  设计者手工判断。
- 按钢筋直径逐种重新设计全部构件、比较用钢量与施工性的过程，因涉及大量重复计算，手工操作效率很低。

## 3. 目标用户

- 需按 KDS 41 20:2022 设计、算量 RC 柱·梁配筋的结构设计者。
- 需判断标准化配筋类型数（施工性）与钢材总重量（经济性）之间 trade-off 的工程人员。

## 4. 核心概念 / 差异化点

- **候选钢筋遍历 → GEN NX 实际重新设计 → 选取验算比通过的最小规格**："本工具不直接计算钢筋。候选
  配筋逐一输入 GEN NX → 按 KDS 41 20:2022 重新分析·重新设计，在 GEN NX 判定验算通过（CHK OK ·
  验算比 ≤ 目标值）的方案中挑选用钢量最少的配筋。也就是最优搜索 + GEN NX 设计引擎的结合，显示的
  所有配筋都是 GEN NX 实际设计·验算过的值" —— UI 中明确说明这不是纯算法计算，而是反复调用 GEN NX
  自身的设计引擎、只采纳已验证值的方式。这段说明本身就被作为可靠性的核心依据提出。
- **候选钢筋遍历**：对选定的每种规格（D19·D22·D25...），把全部柱/梁主筋设为该规格并由 GEN NX
  重新设计，按规格得到各柱所需的变量（验算比：轴力 Rat-P、弯曲 Rat-M、剪切 Rat-V）。
- **按构件最优**：在每根柱中，于"OK 且验算比 ≤ 目标值"的规格里强制选取用钢量最少的规格作为下限。
- **按截面（柱标记）统一**：同一柱标记必须使用同一配筋，因此统一为该标记下所有柱都满足的最大规格
  （以最不利构件为设计基准）。
- **标准化（自动推荐 + 手动施工便利性调整）**：把互不相同的配筋种类压缩到 N 类型以内（从用钢量增加
  最小的标准起依次归并），各截面"分配到面积 ≥ 所需量的最小标准 → 保守地保证验算比 ≤ 1"。N 由自动
  推荐，但用户也可以在类型数 ↔ 用钢量 trade-off 图中直接点击改变类型数。
- **应用·复验**：点击 [应用到模型] 时，GEN NX 把标准配筋作为设计基准重新设计·重新验算，并实测确认
  全部柱验算比 ≤ 1.0（同时说明暂估值此时可能被重新设计成不同值）—— 即区分"预测值"与"实测值"，且
  必须经过复验。
- **控制因素诊断**：自动诊断并显示各构件的配筋为何由该规格决定（例：`pmin 控制` = 强度富余较大，
  配筋由最小配筋率（1%）决定；`P-M 控制` = 轴力-弯矩相关关系起控制作用）—— 与原文第 3 项功能"还会
  提示哪根构件可以继续削减"一致。
- **柱/梁独立选项卡 + PDF 输出**：分离柱（Column）/梁（Beam）选项卡分别优化，配筋表（可下载 CSV）
  与按截面的详细结果可即时输出 PDF。

## 5. 工作流

### Step 1 — API 连接

- 输入 `服务器 URL`（例：`https://moa-engineers.midasit.com:443/gen`）、`MAPI-Key` 后执行"连接测试"。
- 连接成功时立即反馈识别到的构件数量："连接成功 — 识别到 870 个构件。可以[执行优化]"。

### Step 2 — 优化设置（柱）

- 候选钢筋（多选复选框）：D19、D22、D25、D29、D32。
- 输入目标验算比上限（例：1.00）。
- 提示："标准类型数将自动推荐 — 可在结果的 trade-off 图中点击修改"。

### Step 3 — 执行优化（柱）

- 点击"执行优化" → GEN NX Message Window 中顺序输出实际分析日志：`ENTRY FORM_STIFF_MASS_LOAD` →
  `Analysis is in progress`（Forming Element Stiffness and Load Matrices → Static Analysis →
  Eigenvalue Analysis）→ `Save Model Data for RC Design/Checking` → `Calculate Live Load Reduction
  Factor` → `Calculate Effective Length Factors (Ky & Kz)` → `Start Creating Load Combinations for
  Design/Checking` → 按候选钢筋直径的个数（例：4 次）重复 `Design Rebar of Concrete Column...`
  （Stop Design Thread 进度 %）。
- 完成日志："完成 — 柱 40 个 / 截面 15 层 → 标准 3 类型（自动推荐）· 设计基准已恢复原状"。
- 3 张结果摘要卡片：`MIDAS 设计（基准）3,037.5kg` / `按截面最优 2,559.4kg（−15.7%）` /
  `标准化（3 类型，推荐）2,729.4kg（−10.1%）`。
- **标准配筋类型**卡片（例：Type A 6-D19 400×400，Type B 4-2-D29 500×500，Type C 6-D29 500×600）与
  **配筋表（Rebar Schedule）**（Type/标准配筋/主筋分数式/截面数/柱数/主筋总长/用钢量）—— 支持
  下载 CSV·复制表格。
- **类型数 ↔ 用钢量 trade-off** 柱状图：1 类型（4,115kg，+60.8%）/ 2 类型（3,049.9kg，+19.2%）/
  3 类型（2,729.4kg，+6.6%，当前选择）/ 4 类型（2,559.4kg，+0.0%）—— 用数据直接呈现"类型数越少
  施工越便利、但用钢量越增加"的关系。
- **控制因素诊断**："pmin 控制 13 层 / P-M 控制 2 层" —— pmin 控制意味着强度富余较大、配筋由最小
  配筋率（1%）决定，靠钢筋已难以继续削减，暗示混凝土截面有缩减·调整的余地（结构上被重新设计的截面
  需谨慎复核）。
- **按截面（柱标记）结果**表：构件数、配筋（前→后）、验算比（前→后）、主筋配筋率（前→后）、控制
  因素、判定（OK）。点击行可展开设计详情（轴力/弯曲/剪切验算比、所需钢筋量 Ast、配筋依据、控制因素
  依据）。

### Step 4 — 优化设置·执行（梁）

- 把顶部选项卡切换到"梁（Beam）"—— 与柱相同的 UI 原理，只是候选扩展到上/下部主筋规格（D13~D25）
  与箍筋规格（D10·D13·D16）的两轴组合："组合遍历 —（主筋规格 × 箍筋规格）所有组合对全部梁进行设计，
  并由 GEN NX 重新设计，必要时快速调整所需配筋-箍筋间距-CHK"。
- 候选主筋：D13、D16、D19、D22（D25 按"梁应小于柱"的提示以排除状态演示）。候选箍筋：D10、D13
  （排除 D16）。
- 完成日志："完成 — 梁 175 个 / 梁标记 75 种 → 标准 26 类型 · 设计基准已恢复原状"。
- 结果：`基准设计（柱）15,278.1kg` / `按构件最优 7,951.5kg（−48.0%）` / `梁标记统一（26 类型，
  推荐）8,883.3kg（−41.9%）`。
- 标准梁类型卡片（例：Type A 上 2-D13/下 2-D13 350×600，... Type I 上 3-D13/下 4-D13 350×600）数量
  较多（A~Z 以上，26 种）—— 每张卡片还显示箍筋规格·间距、梁标记数、梁个数。
- **配筋表（Beam Schedule）**：上部钢筋/下部钢筋/箍筋/梁标记数/梁个数/用钢量(kg) 列。
- **按梁标记结果**表：构件数、上部钢筋（前→后）、下部钢筋（前→后）、箍筋（前→后）、用钢量(kg)、
  标准类型、判定。点击行则显示按位置（I 端·跨中·J 端）的弯矩 Mu·所需 As+上部钢筋·正弯矩 Mu·所需
  As+下部钢筋·剪力 Vu(LCB)·箍筋·CHK 等细化依据。

### Step 5 — 应用到模型

- 点击"应用到模型" → 把标准配筋作为设计基准写入（`DCRM`），并通过 GEN NX 重新设计·重新验算（再次
  显示 `Analysis is in progress` 进度窗口）。
- 完成时提示："复验完成 — 应用标准配筋后全部柱安全：最大验算比（正常）0.52 → 应用标准化后 0.52
  （已应用柱 40 个）—— 验算虽有富余，但已由 GEN NX 自身设计确认柱 KDS 验算比 1.0 以下。应用后的
  实际主筋用钢量（GEN NX 重新设计实测）、应用后基准：2,729.4kg —— 与按总长统计的暂估值及实测值均已
  确认。取消标准 → 恢复原设计基准"，并提供"取消应用 — 恢复原设计基准"按钮 —— 可回退。

### Step 6 — PDF 输出

- 点击"PDF 输出" → 通过打印对话框（Microsoft Print to PDF）打印按截面（柱标记）结果表（验算比、
  主筋配筋率、控制因素、判定）与"构件变更 — 全部 40 根柱中 40 根被统一为与原设计不同的配筋，变更
  部分减量 Δ −308.1kg"摘要。

## 6. 关联 JSON API 端点

原文文章与画面（Message Window 日志）中都直接暴露了实际 API 名称，确认依据很强：

| 功能 | 画面/原文表述 | 文档位置 |
| --- | --- | --- |
| 按构件记录钢筋设计基准（确定标准配筋） | `DCRM-COLUMN`（柱），`DCRM-BEAM`（梁） | [`26_Design_RC_KDS41202022.md#30-designrckds-41-20-2022dcrm-column--design-criteria-for-rebars-by-column-member-기둥-부재별-철근-설계기준`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#30-designrckds-41-20-2022dcrm-column--design-criteria-for-rebars-by-column-member-按柱构件的钢筋设计准则), [`26_Design_RC_KDS41202022.md#29-designrckds-41-20-2022dcrm-beam--design-criteria-for-rebars-by-beam-member-보-부재별-철근-설계기준`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#29-designrckds-41-20-2022dcrm-beam--design-criteria-for-rebars-by-beam-member-按梁构件的钢筋设计准则) |
| RC 柱设计执行/结果表 | `CD-ANAL` / `CD-TABLE` | [`26_Design_RC_KDS41202022.md#42-designrckds-41-20-2022cd-anal--rc-column-design-perform-rc-기둥-설계-수행`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#42-designrckds-41-20-2022cd-anal--rc-column-design-perform-rc-柱设计执行), [`26_Design_RC_KDS41202022.md#43-designrckds-41-20-2022cd-table--rc-column-design-table-rc-기둥-설계-테이블`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#43-designrckds-41-20-2022cd-table--rc-column-design-table-rc-柱设计表格) |
| RC 梁设计执行/结果表 | `BD-ANAL` / `BD-TABLE` | [`26_Design_RC_KDS41202022.md#39-designrckds-41-20-2022bd-anal--rc-beam-design-perform-rc-보-설계-수행`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#39-designrckds-41-20-2022bd-anal--rc-beam-design-perform-rc-梁设计执行), [`26_Design_RC_KDS41202022.md#40-designrckds-41-20-2022bd-table--rc-beam-design-table-rc-보-설계-테이블`](../../manual/zh-cn/26_Design_RC_KDS41202022.md#40-designrckds-41-20-2022bd-table--rc-beam-design-table-rc-梁设计表格) |
| 结构分析（每种候选规格重新分析） | `POST /doc/ANAL` | [`01_DOC.md#11-docanal--perform-analysis`](../../manual/zh-cn/01_DOC.md#11-docanal--perform-analysis) |

- 原文文章本身就写明"RC 设计 API（DCRM·CD/BD-ANAL·设计结果表）"，视频的 Message Window 中也原样
  显示出 `Save Model Data for RC Design/Checking`、`Calculate Live Load Reduction Factor`、
  `Calculate Effective Length Factors (Ky & Kz)`、`Design Rebar of Concrete Column...`、
  `Start Design by KDS 41 20 : 2022` 等 GEN NX RC 设计流水线的实际内部处理阶段日志，因此本文档相比
  之前的案例，API 映射可信度尤其高。
- ⚠️ 按候选钢筋直径遍历是否为每次 POST 更新 `DCRM-COLUMN`/`DCRM-BEAM` 之后再重新执行 `CD-ANAL`/
  `BD-ANAL`，其确切调用顺序（以及每次重复对应的 API 调用次数）未在画面中暴露，属于推测。

## 7. 输入数据规格

- **候选钢筋规格**（多选）：柱 D19/D22/D25/D29/D32，梁主筋 D13/D16/D19/D22/D25，梁箍筋
  D10/D13/D16。
- **目标验算比上限**：例 1.00。
- **前置条件**：GEN NX 模型中必须已定义 RC 柱·梁构件与 KDS 41 20:2022 设计条件（连接时以"识别到
  870 个构件"自动确认）。

## 8. 输出 / 生成结果

- 标准化后的柱/梁配筋类型卡片及配筋表（CSV）。
- 用钢量比较（基准设计 vs 按构件最优 vs 标准化）及类型数-用钢量 trade-off 数据。
- 按截面（柱标记）/按梁标记的详细结果表（验算比、控制因素、设计依据）。
- 反映到 GEN NX 模型中的实际 `DCRM-COLUMN`/`DCRM-BEAM` 设计基准（应用到模型时）。
- PDF 产出物（按截面结果表 + 变更摘要）。

## 9. 限制事项与局限

- 标准化所显示的削减值是"暂估值"，只有在 [应用到模型] 阶段由 GEN NX 实际重新设计·重新验算之后才
  确定为"实测值" —— UI 自身发出警告，提示不要把标准化画面的数值误认为最终确认值。
- pmin 控制构件意味着靠钢筋已无进一步削减的余地、必须削减混凝土截面本身，但该 Plug-in 不处理截面
  尺寸变更，仅提供诊断。
- 梁的候选组合按（主筋规格 × 箍筋规格）的全组合遍历，因此 UI 中明确提示"大模型需要较长时间" ——
  组合数越多计算成本越大的结构。
- 原文介绍"通过 PDF 输出，大幅缩短设计·算量·验算文档的编制时间"，但视频中仅确认到柱结果的 PDF
  输出画面，梁结果的 PDF 输出画面在帧采样中未被明确捕捉（⚠️ 未确认，推测由同一按钮支持）。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–9 | 片头标题（RC Rebar Optimizer，KDS 41 20:2022） |
| 9–45 | 首次显示 RC Rebar Optimizer 面板、"优化工作原理"说明框、API 连接·连接测试 |
| 45–63 | 输入优化设置（候选钢筋、目标验算比上限），点击"执行优化" |
| 63–99 | GEN NX 分析/RC 设计日志推进（Analysis in progress，Design Rebar of Concrete Column...） |
| 99–126 | 柱优化结果（摘要卡片、标准配筋类型、配筋表、类型数 trade-off 图、控制因素诊断） |
| 126–144 | 切换到梁选项卡、设置候选主筋·箍筋、点击"执行优化" |
| 144–216 | 梁优化结果（摘要卡片、标准梁类型、配筋表、按梁标记详细结果） |
| 216–234 | "应用到模型" → GEN NX 重新设计·复验 → 复验完成提示 |
| 234–261 | "PDF 输出" → 在打印对话框中确认按截面结果表 |
| 261–270 | 收尾 |

---

*下一步：10_RCBeamDeflectionCheck 视频分析与规划文档撰写。*
