# AutoGenerationCmFactor 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/04_AutoGenerationCmFactor.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据对视频(`docs/plugin_cases/videos/04_AutoGenerationCmFactor.mp4`, 30fps, 1920×1080, 约 189秒)按
> 8秒间隔抓取帧（共 24张）后的逐帧目视分析 + 视频内字幕（旁白字幕）撰写。与其他视频不同，本
> 视频是屏幕录制之上叠加字幕卡片的发表资料形式，并与原文
> 文章(`docs/plugin_cases/articles/04_AutoGenerationCmFactor.md`)的四大功能说明交叉
> 确认。形式上由发表者（参赛者昵称 "제로"）以开发意图 → 实际演示 → 后记（不足之处）三部
> 构成进行讲解。

## 1. 概述

**AutoGenerationCmFactor** 是按 KDS 41 17 00 标准自动计算 MIDAS GEN NX 生成荷载组合时所需地震作用的
**Cm Factor（修正系数，Scale-up Factor）**的 Plug-in。通过 API 读取模型中已输入的值，自动填写计算
所需项目，并输出包含计算依据的计算书(.OUT)。

## 2. 问题定义

- 姊妹程序 **MIDAS ADS** 具备针对反应谱荷载工况的 Modification Factor(Scale-up Factor) 计算功能
  (`Modification Factor(Scale-up Factor) for Response Spectrum Load Cases`)，但
  **MIDAS GEN NX 本身完全没有针对动力地震作用的修正系数计算功能。**
- 作为替代，GEN NX 用户为求取该修正系数必须手工编写单独的计算书，此过程中要把多个数值（有效重量、
  加速度、场地类别、固有周期等）逐一从模型中抄录，容易出现误输入等人为误差。
- 开发者评论（字幕）："为尽量减少此过程中各数值的误输入等人为误差，制作了本插件。"

## 3. 目标用户

- 需按 KDS 41 17 00（建筑抗震设计标准）基准，对反应谱分析结果施加地震作用修正系数（Cm Factor）
  并生成荷载组合的结构设计者。
- 需判断并适用 KDS 41 17 00 4.2.2 条例外条款(2)·(3)（涉及基岩深度·场地平均剪切波速等）的实务人员。

## 4. 核心概念 / 差异化点

- **模型数据自动取得（"获取"）**：有效重量基准层（含/不含地下层）、建筑物高度、短周期加速度(SDS)、
  1秒周期加速度(SD1)、有效地面加速度(S)、场地类别、重要性系数(Ie)、反应修正系数(R)、特征值分析
  周期(Td,x/Td,y) — 这 9 个项一次通过 API 从模型中载入。
- **KDS 41 17 00 4.2.2 (2)·(3) 例外条款自动判定**：基岩深度超过 20m 且场地平均剪切波速为 360m/s
  以上时自动适用 Fv 的 80%，场地类别为 S5 且基岩深度不明时自动适用 Fa·Fv 的 110% — 用户无需亲自
  判断规范条款，只要留空即自动计算（"即使将 11 号项留空输入，也会按该标准自动算出 Fa,Fv"）。
- **按骨架形式选择规范公式**：近似固有周期计算式(Ta = Ct·hn^x)的系数(Ct, x)，可从钢筋混凝土抗弯
  框架/钢抗弯框架/钢偏心支撑框架及防屈曲支撑框架/钢筋混凝土剪力墙结构·其他骨架 4 种中选择，
  反映了规范公式随骨架形式而不同这一点。
- **质量参与系数周期的工程师再确认警告**：特征值分析周期(Td,x/Td,y)虽自动取入振型表中各方向的
  周期，但画面上常时显示"质量参与系数的主要方向周期属工程师判断，务必再次确认"这一警告文案 —
  明确指出自动化并不替代工程判断。
- **自动计算依据计算书(.OUT)**：把计算所用的全部数值与推导过程，按与 MIDAS ADS 修正系数计算依据
  计算书相同的格式输出，使复核者可追溯依据。

