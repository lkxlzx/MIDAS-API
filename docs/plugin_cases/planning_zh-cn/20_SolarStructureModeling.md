# SolarStructureModeling 规划文档

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../planning/20_SolarStructureModeling.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> 依据视频（`docs/plugin_cases/videos/20_SolarStructureModeling.mp4`，30fps，1920×1080，约179秒）
> 按8秒间隔截帧（共23张）后逐帧目视分析，并以字幕（推测为 VREW 自动生成的字幕）为依据撰写。已与
> 原文文章（`docs/plugin_cases/articles/20_SolarStructureModeling.md`）的4大功能说明交叉确认。这是
> 本会话所处理的20个案例中最后一个，风荷载计算依据（KDS 41 12:00:2022）按算式步骤原样显示在画面
> 上，荷载自动计算逻辑的透明度非常高。

## 1. 概述

**Solar Structure Modeling** 是在 MIDAS GEN NX 中选择太阳能结构形式（CASE 1~4）并输入尺寸·材料·
截面后，向 GEN NX 模型自动生成节点、梁单元与边界条件的 Plug-in。只需输入安装形式与主要尺寸，柱·
屋面梁·支撑·檩条等所有组成部件的节点与单元即自动计算并生成，重力荷载（固定·活·雪荷载）乃至基于
KDS 的风荷载也自动计算·施加。

## 2. 问题定义

- 太阳能结构（单柱式·1跨·多跨·屋顶安装式）是由柱·屋面梁·支撑·檩条等多种构件重复布置而成的定型化
  结构，但手工建模在节点编号计算、构件坐标确定、边界条件输入等重复工作上耗时较多。
- 太阳能结构的风荷载须按 KDS 41 12:00:2022 区分骨架用与外装材用分别计算，而该计算本身较为复杂，
  手工操作容易出错。

## 3. 目标用户

- 用 GEN NX 反复建模太阳能发电结构物（地面支架、屋顶安装式等）的结构设计人员。
- 需要明确留下按 KDS 41 12:00:2022 计算风荷载依据的现场人员。

## 4. 核心概念 / 差异点

- **4种安装形式（CASE）选择式模板**：在 CASE 1（单柱式太阳能结构）、CASE 2（1SPAN 太阳能结构）、
  CASE 3（多SPAN 太阳能结构）、CASE 4（屋顶式太阳能结构）中，用图形图标选择与实际分析太阳能模块
  相同的形式——依形式不同，其后的输入字段构成本身也随之改变。
- **材料·截面直接从 GEN NX 读取**：用“从 GEN NX 读取”按钮，可将当前模型中已定义的材料·截面分别
  指派到 材料（全部）/柱截面/屋面梁截面/支撑截面/檩条截面 这5个槽位——提供了不新建定义而复用既有
  标准构件的路径。
  （若尚无材料·截面，视频也演示了先在 GEN NX 原生 `Material Data`/`Section Data` 窗口中新建定义、
  再重新读取的流程。）
  - 本例所定义的材料：SS275（钢材），柱截面 B100×100×2.3（方钢管），屋面梁截面 B100×100×2.3，
    支撑/檩条截面 LC-100×50×20×2.3（轻型型钢 Cold Formed Channel）。
- **立面图·背面图实时预览**：输入的所有尺寸（柱高 H、倾角 θ、屋面梁长度 RL/RR、支撑1（方钢管，
  TRUSS）·支撑2（右侧，TRUSS）的构件高度·角度、檩条 PIN 数、Y方向排数·排间距、横向支撑下端/上端
  高度）在输入的瞬间即刷新左侧立面图·背面图，可直观确认形状（图例：柱/屋面梁/支撑(TRUSS)/檩条以
  颜色区分）。
- **边界条件预设**：将柱底节点以“铰（平动约束，转动自由）”等预设方式选择。
- **荷载值自动生成（固定·活·雪荷载）**：勾选“自动生成面荷载”后，以 kN/m² 为单位输入固定荷载
  （Dead Load）·活荷载（Live Load）·雪荷载（Snow Load），按 One-Way 分配（加载方向）·水平投影
  基准自动施加。
