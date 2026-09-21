# 17. DB – Bridge Specialization Results

> **适用产品：** MIDAS Civil NX (桥梁特化)  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **认证头：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../17_DB_Bridge.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分介绍桥梁特化结果设置，包括主梁图(Girder Diagram)定义·图像 Generation、预拱度控制(General / FCM Camber)、拉索未知荷载系数约束(Unknown Load Factor Constraints)。

---

## Endpoint 列表

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/GSBG`](#1-dbgsbg--bridge-girder-diagrams) | 桥梁主梁图 | POST, GET, PUT, DELETE |
| 2 | [`/db/GCMB`](#2-dbgcmb--general-camber-control) | 一般预拱度控制 | POST, GET, PUT, DELETE |
| 3 | [`/db/CAMB`](#3-dbcamb--fcm-camber-control) | FCM 预拱度控制 | POST, GET, PUT, DELETE |
| 4 | [`/db/ULFC`](#4-dbulfc--cable-control--unknown-load-factor-constraints) | 拉索控制 – 未知荷载系数约束 | POST, GET, PUT, DELETE |
| 5 | [`/ope/GSBG`](#5-opegsbg--bridge-girder-diagram-image-generation) | 桥梁主梁图图像 Generation | POST |

---

## 1. `/db/GSBG` — Bridge Girder Diagrams

> **功能：** 定义桥梁主梁(Bridge Girder)单元组的结果图(梁应力或梁构件内力/弯矩)。依结果类型指定应力分量(`BSTRSCOMP`)或构件内力分量(`MOMENT_COMP`)。

### Input URI

```
{base url}/db/GSBG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "GSBG": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name", "type": "string" },
      "BATCH": { "description": "Is Batch Boolean", "type": "boolean" },
      "BODY_ELEM_GRUP_K": { "description": "Body Element Group_K", "type": "integer" },
      "ALLSTAGE": { "description": "Is All Stage Boolean", "type": "boolean" },
      "BSTRSCOMP": { "description": "TODO: BSTRSCOMP", "type": "integer" },
      "BSTRSCOMP_SUB": { "description": "TODO: BSTRSCOMP_SUB", "type": "integer" },
      "MOMENT_COMP": { "description": "TODO: MOMENT_COMP", "type": "integer" },
      "_7TH_DOF_TYPE": { "description": "TODO: 7TH_DOF_TYPE", "type": "integer" },
      "DGRM_TYPE": { "description": "TODO: DGRM_TYPE", "type": "integer" },
      "SCALEFACTOR": { "description": "Scale", "type": "number" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 组名称 | `"NAME"` | String | — | **Required** |
| 2 | 批量处理(Batch) | `"BATCH"` | Boolean | `true` | **Required** |
| 3 | 桥梁主梁单元组 | `"BODY_ELEM_GRUP_K"` | Integer | — | **Required** |
| 4 | 生成选项 · 当前阶段-步骤: `false` / 全部阶段(最后一步): `true` | `"ALLSTAGE"` | Boolean | `false` | Optional |
| 5 | 结果类型 · 梁应力: `0` / 梁构件内力·弯矩: `1` | `"DGRM_TYPE"` | Integer | `0` | Optional |
| 6 | (应力时) 梁应力分量 · Sax: `0` / +Sby: `1` / −Sby: `2` / +Sbz: `3` / −Sbz: `4` / Combined: `5` / 7th DOF: `6` | `"BSTRSCOMP"` | Integer | `0` | Optional |
| 7 | (应力·7th DOF 时) 应力显示位置 · Maximum: `0` / 1(−y,+z): `1` / 2(+y,+z): `2` / 3(+y,−z): `3` / 4(−y,−z): `4` | `"BSTRSCOMP_SUB"` | Integer | `0` | Optional |
| 8 | (应力·7th DOF 时) 7th DOF 类型 · Sax(Warping): `0` / Ssy(Mt): `1` / Ssy(Mw): `2` / Ssz(Mt): `3` / Ssz(Mw): `4` / Combined(Ssy): `5` / Combined(Ssz): `6` | `"_7TH_DOF_TYPE"` | Integer | `0` | Optional |
| 9 | (构件内力时) 梁构件内力·弯矩分量 · Fx: `0` / Fy: `1` / Fz: `2` / Mx: `3` / My: `4` / Mz: `5` / Mb: `6` / Mt: `7` / Mw: `8` | `"MOMENT_COMP"` | Integer | `0` | Optional |
| 10 | 缩放比例 | `"SCALEFACTOR"` | Number | `0` | Optional |

### Request / Response JSON

**POST / PUT Request Body — 梁应力(Beam Stresses)**

```json
{
  "Assign": {
    "1": {
      "NAME": "Dgrm Group1",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 1,
      "ALLSTAGE": false,
      "DGRM_TYPE": 0,
      "BSTRSCOMP": 6,
      "BSTRSCOMP_SUB": 3,
      "_7TH_DOF_TYPE": 0,
      "SCALEFACTOR": 1
    }
  }
}
```

**POST / PUT Request Body — 梁构件内力/弯矩(Beam Forces/Moments)**

```json
{
  "Assign": {
    "2": {
      "NAME": "Dgrm Group2",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 2,
      "ALLSTAGE": true,
      "DGRM_TYPE": 1,
      "MOMENT_COMP": 4,
      "SCALEFACTOR": 1
    }
  }
}
```

**GET Response Body**

```json
{
  "GSBG": {
    "1": {
      "NAME": "Dgrm Group1",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 1,
      "ALLSTAGE": false,
      "DGRM_TYPE": 0,
      "BSTRSCOMP": 6,
      "BSTRSCOMP_SUB": 3,
      "_7TH_DOF_TYPE": 0,
      "SCALEFACTOR": 1
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

# ── POST: 生成 2 种主梁图 (应力 / 构件内力) ─────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "Dgrm Group1",
            "BATCH": True,
            "BODY_ELEM_GRUP_K": 1,
            "ALLSTAGE": False,
            "DGRM_TYPE": 0,          # 梁应力
            "BSTRSCOMP": 6,          # 7th DOF
            "BSTRSCOMP_SUB": 3,      # 应力位置 3(+y,-z)
            "_7TH_DOF_TYPE": 0,      # Sax(Warping)
            "SCALEFACTOR": 1
        },
        "2": {
            "NAME": "Dgrm Group2",
            "BATCH": True,
            "BODY_ELEM_GRUP_K": 2,
            "ALLSTAGE": True,        # 全部阶段(最后一步)
            "DGRM_TYPE": 1,          # 梁构件内力/弯矩
            "MOMENT_COMP": 4,        # My
            "SCALEFACTOR": 1
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/GSBG", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询主梁图 ──────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/GSBG", headers=HEADERS)
for key, val in resp.json().get("GSBG", {}).items():
    dtype = "应力" if val["DGRM_TYPE"] == 0 else "构件内力"
    print(f"  [{key}] {val['NAME']} ({dtype})")
```

---

## 2. `/db/GCMB` — General Camber Control

> **功能：** 定义按施工阶段分组的预拱度(Camber)基准。为各结构组指定预拱度方向(±DX/±DY)，并提供将起点设为 0 的选项。

### Input URI

```
{base url}/db/GCMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "GCMB": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "bSTART_PT_ZERO": { "description": "StartPtZero", "type": "boolean" },
      "GCMB_BASE_ITEMS": {
        "description": "GcmbBaseItems",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "GRUP_NAME": { "description": "GroupName", "type": "string" },
            "DIRECTION": { "description": "Dir", "type": "string" }
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 起点设为 0 | `"bSTART_PT_ZERO"` | Boolean | `true` | Optional |
| 2 | 一般预拱度基准项数组 | `"GCMB_BASE_ITEMS"` | Array [Object] | — | **Required** |
| 2-1 | └ 结构组名称 | `GCMB_BASE_ITEMS[].GRUP_NAME` | String | — | **Required** |
| 2-2 | └ 方向 · `"+DX"` / `"-DX"` / `"+DY"` / `"-DY"` | `GCMB_BASE_ITEMS[].DIRECTION` | String | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "bSTART_PT_ZERO": true,
      "GCMB_BASE_ITEMS": [
        { "GRUP_NAME": "CS_0", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_1", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_2", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_3", "DIRECTION": "+DX" }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "GCMB": {
    "1": {
      "bSTART_PT_ZERO": true,
      "GCMB_BASE_ITEMS": [
        { "GRUP_NAME": "CS_0", "DIRECTION": "+DX" },
        { "GRUP_NAME": "CS_1", "DIRECTION": "+DX" }
      ]
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

# ── POST: 按施工阶段分组批量设置预拱度方向 ──────────────────────
stage_groups = [f"CS_{i}" for i in range(19)]   # CS_0 ~ CS_18
payload = {
    "Assign": {
        "1": {
            "bSTART_PT_ZERO": True,
            "GCMB_BASE_ITEMS": [
                {"GRUP_NAME": g, "DIRECTION": "+DX"} for g in stage_groups
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/GCMB", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询预拱度基准 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/GCMB", headers=HEADERS)
data = resp.json().get("GCMB", {})
for key, val in data.items():
    print(f"  [{key}] StartPtZero={val['bSTART_PT_ZERO']}, 项目数={len(val['GCMB_BASE_ITEMS'])}")
```

---

## 3. `/db/CAMB` — FCM Camber Control

> **功能：** 控制 FCM(Free Cantilever Method，悬臂施工法)桥梁的预拱度。指定主梁单元组、支点节点组、关键节段(Key Segment)单元组。

### Input URI

```
{base url}/db/CAMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "CAMB": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "BODY_GROUP_NAME": { "description": "BodyElementGroupName", "type": "string" },
      "SUPP_GROUP_NAME": { "description": "SupportNodeGroup_KName", "type": "string" },
      "KEYSEG_GROUP_NAME": { "description": "KeySegGroupName", "type": "string" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 桥梁主梁单元组 | `"BODY_GROUP_NAME"` | String | — | **Required** |
| 2 | 支点节点组 | `"SUPP_GROUP_NAME"` | String | — | **Required** |
| 3 | 关键节段单元组 | `"KEYSEG_GROUP_NAME"` | String | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "BODY_GROUP_NAME": "FSM",
      "SUPP_GROUP_NAME": "PSC-BN",
      "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
    }
  }
}
```

**GET Response Body**

```json
{
  "CAMB": {
    "1": {
      "BODY_GROUP_NAME": "FSM",
      "SUPP_GROUP_NAME": "PSC-BN",
      "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
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

# ── POST: 设置 FCM 预拱度控制 ───────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "BODY_GROUP_NAME": "FSM",              # 主梁单元组
            "SUPP_GROUP_NAME": "PSC-BN",           # 支点节点组
            "KEYSEG_GROUP_NAME": "Key-SegK1~K5"    # 关键节段组
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/CAMB", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询 FCM 预拱度控制 ────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CAMB", headers=HEADERS)
print("GET:", resp.json())
```

---

## 4. `/db/ULFC` — Cable Control – Unknown Load Factor Constraints

> **功能：** 定义用于拉索桥未知荷载系数(Unknown Load Factor)分析的约束条件。针对反力·位移·桁架力·梁内力指定等式(Equality)或不等式(Inequality，上·下限)条件。

### Input URI

```
{base url}/db/ULFC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "ULFC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "ConstraintName", "type": "string" },
      "TYPE": { "description": "ConstraintType", "type": "string" },
      "OBJ_ID": { "description": "ObjectID", "type": "integer" },
      "POINT": { "description": "nPoint", "type": "integer" },
      "COMP": { "description": "Component", "type": "integer" },
      "EQ": { "description": "EqualityConditionBoolean", "type": "boolean" },
      "bVALUE": { "description": "ValueBoolean", "type": "boolean" },
      "VALUE": { "description": "ValueDouble", "type": "number" },
      "OtherObject": { "description": "OtherObject", "type": "integer" },
      "bUB": { "description": "UpperBoundBoolean", "type": "boolean" },
      "UB_VALUE": { "description": "UpperBoundValue", "type": "number" },
      "bLB": { "description": "LowerBoundBoolean", "type": "boolean" },
      "LB_VALUE": { "description": "LowerBoundValue", "type": "number" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 约束条件名称 | `"NAME"` | String | — | **Required** |
| 2 | 约束条件类型 · 反力: `"REAC"` / 位移: `"DISP"` / 桁架力: `"TRUSS"` / 梁内力: `"BEAM"` | `"TYPE"` | String | — | **Required** |
| 3 | 单元/节点 ID | `"OBJ_ID"` | Integer | — | **Required** |
| 4 | 位置(Point) · (`TYPE="BEAM"` 时) I端: `0` / 1/4: `1` / 2/4: `2` / 3/4: `3` / J端: `4` | `"POINT"` | Integer | — | **Required** |
| 5 | 分量(Component) · 反力·梁内力/位移/桁架基准 · FX/DX/I端: `0` / FY/DY/J端: `1` / FZ/DZ: `2` / MX/RX: `3` / MY/RY: `4` / MZ/RZ: `5` | `"COMP"` | Integer | — | **Required** |
| 6 | 等式/不等式条件 · 等式: `true` / 不等式: `false` | `"EQ"` | Boolean | `false` | Optional |
| **等式(Equality) 条件 (`EQ=true`)** |
| 7 | 检查值(Check Value) | `"bVALUE"` | Boolean | `false` | Optional |
| 8 | 数值(Value) | `"VALUE"` | Number | — | **Required** |
| 9 | 其他对象(`bVALUE=false` 时) | `"OtherObject"` | Integer | `0` | Optional |
| **不等式(Inequality) 条件 (`EQ=false`)** |
| 7 | 检查上限(Check Upper Bound) | `"bUB"` | Boolean | `false` | Optional |
| 8 | 上限值(Upper Bound Value) | `"UB_VALUE"` | Number | — | **Required** |
| 9 | 检查下限(Check Lower Bound) | `"bLB"` | Boolean | `false` | Optional |
| 10 | 下限值(Lower Bound Value) | `"LB_VALUE"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "2": {
      "NAME": "Ele-03",
      "TYPE": "BEAM",
      "OBJ_ID": 3,
      "POINT": 1,
      "COMP": 4,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -220,
      "bLB": true,
      "LB_VALUE": -230
    },
    "3": {
      "NAME": "Node-07",
      "TYPE": "REAC",
      "OBJ_ID": 7,
      "POINT": 4,
      "COMP": 1,
      "EQ": true,
      "bVALUE": true,
      "VALUE": 500,
      "OtherObject": 0
    },
    "4": {
      "NAME": "Ele-11",
      "TYPE": "DISP",
      "OBJ_ID": 11,
      "POINT": 4,
      "COMP": 2,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -0.05,
      "bLB": true,
      "LB_VALUE": 0.05
    },
    "7": {
      "NAME": "Node106",
      "TYPE": "DISP",
      "OBJ_ID": 106,
      "POINT": 0,
      "COMP": 0,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": 0.0001,
      "bLB": true,
      "LB_VALUE": -0.0001
    }
  }
}
```

**GET Response Body**

```json
{
  "ULFC": {
    "2": {
      "NAME": "Ele-03",
      "TYPE": "BEAM",
      "OBJ_ID": 3,
      "POINT": 1,
      "COMP": 4,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -220,
      "bLB": true,
      "LB_VALUE": -230
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

# ── POST: 定义未知荷载系数约束条件 (不等式 + 等式混合) ──────────
payload = {
    "Assign": {
        # 不等式: 将梁单元 3 号 I 端附近的 My 约束在 -230 ~ -220 范围内
        "2": {
            "NAME": "Ele-03", "TYPE": "BEAM", "OBJ_ID": 3,
            "POINT": 1, "COMP": 4, "EQ": False,
            "bUB": True, "UB_VALUE": -220,
            "bLB": True, "LB_VALUE": -230
        },
        # 等式: 将节点 7 号反力 FY 约束为 500
        "3": {
            "NAME": "Node-07", "TYPE": "REAC", "OBJ_ID": 7,
            "POINT": 4, "COMP": 1, "EQ": True,
            "bVALUE": True, "VALUE": 500, "OtherObject": 0
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/ULFC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询约束条件 ─────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/ULFC", headers=HEADERS)
for key, val in resp.json().get("ULFC", {}).items():
    cond = "等式" if val.get("EQ") else "不等式"
    print(f"  [{key}] {val['NAME']} ({val['TYPE']}) {cond} 约束")
```

---

## 5. `/ope/GSBG` — Bridge Girder Diagram Image Generation

> **功能：** 将通过 [`/db/GSBG`](#1-dbgsbg--bridge-girder-diagrams)定义的主梁图(应力或
> 构件内力)针对指定施工阶段区间生成为图像文件(bmp/jpg/emf)。如果说 `db/GSBG` 是**定义**
> 图组的 Endpoint，那么本 Endpoint 是将该结果**生成为图像的**
> 独立 OPE(Operation) Endpoint。与 `15_OPE.md` §19 文档化同一 Endpoint(官方
> JSON Schema 说明: "GSBG OPE request argument for Bridge Girder Diagram image generation")，
> 为便于桥梁特化章节读者阅读，本章也重复收录。

### Input URI

```
{base url}/ope/GSBG
```

### Active Methods

`POST`

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 荷载工况/组合名称 | `"LC_NAME"` | String | — | **Required** |
| 2 | 图类型 · 应力: `0` / 构件内力: `1` | `"DGRM_TYPE"` | Integer (enum) | — | **Required** |
| 3 | 是否批量处理 (省略时 `true`) | `"BATCH"` | Boolean | `true` | Optional |
| 4 | X 轴类型 · 距离: `0` / 节点: `1` | `"X_AXIS_TYPE"` | Integer (enum) | `0` | Optional |
| **BATCH = true(含省略)** | | | | | |
| 5 | 待导出的输出组名称列表(字符串数组) | `"BATCH_LIST"` | Array [String] | — | **Required** |
| **BATCH = false** | | | | | |
| 6 | 桥梁主梁单元组 | `"BRDG_GROUP"` | String | — | **Required** |
| 7 | 分量 · 应力(DGRM_TYPE=0): Sax `0` / +Sby `1` / −Sby `2` / +Sbz `3` / −Sbz `4` / Combined `5` / 7th DOF `6` · 构件内力(DGRM_TYPE=1): Fx `0` / Fy `1` / Fz `2` / Mx `3` / My `4` / Mz `5` / Mb `6` / Mt `7` / Mw `8` | `"COMPONENTS"` | Integer (enum) | `0` | Optional |
| 8 | (应力·Combined 时) 应力显示位置 · Maximum `0` / 1(−y,+z) `1` / 2(+y,+z) `2` / 3(+y,−z) `3` / 4(−y,−z) `4` | `"COMBINED_COMP"` | Integer (enum) | `0` | Optional |
| 9 | (应力·7th DOF 时) 7th DOF 类型 · Sax(Warping) `0` / Ssy(Mt) `1` / Ssy(Mw) `2` / Ssz(Mt) `3` / Ssz(Mw) `4` / Combined(Ssy) `5` / Combined(Ssz) `6` | `"7TH_DOF_TYPE"` | Integer (enum) | `0` | Optional |
| **仅 DGRM_TYPE = 0(应力)** | | | | | |
| 10 | 容许应力线显示 | `"STRESS_LINE"` | Object | — | Optional |
| (1) | 是否显示容许应力线 | `STRESS_LINE.OPT_USE` | Boolean | `false` | Optional |
| (2) | 受压容许应力(OPT_USE=true 时) | `STRESS_LINE.COMP` | Integer | — | 条件性 **Required** |
| (3) | 受拉容许应力(OPT_USE=true 时) | `STRESS_LINE.TENS` | Integer | — | 条件性 **Required** |
| 11 | 生成图的目标施工阶段列表 | `"STAGE_LIST"` | Array [String] | — | **Required** |
| 12 | 生成图像的保存路径 | `"EXPORT_PATH"` | String | — | **Required** |
| 13 | 保存图像扩展名 · `"bmp"` / `"jpg"` / `"emf"` | `"EXTENSION"` | String (enum) | — | **Required** |

> ✅ **2026-09-06 部分解决确认：** 原文 Specifications 表中应力分量第 4 项曾写作 `"Sbz" 4`、漏掉符号
> 的误记，经 2026-09-01 更新后**已补上符号**，现为 `-Sbz" 4`
> (推测为 2026-08-27 错误提报 Jira `MAPI-2484` 的反映结果)。上表的 `−Sbz` 写法依然有效。
> ⚠️ 只是应出现冒号的位置仍残留 `"`(`-Sbz" 4`)，标点符号误记尚未解决
> ——属剩余错误的提报对象。
> `BATCH=true` 时不得将 `BRDG_GROUP`·`COMPONENTS`·`COMBINED_COMP`·`7TH_DOF_TYPE` 一并置于顶层，
> `BATCH=false` 时则相反，不得发送 `BATCH_LIST`(原文 JSON Schema
> `allOf`/`if-then` 约束)。

### Request / Response JSON

**POST Request Body — 应力，Batch 方式**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 0,
    "BATCH": true,
    "X_AXIS_TYPE": 1,
    "STRESS_LINE": {"OPT_USE": true, "COMP": 210000, "TENS": 180000},
    "BATCH_LIST": ["Stress_Combined_Left", "Stress_7thDOF_Right", "Stress_Girder_Center"],
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\StressBatch",
    "EXTENSION": "jpg"
  }
}
```

**POST Request Body — 构件内力，单一组方式**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 1,
    "BATCH": false,
    "X_AXIS_TYPE": 0,
    "BRDG_GROUP": "BG_RIGHT",
    "COMPONENTS": 8,
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\ForceSingle",
    "EXTENSION": "jpg"
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

# ── POST: 批量保存应力图图像(BATCH) ──────────────────
payload = {
    "Argument": {
        "LC_NAME": "Dead Load",
        "DGRM_TYPE": 0,
        "BATCH": True,
        "X_AXIS_TYPE": 1,
        "STRESS_LINE": {"OPT_USE": True, "COMP": 210000, "TENS": 180000},
        "BATCH_LIST": ["Stress_Combined_Left", "Stress_7thDOF_Right", "Stress_Girder_Center"],
        "STAGE_LIST": ["CS1", "CS2"],
        "EXPORT_PATH": "C:\\Temp\\GSBG\\StressBatch",
        "EXTENSION": "jpg"
    }
}
resp = requests.post(f"{BASE_URL}/ope/GSBG", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## End-to-End Workflow

以下为拉索桥施工阶段分析后，设置桥梁特化结果(预拱度·主梁图·未知荷载系数)的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 定义未知荷载系数约束条件 (用于拉索张力优化) ──────
ulfc_payload = {
    "Assign": {
        "1": {
            "NAME": "Deck-Level", "TYPE": "DISP", "OBJ_ID": 106,
            "POINT": 0, "COMP": 2, "EQ": False,
            "bUB": True, "UB_VALUE": 0.01,
            "bLB": True, "LB_VALUE": -0.01
        }
    }
}
r1 = requests.post(f"{BASE_URL}/db/ULFC", json=ulfc_payload, headers=HEADERS)
print(f"STEP1 ULFC: {r1.status_code}")

# ── STEP 2: 设置一般预拱度基准 (按施工阶段分组) ──────────────────
gcmb_payload = {
    "Assign": {
        "1": {
            "bSTART_PT_ZERO": True,
            "GCMB_BASE_ITEMS": [
                {"GRUP_NAME": f"CS_{i}", "DIRECTION": "+DX"} for i in range(10)
            ]
        }
    }
}
r2 = requests.post(f"{BASE_URL}/db/GCMB", json=gcmb_payload, headers=HEADERS)
print(f"STEP2 GCMB: {r2.status_code}")

# ── STEP 3: 设置 FCM 预拱度控制 ─────────────────────────────────────
camb_payload = {
    "Assign": {
        "1": {
            "BODY_GROUP_NAME": "FSM",
            "SUPP_GROUP_NAME": "PSC-BN",
            "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
        }
    }
}
r3 = requests.post(f"{BASE_URL}/db/CAMB", json=camb_payload, headers=HEADERS)
print(f"STEP3 CAMB: {r3.status_code}")

# ── STEP 4: 设置主梁图 (构件内力 My) ───────────────────────
gsbg_payload = {
    "Assign": {
        "1": {
            "NAME": "Girder_My", "BATCH": True, "BODY_ELEM_GRUP_K": 1,
            "ALLSTAGE": True, "DGRM_TYPE": 1, "MOMENT_COMP": 4, "SCALEFACTOR": 1
        }
    }
}
r4 = requests.post(f"{BASE_URL}/db/GSBG", json=gsbg_payload, headers=HEADERS)
print(f"STEP4 GSBG: {r4.status_code}")

# ── 确认全部设置 ─────────────────────────────────────────────────
print("\n=== 桥梁特化结果设置确认 ===")
for ep in ["ULFC", "GCMB", "CAMB", "GSBG"]:
    r = requests.get(f"{BASE_URL}/db/{ep}", headers=HEADERS)
    data = r.json().get(ep, {})
    print(f"  {ep}: {len(data)} 项")
```