## 5. 工作流

### Step 1 — 连接 API

- 在 Plug-in 窗口顶部输入 `Base URL`、`MAPI-Key`。

### Step 2 — 1. CONDITION：模型数据自动取得

点击"获取"按钮时，下列 9 个项自动由模型填入（依据字幕）：

| No. | 项目 | 自动取得来源（依据字幕） |
| --- | --- | --- |
| 有效重量基准层 | 选择含/不含地下层（下拉） | 用户选择 |
| 1) 建筑物高度 (hn) | Story 最高层高度 | `Story Data` 的最高层(Roof) `Level(m)` |
| 2) 有效重量 (W) | Weight Sum(RX, RY) 的总荷载（地上层或地下层） | 反应谱分析结果的分层 Weight Sum 表 |
| 3)–8) SDS, SD1, S, 场地类别, Ie, R | （视频中未直接显示取得路径，推测为地震作用定义数据） | ⚠️ 未确认 |
| 9) 特征值分析周期 (Td,x / Td,y) | 振型(Eigenvalue Analysis / Modal Participation Masses)表中各方向的周期 | 特征值分析结果表 |

- 10) 规范公式（手动输入）：从 4 种骨架形式中选择（自动显示 Ct、x 系数）。
- 11) 至普通岩深度 / 12) 剪切波速（手动输入，可选）：留空则按 KDS 41 17 00 4.2.2 (2)·(3) 条款
  基准自动算出 Fa/Fv。

### Step 3 — Scale Up Factor(Cm) 计算

- 点击"计算"按钮 → 自动计算并比较静态基底剪力(Vs, X/Y)与动力基底剪力(Vd, X/Y)，最终算出
  Cm Factor(X/Y)。
- 视频示例结果：Vs(X)=15710.30kN, Vs(Y)=15710.30kN, Vd(X)=11885.45kN, Vd(Y)=11575.40kN →
  **Cm Factor X=1.1235, Y=1.1536**。

### Step 4 — 输出计算书(.OUT)

- 点击"计算书"按钮 → 下载 `Cm_Factor_Report.out` 文件。
- 用 MIDAS/Text Editor 打开该文件，即生成与 MIDAS ADS 修正系数计算依据计算书相同的格式（设计
  标准、地震分区、有效地面加速度、场地类别、常数场地放大系数、短周期·1秒周期设计谱加速度、
  重要性系数、反应修正系数、抗震设防类别、建筑物基本振动周期(特征值分析)、地震反应系数(Cs)、
  静态/动力基底剪力、Scale-up Factor）。

## 6. 关联 JSON API 端点

视频中未显示准确的请求/响应 payload，但取得数值时显示的窗口（Story Data 窗口、Vibration Mode
Shape 结果表、Story Shear Force Coefficient 结果表）可清晰识别，故可推测为下列端点：