- **KDS 41 12:00:2022 风荷载完全自动计算**：勾选“自动生成风荷载”后，只输入基本风速（Vs）与地面
  粗糙度类别，即反映模块形状（倾角 12.0°、裸骨架率等），自动算出4个工况（WL1 β=0° A/迎风面、
  WL2 β=0° B/背风面、WL3 β=180° A/反向风、WL4 β=180° B/反向风）的迎风/背风净压力系数
  （C_NW/C_NL）与设计压力（P_W/P_L）。
  - 用**“计算书输出”按钮**可展开查看全部计算依据，实际显示的计算步骤为：
    1. 基本输入值（基本风速 Vs、地面粗糙度类别、平均高度 H、屋面宽度最远端截面 b、倾角、X/Y方向
       基本风、檐口高度（屋面梁间距）、屋面梁的跨度）。
    2. 地面粗糙度系数（KDS 表 5.4-3）：K_D 风向系数、K_zt 地形系数、I_w 重要性系数、C_r 结构系数、
       n_Rb 基本自振频率。
    3. 净压力系数 C_N（β=12.0° 插值）与设计压风压 — 按 WL1~WL4 工况的 C_NW（迎风）·C_NL（背风）·
       P_W·P_L 表。
    4. MIDAS GEN NX 输入区域划分：1区（坡度较高一侧，检验较高部位）/ 2区（补充区域，检验较低
       部位）— 整理各区域把哪个 WL 工况的计算值代入 GEN NX 输入值。
    5. 裸骨架结构荷载 — 柱设计速度压（q_h × G_pa）、柱截面宽度 d、线荷载 W（=P_F × d）。
  - 并以“计算书当然也可以输出”的字幕，确认了计算依据文档化功能。

## 5. 工作流

### Step 1 — 在 Apps 中运行并选择 CASE

- 运行 GEN NX `Apps > Plug-in > Solar Structure Modeling`。
- 在“请选择太阳能结构 CASE”画面中，从 CASE 1~4 中选择与实际分析模块相同的形式（例：CASE 1 —
  单柱式太阳能结构）。

### Step 2 — 连接 API 并选择材料·截面

- 输入 Base URL、API Key、GEN NX 单位(mm) 后点击“连接测试”。
- 点击“从 GEN NX 读取”→ 材料/柱截面/屋面梁截面/支撑截面/檩条截面 下拉框中填入当前模型已定义的
  项目。若没有，先在 GEN NX 原生 Material Data/Section Data 窗口中定义（SS275 钢材，从
  H-Section/Cold Formed Channel 目录中选 B100×100×2.3、LC-100×50×20×2.3 等）后再次读取。

### Step 3 — 输入尺寸·边界条件（填写建模所需信息）

- 柱高（H）、屋面梁（倾角 θ、长度1(RL)·长度2(RR)）。
- 支撑1（方钢管，TRUSS）：构件高度(l1)、角度（以柱为基准）。
- 支撑2（右侧，TRUSS）：构件高度(l2)、角度（以柱为基准）。
- 檩条（PIN-PIN）：檩条数量（最少2）、Y方向布置（排数、排间距 S）。
- 横向支撑（TRUSS）：下端·上端高度。
- 边界条件：柱底节点（铰（平动约束，转动自由）等）。
- 每次输入时，右侧立面图·背面图实时刷新以确认形状。

### Step 4 — 输入荷载值

- 自动生成面荷载：输入固定荷载（Dead Load）、活荷载（Live Load）、雪荷载（Snow Load）kN/m²。
- 自动生成风荷载：输入基本风速（Vs，例 30m/s）、地面粗糙度类别（例 C — 一般地区）、勾选裸骨架
  结构荷载基准运算、柱截面宽度（d，例 200mm）→ 点击“计算书输出”时确认上述5步计算依据的全貌。

### Step 5 — 生成模型

- 点击“生成模型”→ 依据输入信息在 GEN NX 模型中自动生成节点·单元·边界条件·荷载。
- 结果：Nodes 30、Elements 43（Truss 10、Beam 33）、Material 1（SS275）、Section 2（B100×100×2.3、
  LC-100×50×20×2.3）、Supports 3（Type 1 [111111]，即6自由度完全固定）、Beam End Release 8
  （Type 1 [000111]，即弯矩3个方向释放 — 推测施加于桁架/铰接支撑），并生成 Static Load Case 1
  （DL，固定荷载）、Floor Loads 等。
- 在 3D 视图中确认太阳能面板框架形状（柱·V形支撑·倾斜屋面梁·檩条）被准确再现。

## 6. 关联的 JSON API 端点

画面中未显示确切的 API 请求日志，但与最终 GEN NX 模型树（Nodes/Elements(Truss/Beam)/Material/
Section/Supports/Beam End Release/Static Loads/Floor Loads）明确对应：

