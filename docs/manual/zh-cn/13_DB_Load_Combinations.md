# 13. DB – Load Combinations / Results

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头部：** `MAPI-Key: <签发的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../13_DB_Load_Combinations.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## Endpoint 列表

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/LCOM-GEN`](#1-dblcom-gen--load-combinations--general) | 荷载组合 – 一般 | POST, GET, PUT, DELETE |
| 2 | [`/db/LCOM-CONC`](#2-dblcom-conc--load-combinations--concrete-design) | 荷载组合 – 混凝土设计 | POST, GET, PUT, DELETE |
| 3 | [`/db/LCOM-STEEL`](#3-dblcom-steel--load-combinations--steel-design) | 荷载组合 – 钢结构设计 | POST, GET, PUT, DELETE |
| 4 | [`/db/LCOM-SRC`](#4-dblcom-src--load-combinations--src-design) | 荷载组合 – SRC 型钢混凝土设计 | POST, GET, PUT, DELETE |
| 5 | [`/db/LCOM-STLCOMP`](#5-dblcom-stlcomp--load-combinations--composite-steel-girder-design) | 荷载组合 – 钢组合主梁设计 | POST, GET, PUT, DELETE |
| 6 | [`/db/LCOM-SEISMIC`](#6-dblcom-seismic--load-combinations--seismic-design) | 荷载组合 – 抗震设计 | POST, GET, PUT, DELETE |
| 7 | [`/db/CUTL`](#7-dbcutl--cutting-line) | 切断线（Cutting Line） | POST, GET, PUT, DELETE |
| 8 | [`/db/CLWP`](#8-dbclwp--plate-cutting-line-diagram) | 板切断线图 | POST, GET, PUT, DELETE |

---

## 通用概念

### `vCOMB` 数组 — ANAL 类型取值

所有 LCOM 系列 Endpoint 的组合条目数组（`vCOMB`）所使用的分析类型：

| `ANAL` 值 | 说明 |
|-----------|------|
| `"ST"` | Static Load Case (静力荷载工况) |
| `"CS"` | Construction Stage Case (施工阶段工况) |
| `"MV"` | Moving Load Case (移动荷载工况) |
| `"SM"` | Settlement Case (沉降工况) |
| `"RS"` | Response Spectrum Case (反应谱工况) |
| `"TH"` | Time History Case (时程工况) |
| `"CB"` | General Combination (一般组合) |

### `iTYPE` — 叠加方式

| 值 | 方式 | LCOM-GEN | LCOM-CONC | LCOM-STEEL/SRC/STLCOMP | LCOM-SEISMIC |
|----|------|:--------:|:---------:|:----------------------:|:------------:|
| `0` | Add（相加） | ✔ | ✔ | ✔ | ✔ |
| `1` | Envelope（包络） | ✔ | ✔ | ✔ | ✔ |
| `2` | ABS（绝对值） | ✔ | ✔ | — | — |
| `3` | SRSS | ✔ | ✔ | ✔ | ✔ |

---

## 1. `/db/LCOM-GEN` — Load Combinations – General

> **功能：** 定义一般荷载组合。将静力·移动·反应谱·时程·施工阶段·沉降工况加以组合，生成用于结构分析结果的荷载组合。

### Input URI

```
{base url}/db/LCOM-GEN
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-GEN": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber", "type": "integer" },
      "NAME":   { "description": "CombinationName",   "type": "string" },
      "ACTIVE": { "description": "ActiveType",         "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",         "type": "integer" },
      "DESC":   { "description": "Description",        "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType",  "type": "string" },
            "LCNAME": { "description": "LoadCaseName",  "type": "string" },
            "FACTOR": { "description": "Factor",        "type": "number" }
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
| 1 | 组合编号（只读） | `"NO"` | Integer | — | Read Only |
| 2 | 组合名称 | `"NAME"` | String | — | **Required** |
| 3 | 激活类型 · `"INACTIVE"` / `"ACTIVE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 叠加方式 · `0`=Add / `1`=Envelope / `2`=ABS / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 说明 | `"DESC"` | String | `""` | Optional |
| 6 | 结果类型（只读） · `false`=General / `true`=Min/Max/All | `"bCB"` | Boolean | — | Read Only |
| 7 | 组合条目数组 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 分析类型 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 荷载工况名 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 系数 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "LC1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.2D + 1.0L + 1.0RS",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad",   "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad",   "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "SeismicX",   "FACTOR": 1.0 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "LC2",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 1,
      "DESC": "Envelope: Dead + Live",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-GEN": {
    "1": {
      "NO": 1,
      "NAME": "LC1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.2D + 1.0L + 1.0RS",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "SeismicX", "FACTOR": 1.0 }
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

# ── POST：创建一般荷载组合 ──────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "COMB_GEN_1",
            "ACTIVE": "ACTIVE",
            "bCB": False,
            "iTYPE": 0,          # 0=Add
            "DESC": "1.2D + 1.6L",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-GEN", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET：查询全部 ─────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-GEN", headers=HEADERS)
combos = resp.json().get("LCOM-GEN", {})
print(f"一般荷载组合数：{len(combos)}")
for key, val in combos.items():
    print(f"  [{key}] {val['NAME']} ({val['ACTIVE']}) iTYPE={val['iTYPE']}")

# ── DELETE：删除特定组合 ─────────────────────────────────────────
resp = requests.delete(f"{BASE_URL}/db/LCOM-GEN", json={"Assign": {"1": {}}}, headers=HEADERS)
print("DELETE:", resp.status_code)
```

---

## 2. `/db/LCOM-CONC` — Load Combinations – Concrete Design

> **功能：** 定义混凝土设计用荷载组合。可区分强度设计（Strength）/ 使用性设计（Service），并增设混凝土设计专用选项（`bES`）。  
> **适用产品：** Endpoint 本身为 Civil NX·Gen NX 共用。仅 `bES`（Concrete Design Option）字段为 MIDAS Civil NX 专用 — 原文中“MIDAS CIVIL NX only”图标只标在该字段上，并未标注于其他字段与整个 Endpoint（⚠️ 2026-08-26 确认，此前误将整节记为 Civil NX 专用）

### Input URI

```
{base url}/db/LCOM-CONC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-CONC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bES":    { "description": "E (Concrete design only)",   "type": "boolean" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
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
| 1 | 组合编号（只读） | `"NO"` | Integer | — | Read Only |
| 2 | 组合名称 | `"NAME"` | String | — | **Required** |
| 3 | 激活类型 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 混凝土设计专用选项（E） | `"bES"` | Boolean | `false` | Optional |
| 5 | 叠加方式 · `0`=Add / `1`=Envelope / `2`=ABS / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 6 | 说明 | `"DESC"` | String | `""` | Optional |
| 7 | 结果类型（只读） · `false`=General / `true`=Min/Max/All | `"bCB"` | Boolean | — | Read Only |
| 8 | 组合条目数组 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 分析类型 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 荷载工况名 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 系数 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "cLCB1",
      "ACTIVE": "STRENGTH",
      "bES": false,
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.25D + 1.5L (Strength)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.5  }
      ]
    },
    "6": {
      "NO": 6,
      "NAME": "cLCB2",
      "ACTIVE": "SERVICE",
      "bES": false,
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0L (Service)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-CONC": {
    "1": {
      "NO": 1,
      "NAME": "cLCB1",
      "ACTIVE": "STRENGTH",
      "bES": false,
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.25D + 1.5L (Strength)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.5  }
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

# ── POST：创建混凝土设计用荷载组合 ──────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "CONC_STR_1",
            "ACTIVE": "STRENGTH",     # 强度设计
            "bES": False,
            "bCB": False,
            "iTYPE": 0,               # Add
            "DESC": "KDS 41 20:2022 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.25},
                {"ANAL": "ST", "LCNAME": "LiveLoad",  "FACTOR": 1.8},
                {"ANAL": "RS", "LCNAME": "SeismicX",  "FACTOR": 1.0}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "CONC_SRV_1",
            "ACTIVE": "SERVICE",      # 使用性设计
            "bES": False,
            "bCB": False,
            "iTYPE": 0,
            "DESC": "KDS 41 20:2022 사용조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-CONC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET：查询组合列表 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-CONC", headers=HEADERS)
for key, val in resp.json().get("LCOM-CONC", {}).items():
    print(f"  [{key}] {val['NAME']} ({val['ACTIVE']})")
```

---

## 3. `/db/LCOM-STEEL` — Load Combinations – Steel Design

> **功能：** 定义钢结构设计用荷载组合。结构与 LCOM-GEN 相同，但 ACTIVE 类型区分为 STRENGTH / SERVICE，且不支持 ABS 叠加方式。

### Input URI

```
{base url}/db/LCOM-STEEL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-STEEL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
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
| 1 | 组合编号（只读） | `"NO"` | Integer | — | Read Only |
| 2 | 组合名称 | `"NAME"` | String | — | **Required** |
| 3 | 激活类型 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 叠加方式 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 说明 | `"DESC"` | String | `""` | Optional |
| 6 | 结果类型（只读） · `false`=General / `true`=Min/Max/All | `"bCB"` | Boolean | — | Read Only |
| 7 | 组合条目数组 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 分析类型 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 荷载工况名 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 系数 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "sLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.2D + 1.6L (강도)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "sLCB2",
      "ACTIVE": "SERVICE",
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0L (사용성)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-STEEL": {
    "1": {
      "NO": 1,
      "NAME": "sLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": true,
      "iTYPE": 0,
      "DESC": "1.2D + 1.6L (강도)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2 },
        { "ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6 }
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

# ── POST：创建钢结构设计用荷载组合 ───────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "STEEL_STR_1",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,            # Add
            "DESC": "KDS 41 30:2022 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.2},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.6}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "STEEL_STR_2",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 3,            # SRSS
            "DESC": "지진조합 SRSS",
            "vCOMB": [
                {"ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-STEEL", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 4. `/db/LCOM-SRC` — Load Combinations – SRC Design

> **功能：** SRC（型钢混凝土组合）设计用荷载组合。结构与 LCOM-STEEL 相同。

### Input URI

```
{base url}/db/LCOM-SRC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-SRC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
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
| 1 | 组合编号（只读） | `"NO"` | Integer | — | Read Only |
| 2 | 组合名称 | `"NAME"` | String | — | **Required** |
| 3 | 激活类型 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 叠加方式 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 说明 | `"DESC"` | String | `""` | Optional |
| 6 | 结果类型（只读） | `"bCB"` | Boolean | — | Read Only |
| 7 | 组合条目数组 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 分析类型 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 荷载工况名 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 系数 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "rLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.4(cD)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.4 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "rLCB2",
      "ACTIVE": "SERVICE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "SERV:(cD)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-SRC": {
    "1": {
      "NO": 1,
      "NAME": "rLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.4(cD)",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.4 }
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

# ── POST：创建 SRC 设计用荷载组合 ────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "SRC_STR_1",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "AIK-SRC2K 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.4},
                {"ANAL": "ST", "LCNAME": "LiveLoad",  "FACTOR": 1.7}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-SRC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── PUT：修改特定组合 ────────────────────────────────────────────
update_payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "SRC_STR_1_UPD",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "수정된 SRC 강도조합",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25},
                {"ANAL": "ST", "LCNAME": "LiveLoad", "FACTOR": 1.5}
            ]
        }
    }
}
resp = requests.put(f"{BASE_URL}/db/LCOM-SRC", json=update_payload, headers=HEADERS)
print("PUT:", resp.status_code, resp.json())
```

---

## 5. `/db/LCOM-STLCOMP` — Load Combinations – Composite Steel Girder Design

> **功能：** 钢组合主梁（Composite Steel Girder）设计用荷载组合。结构与 LCOM-STEEL 相同。  
> **适用产品：** MIDAS Civil NX 专用（桥梁设计）— ⚠️ 2026-08-26 确认：原文文章并无
> 支撑该产品限制的根据（图标·文字）。钢组合主梁设计属于桥梁专用功能
> 系基于一般常识的推测性标注，并非该文章本身可确认的事实。

### Input URI

```
{base url}/db/LCOM-STLCOMP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-STLCOMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
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
| 1 | 组合编号（只读） | `"NO"` | Integer | — | Read Only |
| 2 | 组合名称 | `"NAME"` | String | — | **Required** |
| 3 | 激活类型 · `"INACTIVE"` / `"STRENGTH"` / `"SERVICE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 叠加方式 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 说明 | `"DESC"` | String | `""` | Optional |
| 6 | 结果类型（只读） | `"bCB"` | Boolean | — | Read Only |
| 7 | 组合条目数组 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 分析类型 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 荷载工况名 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 系数 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "scLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.25D + 1.75L",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.75 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "scLCB2",
      "ACTIVE": "SERVICE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0L",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-STLCOMP": {
    "1": {
      "NO": 1,
      "NAME": "scLCB1",
      "ACTIVE": "STRENGTH",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.25D + 1.75L",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.25 },
        { "ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.75 }
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

# ── POST：创建钢组合主梁设计用荷载组合 ────────────────────────
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "COMP_STR_1",
            "ACTIVE": "STRENGTH",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "교량 강도조합 Ⅰ",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.25},
                {"ANAL": "MV", "LCNAME": "TruckLoad", "FACTOR": 1.75}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "COMP_SRV_1",
            "ACTIVE": "SERVICE",
            "bCB": False,
            "iTYPE": 0,
            "DESC": "교량 사용조합 Ⅱ",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.0},
                {"ANAL": "MV", "LCNAME": "TruckLoad", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-STLCOMP", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET：查询钢组合主梁组合列表 ──────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-STLCOMP", headers=HEADERS)
for key, val in resp.json().get("LCOM-STLCOMP", {}).items():
    print(f"  [{key}] {val['NAME']} ({val['ACTIVE']}) iTYPE={val['iTYPE']}")
```

---

## 6. `/db/LCOM-SEISMIC` — Load Combinations – Seismic Design

> **功能：** 定义抗震设计用荷载组合。ACTIVE 类型与 LCOM-GEN 相同（INACTIVE/ACTIVE），但不支持 ABS 叠加方式。反应谱工况用于 SRSS 或 CQC 组合。

### Input URI

```
{base url}/db/LCOM-SEISMIC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "LCOM-SEISMIC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NO":     { "description": "CombinationNumber",          "type": "integer" },
      "NAME":   { "description": "CombinationName",            "type": "string" },
      "ACTIVE": { "description": "ActiveType",                  "type": "string" },
      "bCB":    { "description": "(ReadOnly) min/max cb type", "type": "boolean" },
      "iTYPE":  { "description": "Sum.method",                 "type": "integer" },
      "DESC":   { "description": "Description",                "type": "string" },
      "vCOMB":  {
        "description": "CombinationList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ANAL":   { "description": "AnalysisType", "type": "string" },
            "LCNAME": { "description": "LoadCaseName", "type": "string" },
            "FACTOR": { "description": "Factor",       "type": "number" }
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
| 1 | 组合编号（只读） | `"NO"` | Integer | — | Read Only |
| 2 | 组合名称 | `"NAME"` | String | — | **Required** |
| 3 | 激活类型 · `"INACTIVE"` / `"ACTIVE"` | `"ACTIVE"` | String | `"ACTIVE"` | Optional |
| 4 | 叠加方式 · `0`=Add / `1`=Envelope / `3`=SRSS | `"iTYPE"` | Integer | `0` | Optional |
| 5 | 说明 | `"DESC"` | String | `""` | Optional |
| 6 | 结果类型（只读） | `"bCB"` | Boolean | — | Read Only |
| 7 | 组合条目数组 | `"vCOMB"` | Array | — | **Required** |
| — | (vCOMB) 分析类型 | `"ANAL"` | String | — | **Required** |
| — | (vCOMB) 荷载工况名 | `"LCNAME"` | String | — | **Required** |
| — | (vCOMB) 系数 | `"FACTOR"` | Number | — | **Required** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NO": 1,
      "NAME": "S1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0RS_X",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0 }
      ]
    },
    "2": {
      "NO": 2,
      "NAME": "S2",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 3,
      "DESC": "SRSS: RX + RY",
      "vCOMB": [
        { "ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "LCOM-SEISMIC": {
    "1": {
      "NO": 1,
      "NAME": "S1",
      "ACTIVE": "ACTIVE",
      "bCB": false,
      "iTYPE": 0,
      "DESC": "1.0D + 1.0RS_X",
      "vCOMB": [
        { "ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0 },
        { "ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0 }
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

# ── POST：创建抗震设计用荷载组合 ───────────────────────────────
# 以 KDS 17:2022 为准的抗震组合：1.0D ± 1.0RS_X ± 0.3RS_Y
payload = {
    "Assign": {
        "1": {
            "NO": 1,
            "NAME": "SEIS_1",
            "ACTIVE": "ACTIVE",
            "bCB": False,
            "iTYPE": 0,            # Add
            "DESC": "1.0D + 1.0RX + 0.3RY",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY",       "FACTOR": 0.3}
            ]
        },
        "2": {
            "NO": 2,
            "NAME": "SEIS_2",
            "ACTIVE": "ACTIVE",
            "bCB": False,
            "iTYPE": 3,            # SRSS
            "DESC": "SRSS(RX, RY, RZ)",
            "vCOMB": [
                {"ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RZ", "FACTOR": 1.0}
            ]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/LCOM-SEISMIC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET：查询抗震组合 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/LCOM-SEISMIC", headers=HEADERS)
seismic_combos = resp.json().get("LCOM-SEISMIC", {})
print(f"抗震荷载组合数：{len(seismic_combos)}")
```

---

## 7. `/db/CUTL` — Cutting Line

> **功能：** 为提取结构模型的截面力（Sectional Force）结果定义切断线（Cutting Line）。指定两点（PT1、PT2）以设定切断方向与位置。

### Input URI

```
{base url}/db/CUTL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "CUTL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name",         "type": "string"  },
      "DIR":  { "description": "Direction",    "type": "string"  },
      "PT1X": { "description": "Point1X",      "type": "number"  },
      "PT1Y": { "description": "Point1Y",      "type": "number"  },
      "PT1Z": { "description": "Point1Z",      "type": "number"  },
      "PT2X": { "description": "Point2X",      "type": "number"  },
      "PT2Y": { "description": "Point2Y",      "type": "number"  },
      "PT2Z": { "description": "Point2Z",      "type": "number"  },
      "R":    { "description": "ColorRValue",  "type": "integer" },
      "G":    { "description": "ColorGValue",  "type": "integer" },
      "B":    { "description": "ColorBValue",  "type": "integer" },
      "TYPE": { "description": "Type",         "type": "integer" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 切断线名称 | `"NAME"` | String | — | **Required** |
| 2 | 方向 · `"NORMAL"` = 法线方向 / `"DIR"` = 面内方向 | `"DIR"` | String | — | **Required** |
| 3 | 点 1 – X 坐标 | `"PT1X"` | Number | — | **Required** |
| 4 | 点 1 – Y 坐标 | `"PT1Y"` | Number | — | **Required** |
| 5 | 点 1 – Z 坐标 | `"PT1Z"` | Number | — | **Required** |
| 6 | 点 2 – X 坐标 | `"PT2X"` | Number | — | **Required** |
| 7 | 点 2 – Y 坐标 | `"PT2Y"` | Number | — | **Required** |
| 8 | 点 2 – Z 坐标 | `"PT2Z"` | Number | — | **Required** |
| 9 | 线颜色 – 红(R) 值 (0–255) | `"R"` | Integer | `0` | Optional |
| 10 | 线颜色 – 绿(G) 值 (0–255) | `"G"` | Integer | `0` | Optional |
| 11 | 线颜色 – 蓝(B) 值 (0–255) | `"B"` | Integer | `0` | Optional |
| 12 | 类型 | `"TYPE"` | Integer | `0` | Optional |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NAME": "Cut-Line#1",
      "DIR":  "NORMAL",
      "PT1X": 8.95,
      "PT1Y": 11.0725,
      "PT1Z": 1.205,
      "PT2X": 8.95,
      "PT2Y": -1.0725,
      "PT2Z": 1.205,
      "R": 255,
      "G": 0,
      "B": 0,
      "TYPE": 0
    },
    "2": {
      "NAME": "Cut-Line#2",
      "DIR":  "DIR",
      "PT1X": 0.0,
      "PT1Y": 5.0,
      "PT1Z": 3.0,
      "PT2X": 10.0,
      "PT2Y": 5.0,
      "PT2Z": 3.0,
      "R": 0,
      "G": 0,
      "B": 255,
      "TYPE": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "CUTL": {
    "1": {
      "NAME": "Cut-Line#1",
      "DIR":  "NORMAL",
      "PT1X": 8.95,  "PT1Y": 11.0725, "PT1Z": 1.205,
      "PT2X": 8.95,  "PT2Y": -1.0725, "PT2Z": 1.205,
      "R": 255, "G": 0, "B": 0,
      "TYPE": 0
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

# ── POST：创建切断线 ──────────────────────────────────────────────
cutting_lines = {
    "1": {
        "NAME": "Section_A-A",
        "DIR":  "NORMAL",        # 法线方向切断
        "PT1X": 5.0,  "PT1Y": 0.0,  "PT1Z": 0.0,
        "PT2X": 5.0,  "PT2Y": 10.0, "PT2Z": 0.0,
        "R": 255, "G": 0, "B": 0,   # 红色
        "TYPE": 0
    },
    "2": {
        "NAME": "Section_B-B",
        "DIR":  "NORMAL",
        "PT1X": 10.0, "PT1Y": 0.0,  "PT1Z": 0.0,
        "PT2X": 10.0, "PT2Y": 10.0, "PT2Z": 0.0,
        "R": 0, "G": 128, "B": 0,   # 绿色
        "TYPE": 0
    }
}
resp = requests.post(
    f"{BASE_URL}/db/CUTL",
    json={"Assign": cutting_lines},
    headers=HEADERS
)
print("POST:", resp.status_code, resp.json())

# ── GET：查询全部切断线 ──────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CUTL", headers=HEADERS)
cutlines = resp.json().get("CUTL", {})
print(f"切断线数量：{len(cutlines)}")
for key, val in cutlines.items():
    print(f"  [{key}] {val['NAME']} DIR={val['DIR']}")
    print(f"       PT1=({val['PT1X']}, {val['PT1Y']}, {val['PT1Z']})")
    print(f"       PT2=({val['PT2X']}, {val['PT2Y']}, {val['PT2Z']})")

# ── DELETE：删除切断线 ────────────────────────────────────────────
resp = requests.delete(
    f"{BASE_URL}/db/CUTL",
    json={"Assign": {"1": {}}},
    headers=HEADERS
)
print("DELETE:", resp.status_code)
```

---

## 8. `/db/CLWP` — Plate Cutting Line Diagram

> **功能：** 定义板（Plate）单元的切断线图。与 CUTL（1D 切断线）不同，以三点（PT1、PT2、PT3）确定平面（Plane）来提取板单元的截面力。

### Input URI

```
{base url}/db/CLWP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "CLWP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name",        "type": "string"  },
      "DIR":  { "description": "Direction",   "type": "string"  },
      "PT1X": { "description": "Point1X",     "type": "number"  },
      "PT1Y": { "description": "Point1Y",     "type": "number"  },
      "PT1Z": { "description": "Point1Z",     "type": "number"  },
      "PT2X": { "description": "Point2X",     "type": "number"  },
      "PT2Y": { "description": "Point2Y",     "type": "number"  },
      "PT2Z": { "description": "Point2Z",     "type": "number"  },
      "PT3X": { "description": "Point3X",     "type": "number"  },
      "PT3Y": { "description": "Point3Y",     "type": "number"  },
      "PT3Z": { "description": "Point3Z",     "type": "number"  },
      "R":    { "description": "ColorRValue", "type": "integer" },
      "G":    { "description": "ColorGValue", "type": "integer" },
      "B":    { "description": "ColorBValue", "type": "integer" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 切断线名称 | `"NAME"` | String | — | **Required** |
| 2 | 方向 · `"NORMAL"` = 法线 / `"DIR"` = 面内 / `"PLANE"` = 平面 | `"DIR"` | String | — | **Required** |
| 3 | 点 1 – X 坐标 | `"PT1X"` | Number | — | **Required** |
| 4 | 点 1 – Y 坐标 | `"PT1Y"` | Number | — | **Required** |
| 5 | 点 1 – Z 坐标 | `"PT1Z"` | Number | — | **Required** |
| 6 | 点 2 – X 坐标 | `"PT2X"` | Number | — | **Required** |
| 7 | 点 2 – Y 坐标 | `"PT2Y"` | Number | — | **Required** |
| 8 | 点 2 – Z 坐标 | `"PT2Z"` | Number | — | **Required** |
| 9 | 点 3 – X 坐标 | `"PT3X"` | Number | — | **Required** |
| 10 | 点 3 – Y 坐标 | `"PT3Y"` | Number | — | **Required** |
| 11 | 点 3 – Z 坐标 | `"PT3Z"` | Number | — | **Required** |
| 12 | 线颜色 – 红(R) 值 (0–255) | `"R"` | Integer | `0` | Optional |
| 13 | 线颜色 – 绿(G) 值 (0–255) | `"G"` | Integer | `0` | Optional |
| 14 | 线颜色 – 蓝(B) 值 (0–255) | `"B"` | Integer | `0` | Optional |

> **参考 — CUTL 与 CLWP 对比：**
>
> | 项目 | CUTL | CLWP |
> |------|------|------|
> | 对象单元 | 梁·桁架·链接等 1D 单元 | 板（Plate）单元 |
> | 点数 | 2 点 (PT1, PT2) | 3 点 (PT1, PT2, PT3) |
> | DIR 值 | `NORMAL` / `DIR` | `NORMAL` / `DIR` / `PLANE` |
> | `TYPE` 字段 | 有 | 无 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NAME": "CL1",
      "DIR":  "PLANE",
      "PT1X": 0,
      "PT1Y": 10710,
      "PT1Z": -1000,
      "PT2X": 0,
      "PT2Y": 10710,
      "PT2Z": 0,
      "PT3X": 0,
      "PT3Y": 9945,
      "PT3Z": 0,
      "R": 0,
      "G": 0,
      "B": 0
    },
    "2": {
      "NAME": "CL2",
      "DIR":  "NORMAL",
      "PT1X": 5.0,
      "PT1Y": 0.0,
      "PT1Z": 0.0,
      "PT2X": 5.0,
      "PT2Y": 10.0,
      "PT2Z": 0.0,
      "PT3X": 5.0,
      "PT3Y": 5.0,
      "PT3Z": 3.0,
      "R": 255,
      "G": 0,
      "B": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "CLWP": {
    "1": {
      "NAME": "CL1",
      "DIR":  "PLANE",
      "PT1X": 0,    "PT1Y": 10710, "PT1Z": -1000,
      "PT2X": 0,    "PT2Y": 10710, "PT2Z": 0,
      "PT3X": 0,    "PT3Y": 9945,  "PT3Z": 0,
      "R": 0, "G": 0, "B": 0
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

# ── POST：创建板切断线图 ───────────────────────────────
# 以三点定义平面（Plane），设定板单元截面力的提取位置
payload = {
    "Assign": {
        "1": {
            "NAME": "PLATE_CUT_1",
            "DIR":  "PLANE",        # 平面切断
            "PT1X": 0.0,  "PT1Y": 10.0, "PT1Z": -2.0,
            "PT2X": 0.0,  "PT2Y": 10.0, "PT2Z":  0.0,
            "PT3X": 0.0,  "PT3Y":  8.0, "PT3Z":  0.0,
            "R": 255, "G": 165, "B": 0   # 橙色
        },
        "2": {
            "NAME": "PLATE_CUT_2",
            "DIR":  "NORMAL",       # 法线方向切断
            "PT1X": 5.0, "PT1Y": 0.0,  "PT1Z": 0.0,
            "PT2X": 5.0, "PT2Y": 10.0, "PT2Z": 0.0,
            "PT3X": 5.0, "PT3Y": 5.0,  "PT3Z": 3.0,
            "R": 0, "G": 0, "B": 200
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/CLWP", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET：查询全部板切断线 ───────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CLWP", headers=HEADERS)
clwp_data = resp.json().get("CLWP", {})
print(f"板切断线数量：{len(clwp_data)}")
for key, val in clwp_data.items():
    print(f"  [{key}] {val['NAME']} DIR={val['DIR']}")

# ── PUT：修改切断线位置 ──────────────────────────────────────────
update = {
    "Assign": {
        "1": {
            "NAME": "PLATE_CUT_1_UPD",
            "DIR":  "PLANE",
            "PT1X": 0.0,  "PT1Y": 12.0, "PT1Z": -2.0,
            "PT2X": 0.0,  "PT2Y": 12.0, "PT2Z":  0.0,
            "PT3X": 0.0,  "PT3Y": 10.0, "PT3Z":  0.0,
            "R": 255, "G": 0, "B": 0
        }
    }
}
resp = requests.put(f"{BASE_URL}/db/CLWP", json=update, headers=HEADERS)
print("PUT:", resp.status_code, resp.json())
```

---

## End-to-End Workflow

以下为桥梁结构物设计的荷载组合完整设置工作流。按各设计代码依次定义相应组合。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1：一般荷载组合（LCOM-GEN）──────────────────────────────
# 用于查看结构分析结果的基本组合
gen_payload = {
    "Assign": {
        "1": {
            "NO": 1, "NAME": "GEN_ULS_1",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 0,
            "DESC": "ULS: 1.35D + 1.5L",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.35},
                {"ANAL": "MV", "LCNAME": "LiveLoad",  "FACTOR": 1.5}
            ]
        },
        "2": {
            "NO": 2, "NAME": "GEN_SLS_1",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 0,
            "DESC": "SLS: 1.0D + 1.0L",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.0}
            ]
        }
    }
}
r1 = requests.post(f"{BASE_URL}/db/LCOM-GEN", json=gen_payload, headers=HEADERS)
print(f"STEP1 LCOM-GEN: {r1.status_code}")

# ── STEP 2：钢组合主梁设计组合（LCOM-STLCOMP）──────────────────
stlcomp_payload = {
    "Assign": {
        "1": {
            "NO": 1, "NAME": "COMP_STR_I",
            "ACTIVE": "STRENGTH", "bCB": False, "iTYPE": 0,
            "DESC": "AASHTO Strength I",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad",  "FACTOR": 1.25},
                {"ANAL": "MV", "LCNAME": "LiveLoad",  "FACTOR": 1.75}
            ]
        },
        "2": {
            "NO": 2, "NAME": "COMP_SRV_I",
            "ACTIVE": "SERVICE", "bCB": False, "iTYPE": 0,
            "DESC": "AASHTO Service I",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "MV", "LCNAME": "LiveLoad", "FACTOR": 1.0}
            ]
        }
    }
}
r2 = requests.post(f"{BASE_URL}/db/LCOM-STLCOMP", json=stlcomp_payload, headers=HEADERS)
print(f"STEP2 LCOM-STLCOMP: {r2.status_code}")

# ── STEP 3：抗震荷载组合（LCOM-SEISMIC）─────────────────────────
seismic_payload = {
    "Assign": {
        "1": {
            "NO": 1, "NAME": "SEIS_EQ_X",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 0,
            "DESC": "1.0D + 1.0EQ_X + 0.3EQ_Y",
            "vCOMB": [
                {"ANAL": "CS", "LCNAME": "DeadLoad", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RX",       "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY",       "FACTOR": 0.3}
            ]
        },
        "2": {
            "NO": 2, "NAME": "SEIS_SRSS",
            "ACTIVE": "ACTIVE", "bCB": False, "iTYPE": 3,  # SRSS
            "DESC": "SRSS(RX, RY, RZ)",
            "vCOMB": [
                {"ANAL": "RS", "LCNAME": "RX", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RY", "FACTOR": 1.0},
                {"ANAL": "RS", "LCNAME": "RZ", "FACTOR": 1.0}
            ]
        }
    }
}
r3 = requests.post(f"{BASE_URL}/db/LCOM-SEISMIC", json=seismic_payload, headers=HEADERS)
print(f"STEP3 LCOM-SEISMIC: {r3.status_code}")

# ── STEP 4：定义切断线（CUTL）────────────────────────────────────
# 在桥梁主跨跨中与端部 2 处切断
cutl_payload = {
    "Assign": {
        "1": {
            "NAME": "MidSpan",  "DIR": "NORMAL",
            "PT1X": 50.0, "PT1Y": 0.0,  "PT1Z": 0.0,
            "PT2X": 50.0, "PT2Y": 15.0, "PT2Z": 0.0,
            "R": 255, "G": 0, "B": 0, "TYPE": 0
        },
        "2": {
            "NAME": "QuarterSpan", "DIR": "NORMAL",
            "PT1X": 25.0, "PT1Y": 0.0,  "PT1Z": 0.0,
            "PT2X": 25.0, "PT2Y": 15.0, "PT2Z": 0.0,
            "R": 0, "G": 0, "B": 255, "TYPE": 0
        }
    }
}
r4 = requests.post(f"{BASE_URL}/db/CUTL", json=cutl_payload, headers=HEADERS)
print(f"STEP4 CUTL: {r4.status_code}")

# ── STEP 5：板单元切断线（CLWP）────────────────────────────────
# 定义桥面板（Deck Plate）切断线
clwp_payload = {
    "Assign": {
        "1": {
            "NAME": "DeckCut_1", "DIR": "PLANE",
            "PT1X": 50.0, "PT1Y": 0.0,  "PT1Z": -0.5,
            "PT2X": 50.0, "PT2Y": 0.0,  "PT2Z":  0.0,
            "PT3X": 50.0, "PT3Y": 15.0, "PT3Z":  0.0,
            "R": 200, "G": 50, "B": 0
        }
    }
}
r5 = requests.post(f"{BASE_URL}/db/CLWP", json=clwp_payload, headers=HEADERS)
print(f"STEP5 CLWP: {r5.status_code}")

# ── 确认全部设置 ─────────────────────────────────────────────────
print("\n=== 荷载组合设置确认 ===")
endpoints = ["LCOM-GEN", "LCOM-STLCOMP", "LCOM-SEISMIC", "CUTL", "CLWP"]
for ep in endpoints:
    r = requests.get(f"{BASE_URL}/db/{ep}", headers=HEADERS)
    data = r.json().get(ep, {})
    print(f"  {ep}: {len(data)}个")
```

---

## 按 LCOM 类型对比摘要

| Endpoint | ACTIVE 值 | iTYPE(ABS) | 附加字段 | 用途 |
|-----------|-----------|:-----------:|----------|------|
| `LCOM-GEN` | INACTIVE / ACTIVE | ✔(2) | — | 一般分析结果 |
| `LCOM-CONC` | INACTIVE / STRENGTH / SERVICE | ✔(2) | `bES` | 混凝土设计 |
| `LCOM-STEEL` | INACTIVE / STRENGTH / SERVICE | — | — | 钢结构设计 |
| `LCOM-SRC` | INACTIVE / STRENGTH / SERVICE | — | — | SRC 组合设计 |
| `LCOM-STLCOMP` | INACTIVE / STRENGTH / SERVICE | — | — | 钢组合主梁设计 |
| `LCOM-SEISMIC` | INACTIVE / ACTIVE | — | — | 抗震设计 |
