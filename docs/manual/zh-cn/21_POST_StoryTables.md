# 21. POST – Analysis Story Tables (楼层结果表格)

> **适用产品：** MIDAS Gen NX（主） · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **认证头部：** `MAPI-Key: <已签发的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/49511531295257)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../21_POST_StoryTables.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本节涉及建筑结构分析的**17种楼层级结果表格**。包括层间位移（Story Drift）·层间位移比·楼层位移（Story Displacement）·层剪力（反应谱）·剪力系数·振型形状·剪力比·偏心（Eccentricity）·倾覆力矩（Overturning Moment）·楼层轴力合计·稳定系数（Stability Coefficient）·扭转不规则（Torsional Irregularity）·扭转放大系数·刚度不规则（软弱层）·强度不规则（薄弱层）·平面规则性判定标准·设计层剪力审查·重量不规则审查等抗震设计所需的楼层结果。所有端点均使用**公共 URI `{base url}/post/TABLE`** ，并仅支持 `POST` 方法。请求体的 `"Argument"` 对象中以 `TABLE_TYPE` 值决定表格种类。

---

## 公共事项

### Input URI（楼层结果表格公共）

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 公共 Request 结构与参数

与解析结果表格（第19章）相同的扩展结构，支持 `UNIT`·`STYLES`·`COMPONENTS`·`NODE_ELEMS`·`LOAD_CASE_NAMES`·`OPT_CS`·`STAGE_STEP`。**下方参数表对17个表格全部公共适用**，各节仅另行记述 `TABLE_TYPE` enum、响应 `HEAD` 列与代表性示例。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 响应表格标题 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表格类型（按表格区分的 enum，参见各节） | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表格保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 力（Force） | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 长度（Length） | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 热（Heat） | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 温度（Temperature） | `UNIT.TEMP` | String | — | Optional |
| 5 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 数字格式 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 小数位数（0~15） | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 结果表格显示列 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 节点/单元指定（下列3种方式之一） | `"NODE_ELEMS"` | Object | All | Optional |
| 7-1 | 方式1：分别指定 ID（例：`[101, 102, 103]`） | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 7-2 | 方式2：指定 ID 范围（例：`"101 to 105"`） | `NODE_ELEMS.TO` | String | — | Optional |
| 7-3 | 方式3：指定结构组名（例：`"SG1"`） | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |
| 8 | 荷载名称与类型（下列后缀规则） | `"LOAD_CASE_NAMES"` | Array [String] | All | Optional |
| 9 | 激活施工阶段步骤（下列 ⚠️ — 取值不同行为不同） | `"OPT_CS"` | Boolean | `false`（标注写法上） | Optional |
| 10 | 施工阶段步骤名称 | `"STAGE_STEP"` | Array [String] | All | Optional |

> ⚠️ **`OPT_CS` 为3状态 —— 省略与 `false` 的行为彼此不同（2026-09-15 确认）。**
> `true` 会切换到 Construction Stage（第一个阶段）返回 CS 结果，`false` 会切换到 PostCS（最终阶段）
> 返回 Post 结果，而**省略该字段时则保持当前视图模式**，并返回与之对应的结果。
> 即「显式指定 `false`」与「完全不发送」并不相同。关于原文依据与 Default 列不一致一事，
> 详细情况请参考[19章公共参数表](./19_POST_AnalysisResult_1.md#通用-request-结构与参数)中
> 同一项的注释。**实际 API 行为未经验证。**

**`LOAD_CASE_NAMES` 后缀规则**

| 荷载类型 | 表示 |
|-----------|------|
| 静力荷载工况 | `NAME(ST)` |
| 一般组合 | `NAME(CB)` / `NAME(CB:all)` / `NAME(CB:max)` / `NAME(CB:min)` |
| 施工阶段 | `NAME(CS)` |
| 反应谱 | `NAME(RS)` |
| 移动荷载 | `NAME(MV:all)` / `NAME(MV:max)` / `NAME(MV:min)` |
| 沉降荷载 | `NAME(SM:all)` / `NAME(SM:max)` / `NAME(SM:min)` |

> **参考：** `OPT_CS`·`STAGE_STEP` 用于查询施工阶段结果。`STAGE_STEP` 项为 `"CS1:001(first)"`、`"CS1:002(last)"` 格式。

> **楼层结果表格荷载注意事项：** 楼层结果表格通常使用静力地震荷载 `(ST)`、反应谱 `(RS)`、荷载组合 `(CB)` 类型的 `LOAD_CASE_NAMES`。特别是**基于反应谱的表格（Story Shear Force (R.S.), Story Shear Force Coefficient (R.S.), Story Mode Shape）必须已定义并分析了 `(RS)` 荷载工况**，若无该荷载则返回为空的 `DATA`。

### 公共 Response 结构

```json
{
  "<TABLE_NAME>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

## 表格列表

| No. | 表格 | `TABLE_TYPE` |
|-----|--------|--------------|
| 1 | [Story Drift](#1-story-drift) | `STORY_DRIFT_X` / `STORY_DRIFT_Y` / `STORY_DRIFT_COMB` |
| 2 | [Story Displacement](#2-story-displacement) | `STORY_DISPLACEMENT_X` / `STORY_DISPLACEMENT_Y` / `STORY_DISPLACEMENT_COMB` |
| 3 | [Story Shear Force (R.S. Analysis)](#3-story-shear-force-rs-analysis) | `STORY_SHEAR_FOR_RS` |
| 4 | [Story Shear Force Coefficient (R.S. Analysis)](#4-story-shear-force-coefficient-rs-analysis) | `STORY_SHEAR_FORCE_COEFFICIENT` |
| 5 | [Story Mode Shape](#5-story-mode-shape) | `STORY_MODE_SHAPE` |
| 6 | [Story Shear Force Ratio](#6-story-shear-force-ratio) | `STORY_SHEAR_FORCE_RATIO` |
| 7 | [Story Eccentricity](#7-story-eccentricity) | `STORY_ECNTRICITY` |
| 8 | [Overturning Moment](#8-overturning-moment) | `OVERTURNING_MOMENT` |
| 9 | [Story Axial Force Sum](#9-story-axial-force-sum) | `STORY_AXIAL_FORCE_SUM` |
| 10 | [Story Stability Coefficient](#10-story-stability-coefficient) | `STORY_STABILITY_COEFFICIENT_X` / `STORY_STABILITY_COEFFICIENT_Y` |
| 11 | [Torsional Irregularity Check](#11-torsional-irregularity-check) | `TORSIONAL_IRREGULARITY_X` / `TORSIONAL_IRREGULARITY_Y` |
| 12 | [Torsional Amplification Factor](#12-torsional-amplification-factor) | `TORSIONAL_AMPLIFICATION_FACTOR_X` / `TORSIONAL_AMPLIFICATION_FACTOR_Y` |
| 13 | [Stiffness Irregularity Check (Soft Story)](#13-stiffness-irregularity-check-soft-story) | `STIFFNESS_IRREGULARITY_X` / `STIFFNESS_IRREGULARITY_Y` |
| 14 | [Capacity Irregularity Check (Weak Story)](#14-capacity-irregularity-check-weak-story) | `CAPACITY_IRREGULARITY` |
| 15 | [Criteria for Regularity in Plan](#15-criteria-for-regularity-in-plan) | `CRITERIA_FOR_REGULARITY_IN_PLAN` |
| 16 | [Ultimate Story Shear For Check](#16-ultimate-story-shear-for-check) | `ULTIMATE_STORY_SHEAR_FORCE_CHECK` |
| 17 | [Weight Irregularity Check](#17-weight-irregularity-check) | `WEIGHT_IRREGULARITY_X` / `WEIGHT_IRREGULARITY_Y` |

---

## 1. Story Drift

> **功能：** 提取各层的层间位移（Story Drift）与层间位移比（Story Drift Ratio）。针对 X/Y 各方向及组合（Combined），同时提供是否超过允许层间位移比（OK/NG）的信息，用于抗震设计的层间位移审查。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_DRIFT_X"` | X方向层间位移 |
| `"STORY_DRIFT_Y"` | Y方向层间位移 |
| `"STORY_DRIFT_COMB"` | 组合（Combined）层间位移（含全方向/所选节点的详细项） |

### Response HEAD

**`STORY_DRIFT_X`**

```json
["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Maximum Drift of All Vertical Elements/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Drift at the Center of Mass/Remark"]
```

**`STORY_DRIFT_Y`**

```json
["Index", "LoadCase", "Story", "StoryHeight", "P-DeltaIncrementalFactor", "AllowableStoryDriftRatio", "MaximumDriftofAllVerticalElements/Node", "MaximumDriftofAllVerticalElements/StoryDrift", "MaximumDriftofAllVerticalElements/ModifiedDrift", "MaximumDriftofAllVerticalElements/StoryDriftRatio", "MaximumDriftofAllVerticalElements/Remark", "DriftattheCenterofMass/StoryDrift", "DriftattheCenterofMass/ModifiedDrift", "DriftattheCenterofMass/DriftFactor", "DriftattheCenterofMass/StoryDriftRatio", "DriftattheCenterofMass/Remark"]
```

**`STORY_DRIFT_COMB`**

> ⚠️ 2026-08-26 确认（article id `49511531295257`）：以下 HEAD 在旧版本中缺失了 "Shear-Weighted
> Average Drift of Vertical Elements" 区块的全部内容（5列），且部分 `Remark`/`Node` 列被
> 错误地归入了其他区块（并非官方原文笔误，而是本仓库的撰写失误）。已以官方
> Response 示例（37列）为基准予以更正。

```json
["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Maximum Drift of All Vertical Elements/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Drift at the Center of Mass/Remark", "Average Drift of Vertical Elements/Story Drift", "Average Drift of Vertical Elements/Modified Drift", "Average Drift of Vertical Elements/Drift Factor", "Average Drift of Vertical Elements/Story Drift Ratio", "Average Drift of Vertical Elements/Remark", "Drift of a Vertical Line on Selected Node/Node", "Drift of a Vertical Line on Selected Node/Story Drift", "Drift of a Vertical Line on Selected Node/Modified Drift", "Drift of a Vertical Line on Selected Node/Drift Factor", "Drift of a Vertical Line on Selected Node/Story Drift Ratio", "Drift of a Vertical Line on Selected Node/Remark", "Average Drift of Vertical Lines on Selected Nodes/Story Drift", "Average Drift of Vertical Lines on Selected Nodes/Modified Drift", "Average Drift of Vertical Lines on Selected Nodes/Drift Factor", "Average Drift of Vertical Lines on Selected Nodes/Story Drift Ratio", "Average Drift of Vertical Lines on Selected Nodes/Remark", "Shear-Weighted Average Drift of Vertical Elements/Story Drift", "Shear-Weighted Average Drift of Vertical Elements/Modified Drift", "Shear-Weighted Average Drift of Vertical Elements/Drift Factor", "Shear-Weighted Average Drift of Vertical Elements/Story Drift Ratio", "Shear-Weighted Average Drift of Vertical Elements/Remark"]
```

### `ADDITIONAL` — 层间位移详细设置（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。详细控制层间位移允许比的判定方式（Method 1/2）与组合（Comb）表格的附加计算方式。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 层间位移比判定参数 | `ADDITIONAL.SET_STORY_DRIFT_PARAMS` | Object | — | Optional |
| 1-1-1 | 　　└ 判定方式：`true`=Method 1（响应修改系数），`false`=Method 2（位移放大系数） | `SET_STORY_DRIFT_PARAMS.RESPONSE_MOD_FACTOR_CHECK` | Boolean | `false` | Optional |
| 1-1-2 | 　　└（Method 1）响应修改系数取值 — 仅当 `RESPONSE_MOD_FACTOR_CHECK: true` 时 | `SET_STORY_DRIFT_PARAMS.RESPONSE_MOD_FACTOR_VALUE` | Number | `1` | Optional |
| 1-1-3 | 　　└（Method 2）位移放大系数(Cd) — 仅当 `RESPONSE_MOD_FACTOR_CHECK: false` 时 | `SET_STORY_DRIFT_PARAMS.DEFLECTION_AMPL_FACTOR_VALUE` | Number | `1` | Optional |
| 1-1-4 | 　　└（Method 2）重要度系数 | `SET_STORY_DRIFT_PARAMS.IMPORTANCE_FACTOR_VALUE` | Number | `1.5` | Optional |
| 1-1-5 | 　　└ 比例（Scale）系数 | `SET_STORY_DRIFT_PARAMS.SCALE_FACTOR_VALUE` | Number | `1` | Optional |
| 1-1-6 | 　　└ 允许层间位移比 | `SET_STORY_DRIFT_PARAMS.ALLOWABLE_RATIO` | Number | `0.015` | Optional |
| 1-1-7 | 　　└ P-Delta 审查用竖向荷载组合列表 | `SET_STORY_DRIFT_PARAMS.LCOMS` | Array [Object] | — | Optional |
| 1-1-7-1 | 　　　　└ 荷载工况名 / 系数 | `LCOMS[].NAME` / `LCOMS[].FACTOR` | String / Number | — | Optional |
| 1-1-8 | 　　└ Beta 值设置 | `SET_STORY_DRIFT_PARAMS.BETA` | Object | — | Optional |
| 1-1-8-1 | 　　　　└ 方式：`"FIXED"`（固定 1.0）/ `"USER"`（按层直接输入） | `BETA.FIX_USER_CHECK` | String | `"FIXED"` | Optional |
| 1-1-8-2 | 　　　　└ 应用起始/终止楼层 — 仅当 `FIX_USER_CHECK: "USER"` 时 | `BETA.NAME_FROM` / `BETA.NAME_TO` | String | — | Optional |
| 1-1-8-3 | 　　　　└ 用户指定 Beta 值 — 仅当 `FIX_USER_CHECK: "USER"` 时 | `BETA.VALUE` | Number | `0` | Optional |
| 1-2 | └（`STORY_DRIFT_COMB` 专用）附加计算方式选择 | `ADDITIONAL.SET_STORY_DRIFT_CALCULATION_METHOD` | Object | `DRIFT_AT_THE_CENTER_OF_MASS` | Optional |
| 1-2-1 | 　　└ 质心位移 | `SET_STORY_DRIFT_CALCULATION_METHOD.DRIFT_AT_THE_CENTER_OF_MASS` | Boolean | `true` | Optional |
| 1-2-2 | 　　└ 竖向构件平均位移 | `SET_STORY_DRIFT_CALCULATION_METHOD.AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS` | Boolean | `false` | Optional |
| 1-2-3 | 　　└ 以所选节点为基准的竖线位移（X_DIR/Y_DIR/COMBINED **Required**） | `SET_STORY_DRIFT_CALCULATION_METHOD.DRIFT_OF_A_VERTICAL_LINE_ON_SELECTED_NODE` | Object | — | Optional |
| 1-2-4 | 　　└ 以所选节点（复数）为基准的竖线平均位移（X_DIR/Y_DIR/COMBINED 数组，**Required**） | `SET_STORY_DRIFT_CALCULATION_METHOD.AVERAGE_DRIFT_OF_VERTICAL_LINES_ON_SELECTED_NODES` | Object | — | Optional |
| 1-2-5 | 　　└ 剪力加权平均位移 | `SET_STORY_DRIFT_CALCULATION_METHOD.SHEAR_WEIGHTED_AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS` | Boolean | `false` | Optional |

> ℹ️ **2026-07-29 官方更正已反映：** 此前方向 Key 在 Specifications 表（`X_DIR`）与请求示例（`X-DIR`）之间不一致，并且 `AVERAGE_DRIFT_OF_VERTICAL_LINES_ON_SELECTED_NODES` 的 Value 类型也误记为 `Array [Object]`。官方文档已将两项均予更正（统一为 `X_DIR`，类型改为 `Object`），下方示例也随之更新。

**请求示例 — 含 `ADDITIONAL`（Comb）**

```json
{
  "Argument": {
    "TABLE_TYPE": "STORY_DRIFT_COMB",
    "LOAD_CASE_NAMES": ["RX(RS)", "RY(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SET_STORY_DRIFT_PARAMS": {
        "RESPONSE_MOD_FACTOR_CHECK": true,
        "RESPONSE_MOD_FACTOR_VALUE": 3,
        "SCALE_FACTOR_VALUE": 4.0,
        "ALLOWABLE_RATIO": 0.03
      },
      "SET_STORY_DRIFT_CALCULATION_METHOD": {
        "DRIFT_AT_THE_CENTER_OF_MASS": true,
        "AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS": true,
        "DRIFT_OF_A_VERTICAL_LINE_ON_SELECTED_NODE": { "X_DIR": 109 },
        "AVERAGE_DRIFT_OF_VERTICAL_LINES_ON_SELECTED_NODES": { "X_DIR": [262, 260] },
        "SHEAR_WEIGHTED_AVERAGE_DRIFT_OF_VERTICAL_ELEMENTS": true
      }
    }
  }
}
```

### Request / Response JSON

**POST 请求体 — X方向层间位移**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Drift(X)",
    "TABLE_TYPE": "STORY_DRIFT_X",
    "UNIT": { "FORCE": "kN", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST 响应体 — X方向层间位移**

```json
{
  "Story Drift(X)": {
    "FORCE": "kN",
    "DIST": "mm",
    "HEAD": ["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Maximum Drift of All Vertical Elements/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Drift at the Center of Mass/Remark"],
    "DATA": [
      ["1", "RX(RS)", "3F", "4000.000000", "1.000000", "0.020000", "21", "1.998633", "4.996583", "0.001249", "OK", "1.998633", "4.996583", "1.000000", "0.001249", "OK"]
    ]
  }
}
```

**POST 请求体 — 组合（Combined）层间位移**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Drift(Comb)",
    "TABLE_TYPE": "STORY_DRIFT_COMB",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["gLCB1(CB)"]
  }
}
```

**POST 响应体 — 组合（Combined）层间位移**

> ⚠️ 2026-08-26 确认（article id `49511531295257`）：旧示例的 HEAD 列顺序与列数与实际不符，
> 无法与 DATA 值对应（37列）。已替换为官方 Response 示例的实际取值。

```json
{
  "Story Drift(Comb)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Story Height", "P-Delta Incremental Factor", "Allowable Story Drift Ratio", "Maximum Drift of All Vertical Elements/Node", "Maximum Drift of All Vertical Elements/Story Drift", "Maximum Drift of All Vertical Elements/Modified Drift", "Maximum Drift of All Vertical Elements/Story Drift Ratio", "Maximum Drift of All Vertical Elements/Remark", "Drift at the Center of Mass/Story Drift", "Drift at the Center of Mass/Modified Drift", "Drift at the Center of Mass/Drift Factor", "Drift at the Center of Mass/Story Drift Ratio", "Drift at the Center of Mass/Remark", "Average Drift of Vertical Elements/Story Drift", "Average Drift of Vertical Elements/Modified Drift", "Average Drift of Vertical Elements/Drift Factor", "Average Drift of Vertical Elements/Story Drift Ratio", "Average Drift of Vertical Elements/Remark", "Drift of a Vertical Line on Selected Node/Node", "Drift of a Vertical Line on Selected Node/Story Drift", "Drift of a Vertical Line on Selected Node/Modified Drift", "Drift of a Vertical Line on Selected Node/Drift Factor", "Drift of a Vertical Line on Selected Node/Story Drift Ratio", "Drift of a Vertical Line on Selected Node/Remark", "Average Drift of Vertical Lines on Selected Nodes/Story Drift", "Average Drift of Vertical Lines on Selected Nodes/Modified Drift", "Average Drift of Vertical Lines on Selected Nodes/Drift Factor", "Average Drift of Vertical Lines on Selected Nodes/Story Drift Ratio", "Average Drift of Vertical Lines on Selected Nodes/Remark", "Shear-Weighted Average Drift of Vertical Elements/Story Drift", "Shear-Weighted Average Drift of Vertical Elements/Modified Drift", "Shear-Weighted Average Drift of Vertical Elements/Drift Factor", "Shear-Weighted Average Drift of Vertical Elements/Story Drift Ratio", "Shear-Weighted Average Drift of Vertical Elements/Remark"],
    "DATA": [
      ["1", "RX(RS)", "10F", "4.0000", "1.0000", "0.0300", "404", "0.0012", "0.0142", "0.0035", "OK", "0.0011", "0.0129", "1.0996", "0.0032", "OK", "0.0011", "0.0130", "1.0916", "0.0032", "OK", "397", "0.0011", "0.0131", "1.0787", "0.0033", "OK", "0.0011", "0.0136", "1.0428", "0.0034", "OK", "0.0049", "0.0587", "0.2411", "0.0147", "OK"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# 查询层间位移（X方向）表格 — 确认是否超过允许位移比（OK/NG）
payload = {
    "Argument": {
        "TABLE_NAME": "Story Drift(X)",
        "TABLE_TYPE": "STORY_DRIFT_X",
        "UNIT": {"FORCE": "kN", "DIST": "mm"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["RX(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Story Drift(X)", {})
head = table.get("HEAD", [])

# 输出各层的最大层间位移比与判定（Remark）
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    story = d["Story"]
    ratio = d["Maximum Drift of All Vertical Elements/Story Drift Ratio"]
    remark = d["Maximum Drift of All Vertical Elements/Remark"]
    print(f"{story}: 层间位移比={ratio}, 判定={remark}")
```

---

## 2. Story Displacement

> **功能：** 提取各层节点的最大位移、平均位移及其比值（Maximum/Average）。用于确认扭转行为与楼层位移分布。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_DISPLACEMENT_X"` | X方向楼层位移 |
| `"STORY_DISPLACEMENT_Y"` | Y方向楼层位移 |
| `"STORY_DISPLACEMENT_COMB"` | 组合（Combined）楼层位移 |

### Response HEAD

```json
["Index", "LoadCase", "Node", "Story", "Level", "StoryHeight", "MaximumDisplacement", "AverageDisplacement", "Maximum/Average"]
```

### Request / Response JSON

**POST 请求体 — X方向楼层位移**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_DISPLACEMENT_X",
    "TABLE_TYPE": "STORY_DISPLACEMENT_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST 响应体 — X方向楼层位移**

```json
{
  "STORY_DISPLACEMENT_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "LoadCase", "Node", "Story", "Level", "StoryHeight", "MaximumDisplacement", "AverageDisplacement", "Maximum/Average"],
    "DATA": [
      ["1", "RX(RS)", "5004", "2F", "11.5000", "0.0000", "0.0070", "0.0070", "1.0000"],
      ["2", "RX(RS)", "47", "1F", "5.5000", "6.0000", "0.0031", "0.0030", "1.0283"]
    ]
  }
}
```

**POST 请求体 — 组合（Combined）楼层位移**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_DISPLACEMENT_COMB",
    "TABLE_TYPE": "STORY_DISPLACEMENT_COMB",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["gLCB1(CB)"]
  }
}
```

**POST 响应体 — 组合（Combined）楼层位移**

> ⚠️ 2026-08-26 确认（article id `49511597474713`）：旧版本缺失 Response 示例，
> 故按官方示例原样补充。

```json
{
  "STORY_DISPLACEMENT_COMB": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "LoadCase", "Node", "Story", "Level", "StoryHeight", "MaximumDisplacement", "AverageDisplacement", "Maximum/Average"],
    "DATA": [
      ["1", "gLCB1", "5004", "2F", "11.5000", "0.0000", "0.0076", "0.0073", "1.0442"],
      ["2", "gLCB1", "48", "1F", "5.5000", "6.0000", "0.0034", "0.0031", "1.1066"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 楼层位移（Y方向）— 以最大/平均位移比确认扭转行为
payload = {
    "Argument": {
        "TABLE_NAME": "STORY_DISPLACEMENT_Y",
        "TABLE_TYPE": "STORY_DISPLACEMENT_Y",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RY(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_DISPLACEMENT_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']} (Node {d['Node']}): Max/Avg={d['Maximum/Average']}")
```

---

## 3. Story Shear Force (R.S. Analysis)

> **功能：** 从反应谱（R.S.）解析结果中提取各层的惯性力（Inertia Force）、计入/不计入弹簧反力的剪力、偏心（Eccentricity）、层力（Story Force）与偏心弯矩。**需要 `(RS)` 荷载工况。**

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_SHEAR_FOR_RS"` | 反应谱解析层剪力 |

### Response HEAD

```json
["Index", "Story", "Level", "Spectrum", "Inertia Force/X", "Inertia Force/Y", "Shear Force/Spring Reactions/X", "Shear Force/Spring Reactions/Y", "Shear Force/Without Spring/X", "Shear Force/Without Spring/Y", "Shear Force/With Spring/X", "Shear Force/With Spring/Y", "Eccentricity", "Story Force", "Eccentric Moment"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_SHEAR_FOR_RS",
    "TABLE_TYPE": "STORY_SHEAR_FOR_RS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_SHEAR_FOR_RS": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Spectrum", "Inertia Force/X", "Inertia Force/Y", "Shear Force/Spring Reactions/X", "Shear Force/Spring Reactions/Y", "Shear Force/Without Spring/X", "Shear Force/Without Spring/Y", "Shear Force/With Spring/X", "Shear Force/With Spring/Y", "Eccentricity", "Story Force", "Eccentric Moment"],
    "DATA": [
      ["1", "2F", "11.500000000000", "RX(RS)", "5.942538531202", "-1.613724870840", "0.000000000000", "0.000000000000", "94.786719429559", "19.670201963351", "94.786719429559", "19.670201963351", "0.000000000000", "5.942538531202", "0.000000000000"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 反应谱层剪力 — 必须具有 (RS) 荷载
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_SHEAR_FOR_RS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_SHEAR_FOR_RS", {})
head = table.get("HEAD", [])
if not table.get("DATA"):
    print("无结果 — 请确认 (RS) 荷载工况是否已定义/已分析。")
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Vx(With Spring)={d['Shear Force/With Spring/X']}")
```

---

## 4. Story Shear Force Coefficient (R.S. Analysis)

> **功能：** 由反应谱解析的各层剪力与累计重量合计（Weight Sum），按 X/Y 方向计算层剪力系数（Story Shear Force Coefficient）。**需要 `(RS)` 荷载工况。**

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_SHEAR_FORCE_COEFFICIENT"` | 反应谱解析层剪力系数 |

### Response HEAD

```json
["Index", "Story", "Spectrum", "Shear Force/X", "Shear Force/Y", "Weight Sum/X", "Weight Sum/Y", "Story Shear Force Coefficient/X", "Story Shear Force Coefficient/Y"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_SHEAR_FORCE_COEFFICIENT",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_COEFFICIENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_SHEAR_FORCE_COEFFICIENT": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Spectrum", "Shear Force/X", "Shear Force/Y", "Weight Sum/X", "Weight Sum/Y", "Story Shear Force Coefficient/X", "Story Shear Force Coefficient/Y"],
    "DATA": [
      ["1", "1F", "RX(RS)", "732.983113710330", "140.189527295489", "8235.050199781430", "8235.050199781430", "0.089007728663", "0.017023518241"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 查询层剪力系数（V/W）
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_SHEAR_FORCE_COEFFICIENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_SHEAR_FORCE_COEFFICIENT", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Cs,x={d['Story Shear Force Coefficient/X']}, Cs,y={d['Story Shear Force Coefficient/Y']}")
```

---

## 5. Story Mode Shape

> **功能：** 提取各层代表节点在各阶振型下的位移形状（UX, UY, UZ, RX, RY, RZ）。用于逐层振型形状确认与动力行为评估。**需要振型分析（R.S.）结果。**

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_MODE_SHAPE"` | 楼层振型形状 |

### Response HEAD

```json
["Index", "Story", "Level", "X", "Y", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]
```

### 专用参数 — 振型筛选（2026-07-24 官方已收录）

> ℹ️ 官方手册中记录了可选择性筛选待查询振型的 `"MODES"` 请求数组，故在此反映。未指定时返回全部振型。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 待查询的振型编号列表（`"Mode" + 编号`，例：`"Mode1"`） | `"MODES"` | Array [String] | All | Optional |

**请求示例 — 含 `MODES`**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_MODE_SHAPE",
    "TABLE_TYPE": "STORY_MODE_SHAPE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "MODES": ["Mode1", "Mode2"]
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_MODE_SHAPE",
    "TABLE_TYPE": "STORY_MODE_SHAPE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 }
  }
}
```

**POST Response Body**

```json
{
  "STORY_MODE_SHAPE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "X", "Y", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "2F", "11.500000000000", "13.793310881566", "0.000000000000", "1", "-0.000000001120", "0.000000005610", "0.000000000000", "0.000000000000", "0.000000000000", "-0.000000000135"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 楼层振型形状 — 确认1阶振型的逐层 UX/UY
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_MODE_SHAPE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 6}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_MODE_SHAPE", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    if d["Mode"] == "1":
        print(f"Mode1 {d['Story']}: UX={d['UX']}, UY={d['UY']}")
```

---

## 6. Story Shear Force Ratio

> **功能：** 针对各层，按构件类型（Frame/Wall 等）提取其剪力以及占全部层剪力的分担率（Ratio），以两个方向（Angle1/Angle2）给出。用于按构件审查剪力分担情况。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_SHEAR_FORCE_RATIO"` | 层剪力分担比 |

### Response HEAD

本表格使用两种 HEAD 数组。首行包含 `Index`，同一组内后续的各行可能省略 `Index` 列返回。

**HEAD（包含 Index）**

```json
["Index", "Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"]
```

**HEAD（省略 Index）**

```json
["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"]
```

响应正文除上述 `DATA` 之外，还包含按构件类型汇总层剪力合计的 `"SUB_TABLES"` 数组。详细情况请参考下方 `SUB_TABLES` 项。

### `ADDITIONAL` — 角度与目标楼层设置（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了指定目标楼层的 `"STORY_NAMES"` 请求数组与 `"ADDITIONAL"` 请求对象，故在此反映。`ADDITIONAL.SET_ANGLE.ANGLE` 作为 Angle1/Angle2 的计算基准角，在本表格中为**必填输入（Required）**。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 目标楼层名称列表 | `"STORY_NAMES"` | Array [String] | All | Optional |
| 2 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 2-1 | └ 角度设置 | `ADDITIONAL.SET_ANGLE` | Object | — | **Required** |
| 2-1-1 | 　　└ Angle1 输入值（Angle2 = Angle1 + 90°） | `SET_ANGLE.ANGLE` | Number | — | **Required** |

**请求示例 — 含 `STORY_NAMES` / `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "LOAD_CASE_NAMES": ["EX(ST)"],
    "STORY_NAMES": ["2F"],
    "ADDITIONAL": {
      "SET_ANGLE": { "ANGLE": 33.5 }
    }
  }
}
```

### `SUB_TABLES` — 层剪力合计子表格（2026-07-24 官方已收录）

> ℹ️ 官方手册中另在响应正文最上层记录了按构件类型汇总层剪力合计的 `"SUB_TABLES"` 数组，故在此反映。数组的各元素是以子表格名称为 Key 的对象，每个子表格具有自身的 `HEAD`/`DATA` 结构。

| No. | 说明 | Key | 值类型 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 子表格列表 | `"SUB_TABLES"` | Array [Object] | 仅响应（Read Only） |
| 1-1 | └ 线性叠加层剪力 | `"LINEAR SUMMATION OF STORY SHEAR FORCE"` | Object | `HEAD`/`DATA` 结构 |
| 1-2 | └ 数值叠加层剪力 | `"NUMERICAL SUMMATION OF STORY SHEAR FORCE"` | Object | `HEAD`/`DATA` 结构 |

**`SUB_TABLES` 子表格 HEAD**（Type = `"Sum"` 的行为构件类型合计，`Ratio1`/`Ratio2` 以空字符串返回）

```json
["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_SHEAR_FORCE_RATIO",
    "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["EX(ST)"]
  }
}
```

**POST Response Body**

> ⚠️ 2026-08-26 确认（article id `49512411760665`）：旧版本的第2个 DATA 行，实际上是把
> 下方 `SUB_TABLES` 中 Frame(Beam) 的合计值误当作单独的行（`No`）抄录进来的结果
> （并非原文笔误）。已替换为官方示例中真正的第2行（No `135`）。

```json
{
  "STORY_SHEAR_FORCE_RATIO": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"],
    "DATA": [
      ["1", "2F", "5.000000000000", "EX", "Frame(Beam)", "129", "33.500000000000", "28.665741744457", "0.007935020134", "123.500000000000", "-22.438153697157", "0.009384022933"],
      ["2", "2F", "5.000000000000", "EX", "Frame(Beam)", "135", "33.500000000000", "17.983888493963", "0.004978155408", "123.500000000000", "-14.838673083899", "0.006205789050"]
    ],
    "SUB_TABLES": [
      {
        "LINEAR SUMMATION OF STORY SHEAR FORCE": {
          "HEAD": ["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"],
          "DATA": [
            ["2F", "", "EX", "Frame(Beam)", "", "33.500000000000", "797.380554817400", "0.220724473589", "123.500000000000", "-544.234513929400", "0.227608261730"],
            ["2F", "", "EX", "Wall", "", "33.500000000000", "2815.180127076000", "0.779275526411", "123.500000000000", "-1846.867240428000", "0.772391738270"],
            ["2F", "", "EX", "Sum", "", "33.500000000000", "3612.560681894000", "", "123.500000000000", "-2391.101754358000", ""]
          ]
        }
      },
      {
        "NUMERICAL SUMMATION OF STORY SHEAR FORCE": {
          "HEAD": ["Story", "Level", "Load", "Type", "No", "Angle1", "Force1", "Ratio1", "Angle2", "Force2", "Ratio2"],
          "DATA": [
            ["2F", "", "EX", "Frame(Beam)", "", "33.500000000000", "797.380554817400", "0.220724473589", "123.500000000000", "-544.234513929400", "0.227608261730"],
            ["2F", "", "EX", "Wall", "", "33.500000000000", "2815.180127076000", "0.779275526411", "123.500000000000", "-1846.867240428000", "0.772391738270"],
            ["2F", "", "EX", "Sum", "", "33.500000000000", "3612.560681894000", "", "123.500000000000", "-2391.101754358000", ""]
          ]
        }
      }
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 层剪力分担比 — 确认各构件类型的分担率
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_SHEAR_FORCE_RATIO",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["EX(ST)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_SHEAR_FORCE_RATIO", {})
head = table.get("HEAD", [])  # 以响应的 HEAD 为基准进行映射
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d.get('Story')} {d.get('Type')}: Ratio1={d.get('Ratio1')}, Ratio2={d.get('Ratio2')}")
```

---

## 7. Story Eccentricity

> **功能：** 提取各层的质心（Weight Center）·刚心（Stiffness Center）坐标、偏心距（Ecc. Dist.）、扭转刚度、弹性半径（El. Radius）、偏心比（Ecc. Ratio）。用于审查偏心引起的扭转。

> **拼写注意：** 本表格的 `TABLE_TYPE` 取值按 API 规格为 `"STORY_ECNTRICITY"`，**字母系有意缺失（Ec**c**ent → Ecnt）**。即使看起来像笔误，也必须按 API 所要求的字符串原样使用 `"STORY_ECNTRICITY"`。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_ECNTRICITY"` | 楼层偏心（按原拼写使用，API 规格） |

### Response HEAD

```json
["Index", "Story", "Level", "Weight Center/X", "Weight Center/Y", "Stiffness Center/X", "Stiffness Center/Y", "Ecc. Dist./X", "Ecc. Dist./Y", "Torsional Stiffness", "El. Radius/X", "El. Radius/Y", "Ecc. Ratio/X", "Ecc. Ratio/Y"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_ECNTRICITY",
    "TABLE_TYPE": "STORY_ECNTRICITY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 }
  }
}
```

**POST Response Body**

```json
{
  "STORY_ECNTRICITY": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Weight Center/X", "Weight Center/Y", "Stiffness Center/X", "Stiffness Center/Y", "Ecc. Dist./X", "Ecc. Dist./Y", "Torsional Stiffness", "El. Radius/X", "El. Radius/Y", "Ecc. Ratio/X", "Ecc. Ratio/Y"],
    "DATA": [
      ["1", "Roof", "8.500000000000", "-3.615980663971", "-2.556113113542", "-5.744037990008", "0.437974763722", "2.128057326037", "2.994087877264", "10819091.305889900774", "2.299549236852", "2.770672579299", "1.302032515452", "0.768065249549"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 楼层偏心 — 注意拼写："STORY_ECNTRICITY"（按 API 规格原样）
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_ECNTRICITY",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_ECNTRICITY", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 偏心比 X={d['Ecc. Ratio/X']}, Y={d['Ecc. Ratio/Y']}")
```

---

## 8. Overturning Moment

> **功能：** 提取各层的倾覆力矩（Overturning Moment），按构件类型（Frame/Wall）给出分担值与分担比，涵盖两个方向（Angle1/Angle2）。用于倾覆稳定性以及墙体/框架分担审查。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"OVERTURNING_MOMENT"` | 倾覆力矩 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Reduction Factor", "Angle1", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force1 * Distance", "Overturning Moment1", "Angle2", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force2 * Distance", "Overturning Moment2"]
```

### `ADDITIONAL` — 倾覆力矩计算条件（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。详细控制倾覆力矩计算的基准角（Angle1/Angle2）、反应谱比例系数以及折减系数（Reduction Factor）的计算方式。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 角度设置 | `ADDITIONAL.SET_ANGLE` | Object | — | Optional |
| 1-1-1 | 　　└ Angle1 输入值（Angle2 = Angle1 + 90°） | `SET_ANGLE.ANGLE` | Number | `0` | Optional |
| 1-2 | └ 倾覆力矩计算参数 | `ADDITIONAL.SET_OVERTURNING_MOMENT_PARAMS` | Object | — | Optional |
| 1-2-1 | 　　└ 反应谱比例（Scale）系数 | `SET_OVERTURNING_MOMENT_PARAMS.SF_FOR_RS` | Number | `1` | Optional |
| 1-2-2 | 　　└ 折减系数（Reduction Factor）计算方式：`"FIXED"`（固定 1.0）/ `"AUTO"`（自动计算） | `SET_OVERTURNING_MOMENT_PARAMS.DEFINE_RF` | String | `"FIXED"` | Optional |

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "OVERTURNING_MOMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "LOAD_CASE_NAMES": ["Rx(RS)", "Ry(RS)"],
    "ADDITIONAL": {
      "SET_ANGLE": { "ANGLE": 33.5 },
      "SET_OVERTURNING_MOMENT_PARAMS": {
        "SF_FOR_RS": 0,
        "DEFINE_RF": "AUTO"
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "OVERTURNING_MOMENT",
    "TABLE_TYPE": "OVERTURNING_MOMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "OVERTURNING_MOMENT": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Reduction Factor", "Angle1", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force1 * Distance", "Overturning Moment1", "Angle2", "Overturning Moment by Vertical Member Types/Frame/Value", "Overturning Moment by Vertical Member Types/Frame/Ratio", "Overturning Moment by Vertical Member Types/Wall/Value", "Overturning Moment by Vertical Member Types/Wall/Ratio", "Sum of Story Force2 * Distance", "Overturning Moment2"],
    "DATA": [
      ["1", "RX(RS)", "12F", "46.000000000000", "4.000000000000", "1.000000000000", "0.000000000000", "2295.801974529160", "0.585868242113", "1622.829911454460", "0.414131757887", "3918.631885983620", "3918.631885983620", "90.000000000000", "569.013713175881", "0.581454548541", "409.590228617339", "0.418545451459", "978.603941793220", "978.603941793220"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 倾覆力矩 — 确认方向1的倾覆力矩与墙体分担比
payload = {
    "Argument": {
        "TABLE_TYPE": "OVERTURNING_MOMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("OVERTURNING_MOMENT", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: OTM1={d['Overturning Moment1']}, "
          f"Wall分担比={d['Overturning Moment by Vertical Member Types/Wall/Ratio']}")
```

---

## 9. Story Axial Force Sum

> **功能：** 提取各层竖向构件（柱·墙）的轴力合计（Axial Force Sum）与轴力中心（Center of Axial Forces）坐标。用于确认楼层竖向荷载分布与轴力中心。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_AXIAL_FORCE_SUM"` | 楼层轴力合计 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Axial Force Sum of Vertical Elements", "Center of Axial Forces/X Coordinate", "Center of Axial Forces/Y Coordinate"]
```

### Request / Response JSON

> ⚠️ 2026-08-26 确认（article id `49512116327065`）：以下示例的 `DATA` 取值直接取自官方示例
> （单位 `FORCE: "LBF"`），而旧版本将 `UNIT.FORCE` 误标为 `"kN"`（同一组数值不可能
> 在两种单位系下同时成立 — 并非原文笔误，而是本仓库的
> 撰写失误）。已更正为 `lbf`。

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_AXIAL_FORCE_SUM",
    "TABLE_TYPE": "STORY_AXIAL_FORCE_SUM",
    "UNIT": { "FORCE": "lbf", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "STORY_AXIAL_FORCE_SUM": {
    "FORCE": "lbf",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Axial Force Sum of Vertical Elements", "Center of Axial Forces/X Coordinate", "Center of Axial Forces/Y Coordinate"],
    "DATA": [
      ["1", "DL", "12F", "46.000000000000", "4.000000000000", "-2243898.534310730174", "18.015185337274", "14.191484061342"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 楼层轴力合计 — 以固定荷载(DL)为基准
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_AXIAL_FORCE_SUM",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_AXIAL_FORCE_SUM", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: ΣN={d['Axial Force Sum of Vertical Elements']}")
```

---

## 10. Story Stability Coefficient

> **功能：** 由竖向荷载、层剪力与修正层间位移计算各层的稳定系数（Stability Coefficient, θ），同时给出是否超过允许限值（Allowable Limit）（OK/NG）与 P-Delta 放大系数。针对 X/Y 各方向审查 P-Δ 效应。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STORY_STABILITY_COEFFICIENT_X"` | X方向稳定系数 |
| `"STORY_STABILITY_COEFFICIENT_Y"` | Y方向稳定系数 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Story Height", "Vertical Load", "Story Shear Force", "Modified Story Drift", "Beta", "Stability Coefficient", "Allowable Limit", "Remark", "P-Delta Incremental Factor"]
```

### `ADDITIONAL` — 稳定系数计算参数（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。详细控制稳定系数（θ）计算所用的位移放大系数、重要度系数等参数与 Beta 值、层间位移计算方式。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 稳定系数计算参数 | `ADDITIONAL.SET_STABILITY_COEFFICIENT_PARAMS` | Object | — | Optional |
| 1-1-1 | 　　└ 位移放大系数(Cd) | `SET_STABILITY_COEFFICIENT_PARAMS.DEFLECTION_AMPL_FACTOR_VALUE` | Number | System | Optional |
| 1-1-2 | 　　└ 重要度系数 | `SET_STABILITY_COEFFICIENT_PARAMS.IMPORTANCE_FACTOR_VALUE` | Integer | System | Optional |
| 1-1-3 | 　　└ 比例（Scale）系数 | `SET_STABILITY_COEFFICIENT_PARAMS.SCALE_FACTOR_VALUE` | Integer | System | Optional |
| 1-1-4 | 　　└ P-Delta 审查用竖向荷载组合列表 | `SET_STABILITY_COEFFICIENT_PARAMS.LCOMS` | Array [Object] | System | Optional |
| 1-1-4-1 | 　　　　└ 荷载工况名 / 系数 | `LCOMS[].NAME` / `LCOMS[].FACTOR` | String / Number | — | Optional |
| 1-1-5 | 　　└ Beta 值设置 | `SET_STABILITY_COEFFICIENT_PARAMS.BETA` | Object | — | Optional |
| 1-1-5-1 | 　　　　└ 方式：`"FIXED"`（固定 1.0）/ `"USER"`（按层直接输入） | `BETA.FIX_USER_CHECK` | String | System | Optional |
| 1-1-5-2 | 　　　　└ 应用起始/终止楼层 — 仅当 `FIX_USER_CHECK: "USER"` 时 | `BETA.NAME_FROM` / `BETA.NAME_TO` | String | — | Optional |
| 1-1-5-3 | 　　　　└ 用户指定 Beta 值 — 仅当 `FIX_USER_CHECK: "USER"` 时 | `BETA.VALUE` | Number | — | Optional |
| 1-2 | └ 层间位移计算方式选择 | `ADDITIONAL.SET_CALCULATION_METHOD` | Object | — | Optional |
| 1-2-1 | 　　└ 方式：`"Drift at the Center of Mass"`（质心位移）/ `"Max. Drift of Outer Extreme Points"`（外缘最大位移）/ `"Max. Drift of All Vertical Elements"`（全部竖向构件最大位移） | `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` | String | — | Optional |

> ℹ️ **2026-08-20 官方反映 — `STORY_DRIFT_METHOD` 的取值最终统一为 `"Drift at the Center of Mass"`。** 该取值的写法曾两度反复，故留下依据。（1）2026-07-30 时点，官方负责人确认「本表格所属的产品界面实际使用的是 'Drift on'」，于是仅更正拼写为 `"Drift on the Center of Mass"`（Jira MAPI-2009）。（2）此后另有独立 Issue 指出，API 实际上混存 `SET_STORY_DRIFT_METHOD`（被忽略）与 `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` 两种结构，甚至难以确认取值是否被应用（Jira MAPI-2375），负责开发的工程师经审议后决定「统一为 at」（2026-08-10）— 即把产品 UI 与 API enum 一并对齐到 `"Drift at the Center of Mass"`。官方文章也已于 2026-08-20 以该取值更新，与 [13. Stiffness Irregularity Check](#13-stiffness-irregularity-check-soft-story)·[17. Weight Irregularity Check](#17-weight-irregularity-check) 相同。也就是说，旧的 "on" 写法以当时为基准是准确的，但此后产品本身改成了 "at"，并非把笔误改回去。

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_X",
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "ADDITIONAL": {
      "SET_STABILITY_COEFFICIENT_PARAMS": {
        "DEFLECTION_AMPL_FACTOR_VALUE": 2,
        "IMPORTANCE_FACTOR_VALUE": 5,
        "SCALE_FACTOR_VALUE": 2,
        "LCOMS": [
          { "NAME": "DL", "FACTOR": 1 }
        ],
        "BETA": {
          "FIX_USER_CHECK": "USER",
          "NAME_FROM": "1F",
          "NAME_TO": "12F",
          "VALUE": 2
        }
      },
      "SET_CALCULATION_METHOD": {
        "STORY_DRIFT_METHOD": "Max. Drift of All Vertical Elements"
      }
    }
  }
}
```

### Request / Response JSON

**POST 请求体 — X方向**

```json
{
  "Argument": {
    "TABLE_NAME": "STORY_STABILITY_COEFFICIENT_X",
    "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST 响应体 — X方向**

```json
{
  "STORY_STABILITY_COEFFICIENT_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Story Height", "Vertical Load", "Story Shear Force", "Modified Story Drift", "Beta", "Stability Coefficient", "Allowable Limit", "Remark", "P-Delta Incremental Factor"],
    "DATA": [
      ["1", "RX(RS)", "12F", "4.000000000000", "9981.361069987301", "979.657971495906", "0.001432662061", "1.000000000000", "0.000912302925", "0.250000000000", "OK", "1.000000000000"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 稳定系数（Y方向）— 确认是否超过允许限值（OK/NG）
payload = {
    "Argument": {
        "TABLE_TYPE": "STORY_STABILITY_COEFFICIENT_Y",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["RY(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STORY_STABILITY_COEFFICIENT_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: θ={d['Stability Coefficient']} (限值={d['Allowable Limit']}) → {d['Remark']}")
```

---

## 11. Torsional Irregularity Check

> **功能：** 扭转不规则（Torsional Irregularity）审查表格。比较外缘层间位移的平均值及1.2倍取值与最大值（Maximum Value），按 X/Y 方向判定是否扭转不规则（Regular/Irregular）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TORSIONAL_IRREGULARITY_X"` | X方向扭转不规则审查 |
| `"TORSIONAL_IRREGULARITY_Y"` | Y方向扭转不规则审查 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Average Value of Extreme Points/Story Drift", "Average Value of Extreme Points/1.2*Story Drift", "Maximum Value/Node", "Maximum Value/Story Drift", "Remark"]
```

### `ADDITIONAL` — 扭转不规则审查目标外缘节点选择（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。扭转不规则审查所用的外缘（Extreme Points）节点，可由用户直接指定以代替自动计算。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 扭转不规则审查目标外缘节点选择 | `ADDITIONAL.SELECT_IRREGULAR_ENDS` | Object | — | Required |
| 1-1-1 | 　　└ 节点选择方式：`false`=自动计算 / `true`=用户指定 | `SELECT_IRREGULAR_ENDS.USER_DEFINE` | Boolean | — | Required |
| 1-1-2 | 　　└ 指定外缘节点编号2个 — 仅当 `USER_DEFINE: true` 时 | `SELECT_IRREGULAR_ENDS.SELECT_NODES` | Array [Integer] | — | Required |

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SELECT_IRREGULAR_ENDS": {
        "USER_DEFINE": true,
        "SELECT_NODES": [1, 37]
      }
    }
  }
}
```

### Request / Response JSON

**POST 请求体 — X方向**

```json
{
  "Argument": {
    "TABLE_NAME": "TORSIONAL_IRREGULARITY_X",
    "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST 响应体 — X方向**

```json
{
  "TORSIONAL_IRREGULARITY_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Average Value of Extreme Points/Story Drift", "Average Value of Extreme Points/1.2*Story Drift", "Maximum Value/Node", "Maximum Value/Story Drift", "Remark"],
    "DATA": [
      ["1", "RX(RS)", "12F", "46.0000", "4.0000", "0.0016", "0.0019", "388", "0.0018", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 扭转不规则审查（X方向）— 确认判定（Remark）
payload = {
    "Argument": {
        "TABLE_TYPE": "TORSIONAL_IRREGULARITY_X",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RX(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TORSIONAL_IRREGULARITY_X", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 最大位移={d['Maximum Value/Story Drift']} → {d['Remark']}")
```

---

## 12. Torsional Amplification Factor

> **功能：** 计算扭转放大系数（Torsional Amplification Factor, Ax）。利用外缘平均位移与最大位移（Maximum Displacement）之比，按 X/Y 方向计算针对偶然扭转力矩的放大系数。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TORSIONAL_AMPLIFICATION_FACTOR_X"` | X方向扭转放大系数 |
| `"TORSIONAL_AMPLIFICATION_FACTOR_Y"` | Y方向扭转放大系数 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Average Displacement of Extreme Points", "Maximum Displacement/Node", "Maximum Displacement/Displacement", "Torsional Amplification Factor", "Note"]
```

### `ADDITIONAL` — 扭转放大系数计算目标外缘节点选择（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。扭转放大系数（Ax）计算所用的外缘（Extreme Points）节点，可由用户直接指定以代替自动计算。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 扭转放大系数计算目标外缘节点选择 | `ADDITIONAL.SELECT_IRREGULAR_ENDS` | Object | — | Required |
| 1-1-1 | 　　└ 节点选择方式：`false`=自动计算 / `true`=用户指定 | `SELECT_IRREGULAR_ENDS.USER_DEFINE` | Boolean | — | Required |
| 1-1-2 | 　　└ 指定外缘节点编号2个 — 仅当 `USER_DEFINE: true` 时 | `SELECT_IRREGULAR_ENDS.SELECT_NODES` | Array [Integer] | — | Required |

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SELECT_IRREGULAR_ENDS": {
        "USER_DEFINE": true,
        "SELECT_NODES": [424, 1]
      }
    }
  }
}
```

### Request / Response JSON

**POST 请求体 — X方向**

```json
{
  "Argument": {
    "TABLE_NAME": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST 响应体 — X方向**

```json
{
  "TORSIONAL_AMPLIFICATION_FACTOR_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Average Displacement of Extreme Points", "Maximum Displacement/Node", "Maximum Displacement/Displacement", "Torsional Amplification Factor", "Note"],
    "DATA": [
      ["1", "RX(RS)", "Roof", "50.0000", "0.0000", "0.0224", "424", "0.0269", "1.0063", ""]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 扭转放大系数（Y方向）— 确认 Ax 值
payload = {
    "Argument": {
        "TABLE_TYPE": "TORSIONAL_AMPLIFICATION_FACTOR_Y",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RY(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TORSIONAL_AMPLIFICATION_FACTOR_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Ax={d['Torsional Amplification Factor']}")
```

---

## 13. Stiffness Irregularity Check (Soft Story)

> **功能：** 刚度不规则（软弱层，Soft Story）审查表格。将各层刚度（Story Stiffness）与上部层刚度的0.7倍（0.7Ku1）、0.8倍平均（0.8Ku123）进行比较，以层刚度比与层位移角比按 X/Y 方向判定是否为软弱层（Regular/Irregular）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STIFFNESS_IRREGULARITY_X"` | X方向刚度不规则（软弱层）审查 |
| `"STIFFNESS_IRREGULARITY_Y"` | Y方向刚度不规则（软弱层）审查 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Story Drift", "Story Shear Force", "Story Stiffness", "Upper Story Stiffness/0.7Ku1", "Upper Story Stiffness/0.8Ku123", "Story Stiffness Ratio", "Story Drift Angle Ratio", "Remark"]
```

### `ADDITIONAL` — 层刚度计算方式设置（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。指定软弱层（Soft Story）判定所使用的层间位移计算方式与层刚度计算方式。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 计算方式设置 | `ADDITIONAL.SET_CALCULATION_METHOD` | Object | — | Required |
| 1-1-1 | 　　└ 层间位移计算方式：`"Drift at the Center of Mass"`（质心位移）/ `"Max. Drift of Outer Extreme Points"`（外缘最大位移）/ `"Max. Drift of All Vertical Elements"`（全部竖向构件最大位移） | `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` | String | `System` | Optional |
| 1-1-2 | 　　└ 层刚度计算方式：`"1 / Story Drift Ratio"`（层间位移比的倒数）/ `"Story Shear / Story Drift"`（层剪力/层间位移） | `SET_CALCULATION_METHOD.STORY_STIFFNESS_METHOD` | String | `System` | Optional |

> ⚠️ 2026-08-26 确认（article id `49513107644057`）：旧版本中曾有一条注释，指出官方 Specifications
> 表的 `"Max. Drfit of All Vertical Elements"` 拼写错误（`Drfit`→`Drift`），但
> 重新确认后官方原文已更正为 `"Drift"`（不再是笔误 — 推测官方自上次同步
> 之后已自行修改）。此外两个项的`默认值`在旧版本中分别被误记为
> `"Drift at the Center of Mass"`/`"1 / Story Drift Ratio"`，而官方
> 表两项均明确标注 `Default: System`，故予以更正。

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"],
    "ADDITIONAL": {
      "SET_CALCULATION_METHOD": {
        "STORY_DRIFT_METHOD": "Drift at the Center of Mass",
        "STORY_STIFFNESS_METHOD": "1 / Story Drift Ratio"
      }
    }
  }
}
```

### Request / Response JSON

**POST 请求体 — X方向**

```json
{
  "Argument": {
    "TABLE_NAME": "STIFFNESS_IRREGULARITY_X",
    "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["RX(RS)"]
  }
}
```

**POST 响应体 — X方向**

```json
{
  "STIFFNESS_IRREGULARITY_X": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Story Drift", "Story Shear Force", "Story Stiffness", "Upper Story Stiffness/0.7Ku1", "Upper Story Stiffness/0.8Ku123", "Story Stiffness Ratio", "Story Drift Angle Ratio", "Remark"],
    "DATA": [
      ["1", "RX(RS)", "12F", "46.0000", "4.0000", "0.0016", "979.6580", "2536.9104", "0.0000", "0.0000", "0.0000", "0.0000", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 刚度不规则（软弱层）审查（X方向）— 确认层刚度比与判定
payload = {
    "Argument": {
        "TABLE_TYPE": "STIFFNESS_IRREGULARITY_X",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["RX(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("STIFFNESS_IRREGULARITY_X", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 层刚度比={d['Story Stiffness Ratio']} → {d['Remark']}")
```

---

## 14. Capacity Irregularity Check (Weak Story)

> **功能：** 强度不规则（薄弱层，Weak Story）审查表格。将各层的抗剪强度（Story Shear Strength）与上部层抗剪强度进行比较，按两个方向（Angle1/Angle2）判定抗剪强度比（Story Shear Strength Ratio）与是否为薄弱层（Remark）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"CAPACITY_IRREGULARITY"` | 强度不规则（薄弱层）审查 |

### Response HEAD

```json
["Index", "Story", "Level", "Story Height", "Angle1", "Story Shear Strength1", "Upper Story Shear Strength1", "Story Shear Strength Ratio1", "Remark1", "Angle2", "Story Shear Strength2", "Upper Story Shear Strength2", "Story Shear Strength Ratio2", "Remark2"]
```

### `ADDITIONAL` — 强度计算角度设置（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。此处指定计算抗剪强度（Story Shear Strength）的基准角度（Angle1），Angle2 按 Angle1 + 90° 自动计算。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 角度设置 | `ADDITIONAL.SET_ANGLE` | Object | — | Required |
| 1-1-1 | 　　└ Angle1 输入角度(°) — Angle2 = Angle1 + 90° | `SET_ANGLE.ANGLE` | Number | — | Required |

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_TYPE": "CAPACITY_IRREGULARITY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 33.5
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CAPACITY_IRREGULARITY",
    "TABLE_TYPE": "CAPACITY_IRREGULARITY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 }
  }
}
```

**POST Response Body**

```json
{
  "CAPACITY_IRREGULARITY": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Story Height", "Angle1", "Story Shear Strength1", "Upper Story Shear Strength1", "Story Shear Strength Ratio1", "Remark1", "Angle2", "Story Shear Strength2", "Upper Story Shear Strength2", "Story Shear Strength Ratio2", "Remark2"],
    "DATA": [
      ["1", "12F", "46.0000", "4.0000", "33.5000", "12695.2055", "0.0000", "0.0000", "-", "123.5000", "12960.1189", "0.0000", "0.0000", "-"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 强度不规则（薄弱层）审查 — 确认各方向的抗剪强度比/判定
payload = {
    "Argument": {
        "TABLE_TYPE": "CAPACITY_IRREGULARITY",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CAPACITY_IRREGULARITY", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 强度比1={d['Story Shear Strength Ratio1']}({d['Remark1']}), "
          f"强度比2={d['Story Shear Strength Ratio2']}({d['Remark2']})")
```

---

## 15. Criteria for Regularity in Plan

> **功能：** 平面规则性（Regularity in Plan）判定标准表格。计算平动质量（Translational Mass）·转动质量（Rotational Mass）、回转半径比（Rx）与 r²/Is² 值，审查 X/Y 方向的平面规则性（Regular/Irregular）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"CRITERIA_FOR_REGULARITY_IN_PLAN"` | 平面规则性判定标准 |

### Response HEAD

```json
["Index", "Story", "Level", "Translational Mass/X-DIR", "Translational Mass/Y-DIR", "Rotational Mass", "Rx/X", "Rx/Y", "r²/Is²/X", "r²/Is²/Y", "Check/X", "Check/Y"]
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CRITERIA_FOR_REGULARITY_IN_PLAN",
    "TABLE_TYPE": "CRITERIA_FOR_REGULARITY_IN_PLAN",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 }
  }
}
```

**POST Response Body**

```json
{
  "CRITERIA_FOR_REGULARITY_IN_PLAN": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Translational Mass/X-DIR", "Translational Mass/Y-DIR", "Rotational Mass", "Rx/X", "Rx/Y", "r²/Is²/X", "r²/Is²/Y", "Check/X", "Check/Y"],
    "DATA": [
      ["1", "Roof", "50.0000", "943.5741", "943.5741", "196998.8801", "11.3386", "15.0598", "0.6158", "1.0863", "Irregular", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 平面规则性判定 — 确认各方向的 Check 结果
payload = {
    "Argument": {
        "TABLE_TYPE": "CRITERIA_FOR_REGULARITY_IN_PLAN",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4}
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CRITERIA_FOR_REGULARITY_IN_PLAN", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Check X={d['Check/X']}, Y={d['Check/Y']}")
```

---

## 16. Ultimate Story Shear For Check

> **功能：** 设计层剪力审查（Ultimate Story Shear Force Check）表格。将作用剪力（Applied Shear Force, Ve）与顺时针/逆时针极限剪力（Ultimate Shear Force, Vp）按柱、墙逐一对比，判定抗剪强度是否满足（OK/NG）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"ULTIMATE_STORY_SHEAR_FORCE_CHECK"` | 设计层剪力审查 |

### Response HEAD

```json
["Index", "Story", "Load Case", "Angle", "Applied Shear Force (Ve)", "Clockwise/Ultimate Shear Force1 (Vp)/Column", "Clockwise/Ultimate Shear Force1 (Vp)/Wall", "Clockwise/Ultimate Shear Force1 (Vp)/SUM", "Clockwise/Ratio1", "Clockwise/Beta1", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Column", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Wall", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/SUM", "Counter-Clockwise/Ratio2", "Counter-Clockwise/Beta2", "MIN", "Remark"]
```

### `ADDITIONAL` — 剪力计算角度设置（2026-07-30 官方已收录）

> ℹ️ 官方手册中另记录了 `"ADDITIONAL"` 请求对象，故在此反映。字段构成与 [14. Capacity Irregularity Check](#14-capacity-irregularity-check-weak-story) 相同（指定计算剪力所需的基准角度（Angle）），但以官方 Specifications 表为准，**这里 `SET_ANGLE`/`ANGLE` 均为 Optional** — 第14章为 Required，故必填性彼此不同。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 详细设置对象 | `"ADDITIONAL"` | Object | — | Optional |
| 1-1 | └ 角度设置 | `ADDITIONAL.SET_ANGLE` | Object | — | Optional |
| 1-1-1 | 　　└ 计算角度(°) | `SET_ANGLE.ANGLE` | Number | — | Optional |

**请求示例 — 含 `ADDITIONAL`**

```json
{
  "Argument": {
    "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["Rx(RS)"],
    "ADDITIONAL": {
      "SET_ANGLE": {
        "ANGLE": 0
      }
    }
  }
}
```

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "LOAD_CASE_NAMES": ["Rx(RS)"]
  }
}
```

**POST Response Body**

```json
{
  "ULTIMATE_STORY_SHEAR_FORCE_CHECK": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Load Case", "Angle", "Applied Shear Force (Ve)", "Clockwise/Ultimate Shear Force1 (Vp)/Column", "Clockwise/Ultimate Shear Force1 (Vp)/Wall", "Clockwise/Ultimate Shear Force1 (Vp)/SUM", "Clockwise/Ratio1", "Clockwise/Beta1", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Column", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/Wall", "Counter-Clockwise/Ultimate Shear Force2 (Vp)/SUM", "Counter-Clockwise/Ratio2", "Counter-Clockwise/Beta2", "MIN", "Remark"],
    "DATA": [
      ["1", "PR", "Rx(RS)", "0.0000", "298.9810", "0.0000", "0.0000", "0.0000", "0.0000", "-", "0.0000", "0.0000", "0.0000", "0.0000", "-", "-", "OK"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 设计层剪力审查 — 确认作用剪力(Ve)与最终判定(Remark)
payload = {
    "Argument": {
        "TABLE_TYPE": "ULTIMATE_STORY_SHEAR_FORCE_CHECK",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "LOAD_CASE_NAMES": ["Rx(RS)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("ULTIMATE_STORY_SHEAR_FORCE_CHECK", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: Ve={d['Applied Shear Force (Ve)']} → {d['Remark']}")
```

---

## 17. Weight Irregularity Check

> **功能：** 重量不规则（Weight Irregularity）审查表格。将各层重量（Story Weight）与相邻（下部）层重量的1.25倍、0.75倍进行比较，以重量比（Story Weight Ratio）按 X/Y 方向判定是否重量不规则（Regular/Irregular）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"WEIGHT_IRREGULARITY_X"` | X方向重量不规则审查 |
| `"WEIGHT_IRREGULARITY_Y"` | Y方向重量不规则审查 |

### Response HEAD

```json
["Index", "Load Case", "Story", "Level", "Story Height", "Story Weight", "Adjacent Story Weight/1.25M(Lower)", "Adjacent Story Weight/0.75M(Lower)", "Story Weight Ratio", "Story Drift Angle Ratio", "Remark"]
```

### `SET_CALCULATION_METHOD` — 层间位移计算方式设置（2026-07-24 官方已收录）

> ℹ️ 官方手册中另记录了 `"SET_CALCULATION_METHOD"` 请求字段，故在此反映。与其他表格不同，它不包裹在 `"ADDITIONAL"` 对象内，而是位于 `"Argument"` 的直接下级（= 与 `"TABLE_TYPE"`、`"UNIT"` 等同级）。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 计算方式设置（非 `"ADDITIONAL"`，而是 `"Argument"` 最上层字段） | `"SET_CALCULATION_METHOD"` | Object | — | Optional |
| 1-1 | 　　└ 层间位移计算方式：`"Drift at the Center of Mass"`（质心位移）/ `"Max. Drift of Outer Extreme Points"`（外缘最大位移）/ `"Max. Drift of All Vertical Elements"`（全部竖向构件最大位移） | `SET_CALCULATION_METHOD.STORY_DRIFT_METHOD` | String | `""` | Optional |

**请求示例 — 含 `SET_CALCULATION_METHOD`**

```json
{
  "Argument": {
    "TABLE_TYPE": "WEIGHT_IRREGULARITY_X",
    "UNIT": { "FORCE": "kgf", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["DL(ST)"],
    "SET_CALCULATION_METHOD": {
      "STORY_DRIFT_METHOD": "Drift at the Center of Mass"
    }
  }
}
```

### Request / Response JSON

**POST 请求体 — X方向**

```json
{
  "Argument": {
    "TABLE_NAME": "WEIGHT_IRREGULARITY_X",
    "TABLE_TYPE": "WEIGHT_IRREGULARITY_X",
    "UNIT": { "FORCE": "kgf", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST 响应体 — X方向**

```json
{
  "WEIGHT_IRREGULARITY_X": {
    "FORCE": "kgf",
    "DIST": "mm",
    "HEAD": ["Index", "Load Case", "Story", "Level", "Story Height", "Story Weight", "Adjacent Story Weight/1.25M(Lower)", "Adjacent Story Weight/0.75M(Lower)", "Story Weight Ratio", "Story Drift Angle Ratio", "Remark"],
    "DATA": [
      ["1", "DL", "Roof", "57700", "0", "750967.810373254", "800925.897425977", "480555.538455586", "0.172030728414953", "0", "Regular"]
    ]
  }
}
```

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# 重量不规则审查（Y方向）— 确认重量比与判定
payload = {
    "Argument": {
        "TABLE_TYPE": "WEIGHT_IRREGULARITY_Y",
        "UNIT": {"FORCE": "kgf", "DIST": "mm"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}

resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("WEIGHT_IRREGULARITY_Y", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"{d['Story']}: 重量比={d['Story Weight Ratio']} → {d['Remark']}")
```

---

## End-to-End Workflow

以下是执行反应谱解析后，按顺序提取主要楼层结果表格（层间位移 → 楼层位移 → 层剪力(RS) → 扭转不规则 → 重量不规则）并输出摘要的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_story_table(table_type, name, load_cases=None, unit=None, place=6, extra=None):
    """楼层结果表格提取公共函数"""
    arg = {
        "TABLE_NAME": name,
        "TABLE_TYPE": table_type,
        "UNIT": unit or {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": place}
    }
    if load_cases:
        arg["LOAD_CASE_NAMES"] = load_cases
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    table = resp.json().get(name, {})
    return table.get("HEAD", []), table.get("DATA", [])

# ── STEP 1: 层间位移(X) — 允许位移比判定 ─────────────────────────
head, data = get_story_table("STORY_DRIFT_X", "Drift(X)", ["RX(RS)"],
                             unit={"FORCE": "kN", "DIST": "mm"})
ng = [dict(zip(head, r)) for r in data
      if dict(zip(head, r)).get("Maximum Drift of All Vertical Elements/Remark") == "NG"]
print(f"STEP1 层间位移: {len(data)}层, 超限(NG) {len(ng)}层")

# ── STEP 2: 楼层位移(X) — 最大/平均位移比 ──────────────────────────
head, data = get_story_table("STORY_DISPLACEMENT_X", "Disp(X)", ["RX(RS)"], place=4)
for r in data[:3]:
    d = dict(zip(head, r))
    print(f"  STEP2 {d['Story']}: Max/Avg={d['Maximum/Average']}")

# ── STEP 3: 层剪力(反应谱) ─────────────────────────────────
head, data = get_story_table("STORY_SHEAR_FOR_RS", "ShearRS", ["Rx(RS)"])
if data:
    d = dict(zip(head, data[0]))
    print(f"STEP3 层剪力(RS) 最上层: Vx={d['Shear Force/With Spring/X']}")
else:
    print("STEP3 层剪力(RS): 无结果 — 需确认 (RS) 荷载工况")

# ── STEP 4: 扭转不规则(X) ───────────────────────────────────────
head, data = get_story_table("TORSIONAL_IRREGULARITY_X", "TorIrr(X)", ["RX(RS)"], place=4)
irr = [dict(zip(head, r)) for r in data
       if dict(zip(head, r)).get("Remark") == "Irregular"]
print(f"STEP4 扭转不规则: {len(data)}层中 Irregular {len(irr)}层")

# ── STEP 5: 重量不规则(X) ─────────────────────────────────────────
head, data = get_story_table("WEIGHT_IRREGULARITY_X", "WtIrr(X)", ["DL(ST)"],
                             unit={"FORCE": "kgf", "DIST": "mm"})
for r in data[:3]:
    d = dict(zip(head, r))
    print(f"  STEP5 {d['Story']}: 重量比={d['Story Weight Ratio']} → {d['Remark']}")

print("楼层结果表格批量提取完成")
```
