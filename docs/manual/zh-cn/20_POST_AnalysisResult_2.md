# 20. POST – Analysis Result Tables (Part 2)

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头部：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../20_POST_AnalysisResult_2.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分涵盖分析结果表中的**板(Plate)·平面应力(Plane Stress)·平面应变(Plane Strain)·轴对称(Axisymmetric)·实体(Solid)·连接(Link)·模态(Mode)·预应力束(Tendon)·施工阶段组合截面(Composite Section for C.S.)·墙(Wall)**结果。所有端点**均使用通用 URI `{base url}/post/TABLE`**，且仅支持 `POST` 方法。由请求体中 `"Argument"` 对象的 `TABLE_TYPE` 值决定表的种类。

---

## 通用事项

### Input URI（分析结果表通用）

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 通用 Request 结构与参数

相较前处理表（第18章）为扩展结构，支持 `UNIT`·`STYLES`·`COMPONENTS`·`NODE_ELEMS`·`LOAD_CASE_NAMES`·`OPT_CS`·`STAGE_STEP`。**下方参数表统一适用于本部分全部39张表**，各节仅另行说明 `TABLE_TYPE` enum、响应 `HEAD` 列与代表性示例。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 响应表标题 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型（各表专属 enum，参见各节） | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 力(Force) | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 长度(Length) | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 热(Heat) | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 温度(Temperature) | `UNIT.TEMP` | String | — | Optional |
| 5 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 数字格式 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 小数位数（0~15） | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 结果表显示列 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 指定节点/单元（下列3种方式之一） | `"NODE_ELEMS"` | Object | All | Optional |
| 7-1 | 方式1：逐个指定 ID（例：`[101, 102, 103]`） | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 7-2 | 方式2：指定 ID 范围（例：`"101 to 105"`） | `NODE_ELEMS.TO` | String | — | Optional |
| 7-3 | 方式3：指定结构组名（例：`"SG1"`） | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |
| 8 | 荷载名称 & 类型（下列接尾规则） | `"LOAD_CASE_NAMES"` | Array [String] | All | Optional |
| 9 | 启用施工阶段步骤（下方 ⚠️ — 各取值行为不同） | `"OPT_CS"` | Boolean | `false`（标注值） | Optional |
| 10 | 施工阶段步骤名称 | `"STAGE_STEP"` | Array [String] | All | Optional |

