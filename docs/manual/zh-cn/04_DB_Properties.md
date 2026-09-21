# 04 DB — Properties

> **Source**: [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **Sync date**: 2026-07-12  
> **Endpoints covered**: `/db/MATL`, `/db/MATL-M1`, `/db/IMFM`, `/db/IMFM-M1`, `/db/TDMF`, `/db/TDMT`, `/db/TDME`, `/db/EDMP`, `/db/TMAT`, `/db/EPMT`, `/db/EPMT-M1`, `/db/SECT`, `/db/THIK`, `/db/TSGR`, `/db/SECF`, `/db/RPSC`, `/db/STRPSSM`, `/db/PSSF`, `/db/VBEM`, `/db/VSEC`, `/db/EWSF`, `/db/IEHC`, `/db/IEHG`, `/db/IEHG-BEAM-M1`, `/db/IEHG-TRUSS-M1`, `/db/IEHG-GL-M1`, `/db/IEHG-PSS-M1`, `/db/FIMP`, `/db/FIBR`, `/db/GRDP`, `/db/ESSF`, `/db/MATD`

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../04_DB_Properties.md) · **原文同步日期：** 2026-07-12  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## Table of Contents

| No. | Endpoint | 功能 | Methods |
|-----|----------|------|---------|
| 1 | [`/db/MATL`](#1-dbmatl) | Material Properties | POST, GET, PUT, DELETE |
| 2 | [`/db/MATL-M1`](#2-dbmatl-m1) | Material Properties (Hyper-S) | POST, GET, PUT, DELETE |
| 3 | [`/db/IMFM`](#3-dbimfm) | Inelastic Material Props for Fiber Model | POST, GET, PUT, DELETE |
| 4 | [`/db/IMFM-M1`](#4-dbimfm-m1) | Inelastic Material Link for Auto Generation (Hyper-S) | POST, GET, PUT, DELETE |
| 5 | [`/db/TDMF`](#5-dbtdmf) | Time Dependent Material – User Defined | POST, GET, PUT, DELETE |
| 6 | [`/db/TDMT`](#6-dbtdmt) | Time Dependent Material – Creep/Shrinkage | POST, GET, PUT, DELETE |
| 7 | [`/db/TDME`](#7-dbtdme) | Time Dependent Material – Compressive Strength | POST, GET, PUT, DELETE |
| 8 | [`/db/EDMP`](#8-dbedmp) | Change Property | POST, GET, PUT, DELETE |
| 9 | [`/db/TMAT`](#9-dbtmat) | Time Dependent Material Link | POST, GET, PUT, DELETE |
| 10 | [`/db/EPMT`](#10-dbepmt) | Plastic Material | POST, GET, PUT, DELETE |
| 11 | [`/db/EPMT-M1`](#11-dbepmt-m1) | Plastic Material (Hyper-S) | POST, GET, PUT, DELETE |
| 12 | [`/db/SECT`](#12-dbsect) | Section Properties | POST, GET, PUT, DELETE |
| 13 | [`/db/THIK`](#13-dbthik) | Thickness | POST, GET, PUT, DELETE |
| 14 | [`/db/TSGR`](#14-dbtsgr) | Tapered Group | POST, GET, PUT, DELETE |
| 15 | [`/db/SECF`](#15-dbsecf) | Section Manager – Stiffness | POST, GET, PUT, DELETE |
| 16 | [`/db/RPSC`](#16-dbrpsc) | Section Manager – Reinforcements | POST, GET, PUT, DELETE |
| 17 | [`/db/STRPSSM`](#17-dbstrpssm) | Section Manager – Stress Points | POST, GET, PUT, DELETE |
| 18 | [`/db/PSSF`](#18-dbpssf) | Section Manager – Plate Stiffness Scale Factor | POST, GET, PUT, DELETE |
| 19 | [`/db/VBEM`](#19-dbvbem) | Virtual Beam | POST, GET, PUT, DELETE |
| 20 | [`/db/VSEC`](#20-dbvsec) | Virtual Section | POST, GET, PUT, DELETE |
| 21 | [`/db/EWSF`](#21-dbewsf) | Effective Width Scale Factor | POST, GET, PUT, DELETE |
| 22 | [`/db/IEHC`](#22-dbiehc) | Inelastic Hinge Control Data | POST, GET, PUT, DELETE |
| 23 | [`/db/IEHG`](#23-dbiehg) | Assign Inelastic Hinge Properties | POST, GET, PUT, DELETE |
| 24 | [`/db/IEHG-BEAM-M1`](#24-dbiehg-beam-m1) | Assign Inelastic Hinges – Beam (Hyper-S) | POST, GET, PUT, DELETE |
| 25 | [`/db/IEHG-TRUSS-M1`](#25-dbiehg-truss-m1) | Assign Inelastic Hinges – Truss (Hyper-S) | POST, GET, PUT, DELETE |
| 26 | [`/db/IEHG-GL-M1`](#26-dbiehg-gl-m1) | Assign Inelastic Hinges – General Link (Hyper-S) | POST, GET, PUT, DELETE |
| 27 | [`/db/IEHG-PSS-M1`](#27-dbiehg-pss-m1) | Assign Inelastic Hinges – Point Spring (Hyper-S) | POST, GET, PUT, DELETE |
| 28 | [`/db/FIMP`](#28-dbfimp) | Inelastic Material Properties | POST, GET, PUT, DELETE |
| 29 | [`/db/FIBR`](#29-dbfibr) | Fiber Division of Section | POST, GET, PUT, DELETE |
| 30 | [`/db/GRDP`](#30-dbgrdp) | Group Damping | POST, GET, PUT, DELETE |
| 31 | [`/db/ESSF`](#31-dbessf) | Element Stiffness Scale Factor | POST, GET, PUT, DELETE |
| 32 | [`/db/MATD`](#32-dbmatd) | Modify Concrete Materials | GET, PUT |

---

## 通用设置

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/db/MATL`

> **Material Properties** — 定义材料特性。支持 DB（标准）、Isotropic（各向同性）、Orthotropic（正交各向异性）3种类型。

- **URL**: `{base url}/db/MATL`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Material Properties ↗](https://support.midasuser.com/hc/en-us/articles/35807411331993)

### JSON Schema

```json
{
  "MATL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE":       { "description": "Material Type",    "type": "string" },
      "NAME":       { "description": "Material Name",   "type": "string" },
      "HE_SPEC":    { "description": "Specific Heat",   "type": "number" },
      "HE_COND":    { "description": "Heat Conduction", "type": "number" },
      "PLMT":       { "description": "Plasticity Key",  "type": "integer" },
      "P_NAME":     { "description": "Plasticity Name", "type": "string" },
      "bMASS_DENS": { "description": "Use Mass Density","type": "boolean" },
      "DAMP_RAT":   { "description": "Damping Ratio",   "type": "number" },
      "PARAM":      { "description": "Material Data",   "type": "array" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Type • Concrete: `"CONC"` • Steel: `"STEEL"` • SRC: `"SRC"` • Aluminum: `"ALUMINUM"` • User Defined: `"USER"` | `"TYPE"` | String | - | **Required** |
| 2 | Material Name | `"NAME"` | String | - | **Required** |
| 3 | Specific Heat | `"HE_SPEC"` | Number | 0 | Optional |
| 4 | Heat Conduction | `"HE_COND"` | Number | 0 | Optional |
| 5 | Plastic Material No. | `"PLMT"` | Integer | 0 | Optional |
| 6 | Plastic Material Name | `"P_NAME"` | String | Blank | Optional |
| 7 | Use Mass Density | `"bMASS_DENS"` | Boolean | false | Optional |
| 8 | Damping Ratio | `"DAMP_RAT"` | Number | 0 | Optional |
| 9 | Material Parameter | `"PARAM"` | Object | - | **Required** |
| (1) | Material Parameter Type • Standard: 1 • Isotropic: 2 • Orthotropic: 3 | `"P_TYPE"` | Integer | - | **Required** |

#### PARAM — P_TYPE = 1 (Standard / DB)

| Sub-No. | Description | Key | Value Type | Default | Required |
|---------|-------------|-----|------------|---------|----------|
| (2) | Standard Name | `"STANDARD"` | String | - | **Required** |
| (3) | Code Name | `"CODE"` | String | Blank | Optional |
| (4) | DB Name | `"DB"` | String | - | **Required** |
| (5) | Use Young's Modulus (User Option) | `"bELAST"` | Boolean | false | Optional |

#### PARAM — P_TYPE = 2 (Isotropic / User)

| Sub-No. | Description | Key | Value Type | Default | Required |
|---------|-------------|-----|------------|---------|----------|
| (2) | Modulus of Elasticity | `"ELAST"` | Number | - | **Required** |
| (3) | Poisson's Ratio | `"POISN"` | Number | - | **Required** |
| (4) | Thermal Coefficient | `"THERMAL"` | Number | - | **Required** |
| (5) | Weight Density | `"DEN"` | Number | - | **Required** |
| (6) | Mass Density | `"MASS"` | Number | - | **Required** |

#### PARAM — P_TYPE = 3 (Orthotropic / User)

| Sub-No. | Description | Key | Value Type | Default | Required |
|---------|-------------|-----|------------|---------|----------|
| (2) | Modulus of Elasticity (3 values) | `"ELAST_M"` | Array[Number] | - | **Required** |
| (3) | Poisson's Ratio (3 values) | `"POISN_M"` | Array[Number] | - | **Required** |
| (4) | Thermal Coefficient (3 values) | `"THERMAL_M"` | Array[Number] | - | **Required** |
| (5) | Shear Modulus (3 values) | `"SHEAR_M"` | Array[Number] | - | **Required** |
| (6) | Weight Density | `"DEN"` | Number | - | **Required** |
| (7) | Mass Density | `"MASS"` | Number | - | **Required** |

### Request Body 示例

#### Standard DB 材料（Steel + Concrete）

```json
{
  "Assign": {
    "1": {
      "TYPE": "STEEL",
      "NAME": "DB_Steel",
      "HE_SPEC": 0, "HE_COND": 0,
      "PLMT": 0, "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.02,
      "PARAM": [{ "P_TYPE": 1, "STANDARD": "EN05(S)", "CODE": "", "DB": "S450", "bELAST": false }]
    },
    "2": {
      "TYPE": "CONC",
      "NAME": "DB_Conc",
      "HE_SPEC": 0, "HE_COND": 0,
      "PLMT": 0, "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.05,
      "PARAM": [{ "P_TYPE": 1, "STANDARD": "KS21(RC)", "CODE": "", "DB": "C24", "bELAST": false }]
    }
  }
}
```

#### Isotropic User 材料

```json
{
  "Assign": {
    "5": {
      "TYPE": "USER",
      "NAME": "User_Steel",
      "HE_SPEC": 0, "HE_COND": 0,
      "PLMT": 0, "P_NAME": "",
      "bMASS_DENS": true,
      "DAMP_RAT": 0,
      "PARAM": [{
        "P_TYPE": 2,
        "ELAST": 205000000,
        "POISN": 0.3,
        "THERMAL": 6.667e-06,
        "DEN": 76.98,
        "MASS": 7.85
      }]
    }
  }
}
```

### Python 示例

```python
# --- GET：查询全部材料 ---
result = midas_api("GET", "/db/MATL")
materials = result.get("MATL", {})
print(f"定义的材料数量：{len(materials)}")
for mid, m in materials.items():
    print(f"  {mid}: {m['NAME']} ({m['TYPE']})")

# --- POST：创建 DB 材料（KS 混凝土 + 钢材） ---
matl_data = {
    "Assign": {
        "1": {
            "TYPE": "CONC", "NAME": "C24",
            "bMASS_DENS": False, "DAMP_RAT": 0.05,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(RC)", "CODE": "", "DB": "C24", "bELAST": False}]
        },
        "2": {
            "TYPE": "STEEL", "NAME": "SS400",
            "bMASS_DENS": False, "DAMP_RAT": 0.02,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(S)", "CODE": "", "DB": "SS400", "bELAST": False}]
        }
    }
}
midas_api("POST", "/db/MATL", matl_data)

# --- DELETE ---
midas_api("DELETE", "/db/MATL", {"Assign": {"3": None}})
```

---

## 2. `/db/MATL-M1`

> **Material Properties (Hyper-S)** — 定义 Hyper-S 求解器专用材料特性。  
> ¹⁾ 使用同一 `/db/MATL` 端点，但额外支持 Hyper-S 专用参数。

- **URL**: `{base url}/db/MATL-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Material Properties (Hyper-S) ↗](https://support.midasuser.com/hc/ko/articles/56396523438873)

> **Note**: 本端点仅用于 Hyper-S 求解器。基本材料结构与 `/db/MATL` 相同，并额外支持 Hyper-S 专用的超弹性（Hyperelastic）材料模型。

```python
# 查询 Hyper-S 材料
result = midas_api("GET", "/db/MATL-M1")
```

---

## 3. `/db/IMFM`

> **Inelastic Material Properties for Fiber Model** — 为纤维模型（Fiber Model）分配非线性材料特性。

- **URL**: `{base url}/db/IMFM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Material Properties for Fiber Model ↗](https://support.midasuser.com/hc/en-us/articles/35807475893401)

### JSON Schema

```json
{
  "IMFM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "CONC_NAME":          { "description": "Fiber Model Property Name (Concrete)",         "type": "string" },
      "CONFINED_CONC_NAME": { "description": "Fiber Model Property Name (Confined Concrete)","type": "string" },
      "REBAR_NAME":         { "description": "Fiber Model Property Name (Rebar)",            "type": "string" },
      "STEEL_NAME":         { "description": "Fiber Model Property Name (Steel)",            "type": "string" }
    }
  }
}
```

### Specifications

#### Concrete Material

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Inelastic Material of Concrete | `"CONC_NAME"` | String | Blank | Optional |
| 2 | Confined Concrete for Columns | `"CONFINED_CONC_NAME"` | String | Blank | Optional |
| 3 | Inelastic Material of Rebar | `"REBAR_NAME"` | String | Blank | Optional |

#### Steel Material

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Inelastic Material of Steel | `"STEEL_NAME"` | String | Blank | Optional |

### Request Body

```json
{
  "Assign": {
    "1": {
      "CONC_NAME": "Concrete_KP",
      "CONFINED_CONC_NAME": "Confined_KP",
      "REBAR_NAME": "Rebar_Menegotto"
    },
    "2": {
      "STEEL_NAME": "Steel_Bilinear"
    }
  }
}
```

### Python 示例

```python
# 为混凝土单元分配纤维模型材料
imfm_data = {
    "Assign": {
        "3": {
            "CONC_NAME": "Conc_Kent&Park",
            "CONFINED_CONC_NAME": "Confined_Conc",
            "REBAR_NAME": "Rebar_MP"
        }
    }
}
midas_api("POST", "/db/IMFM", imfm_data)
```

---

## 4. `/db/IMFM-M1`

> **Inelastic Material Link for Auto Generation (Hyper-S)** — Hyper-S 专用的非线性材料自动生成链接。

- **URL**: `{base url}/db/IMFM-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Material Link for Auto Generation ↗](https://support.midasuser.com/hc/ko/articles/56375076523929)

```python
result = midas_api("GET", "/db/IMFM-M1")
```

---

## 5. `/db/TDMF`

> **Time Dependent Material – User Defined** — 定义徐变/干燥收缩/松弛的用户自定义函数。

- **URL**: `{base url}/db/TDMF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Properties - User Defined ↗](https://support.midasuser.com/hc/en-us/articles/35807665049369)

### JSON Schema

```json
{
  "TDMF": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Material Function Name", "type": "string" },
      "FTYPE":      { "description": "Material Func Type",    "type": "string" },
      "SCALE":      { "description": "Scale Factor",          "type": "number" },
      "CTYPE":      { "description": "Creep Type",            "type": "string" },
      "DESC":       { "description": "Description",           "type": "string" },
      "RELAXATION": { "description": "Relaxation Time",       "type": "integer" },
      "vDAY":       { "description": "Function Data",         "type": "array" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Function Name | `"NAME"` | String | - | **Required** |
| 2 | Material Function Type • Creep: `"CREEP"` • Shrinkage Strain: `"SHRINK"` • Relaxation: `"RELAX"` | `"FTYPE"` | String | - | **Required** |
| 3 | Scale Factor | `"SCALE"` | Number | - | **Required** |
| 4 | Description | `"DESC"` | String | Blank | Optional |
| 5 | Function Data (Array of `{DAY, VALUE}`) | `"vDAY"` | Array[Object] | - | **Required** |
| (1) | Time | `"DAY"` | Number | - | **Required** |
| (2) | Value | `"VALUE"` | Number | - | **Required** |
| 6 (Creep only) | Creep Type • Specific Creep: `"SC"` • Creep Function: `"CF"` • Creep Coefficient: `"CC"` | `"CTYPE"` | String | - | **Required** |
| 6 (Relax only) | Relaxation Time • Hour: 0 • Day: 1 | `"RELAXATION"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "CreepFunc_1",
      "FTYPE": "CREEP",
      "CTYPE": "CC",
      "SCALE": 1.0,
      "DESC": "사용자 정의 크리프 함수",
      "vDAY": [
        {"DAY": 28,  "VALUE": 0.5},
        {"DAY": 90,  "VALUE": 1.0},
        {"DAY": 365, "VALUE": 1.5},
        {"DAY": 3650,"VALUE": 2.0}
      ]
    }
  }
}
```

### Python 示例

```python
tdmf_data = {
    "Assign": {
        "1": {
            "NAME": "Shrinkage_User",
            "FTYPE": "SHRINK",
            "SCALE": 1.0,
            "DESC": "건조수축 함수",
            "vDAY": [
                {"DAY": 28,   "VALUE": 0.0001},
                {"DAY": 90,   "VALUE": 0.0002},
                {"DAY": 365,  "VALUE": 0.0003},
                {"DAY": 3650, "VALUE": 0.0004}
            ]
        }
    }
}
midas_api("POST", "/db/TDMF", tdmf_data)
```

---

## 6. `/db/TDMT`

> **Time Dependent Material – Creep/Shrinkage** — 定义基于规范的徐变/干燥收缩材料特性。支持 CEB-FIP(2010/1990/1978)、ACI、KDS 等多种国际/国内规范。

- **URL**: `{base url}/db/TDMT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Properties - Creep/Shrinkage ↗](https://support.midasuser.com/hc/en-us/articles/35808006330009)

### JSON Schema

```json
{
  "TDMT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Material Name",       "type": "string" },
      "CODE":       { "description": "Code Name",           "type": "string" },
      "STR":        { "description": "Compression Strength","type": "number" },
      "HU":         { "description": "Relative Humidity",  "type": "number" },
      "MSIZE":      { "description": "Notional Size",       "type": "number" },
      "CTYPE":      { "description": "Cement Type",         "type": "string" },
      "AGE":        { "description": "Concrete Age",        "type": "number" },
      "VOL":        { "description": "Volume/Surface Ratio","type": "number" },
      "CMETHOD":    { "description": "Curing Method",       "type": "string" },
      "TYPEOFAFFR": { "description": "Type of Aggregate",   "type": "integer" }
    }
  }
}
```

### Specifications（通用键 + CEB-FIP）

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Time Dependent Material Name | `"NAME"` | String | - | **Required** |
| 2 | Code Name ¹⁾ | `"CODE"` | String | - | **Required** |
| 3 | Compression Strength | `"STR"` | Number | - | **Required** |
| 4 | Relative Humidity (CEB-FIP 2010/1990: 40~99%; 1978: 40~100%) | `"HU"` | Number | - | **Required** |
| 5 (CEB-FIP) | Notional Size of Member | `"MSIZE"` | Number | - | **Required** |
| 6 | Type of Cement ²⁾ | `"CTYPE"` | String | `"RS"` | Optional |
| 7 | Concrete Age | `"AGE"` | Number | - | **Required** |
| 8 (CEB-FIP 2010) | Type of Aggregate • 0: Basalt/dense limestone • 1: Quartzite • 2: Limestone • 3: Sandstone | `"TYPEOFAFFR"` | Integer | 0 | Optional |
| 5 (ACI) | Volume/Surface Ratio | `"VOL"` | Number | - | **Required** |
| 7 (ACI) | Curing Method • Moist: `"MOIST"` • Steam: `"STEAM"` | `"CMETHOD"` | String | `"MOIST"` | Optional |

#### ¹⁾ Code Name 代码表（`TDMT.CODE`）

| 显示名 | `"CODE"` |
| --- | --- |
| CEB-FIP (2010) | `"CEB_FIP_2010"` |
| CEB-FIP (1990) | `"CEB"` |
| CEB-FIP (1978) | `"CEB_FIP_1978"` |
| ACI | `"ACI"` |
| PCA | `"PCA"` |
| Combined (ACI & PCA) | `"COMBINED"` |
| AASHTO | `"AASHTO"` |
| JAPAN (JSCE2012) | `"JSCE_12"` |
| JAPAN (JSCE2007) | `"JSCE_07"` |
| Japanese Standard | `"JAPAN"` |
| JAPAN (JSCE) | `"JSCE"` |
| INDIA (IRC:112-2020) | `"INDIA_IRC_112_2020"` |
| INDIA (IRC:18-2000) | `"INDIA_IRC_18_2000"` |
| INDIA (IRC:112-2011) | `"INDIA_IRC_112_2011"` |
| European | `"EUROPEAN"` |
| AS 5100.5-2017 Amd 2:2024 | `"AS_2017_AMD_2024"` |
| AS 5100.5-2017 | `"AS_5100_5_2017"` |
| AS 5100.5-2016 | `"AS_5100_5_2016"` |
| AS/RTA 5100.5-2011 | `"AS_RTA_5100_5_2011"` |
| AS 3600-2018 Amd 2:2021 | `"AS_2018_AMD_2021"` |
| AS 3600-2009 | `"AS_3600_2009"` |
| NZ Bridge (SP/M/022 Amd 4:2022) | `"NEWZEALAND_2022"` |
| NZ Bridge (SP/M/022) | `"NEWZEALAND"` |
| Russian | `"RUSSIAN"` |
| Chinese Standard | `"CHINESE"` |
| China (JTG D62-2004) | `"JTG"` |
| China (JTG3362-2018) | `"CHINA_JTG3362_2018"` |
| China (JTG/T D65-06-2015) | `"CHJTG_T_D65_2015"` |
| **KDS-2016** | **`"KDS_2016"`** |
| KCI-USD12 | `"KSI_USD12"` |
| KSCE 2010 | `"KSCE_2010"` |
| Korea Standard | `"KS"` |
| User Defined | `"USER_DEFINED"` |

> ⚠️ **2026-08-25 复核补强：** 代码表中原本遗漏的5个条目（`INDIA_IRC_112_2020`、`AS_2017_AMD_2024`、`AS_2018_AMD_2021`、`NEWZEALAND_2022`、`CHJTG_T_D65_2015`）
> 已对照
> 原文（文章 id `35808006330009`）补充。
>
> ⚠️ **2026-07-25 更正：** `CODE` 取值不是 `"KDS2016"`（无分隔符），而是 **`"KDS_2016"`**（下划线）。
> 此前版本文档与下方示例的写法有误。已在官方文章的 Request Examples
> （`"KDS-2016, KCI-USD12, KSCE 2010, Korea Standard"` 示例）中以实际载荷确认。
> `/db/TDME`（§7）中同系列的 `CODENAME` 字段却写作 `"KDS-2016"`（连字符），
> 请勿混淆 — 两个端点对同一韩国规范使用了不同的字面量。

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "KDS-2016",
      "CODE": "KDS_2016",
      "STR": 24000,
      "HU": 70,
      "MSIZE": 0.2,
      "CTYPE": "RS",
      "AGE": 28
    }
  }
}
```

### Python 示例

```python
# 定义基于 KDS 2016 规范的徐变/收缩
tdmt_data = {
    "Assign": {
        "1": {
            "NAME": "Creep_C24_KDS",
            "CODE": "KDS_2016",  # 注意：下划线写法（TDME 的 CODENAME 为连字符 "KDS-2016"）
            "STR": 24000,        # 抗压强度（kPa）
            "HU": 70,            # 相对湿度（%）
            "MSIZE": 0.2,        # 构件公称尺寸（m）
            "CTYPE": "RS",       # 水泥种类：普通
            "AGE": 28            # 浇筑龄期（days）
        }
    }
}
midas_api("POST", "/db/TDMT", tdmt_data)
```

---

## 7. `/db/TDME`

> **Time Dependent Material – Compressive Strength** — 定义混凝土抗压强度的时间依赖性。

- **URL**: `{base url}/db/TDME`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Properties - Compressive Strength ↗](https://support.midasuser.com/hc/en-us/articles/35808102389401)

### JSON Schema

```json
{
  "TDME": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "Material Name",       "type": "string" },
      "TYPE":     { "description": "Code or User Type",   "type": "string" },
      "CODENAME": { "description": "Code Name",           "type": "string" },
      "STRENGTH": { "description": "Compression Strength","type": "number" },
      "A":        { "description": "Factor A",            "type": "number" },
      "B":        { "description": "Factor B",            "type": "number" },
      "iCTYPE":   { "description": "Cement Type",         "type": "integer" },
      "nAGGRE":   { "description": "Aggregate Type",      "type": "integer" }
    }
  }
}
```

### Specifications

> ⚠️ **2026-08-25 复核全面更正。** 此前版本把 `A`/`B`（Factor a, b）字段组归为 "ACI/KDS"
> 一组，**误记为 `KDS-2016` 也使用 A/B 系数**。对照原文（文章 id
> `35808102389401`）可知 A/B 系数组属于 **`ACI`·`Korean Standard`**（CODENAME
> `"Korean Standard"`，第20号 — 与 `KDS-2016` 是不同的独立规范），而
> **`KDS-2016` 实际属于 `iCTYPE`（Cement Type）+ `DENSITY`（Weight Density）组**（与 `GILBERT AND RANZI` 结构相同）。
> 由于韩国用户最常用的规范中必填字段都是错的，故整张表按规范
> 分组重写。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Material Name | `"NAME"` | String | - | **Required** |
| 2 | Material Type · Code: `"CODE"` / User: `"USER"` | `"TYPE"` | String | - | **Required** |
| 3 (TYPE=CODE) | Code Name ¹⁾ | `"CODENAME"` | String | - | **Required** |
| 4 (TYPE=CODE) | Compression Strength | `"STRENGTH"` | Number | - | **Required** |

仅靠通用4个字段即可结束的规范：`INDIA(IRC:18-2000)` · `CEB-FIP(1978)` · `AS 5100.5-2017` ·
`AS 5100.5-2016` · `AS/RTA 5100.5-2011` · `AS 3600-2009`.

#### `ACI`、`Korean Standard` 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Factor, a | `"A"` | Number | - | **Required** |
| 6 | Factor, b | `"B"` | Number | - | **Required** |

#### `CEB-FIP(1990)` · `Ohzagi` · `European` · `INDIA(IRC:112-2011)` · `KCI-USD12` 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |

#### `CEB-FIP(2010)` · `INDIA(IRC:112-2020)` 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |
| 6 | Aggregate Type · Basalt/dense limestone: `0` / Quartzite: `1` / Limestone: `2` / Sandstone: `3` | `"nAGGRE"` | Integer | - | **Required** |

#### `Russian` 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |
| 6 | Curing Method · Natural Cure: `0` / Steam Cure: `1` | `"CMETH"` | Integer | - | **Required** |
| 7 | Concrete Type · Heavy Concrete: `0` / Fine-Grained Concrete: `1` | `"CTYPE"` | Integer | - | **Required** |
| 8 | Maximum Aggregate Size | `"MAXS"` | Number | - | **Required** |
| 9 | Specific Content of the Cement Paste | `"PZ"` | Number | - | **Required** |

> ⚠️ 本组的 `"CTYPE"`（Concrete Type，Integer）与最外层 `"TYPE"`（Code/User 区分，String）
> 名称相同但属于不同字段。已照原文原样搬运。

#### `GILBERT AND RANZI`、**`KDS-2016`** 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |
| 6 | Weight Density | `"DENSITY"` | Number | - | **Required** |

#### `Japan (Hydration)` 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Tensile Strength Factor | `"TENS_STRN_FACTOR"` | Number | - | **Required** |
| 6 | Use Concrete Data Option | `"bUSE"` | Boolean | `false` | Optional |
| 7 (bUSE=false) | Factor, a | `"A"` | Number | - | **Required** |
| 8 (bUSE=false) | Factor, b | `"B"` | Number | - | **Required** |
| 9 (bUSE=false) | Factor, d | `"D"` | Number | - | **Required** |
| 7 (bUSE=true) | Cement Type ²⁾ | `"iCTYPE"` | Integer | - | **Required** |

#### `Japan (Elastic)` 专用附加字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Elastic Cement Type · Normal Type: `0` / Rapid Type: `1` | `"iECTYPE"` | Integer | - | **Required** |

#### `TYPE = "USER"`（User Defined）专用字段

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 5 | Scale Factor | `"SCALE"` | Number | - | **Required** |
| 6 | Function Data (Array of `{TIME, COMP, TENS, ELAST}`) | `"SCALE"` | Array [Object] | - | **Required** |
| (1) | Time (day) | `"TIME"` | Number | - | **Required** |
| (2) | Compression Strength | `"COMP"` | Number | - | **Required** |
| (3) | Tensile Strength | `"TENS"` | Number | - | **Required** |
| (4) | Elastic Modulus | `"ELAST"` | Number | - | **Required** |

> ⚠️ 原文 Specifications 表在 "Scale Factor"（Number）与 "Function Data"（Array[Object]）两个
> 字段上都重复标注了 Key `"SCALE"`。看似笔误，但无可确认实际键名的示例，
> 故照原文搬运并以此注释留存（报错对象）。

#### ¹⁾ Code Name 代码表（`TDME.CODENAME`）

| No. | 显示名 | `"CODENAME"` |
| --- | --- | --- |
| 1 | ACI | `"ACI"` |
| 2 | CEB-FIP (2010) | `"CEB-FIP(2010)"` |
| 3 | CEB-FIP (1990) | `"CEB-FIP(1990)"` |
| 4 | Ohzagi | `"Ohzagi"` |
| 5 | European | `"European"` |
| 6 | INDIA (IRC:18-2000) | `"INDIA(IRC:18-2000)"` |
| 7 | CEB-FIP (1978) | `"CEB-FIP(1978)"` |
| 8 | AS 5100.5-2017 | `"AS 5100.5-2017"` |
| 9 | AS 5100.5-2016 | `"AS 5100.5-2016"` |
| 10 | AS/RTA 5100.5-2011 | `"AS/RTA 5100.5-2011"` |
| 11 | AS 3600-2009 | `"AS 3600-2009"` |
| 12 | INDIA (IRC:112-2011) | `"INDIA(IRC:112-2011)"` |
| 13 | INDIA (IRC:112-2020) | `"INDIA(IRC:112-2020)"` |
| 14 | Russian | `"Russian"` |
| 15 | GILBERT AND RANZI | `"GILBERT AND RANZI"` |
| 16 | Japan (Hydration) | `"Japan(hydration)"` |
| 17 | Japan (Elastic) | `"Japan(elastic)"` |
| 18 | **KDS-2016** | **`"KDS-2016"`** |
| 19 | KCI-USD12 | `"KCI-USD12"` |
| 20 | Korean Standard | `"Korean Standard"` |

> ⚠️ **2026-07-25 更正：** `CODENAME` 取值不是 `"KDS2016"`（无分隔符），而是 **`"KDS-2016"`**（连字符）。
> 此前版本文档与下方示例的写法有误。`/db/TDMT`（§6）的 `CODE` 字段对同一
> 韩国规范使用下划线写法 `"KDS_2016"`，因此两个端点的写法彼此不同 —
> 请按端点确认准确的字面量。

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "TDME_KDS2016",
      "TYPE": "CODE",
      "CODENAME": "KDS-2016",
      "STRENGTH": 30000,
      "iCTYPE": 1,
      "DENSITY": 230
    }
  }
}
```

> ⚠️ `KDS-2016` 仅有 `STRENGTH` 并不完整 — `iCTYPE`（Cement Type）与
> `DENSITY`（Weight Density）同为 **Required**。上例是原文 Request Example
> （文章 id `35808102389401`）实际载荷的原样搬运。

### Python 示例

```python
tdme_data = {
    "Assign": {
        "1": {
            "NAME": "CompStr_C24_KDS",
            "TYPE": "CODE",
            "CODENAME": "KDS-2016",  # 注意：连字符写法（TDMT 的 CODE 为下划线 "KDS_2016"）
            "iCTYPE": 1,   # Cement Type（KDS-2016 仅靠 STRENGTH 不足 — iCTYPE/DENSITY 必填）
            "DENSITY": 230,  # Weight Density
            "STRENGTH": 24000
        }
    }
}
midas_api("POST", "/db/TDME", tdme_data)
```

---

## 8. `/db/EDMP`

> **Change Property** — 按单元变更时间依赖材料特性（公称尺寸或体积/表面积比）。

- **URL**: `{base url}/db/EDMP`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Change Property ↗](https://support.midasuser.com/hc/en-us/articles/35808245801881)

### JSON Schema

```json
{
  "EDMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE": { "description": "TYPE",   "type": "string" },
      "H_VS": { "description": "H (VS)", "type": "number" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Change Property Method • Notional Size: `"NSM"` • Volume/Surface Ratio: `"VSR"` | `"TYPE"` | String | - | **Required** |
| 2 | Change Property Value (h for NSM, v/s for VSR) | `"H_VS"` | Number | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "10": { "TYPE": "NSM", "H_VS": 0.10 },
    "20": { "TYPE": "VSR", "H_VS": 0.15 }
  }
}
```

### Python 示例

```python
# 变更指定单元的公称尺寸
edmp_data = {
    "Assign": {
        "101": {"TYPE": "NSM", "H_VS": 0.20},
        "102": {"TYPE": "NSM", "H_VS": 0.20},
        "103": {"TYPE": "NSM", "H_VS": 0.30}
    }
}
midas_api("POST", "/db/EDMP", edmp_data)
```

---

## 9. `/db/TMAT`

> **Time Dependent Material Link** — 将时间依赖特性（徐变/干燥收缩 + 抗压强度）链接到材料。

- **URL**: `{base url}/db/TMAT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Time Dependent Material Link ↗](https://support.midasuser.com/hc/en-us/articles/35808280891033)

### JSON Schema

```json
{
  "TMAT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TDMT_NAME": { "description": "TDM-TYPE1 (CREEP/SHRINKAGE)", "type": "string" },
      "TDME_NAME": { "description": "TDM-TYPE2 (ELASTICITY)",      "type": "string" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Creep/Shrinkage Name | `"TDMT_NAME"` | String | - | **Required** |
| 2 | Comp. Strength Name | `"TDME_NAME"` | String | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "2": {
      "TDMT_NAME": "KDS2016",
      "TDME_NAME": "KDS2016"
    }
  }
}
```

### Python 示例

```python
# 将时间依赖特性链接到2号材料
tmat_data = {
    "Assign": {
        "2": {
            "TDMT_NAME": "Creep_C24_KDS",   # 在 /db/TDMT 中定义的名称
            "TDME_NAME": "CompStr_C24_KDS"  # 在 /db/TDME 中定义的名称
        }
    }
}
midas_api("POST", "/db/TMAT", tmat_data)
```

---

## 10. `/db/EPMT`

> **Plastic Material** — 定义塑性材料模型。支持 Tresca、Von-Mises、Mohr-Coulomb、Drucker-Prager、Masonry、Concrete Damage 等6种模型。

- **URL**: `{base url}/db/EPMT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Plastic Material ↗](https://support.midasuser.com/hc/en-us/articles/35808376517913)

### JSON Schema

```json
{
  "EPMT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":       { "description": "Name",       "type": "string" },
      "MODEL_TYPE": { "description": "Model Type", "type": "string" },
      "TRESCA":     { "description": "Tresca",     "type": "object" },
      "VMISES":     { "description": "Von Mises",  "type": "object" },
      "MOHRCL":     { "description": "Mohr-Coulomb","type": "object" },
      "DRUCKER":    { "description": "Drucker-Prager","type": "object" },
      "MASONRY":    { "description": "Masonry",    "type": "object" },
      "CONCDMG":    { "description": "Concrete Damage","type": "object" }
    }
  }
}
```

> ⚠️ **2026-08-25 复核补强。** 此前版本缺少 `MODEL_TYPE` 为 `"DP"`（Drucker-Prager）·`"MA"`
> （Masonry）·`"DM"`（Concrete Damage）时所需的 `DRUCKER`/`MASONRY`/`CONCDMG` 对象结构，
> 整个都漏掉了。此外 Tresca/Von-Mises/Mohr-Coulomb 公共参数中的 `HARDENING_COEF` 实际
> 上是 **Required**（按原文，当 `OPT_HARDENING` 取默认值 `0`=Activated 时），此前
> 版本误记为 Optional。经与原文（文章 id `35808376517913`）重新对照后全面补强。

### Specifications

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Plastic Material Name | `"NAME"` | String | - | **Required** |
| 2 | Model Type · `"TR"`(Tresca) / `"VM"`(Von-Mises) / `"MC"`(Mohr-Coulomb) / `"DP"`(Drucker-Prager) / `"MA"`(Masonry) / `"DM"`(Concrete Damage) | `"MODEL_TYPE"` | String | - | **Required** |

#### Tresca / Von-Mises 公共参数（`"TRESCA"` or `"VMISES"` object）

| Key | Description | Default | Required |
| --- | --- | --- | --- |
| `"INIT_YIELD_STRESS"` | Initial Uniaxial Yield Stress | - | **Required** |
| `"OPT_HARDENING"` | Hardening Option · Activated: `0` / Inactivated: `1` | `0` | Optional |
| `"HARDENING_TYPE"` | （仅 `OPT_HARDENING`=0 时）`"ISO"` / `"KIN"` / `"MIX"` | `"ISO"` | Optional |
| `"HARDENING_COEF"` | （`OPT_HARDENING`=0 时）Hardening Coefficient | - | **Required** |
| `"BACK_STRESS_COEF"` | （`HARDENING_TYPE`=`"MIX"` 时）Back Stress Coefficient | - | **Required** |

#### Mohr-Coulomb / Drucker-Prager 公共参数（`"MOHRCL"` or `"DRUCKER"` object）

| Key | Description | Default | Required |
| --- | --- | --- | --- |
| `"INIT_COHESION"` | Initial Cohesion | - | **Required** |
| `"INIT_FRIC_ANGLE"` | Initial Friction Angle (deg) | - | **Required** |
| `"OPT_HARDENING"` | Hardening Option · Activated: `0` / Inactivated: `1` | `0` | Optional |
| `"HARDENING_TYPE"` | （仅 `OPT_HARDENING`=0 时）`"ISO"` / `"KIN"` / `"MIX"` | `"ISO"` | Optional |
| `"HARDENING_COEF"` | （`OPT_HARDENING`=0 时）Hardening Coefficient | - | **Required** |
| `"BACK_STRESS_COEF"` | （`HARDENING_TYPE`=`"MIX"` 时）Back Stress Coefficient | - | **Required** |

#### Masonry 参数（`"MASONRY"` object）

Brick(`"BM"`)·Bed Joint(`"BED_JOINT"`)·Head Joint(`"HEAD_JOINT"`) 这3个材料 object 各自
具有与下方相同的子结构（全部 **Required**）：

| Key | Description |
| --- | --- |
| `"YOUNG_S_MODULUS"` | Young's Modulus |
| `"POSSIONS_S_RATIO"` | Poisson's Ratio |
| `"TENSION_STRENGTH"` | Tensile Strength |
| `"SOFTENING_PARAMETER"`(BM) / `"HARDENING_PARAM"`(BED_JOINT·HEAD_JOINT) | Stiffness Reduction Factor |

此外还需要形状信息 object `"GEOM"`（**Required**）：

| Key | Description | Required |
| --- | --- | --- |
| `"BRICK_LENGTH"` | Brick Length | **Required** |
| `"BRICK_HEIGHT"` | Brick Height | **Required** |
| `"THICKNESS_BED"` | Thickness of Bed | **Required** |
| `"THICKNESS_HEAD"` | Thickness of Head | **Required** |
| `"COORD_TYPE"` | Material Coordinate System（竖直/水平） · Global-Y/Global-X: `0` / Local-y/Local-z: `-1` / Global-Z/Angle: `-4` | **Required** |
| `"COORD_ANGLE"` | （`COORD_TYPE`=`-4` 时）以 Global X 轴为基准的角度 | **Required** |

#### Concrete Damage 参数（`"CONCDMG"` object）

| Key | Description | Required |
| --- | --- | --- |
| `"DILIATION_ANGLE"` | Dilation Angle | **Required** |
| `"ECCEN"` | Eccentricity | **Required** |
| `"FBO_FCO"` | fbo/fco | **Required** |
| `"K"` | K | **Required** |
| `"VISCOSITY_PARAM"` | Viscosity Parameter | **Required** |
| `"COMP_ITEMS"` | Compressive Behavior — Array of `{INELASTIC_STRAIN, YIELD_STRESS, DAMAGE}` | **Required** |
| `"TENSILE_ITEMS"` | Tensile Behavior — Array of `{INELASTIC_STRAIN, YIELD_STRESS, DAMAGE}` | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Steel_VonMises",
      "MODEL_TYPE": "VM",
      "VMISES": {
        "INIT_YIELD_STRESS": 235000,
        "OPT_HARDENING": 0,
        "HARDENING_TYPE": "ISO",
        "HARDENING_COEF": 21000
      }
    }
  }
}
```

### Python 示例

```python
epmt_data = {
    "Assign": {
        "1": {
            "NAME": "Steel_VM",
            "MODEL_TYPE": "VM",
            "VMISES": {
                "INIT_YIELD_STRESS": 235000,
                "OPT_HARDENING": 0,
                "HARDENING_TYPE": "ISO",
                "HARDENING_COEF": 21000
            }
        }
    }
}
midas_api("POST", "/db/EPMT", epmt_data)
```

---

## 11. `/db/EPMT-M1`

> **Plastic Material (Hyper-S)** — Hyper-S 专用塑性材料模型。

- **URL**: `{base url}/db/EPMT-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Plastic Material (Hyper-S) ↗](https://support.midasuser.com/hc/ko/articles/56511025581337)

```python
result = midas_api("GET", "/db/EPMT-M1")
```

---

## 12. `/db/SECT`

> **Section Properties** — 定义截面特性。依 `SECTTYPE` 取值支持 DB/User、Value、SRC、Combined、PSC、Tapered、Composite、Steel Girder 等多种子类型。

- **URL**: `{base url}/db/SECT`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Properties - Common ↗](https://support.midasuser.com/hc/en-us/articles/35808653964185)

### SECTTYPE 代码表

| SECTTYPE | 说明 |
|----------|------|
| `"DBUSER"` | DB / User 定义截面 |
| `"VALUE"` | 直接输入值的截面 |
| `"SRC"` | SRC（Steel-Reinforced Concrete）型钢混凝土组合截面 |
| `"COMBINED"` | 组合截面 |
| `"PSC"` | PSC（Prestressed Concrete）截面 |
| `"TAPERED"` | 变截面（Taper） |
| `"COMPOSITE"` | 钢-混凝土组合截面（PSC 或 Steel） |
| `"SOD"` | 钢主梁（Steel Girder） |

### JSON Schema（通用）

```json
{
  "SECT": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "SECTTYPE":   { "description": "Type",        "type": "string" },
      "SECT_NAME":  { "description": "Sect Name",   "type": "string" },
      "SECT_BEFORE":{ "description": "Sect Before", "type": "object",
        "properties": {
          "SHAPE":              { "type": "string" },
          "OFFSET_PT":          { "type": "string" },
          "OFFSET_CENTER":      { "type": "integer" },
          "HORZ_OFFSET_OPT":    { "type": "integer" },
          "VERT_OFFSET_OPT":    { "type": "integer" },
          "USERDEF_OFFSET_YI":  { "type": "number" },
          "USERDEF_OFFSET_ZI":  { "type": "number" },
          "USE_SHEAR_DEFORM":   { "type": "boolean" },
          "USE_WARPING_EFFECT": { "type": "boolean" }
        }
      }
    }
  }
}
```

### 通用 Specifications（所有 SECTTYPE 通用）

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Section Data Type | `"SECTTYPE"` | String | - | **Required** |
| 2 | Section Name | `"SECT_NAME"` | String | - | **Required** |
| 3 | Section Data (Before Stage) | `"SECT_BEFORE"` | Object | - | **Required** |
| (1) | Section Shape ²⁾ | `"SHAPE"` | String | - | **Required** |
| (2) | Offset Direction | `"OFFSET_PT"` | String | `"CC"` | Optional |
| (3) | Center Location (0: Centroid, 1: Center of Section) | `"OFFSET_CENTER"` | Integer | 0 | Optional |
| (4) | Horizontal Offset Option (0: Extreme Fiber, 1: User) | `"HORZ_OFFSET_OPT"` | Integer | 0 | Optional |
| (5) | Horizontal Offset Value (I-end) | `"USERDEF_OFFSET_YI"` | Number | 0 | Optional |
| (6) | Horizontal Offset Value (J-end, Tapered only) | `"USERDEF_OFFSET_YJ"` | Number | 0 | Optional |
| (7) | Vertical Offset Option | `"VERT_OFFSET_OPT"` | Integer | 0 | Optional |
| (8) | Vertical Offset Value (I-end) | `"USERDEF_OFFSET_ZI"` | Number | 0 | Optional |
| (9) | Vertical Offset Value (J-end, Tapered only) | `"USERDEF_OFFSET_ZJ"` | Number | 0 | Optional |
| (10) | User Type Offset Reference (0: Centroid, 1: Extreme Fiber) | `"USER_OFFSET_REF"` | Integer | 0 | Optional |
| (11) | Consider Shear Deformation | `"USE_SHEAR_DEFORM"` | Boolean | false | Optional |
| (12) | Consider Warping Effect | `"USE_WARPING_EFFECT"` | Boolean | false | Optional |

#### Offset Direction 代码表

| Code | Position |
|------|----------|
| `"LT"` | Left-Top |
| `"CT"` | Center-Top |
| `"RT"` | Right-Top |
| `"LC"` | Left-Center |
| `"CC"` | Center-Center |
| `"RC"` | Right-Center |
| `"LB"` | Left-Bottom |
| `"CB"` | Center-Bottom |
| `"RB"` | Right-Bottom |

---

### 12-A. SECT — DB/User (`"SECTTYPE": "DBUSER"`)

- **Source**: [Section Properties - DB/User ↗](https://support.midasuser.com/hc/en-us/articles/35809067039513)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| (1) | Data Type • DB: 1 • User: 2 | `"DATATYPE"` | Integer | - | **Required** |
| (2) | Section Specifications | `"SECT_I"` | Object | - | **Required** |
| DB | DB Name | `"DB_NAME"` | String | - | **Required** |
| DB | Section Name of DB | `"SECT_NAME"` | String | - | **Required** |
| User | Dimension of Section | `"vSIZE"` | Array[Number] | - | **Required** |

```json
{
  "Assign": {
    "1": {
      "SECTTYPE": "DBUSER",
      "SECT_NAME": "H300x150",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": true,
        "SHAPE": "H",
        "DATATYPE": 1,
        "SECT_I": { "DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9" }
      }
    }
  }
}
```

---

### 12-B. SECT — Value (`"SECTTYPE": "VALUE"`)

- **Source**: [Section Properties - Value ↗](https://support.midasuser.com/hc/en-us/articles/35839753881497)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Calculation Options | `"CALC_OPT"` | Boolean | true | Create Only |
| (1) | Dimension of Section ³⁾ | `"vSIZE"` | Array[Number] | - | **Required** |

```json
{
  "Assign": {
    "101": {
      "SECTTYPE": "VALUE",
      "SECT_NAME": "H_User",
      "CALC_OPT": true,
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": true,
        "SHAPE": "H",
        "SECT_I": {
          "vSIZE": [0.30, 0.15, 0.0065, 0.009, 0, 0, 0, 0]
        }
      }
    }
  }
}
```

---

### 12-C. SECT — SRC (`"SECTTYPE": "SRC"`)

- **Source**: [Section Properties - SRC ↗](https://support.midasuser.com/hc/en-us/articles/35845378225689)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| (1) | SRC Type • DB: 1 • User: 2 | `"SRC_TYPE"` | Integer | - | **Required** |
| (3) | E Ratio (Steel/Concrete) | `"MATL_ELAST"` | Number | - | **Required** |
| (4) | Density Ratio | `"MATL_DENS"` | Number | - | **Required** |
| (5) | Poisson's Ratio (Steel) | `"MATL_POIS_S"` | Number | - | **Required** |
| (6) | Poisson's Ratio (Concrete) | `"MATL_POIS_C"` | Number | - | **Required** |
| (7) | Stiffness Reduction Factor (Concrete) | `"MATL_STIF_FACTOR"` | Number | - | **Required** |
| (9) DB | Steel Section (DB/User) | `"SECT_I"` | Object | - | **Required** |
| (10) | Concrete Dimensions | `"SECT_J"` | Object | - | **Required** |

```json
{
  "Assign": {
    "201": {
      "SECTTYPE": "SRC",
      "SECT_NAME": "SRC_H300",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "RBO",
        "SRC_TYPE": 1,
        "MATL_ELAST": 7.69, "MATL_DENS": 2.94,
        "MATL_POIS_S": 0.3, "MATL_POIS_C": 0.18,
        "MATL_STIF_FACTOR": 1.0,
        "SECT_I": { "DB_NAME": "KS21", "SECT_NAME": "B400x400x12" },
        "SECT_J": { "vSIZE": [0.06, 0.065] }
      }
    }
  }
}
```

---

### 12-D. SECT — PSC (`"SECTTYPE": "PSC"`)

- **Source**: [Section Properties - PSC ↗](https://support.midasuser.com/hc/en-us/articles/35851688190105)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| i | Outer-Height array | `"vSIZE_PSC_A"` | Array[Number] | - | **Required** |
| ii | Outer-Breadth array | `"vSIZE_PSC_B"` | Array[Number] | - | **Required** |
| iii | Inner-Height array | `"vSIZE_PSC_C"` | Array[Number] | - | **Required** |
| iv | Inner-Breadth array | `"vSIZE_PSC_D"` | Array[Number] | - | **Required** |
| (6) | Web Thickness Check [i, j] | `"USE_WEB_THICK"` | Array[Boolean] | false | **Required** |

```json
{
  "Assign": {
    "401": {
      "SECTTYPE": "PSC",
      "SECT_NAME": "PSC_I-Girder",
      "SECT_BEFORE": {
        "OFFSET_PT": "CB",
        "HORZ_OFFSET_OPT": 0, "VERT_OFFSET_OPT": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "PSC1",
        "SECT_I": {
          "vSIZE_PSC_A": [0.20, 0.05, 0.10, 0.05, 0.05, 0.20],
          "vSIZE_PSC_B": [0.60, 0.40, 0.20, 0.18, 0.40, 0.60],
          "vSIZE_PSC_C": [0.0],
          "vSIZE_PSC_D": [0.0]
        },
        "USE_WEB_THICK": [false, false]
      }
    }
  }
}
```

---

### 12-E. SECT — Tapered (`"SECTTYPE": "TAPERED"`)

- **Source**: [Section Properties - Tapered - DB/User ↗](https://support.midasuser.com/hc/en-us/articles/35852806893593)

Tapered 截面在 `"SECT_BEFORE"`（I-end）之外另加定义 `"SECT_AFTER"`（J-end）。

```json
{
  "Assign": {
    "501": {
      "SECTTYPE": "TAPERED",
      "SECT_NAME": "Tapered_H",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0, "USERDEF_OFFSET_YJ": 0,
        "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0, "USERDEF_OFFSET_ZJ": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "H",
        "DATATYPE": 1,
        "SECT_I": { "DB_NAME": "KS21", "SECT_NAME": "H400x200x8/13" },
        "SECT_J": { "DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9" }
      }
    }
  }
}
```

---

### 12-F. SECT — Composite / Steel Girder

- **Source**: [Section Properties - Composite - Steel ↗](https://support.midasuser.com/hc/en-us/articles/35939122737689) | [Steel Girder ↗](https://support.midasuser.com/hc/en-us/articles/35939506348697)

```json
{
  "Assign": {
    "701": {
      "SECTTYPE": "COMPOSITE",
      "SECT_NAME": "SteelBox_Comp",
      "SECT_BEFORE": {
        "OFFSET_PT": "CC",
        "HORZ_OFFSET_OPT": 0, "VERT_OFFSET_OPT": 0,
        "USE_SHEAR_DEFORM": true, "USE_WARPING_EFFECT": false,
        "SHAPE": "SOD_BOX"
      }
    }
  }
}
```

### Python 示例（SECT 全部）

```python
# --- GET：查询所有截面 ---
result = midas_api("GET", "/db/SECT")
sections = result.get("SECT", {})
print(f"定义的截面数量：{len(sections)}")
for sid, s in sections.items():
    print(f"  {sid}: {s.get('SECT_NAME', '?')} ({s.get('SECTTYPE', '?')})")

# --- POST：创建 H 形钢 DB 截面 ---
sect_data = {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER",
            "SECT_NAME": "H300x150",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H",
                "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9"}
            }
        },
        "2": {
            "SECTTYPE": "DBUSER",
            "SECT_NAME": "H400x200",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H",
                "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H400x200x8/13"}
            }
        }
    }
}
midas_api("POST", "/db/SECT", sect_data)
```

---

## 13. `/db/THIK`

> **Thickness** — 定义板（Plate/Wall）单元的厚度。支持 Value 与 Stiffened（加劲板）4种子类型。

- **URL**: `{base url}/db/THIK`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Thickness - Value ↗](https://support.midasuser.com/hc/en-us/articles/35942236652697)

### JSON Schema

```json
{
  "THIK": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":   { "description": "Name",       "type": "string" },
      "TYPE":   { "description": "Type",       "type": "string" },
      "STYPE":  { "description": "Sub Type",   "type": "string" },
      "bINOUT": { "description": "Thick Type", "type": "boolean" },
      "T_IN":   { "description": "Thick In",   "type": "number" },
      "T_OUT":  { "description": "Thick Out",  "type": "number" },
      "OFFSET": { "description": "Offset",     "type": "integer" },
      "O_VALUE":{ "description": "Offset Value","type": "number" }
    }
  }
}
```

### Specifications — Value (`"TYPE": "VALUE"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Thickness Name | `"NAME"` | String | - | **Required** |
| 2 | Thickness Type • Value: `"VALUE"` • Stiffened: `"STIFFENED"` | `"TYPE"` | String | - | **Required** |
| 3 | Plane • false: In-plane & Out-of-plane (same) • true: Different I/O values | `"bINOUT"` | Boolean | false | Optional |
| 4 | In-plane Thickness | `"T_IN"` | Number | - | **Required** |
| 5 | Out-of-plane Thickness (when `"bINOUT"` is true) | `"T_OUT"` | Number | - | Required |
| 6 | Plate Offset Option • None: 0 • Thickness Ratio: 1 • Value: 2 | `"OFFSET"` | Integer | 0 | Optional |
| 7 | Local z Direction Offset Value | `"O_VALUE"` | Number | 0 | Optional |

### Specifications — Stiffened DB (`"STYPE": "DB"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Thickness Type | `"TYPE"` | String | - | **Required** |
| 2 | Stiffened Thickness Sub-Type • Value: `"VALUE"` • User: `"USER"` • DB: `"DB"` | `"STYPE"` | String | - | **Required** |
| 3 | Rib Position • `"LOWER"` • `"UPPER"` | `"RIB_POS"` | String | - | **Required** |
| 4 | Defined Stiffener | `"SECTION"` | Object | - | **Required** |
| (1) | Thickness | `"THIKNESS"` | Number | - | **Required** |
| (2) | DB Name | `"DBNAME"` | String | - | **Required** |
| (3) | XZ Section | `"XZ"` | Object | - | **Required** |
| i | Use Rib Attached | `"bRIB"` | Boolean | false | Optional |
| ii | Shape | `"SHAPE"` | String | - | **Required** |
| iii | Section Name | `"NAME"` | String | - | **Required** |
| iv | Rib Spacing Distance | `"DIST"` | Number | - | **Required** |

### Request Body 示例

#### Value 厚度

```json
{
  "Assign": {
    "1": {
      "NAME": "T200",
      "TYPE": "VALUE",
      "bINOUT": false,
      "T_IN": 0.20,
      "T_OUT": 0,
      "O_VALUE": 0
    }
  }
}
```

#### Stiffened DB 厚度

```json
{
  "Assign": {
    "101": {
      "NAME": "Stiff_DB",
      "TYPE": "STIFFENED",
      "STYPE": "DB",
      "RIB_POS": "LOWER",
      "SECTION": {
        "THIKNESS": 0.012,
        "DBNAME": "KS21",
        "XZ": { "bRIB": true, "SHAPE": "C", "NAME": "C75x40x5/7", "DIST": 0.4 }
      }
    }
  }
}
```

### Python 示例

```python
# --- GET：查询全部厚度 ---
result = midas_api("GET", "/db/THIK")
thiks = result.get("THIK", {})
print(f"定义的厚度数量：{len(thiks)}")

# --- POST：创建 Value 厚度 ---
thik_data = {
    "Assign": {
        "1": {"NAME": "T150", "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.15, "T_OUT": 0, "O_VALUE": 0},
        "2": {"NAME": "T200", "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.20, "T_OUT": 0, "O_VALUE": 0},
        "3": {"NAME": "T250", "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.25, "T_OUT": 0, "O_VALUE": 0},
    }
}
midas_api("POST", "/db/THIK", thik_data)
```

---

## 14. `/db/TSGR`

> **Tapered Group** — 定义变截面组。设置线性（Linear）或多项式（Polynomial）截面变化。

- **URL**: `{base url}/db/TSGR`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Tapered Group ↗](https://support.midasuser.com/hc/en-us/articles/35942955627673)

### JSON Schema

```json
{
  "TSGR": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "Group Name",                     "type": "string" },
      "ELEMLIST": { "description": "Element Key List",               "type": "array", "items": {"type": "integer"} },
      "ZVAR":     { "description": "Section shape z-axis variation", "type": "string" },
      "YVAR":     { "description": "Section shape y-axis variation", "type": "string" },
      "ZEXP":     { "description": "Z axis Exponent",                "type": "number" },
      "ZFROM":    { "description": "Z axis Symmetric Plane",         "type": "string" },
      "ZDIST":    { "description": "Z axis Symmetric Distance",      "type": "number" },
      "YEXP":     { "description": "Y axis Exponent",                "type": "number" },
      "YFROM":    { "description": "Y axis Symmetric Plane",         "type": "string" },
      "YDIST":    { "description": "Y axis Symmetric Distance",      "type": "number" }
    }
  }
}
```

### Specifications

> ⚠️ **2026-08-25 复核补强：** Y 轴多项式系列字段（`YEXP`/`YFROM`/`YDIST`）原本遗漏，
> 已按与 Z 轴的对称关系补充（文章 id `35942955627673`）。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Tapered Group Name | `"NAME"` | String | - | **Required** |
| 2 | Element No. list | `"ELEMLIST"` | Array[Integer] | - | **Required** |
| 3 | Z-axis Section Shape Variation · Linear: `"LINEAR"` / Polynomial: `"POLY"` | `"ZVAR"` | String | - | **Required** |
| 4 | Y-axis Section Shape Variation · Linear: `"LINEAR"` / Polynomial: `"POLY"` | `"YVAR"` | String | - | **Required** |
| 5 (ZVAR=POLY) | Z axis Exponent | `"ZEXP"` | Number | - | **Required** |
| 6 (ZVAR=POLY) | Z axis Symmetric Plane from i or j | `"ZFROM"` | String | `"i"` | Optional |
| 7 (ZVAR=POLY) | Z axis Symmetric Plane Distance (m) | `"ZDIST"` | Number | 0 | Optional |
| 8 (YVAR=POLY) | Y axis Exponent | `"YEXP"` | Number | - | **Required** |
| 9 (YVAR=POLY) | Y axis Symmetric Plane from i or j | `"YFROM"` | String | `"i"` | Optional |
| 10 (YVAR=POLY) | Y axis Symmetric Plane Distance (m) | `"YDIST"` | Number | 0 | Optional |

### Request Body

```json
{
  "Assign": {
    "1": { "NAME": "LinearGroup", "ELEMLIST": [1, 2, 3], "ZVAR": "LINEAR", "YVAR": "LINEAR" },
    "2": { "NAME": "PolyGroup",   "ELEMLIST": [4, 5, 6], "ZVAR": "POLY",   "YVAR": "LINEAR", "ZEXP": 2.0, "ZFROM": "i", "ZDIST": 0 }
  }
}
```

### Python 示例

```python
tsgr_data = {
    "Assign": {
        "1": {
            "NAME": "Haunch_Linear",
            "ELEMLIST": [10, 11, 12, 13],
            "ZVAR": "LINEAR",
            "YVAR": "LINEAR"
        }
    }
}
midas_api("POST", "/db/TSGR", tsgr_data)
```

---

## 15. `/db/SECF`

> **Section Manager – Stiffness** — 分配截面刚度修正系数。可按施工阶段、地震、设计等各分组设置刚度倍率。

- **URL**: `{base url}/db/SECF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Stiffness ↗](https://support.midasuser.com/hc/en-us/articles/35943174833177)

### Specifications

> ⚠️ **2026-08-25 复核补强：** 变截面（Tapered）J端系数11个字段（`W_SF`·`IPART`·`bDiffIJ`·
> `J1`~`J8`）整个都缺失（文章 id `35943174833177`）。J端字段与 I端命名规则不同，
> 不写作 `AREA_SF_J` 而是 **`J1`~`J8`**（按顺序对应 Area/Asy/Asz/Ixx/Iyy/Izz/Weight/Warping），
> 故照原文原样搬运。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Stiffness Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Area Scale Factor (I) | `"AREA_SF"` | Number | 1 | Optional |
| (4) | Asy Scale Factor (I) | `"ASY_SF"` | Number | 1 | Optional |
| (5) | Asz Scale Factor (I) | `"ASZ_SF"` | Number | 1 | Optional |
| (6) | Ixx Scale Factor (I) | `"IXX_SF"` | Number | 1 | Optional |
| (7) | Iyy Scale Factor (I) | `"IYY_SF"` | Number | 1 | Optional |
| (8) | Izz Scale Factor (I) | `"IZZ_SF"` | Number | 1 | Optional |
| (9) | Weight Scale Factor | `"WGT_SF"` | Number | 1 | Optional |
| (10) | Warping Scale Factor (I) | `"W_SF"` | Number | 1 | Optional |
| (11) | Composite Section 适用时点 · 仅 Before：`1` / 仅 After：`2` / Before+After：`3` | `"IPART"` | Integer | 1 | Optional |
| (12) | Tapered Section — 是否单独使用 J端值 | `"bDiffIJ"` | Boolean | `true` | Optional |
| (13) | Area Scale Factor (J, Tapered) | `"J1"` | Number | 1 | Optional |
| (14) | Asy Scale Factor (J) | `"J2"` | Number | 1 | Optional |
| (15) | Asz Scale Factor (J) | `"J3"` | Number | 1 | Optional |
| (16) | Ixx Scale Factor (J) | `"J4"` | Number | 1 | Optional |
| (17) | Iyy Scale Factor (J) | `"J5"` | Number | 1 | Optional |
| (18) | Izz Scale Factor (J) | `"J6"` | Number | 1 | Optional |
| (19) | Weight Scale Factor (J) | `"J7"` | Number | 1 | Optional |
| (20) | Warping Scale Factor (J) | `"J8"` | Number | 1 | Optional |

### Request Body

```json
{
  "Assign": {
    "9001": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Creep716",
        "AREA_SF": 2.61, "ASY_SF": 3.25, "ASZ_SF": 1.09,
        "IXX_SF": 1.39, "IYY_SF": 1.52, "IZZ_SF": 1.0,
        "WGT_SF": 1.0
      }]
    }
  }
}
```

### Python 示例

```python
# 开裂截面刚度折减（混凝土梁：Izz = 0.35）
secf_data = {
    "Assign": {
        "5": {
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "Seismic",
                "AREA_SF": 1.0, "ASY_SF": 1.0, "ASZ_SF": 1.0,
                "IXX_SF": 1.0, "IYY_SF": 0.70, "IZZ_SF": 0.35,
                "WGT_SF": 1.0
            }]
        }
    }
}
midas_api("POST", "/db/SECF", secf_data)
```

---

## 16. `/db/RPSC`

> **Section Manager – Reinforcements** — 设置 PSC/RC 截面的钢筋配筋数据。

- **URL**: `{base url}/db/RPSC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Reinforcements ↗](https://support.midasuser.com/hc/en-us/articles/35943227821465)

### Specifications

> ⚠️ **2026-08-25 复核全面补强。** 此前版本剪力钢筋（`SBAR_ITEMS`）中只有斜筋（DR）4个
> 字段，SBW·TR·SR·Enclosing Stirrup 以及纵向钢筋（`MBAR_ITEMS`）整体全部缺失
> （文章 id `35943227821465`）。已按原文补全全部字段。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Same Rebar Data at i and j-end (Longitudinal) | `"OPT_MBAR_J"` | Boolean | - | **Required** |
| 2 | Same Shear Rebar Data at i and j-end | `"OPT_SBAR_J"` | Boolean | - | **Required** |
| 3 | Cracked Section | `"OPT_CRACKED"` | Boolean | - | **Required** |
| 4 | Shear Reinforcement Data (Array, Index 0=i-section / 1=j-section) | `"SBAR_ITEMS"` | Array[Object] | - | **Required** |
| 5 | Longitudinal Reinforcement Data (Array, Index 0=i-section / 1=j-section) | `"MBAR_ITEMS"` | Array[Object] | - | **Required** |

#### `SBAR_ITEMS[]` — 剪力钢筋

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| (1) | Diagonal Reinforcement (DR) | `"OPT_DR"` | Boolean | `false` | Optional |
| (2) | [DR] Pitch | `"DR_PITCH"` | Number | - | Optional |
| (3) | [DR] Angle | `"DR_THETA"` | Number | - | Optional |
| (4) | [DR] Area | `"DR_AW"` | Number | - | Optional |
| (5) | Steel Bar for Web (SBW) | `"OPT_SBW"` | Boolean | `false` | Optional |
| (6) | [SBW] Pitch | `"SBW_PITCH"` | Number | - | Optional |
| (7) | [SBW] Angle | `"SBW_ANGLE"` | Number | - | Optional |
| (8) | [SBW] Area | `"SBW_AP"` | Number | - | Optional |
| (9) | [SBW] Pre-force | `"SBW_PS"` | Number | - | Optional |
| (10) | [SBW] Shear Reduction Factor | `"SBW_FACTOR"` | Number | - | Optional |
| (11) | Torsional Reinforcement (TR) | `"OPT_TR"` | Boolean | `false` | Optional |
| (12) | [TR] Pitch | `"TR_PITCH"` | Number | - | Optional |
| (13) | [TR] Area (Web) | `"TR_AWT"` | Number | - | Optional |
| (14) | [TR] Area (Longitudinal) | `"TR_ALT"` | Number | - | Optional |
| (15) | Stirrup Exist | `"OPT_SR"` | Boolean | `false` | Optional |
| (16) | [SR] Pitch | `"SR_PITCH"` | Number | - | Optional |
| (17) | [SR] Area | `"SR_AW"` | Number | - | Optional |
| (18) | Enclosing Stirrup | `"OPT_LBAR_FLG"` | Boolean | `false` | Optional |
| (19) | （Enclosed 截面面积计算用）Cover Thickness | `"LBAR_THICK"` | Number | - | Optional |
| (20) | Include Flange/Cantilever · Off: `0` / On: `1` | `"LBAR_INC_FC"` | Integer | - | Optional |

#### `MBAR_ITEMS[]` — 纵向钢筋

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| (1) | Section Position · `"I"` / `"J"` | `"IJ"` | String | - | **Required** |
| (2) | Bar Name | `"NAME"` | String | - | **Required** |
| (3) | Reference Y · Centroid: `0` / Left: `1` | `"REF_Y"` | Integer | - | **Required** |
| (4) | Distance from Reference (Y-dir) | `"Y"` | Number | 0 | Optional |
| (5) | Reference Z · Top: `0` / Bottom: `1` | `"REF_Z"` | Integer | - | **Required** |
| (6) | Distance from Reference (Z-dir) | `"Z"` | Number | 0 | Optional |
| (7) | Number of Rebar | `"NUM"` | Integer | - | **Required** |
| (8) | Spacing between Rebars | `"SPACING"` | Number | 0 | Optional |
| (9) | Part | `"PART"` | Integer | - | - |

### Request Body

```json
{
  "Assign": {
    "401": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": false,
      "SBAR_ITEMS": [
        { "OPT_DR": false },
        { "OPT_DR": false }
      ],
      "MBAR_ITEMS": [
        { "IJ": "I", "NAME": "D25", "REF_Y": 0, "Y": 0, "REF_Z": 1, "Z": 0.05, "NUM": 4, "SPACING": 0.15 }
      ]
    }
  }
}
```

---

## 17. `/db/STRPSSM`

> **Section Manager – Stress Points** — 定义截面的附加应力计算点。

- **URL**: `{base url}/db/STRPSSM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Stress Points ↗](https://support.midasuser.com/hc/en-us/articles/35943448721177)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Same Stress Points at i and j-end | `"OPT_SAME_J"` | Boolean | true | Optional |
| 2 | Number of Stress Points (I) | `"POINT_SIZE_1"` | Integer | - | **Required** |
| 3 | Number of Stress Points (J) | `"POINT_SIZE_2"` | Integer | - | **Required** |
| 4 | Stress Point Coordinates (I) | `"POINT1"` | Array[{PY, PZ}] | - | **Required** |
| (1) | Point Y | `"PY"` | Number | - | **Required** |
| (2) | Point Z | `"PZ"` | Number | - | **Required** |
| 5 | Stress Point Coordinates (J) | `"POINT2"` | Array[{PY, PZ}] | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "9003": {
      "OPT_SAME_J": true,
      "POINT_SIZE_1": 2, "POINT_SIZE_2": 2,
      "POINT1": [{"PY": 0.00583, "PZ": 0.00476}, {"PY": -0.00506, "PZ": 0.00097}],
      "POINT2": [{"PY": 0.00583, "PZ": 0.00476}, {"PY": -0.00506, "PZ": 0.00097}]
    }
  }
}
```

---

## 18. `/db/PSSF`

> **Section Manager – Plate Stiffness Scale Factor** — 设置板单元刚度修正系数。

- **URL**: `{base url}/db/PSSF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Plate Stiffness Scale Factor ↗](https://support.midasuser.com/hc/en-us/articles/35943557337753)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Axial Fxx Scale Factor | `"AXIAL_X"` | Number | 1 | Optional |
| (4) | Axial Fyy Scale Factor | `"AXIAL_Y"` | Number | 1 | Optional |
| (5) | Shear Fxy Scale Factor | `"SHEAR"` | Number | 1 | Optional |
| (6) | Bending Mxx Scale Factor | `"OUT_BENDING_X"` | Number | 1 | Optional |
| (7) | Bending Myy Scale Factor | `"OUT_BENDING_Y"` | Number | 1 | Optional |
| (8) | Bending Mxy Scale Factor | `"OUT_TORSION"` | Number | 1 | Optional |
| (9) | Shear Vxx Scale Factor | `"OUT_SHEAR_X"` | Number | 1 | Optional |
| (10) | Shear Vyy Scale Factor | `"OUT_SHEAR_Y"` | Number | 1 | Optional |

### Request Body

```json
{
  "Assign": {
    "12": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service",
        "AXIAL_X": 0.6, "AXIAL_Y": 0.7, "SHEAR": 0.8,
        "OUT_BENDING_X": 0.9, "OUT_BENDING_Y": 1.0,
        "OUT_TORSION": 1.1, "OUT_SHEAR_X": 1.0, "OUT_SHEAR_Y": 1.0
      }]
    }
  }
}
```

---

## 19. `/db/VBEM`

> **Virtual Beam** — 定义用于结果力计算的虚拟梁截面。由2个虚拟截面构成。

- **URL**: `{base url}/db/VBEM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Virtual Beam ↗](https://support.midasuser.com/hc/en-us/articles/35943802727065)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Virtual Section 1 | `"VSEC1"` | Integer | - | **Required** |
| 2 | Virtual Section 2 | `"VSEC2"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": { "VSEC1": 1, "VSEC2": 2 }
  }
}
```

---

## 20. `/db/VSEC`

> **Virtual Section** — 定义用于结果力计算的虚拟截面。使用节点列表与法向矢量。

- **URL**: `{base url}/db/VSEC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Section Manager - Virtual Section ↗](https://support.midasuser.com/hc/en-us/articles/35943859944729)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Name | `"NAME"` | String | - | **Required** |
| 2 | Centroid Calculation Type | `"CENT_CALC_TYPE"` | Integer | - | **Required** |
| 3 | Centroid X (Global) | `"CEN_PT_X"` | Number | - | **Required** |
| 4 | Centroid Y (Global) | `"CEN_PT_Y"` | Number | - | **Required** |
| 5 | Centroid Z (Global) | `"CEN_PT_Z"` | Number | - | **Required** |
| 6 | Direction Normal Vector (X) | `"NORMAL_X"` | Number | - | **Required** |
| 7 | Direction Normal Vector (Y) | `"NORMAL_Y"` | Number | - | **Required** |
| 8 | Direction Normal Vector (Z) | `"NORMAL_Z"` | Number | - | **Required** |
| 9 | Node List | `"NODE_LIST"` | Integer | - | **Required** |
| 10 | Element List | `"ELEM_LIST"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Girder_I_Section",
      "CENT_CALC_TYPE": 0,
      "CEN_PT_X": 0, "CEN_PT_Y": 18.0, "CEN_PT_Z": 0.934,
      "NORMAL_X": 1, "NORMAL_Y": 0, "NORMAL_Z": 0,
      "NODE_LIST": [20, 29, 26, 23],
      "ELEM_LIST": [10, 11, 12]
    }
  }
}
```

---

## 21. `/db/EWSF`

> **Effective Width Scale Factor** — 向截面分配有效宽度折减系数。

- **URL**: `{base url}/db/EWSF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Effective Width Scale Factor ↗](https://support.midasuser.com/hc/en-us/articles/35943954272281)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | ly Scale Factor for Sbz (I-End) | `"LYSCALE"` | Number | 1 | **Required** |
| (4) | z_top Scale Factor (I-End) | `"ZTSCALE"` | Number | 1 | **Required** |
| (5) | z_bot Scale Factor (I-End) | `"ZBSCALE"` | Number | 1 | **Required** |
| (6) | J-End Option | `"bJ"` | Boolean | false | **Required** |
| (7) | ly Scale Factor (J-End) | `"LYSCALE_J"` | Number | 1 | Optional |
| (8) | z_top Scale Factor (J-End) | `"ZTSCALE_J"` | Number | 1 | Optional |
| (9) | z_bot Scale Factor (J-End) | `"ZBSCALE_J"` | Number | 1 | Optional |

### Request Body

```json
{
  "Assign": {
    "10": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service",
        "LYSCALE": 0.5, "ZTSCALE": 0.6, "ZBSCALE": 0.7,
        "bJ": true,
        "LYSCALE_J": 0.8, "ZTSCALE_J": 0.9, "ZBSCALE_J": 1.0
      }]
    }
  }
}
```

---

## 22. `/db/IEHC`

> **Inelastic Hinge Control Data** — 设置非线性铰控制数据（纤维划分数量等）。

- **URL**: `{base url}/db/IEHC`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Hinge Control Data ↗](https://support.midasuser.com/hc/en-us/articles/35944093809689)

### Specifications

> ⚠️ **2026-08-25 复核全面补强。** Cover（保护层）相关 Beam 字段2个与 GEN 专用 Wall 相关
> 字段9个整个都缺失（文章 id `35944093809689`）。原有 Request Body 示例还使用了
> `CoverDivNumNy`/`CoverDivNumNz` 这类原文中不存在的键，实际键名为
> `BeamDivNumNyCover`/`BeamDivNumNzCover` — 已按原文 Examples 原样替换。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Reference Location for Distributed Hinges · I-End: `0` / Center: `1` / J-End: `2` | `"BEAM_LOC"` | Integer | - | **Required** |
| 2 | Consider Reinforcement Area | `"OPT_ConsiderRebarArea1D"` | Boolean | - | **Required** |
| 3 | Fiber Beam Areas Core · Auto Size: `0` / Equal-Size: `1` | `"FAreaSizeCore"` | Integer | - | **Required** |
| 4 | Number of Divisions(Beam-Column) — Ny (y-dir) | `"BeamDivNumNy"` | Integer | - | **Required** |
| 5 | Number of Divisions(Beam-Column) — Nz (z-dir) | `"BeamDivNumNz"` | Integer | - | **Required** |
| 6 | Fiber Beam Areas Cover · Auto Size: `0` / Equal-Size: `1` | `"FAreaSizeCover"` | Integer | - | **Required** |
| 7 | Number of divisions(Beam-Column, Cover) — Ny | `"BeamDivNumNyCover"` | Integer | - | **Required** |
| 8 | Number of divisions(Beam-Column, Cover) — Nz | `"BeamDivNumNzCover"` | Integer | - | **Required** |

#### GEN 专用字段（Wall/墙单元）

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 9 | Consider Out of Plane Nonlinearity of Plate Type | `"WallConsOut"` | Boolean | - | **Required** |
| 10 | Fiber Wall Areas Core | `"WAreaSize"` | Integer | - | **Required** |
| 11 | Number of divisions — z, Core | `"WallDivNumZ"` | Integer | - | **Required** |
| 12 | Number of divisions — y, Core | `"WallDivNumY"` | Integer | - | **Required** |
| 13 | Fiber Wall Areas Cover | `"WAreaSizeCover"` | Integer | - | **Required** |
| 14 | Number of divisions — z, Cover | `"WallDivNumZCover"` | Integer | - | **Required** |
| 15 | Number of divisions — y, Cover | `"WallDivNumYCover"` | Integer | - | **Required** |
| 16 | Wall, Consider Rebar Area | `"OPT_ConsiderRebarAreaWall"` | Boolean | - | **Required** |
| 17 | Shear Spring Location | `"dR"` | Number | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "BEAM_LOC": 1,
      "BeamDivNumNy": 15,
      "BeamDivNumNz": 20,
      "WallConsOut": false,
      "WallDivNumZ": 8,
      "WallDivNumY": 1,
      "dR": 0.4,
      "WAreaSize": "AUTO",
      "OPT_ConsiderRebarArea1D": false,
      "OPT_ConsiderRebarAreaWall": false,
      "FAreaSizeCore": 1,
      "FAreaSizeCover": 1,
      "WAreaSizeCover": 1,
      "BeamDivNumNyCover": 20,
      "BeamDivNumNzCover": 15,
      "WallDivNumZCover": 8,
      "WallDivNumYCover": 1
    }
  }
}
```

> ⚠️ 原文 Specifications 表将 `"WAreaSize"` 标注为 Integer，但原文 Request Example
> 直接发送字符串 `"AUTO"`。按本仓库惯例示例优先于表格，故原样搬运了示例值
> — 实际发送时注意写法（Integer vs `"AUTO"`）。

---

## 23. `/db/IEHG`

> **Assign Inelastic Hinge Properties** — 将非线性铰属性（Inelastic Hinge Property + Fiber Division）分配给单元。

- **URL**: `{base url}/db/IEHG`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinge Properties ↗](https://support.midasuser.com/hc/en-us/articles/35944228031001)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Name of Inelastic Hinge Property | `"PROP_NAME"` | String | - | **Required** |
| 2 | Name of Fiber Division | `"FIBER_NAME"` | String | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "2101": {
      "PROP_NAME": "Fiber_Auto",
      "FIBER_NAME": "B2102_Column12"
    }
  }
}
```

---

## 24. `/db/IEHG-BEAM-M1`

> **Assign Inelastic Hinges – Beam (Hyper-S)** — Hyper-S 专用梁单元非线性铰分配。

- **URL**: `{base url}/db/IEHG-BEAM-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Beam ↗](https://support.midasuser.com/hc/ko/articles/57668691043865)

```python
result = midas_api("GET", "/db/IEHG-BEAM-M1")
```

---

## 25. `/db/IEHG-TRUSS-M1`

> **Assign Inelastic Hinges – Truss (Hyper-S)** — Hyper-S 专用桁架单元非线性铰分配。

- **URL**: `{base url}/db/IEHG-TRUSS-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Truss ↗](https://support.midasuser.com/hc/ko/articles/57668724267545)

```python
result = midas_api("GET", "/db/IEHG-TRUSS-M1")
```

---

## 26. `/db/IEHG-GL-M1`

> **Assign Inelastic Hinges – General Link (Hyper-S)** — Hyper-S 专用一般连接非线性铰分配。

- **URL**: `{base url}/db/IEHG-GL-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - General Link ↗](https://support.midasuser.com/hc/ko/articles/57668691115801)

```python
result = midas_api("GET", "/db/IEHG-GL-M1")
```

---

## 27. `/db/IEHG-PSS-M1`

> **Assign Inelastic Hinges – Point Spring Support (Hyper-S)** — Hyper-S 专用点弹簧支承非线性铰分配。

- **URL**: `{base url}/db/IEHG-PSS-M1`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Assign Inelastic Hinges - Point Spring Support ↗](https://support.midasuser.com/hc/ko/articles/57668755432473)

```python
result = midas_api("GET", "/db/IEHG-PSS-M1")
```

---

## 28. `/db/FIMP`

> **Inelastic Material Properties** — 定义纤维模型非线性材料。支持混凝土（Kent&Park、Mander 等）与钢材（Bilinear、Menegotto-Pinto 等）多种滞回（Hysteresis）模型。

- **URL**: `{base url}/db/FIMP`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Inelastic Material Properties ↗](https://support.midasuser.com/hc/en-us/articles/35944335180569)

### JSON Schema

```json
{
  "FIMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":      { "description": "Name",            "type": "string" },
      "MATL_TYPE": { "description": "Material Type",   "type": "string" },
      "HYS_MODEL": { "description": "Hysteresis Model","type": "string" },
      "CONC":      { "description": "Concrete Model",  "type": "object" },
      "STEEL":     { "description": "Steel Model",     "type": "object" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Material Name | `"NAME"` | String | - | **Required** |
| 2 | Material Type • Concrete: `"CONC"` • Steel: `"STEEL"` | `"MATL_TYPE"` | String | - | **Required** |
| 3 | Hysteresis Model ¹⁾ | `"HYS_MODEL"` | String | - | **Required** |

> ⚠️ FIMP 原文（文章 id `35944335180569`）是处理混凝土（Kent&Park·Japanese Standard·Mander 等）与
> 钢材（Bilinear·Menegotto-Pinto 等）多数滞回模型、长达5900行以上的庞大文档。
> 本仓库仅选取其中使用最广的 **Kent & Park 模型作为代表详细记述**，其余
> 模型只保留「以 `MATL_TYPE`/`HYS_MODEL` 组合存在」这一事实，不做全量记述。

#### Concrete — Kent & Park (`"HYS_MODEL": "KPM"`)

| Key | Description | Required |
| --- | --- | --- |
| `"KENPAR"."FC"` | Concrete Strength (fc') | **Required** |
| `"KENPAR"."PARTIAL_FACT"` | Partial Safety Factor | **Required** |
| `"KENPAR"."K"` | Strength/Strain Factor | **Required** |
| `"KENPAR"."EC0"` | Peak Strain (εc0) | **Required** |
| `"KENPAR"."EC1_METHOD"` | Hardening Strain Method · Manual: `0` / Calculation: `1` | **Required** |
| `"KENPAR"."EC1"` | Hardening Strain Manual (εc1) | **Required** |
| `"KENPAR"."Z"` | Hardening Strain Calculation (Z) | **Required** |
| `"KENPAR"."ECU"` | Ultimate Strain (εcu) | **Required** |
| `"KENPAR"."STRENGTH_AFTER"` | Strength After Critical Strain · Zero: `0` / Keep: `1` | **Required** |

### Request Body

```json
{
  "Assign": {
    "3": {
      "NAME": "Conc_Kent&Park",
      "MATL_TYPE": "CONC",
      "HYS_MODEL": "KPM",
      "CONC": {
        "KENPAR": {
          "FC": 30000,
          "PARTIAL_FACT": 1.0,
          "K": 1.0,
          "EC0": 0.002,
          "EC1_METHOD": 1,
          "EC1": 0.0035,
          "Z": 100,
          "ECU": 0.003,
          "STRENGTH_AFTER": 0
        }
      }
    }
  }
}
```

### Python 示例

```python
fimp_data = {
    "Assign": {
        "1": {
            "NAME": "Concrete_KP",
            "MATL_TYPE": "CONC",
            "HYS_MODEL": "KPM",
            "CONC": {
                "KENPAR": {
                    "FC": 24000,          # 抗压强度（kPa）
                    "PARTIAL_FACT": 1.0,
                    "K": 1.0,
                    "EC0": 0.002,         # 最大应变
                    "EC1_METHOD": 1,      # 0=手动输入，1=计算
                    "EC1": 0.0035,
                    "Z": 100,
                    "ECU": 0.003,
                    "STRENGTH_AFTER": 0   # 0=极限应变后强度为 0，1=强度保持
                }
            }
        }
    }
}
midas_api("POST", "/db/FIMP", fimp_data)
```

---

## 29. `/db/FIBR`

> **Fiber Division of Section** — 将截面划分为纤维（Fiber）并分配非线性材料。

- **URL**: `{base url}/db/FIBR`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Fiber Division of Section ↗](https://support.midasuser.com/hc/en-us/articles/35944476555801)

### Specifications

> ⚠️ **2026-08-25 复核全面补强。** `FIBR_BASE[]` 的实际逐纤维属性（REBAR_NAME/AREA/坐标/
> 材料连接等）8个字段与上层的监测纤维指定2个字段整个都缺失
> （文章 id `35944476555801`）。另外 `FIBR_BASE_KEY` 在表中写作 Boolean，但原文
> JSON Schema 与 Request Example 均按 **Integer**（纤维标识键值，例：`752`）处理，已更正。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Fiber Division Name | `"NAME"` | String | - | **Required** |
| 2 | Assigned Section ID | `"SECT_KEY"` | Integer | - | **Required** |
| 3 | Assign Type | `"ASSIGN_TYPE"` | Integer | - | **Required** |
| 4 | Inelastic Material Properties Name (6 elements) | `"FIMP_NAME"` | Array[String, 6] | - | **Required** |
| 5 | Inelastic Material Properties Color (6 elements) | `"FIMP_COLOR"` | Array[Object, 6] | - | Optional |
| (1) R/G/B | Color components | `"R"` `"G"` `"B"` | Integer | 0 | Optional |
| 6 | Fiber Division Base Data | `"FIBR_BASE"` | Array[Object] | - | **Required** |
| (1) | Fiber Base Key | `"FIBR_BASE_KEY"` | Integer | - | **Required** |
| (2) | Rebar Name | `"REBAR_NAME"` | String | - | **Required** |
| (3) | Area | `"AREA"` | Number | - | **Required** |
| (4) | Center Y | `"CENTER_Y"` | Number | - | **Required** |
| (5) | Center Z | `"CENTER_Z"` | Number | - | **Required** |
| (6) | Fiber Material ID（`FIMP_NAME`/`FIMP_COLOR` 数组中第几个材料） | `"FIBER_MATL_ID"` | Number | - | **Required** |
| (7) | Area Consider Rebar | `"AREA_CONSIDER_REBAR"` | Number | - | **Required** |
| (8) | Is Rebar | `"OPT_IS_REBAR"` | Boolean | - | **Required** |
| (9) | Fiber 外轮廓多边形 Point Y 列表 | `"POINT_Y"` | Array[Number] | - | **Required** |
| (10) | Fiber 外轮廓多边形 Point Z 列表 | `"POINT_Z"` | Array[Number] | - | **Required** |
| 7 | Monitored Fiber 使用与否 | `"OPT_MONITORED_FIBER"` | Boolean | - | **Required** |
| 8 | Monitored Fiber（对应 `FIBR_BASE` 各项的 0/1 标志数组） | `"MONITORED_FIBER"` | Array[Integer] | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Column_Fiber",
      "SECT_KEY": 11001,
      "ASSIGN_TYPE": 0,
      "FIMP_NAME": [
        "Steel", "Cover Concrete", "Core Conc 1",
        "Core Conc 1", "Core Conc 1", "Core Conc 1"
      ],
      "FIMP_COLOR": [
        {"R": 255, "G": 0, "B": 0},
        {"R": 128, "G": 128, "B": 128},
        {"R": 0, "G": 128, "B": 0},
        {"R": 0, "G": 128, "B": 0},
        {"R": 0, "G": 128, "B": 0},
        {"R": 0, "G": 128, "B": 0}
      ],
      "FIBR_BASE": [
        {
          "FIBR_BASE_KEY": 752,
          "REBAR_NAME": "",
          "AREA": 0.00688072,
          "CENTER_Y": -1.05047e-16,
          "CENTER_Z": 1.06179,
          "FIBER_MATL_ID": 1,
          "AREA_CONSIDER_REBAR": 0,
          "OPT_IS_REBAR": false,
          "POINT_Y": [0.0527429, 0.0527429, -0.0527429, -0.0527429, 0],
          "POINT_Z": [1.08596, 1.029, 1.029, 1.08596, 1.1025]
        }
      ],
      "OPT_MONITORED_FIBER": true,
      "MONITORED_FIBER": [0, 0, 0, 0, 0, 0]
    }
  }
}
```

---

## 30. `/db/GRDP`

> **Group Damping** — 按材料组、结构组、边界组设置阻尼比。

- **URL**: `{base url}/db/GRDP`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Group Damping ↗](https://support.midasuser.com/hc/en-us/articles/35944577940633)

### Specifications

> ⚠️ **2026-08-25 复核全面补强。** 本端点处理阻尼比指定的两种方式 —
> **Strain Energy Proportional**（应变能比例，按振型计算阻尼比）与
> **Element Mass & Stiffness Proportional**（Rayleigh 阻尼系数直接输入/基于振型计算） —
> 此前版本只有 Strain Energy 一侧的部分（3个字段），Element Mass & Stiffness
> Proportional 系列18个字段（含按组覆盖用的 `GROUP_DAMPING_ITEMS[]` 的13个子字段
> 在内）与分组优先级4个字段整体缺失（文章 id `35944577940633`）。

#### Strain Energy Proportional

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | 是否使用 Strain Energy Proportional | `"bExistStrain"` | Boolean | - | **Required** |
| 2 | Damping Ratio Items（按材料/结构组/边界组的阻尼比） | `"STRAIN_GROUP_ITEMS"` | Array[Object] | - | **Required** |
| (1) | Damping Ratio Type · Material: `"MATERIAL"` / Structure Group: `"STRUCTURE"` / Boundary: `"BOUNDARY"` | `"GROUP_TYPE"` | String | - | **Required** |
| (2) | Damping Ratio Name（材料为 ID，结构组/边界组为名称） | `"GROUP_NAME"` | String | - | **Required** |
| (3) | Damping Ratio | `"DAMPING_RATIO"` | Number | - | **Required** |
| 3 | Calculate Only When Used | `"OPT_CALC_WHEN_USED"` | Boolean | - | **Required** |
| 4 | Priority: Material Data vs Structure Group · Material: `0` / Structure Group: `1` | `"STRAIN_GROUP_PRIORITY"` | Integer | - | **Required** |
| 5 | Priority between Structure Groups · Smallest: `0` / Largest: `1` | `"STRAIN_VALUE_PRIORITY"` | Integer | - | **Required** |

#### Element Mass & Stiffness Proportional

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 6 | 是否使用 Element Mass & Stiffness Proportional | `"bExistElement"` | Boolean | - | **Required** |
| 7 | （未指定单元）Mass Proportional 选项 | `"OPT_MASS_PROP_DEFAULT"` | Boolean | `false` | Optional |
| 8 | （未指定单元）Stiffness Proportional 选项 | `"OPT_STIFF_PROP_DEFAULT"` | Boolean | `false` | Optional |
| 9 | 直接输入/基于振型计算 · Direct: `0` / Calculate from Modal Damping: `1` | `"DIRECT_CALC_MODE_DEFAULT"` | Integer | - | **Required** |
| 10 | Mass Proportional 值 | `"MASS_COEF_DEFAULT"` | Number | - | **Required** |
| 11 | Stiffness Proportional 值 | `"STIFF_COEF_DEFAULT"` | Number | - | **Required** |
| 12 | 系数计算基准 · Frequency: `0` / Period: `1` | `"FREQ_PERIOD_MODE_DEFAULT"` | Integer | - | **Required** |
| 13 | Frequency Mode 1 | `"FREQ_MODE_1_DEFAULT"` | Number | - | **Required** |
| 14 | Frequency Mode 2 | `"FREQ_MODE_2_DEFAULT"` | Number | - | **Required** |
| 15 | Period Mode 1 | `"PERIOD_MODE_1_DEFAULT"` | Number | - | **Required** |
| 16 | Period Mode 2 | `"PERIOD_MODE_2_DEFAULT"` | Number | - | **Required** |
| 17 | Damping Ratio Mode 1 | `"DAMPING_MODE_1_DEFAULT"` | Number | - | **Required** |
| 18 | Damping Ratio Mode 2 | `"DAMPING_MODE_2_DEFAULT"` | Number | - | **Required** |
| 19 | 按组覆盖 Rayleigh 阻尼 | `"GROUP_DAMPING_ITEMS"` | Array[Object] | - | **Required** |
| 20 | Priority: Material Data vs Structure Group（单元侧） | `"ELEM_GROUP_PRIORITY"` | Integer | - | **Required** |
| 21 | Priority between Structure Groups（单元侧） | `"ELEM_VALUE_PRIORITY"` | Integer | - | **Required** |

`GROUP_DAMPING_ITEMS[]` 以组为单位覆盖与上方7~18号同义的字段，
使用的名称仅去掉 `"_DEFAULT"` 后缀：`GROUP_TYPE`/`GROUP_NAME`（与上方 `STRAIN_GROUP_ITEMS`
相同的 3-way 规则）+ `STIFF_COEF`/`OPT_STIFF_PROP`/`MASS_COEF`/`OPT_MASS_PROP`/
`DIRECT_CALC_MODE`/`FREQ_PERIOD_MODE`/`FREQ_MODE_1`/`FREQ_MODE_2`/`PERIOD_MODE_1`/
`PERIOD_MODE_2`/`DAMPING_RATIO_MODE`/`DAMPING_RATIO_MODE_1`/`DAMPING_RATIO_MODE_2`.

### Request Body

```json
{
  "Assign": {
    "1": {
      "STIFF_COEF_DEFAULT": 0.0848826377636192,
      "MASS_COEF_DEFAULT": 0.04188790133333333,
      "OPT_CALC_WHEN_USED": true,
      "OPT_MASS_PROP_DEFAULT": true,
      "OPT_STIFF_PROP_DEFAULT": true,
      "DIRECT_CALC_MODE_DEFAULT": 1,
      "FREQ_PERIOD_MODE_DEFAULT": 0,
      "FREQ_MODE_1_DEFAULT": 0.1,
      "FREQ_MODE_2_DEFAULT": 0.2,
      "PERIOD_MODE_1_DEFAULT": 0,
      "PERIOD_MODE_2_DEFAULT": 0,
      "DAMPING_MODE_1_DEFAULT": 0.06,
      "DAMPING_MODE_2_DEFAULT": 0.07,
      "bExistElement": true,
      "bExistStrain": true,
      "GROUP_DAMPING_ITEMS": [
        {
          "GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1",
          "STIFF_COEF": 0.005787452574792216, "OPT_STIFF_PROP": true,
          "MASS_COEF": 0.06854383854545451, "OPT_MASS_PROP": true,
          "DIRECT_CALC_MODE": 1, "FREQ_PERIOD_MODE": 0,
          "FREQ_MODE_1": 0.5, "FREQ_MODE_2": 0.6,
          "PERIOD_MODE_1": 0, "PERIOD_MODE_2": 0,
          "DAMPING_RATIO_MODE": 0,
          "DAMPING_RATIO_MODE_1": 0.02, "DAMPING_RATIO_MODE_2": 0.02
        }
      ],
      "STRAIN_GROUP_ITEMS": [
        { "GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1", "DAMPING_RATIO": 0.02 }
      ],
      "ELEM_GROUP_PRIORITY": 0,
      "ELEM_VALUE_PRIORITY": 0,
      "STRAIN_GROUP_PRIORITY": 0,
      "STRAIN_VALUE_PRIORITY": 0
    }
  }
}
```

### Python 示例

```python
# 设置1号材料 Strain Energy 阻尼比 2% + Rayleigh 系数（Frequency Mode 1/2 = 0.1/0.2Hz）
grdp_data = {
    "Assign": {
        "1": {
            "bExistStrain": True,
            "bExistElement": True,
            "OPT_CALC_WHEN_USED": True,
            "OPT_MASS_PROP_DEFAULT": True,
            "OPT_STIFF_PROP_DEFAULT": True,
            "DIRECT_CALC_MODE_DEFAULT": 1,   # 1=基于振型计算
            "FREQ_PERIOD_MODE_DEFAULT": 0,   # 0=以 Frequency 为基准
            "FREQ_MODE_1_DEFAULT": 0.1,
            "FREQ_MODE_2_DEFAULT": 0.2,
            "PERIOD_MODE_1_DEFAULT": 0,
            "PERIOD_MODE_2_DEFAULT": 0,
            "DAMPING_MODE_1_DEFAULT": 0.06,
            "DAMPING_MODE_2_DEFAULT": 0.07,
            "STIFF_COEF_DEFAULT": 0.0849,
            "MASS_COEF_DEFAULT": 0.0419,
            "STRAIN_GROUP_ITEMS": [
                {"GROUP_TYPE": "MATERIAL", "GROUP_NAME": "1", "DAMPING_RATIO": 0.05}
            ],
            "ELEM_GROUP_PRIORITY": 0,
            "ELEM_VALUE_PRIORITY": 0,
            "STRAIN_GROUP_PRIORITY": 0,
            "STRAIN_VALUE_PRIORITY": 0
        }
    }
}
midas_api("POST", "/db/GRDP", grdp_data)
```

---

## 31. `/db/ESSF`

> **Element Stiffness Scale Factor** — 直接按单元分配截面刚度修正系数。

- **URL**: `{base url}/db/ESSF`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Element Stiffness Scale Factor ↗](https://support.midasuser.com/hc/en-us/articles/44613910309401)

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Items (Array of Objects) | `"ITEMS"` | Array[Object] | - | **Required** |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Area (Cross-sectional area) | `"AREA_SF"` | Number | 1.0 | Optional |
| (3) | Asy (Shear area, local y) | `"ASY_SF"` | Number | 1.0 | Optional |
| (4) | Asz (Shear area, local z) | `"ASZ_SF"` | Number | 1.0 | Optional |
| (5) | Ixx (Torsional resistance) | `"IXX_SF"` | Number | 1.0 | Optional |
| (6) | Iyy (Moment of Inertia, y-axis) | `"IYY_SF"` | Number | 1.0 | Optional |
| (7) | Izz (Moment of Inertia, z-axis) | `"IZZ_SF"` | Number | 1.0 | Optional |
| (8) | Weight | `"WGT_SF"` | Number | 1.0 | Optional |
| (9) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (10) | Part（组合截面专用） · Before: `"Before"` / After: `"After"` / All: `"All"` | `"iPart"` | String | `"Before"` | Optional |

### Request Body

```json
{
  "Assign": {
    "1": {
      "ITEMS": [{
        "ID": 1,
        "AREA_SF": 0.5,
        "ASY_SF": 0.6, "ASZ_SF": 0.7,
        "IXX_SF": 0.8, "IYY_SF": 0.8, "IZZ_SF": 0.9,
        "WGT_SF": 0.95,
        "GROUP_NAME": "",
        "iPart": "All"
      }]
    }
  }
}
```

> ⚠️ **2026-08-25 复核补强：** 组合截面专用字段 `iPart`（Before/After/All）原本遗漏，
> 已补充（文章 id `44613910309401`）。

### Python 示例

```python
# RC 柱开裂截面刚度折减（按 ACI 318：Izz = 0.70，Iyy = 0.70）
essf_data = {
    "Assign": {
        "5": {
            "ITEMS": [{
                "ID": 1,
                "AREA_SF": 1.0,
                "ASY_SF": 1.0, "ASZ_SF": 1.0,
                "IXX_SF": 0.20,  # 扭转刚度折减
                "IYY_SF": 0.70,  # 开裂截面
                "IZZ_SF": 0.70,
                "WGT_SF": 1.0,
                "GROUP_NAME": ""
            }]
        }
    }
}
midas_api("POST", "/db/ESSF", essf_data)
```

---

## 32. `/db/MATD`

> **Modify Concrete Materials** — 查询·修改既有混凝土材料（`TYPE:"CONC"`）的设计值（强度）与钢筋等级。与 `/db/MATL` 不同，**仅支持 GET/PUT**。

- **URL**: `{base url}/db/MATD`
- **Methods**: `GET`, `PUT`
- **Source**: [Modify Concrete Materials ↗](https://support.midasuser.com/hc/en-us/articles/35993732216985-Modify-Concrete-Materials)

### Specifications

> ✅ **2026-09-06 解决确认：** 原文 Specifications 表4号 Key 曾为 `"RABAR_CODENAME"`（漏 E 的笔误），
> 已由 2026-09-01 原文更新更正为 `"REBAR_CODENAME"`（复确认时
> `REBAR_CODENAME` 3次、`RABAR_CODENAME` 0次）。本文档从一开始即为正常写法。
> 应为 2026-08-27 报错（Jira `MAPI-2484`）的反映结果。
>
> ⚠️ **仅存在于 schema 中的字段（无说明依据）。** `DATA1.DESIGN` 下的
> `bLAMBDA`/`dLAMBDA`/`bTRANSFER`/`dTRANSFERFCI` 4个字段只在 JSON Schema 中存在，原文
> Specifications 表与 Request Example 中都没有说明与示例 — 推测与轻骨料混凝土 λ系数·预应力
> 传递强度相关，但必填与否·默认值均无依据，故仅作参考标注。除此之外
> **2026-09-01 更新又新增了3个最外层字段**（见下表），它们同样只在 schema 中
> 存在，表与示例中都没有。
>
> ⚠️ **原文 JSON Schema 语法错误（2026-09-06 确认）：** 在新增的 `"bSERVCHECK"` 之前，
> 闭合 `SUBREBAR_B_FY` 块的 `}` 后面**缺少逗号**，导致整个 schema 块不是有效 JSON
> （原文如此：`..."type": "number" } "bSERVCHECK": {...`）。报错对象。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Material Type (Concrete: `"CONC"`) | `"TYPE"` | String | - | **Required** |
| 2 | Material Name | `"NAME"` | String | - | **Required** |
| 3 | Concrete Material Information | `"DATA1"` | Object | - | **Required** |
| 3-(1) | Material Code Name | `"DATA1.CODENAME"` | String | - | **Required** |
| 3-(3) | Material Grade | `"DATA1.CODEMATLNAME"` | String | - | **Required** |
| 3-(4) | Material Design Values | `"DATA1.DESIGN"` | Object | - | **Required** |
| 3-(4)-i | Strength | `"DATA1.DESIGN.C_FC"` | Number | - | GET only |
| 3-(4)-ii | （推测）是否应用 Lambda ⚠️表与示例中无依据 | `"DATA1.DESIGN.bLAMBDA"` | Boolean | - | 不明 |
| 3-(4)-iii | （推测）Lambda 值 ⚠️表与示例中无依据 | `"DATA1.DESIGN.dLAMBDA"` | Number | - | 不明 |
| 3-(4)-iv | Strength (Initial) | `"DATA1.DESIGN.C_FCI"` | Number | - | GET only |
| 3-(4)-v | （推测）是否应用 Transfer ⚠️表与示例中无依据 | `"DATA1.DESIGN.bTRANSFER"` | Boolean | - | 不明 |
| 3-(4)-vi | （推测）Transfer 时的 fci 值 ⚠️表与示例中无依据 | `"DATA1.DESIGN.dTRANSFERFCI"` | Number | - | 不明 |
| 4 | Rebar Code Name | `"REBAR_CODENAME"` | String | - | **Required** |
| 5 | Main Rebar Name | `"MAINREBAR_REBARNAME"` | String | - | **Required** |
| 6 | Sub Rebar Name | `"SUBREBAR_REBARNAME"` | String | Blank | Optional |
| 7 | Main Rebar (fy) | `"MAINREBAR_B_FY"` | Number | 0 | GET only |
| 8 | Sub Rebar (fy) | `"SUBREBAR_B_FY"` | Number | 0 | GET only |
| 9 | （推测）使用性能验算与否 ⚠️表与示例中无依据（schema 说明 `ServiceabilityCheck`） | `"bSERVCHECK"` | Boolean | - | 不明 |
| 10 | （推测）短期系数 ⚠️表与示例中无依据（schema 说明 `ShortTerm`） | `"dSHORTTERM"` | Number | - | 不明 |
| 11 | （推测）长期系数 ⚠️表与示例中无依据（schema 说明 `LongTerm`） | `"dLONGTERM"` | Number | - | 不明 |

> `C_FC`·`C_FCI`·`MAINREBAR_B_FY`·`SUBREBAR_B_FY` 是依赖于 `CODENAME`/`CODEMATLNAME`/`REBAR_CODENAME` 的计算值，仅在 GET 响应中填充，PUT 请求时会被忽略。
>
> 9~11号（`bSERVCHECK`/`dSHORTTERM`/`dLONGTERM`）是 2026-09-01 原文更新时在 JSON Schema
> 最外层新增的字段（2026-09-06 定期检查中发现）。原文 Specifications 表与 Request Example
> 尚未反映，除类型外没有依据，故上述说明是基于 schema `description` 字符串的
> 推测。
>
> ⚠️ **原文 Specifications 表缺失 — 待报错。** 只存在于 schema 而表中没有对应行，仅看表的
> 用户无从得知这3个字段的存在。2026-09-18 实测验证已确认这3个字段实际会被发送·
> 存储（`bSERVCHECK=true`、`dSHORTTERM=1.25`、`dLONGTERM=1.5`），可见并非死 schema 而是
> **表缺失**。不过各字段的含义仍是基于 schema 说明字符串的推测，故保留上方
> 「（推测）」标注。验证详情参见
> [live_verification_feedback_20260918.md](../../zh-cn/error_reports/live_verification_feedback_20260918.md)。

### Request Body

```json
{
  "Assign": {
    "1": {
      "TYPE": "CONC",
      "NAME": "C16/20",
      "DATA1": {
        "CODENAME": "EN(RC)",
        "CODEMATLNAME": "C16/20",
        "DESIGN": { "C_FC": 16000, "C_FCI": 11200 }
      },
      "REBAR_CODENAME": "EN04(RC)",
      "MAINREBAR_REBARNAME": "ClassB",
      "SUBREBAR_REBARNAME": "ClassC",
      "MAINREBAR_B_FY": 500000,
      "SUBREBAR_B_FY": 600000
    }
  }
}
```

### Python 示例

```python
# 修改既有混凝土材料（ID=1）的钢筋等级
matd_data = {
    "Assign": {
        "1": {
            "TYPE": "CONC",
            "NAME": "C16/20",
            "DATA1": {
                "CODENAME": "EN(RC)",
                "CODEMATLNAME": "C16/20"
            },
            "REBAR_CODENAME": "EN04(RC)",
            "MAINREBAR_REBARNAME": "ClassB",
            "SUBREBAR_REBARNAME": "ClassC"
        }
    }
}
midas_api("PUT", "/db/MATD/1", matd_data)
```

---

## 完整工作流示例 — 材料·截面·厚度自动设置

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY"

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}

# ── Step 1: 定义材料 ─────────────────────────────────────
midas_api("POST", "/db/MATL", {
    "Assign": {
        "1": {
            "TYPE": "CONC", "NAME": "C24",
            "bMASS_DENS": False, "DAMP_RAT": 0.05,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(RC)", "CODE": "", "DB": "C24", "bELAST": False}]
        },
        "2": {
            "TYPE": "STEEL", "NAME": "SS400",
            "bMASS_DENS": False, "DAMP_RAT": 0.02,
            "HE_SPEC": 0, "HE_COND": 0, "PLMT": 0, "P_NAME": "",
            "PARAM": [{"P_TYPE": 1, "STANDARD": "KS21(S)", "CODE": "", "DB": "SS400", "bELAST": False}]
        }
    }
})

# ── Step 2: 定义截面（H 形钢 DB） ───────────────────────────
midas_api("POST", "/db/SECT", {
    "Assign": {
        "1": {
            "SECTTYPE": "DBUSER", "SECT_NAME": "H300x150",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H", "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H300x150x6.5/9"}
            }
        },
        "2": {
            "SECTTYPE": "DBUSER", "SECT_NAME": "H400x200",
            "SECT_BEFORE": {
                "OFFSET_PT": "CC",
                "OFFSET_CENTER": 0, "USER_OFFSET_REF": 0,
                "HORZ_OFFSET_OPT": 0, "USERDEF_OFFSET_YI": 0,
                "VERT_OFFSET_OPT": 0, "USERDEF_OFFSET_ZI": 0,
                "USE_SHEAR_DEFORM": True, "USE_WARPING_EFFECT": True,
                "SHAPE": "H", "DATATYPE": 1,
                "SECT_I": {"DB_NAME": "KS21", "SECT_NAME": "H400x200x8/13"}
            }
        }
    }
})

# ── Step 3: 定义厚度（楼板、墙） ─────────────────────────
midas_api("POST", "/db/THIK", {
    "Assign": {
        "1": {"NAME": "Slab_200",  "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.20, "T_OUT": 0, "O_VALUE": 0},
        "2": {"NAME": "Wall_250",  "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.25, "T_OUT": 0, "O_VALUE": 0},
        "3": {"NAME": "Slab_150",  "TYPE": "VALUE", "bINOUT": False, "T_IN": 0.15, "T_OUT": 0, "O_VALUE": 0},
    }
})

print("✓ 材料、截面、厚度定义完成")
```

---

*[04_DB_Properties.md] 已完成 — 下一个文件 [05_DB_Boundary.md] 已可开始推进。*