| 功能 | 推测 API | 文档位置 |
| --- | --- | --- |
| 材料·截面查询 | `GET /db/MATL`、`GET /db/SECT` | [`04_DB_Properties.md#1-dbmatl`](../../manual/zh-cn/04_DB_Properties.md#1-dbmatl)、[`#12-dbsect`](../../manual/zh-cn/04_DB_Properties.md#12-dbsect) |
| 节点·构件（柱/屋面梁/支撑/檩条）生成 | `POST /db/NODE`、`POST /db/ELEM` | [`03_DB_Node_Element.md#1-dbnode`](../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode)、[`#2-dbelem`](../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) |
| 边界条件（柱底铰节点） | `POST /db/CONS` | [`05_DB_Boundary.md#1-dbcons--constraint-support`](../../manual/zh-cn/05_DB_Boundary.md#1-dbcons--constraint-support) |
| 构件端部释放（支撑/檩条铰接） | `POST /db/FRLS` | [`05_DB_Boundary.md#12-dbfrls--beam-end-release`](../../manual/zh-cn/05_DB_Boundary.md#12-dbfrls--beam-end-release) |
| 静力荷载工况（DL/LL/雪荷载）生成 | `POST /db/STLD` | [`06_DB_Static_Loads.md#1-dbstld--static-load-cases`](../../manual/zh-cn/06_DB_Static_Loads.md#1-dbstld--static-load-cases) |

- ⚠️ 用于生成“面荷载”（Floor Load）的确切端点（是 `/db/STLD` 系列的 Floor Load Type 还是另有专门
  端点）未在画面中显示，属推测。
- KDS 41 12:00:2022 风荷载计算本身（净压力系数 C_N、设计压力 P_W/P_L、裸骨架结构荷载的计算）并非
  GEN NX Open API 提供的结果，而似乎是 Plug-in 自行实现的计算逻辑——与 #10（RCBeamDeflectionCheck）
  的挠度计算、#16（CraneLoader）的 KDS 41 10 15 计算同样，推测采用“用 API 只取得最低限度的形状
  数据，专业荷载计算自行完成后写入节点荷载/荷载工况”的模式。

## 7. 输入数据规格

- **CASE 选择**：CASE 1~4 之一。
- **尺寸**：柱高、屋面梁倾角·长度(RL/RR)、支撑1·2 构件高度·角度、檩条数量·Y方向排数·排间距、
  横向支撑上下高度。
- **材料·截面**：复用既有 GEN NX 定义或新建定义。
- **荷载**：固定·活·雪荷载(kN/m²)，风荷载（基本风速、地面粗糙度类别、柱截面宽度）。

## 8. 输出 / 生成结果

- GEN NX 模型的 Node/Element(Truss/Beam)/Material/Section/Supports/Beam End Release/Static Load
  Case(DL/LL/Floor Loads)/风荷载节点荷载全部内容。
- 风荷载计算依据计算书（可输出）。

## 9. 限制事项与局限

- 仅支持以4种 CASE 定型化的太阳能结构形式，非定型布置（例：曲面屋面、非对称支撑构成）似不在本
  Plug-in 的覆盖范围之内。
- 观察到 Beam End Release 一律以 "Type 1 [000111]" 施加，这究竟是对所有支撑·檩条相同适用的固定
  规则，还是按 CASE·构件种类分别不同施加，画面上未明确确认（⚠️ 未确认）。
- 风荷载计算看似仅支持 KDS 41 12:00:2022 一种标准，对其他国家标准·版本的支持情况未被提及。

## 10. 画面清单

| 时点（秒） | 画面内容 |
| --- | --- |
| 0–8 | 片头标题（VREW 字幕水印） |
| 8–24 | 在 GEN NX Apps 中运行 Plug-in、CASE 1~4 选择画面 |
| 24–48 | API 连接（Base URL/API Key）、材料·截面选择画面（GEN NX 中无可读取对象 → 新建定义） |
| 48–64 | 在 GEN NX 原生 Material Data/Section Data 窗口中定义 SS275、B100×100×2.3、LC-100×50×20×2.3 |
| 64–96 | 材料·截面读取完成，输入尺寸（柱高/倾角/RL/RR/支撑1·2/檩条/Y方向/横向支撑），立面图实时刷新 |
| 96–144 | 边界条件、荷载值（固定·活·雪荷载）输入，自动生成风荷载（基本风速/地面粗糙度类别），确认计算书明细 |
| 144–168 | 执行“生成模型”，确认 GEN NX 树（Nodes 30/Elements 43/Supports 3/Beam End Release 8） |
| 168–179 | 检查完成的 3D 太阳能结构模型，再次确认立面图·背面图 |

---

*至此，20个 Plug-in 案例（01_WALL_STACKER ~ 20_SolarStructureModeling）的规划文档撰写全部完成。*
