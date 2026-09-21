# 02. DB — Project / View / Structure Endpoints

> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **官方最后编辑：** 2025.11.04 · **本文件同步：** 2026-06-29  
> **适用产品：** MIDAS Civil NX · MIDAS Gen NX

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../02_DB_Project_Structure.md) · **原文同步日期：** 2026-06-29  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 概述

处理项目基本信息、单位制、结构类型、组、视图颜色、跨（Span）·楼层（Story）数据的一组 Endpoint。

**通用规则：**
- **请求体：** 以 `"Assign"` 键起始，编号键（ID）→ 数据结构
- 单位（`/db/UNIT`）·结构类型（`/db/STYP`）等新建文件必需数据**仅支持 `GET` / `PUT`**
- 其余一般数据均支持 `POST / GET / PUT / DELETE`

| No. | Endpoint | 功能 | 方法 |
|-----|----------|------|--------|
| 1 | [`/db/PJCF`](#1-dbpjcf--project-information) | Project Information | POST, GET, PUT, DELETE |
| 2 | [`/db/UNIT`](#2-dbunit--unit-system) | Unit System | **GET, PUT** |
| 3 | [`/db/STYP`](#3-dbstyp--structure-type) | Structure Type | **GET, PUT** |
| 4 | [`/db/STYP-M1`](#4-dbstyp-m1--structure-type-hyper-s) | Structure Type (Hyper-S) | **GET, PUT, DELETE** |
| 5 | [`/db/GRUP`](#5-dbgrup--structure-group) | Structure Group | POST, GET, PUT |
| 6 | [`/db/BNGR`](#6-dbbngr--boundary-group) | Boundary Group | POST, GET, PUT |
| 7 | [`/db/LDGR`](#7-dbldgr--load-group) | Load Group | POST, GET, PUT, DELETE |
| 8 | [`/db/TDGR`](#8-dbtdgr--tendon-group) | Tendon Group | POST, GET, PUT, DELETE |
| 9 | [`/db/NPLN`](#9-dbnpln--named-plane) | Named Plane | POST, GET, PUT, DELETE |
| 10 | [`/db/CO_M`](#10-dbco_m--material-color) | Material Color | **GET, PUT** |
| 11 | [`/db/CO_S`](#11-dbco_s--section-color) | Section Color | **GET, PUT** |
| 12 | [`/db/CO_T`](#12-dbco_t--thickness-color) | Thickness Color | **GET, PUT** |
| 13 | [`/db/CO_F`](#13-dbco_f--floor-load-color) | Floor Load Color | **GET, PUT** |
| 14 | [`/db/SPAN`](#14-dbspan--span-information) | Span Information | POST, GET, PUT, DELETE |
| 15 | [`/db/STOR`](#15-dbstor--story-data) | Story Data | POST, GET, PUT, DELETE |

---

## 通用辅助函数（Python）

```python
import requests
import os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": MAPI_KEY,
    }
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/db/PJCF` — Project Information

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/PJCF` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **官方文档** | [Project Information ↗](https://support.midasuser.com/hc/en-us/articles/35801869341337) |

### JSON Schema

```json
{
  "PJCF": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "PROJECT":  { "description": "ProjectName",   "type": "string" },
      "REVISION": { "description": "RevisionInfo",  "type": "string" },
      "USER":     { "description": "User",           "type": "string" },
      "EMAIL":    { "description": "E-mail",         "type": "string" },
      "ADDRESS":  { "description": "Address",        "type": "string" },
      "TEL":      { "description": "Telephone",      "type": "string" },
      "FAX":      { "description": "Fax",            "type": "string" },
      "CLIENT":   { "description": "Client",         "type": "string" },
      "TITLE":    { "description": "Title",          "type": "string" },
      "ENGINEER": { "description": "ReviewName",     "type": "string" },
      "EDATE":    { "description": "ReviewDate",     "type": "string" },
      "CHECK1":   { "description": "ReviewName",     "type": "string" },
      "CDATE1":   { "description": "ReviewDate",     "type": "string" },
      "CHECK2":   { "description": "ReviewName",     "type": "string" },
      "CDATE2":   { "description": "ReviewDate",     "type": "string" },
      "CHECK3":   { "description": "ReviewName",     "type": "string" },
      "CDATE3":   { "description": "ReviewDate",     "type": "string" },
      "APPROVE":  { "description": "ReviewName",     "type": "string" },
      "ADATE":    { "description": "ReviewDate",     "type": "string" },
      "COMMENT":  { "description": "Comments",       "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "PROJECT":  "Cable",
      "REVISION": "940",
      "USER":     "LJW",
      "EMAIL":    "cle1123",
      "ADDRESS":  "MIDASIT",
      "TEL":      "031789",
      "FAX":      "031789",
      "CLIENT":   "MIDASIT",
      "TITLE":    "CableBridge",
      "ENGINEER": "A",
      "EDATE":    "23.11",
      "CHECK1":   "B",
      "CDATE1":   "24.11",
      "CHECK2":   "C",
      "CDATE2":   "24.12",
      "CHECK3":   "D",
      "CDATE3":   "24.12",
      "APPROVE":  "E",
      "ADATE":    "14.2",
      "COMMENT":  "Good"
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Project Name | `"PROJECT"` | String | - | Optional |
| 2 | Revision Info | `"REVISION"` | String | - | Optional |
| 3 | Username | `"USER"` | String | - | Optional |
| 4 | E-mail | `"EMAIL"` | String | - | Optional |
| 5 | Address | `"ADDRESS"` | String | - | Optional |
| 6 | Telephone Numbers | `"TEL"` | String | - | Optional |
| 7 | Fax Numbers | `"FAX"` | String | - | Optional |
| 8 | Client | `"CLIENT"` | String | - | Optional |
| 9 | Title | `"TITLE"` | String | - | Optional |
| 10 | Engineer (Review Name) | `"ENGINEER"` | String | - | Optional |
| 11 | Engineer Review Date | `"EDATE"` | String | - | Optional |
| 12 | Checker 1 Name | `"CHECK1"` | String | - | Optional |
| 13 | Checker 1 Date | `"CDATE1"` | String | - | Optional |
| 14 | Checker 2 Name | `"CHECK2"` | String | - | Optional |
| 15 | Checker 2 Date | `"CDATE2"` | String | - | Optional |
| 16 | Checker 3 Name | `"CHECK3"` | String | - | Optional |
| 17 | Checker 3 Date | `"CDATE3"` | String | - | Optional |
| 18 | Approver Name | `"APPROVE"` | String | - | Optional |
| 19 | Approver Date | `"ADATE"` | String | - | Optional |
| 20 | Comments | `"COMMENT"` | String | - | Optional |

> ✅ **2026-09-06 已确认解决：** 原文 Specifications 表第 18 项 Key 曾误写为 `"APROVE"`（1 个 P），
> 2026-09-01 原文更新后已更正为 `"APPROVE"`（2 个 P）（article id `35801869341337`，复核时
> `APPROVE` 出现 3 次·`APROVE` 出现 0 次）。我方文档从一开始就是正确写法，故表格未作修改。
> 应为采纳 2026-08-27 错误上报（Jira `MAPI-2484`）的结果。

### Python 示例

```python
# 设置项目信息
result = midas_api("POST", "/db/pjcf", {
    "Assign": {
        "1": {
            "PROJECT":  "My Building Project",
            "USER":     "Dennis",
            "CLIENT":   "ABC Corp",
            "TITLE":    "10-Story RC Frame",
            "ENGINEER": "Dennis",
            "EDATE":    "2026-06-29",
            "COMMENT":  "Initial modeling"
        }
    }
})

# 查询项目信息
result = midas_api("GET", "/db/pjcf")
print(result)
```

---

## 2. `/db/UNIT` — Unit System

> ⚠️ **新建文件的必需数据：** 仅支持 `GET` / `PUT`。

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/UNIT` |
| **Methods** | `GET`, `PUT` |
| **官方文档** | [Unit System ↗](https://support.midasuser.com/hc/en-us/articles/35802155483801) |

### JSON Schema

```json
{
  "UNIT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "FORCE":  { "description": "Force",       "type": "string" },
      "DIST":   { "description": "Distance",    "type": "string" },
      "HEAT":   { "description": "Heat",        "type": "string" },
      "TEMPER": { "description": "TemperUnit",  "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "FORCE":  "KN",
      "DIST":   "M",
      "HEAT":   "KJ",
      "TEMPER": "C"
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Force (Mass) · `"N"` / `"KN"` / `"KGF"` / `"TONF"` / `"LBF"` / `"KIPS"` | `"FORCE"` | String | - | Optional |
| 2 | Length · `"M"` / `"CM"` / `"MM"` / `"FT"` / `"IN"` | `"DIST"` | String | - | Optional |
| 3 | Heat · `"CAL"` / `"KCAL"` / `"J"` / `"KJ"` / `"BTU"` | `"HEAT"` | String | - | Optional |
| 4 | Temperature · `"C"` (Celsius) / `"F"` (Fahrenheit) | `"TEMPER"` | String | - | Optional |

#### Force 单位详情

| 值 | 力单位 | 质量单位 |
|----|---------|----------|
| `"N"` | N | kg |
| `"KN"` | kN | ton |
| `"KGF"` | kgf | kg |
| `"TONF"` | tonf | ton |
| `"LBF"` | lbf | lb |
| `"KIPS"` | kips | kips/g |

#### Length 单位详情

| 值 | 长度单位 |
|----|----------|
| `"M"` | m |
| `"CM"` | cm |
| `"MM"` | mm |
| `"FT"` | ft |
| `"IN"` | in |

### Python 示例

```python
# 设置单位（SI：kN, m — 韩国建筑结构基准）
result = midas_api("PUT", "/db/unit", {
    "Assign": {
        "1": {
            "FORCE":  "KN",
            "DIST":   "M",
            "HEAT":   "KJ",
            "TEMPER": "C"
        }
    }
})

# 设置单位（tonf, m — 台湾 RC 设计基准）
result = midas_api("PUT", "/db/unit", {
    "Assign": {
        "1": {
            "FORCE":  "TONF",
            "DIST":   "M",
            "HEAT":   "KCAL",
            "TEMPER": "C"
        }
    }
})

# 查询当前单位
result = midas_api("GET", "/db/unit")
print(result)
```

---

## 3. `/db/STYP` — Structure Type

> ⚠️ **新建文件的必需数据：** 仅支持 `GET` / `PUT`。

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/STYP` |
| **Methods** | `GET`, `PUT` |
| **官方文档** | [Structure Type ↗](https://support.midasuser.com/hc/en-us/articles/35802404495257) |

### JSON Schema

```json
{
  "STYP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "STYP":        { "description": "StructureType",            "type": "integer" },
      "MASS":        { "description": "MassType",                 "type": "integer" },
      "bMASSOFFSET": { "description": "ConsiderOffset",           "type": "boolean" },
      "bSELFWEIGHT": { "description": "ConvertSelfWeight",        "type": "boolean" },
      "SMASS":       { "description": "StructureMassType",        "type": "integer" },
      "GRAV":        { "description": "Gravity",                  "type": "number"  },
      "TEMP":        { "description": "InitialTemperature",       "type": "number"  },
      "bALIGNBEAM":  { "description": "AlignTopofBeamSection",    "type": "boolean" },
      "bALIGNSLAB":  { "description": "AlignTopofSlab(Plate)",    "type": "boolean" },
      "bROTRIGID":   { "description": "ConsideringRotationalRigid","type": "boolean" }
    }
  }
}
```

### Request Examples

**基本 3-D 结构（无自重转换）**

```json
{
  "Assign": {
    "1": {
      "STYP":        0,
      "MASS":        1,
      "bMASSOFFSET": false,
      "bSELFWEIGHT": false,
      "GRAV":        9.806,
      "TEMP":        0,
      "bALIGNBEAM":  false,
      "bALIGNSLAB":  false,
      "bROTRIGID":   false
    }
  }
}
```

**3-D 结构（自重 → 质量转换，考虑转动刚体）**

```json
{
  "Assign": {
    "1": {
      "STYP":        0,
      "MASS":        2,
      "bMASSOFFSET": false,
      "bSELFWEIGHT": true,
      "SMASS":       2,
      "GRAV":        9.806,
      "TEMP":        0,
      "bALIGNBEAM":  false,
      "bALIGNSLAB":  false,
      "bROTRIGID":   true
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Structure Type · `0`=3-D / `1`=X-Z Plane / `2`=Y-Z Plane / `3`=X-Y Plane / `4`=Constraint RZ | `"STYP"` | Integer | System | Optional |
| 2 | Mass Type · `1`=Lumped Mass / `2`=Consistent Mass | `"MASS"` | Integer | - | Optional |
| 3 | Consider Off-diagonal Masses | `"bMASSOFFSET"` | Boolean | `false` | Optional |
| 4 | Convert Self-Weight to Mass | `"bSELFWEIGHT"` | Boolean | `false` | Optional |
| 5 | Structure Mass Type (自重→质量转换时) · `1`=Convert to X,Y,Z / `2`=Convert to X,Y / `3`=Convert to Z | `"SMASS"` | Integer | `1` | Optional |
| 6 | Gravity Acceleration (m/s²) | `"GRAV"` | Number | System | Optional |
| 7 | Initial Temperature | `"TEMP"` | Number | 0 | Optional |
| 8 | Align Top of Beam Section | `"bALIGNBEAM"` | Boolean | `false` | Optional |
| 9 | Align Top of Slab (Plate) | `"bALIGNSLAB"` | Boolean | `false` | Optional |
| 10 | Considering Rotational Rigid | `"bROTRIGID"` | Boolean | `false` | Optional |

> ⚠️ **2026-08-25 复核更正：** `bMASSOFFSET`/`bSELFWEIGHT`/`bALIGNBEAM`/`bALIGNSLAB`/`bROTRIGID`
> 的默认值此前为 `-`（未记载），但原文 Specifications 表（article id `35802404495257`）中
> 均已明确标注为 `false`，故予以更正。`SMASS` 也已明确标注默认值 `1`，一并反映。

#### Structure Type (`STYP`) 详情

| 值 | 结构类型 |
|----|----------|
| `0` | 3-D（默认） |
| `1` | X-Z Plane |
| `2` | Y-Z Plane |
| `3` | X-Y Plane |
| `4` | Constraint RZ |

### Python 示例

```python
# 设置结构类型（3-D、Lumped Mass、无自重转换）
result = midas_api("PUT", "/db/styp", {
    "Assign": {
        "1": {
            "STYP":        0,       # 3-D
            "MASS":        1,       # Lumped Mass
            "bMASSOFFSET": False,
            "bSELFWEIGHT": False,
            "GRAV":        9.806,
            "TEMP":        0,
            "bALIGNBEAM":  False,
            "bALIGNSLAB":  False,
            "bROTRIGID":   False
        }
    }
})

# 查询当前结构类型
result = midas_api("GET", "/db/styp")
print(result)
```

---

## 4. `/db/STYP-M1` — Structure Type (Hyper-S)

> ⚠️ **仅 Hyper-S（MEC）求解器专用。** 该端点与经典 `/db/STYP` 分属不同的 article 与 schema。
> **Active Methods:** `GET`、`PUT`、`DELETE`（不支持 POST）。原文没有说明为何不含 POST，也没有说明
> DELETE 的实际行为（例如是重置为默认值，还是变为完全空的状态），因此无法确认 —
> 考虑到它与经典 `/db/UNIT`·`/db/STYP` 一样属于新建文件中必须存在的数据，这一组合颇为反常，
> 故建议在实际使用前先用 GET 确认响应。

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/STYP-M1` |
| **Methods** | `GET`, `PUT`, `DELETE` |
| **官方文档** | [Structure Type (Hyper-S) ↗](https://support.midasuser.com/hc/ko/articles/56375311138201) |

### JSON Schema

```json
{
  "STYP-M1": {
    "Assign": {
      "<ID>": {
        "STYPE": { "description": "Structure Type", "type": "string (enum)" },
        "MASS_CONTROL": {
          "description": "Mass Control Parameter (Required)",
          "type": "object",
          "properties": {
            "MASS_TYPE":  { "description": "Lumped Mass(LUMPED) / Consistent Mass(CONSISTENT)", "type": "string (enum)" },
            "MASS_POS":   { "description": "MASS_TYPE=LUMPED일 때 필수 — Centroid(CENTROID) / Offset(OFFSET). MASS_TYPE=CONSISTENT면 불가", "type": "string (enum)" },
            "SELFWEIGHT": { "description": "자중을 질량으로 변환할지 여부", "type": "boolean" },
            "MASS_AXIS":  { "description": "SELFWEIGHT=true일 때 필수 — XYZ / XY / Z (SELFWEIGHT=false면 불가. MASS_TYPE=CONSISTENT & SELFWEIGHT=true면 XYZ만 허용)", "type": "string (enum)" }
          }
        },
        "GRAV":      { "description": "Gravity Acceleration", "type": "number" },
        "TEMP":      { "description": "Initial Temperature", "type": "number" },
        "ALIGNBEAM": { "description": "Align Top of Beam Section with Center Line (X-Y Plane) for Display", "type": "boolean" },
        "ALIGNSLAB": { "description": "Align Top of Slab(Plate) Section with Center Line (X-Y Plane) for Display", "type": "boolean" }
      }
    }
  }
}
```

> ⚠️ 原文 JSON Schema 的 `STYPE` enum 定义为 `["_3D", "XZ", "YZ", "XY", "RZ"]`（含前导下划线），
> 但同一 article 的 Request Examples 与 Specifications 表都一致地标为 `"3D"`（无下划线）。
> 按本仓库原则（示例优先于表格），下方示例与表使用 `"3D"`。

### Request Examples

**Lumped Mass**

```json
{
  "Assign": {
    "1": {
      "STYPE": "3D",
      "MASS_CONTROL": {
        "MASS_TYPE": "LUMPED",
        "MASS_POS": "CENTROID",
        "SELFWEIGHT": true,
        "MASS_AXIS": "XYZ"
      },
      "GRAV": 9.806,
      "TEMP": 0,
      "ALIGNBEAM": false,
      "ALIGNSLAB": false
    }
  }
}
```

**Consistent Mass**

```json
{
  "Assign": {
    "1": {
      "STYPE": "3D",
      "MASS_CONTROL": {
        "MASS_TYPE": "CONSISTENT",
        "SELFWEIGHT": true,
        "MASS_AXIS": "XYZ"
      },
      "GRAV": 9.806,
      "TEMP": 0,
      "ALIGNBEAM": false,
      "ALIGNSLAB": false
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Structure Type · 3-D: `3D` / X-Z Plane: `XZ` / Y-Z Plane: `YZ` / X-Y Plane: `XY` / Constraint RZ: `RZ` | `"STYPE"` | String (enum) | `"3D"` | Optional |
| 2 | Mass Control Parameter | `"MASS_CONTROL"` | Object | – | Required |
| 2-(1) | └ Mass Type · Lumped Mass: `LUMPED` / Consistent Mass: `CONSISTENT` | `"MASS_TYPE"` | String (enum) | – | Required |
| 2-(2) | └ Mass Position (`MASS_TYPE="LUMPED"` 时) · Centroid: `CENTROID` / Offset: `OFFSET` | `"MASS_POS"` | String (enum) | – | 条件必填 |
| 2-(3) | └ Convert Self-weight into Masses | `"SELFWEIGHT"` | Boolean | – | Required |
| 2-(4) | └ Mass Axis (`SELFWEIGHT=true` 时) · X,Y,Z: `XYZ` / X,Y: `XY` / Z: `Z` (`MASS_TYPE="CONSISTENT"` 时仅允许 `XYZ`) | `"MASS_AXIS"` | String (enum) | – | 条件必填 |
| 3 | Gravity Acceleration | `"GRAV"` | Number | System | Optional |
| 4 | Initial Temperature | `"TEMP"` | Number | `0` | Optional |
| 5 | Align Top of Beam Section with Center Line (X-Y Plane) for Display | `"ALIGNBEAM"` | Boolean | `false` | Optional |
| 6 | Align Top of Slab(Plate) Section with Center Line (X-Y Plane) for Display | `"ALIGNSLAB"` | Boolean | `false` | Optional |

### Python 示例

```python
# 设置结构类型（Hyper-S、3-D、Lumped Mass、含自重转换）
payload = {
    "Assign": {
        "1": {
            "STYPE": "3D",
            "MASS_CONTROL": {
                "MASS_TYPE": "LUMPED",
                "MASS_POS": "CENTROID",
                "SELFWEIGHT": True,
                "MASS_AXIS": "XYZ"
            },
            "GRAV": 9.806,
            "TEMP": 0,
            "ALIGNBEAM": False,
            "ALIGNSLAB": False
        }
    }
}
result = midas_api("PUT", "/db/STYP-M1", payload)

# 查询当前结构类型（Hyper-S）
result = midas_api("GET", "/db/STYP-M1")
print(result)
```

---

## 5. `/db/GRUP` — Structure Group

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/GRUP` |
| **Methods** | `POST`, `GET`, `PUT` |
| **官方文档** | [Structure Group ↗](https://support.midasuser.com/hc/en-us/articles/35802441712921) |

### JSON Schema

```json
{
  "GRUP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":   { "description": "GroupName",    "type": "string" },
      "P_TYPE": { "description": "PlaneType",    "type": "integer" },
      "N_LIST": {
        "description": "NodeList",
        "type": "array",
        "items": { "type": "integer" }
      },
      "E_LIST": {
        "description": "ElementList",
        "type": "array",
        "items": { "type": "integer" }
      }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "NAME":   "CENTER_",
      "P_TYPE": 0,
      "N_LIST": [1, 2, 3, 4, 5],
      "E_LIST": [1, 2, 3, 4, 5]
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Structure Group Name | `"NAME"` | String | - | **Required** |
| 2 | Plane Type | `"P_TYPE"` | Integer | 0 | Optional |
| 3 | Node List | `"N_LIST"` | Array [Integer] | - | Optional |
| 4 | Element List | `"E_LIST"` | Array [Integer] | - | Optional |

### Python 示例

```python
# 创建结构组（含节点·单元）
result = midas_api("POST", "/db/grup", {
    "Assign": {
        "1": {
            "NAME":   "Column_Group",
            "P_TYPE": 0,
            "N_LIST": [1, 2, 3, 4],
            "E_LIST": [1, 2, 3, 4]
        },
        "2": {
            "NAME":   "Beam_Group",
            "P_TYPE": 0,
            "N_LIST": [5, 6, 7, 8],
            "E_LIST": [5, 6, 7, 8]
        }
    }
})

# 查询全部组
result = midas_api("GET", "/db/grup")
print(result)
```

---

## 6. `/db/BNGR` — Boundary Group

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/BNGR` |
| **Methods** | `POST`, `GET`, `PUT` |
| **官方文档** | [Boundary Group ↗](https://support.midasuser.com/hc/en-us/articles/35804937452313) |

### JSON Schema

```json
{
  "BNGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "BoundaryGroupName", "type": "string" },
      "AUTOTYPE": { "description": "AutoType",          "type": "integer" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": { "NAME": "fix1", "AUTOTYPE": 0 },
    "2": { "NAME": "fix2", "AUTOTYPE": 0 },
    "3": { "NAME": "fix3", "AUTOTYPE": 0 }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Boundary Group Name | `"NAME"` | String | - | **Required** |
| 2 | Auto-generated boundary groups for CR/SH in Composite Section ¹⁾ · `0`=Creep / `1`=Shrinkage | `"AUTOTYPE"` | Integer | Auto | Optional |

> ¹⁾ 组合截面（Composite Section）的徐变（Creep）/干燥收缩（Shrinkage）自动边界组

### Python 示例

```python
# 创建边界组
result = midas_api("POST", "/db/bngr", {
    "Assign": {
        "1": { "NAME": "Foundation_BG", "AUTOTYPE": 0 },
        "2": { "NAME": "Stage1_BG",     "AUTOTYPE": 0 }
    }
})
print(result)
```

---

## 7. `/db/LDGR` — Load Group

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/LDGR` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **官方文档** | [Load Group ↗](https://support.midasuser.com/hc/en-us/articles/35804975346841) |

### JSON Schema

```json
{
  "LDGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "LoadGroupName", "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": { "NAME": "SW" },
    "2": { "NAME": "WetConcrete" }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Group Name | `"NAME"` | String | - | **Required** |

### Python 示例

```python
# 创建荷载组
result = midas_api("POST", "/db/ldgr", {
    "Assign": {
        "1": { "NAME": "Dead_Load_Group" },
        "2": { "NAME": "Live_Load_Group" },
        "3": { "NAME": "Wind_Load_Group" }
    }
})

# 删除指定荷载组
result = midas_api("DELETE", "/db/ldgr", {
    "Assign": { "3": {} }
})
print(result)
```

---

## 8. `/db/TDGR` — Tendon Group

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/TDGR` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **官方文档** | [Tendon Group ↗](https://support.midasuser.com/hc/en-us/articles/35805198736793) |

### JSON Schema

```json
{
  "TDGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "Name", "type": "string" }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": { "NAME": "TGR1" },
    "2": { "NAME": "TGR2" }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Tendon Group Name | `"NAME"` | String | - | **Required** |

### Python 示例

```python
# 创建预应力束组（用于 PSC 桥梁等）
result = midas_api("POST", "/db/tdgr", {
    "Assign": {
        "1": { "NAME": "Tendon_Span1" },
        "2": { "NAME": "Tendon_Span2" }
    }
})
print(result)
```

---

## 9. `/db/NPLN` — Named Plane

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/NPLN` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **官方文档** | [Named Plane ↗](https://support.midasuser.com/hc/en-us/articles/35805287066649) |

### JSON Schema

```json
{
  "NPLN": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME": { "description": "PlaneName", "type": "string" },
      "TYPE": { "description": "PlaneType", "type": "integer" },
      "TOL":  { "description": "Tolerance", "type": "number" },
      "POINT": {
        "description": "Point",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ITEM": {
              "description": "PointItem",
              "type": "array",
              "items": { "type": "number" }
            }
          }
        }
      },
      "COORD": { "description": "Coord", "type": "number" }
    }
  }
}
```

### Request Example

```json
{
  "NPLN": {
    "1": {
      "NAME": "NP11",
      "TYPE": 1,
      "TOL":  1,
      "POINT": [
        { "ITEM": [0,     235,  0] },
        { "ITEM": [0,     9710, 0] },
        { "ITEM": [15250, 9710, 0] }
      ]
    },
    "2": {
      "NAME":  "NP12",
      "TYPE":  2,
      "TOL":   1,
      "COORD": -12000
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Plane Name | `"NAME"` | String | - | **Required** |
| 2 | Plane Type · `1`=3 Points / `2`=X-Y Plane / `3`=X-Z Plane / `4`=Y-Z Plane | `"TYPE"` | Integer | - | **Required** |
| 3 | Tolerance | `"TOL"` | Number | `0` | Optional |
| 4 | Point Data (TYPE=1 时) · 第1/2/3个点坐标 `[X, Y, Z]` | `"POINT"[].ITEM"` | Array [Number] | - | Required (TYPE=1) |
| 5 | Coordinate (TYPE=2,3,4 时) · Z/Y/X 位置 | `"COORD"` | Number | `0` | Optional |

> ⚠️ **2026-08-25 复核更正：** `TOL` 默认值 `-`→`0`；`COORD` 在原文 Specifications 表中
> 并非 Required，而是明确标注为 **Optional（默认值 0）**，故予以更正（article id `35805287066649`）。
> 该值仅在 TYPE=1 时不会被使用，因此实务上看似「条件必填」，但原文标注为 Optional。

#### Plane Type 详情

| 值 | 类型 | 所需数据 |
|----|------|------------|
| `1` | 3 Points | `POINT` (3个点的坐标) |
| `2` | X-Y Plane | `COORD` (Z 位置) |
| `3` | X-Z Plane | `COORD` (Y 位置) |
| `4` | Y-Z Plane | `COORD` (X 位置) |

### Python 示例

```python
# 由3个点定义的平面
result = midas_api("POST", "/db/npln", {
    "NPLN": {
        "1": {
            "NAME": "FloorPlane_1F",
            "TYPE": 2,       # X-Y Plane
            "TOL":  1,
            "COORD": 0       # Z = 0（1层楼面）
        },
        "2": {
            "NAME": "FloorPlane_2F",
            "TYPE": 2,
            "TOL":  1,
            "COORD": 3200    # Z = 3200mm（2层楼面）
        }
    }
})
print(result)
```

---

## 10. `/db/CO_M` — Material Color

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/CO_M` |
| **Methods** | `GET`, `PUT` |
| **官方文档** | [Material Color ↗](https://support.midasuser.com/hc/en-us/articles/35805703171353) |

### JSON Schema

```json
{
  "CO_M": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "W_R":    { "description": "WireFrameRed",    "type": "integer" },
      "W_G":    { "description": "WireFrameGreen",  "type": "integer" },
      "W_B":    { "description": "WireFrameBlue",   "type": "integer" },
      "HF_R":   { "description": "HiddenFillRed",   "type": "integer" },
      "HF_G":   { "description": "HiddenFillGreen", "type": "integer" },
      "HF_B":   { "description": "HiddenFillBlue",  "type": "integer" },
      "HE_R":   { "description": "HiddenEdgeRed",   "type": "integer" },
      "HE_G":   { "description": "HiddenEdgeGreen", "type": "integer" },
      "HE_B":   { "description": "HiddenEdgeBlue",  "type": "integer" },
      "bBLEMD": { "description": "OpacityBoolean",  "type": "boolean" },
      "FACT":   { "description": "OpacityValue",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "W_R": 131, "W_G": 131, "W_B": 131,
      "HF_R": 178, "HF_G": 178, "HF_B": 178,
      "HE_R": 131, "HE_G": 131, "HE_B": 131,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Wire Frame Red (0–255) | `"W_R"` | Integer | - | Optional |
| 2 | Wire Frame Green (0–255) | `"W_G"` | Integer | - | Optional |
| 3 | Wire Frame Blue (0–255) | `"W_B"` | Integer | - | Optional |
| 4 | Hidden Fill Red (0–255) | `"HF_R"` | Integer | - | Optional |
| 5 | Hidden Fill Green (0–255) | `"HF_G"` | Integer | - | Optional |
| 6 | Hidden Fill Blue (0–255) | `"HF_B"` | Integer | - | Optional |
| 7 | Hidden Edge Red (0–255) | `"HE_R"` | Integer | - | Optional |
| 8 | Hidden Edge Green (0–255) | `"HE_G"` | Integer | - | Optional |
| 9 | Hidden Edge Blue (0–255) | `"HE_B"` | Integer | - | Optional |
| 10 | Opacity Boolean | `"bBLEMD"` | Boolean | - | Optional |
| 11 | Opacity Value (0.0–1.0) | `"FACT"` | Number | - | Optional |

### Python 示例

```python
# 设置材料颜色（材料 ID 1号 = 灰色系）
result = midas_api("PUT", "/db/co_m", {
    "Assign": {
        "1": {
            "W_R": 131, "W_G": 131, "W_B": 131,
            "HF_R": 178, "HF_G": 178, "HF_B": 178,
            "HE_R": 131, "HE_G": 131, "HE_B": 131,
            "bBLEMD": False,
            "FACT": 0.5
        }
    }
})
print(result)
```

---

## 11. `/db/CO_S` — Section Color

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/CO_S` |
| **Methods** | `GET`, `PUT` |
| **官方文档** | [Section Color ↗](https://support.midasuser.com/hc/en-us/articles/35805763514393) |

### JSON Schema

```json
{
  "CO_S": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "W_R":    { "description": "WireFrameRed",    "type": "integer" },
      "W_G":    { "description": "WireFrameGreen",  "type": "integer" },
      "W_B":    { "description": "WireFrameBlue",   "type": "integer" },
      "HF_R":   { "description": "HiddenFillRed",   "type": "integer" },
      "HF_G":   { "description": "HiddenFillGreen", "type": "integer" },
      "HF_B":   { "description": "HiddenFillBlue",  "type": "integer" },
      "HE_R":   { "description": "HiddenEdgeRed",   "type": "integer" },
      "HE_G":   { "description": "HiddenEdgeGreen", "type": "integer" },
      "HE_B":   { "description": "HiddenEdgeBlue",  "type": "integer" },
      "bBLEMD": { "description": "OpacityBoolean",  "type": "boolean" },
      "FACT":   { "description": "OpacityValue",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "2": {
      "W_R": 111, "W_G": 142, "W_B": 91,
      "HF_R": 159, "HF_G": 205, "HF_B": 131,
      "HE_R": 111, "HE_G": 142, "HE_B": 91,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```

### Specifications

与 CO_M 相同的字段结构（键名相同）。按 Section ID 指定颜色。

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1–9 | Wire Frame / Hidden Fill / Hidden Edge RGB (0–255) | `"W_R"` ~ `"HE_B"` | Integer | - | Optional |
| 10 | Opacity Boolean | `"bBLEMD"` | Boolean | - | Optional |
| 11 | Opacity Value (0.0–1.0) | `"FACT"` | Number | - | Optional |

### Python 示例

```python
# 设置截面颜色（截面 ID 2号 = 绿色系）
result = midas_api("PUT", "/db/co_s", {
    "Assign": {
        "2": {
            "W_R": 111, "W_G": 142, "W_B": 91,
            "HF_R": 159, "HF_G": 205, "HF_B": 131,
            "HE_R": 111, "HE_G": 142, "HE_B": 91,
            "bBLEMD": False,
            "FACT": 0.5
        }
    }
})
print(result)
```

---

## 12. `/db/CO_T` — Thickness Color

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/CO_T` |
| **Methods** | `GET`, `PUT` |
| **官方文档** | [Thickness Color ↗](https://support.midasuser.com/hc/en-us/articles/35805833925785) |

### JSON Schema

与 CO_M、CO_S 相同的字段结构。

```json
{
  "CO_T": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "W_R":    { "description": "WireFrameRed",    "type": "integer" },
      "W_G":    { "description": "WireFrameGreen",  "type": "integer" },
      "W_B":    { "description": "WireFrameBlue",   "type": "integer" },
      "HF_R":   { "description": "HiddenFillRed",   "type": "integer" },
      "HF_G":   { "description": "HiddenFillGreen", "type": "integer" },
      "HF_B":   { "description": "HiddenFillBlue",  "type": "integer" },
      "HE_R":   { "description": "HiddenEdgeRed",   "type": "integer" },
      "HE_G":   { "description": "HiddenEdgeGreen", "type": "integer" },
      "HE_B":   { "description": "HiddenEdgeBlue",  "type": "integer" },
      "bBLEMD": { "description": "OpacityBoolean",  "type": "boolean" },
      "FACT":   { "description": "OpacityValue",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "W_R": 111, "W_G": 142, "W_B": 91,
      "HF_R": 159, "HF_G": 205, "HF_B": 131,
      "HE_R": 111, "HE_G": 142, "HE_B": 91,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1–9 | Wire Frame / Hidden Fill / Hidden Edge RGB (0–255) | `"W_R"` ~ `"HE_B"` | Integer | - | Optional |
| 10 | Opacity Boolean | `"bBLEMD"` | Boolean | - | Optional |
| 11 | Opacity Value (0.0–1.0) | `"FACT"` | Number | - | Optional |

### Python 示例

```python
# 设置厚度颜色（厚度 ID 1号）
result = midas_api("PUT", "/db/co_t", {
    "Assign": {
        "1": {
            "W_R": 111, "W_G": 142, "W_B": 91,
            "HF_R": 159, "HF_G": 205, "HF_B": 131,
            "HE_R": 111, "HE_G": 142, "HE_B": 91,
            "bBLEMD": False, "FACT": 0.5
        }
    }
})
print(result)
```

---

## 13. `/db/CO_F` — Floor Load Color

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/CO_F` |
| **Methods** | `GET`, `PUT` |
| **官方文档** | [Floor Load Color ↗](https://support.midasuser.com/hc/en-us/articles/35805846236441) |

### JSON Schema

```json
{
  "CO_F": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":         { "description": "FloorLoadTypeName", "type": "string"  },
      "WF_R":         { "description": "WireFrame_Red",     "type": "integer" },
      "WF_G":         { "description": "WireFrame_Green",   "type": "integer" },
      "WF_B":         { "description": "WireFrame_Blue",    "type": "integer" },
      "HF_R":         { "description": "HiddenFill_Red",    "type": "integer" },
      "HF_G":         { "description": "HiddenFill_Green",  "type": "integer" },
      "HF_B":         { "description": "HiddenFill_Blue",   "type": "integer" },
      "HE_R":         { "description": "HiddenEdge_Red",    "type": "integer" },
      "HE_G":         { "description": "HiddenEdge_Green",  "type": "integer" },
      "HE_B":         { "description": "HiddenEdge_Blue",   "type": "integer" },
      "OPT_BLEND":    { "description": "Blending",          "type": "boolean" },
      "BLEND_FACTOR": { "description": "BlendingFactor",    "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "NAME": "FL",
      "WF_R": 166, "WF_G": 202, "WF_B": 240,
      "HF_R": 166, "HF_G": 202, "HF_B": 240,
      "HE_R": 166, "HE_G": 202, "HE_B": 240,
      "OPT_BLEND":    true,
      "BLEND_FACTOR": 0.25
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Floor Load Type Name | `"NAME"` | String | - | **Required** |
| 2 | Wire Frame Red (0–255) | `"WF_R"` | Integer | - | Optional |
| 3 | Wire Frame Green (0–255) | `"WF_G"` | Integer | - | Optional |
| 4 | Wire Frame Blue (0–255) | `"WF_B"` | Integer | - | Optional |
| 5 | Hidden Fill Red (0–255) | `"HF_R"` | Integer | - | Optional |
| 6 | Hidden Fill Green (0–255) | `"HF_G"` | Integer | - | Optional |
| 7 | Hidden Fill Blue (0–255) | `"HF_B"` | Integer | - | Optional |
| 8 | Hidden Edge Red (0–255) | `"HE_R"` | Integer | - | Optional |
| 9 | Hidden Edge Green (0–255) | `"HE_G"` | Integer | - | Optional |
| 10 | Hidden Edge Blue (0–255) | `"HE_B"` | Integer | - | Optional |
| 11 | Blending | `"OPT_BLEND"` | Boolean | - | Optional |
| 12 | Blending Factor (0.0–1.0) | `"BLEND_FACTOR"` | Number | - | Optional |

### Python 示例

```python
# 设置楼面荷载类型颜色
result = midas_api("PUT", "/db/co_f", {
    "Assign": {
        "1": {
            "NAME": "Residential_Floor",
            "WF_R": 166, "WF_G": 202, "WF_B": 240,
            "HF_R": 166, "HF_G": 202, "HF_B": 240,
            "HE_R": 166, "HE_G": 202, "HE_B": 240,
            "OPT_BLEND": True,
            "BLEND_FACTOR": 0.25
        }
    }
})
print(result)
```

---

## 14. `/db/SPAN` — Span Information

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/SPAN` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **官方文档** | [Span Information ↗](https://support.midasuser.com/hc/en-us/articles/35805957502233) |

### JSON Schema

```json
{
  "SPAN": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Name",       "type": "string"  },
      "bEXACTSPAN": { "description": "bExactSpan", "type": "boolean" },
      "DIRECTION":  { "description": "nDirection", "type": "integer" },
      "SECTTYPE":   { "description": "nSectType",  "type": "integer" },
      "SPAN_LIST":  {
        "description": "Span",
        "type": "array",
        "items": { "type": "number" }
      },
      "SPAN_BASE_ITEMS": {
        "description": "SpanBaseItems",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "ELEM_KEY": { "description": "Element", "type": "integer" },
            "SUPPORT":  { "description": "Support", "type": "integer" }
          }
        }
      }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "NAME":       "s1",
      "bEXACTSPAN": true,
      "DIRECTION":  0,
      "SECTTYPE":   0,
      "SPAN_LIST":  [2.5, 5, 32.5],
      "SPAN_BASE_ITEMS": [
        { "ELEM_KEY": 1,  "SUPPORT": 1 },
        { "ELEM_KEY": 2,  "SUPPORT": 1 },
        { "ELEM_KEY": 3,  "SUPPORT": 2 },
        { "ELEM_KEY": 4,  "SUPPORT": 0 }
      ]
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Span Name | `"NAME"` | String | - | **Required** |
| 2 | Exact Span Option | `"bEXACTSPAN"` | Boolean | - | **Required** |
| 3 | Inner Direction of Multiple Girders · `0`=(-) Local y / `1`=(+) Local y / `2`=Both / `3`=None | `"DIRECTION"` | Integer | - | **Required** |
| 4 | Assign Elements · `0`=By Selection / `1`=Number | `"SECTTYPE"` | Integer | - | **Required** |
| 5 | Span List (bEXACTSPAN=true 时) | `"SPAN_LIST"` | Array [Number] | - | Required (bEXACTSPAN=true) |
| 6 | Span Base Items (bEXACTSPAN=true 时) · Element Key | `"SPAN_BASE_ITEMS"[].ELEM_KEY"` | Integer | - | Required (bEXACTSPAN=true) |
| 7 | Span Base Items · Support type · `0`=None / `1`=Start / `2`=End | `"SPAN_BASE_ITEMS"[].SUPPORT"` | Integer | - | Required (bEXACTSPAN=true) |

### Python 示例

```python
# 设置跨信息（桥梁等）
result = midas_api("POST", "/db/span", {
    "Assign": {
        "1": {
            "NAME":       "Main_Span",
            "bEXACTSPAN": True,
            "DIRECTION":  0,
            "SECTTYPE":   0,
            "SPAN_LIST":  [40.0, 60.0, 40.0],
            "SPAN_BASE_ITEMS": [
                {"ELEM_KEY": 1, "SUPPORT": 1},
                {"ELEM_KEY": 5, "SUPPORT": 2},
            ]
        }
    }
})
print(result)
```

---

## 15. `/db/STOR` — Story Data

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/db/STOR` |
| **Methods** | `POST`, `GET`, `PUT`, `DELETE` |
| **官方文档** | [Story Data ↗](https://support.midasuser.com/hc/en-us/articles/49513466793113) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "STORY_NAME":               { "description": "StoryName",                            "type": "string"  },
      "STORY_LEVEL":              { "description": "StoryLevel",                           "type": "number"  },
      "bFLOOR_DIAPHRAGM":         { "description": "FloorDiaphragm",                      "type": "boolean" },
      "WIND_FLOOR_WIDTH_X":       { "description": "WindFloorWidthX-Dir",                 "type": "number"  },
      "WIND_FLOOR_WIDTH_Y":       { "description": "WindFloorWidthY-Dir",                 "type": "number"  },
      "WIND_CENTER_X":            { "description": "WindFloorCenterXc",                   "type": "number"  },
      "WIND_CENTER_Y":            { "description": "WindFloorCenterYc",                   "type": "number"  },
      "WIND_ECCENT_X":            { "description": "WindEccentricityX-Dir",               "type": "number"  },
      "WIND_ECCENT_Y":            { "description": "WindEccentricityY-Dir",               "type": "number"  },
      "SEIS_ACC_ECCENT_X":        { "description": "SeismicAccidentalEccentricityX-Dir",  "type": "number"  },
      "SEIS_ACC_ECCENT_Y":        { "description": "SeismicAccidentalEccentricityY-Dir",  "type": "number"  },
      "SEIS_INHERENT_ECCENT_X":   { "description": "SeismicInherentEccentricityX-Dir",    "type": "number"  },
      "SEIS_INHERENT_ECCENT_Y":   { "description": "SeismicInherentEccentricityY-Dir",    "type": "number"  },
      "SEIS_TORSIONAL_AMP_FACTOR_X": { "description": "SeismicTorsionalAmpFactorX-Dir",  "type": "number"  },
      "SEIS_TORSIONAL_AMP_FACTOR_Y": { "description": "SeismicTorsionalAmpFactorY-Dir",  "type": "number"  }
    }
  }
}
```

### Request Example

```json
{
  "Assign": {
    "1": {
      "STORY_NAME":               "1F",
      "STORY_LEVEL":              0,
      "bFLOOR_DIAPHRAGM":         false,
      "WIND_FLOOR_WIDTH_X":       36,
      "WIND_FLOOR_WIDTH_Y":       27.6,
      "WIND_CENTER_X":            18,
      "WIND_CENTER_Y":            13.8,
      "WIND_ECCENT_X":            5.4,
      "WIND_ECCENT_Y":            4.14,
      "SEIS_ACC_ECCENT_X":        1.8,
      "SEIS_ACC_ECCENT_Y":        1.38,
      "SEIS_INHERENT_ECCENT_X":   0,
      "SEIS_INHERENT_ECCENT_Y":   0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "2": {
      "STORY_NAME":               "2F",
      "STORY_LEVEL":              5,
      "bFLOOR_DIAPHRAGM":         true,
      "WIND_FLOOR_WIDTH_X":       36,
      "WIND_FLOOR_WIDTH_Y":       29.1,
      "WIND_CENTER_X":            18,
      "WIND_CENTER_Y":            14.55,
      "WIND_ECCENT_X":            5.4,
      "WIND_ECCENT_Y":            4.365,
      "SEIS_ACC_ECCENT_X":        1.8,
      "SEIS_ACC_ECCENT_Y":        1.455,
      "SEIS_INHERENT_ECCENT_X":   0,
      "SEIS_INHERENT_ECCENT_Y":   0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Story Name | `"STORY_NAME"` | String | - | **Required** |
| 2 | Story Height (elevation) | `"STORY_LEVEL"` | Number | - | **Required** |
| 3 | Floor Diaphragm (是否假定刚性隔板) | `"bFLOOR_DIAPHRAGM"` | Boolean | false | **Required** |
| 4 | Wind Floor Width X-Dir (GCS 中承受 Y 方向风荷载暴露的 X 轴宽度) | `"WIND_FLOOR_WIDTH_X"` | Number | - | Required |
| 5 | Wind Floor Width Y-Dir (GCS 中承受 X 方向风荷载暴露的 Y 轴宽度) | `"WIND_FLOOR_WIDTH_Y"` | Number | - | Required |
| 6 | Wind Floor Center Xc | `"WIND_CENTER_X"` | Number | - | Required |
| 7 | Wind Floor Center Yc | `"WIND_CENTER_Y"` | Number | - | Required |
| 8 | Wind Eccentricity X-Dir | `"WIND_ECCENT_X"` | Number | - | Required |
| 9 | Wind Eccentricity Y-Dir | `"WIND_ECCENT_Y"` | Number | - | Required |
| 10 | Seismic Accidental Eccentricity X-Dir | `"SEIS_ACC_ECCENT_X"` | Number | - | Required |
| 11 | Seismic Accidental Eccentricity Y-Dir | `"SEIS_ACC_ECCENT_Y"` | Number | - | Required |
| 12 | Seismic Inherent Eccentricity X-Dir | `"SEIS_INHERENT_ECCENT_X"` | Number | - | Required |
| 13 | Seismic Inherent Eccentricity Y-Dir | `"SEIS_INHERENT_ECCENT_Y"` | Number | - | Required |
| 14 | Seismic Torsional Amplification Factor X-Dir | `"SEIS_TORSIONAL_AMP_FACTOR_X"` | Number | - | Required |
| 15 | Seismic Torsional Amplification Factor Y-Dir | `"SEIS_TORSIONAL_AMP_FACTOR_Y"` | Number | - | Required |

### Python 示例 — 多层建筑楼层数据自动生成

```python
def create_story_data(story_heights: list, floor_width_x: float, floor_width_y: float,
                       eccentricity_ratio: float = 0.05) -> dict:
    """
    自动生成多层建筑的楼层数据。

    Args:
        story_heights  : 各楼层的绝对高度（elevation）列表。例：[0, 4, 8, 12]
        floor_width_x  : 楼板 X 方向宽度 (m)
        floor_width_y  : 楼板 Y 方向宽度 (m)
        eccentricity_ratio: 偏心率（默认 5%）

    Returns:
        dict: 传递给 /db/STOR 的 Assign 字典
    """
    story_names = ["B1F", "1F"] + [f"{i}F" for i in range(2, len(story_heights))]
    story_names[-1] = "Roof"

    assign = {}
    for i, (name, level) in enumerate(zip(story_names, story_heights), start=1):
        eccent_x = floor_width_x * eccentricity_ratio
        eccent_y = floor_width_y * eccentricity_ratio
        assign[str(i)] = {
            "STORY_NAME":               name,
            "STORY_LEVEL":              level,
            "bFLOOR_DIAPHRAGM":         (i > 1),   # 自地面层起施加刚性隔板
            "WIND_FLOOR_WIDTH_X":       floor_width_x,
            "WIND_FLOOR_WIDTH_Y":       floor_width_y,
            "WIND_CENTER_X":            floor_width_x / 2,
            "WIND_CENTER_Y":            floor_width_y / 2,
            "WIND_ECCENT_X":            eccent_x,
            "WIND_ECCENT_Y":            eccent_y,
            "SEIS_ACC_ECCENT_X":        eccent_x * 0.333,
            "SEIS_ACC_ECCENT_Y":        eccent_y * 0.333,
            "SEIS_INHERENT_ECCENT_X":   0,
            "SEIS_INHERENT_ECCENT_Y":   0,
            "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
            "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
        }
    return assign


# 10层建筑（层高 4m），楼板 36m × 27.6m
story_heights = [i * 4 for i in range(11)]  # [0, 4, 8, ..., 40]
story_heights[0] = 0  # 1F = GL

assign_data = create_story_data(
    story_heights=story_heights,
    floor_width_x=36.0,
    floor_width_y=27.6
)
result = midas_api("POST", "/db/stor", {"Assign": assign_data})
print(result)
```

---

## 完整项目初始设置工作流

```python
import requests, os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{res.status_code}] {method.upper()} {endpoint}")
    return res.json() if res.text else {}


# ── Step 1: 新建项目 ──────────────────────────────────
midas_api("POST", "/doc/new", {"Argument": {}})

# ── Step 2: 设置单位（kN, m）───────────────────────────
midas_api("PUT", "/db/unit", {
    "Assign": {"1": {"FORCE": "KN", "DIST": "M", "HEAT": "KJ", "TEMPER": "C"}}
})

# ── Step 3: 结构类型（3-D, Lumped Mass）────────────────
midas_api("PUT", "/db/styp", {
    "Assign": {"1": {
        "STYP": 0, "MASS": 1, "bMASSOFFSET": False,
        "bSELFWEIGHT": False, "GRAV": 9.806, "TEMP": 0,
        "bALIGNBEAM": False, "bALIGNSLAB": False, "bROTRIGID": False
    }}
})

# ── Step 4: 项目信息 ───────────────────────────────
midas_api("POST", "/db/pjcf", {
    "Assign": {"1": {
        "PROJECT": "10F RC Frame", "USER": "Dennis",
        "CLIENT": "ABC Corp", "TITLE": "Structural Analysis"
    }}
})

# ── Step 5: 楼层数据（10层 @ 4m）──────────────────────
story_names = [f"{i}F" for i in range(1, 11)] + ["Roof"]
assign = {}
for i, name in enumerate(story_names, start=1):
    assign[str(i)] = {
        "STORY_NAME": name, "STORY_LEVEL": (i - 1) * 4,
        "bFLOOR_DIAPHRAGM": (i > 1),
        "WIND_FLOOR_WIDTH_X": 36, "WIND_FLOOR_WIDTH_Y": 27.6,
        "WIND_CENTER_X": 18, "WIND_CENTER_Y": 13.8,
        "WIND_ECCENT_X": 1.8, "WIND_ECCENT_Y": 1.38,
        "SEIS_ACC_ECCENT_X": 1.8, "SEIS_ACC_ECCENT_Y": 1.38,
        "SEIS_INHERENT_ECCENT_X": 0, "SEIS_INHERENT_ECCENT_Y": 0,
        "SEIS_TORSIONAL_AMP_FACTOR_X": 1, "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    }
midas_api("POST", "/db/stor", {"Assign": assign})

# ── Step 6: 保存 ─────────────────────────────────────────
midas_api("POST", "/doc/save", {"Argument": {}})
```

---

## 相关文档

- [INDEX.md](./INDEX.md) — 全部 Endpoint 目录
- [01_DOC.md](./01_DOC.md) — 文档管理
- [03_DB_Node_Element.md](./03_DB_Node_Element.md) — 节点·单元
- [MIDAS API Online Manual (官方)](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)