| 取得项目 | 推测 API | 文档位置 |
| --- | --- | --- |
| 建筑物高度(hn)、Story 列表 | `GET /db/STOR` | [`02_DB_Project_Structure.md#15-dbstor--story-data`](../../manual/zh-cn/02_DB_Project_Structure.md#15-dbstor--story-data) |
| 有效重量(W)、Weight Sum X/Y | `POST /post/table` (`TABLE_TYPE: STORY_SHEAR_FORCE_COEFFICIENT`) | [`21_POST_StoryTables.md#4-story-shear-force-coefficient-rs-analysis`](../../manual/zh-cn/21_POST_StoryTables.md#4-story-shear-force-coefficient-rs-analysis) |
| 特征值分析周期(Td,x, Td,y) | `POST /post/table` (`TABLE_TYPE: EIGENVALUEMODE` 或 `PARTICIPATIONVECTORMODE`) | [`20_POST_AnalysisResult_2.md#28-vibration-mode-shape`](../../manual/zh-cn/20_POST_AnalysisResult_2.md#28-vibration-mode-shape) |
| 静态/动力基底剪力(Vs, Vd) | `POST /post/table` (`TABLE_TYPE: STORY_SHEAR_FOR_RS` 等，与静态地震作用结果的比较) | [`21_POST_StoryTables.md#3-story-shear-force-rs-analysis`](../../manual/zh-cn/21_POST_StoryTables.md#3-story-shear-force-rs-analysis) |

- ⚠️ 上表的映射依据画面所显示结果表的列构成（Story/Spectrum/Shear Force X·Y/Weight Sum X·Y/
  Story Shear Force Coefficient X·Y — 视频 t=80s 前后的表格与 `21_POST_StoryTables.md` §4 的
  Response HEAD 完全一致）已获确认，但本 Plug-in 实际调用的请求体（TABLE_NAME、
  LOAD_CASE_NAMES 等）未在画面上显示，故属推测。
- SDS/SD1/S/场地类别/Ie/R（3~8 号项）画面上只见点击一次"获取"按钮即批量填入的场景，其来源 UI 并未
  另行显示，因此推测为 `/db/*` 系列的地震作用定义端点（例：静态地震作用数据）调用，但不予特定
  指明（⚠️ 未确认）。

## 7. 输入数据规格

- **前置条件**：GEN NX 模型中必须已存在 Story Data、静态地震作用（等效静力法）、反应谱(RS)荷载
  工况、特征值分析（振型分析）结果。
- **规范公式选择**：4 种骨架形式中必须选择 1 个。
- **可选输入**：至普通岩深度(m)、平均剪切波速 — 未输入时按 KDS 41 17 00 4.2.2 (2)·(3) 自动判定。

## 8. 输出 / 生成结果

- Scale Up Factor(Cm Factor) 的 X/Y 值（画面显示）。
- `Cm_Factor_Report.out` 计算书文件（可用 MIDAS/Text Editor 查阅，与 MIDAS ADS 同一格式）。

## 9. 限制事项与局限

- 开发者亲自指出的 2 处不足之处（后记）：
  1. 到"荷载组合自动生成"的修正系数输入部分为止并未自动反映 — 即本 Plug-in 只算出 Cm Factor，
     并未实现把该值自动推入 GEN NX 荷载组合自动生成功能的联动。
  2. 保存计算书(.OUT)文件后也不会自动用 MIDAS/Text Editor 打开，需用户以其他程序手动打开。
- 从设计上看仅适用于 KDS 41 17 00 标准，推测不适用于其他设计标准（代码）（视频全程只涉及该标准）。
- 明确附有警告：以质量参与系数为基准的主要方向周期，不要照原样信任自动计算值，应由工程师再次
  确认 — 其定位并非完全自动化，而是辅助判断的工具。

## 10. 画面清单

| 时点(秒) | 画面内容 |
| --- | --- |
| 0–8 | 片头卡片（参赛作品/参赛者昵称） |
| 16–40 | 1. 开发意图 — MIDAS ADS 有而 GEN NX 没有的修正系数计算功能、手工编写计算书的繁琐 |
| 48–56 | 2. 插件运行视频 — 整体 UI 首次显示（CONDITION 9 个项 + Scale Up Factor 计算区） |
| 64–96 | 点击"获取" → 1~9 号项自动填入，说明 Story Data/Weight Sum/Eigenvalue 结果表中的数值来源 |
| 104–120 | 质量参与系数周期再确认警告，按骨架形式说明规范公式(Ct, x) |
| 128–136 | 11)·12) 至普通岩深度/剪切波速手动输入字段，KDS 41 17 00 4.2.2 条款说明 |
| 144–152 | 点击"计算" → 算出 Cm Factor，点击"计算书" → 下载并确认 .OUT 文件 |
| 160–184 | 3. 后记 — 2 处不足之处（荷载组合自动生成未联动、.OUT 未自动打开） |
| 184–189 | 结束卡片（淡出） |

---

*下一步：05_WallStiffnessAuto 视频分析与规划文档撰写。*