> ⚠️ **`OPT_CS` 为三态 — 省略与 `false` 的行为互不相同（2026-09-15 确认）。**
> `true` 切换到 Construction Stage（首阶段）并返回 CS 结果，`false` 切换到 PostCS（末阶段）并返回
> Post 结果，**若省略该字段则维持当前视图模式**，并返回与之对应的结果。
> 即显式写明 `false` 与完全不发送并不相同。关于原文依据与 Default 列不一致的
> 详细内容，请参考 [19章通用参数表](./19_POST_AnalysisResult_1.md#通用-request-结构与参数)中
> 同一项的注释。**未验证实际 API 行为。**

**`LOAD_CASE_NAMES` 接尾规则**

| 荷载类型 | 表示 |
|-----------|------|
| 静力荷载工况 | `NAME(ST)` |
| 一般组合 | `NAME(CB)` / `NAME(CB:all)` / `NAME(CB:max)` / `NAME(CB:min)` |
| 施工阶段 | `NAME(CS)` |
| 反应谱 | `NAME(RS)` |
| 移动荷载 | `NAME(MV:all)` / `NAME(MV:max)` / `NAME(MV:min)` |
| 沉降荷载 | `NAME(SM:all)` / `NAME(SM:max)` / `NAME(SM:min)` |

> **参考：** `OPT_CS`·`STAGE_STEP` 用于查询施工阶段结果。在板/实体应变（非线性·施工阶段）、预应力束伸长量等包含 `Step`·`Stage` 列的表中一并指定。`STAGE_STEP` 项为 `"CS1:001(first)"`、`"CS1:002(last)"` 或 `"nl_001"` 格式。但预应力束系列部分（第30·31·33·34·36节）、同时节点力类（第19章第13节的类似模式）、预应力束布置（第32节）不支持这两个字段，请确认相应节的专用参数。

> ⚠️ 2026-08-26 确认：以下两个参数在先前版本文档中整体遗漏 — 39张表中
> 多数（第1~19、22~25节）的官方 schema 里存在，但因各表是否适用不一，未纳入通用表，
> 而以此表整理。各节仅在存在对应项时以“专用参数”另行标注。
>
> | 参数 | 说明 | 值类型 | 默认值 | 适用节（以1~25节为准） |
> |---|---|---|---|---|
> | `"AVERAGE_NODAL_RESULT"` | 节点平均值结果选项 | Boolean | `false` | 1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19,23,24,25 |
> | `"NODE_FLAG"`（下级：`CENTER`/`NODES`，两者均为 Boolean/`false`） | 单元中心(Cent)/节点(Node)各自输出与否 | Object | — | 3,4,5,6,7,10,11,14,15,18,19,22,23,24,25 |
>
> 第20~21节（Solid Force Local/Global）已确认原文中两个参数均不存在（无变更）。

### 通用 Response 结构

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

## 表列表

| No. | 表 | `TABLE_TYPE` |
|-----|--------|--------------|
| 1 | [Plate Force (Local)](#1-plate-force-local) | `PLATEFORCEL` |
| 2 | [Plate Force (Global)](#2-plate-force-global) | `PLATEFORCEG` |
| 3 | [Plate Force (Unit Length)](#3-plate-force-unit-length) | `PLATEFORCEUL` / `PLATEFORCEUG` / `PLATEFORCEULVBM` / `PLATEFORCEUGVBM` / `PLATEFORCEWA` |
| 4 | [Plate Stress (Local)](#4-plate-stress-local) | `PLATESTRESSL` |
| 5 | [Plate Stress (Global)](#5-plate-stress-global) | `PLATESTRESSG` |
| 6 | [Plate Strain (Local)](#6-plate-strain-local) | `PLATESTRAINPL` / `PLATESTRAINTL` |
| 7 | [Plate Strain (Global)](#7-plate-strain-global) | `PLATESTRAINPG` / `PLATESTRAINTG` |
| 8 | [Plane Stress Force (Local)](#8-plane-stress-force-local) | `PLANESTRESSFL` |
| 9 | [Plane Stress Force (Global)](#9-plane-stress-force-global) | `PLANESTRESSFG` |
| 10 | [Plane Stress (Local)](#10-plane-stress-local) | `PLANESTRESSSL` |
| 11 | [Plane Stress (Global)](#11-plane-stress-global) | `PLANESTRESSSG` |
| 12 | [Plane Strain Force (Local)](#12-plane-strain-force-local) | `PLANESTRAINFL` |
| 13 | [Plane Strain Force (Global)](#13-plane-strain-force-global) | `PLANESTRAINFG` |
| 14 | [Plane Strain Stress (Local)](#14-plane-strain-stress-local) | `PLANESTRAINSL` |
| 15 | [Plane Strain Stress (Global)](#15-plane-strain-stress-global) | `PLANESTRAINSG` |
| 16 | [Axisymmetric Force (Local)](#16-axisymmetric-force-local) | `AXISYMMETRICFL` |
| 17 | [Axisymmetric Force (Global)](#17-axisymmetric-force-global) | `AXISYMMETRICFG` |
| 18 | [Axisymmetric Stress (Local)](#18-axisymmetric-stress-local) | `AXISYMMETRICSL` |
| 19 | [Axisymmetric Stress (Global)](#19-axisymmetric-stress-global) | `AXISYMMETRICSG` |
| 20 | [Solid Force (Local)](#20-solid-force-local) | `SOLIDFL` |
| 21 | [Solid Force (Global)](#21-solid-force-global) | `SOLIDFG` |
| 22 | [Solid Stress (Local)](#22-solid-stress-local) | `SOLIDSL` |
| 23 | [Solid Stress (Global)](#23-solid-stress-global) | `SOLIDSG` |
| 24 | [Solid Strain (Local)](#24-solid-strain-local) | `SOLID_LOCA_PLAST_STRAIN` / `SOLID_LOCA_TOTAL_STRAIN` |
| 25 | [Solid Strain (Global)](#25-solid-strain-global) | `SOLID_GLOB_PLAST_STRAIN` / `SOLID_GLOB_TOTAL_STRAIN` |
| 26 | [Elastic Link](#26-elastic-link) | `ELASTICLINK` / `ELASTICLINKVBM` |
| 27 | [General Link](#27-general-link) | `GENERAL_LINK_FORCE` / `GENERAL_LINK_FORCEVBM` / `GENERAL_LINK_DEFORM` |
| 28 | [Vibration Mode Shape](#28-vibration-mode-shape) | `EIGENVALUEMODE` / `PARTICIPATIONVECTORMODE` |
| 29 | [Buckling Mode Shape](#29-buckling-mode-shape) | `BUCKLINGMODE` |
| 30 | [Tendon Coordinates](#30-tendon-coordinates) | `TNDN_COORDINATES` |
| 31 | [Tendon Elongation](#31-tendon-elongation) | `TNDN_ELONGATION` |
| 32 | [Tendon Arrangement](#32-tendon-arrangement) | `TNDN_ARRANGEMENT` |
| 33 | [Tendon Loss](#33-tendon-loss) | `TNDN_LOSS_FORCE` / `TNDN_LOSS_STRESS` |
| 34 | [Tendon Weight](#34-tendon-weight) | `TNDN_WEIGHT_GROUP` / `TNDN_WEIGHT_PROFILE` / `TNDN_WEIGHT_PROPERTY` |
| 35 | [Tendon Stress Limit Check](#35-tendon-stress-limit-check) | `TNDN_STRS_LIMIT_CHECK` |
| 36 | [Tendon Approximate Loss](#36-tendon-approximate-loss) | `TNDN_APPROX_LOSS_FORCE` / `TNDN_APPROX_LOSS_STRESS` |
| 37 | [Composite Section for C.S. (Force and Stress)](#37-composite-section-for-cs-force-and-stress) | `COMPSECTBEAMFORCE` / `COMPSECTBEAMSTRESS` |
| 38 | [Composite Section for C.S. (Self-Constraint Force and Stress)](#38-composite-section-for-cs-self-constraint-force-and-stress) | `SELF_CONST_BEAM_FORCE` / `SELF_CONST_BEAM_STRESS` |
| 39 | [Wall Force](#39-wall-force) | `WALL_FORCE_MOMENT` |

---

## 1. Plate Force (Local)

> **功能：** 按单元局部坐标系(Local)提取板(Plate)单元各节点的构件内力/弯矩。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATEFORCEL"` | Plate 构件内力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForceLocal",
    "TABLE_TYPE": "PLATEFORCEL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "592", "DL", "773", "39.425020700000", "0.000000000025", "10.288067200000", "0.000000000090", "-2.325503050000", "0.000000000297"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取板单元构件内力（局部坐标系） ────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateForceLocal",
        "TABLE_TYPE": "PLATEFORCEL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateForceLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} Node {d['Node']}: Fx={d['Fx']}, Mz={d['Mz']}")
```

---

## 2. Plate Force (Global)

> **功能：** 按全局坐标系(Global)提取板(Plate)单元各节点的构件内力/弯矩。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATEFORCEG"` | Plate 构件内力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ", "MX", "MY", "MZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForceGlobal",
    "TABLE_TYPE": "PLATEFORCEG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "592", "DL", "773", "39.425020700000", "0.000000000025", "10.288067200000", "0.000000000090", "-2.325503050000", "0.000000000297"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取板单元构件内力（全局坐标系） ────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateForceGlobal",
        "TABLE_TYPE": "PLATEFORCEG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateForceGlobal", {})
print(f"板构件内力(全局) {len(table.get('DATA', []))} 行")
```

---

## 3. Plate Force (Unit Length)

> **功能：** 提取板(Plate)单元单位长度的构件内力/弯矩（ membrane 力 Fxx·Fyy·Fxy、弯曲 Mxx·Myy·Mxy、主值 Fmax/Fmin·Mmax/Mmin、剪力 Vxx·Vyy）。可选局部/全局、一般/最大值基准(by-max)、Wood-Armer 设计弯矩。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATEFORCEUL"` | 单位长度构件内力（局部坐标系，Unit Length Local） |
| `"PLATEFORCEUG"` | 单位长度构件内力（全局坐标系，Unit Length Global） |
| `"PLATEFORCEULVBM"` | 单位长度构件内力（局部，最大值基准，View by Max Value） |
| `"PLATEFORCEUGVBM"` | 单位长度构件内力（全局，最大值基准，View by Max Value） |
| `"PLATEFORCEWA"` | 单位长度构件内力（Wood-Armer 设计弯矩） |

> ⚠️ 2026-08-26 确认（article id `36012822385817`）：本表除 `AVERAGE_NODAL_RESULT`/
> `NODE_FLAG`（参见通用事项）外，还支持 `ULVBM`/`UGVBM` 专用的 `"ITEM_TO_DISPLAY"`（Array [String]，
> enum: `Fxx`/`Fyy`/`Fxy`/`Mxx`/`Myy`/`Mxy`/`Vxx`/`Vyy`，默认值 All，Optional）。
> 此外先前版本文档只标注了 `PLATEFORCEUL`/`UG` 的一个 Response HEAD，易被误认为
> `ULVBM`/`UGVBM`·`WA` 也是同一结构 — 实际如下方所示具有3种互不相同的响应结构。

### Response HEAD

- `PLATEFORCEUL`/`PLATEFORCEUG`: `["Index", "Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Angle", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Angle", "Vxx", "Vyy"]`
- `PLATEFORCEULVBM`/`PLATEFORCEUGVBM`: 在 `Node` 之后 `Component` 列被追加， `Fmax`/`Fmin`/`Mmax`/`Mmin`/`Angle` 被移除 — `["Index", "Elem", "Load", "Node", "Component", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"]`
- `PLATEFORCEWA`(Wood-Armer)：结构完全不同 — 完全没有 `Fxx`/`Fyy` 系列，按4个方向（Top Dir.1/Dir.2、Bot Dir.1/Dir.2）各自重复 `Ma`/`Mb`/`Mab`/`W-AMoment` 区块循环出现 — `["Index", "Elem", "Load", "Node", "Ma", "Mb", "Mab", "W-AMomentTopDir.1", "Ma", "Mb", "Mab", "W-AMomentTopDir.2", "Ma", "Mb", "Mab", "W-AMomentBotDir.1", "Ma", "Mb", "Mab", "W-AMomentBotDir.2"]`

### Request / Response JSON

**POST Request Body — PLATEFORCEUL**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForceUnitLength",
    "TABLE_TYPE": "PLATEFORCEUL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Vxx", "Vyy"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body — PLATEFORCEUL**

```json
{
  "PlateForceUnitLength": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fxx", "Fyy", "Fxy", "Fmax", "Fmin", "Angle", "Mxx", "Myy", "Mxy", "Mmax", "Mmin", "Angle", "Vxx", "Vyy"],
    "DATA": [
      ["1", "592", "DL", "773", "-108.226897000000", "5.103138340000", "-0.000000011818", "5.103138340000", "-108.226897000000", "-89.999999994025", "1.744257540000", "0.141650776000", "0.000000000120", "1.744257540000", "0.141650776000", "0.000000004303", "-1.405381470000", "-0.000000000024"]
    ]
  }
}
```

**POST Request Body — PLATEFORCEULVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForce(UL:L)ViewByMaxValue",
    "TABLE_TYPE": "PLATEFORCEULVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Component", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"],
    "NODE_ELEMS": { "KEYS": [503] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "AVERAGE_NODAL_RESULT": true,
    "NODE_FLAG": { "CENTER": false, "NODES": true },
    "ITEM_TO_DISPLAY": ["Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"]
  }
}
```

**POST Response Body — PLATEFORCEULVBM(View by Max Value)**

```json
{
  "PlateForce(UL:L)ViewByMaxValue": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Component", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"],
    "DATA": [
      ["1", "503", "STLENV_STR(max)", "52", "Fxx", "14.643051500000", "14.413288400000", "28.554175400000", "6.211062100000", "11.092328400000", "11.090774500000", "23.467790500000", "69.014747700000"],
      ["2", "503", "STLENV_STR(max)", "52", "Fyy", "14.643051500000", "14.413288400000", "28.554175400000", "6.211062100000", "11.092328400000", "11.090774500000", "23.467790500000", "69.014747700000"]
    ]
  }
}
```

**POST Request Body — PLATEFORCEWA(Wood-Armer)**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateForce(UnitLength:W-AMoment)",
    "TABLE_TYPE": "PLATEFORCEWA",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Ma", "Mb", "Mab", "W-AMomentTopDir.1", "Ma", "Mb", "Mab", "W-AMomentTopDir.2", "Ma", "Mb", "Mab", "W-AMomentBotDir.1", "Ma", "Mb", "Mab", "W-AMomentBotDir.2"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"],
    "AVERAGE_NODAL_RESULT": true,
    "NODE_FLAG": { "CENTER": false, "NODES": true }
  }
}
```

**POST Response Body — PLATEFORCEWA(Wood-Armer)**

```json
{
  "PlateForce(UnitLength:W-AMoment)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Ma", "Mb", "Mab", "W-AMomentTopDir.1", "Ma", "Mb", "Mab", "W-AMomentTopDir.2", "Ma", "Mb", "Mab", "W-AMomentBotDir.1", "Ma", "Mb", "Mab", "W-AMomentBotDir.2"],
    "DATA": [
      ["1", "592", "DL", "773", "1.744257540000", "0.141650776000", "0.000000000120", "0.054348959200", "1.744257540000", "0.141650776000", "0.000000000120", "0.105709883000", "1.744257540000", "0.141650776000", "0.000000000120", "1.788450260000", "1.744257540000", "0.141650776000", "0.000000000120", "0.237204424000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取单位长度板构件内力 ───────────────────────────────
#   Wood-Armer 设计弯矩：TABLE_TYPE="PLATEFORCEWA"
#   最大值基准(by-max)：   TABLE_TYPE="PLATEFORCEULVBM" / "PLATEFORCEUGVBM"
payload = {
    "Argument": {
        "TABLE_NAME": "PlateForceUnitLength",
        "TABLE_TYPE": "PLATEFORCEUL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateForceUnitLength", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Mmax={d['Mmax']}, Mmin={d['Mmin']}")
```

---

## 4. Plate Stress (Local)

> **功能：** 按单元局部坐标系(Local)提取板(Plate)单元上·下表面(Top/Bot)各自的应力。包含分量应力(Sig-xx·yy·xy)、主应力(Sig-Max/Min)、有效应力(Sig-EFF)、最大剪应力(Max-Shear)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATESTRESSL"` | Plate 应力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`  
（前8个为 `Top` 分量，后8个为 `Bot` 分量）

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStressLocal",
    "TABLE_TYPE": "PLATESTRESSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear", "Part", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "592", "DL", "773", "Top", "-0.600356311193", "0.006814078891", "-0.000000000059", "0.006814078891", "-0.600356311193", "-89.999999994449", "0.603792188859", "0.303585195042", "Bot", "-0.265458864386", "0.034011027791", "-0.000000000036", "0.034011027791", "-0.265458864386", "-89.999999993166", "0.283995928680", "0.149734946089"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取板应力（局部坐标系） ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStressLocal",
        "TABLE_TYPE": "PLATESTRESSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStressLocal", {})
print(f"板应力(局部) {len(table.get('DATA', []))} 行")
```

---

## 5. Plate Stress (Global)

> **功能：** 按全局坐标系(Global)提取板(Plate)单元上·下表面(Top/Bot)各自的应力。包含6分量应力(Sig-XX·YY·ZZ·XY·YZ·XZ)以及主应力·有效应力·最大剪应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATESTRESSG"` | Plate 应力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear"]`  
（前11个为 `Top` 分量，后11个为 `Bot` 分量）

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStressGlobal",
    "TABLE_TYPE": "PLATESTRESSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [592] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear", "Part", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "ANG", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "592", "DL", "773", "Top", "-0.600356311193", "0.006814078891", "0.000000000000", "-0.000000000059", "0.000000000000", "0.000000000000", "0.006814078891", "-0.600356311193", "0.000000005579", "0.603792188859", "0.303585195042", "Bot", "-0.265458864386", "0.034011027791", "0.000000000000", "-0.000000000036", "0.000000000000", "0.000000000000", "0.034011027791", "-0.265458864386", "0.000000026901", "0.283995928680", "0.149734946089"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取板应力（全局坐标系） ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStressGlobal",
        "TABLE_TYPE": "PLATESTRESSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [592]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStressGlobal", {})
print(f"板应力(全局) {len(table.get('DATA', []))} 行")
```

---

## 6. Plate Strain (Local)

> **功能：** 按单元局部坐标系(Local)提取板(Plate)单元上·下表面(Top/Bot)各自的应变。可选塑性应变(Plastic)/总应变(Total)，并按非线性·施工阶段的 `Step` 查询。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATESTRAINPL"` | Plate 应变（局部，塑性 Plastic Strain） |
| `"PLATESTRAINTL"` | Plate 应变（局部，总 Total Strain） |

> ⚠️ 2026-08-26 确认：本表 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional — 单元中心(Cent)/按节点输出与否）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"]`  
（前7个为 `Top` 分量，后7个为 `Bot` 分量）

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStrainLocal",
    "TABLE_TYPE": "PLATESTRAINTL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStrainLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-xx", "Strain-yy", "Strain-xy", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"],
    "DATA": [
      ["1", "1", "Comp", "nl_001", "Cent", "Top", "-8.741440490892e-07", "9.705634584017e-06", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06", "Bot", "-8.741440490892e-07", "9.705634584017e-06", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取板应变（局部） ───────────────────────────────────
#   塑性应变：TABLE_TYPE="PLATESTRAINPL"
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStrainLocal",
        "TABLE_TYPE": "PLATESTRAINTL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStrainLocal", {})
print(f"板应变(局部) {len(table.get('DATA', []))} 行")
```

---

## 7. Plate Strain (Global)

> **功能：** 按全局坐标系(Global)提取板(Plate)单元上·下表面(Top/Bot)各自的应变。可选塑性/总应变，包含6分量(Strain-XX·YY·ZZ·XY·YZ·XZ)以及主应变·最大剪应变。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLATESTRAINPG"` | Plate 应变（全局，塑性 Plastic Strain） |
| `"PLATESTRAINTG"` | Plate 应变（全局，总 Total Strain） |

> ⚠️ 2026-08-26 确认：本表 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional — 单元中心(Cent)/按节点输出与否）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"]`  
（前10个为 `Top` 分量，后10个为 `Bot` 分量）

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlateStrainGlobal",
    "TABLE_TYPE": "PLATESTRAINTG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "PlateStrainGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear", "Part", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-Max", "Strain-Min", "Angle", "Max-Shear"],
    "DATA": [
      ["1", "1", "Comp", "nl_001", "Cent", "Top", "-8.741440490892e-07", "0.000000000000e+00", "9.705634584017e-06", "0.000000000000e+00", "0.000000000000e+00", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06", "Bot", "-8.741440490892e-07", "0.000000000000e+00", "9.705634584017e-06", "0.000000000000e+00", "0.000000000000e+00", "3.124953352515e-06", "1.055970672867e-05", "-1.728216193741e-06", "7.471396063715e+01", "6.143961461205e-06"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取板应变（全局） ───────────────────────────────────
#   塑性应变：TABLE_TYPE="PLATESTRAINPG"
payload = {
    "Argument": {
        "TABLE_NAME": "PlateStrainGlobal",
        "TABLE_TYPE": "PLATESTRAINTG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlateStrainGlobal", {})
print(f"板应变(全局) {len(table.get('DATA', []))} 行")
```

---

## 8. Plane Stress Force (Local)

> **功能：** 按单元局部坐标系(Local)提取平面应力(Plane Stress)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRESSFL"` | 平面应力单元构件内力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressForceLocal",
    "TABLE_TYPE": "PLANESTRESSFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStressForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-920.132331101835", "-13.885776516351"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应力单元构件内力（局部） ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressForceLocal",
        "TABLE_TYPE": "PLANESTRESSFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressForceLocal", {})
for row in table.get("DATA", []):
    print(f"  Elem {row[1]} Node {row[3]}: Fx={row[4]}, Fy={row[5]}")
```

---

## 9. Plane Stress Force (Global)

> **功能：** 按全局坐标系(Global)提取平面应力(Plane Stress)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRESSFG"` | 平面应力单元构件内力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressForceGlobal",
    "TABLE_TYPE": "PLANESTRESSFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStressForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-920.132331101835", "-13.885776516351", "0.000000000000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应力单元构件内力（全局） ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressForceGlobal",
        "TABLE_TYPE": "PLANESTRESSFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressForceGlobal", {})
print(f"平面应力构件内力(全局) {len(table.get('DATA', []))} 行")
```

---

## 10. Plane Stress (Local)

> **功能：** 按单元局部坐标系(Local)提取平面应力(Plane Stress)单元的应力。包含分量应力·主应力·有效应力(Sig-EFF)·最大剪应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRESSSL"` | 平面应力单元应力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressLocal",
    "TABLE_TYPE": "PLANESTRESSSL",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 确认：`COMPONENTS` 中遗漏了 `"Angle"`（HEAD 中原本已有），且 `UNIT`
> 被误标为 `kN`/`m`（DATA 值本身与原文示例的 N/mm 值一致，仅单位标注不一致
> — 已更正为 N/mm）。

**POST Response Body**

```json
{
  "PlaneStressLocal": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-xy", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "9.923982961671", "1.180584451040", "-0.319470675593", "9.935640398605", "1.168927014105", "-2.089787188087", "9.405812140923", "4.967820199303"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应力单元应力（局部） ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressLocal",
        "TABLE_TYPE": "PLANESTRESSSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-EFF={d['Sig-EFF']}")
```

---

## 11. Plane Stress (Global)

> **功能：** 按全局坐标系(Global)提取平面应力(Plane Stress)单元的应力。包含6分量应力(Sig-XX·YY·ZZ·XY·YZ·XZ)以及主应力·有效应力·最大剪应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRESSSG"` | 平面应力单元应力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStressGlobal",
    "TABLE_TYPE": "PLANESTRESSSG",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 确认：`COMPONENTS` 中遗漏了 `"Angle"`，且 `UNIT` 被误标为 `kN`/`m`
> （值与原文 N/mm 示例一致 — 与第10节同一模式）。

**POST Response Body**

```json
{
  "PlaneStressGlobal": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-Max", "Sig-Min", "Angle", "Sig-EFF", "Max-Shear"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "9.923982961671", "1.180584451040", "0.000000000000", "-0.319470675593", "0.000000000000", "0.000000000000", "9.935640398605", "1.168927014105", "-2.089787188087", "9.405812140923", "4.967820199303"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应力单元应力（全局） ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStressGlobal",
        "TABLE_TYPE": "PLANESTRESSSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStressGlobal", {})
print(f"平面应力应力(全局) {len(table.get('DATA', []))} 行")
```

---

## 12. Plane Strain Force (Local)

> **功能：** 按单元局部坐标系(Local)提取平面应变(Plane Strain)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRAINFL"` | 平面应变单元构件内力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainForceLocal",
    "TABLE_TYPE": "PLANESTRAINFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStrainForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-1027.821540000000", "-45.249848700000", "0.000000000000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应变单元构件内力（局部） ───────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainForceLocal",
        "TABLE_TYPE": "PLANESTRAINFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainForceLocal", {})
print(f"平面应变构件内力(局部) {len(table.get('DATA', []))} 行")
```

---

## 13. Plane Strain Force (Global)

> **功能：** 按全局坐标系(Global)提取平面应变(Plane Strain)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRAINFG"` | 平面应变单元构件内力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainForceGlobal",
    "TABLE_TYPE": "PLANESTRAINFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "PlaneStrainForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "-1027.821540000000", "0.000000000000", "-45.249848700000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应变单元构件内力（全局） ───────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainForceGlobal",
        "TABLE_TYPE": "PLANESTRAINFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainForceGlobal", {})
print(f"平面应变构件内力(全局) {len(table.get('DATA', []))} 行")
```

---

## 14. Plane Strain Stress (Local)

> **功能：** 按单元局部坐标系(Local)提取平面应变(Plane Strain)单元的应力。包含分量应力·主应力(Sig-P1/P2/P3)·最大剪应力·有效应力(Sig-EFF)·八面体应力(Sig-OCT)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRAINSL"` | 平面应变单元应力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainStressLocal",
    "TABLE_TYPE": "PLANESTRAINSL",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 确认：`UNIT` 被误标为 `kN`/`m`（值与原文 N/mm 示例一致）。

**POST Response Body**

```json
{
  "PlaneStrainStressLocal": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "11.045924719309", "1.590139074056", "2.274491482806", "-0.288713831615", "11.054731825832", "2.274491482806", "1.581331967533", "4.736699929150", "9.146540205732", "4.311720402579"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应变单元应力（局部） ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainStressLocal",
        "TABLE_TYPE": "PLANESTRAINSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-EFF={d['Sig-EFF']}")
```

---

## 15. Plane Strain Stress (Global)

> **功能：** 按全局坐标系(Global)提取平面应变(Plane Strain)单元的应力。包含分量应力·主应力·最大剪应力·有效应力·八面体应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"PLANESTRAINSG"` | 平面应变单元应力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "PlaneStrainStressGlobal",
    "TABLE_TYPE": "PLANESTRAINSG",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
  }
}
```

> ⚠️ 2026-08-26 确认：`UNIT` 被误标为 `kN`/`m`（值与原文 N/mm 示例一致）。

**POST Response Body**

```json
{
  "PlaneStrainStressGlobal": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "1", "DeadLoads", "1", "11.045924719309", "2.274491482806", "1.590139074056", "-0.288713831615", "11.054731825832", "2.274491482806", "1.581331967533", "4.736699929150", "9.146540205732", "4.311720402579"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取平面应变单元应力（全局） ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "PlaneStrainStressGlobal",
        "TABLE_TYPE": "PLANESTRAINSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DeadLoads(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("PlaneStrainStressGlobal", {})
print(f"平面应变应力(全局) {len(table.get('DATA', []))} 行")
```

---

## 16. Axisymmetric Force (Local)

> **功能：** 按单元局部坐标系(Local)提取轴对称(Axisymmetric)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"AXISYMMETRICFL"` | 轴对称单元构件内力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiForceLocal",
    "TABLE_TYPE": "AXISYMMETRICFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "DATA": [
      ["1", "168", "Pressure", "195", "38.836185000000", "-21.331526100000", "0.000000000000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取轴对称单元构件内力（局部） ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiForceLocal",
        "TABLE_TYPE": "AXISYMMETRICFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiForceLocal", {})
print(f"轴对称构件内力(局部) {len(table.get('DATA', []))} 行")
```

---

## 17. Axisymmetric Force (Global)

> **功能：** 按全局坐标系(Global)提取轴对称(Axisymmetric)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"AXISYMMETRICFG"` | 轴对称单元构件内力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional — 节点平均值结果选项）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiForceGlobal",
    "TABLE_TYPE": "AXISYMMETRICFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "168", "Pressure", "195", "37.968593500000", "0.000000000000", "-22.839378200000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取轴对称单元构件内力（全局） ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiForceGlobal",
        "TABLE_TYPE": "AXISYMMETRICFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiForceGlobal", {})
print(f"轴对称构件内力(全局) {len(table.get('DATA', []))} 行")
```

---

## 18. Axisymmetric Stress (Local)

> **功能：** 按单元局部坐标系(Local)提取轴对称(Axisymmetric)单元的应力。包含分量应力·主应力·最大剪应力·有效应力·八面体应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"AXISYMMETRICSL"` | 轴对称单元应力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiStressLocal",
    "TABLE_TYPE": "AXISYMMETRICSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "168", "Pressure", "195", "1990.431496539230", "2083.494588655180", "2037.166754685250", "593.843481294873", "2632.626761027040", "2037.166754685250", "1441.299324167370", "595.663718429839", "1031.719844657850", "486.357398961529"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取轴对称单元应力（局部） ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiStressLocal",
        "TABLE_TYPE": "AXISYMMETRICSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-P1={d['Sig-P1']}, Sig-EFF={d['Sig-EFF']}")
```

---

## 19. Axisymmetric Stress (Global)

> **功能：** 按全局坐标系(Global)提取轴对称(Axisymmetric)单元的应力。包含分量应力·主应力·最大剪应力·有效应力·八面体应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"AXISYMMETRICSG"` | 轴对称单元应力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "AxiStressGlobal",
    "TABLE_TYPE": "AXISYMMETRICSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [168] },
    "LOAD_CASE_NAMES": ["Pressure(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "AxiStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "DATA": [
      ["1", "168", "Pressure", "195", "2037.166754718370", "2037.166754685250", "2036.759330476040", "595.663683594885", "2632.626761026030", "2037.166754685250", "1441.299324168380", "595.663718428826", "1031.719844655510", "486.357398960426"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取轴对称单元应力（全局） ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "AxiStressGlobal",
        "TABLE_TYPE": "AXISYMMETRICSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [168]},
        "LOAD_CASE_NAMES": ["Pressure(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("AxiStressGlobal", {})
print(f"轴对称应力(全局) {len(table.get('DATA', []))} 行")
```

---

## 20. Solid Force (Local)

> **功能：** 按单元局部坐标系(Local)提取实体(Solid)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SOLIDFL"` | 实体单元构件内力（局部坐标系，Local） |

### Response HEAD

`["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidForceLocal",
    "TABLE_TYPE": "SOLIDFL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidForceLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Fx", "Fy", "Fz"],
    "DATA": [
      ["1", "3381", "DL", "4052", "0.707825934544", "0.602292418927", "0.687505765503"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取实体单元构件内力（局部） ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidForceLocal",
        "TABLE_TYPE": "SOLIDFL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidForceLocal", {})
print(f"实体构件内力(局部) {len(table.get('DATA', []))} 行")
```

---

## 21. Solid Force (Global)

> **功能：** 按全局坐标系(Global)提取实体(Solid)单元的节点构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SOLIDFG"` | 实体单元构件内力（全局坐标系，Global） |

### Response HEAD

`["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidForceGlobal",
    "TABLE_TYPE": "SOLIDFG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "FX", "FY", "FZ"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidForceGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "3381", "DL", "4052", "0.845100207437", "-0.386754897708", "0.687505765503"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取实体单元构件内力（全局） ───────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidForceGlobal",
        "TABLE_TYPE": "SOLIDFG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidForceGlobal", {})
print(f"实体构件内力(全局) {len(table.get('DATA', []))} 行")
```

---

## 22. Solid Stress (Local)

> **功能：** 按单元局部坐标系(Local)提取实体(Solid)单元的应力。包含6分量应力·主应力(Sig-P1/P2/P3)及各主应力的方向余弦（P1/ux·uy·uz 等）·最大剪应力·有效应力·八面体应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SOLIDSL"` | 实体单元应力（局部坐标系，Local） |

> ⚠️ 2026-08-26 确认：本表 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional — 单元中心(Cent)/按节点输出与否）（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStressLocal",
    "TABLE_TYPE": "SOLIDSL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStressLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"],
    "DATA": [
      ["1", "3381", "DL", "Cent", "-0.009540404177", "-0.009754688093", "-0.067613370680", "0.000000149510", "-0.000003700681", "-0.003643177715", "-0.009312743454", "-0.009754688186", "-0.067841031311", "0.029264143929", "0.058308571635", "0.027486924270", "0.998052857758", "0.000859886913", "-0.062367890106", "-0.000862168620", "0.999999628286", "-0.000009672638", "0.062367858606", "0.000063425441", "0.998053228135"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取实体单元应力（局部） ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStressLocal",
        "TABLE_TYPE": "SOLIDSL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStressLocal", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']}: Sig-P1={d['Sig-P1']}, Sig-EFF={d['Sig-EFF']}")
```

---

## 23. Solid Stress (Global)

> **功能：** 按全局坐标系(Global)提取实体(Solid)单元的应力。包含6分量应力·主应力·方向余弦·最大剪应力·有效应力·八面体应力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SOLIDSG"` | 实体单元应力（全局坐标系，Global） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStressGlobal",
    "TABLE_TYPE": "SOLIDSG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT"],
    "NODE_ELEMS": { "KEYS": [3381] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStressGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Node", "Sig-XX", "Sig-YY", "Sig-ZZ", "Sig-XY", "Sig-YZ", "Sig-XZ", "Sig-P1", "Sig-P2", "Sig-P3", "Max-Shear", "Sig-EFF", "Sig-OCT", "Sig-P1/ux", "Sig-P1/uy", "Sig-P1/uz", "Sig-P2/ux", "Sig-P2/uy", "Sig-P2/uz", "Sig-P3/ux", "Sig-P3/uy", "Sig-P3/uz"],
    "DATA": [
      ["1", "3381", "DL", "4052", "-0.013482340647", "-0.013660921945", "-0.066735565488", "0.000127121684", "0.003275593336", "-0.002050775097", "-0.013403458224", "-0.013459546178", "-0.067015823678", "0.026806182727", "0.053584343493", "0.025259901766", "0.999095568656", "0.020691098082", "-0.037147316882", "-0.018358914462", "0.997903478478", "0.062061243156", "0.038353552001", "-0.061323128609", "0.997380809393"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取实体单元应力（全局） ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStressGlobal",
        "TABLE_TYPE": "SOLIDSG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [3381]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStressGlobal", {})
print(f"实体应力(全局) {len(table.get('DATA', []))} 行")
```

---

## 24. Solid Strain (Local)

> **功能：** 按单元局部坐标系(Local)提取实体(Solid)单元的应变。可选塑性/总应变，并按非线性·施工阶段的 `Step` 查询。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SOLID_LOCA_PLAST_STRAIN"` | 实体应变（局部，塑性 Plastic Strain） |
| `"SOLID_LOCA_TOTAL_STRAIN"` | 实体应变（局部，总 Total Strain） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

- `SOLID_LOCA_TOTAL_STRAIN`: `["Index", "Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"]`
- `SOLID_LOCA_PLAST_STRAIN`: 在上述列之后 `Comp.Damage`/`Tens.Damage`/`Damage` 共新增3个列。

> ⚠️ 2026-08-26 确认：`SOLID_LOCA_PLAST_STRAIN` 专用列3个（`Comp.Damage`/`Tens.Damage`/
> `Damage`）在先前版本文档中有所遗漏（因只标注了单一 HEAD，塑性/总应变具有相同结构
> 的说法易被误认）。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStrainLocal",
    "TABLE_TYPE": "SOLID_LOCA_TOTAL_STRAIN",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [205] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStrainLocal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Strain-xx", "Strain-yy", "Strain-zz", "Strain-xy", "Strain-yz", "Strain-xz", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "DATA": [
      ["1", "205", "Comp", "nl_001", "1", "4.390947924304e-06", "-1.526607997151e-07", "-1.869003906363e-07", "1.999020761608e-06", "-2.101840625867e-08", "6.652619107252e-07", "5.215377841926e-06", "-1.701366927411e-07", "-9.938544152325e-07", "3.104616128579e-06"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取实体应变（局部） ───────────────────────────────
#   塑性应变：TABLE_TYPE="SOLID_LOCA_PLAST_STRAIN"
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStrainLocal",
        "TABLE_TYPE": "SOLID_LOCA_TOTAL_STRAIN",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [205]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStrainLocal", {})
print(f"实体应变(局部) {len(table.get('DATA', []))} 行")
```

---

## 25. Solid Strain (Global)

> **功能：** 按全局坐标系(Global)提取实体(Solid)单元的应变。可选塑性/总应变，并按非线性·施工阶段的 `Step` 查询。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SOLID_GLOB_PLAST_STRAIN"` | 实体应变（全局，塑性 Plastic Strain） |
| `"SOLID_GLOB_TOTAL_STRAIN"` | 实体应变（全局，总 Total Strain） |

> ⚠️ 2026-08-26 确认：本表 `"AVERAGE_NODAL_RESULT"`（Boolean、默认值 `false`、Optional）与 `"NODE_FLAG"`（Object: `CENTER`/`NODES`，两者均为 Boolean·默认值 `false`、Optional）两者均支持（参见通用事项中的适用节表）。先前版本文档中有所遗漏。

### Response HEAD

- `SOLID_GLOB_TOTAL_STRAIN`: `["Index", "Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"]`
- `SOLID_GLOB_PLAST_STRAIN`: 在上述列之后 `Comp.Damage`/`Tens.Damage`/`Damage` 共新增3个列。

> ⚠️ 2026-08-26 确认：`SOLID_GLOB_PLAST_STRAIN` 专用列3个（`Comp.Damage`/`Tens.Damage`/
> `Damage`）在先前版本文档中有所遗漏（与第24节同一模式）。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "SolidStrainGlobal",
    "TABLE_TYPE": "SOLID_GLOB_TOTAL_STRAIN",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "NODE_ELEMS": { "KEYS": [205] },
    "LOAD_CASE_NAMES": ["Comp(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "SolidStrainGlobal": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Node", "Strain-XX", "Strain-YY", "Strain-ZZ", "Strain-XY", "Strain-YZ", "Strain-XZ", "Strain-P1", "Strain-P2", "Strain-P3", "Max-Shear"],
    "DATA": [
      ["1", "205", "Comp", "nl_001", "1", "-1.526607997151e-07", "-1.869003906363e-07", "4.390947924304e-06", "-2.101840625867e-08", "6.652619107252e-07", "1.999020761608e-06", "5.215377841926e-06", "-1.701366927411e-07", "-9.938544152325e-07", "3.104616128579e-06"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取实体应变（全局） ───────────────────────────────
#   塑性应变：TABLE_TYPE="SOLID_GLOB_PLAST_STRAIN"
payload = {
    "Argument": {
        "TABLE_NAME": "SolidStrainGlobal",
        "TABLE_TYPE": "SOLID_GLOB_TOTAL_STRAIN",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [205]},
        "LOAD_CASE_NAMES": ["Comp(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SolidStrainGlobal", {})
print(f"实体应变(全局) {len(table.get('DATA', []))} 行")
```

---

## 26. Elastic Link

> **功能：** 按节点提取弹性连接(Elastic Link)单元的构件内力（轴力·剪力·扭转·弯矩）。可选一般/最大值基准(by-max)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"ELASTICLINK"` | 弹性连接构件内力 |
| `"ELASTICLINKVBM"` | 弹性连接构件内力（最大值基准，View by Max Value） |

> ⚠️ 2026-08-26 确认（article id `36017416195737`）：`ELASTICLINKVBM` 专用参数
> `"ITEM_TO_DISPLAY"`（Array [String]，enum: `Axial`/`Shear-y`/`Shear-z`/`Torsion`/`Moment-y`/
> `Moment-z`，默认值 All，Optional）在先前版本文档中有所遗漏 — 该字段用于指定
> 计算最大值的对象分量。

### Response HEAD

- `ELASTICLINK`: `["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`
- `ELASTICLINKVBM`：在 `Node` 之后追加用于指示哪个分量产生最大值的 `Component` 列 — `["Index", "No.", "Load", "Node", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body — ELASTICLINK**

```json
{
  "Argument": {
    "TABLE_NAME": "ElasticLink",
    "TABLE_TYPE": "ELASTICLINK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
  }
}
```

**POST Response Body — ELASTICLINK**

```json
{
  "ElasticLink": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "SWofGirders", "1", "-2.163226913452", "0.262795234546", "7.112188879013", "-0.000000245586", "1.306126533508", "0.030306393385"]
    ]
  }
}
```

**POST Request Body — ELASTICLINKVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "ElasticLinkViewByMaxValueItems",
    "TABLE_TYPE": "ELASTICLINKVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Response Body — ELASTICLINKVBM(View by Max Value)**

```json
{
  "ElasticLinkViewByMaxValueItems": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "No.", "Load", "Node", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "STLENV_STR(max)", "1", "Axial", "8.761203247070", "16.289886962891", "45.691238769531", "0.000035891681", "8.390747558594", "6.234448486328"],
      ["2", "1", "STLENV_STR(max)", "1", "Shear-y", "8.761203247070", "16.289886962891", "45.691238769531", "0.000035891681", "8.390747558594", "6.234448486328"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取弹性连接构件内力 ────────────────────────────────────
#   最大值基准(by-max)：TABLE_TYPE="ELASTICLINKVBM"
payload = {
    "Argument": {
        "TABLE_NAME": "ElasticLink",
        "TABLE_TYPE": "ELASTICLINK",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("ElasticLink", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Link {d['No.']}: Axial={d['Axial']}, Shear-z={d['Shear-z']}")
```

---

## 27. General Link

> **功能：** 提取一般连接(General Link)单元的构件内力（轴力·剪力·扭转·弯矩）或变形(Deform)。构件内力可选一般/最大值基准(by-max)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"GENERAL_LINK_FORCE"` | 一般连接构件内力 |
| `"GENERAL_LINK_FORCEVBM"` | 一般连接构件内力（最大值基准，View by Max Value） |
| `"GENERAL_LINK_DEFORM"` | 一般连接变形（Deform） |

> ⚠️ 2026-08-26 确认（article id `36017500761369`）：`GENERAL_LINK_FORCEVBM` 专用参数
> `"ITEM_TO_DISPLAY"`（Array [String]，enum: `Axial`/`Shear-y`/`Shear-z`/`Torsion`/`Moment-y`/
> `Moment-z`，默认值 All，Optional）在先前版本文档中有所遗漏（与第26节 Elastic Link 同一
> 模式）。此外 `GENERAL_LINK_DEFORM` 具有与构件内力完全不同的响应结构（两端位移/转动），
> 而先前版本文档只标注了构件内力用的 Response HEAD，易被误认为 DEFORM 也是同一结构。

### Response HEAD

- `GENERAL_LINK_FORCE`: `["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`
- `GENERAL_LINK_FORCEVBM`：在 `Node` 之后追加 `Component` 列 — `["Index", "No.", "Load", "Node", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`
- `GENERAL_LINK_DEFORM`：结构完全不同 — 连接两端的位移(Dx/Dy/Dz)·转动(Rx/Ry/Rz)按 `Node` 区块循环出现 — `["Index", "No.", "Load", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"]`

### Request / Response JSON

**POST Request Body — GENERAL_LINK_FORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink",
    "TABLE_TYPE": "GENERAL_LINK_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
  }
}
```

**POST Response Body — GENERAL_LINK_FORCE**

```json
{
  "GeneralLink": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "No.", "Load", "Node", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "SWofGirders", "3536", "-24.885666367763", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"]
    ]
  }
}
```

**POST Request Body — GENERAL_LINK_FORCEVBM(View by Max Value)**

```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink-Force-ViewByMaxValueItems",
    "TABLE_TYPE": "GENERAL_LINK_FORCEVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "NODE_ELEMS": { "KEYS": [2] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Request Body — GENERAL_LINK_DEFORM**

```json
{
  "Argument": {
    "TABLE_NAME": "GeneralLink-Deformation",
    "TABLE_TYPE": "GENERAL_LINK_DEFORM",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["No.", "Load", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
  }
}
```

**POST Response Body — GENERAL_LINK_DEFORM**

```json
{
  "GeneralLink-Deformation": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "No.", "Load", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "DATA": [
      ["1", "1", "SWofGirders", "3536", "-2.537631746597e-05", "1.256078938754e-04", "-1.455055139484e-01", "-4.829228297583e-07", "1.587459476372e-04", "-1.964780569004e-05", "1236", "-2.537631746597e-05", "1.256078938754e-04", "-1.455055139484e-01", "-4.829228297583e-07", "1.587459476372e-04", "-1.964780569004e-05"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取一般连接构件内力 ────────────────────────────────────
#   最大值基准(by-max)：TABLE_TYPE="GENERAL_LINK_FORCEVBM"
#   变形(Deform)：        TABLE_TYPE="GENERAL_LINK_DEFORM"
payload = {
    "Argument": {
        "TABLE_NAME": "GeneralLink",
        "TABLE_TYPE": "GENERAL_LINK_FORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SWofGirders(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("GeneralLink", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Link {d['No.']}: Axial={d['Axial']}")
```

---

## 28. Vibration Mode Shape

> **功能：** 按节点·按模态提取特征值分析(Eigenvalue)的振动模态形状或参与向量(Participation Vector)模态形状（平动 UX·UY·UZ，转动 RX·RY·RZ）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"EIGENVALUEMODE"` | 特征值(Eigenvalue)振动模态形状 |
| `"PARTICIPATIONVECTORMODE"` | 参与向量(Participation Vector)模态形状 |

### 专用参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 8 | 模态编号列表（`"Mode" + 编号`，例：`"Mode1"`） | `"MODES"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 确认（article id `36017669319321`）：`MODES` 参数与响应中的 `SUB_TABLES`
> 数组（模态分析汇总信息）在先前版本文档中均有遗漏。

### Response HEAD

主 `HEAD`/`DATA`：`["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]`

此外，响应最上层追加存放模态分析汇总信息的 `SUB_TABLES` 数组，
包含下列4类子表（各 `HEAD`/`DATA` 按模态编号各1行）：

| 子表键 | 内容 | HEAD |
|---|---|---|
| `EIGENVALUEANALYSIS` | 固有频率·周期 | `["ModeNo", "Frequency(rad/sec)", "Frequency(cycle/sec)", "Period(sec)", "Tolerance"]` |
| `MODALPARTICIPATIONMASSESPRINTOUT(1)` | 模态参与质量(%, 累计%) | `["ModeNo", "TRAN-XMASS(%)", "TRAN-XSUM(%)", "TRAN-YMASS(%)", "TRAN-YSUM(%)", "TRAN-ZMASS(%)", "TRAN-ZSUM(%)", "ROTN-XMASS(%)", "ROTN-XSUM(%)", "ROTN-YMASS(%)", "ROTN-YSUM(%)", "ROTN-ZMASS(%)", "ROTN-ZSUM(%)"]` |
| `MODALPARTICIPATIONMASSESPRINTOUT(2)` | 模态参与质量（绝对值、累计值） | 与上方同名列但去掉 `(%)` |
| `MODALPARTICIPATIONFACTORPRINTOUT(kN,m)` | 模态参与系数 | `["ModeNo", "TRAN-XValue", "TRAN-YValue", "TRAN-ZValue", "ROTN-XValue", "ROTN-YValue", "ROTN-ZValue"]` |
| `MODALDIRECTIONFACTORPRINTOUT` | 模态方向系数 | 与上方相同 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "EigenvalueMode",
    "TABLE_TYPE": "EIGENVALUEMODE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "MODES": ["Mode1", "Mode2"]
  }
}
```

**POST Response Body**

```json
{
  "EigenvalueMode": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "1", "3.837572718516e-02", "-2.976241858587e-07", "0.000000000000e+00", "2.380992695526e-07", "4.126895212051e-06", "-5.142371718861e-07"],
      ["2", "1", "2", "4.396886676826e-05", "7.802487500606e-04", "3.449011941636e-10", "-6.241987277788e-04", "-5.791213526283e-04", "1.761254899933e-03"]
    ],
    "SUB_TABLES": [
      {
        "EIGENVALUEANALYSIS": {
          "HEAD": ["ModeNo", "Frequency(rad/sec)", "Frequency(cycle/sec)", "Period(sec)", "Tolerance"],
          "DATA": [
            ["1.0000", "9.1608", "1.4580", "0.6859", "0.0000e+00"],
            ["2.0000", "9.8717", "1.5711", "0.6365", "0.0000e+00"]
          ]
        }
      },
      {
        "MODALPARTICIPATIONMASSESPRINTOUT(1)": {
          "HEAD": ["ModeNo", "TRAN-XMASS(%)", "TRAN-XSUM(%)", "TRAN-YMASS(%)", "TRAN-YSUM(%)", "TRAN-ZMASS(%)", "TRAN-ZSUM(%)", "ROTN-XMASS(%)", "ROTN-XSUM(%)", "ROTN-YMASS(%)", "ROTN-YSUM(%)", "ROTN-ZMASS(%)", "ROTN-ZSUM(%)"],
          "DATA": [
            ["1.0000", "91.64", "91.64", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.01", "0.01", "0.00", "0.00"]
          ]
        }
      },
      {
        "MODALPARTICIPATIONMASSESPRINTOUT(2)": {
          "HEAD": ["ModeNo", "TRAN-XMASS", "TRAN-XSUM", "TRAN-YMASS", "TRAN-YSUM", "TRAN-ZMASS", "TRAN-ZSUM", "ROTN-XMASS", "ROTN-XSUM", "ROTN-YMASS", "ROTN-YSUM", "ROTN-ZMASS", "ROTN-ZSUM"],
          "DATA": [
            ["1.0000", "724.1700", "724.1700", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "148.1200", "148.1200", "0.00", "0.00"]
          ]
        }
      },
      {
        "MODALPARTICIPATIONFACTORPRINTOUT(kN,m)": {
          "HEAD": ["ModeNo", "TRAN-XValue", "TRAN-YValue", "TRAN-ZValue", "ROTN-XValue", "ROTN-YValue", "ROTN-ZValue"],
          "DATA": [
            ["1.0000", "26.91", "-0.01", "0.06", "0.00", "0.18", "0.00"]
          ]
        }
      },
      {
        "MODALDIRECTIONFACTORPRINTOUT": {
          "HEAD": ["ModeNo", "TRAN-XValue", "TRAN-YValue", "TRAN-ZValue", "ROTN-XValue", "ROTN-YValue", "ROTN-ZValue"],
          "DATA": [
            ["1.0000", "99.98", "0.00", "0.00", "0.00", "0.01", "0.00"]
          ]
        }
      }
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取振动模态形状 ───────────────────────────────────────
#   参与向量：TABLE_TYPE="PARTICIPATIONVECTORMODE"
payload = {
    "Argument": {
        "TABLE_NAME": "VibrationMode",
        "TABLE_TYPE": "EIGENVALUEMODE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("VibrationMode", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Node {d['Node']} Mode {d['Mode']}: UX={d['UX']}")
```

---

## 29. Buckling Mode Shape

> **功能：** 按节点·按模态提取屈曲分析(Buckling)的模态形状（平动 UX·UY·UZ，转动 RX·RY·RZ）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BUCKLINGMODE"` | 屈曲(Buckling)模态形状 |

### 专用参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 8 | 模态编号列表（`"Mode" + 编号`，例：`"Mode1"`） | `"MODES"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 确认（article id `36017712087065`）：`MODES` 参数与响应中的 `SUB_TABLES`
> （`BUCKLINGANALYSIS` — 各模态屈曲系数(Eigenvalue)·Tolerance）在先前版本文档中
> 有所遗漏（与第28节 Vibration Mode Shape 同一模式）。

### Response HEAD

主 `HEAD`/`DATA`：`["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"]`

此外响应最上层追加 `SUB_TABLES` 数组，包含 `BUCKLINGANALYSIS` 子表
（`HEAD`: `["Mode", "Eigenvalue", "Tolerance"]`，按模态编号各1行）。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BucklingMode",
    "TABLE_TYPE": "BUCKLINGMODE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 12 },
    "COMPONENTS": ["Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "MODES": ["Mode1", "Mode2"]
  }
}
```

**POST Response Body**

```json
{
  "BucklingMode": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Mode", "UX", "UY", "UZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "1", "-3.068406433733e-05", "1.071752325513e-10", "-2.756625224655e-08", "0.000000000000e+00", "2.040060468720e-08", "1.430189905494e-10"],
      ["2", "1", "2", "8.776101828229e-08", "0.000000000000e+00", "-1.232408164286e-08", "0.000000000000e+00", "4.962889338148e-08", "0.000000000000e+00"]
    ],
    "SUB_TABLES": [
      {
        "BUCKLINGANALYSIS": {
          "HEAD": ["Mode", "Eigenvalue", "Tolerance"],
          "DATA": [
            ["1", "2.909991059676e+03", "0.0000e+00"],
            ["2", "3.056712238985e+03", "0.0000e+00"]
          ]
        }
      }
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取屈曲模态形状 ───────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BucklingMode",
        "TABLE_TYPE": "BUCKLINGMODE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [1]}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BucklingMode", {})
print(f"屈曲模态形状 {len(table.get('DATA', []))} 行")
```

---

## 30. Tendon Coordinates

> **功能：** 按预应力束·按区段(No)提取预应力束(Tendon)的线形坐标（x·y·z）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_COORDINATES"` | 预应力束坐标 |

### Response HEAD

`["Index", "TendonName", "No", "x", "y", "z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonCoordinates",
    "TABLE_TYPE": "TNDN_COORDINATES",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "No", "x", "y", "z"]
  }
}
```

**POST Response Body**

```json
{
  "TendonCoordinates": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "No", "x", "y", "z"],
    "DATA": [
      ["1", "Bot-Key-A01", "0", "139.500000000000", "0.000000000000", "0.000000000000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束坐标 ───────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonCoordinates",
        "TABLE_TYPE": "TNDN_COORDINATES",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonCoordinates", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['TendonName']} #{d['No']}: ({d['x']}, {d['y']}, {d['z']})")
```

---

## 31. Tendon Elongation

> **功能：** 按施工阶段(Stage)·步骤(Step)提取预应力束(Tendon)的伸长量(Elongation)。将预应力束自身伸长·单元伸长·合计区分为起始端(Begin)/终止端(End)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_ELONGATION"` | 预应力束伸长量 |

### Response HEAD

`["Index", "TendonName", "Stage", "Step", "TendonElongation/Begin", "TendonElongation/End", "ElementElongation/Begin", "ElementElongation/End", "Summation/Begin", "Summation/End"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonElongation",
    "TABLE_TYPE": "TNDN_ELONGATION",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "Stage", "Step", "TendonElongation/Begin", "TendonElongation/End", "ElementElongation/Begin", "ElementElongation/End", "Summation/Begin", "Summation/End"]
  }
}
```

**POST Response Body**

```json
{
  "TendonElongation": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "Stage", "Step", "TendonElongation/Begin", "TendonElongation/End", "ElementElongation/Begin", "ElementElongation/End", "Summation/Begin", "Summation/End"],
    "DATA": [
      ["1", "Bot-Key-A01", "CS16", "001(first)", "0.127805425338", "0.000000000000", "0.000217812956", "0.000000000000", "0.128023238294", "0.000000000000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束伸长量 ─────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonElongation",
        "TABLE_TYPE": "TNDN_ELONGATION",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonElongation", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['TendonName']} ({d['Stage']}): 合计={d['Summation/Begin']}")
```

---

## 32. Tendon Arrangement

> **功能：** 按单元·位置(Part)·预应力束编号提取预应力束(Tendon)在单元内的布置信息（截面位置 Yp·Zp、平均方向 sin/cos、平均应力·平均力）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_ARRANGEMENT"` | 预应力束布置 |

### ADDITIONAL — 预应力束组·施工阶段指定（2026-08-26 官方已反映）

本表**不使用**通用事项中的 `NODE_ELEMS`，而改用下方 `ADDITIONAL` 对象
指定预应力束组与施工阶段（两者均为 Required）。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 7 | 预应力束组·施工阶段指定 | `"ADDITIONAL"` | Object | — | **Required** |
| 7-1 | └ 预应力束组·施工阶段设置 | `ADDITIONAL.SET_TENDON_PARAMS` | Object | — | **Required** |
| 7-1-1 | 　└ 预应力束组名称 | `SET_TENDON_PARAMS.TENDON_GROUP` | String | — | **Required** |
| 7-1-2 | 　└ 施工阶段名称 | `SET_TENDON_PARAMS.STAGE` | String | — | **Required** |

> ⚠️ 2026-08-26 确认（article id `36018062664857`）：先前版本文档误记为本表同样使用通用
> `NODE_ELEMS`（指定单元），但官方 schema 中根本没有 `NODE_ELEMS`，而是以
> `ADDITIONAL.SET_TENDON_PARAMS`（预应力束组名 + 施工阶段名，两者均为 Required）指定对象
> — 用先前的示例无法选取到实际数据。

### Response HEAD

`["Index", "Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonArrangement(TendonGroup)",
    "TABLE_TYPE": "TNDN_ARRANGEMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"],
    "ADDITIONAL": {
      "SET_TENDON_PARAMS": {
        "TENDON_GROUP": "Top-P2-A",
        "STAGE": "CS2"
      }
    }
  }
}
```

**POST Response Body**

```json
{
  "TendonArrangement(TendonGroup)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Part", "TendonNumber", "Yp", "Zp", "AverageSinθ", "AverageCosθ", "AverageStress", "AverageForce"],
    "DATA": [
      ["1", "50", "I", "0", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"],
      ["2", "50", "J", "0", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束布置（指定预应力束组 + 施工阶段） ────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonArrangement(TendonGroup)",
        "TABLE_TYPE": "TNDN_ARRANGEMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "ADDITIONAL": {
            "SET_TENDON_PARAMS": {"TENDON_GROUP": "Top-P2-A", "STAGE": "CS2"}
        }
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonArrangement(TendonGroup)", {})
print(f"预应力束布置 {len(table.get('DATA', []))} 行")
```

---

## 33. Tendon Loss

> **功能：** 按单元·位置(Part)提取预应力束(Tendon)的损失(Loss)。包含即时损失后应力、弹性变形损失、徐变/干燥收缩损失、松弛损失、总损失后/即时损失后应力比、有效根数。可选择按构件内力(Force)/应力(Stress)基准。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_LOSS_FORCE"` | 预应力束损失（按构件内力 Force 基准） |
| `"TNDN_LOSS_STRESS"` | 预应力束损失（按应力 Stress 基准） |

### ADDITIONAL — 预应力束组·施工阶段指定（2026-08-26 官方已反映）

本表**不支持**通用事项中的 `NODE_ELEMS`/`LOAD_CASE_NAMES`/`OPT_CS`/`STAGE_STEP`，
而改用与第32节（Tendon Arrangement）相同的 `ADDITIONAL.SET_TENDON_PARAMS`（预应力束组名 + 施工阶段名，
两者均为 Required）指定对象。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 7 | 预应力束组·施工阶段指定 | `"ADDITIONAL"` | Object | — | **Required** |
| 7-1 | └ 预应力束组·施工阶段设置 | `ADDITIONAL.SET_TENDON_PARAMS` | Object | — | **Required** |
| 7-1-1 | 　└ 预应力束组名称 | `SET_TENDON_PARAMS.TENDON_GROUP` | String | — | **Required** |
| 7-1-2 | 　└ 施工阶段名称 | `SET_TENDON_PARAMS.STAGE` | String | — | **Required** |

> ⚠️ 2026-08-26 确认（article id `36018150905881`）：先前版本文档用 `NODE_ELEMS` 指定对象，
> 但该字段并不存在于官方 schema，实际需要的是 `ADDITIONAL.SET_TENDON_PARAMS`。

### Response HEAD

- `TNDN_LOSS_STRESS`: `["Index", "Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."]`
- `TNDN_LOSS_FORCE`: 不用 `Stress(...)`，改用 `Force(...)` 列名 — `["Index", "Elem", "Part", "Force(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Force(AfterAllLoss)/Force(AfterImmediateLoss)", "EffectiveNum."]`

### Request / Response JSON

**POST Request Body — TNDN_LOSS_STRESS**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonLoss(Stress)",
    "TABLE_TYPE": "TNDN_LOSS_STRESS",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."],
    "ADDITIONAL": {
      "SET_TENDON_PARAMS": { "TENDON_GROUP": "Bot-Key-B", "STAGE": "CS16" }
    }
  }
}
```

**POST Response Body — TNDN_LOSS_STRESS**

```json
{
  "TendonLoss(Stress)": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Part", "Stress(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Stress(AfterAllLoss)/Stress(AfterImmediateLoss)", "EffectiveNum."],
    "DATA": [
      ["1", "33", "I", "1029.576204812610", "1.193871724644", "1.001159575871", "-68.776503747849", "-44.450510039386", "0.891185187130", "2.000000000000"],
      ["2", "33", "J", "1135.213914944730", "0.738061054845", "1.000650151522", "-64.974951541191", "-49.011270158760", "0.900240686663", "2.000000000000"]
    ]
  }
}
```

**POST Request Body — TNDN_LOSS_FORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonLoss(Force)",
    "TABLE_TYPE": "TNDN_LOSS_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "Force(AfterImmediateLoss):A", "ElasticDeform.Loss:B", "Ratio/A", "Creep/ShrinkageLoss", "RelaxationLoss", "Force(AfterAllLoss)/Force(AfterImmediateLoss)", "EffectiveNum."],
    "ADDITIONAL": {
      "SET_TENDON_PARAMS": { "TENDON_GROUP": "Bot-Key-B", "STAGE": "CS16" }
    }
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束损失（按应力基准） ───────────────────────────────
#   按构件内力基准：TABLE_TYPE="TNDN_LOSS_FORCE"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonLoss(Stress)",
        "TABLE_TYPE": "TNDN_LOSS_STRESS",
        "UNIT": {"FORCE": "N", "DIST": "mm"},
        "ADDITIONAL": {
            "SET_TENDON_PARAMS": {"TENDON_GROUP": "Bot-Key-B", "STAGE": "CS16"}
        }
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonLoss(Stress)", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} ({d['Part']}): 松弛损失={d['RelaxationLoss']}")
```

---

## 34. Tendon Weight

> **功能：** 按组/按线形/按特性提取预应力束(Tendon)的工程量(Weight)。包含预应力束根数·截面积·长度·单位长度重量·重量·总重量。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_WEIGHT_PROFILE"` | 预应力束工程量（按线形 Profile） |
| `"TNDN_WEIGHT_PROPERTY"` | 预应力束工程量（按特性 Property） |
| `"TNDN_WEIGHT_GROUP"` | 预应力束工程量（按组 Group） |

> ⚠️ 2026-08-26 确认（article id `36018235852569`）：先前版本文档将 `TABLE_TYPE`
> 标注为 `"TNDN_WEIGHT_GROUP"`，但示例本身实际沿用着 `"TNDN_WEIGHT_PROFILE"`（按线形）
> 的响应数据（`TendonName`/`TendonNum` 列、`"Bot-Key-A01"` 等）—
> Group 响应的列构成完全不同。3种的响应结构各不相同，故在下方逐一更正并补充。

### Response HEAD

- `TNDN_WEIGHT_PROFILE`: `["Index", "TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"]`
- `TNDN_WEIGHT_PROPERTY`: `["Index", "TendonProperty", "Area", "TotalLength", "Weight/Length", "TotalWeight"]`
- `TNDN_WEIGHT_GROUP`: `["Index", "TendonGroup", "TotalLength", "TotalWeight"]`

### Request / Response JSON

**POST Request Body — TNDN_WEIGHT_PROFILE**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonProfile",
    "TABLE_TYPE": "TNDN_WEIGHT_PROFILE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"]
  }
}
```

**POST Response Body — TNDN_WEIGHT_PROFILE**

```json
{
  "TendonProfile": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonName", "TendonNum", "Area", "Length", "Weight/Length", "Weight", "TotalWeight"],
    "DATA": [
      ["1", "Bot-Key-A01", "1.000000000000", "0.002635300000", "21.048299083539", "0.202871198248", "4.270093656165", "4.270093656165"],
      ["2", "Bot-Key-A02", "1.000000000000", "0.002635300000", "21.035730337216", "0.202871198248", "4.267543819538", "4.267543819538"]
    ]
  }
}
```

**POST Request Body — TNDN_WEIGHT_PROPERTY**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonProperty",
    "TABLE_TYPE": "TNDN_WEIGHT_PROPERTY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonProperty", "Area", "TotalLength", "Weight/Length", "TotalWeight"]
  }
}
```

**POST Response Body — TNDN_WEIGHT_PROPERTY**

```json
{
  "TendonProperty": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonProperty", "Area", "TotalLength", "Weight/Length", "TotalWeight"],
    "DATA": [
      ["1", "Bot", "0.002635300000", "2073.687453151790", "0.202871198248", "420.691458413265"],
      ["2", "Top", "0.002635300000", "5553.015935350260", "0.202871198248", "1126.546996696130"],
      ["3", "SUM", "-", "7626.703388502000", "-", "1547.238455109000"]
    ]
  }
}
```

**POST Request Body — TNDN_WEIGHT_GROUP**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonGroup",
    "TABLE_TYPE": "TNDN_WEIGHT_GROUP",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["TendonGroup", "TotalLength", "TotalWeight"]
  }
}
```

**POST Response Body — TNDN_WEIGHT_GROUP**

```json
{
  "TendonGroup": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "TendonGroup", "TotalLength", "TotalWeight"],
    "DATA": [
      ["1", "Bot-Key-A", "446.379820137516", "90.557608985136"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束工程量（按线形） ──────────────────────────────────
#   按特性：TABLE_TYPE="TNDN_WEIGHT_PROPERTY"
#   按组：TABLE_TYPE="TNDN_WEIGHT_GROUP"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonProfile",
        "TABLE_TYPE": "TNDN_WEIGHT_PROFILE",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonProfile", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['TendonName']}: 总重量={d['TotalWeight']}")
```

---

## 35. Tendon Stress Limit Check

> **功能：** 提取预应力束(Tendon)的应力限值验算结果。将预应力束应力(f_p1·f_p2·f_pe)与锚固端/锚固端以外/正常使用极限状态应力限值进行比较。可用 `ADDITIONAL.REDUCTION_FACTOR` 直接指定各项应力限值所乘的折减系数。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_STRS_LIMIT_CHECK"` | 预应力束应力限值验算 |

### Response HEAD

`["Index", "Tendon", "Tendon Stress/f_p1", "Tendon Stress/f_p2", "Tendon Stress/f_pe", "Tendon Stress Limit/Immediately after anchor set/At anch.", "Tendon Stress Limit/Immediately after anchor set/Away from anch.", "Tendon Stress Limit/At service"]`

### `ADDITIONAL.REDUCTION_FACTOR`（Optional）

对锚固瞬间(anchor set)／正常使用极限状态(service)应力限值相乘的折减系数。省略时使用默认值。

| Key | 说明 | Value Type | Default |
|-----|------|-----------|---------|
| `"AT_ANCH"` | 锚固端(anchorage)应力限值折减系数 （仅后张法） | Number | 0.7 |
| `"AWAY_FROM_ANCH"` | 锚固端以外(away from anchorages)应力限值折减系数 （仅后张法） | Number | 0.74 |
| `"AT_SERVICE"` | 正常使用极限状态(service)应力限值折减系数 | Number | 0.8 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonStressLimitCheck",
    "TABLE_TYPE": "TNDN_STRS_LIMIT_CHECK",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Tendon", "TendonStress/f_p1", "TendonStress/f_p2", "TendonStress/f_pe", "TendonStressLimit/Atanch.", "TendonStressLimit/Awayfromanch.", "TendonStressLimit/Atservice"],
    "ADDITIONAL": {
      "REDUCTION_FACTOR": { "AT_ANCH": 1, "AWAY_FROM_ANCH": 1, "AT_SERVICE": 1 }
    }
  }
}
```

**POST Response Body**

```json
{
  "TendonStressLimitCheck": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Tendon", "Tendon Stress/f_p1", "Tendon Stress/f_p2", "Tendon Stress/f_pe", "Tendon Stress Limit/Immediately after anchor set/At anch.", "Tendon Stress Limit/Immediately after anchor set/Away from anch.", "Tendon Stress Limit/At service"],
    "DATA": [
      ["1", "A1L", "1094382.612985240063", "1209052.195195989916", "1037017.037908399943", "1900000.000000000000", "1900000.000000000000", "1600000.000000000000"]
    ]
  }
}
```

> ⚠️ 响应根键已由 `TendonStressLimit` 变更为 **`TendonStressLimitCheck`**（已反映 2026-07 官方手册更新）。

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束应力限值验算 ─────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TendonStressLimitCheck",
        "TABLE_TYPE": "TNDN_STRS_LIMIT_CHECK",
        "UNIT": {"FORCE": "kN", "DIST": "m"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonStressLimitCheck", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['Tendon']}: f_pe={d['Tendon Stress/f_pe']} / 限值(service)={d['Tendon Stress Limit/At service']}")
```

---

## 36. Tendon Approximate Loss

> **功能：** 按单元·位置(Part)提取预应力束(Tendon)的近似损失(Approximate Loss)。包含即时损失、徐变/干燥收缩/松弛损失、总损失以及即时/总损失后的应力与应力比。可选择按构件内力(Force)/应力(Stress)基准。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TNDN_APPROX_LOSS_FORCE"` | 预应力束近似损失（按构件内力 Force 基准） |
| `"TNDN_APPROX_LOSS_STRESS"` | 预应力束近似损失（按应力 Stress 基准） |

> ⚠️ 2026-08-26 确认（article id `36018411935129`）：本表**不支持**通用事项中的 `NODE_ELEMS`
> （官方 schema 中仅存在 `TABLE_NAME`/`TABLE_TYPE`/`EXPORT_PATH`/`UNIT`/`STYLES`/
> `COMPONENTS`）— 先前版本文档中误为包含。不设对象限制，返回的
> 是全部预应力束单元。

### Response HEAD

- `TNDN_APPROX_LOSS_STRESS`: `["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"]`
- `TNDN_APPROX_LOSS_FORCE`: 不用 `Stress(...)`，改用 `Force(...)` 列名 — `["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Force(ImmediateLoss)", "Force(AllLoss)", "Force(AllLoss)/Force"]`

### Request / Response JSON

**POST Request Body — TNDN_APPROX_LOSS_STRESS**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonApproximateLoss(Stress)",
    "TABLE_TYPE": "TNDN_APPROX_LOSS_STRESS",
    "UNIT": { "FORCE": "kips", "DIST": "in" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"]
  }
}
```

**POST Response Body — TNDN_APPROX_LOSS_STRESS**

```json
{
  "TendonApproximateLoss(Stress)": {
    "FORCE": "kips",
    "DIST": "in",
    "HEAD": ["Index", "Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Stress(ImmediateLoss)", "Stress(AllLoss)", "Stress(AllLoss)/Stress"],
    "DATA": [
      ["1", "1", "I", "-6.424509690435", "-8.904593184079", "-9.582009033589", "-2.465640773855", "-27.376752681958", "196.075490309565", "175.123247318042", "0.893141957934"]
    ]
  }
}
```

**POST Request Body — TNDN_APPROX_LOSS_FORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "TendonApproximateLoss(Force)",
    "TABLE_TYPE": "TNDN_APPROX_LOSS_FORCE",
    "UNIT": { "FORCE": "kips", "DIST": "in" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Part", "ImmediateLoss", "CreepLoss", "ShrinkageLoss", "RelaxationLoss", "AllLoss", "Force(ImmediateLoss)", "Force(AllLoss)", "Force(AllLoss)/Force"]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取预应力束近似损失（按应力基准） ──────────────────────────
#   按构件内力基准：TABLE_TYPE="TNDN_APPROX_LOSS_FORCE"
payload = {
    "Argument": {
        "TABLE_NAME": "TendonApproximateLoss(Stress)",
        "TABLE_TYPE": "TNDN_APPROX_LOSS_STRESS",
        "UNIT": {"FORCE": "kips", "DIST": "in"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TendonApproximateLoss(Stress)", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} ({d['Part']}): 总损失={d['AllLoss']}")
```

---

## 37. Composite Section for C.S. (Force and Stress)

> **功能：** 按截面部件(SectionPart)·构件位置(Part)提取施工阶段组合截面（Composite Section for Construction Stage）的构件内力/应力。包含轴力·弯矩-y·弯矩-z，可选择按构件内力/应力基准。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"COMPSECTBEAMFORCE"` | 施工阶段组合截面构件内力（Beam Force） |
| `"COMPSECTBEAMSTRESS"` | 施工阶段组合截面应力（Beam Stress） |

> ⚠️ 2026-08-26 确认（article id `36018521410457`）：本表支持构件位置指定参数
> `"PARTS"`（Array [String]，取值：`"PartI"`/`"Part1/4"`/`"Part2/4"`/`"Part3/4"`/`"PartJ"`，默认值
> All，Optional — 与第19章第8~12节的 PARTS 同一模式）。先前版本文档中
> 有所遗漏。

### Response HEAD

`["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CompSectForce",
    "TABLE_TYPE": "COMPSECTBEAMFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DL(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS1:001(first)"],
    "PARTS": ["PartI", "PartJ"]
  }
}
```

**POST Response Body**

```json
{
  "CompSectForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "DL", "1", "I", "-0.000471429623", "-0.000083949590", "-0.077218286415"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取施工阶段组合截面构件内力 ────────────────────────────
#   按应力基准：TABLE_TYPE="COMPSECTBEAMSTRESS"
payload = {
    "Argument": {
        "TABLE_NAME": "CompSectForce",
        "TABLE_TYPE": "COMPSECTBEAMFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DL(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["CS1:001(first)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CompSectForce", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 截面{d['SectionPart']}: Moment-z={d['Moment-z']}")
```

---

## 38. Composite Section for C.S. (Self-Constraint Force and Stress)

> **功能：** 按截面部件(SectionPart)·构件位置(Part)提取施工阶段组合截面的自约束(Self-Constraint)构件内力/应力。包含温度梯度(TG)等自平衡荷载下的轴力·弯矩-y·弯矩-z，可选择按构件内力/应力基准。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SELF_CONST_BEAM_FORCE"` | 组合截面自约束构件内力（Self-Constraint Beam Force） |
| `"SELF_CONST_BEAM_STRESS"` | 组合截面自约束应力（Self-Constraint Beam Stress） |

> ⚠️ 2026-08-26 确认（article id `36018582743705`）：本表支持构件位置指定参数
> `"PARTS"`（Array [String]，取值：`"PartI"`/`"Part1/4"`/`"Part2/4"`/`"Part3/4"`/`"PartJ"`，默认值
> All，Optional）（与第37节相同）。先前版本文档中有所遗漏。

### Response HEAD

- General/Post CS: `["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`
- 施工阶段（Construction Stage，`COMPONENTS` 中包含 `Stage`/`Step` 时）：在 `Load` 之后追加 `Stage`/`Step` — `["Index", "Elem", "Load", "Stage", "Step", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"]`

> ⚠️ 2026-08-26 确认：查询施工阶段时会追加 `Stage`/`Step` 列，此点在先前版本文档中
> 有所遗漏（因第37节的官方示例不含该列，故第37节本身不作更正 — 判断为原文
> article 之间的标注差异，属错误上报对象）。

### Request / Response JSON

**POST Request Body — General/Post CS**

```json
{
  "Argument": {
    "TABLE_NAME": "SelfConstForce",
    "TABLE_TYPE": "SELF_CONST_BEAM_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["TG(+)(CS)"],
    "PARTS": ["PartI", "PartJ"]
  }
}
```

**POST Response Body — General/Post CS**

```json
{
  "SelfConstForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1", "TG(+)", "1", "I", "326.337945299092", "-691.230653270694", "0.000000000000"]
    ]
  }
}
```

**POST Request Body — 施工阶段（Construction Stage）**

```json
{
  "Argument": {
    "TABLE_NAME": "Self-ConstraintBeamForce",
    "TABLE_TYPE": "SELF_CONST_BEAM_FORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Stage", "Step", "SectionPart", "Part", "Axial", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "PARTS": ["PartI", "PartJ"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS4:001(first)", "CS4:002(last)"]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取施工阶段组合截面自约束构件内力 ───────────────────
#   按应力基准：TABLE_TYPE="SELF_CONST_BEAM_STRESS"
payload = {
    "Argument": {
        "TABLE_NAME": "SelfConstForce",
        "TABLE_TYPE": "SELF_CONST_BEAM_FORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["TG(+)(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["CS1:001(first)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("SelfConstForce", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 截面{d['SectionPart']}: Axial={d['Axial']}, Moment-y={d['Moment-y']}")
```

---

## 39. Wall Force

> **功能：** 按楼层(Story)·标高(top/bot)提取墙(Wall)单元的构件内力/弯矩。与一般 Plate Force 不同，可用 `STORY_NAMES` 指定楼层，且响应中同时给出上/下端(Part: `top`/`bot`)的取值。
>
> ℹ️ **2026-07-22 新增已反映：** 本项为本次在官方手册中确认到的内容，先前版本文档中有所遗漏。

### `TABLE_TYPE`

| 值 | 说明 |
| --- | --- |
| `"WALL_FORCE_MOMENT"` | 墙单元构件内力/弯矩（按楼层·上下端） |

### Response HEAD

`["Index", "Story", "Level", "Wall", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

> HEAD 中 `Part`·`Axial`·... 列重复两次，分别表示上端(`top`)·下端(`bot`)的取值。

### 专用参数

除通用参数（`TABLE_NAME`/`TABLE_TYPE`/`EXPORT_PATH`/`UNIT`/`STYLES`/`COMPONENTS`/`NODE_ELEMS`/`LOAD_CASE_NAMES`）外，还额外支持下列项。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 指定楼层名称 | `"STORY_NAMES"` | Array [String] | All | Optional |

> ℹ️ **2026-07-30 官方确认：** 先前版本文档把仅出现在 JSON Schema 中的 `SECT_POSITION`·`PARTS` 连同推测说明一并写入，但经官方负责人确认，该 Table Type(`WALL_FORCE_MOMENT`) 不支持这两项，官方 article 中亦已删除（Jira MAPI-2012）。据此已从上方表中移除。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "WALL_FORCE_MOMENT",
    "TABLE_TYPE": "WALL_FORCE_MOMENT",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "NODE_ELEMS": { "KEYS": [1, 2, 3] },
    "LOAD_CASE_NAMES": ["gLCB6(CB)"],
    "STORY_NAMES": ["1F"],
    "COMPONENTS": ["Story", "Level", "Wall", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Response Body**

```json
{
  "WALL_FORCE_MOMENT": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Story", "Level", "Wall", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "1F", "0.000", "1", "gLCB6", "top", "-8546.789", "0.000", "-57.818", "0.000", "114.403", "0.000", "bot", "-8750.140", "0.000", "-57.818", "0.000", "-174.688", "0.000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取墙单元构件内力（按楼层） ───────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "WALL_FORCE_MOMENT",
        "TABLE_TYPE": "WALL_FORCE_MOMENT",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [1, 2, 3]},
        "LOAD_CASE_NAMES": ["gLCB6(CB)"],
        "STORY_NAMES": ["1F"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("WALL_FORCE_MOMENT", {})

# 注意：本表 HEAD 中 Part·Axial·… 列以 top/bot 重复两次，
# 若如其他节那样用 dict(zip(head, row)) 包裹，bot 值会覆盖 top 值。
# 按位置索引将上、下端分开读取。
for row in table.get("DATA", []):
    story, wall, load = row[1], row[3], row[4]
    top = row[5:12]    # Part, Axial, Shear-y, Shear-z, Torsion, Moment-y, Moment-z
    bot = row[12:19]   # 顺序相同的下端值
    print(f"  Wall {wall} ({story}, {load}): Axial top={top[1]} / bot={bot[1]}")
```

---

## End-to-End Workflow

以下为执行分析后依次批量提取板应力·实体应力·连接构件内力·振动模态形状·预应力束损失的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_result(table_type, name, load_cases=None, extra=None):
    """提取分析结果表的通用函数"""
    arg = {
        "TABLE_NAME": name,
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6}
    }
    if load_cases:
        arg["LOAD_CASE_NAMES"] = load_cases
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    return resp.json().get(name, {})

# ── STEP 1：板应力（全局） ─────────────────────────────────────────
ps = get_result("PLATESTRESSG", "PlateStress", ["DL(ST)"],
                extra={"NODE_ELEMS": {"KEYS": [592]}})
print(f"STEP1 板应力 {len(ps.get('DATA', []))} 行")

# ── STEP 2：实体应力（全局） ─────────────────────────────────────
ss = get_result("SOLIDSG", "SolidStress", ["DL(ST)"],
                extra={"NODE_ELEMS": {"KEYS": [3381]}})
print(f"STEP2 实体应力 {len(ss.get('DATA', []))} 行")

# ── STEP 3：弹性连接构件内力 ───────────────────────────────────────
lf = get_result("ELASTICLINK", "ElasticLink", ["SWofGirders(ST)"])
print(f"STEP3 连接构件内力 {len(lf.get('DATA', []))} 行")

# ── STEP 4：振动模态形状（无需荷载工况） ──────────────────────
vm = get_result("EIGENVALUEMODE", "VibMode",
                extra={"STYLES": {"FORMAT": "Scientific", "PLACE": 12},
                       "NODE_ELEMS": {"KEYS": [1]}})
print(f"STEP4 振动模态形状 {len(vm.get('DATA', []))} 行")

# ── STEP 5：预应力束损失（按应力基准） ──────────────────────────────────
tl = get_result("TNDN_LOSS_STRESS", "TendonLoss",
                extra={"NODE_ELEMS": {"KEYS": [33]}})
print(f"STEP5 预应力束损失 {len(tl.get('DATA', []))} 行")
```
