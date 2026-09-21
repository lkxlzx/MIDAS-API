# DB – Static Loads

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:** `https://moa-engineers.midasit.com:443/gen`  
> **认证：** 所有请求都必须带 `MAPI-Key: <key>` 头  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../06_DB_Static_Loads.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | [/db/STLD](#1-dbstld--static-load-cases) | Static Load Cases |
| 2 | [/db/BODF](#2-dbbodf--self-weight) | Self-Weight |
| 3 | [/db/CNLD](#3-dbcnld--nodal-loads) | Nodal Loads |
| 4 | [/db/BMLD](#4-dbbmld--beam-loads) | Beam Loads |
| 5 | [/db/SDSP](#5-dbsdsp--specified-displacements-of-support) | Specified Displacements of Support |
| 6 | [/db/NMAS](#6-dbnmas--nodal-masses) | Nodal Masses |
| 7 | [/db/LTOM](#7-dbltom--loads-to-masses) | Loads to Masses |
| 8 | [/db/NBOF](#8-dbnbof--nodal-body-force) | Nodal Body Force |
| 9 | [/db/PSLT](#9-dbpslt--define-pressure-load-type) | Define Pressure Load Type |
| 10 | [/db/PRES](#10-dbpres--assign-pressure-loads) | Assign Pressure Loads |
| 11 | [/db/PNLD](#11-dbpnld--define-plane-load-type) | Define Plane Load Type |
| 12 | [/db/PNLA](#12-dbpnla--assign-plane-loads) | Assign Plane Loads |
| 13 | [/db/FBLD](#13-dbfbld--define-floor-load-type) | Define Floor Load Type |
| 14 | [/db/FBLA](#14-dbfbla--assign-floor-loads) | Assign Floor Loads |
| 15 | [/db/FMLD](#15-dbfmld--finishing-material-loads) | Finishing Material Loads |
| 16 | [/db/POSP](#16-dbposp--parameter-of-soil-properties) | Parameter of Soil Properties |
| 17 | [/db/EPST](#17-dbepst--static-earth-pressure) | Static Earth Pressure |
| 18 | [/db/EPSE](#18-dbepse--seismic-earth-pressure) | Seismic Earth Pressure |
| 19 | [/db/POSL](#19-dbposl--parameter-of-seismic-loads) | Parameter of Seismic Loads |
| 20 | [/db/SWIND](#20-dbswind--static-wind-load) | Static Wind Load (KDS 41-12:2022 / User Type) |
| 21 | [/db/SSEIS](#21-dbsseis--static-seismic-load) | Static Seismic Load (KDS 41-17-00:2019 / User Type) |

---

## 公共 Python 辅助函数

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. /db/STLD — Static Load Cases

> 定义静力荷载工况(Load Case)。此后所有荷载数据均引用此处定义的 `NAME`(荷载工况名)。

**Input URI:** `{base url}/db/STLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "NAME": "DL",
      "TYPE": "D",
      "DESC": "DeadLoads"
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Ordering Index in GUI | `"NO"` | Integer | - | Read Only |
| 2 | Load Case Name | `"NAME"` | String | - | Required |
| 3 | Load Type ¹⁾ | `"TYPE"` | String | - | Required |
| 4 | Description | `"DESC"` | String | Blank | Optional |

> ¹⁾ Load Type 取值列表（67种）：

| No. | Load Type | Value | No. | Load Type | Value |
|-----|-----------|-------|-----|-----------|-------|
| 1 | User Defined Load | `"USER"` | 2 | Dead Load | `"D"` |
| 3 | Dead Load of Component and Attachments | `"DC"` | 4 | Dead Load of Wearing Surfaces and Utilities | `"DW"` |
| 5 | Down Drag | `"DD"` | 6 | Earth Pressure | `"EP"` |
| 7 | Active Earth Pressure – Native Ground / Non-cohesive | `"EANN"` | 8 | Active Earth Pressure – Native Ground / Cohesive | `"EANC"` |
| 9 | Active Earth Pressure – Made Ground / Non-cohesive | `"EAMN"` | 10 | Active Earth Pressure – Made Ground / Cohesive | `"EAMC"` |
| 11 | Passive Earth Pressure – Native Ground / Non-cohesive | `"EPNN"` | 12 | Passive Earth Pressure – Native Ground / Cohesive | `"EPNC"` |
| 13 | Passive Earth Pressure – Made Ground / Non-cohesive | `"EPMN"` | 14 | Passive Earth Pressure – Made Ground / Cohesive | `"EPMC"` |
| 15 | Horizontal Earth Pressure | `"EH"` | 16 | Vertical Earth Pressure | `"EV"` |
| 17 | Earth Surcharge Load | `"ES"` | 18 | Locked in Erection Stresses | `"EL"` |
| 19 | Live Load Surcharge | `"LS"` | 20 | Trailer or Crawler Induced Surcharge | `"LSC"` |
| 21 | Live Load | `"L"` | 22 | Trailer or Crawler Induced Live Load | `"LC"` |
| 23 | Overload Live Load | `"LP"` | 24 | Live Load Impact | `"IL"` |
| 25 | Overload Live Load Impact | `"ILP"` | 26 | Centrifugal Force | `"CF"` |
| 27 | Braking Load | `"BRK"` | 28 | Longitudinal Force from Live Load | `"BK"` |
| 29 | Crowd Load | `"CRL"` | 30 | Prestress | `"PS"` |
| 31 | Buoyancy | `"B"` | 32 | Ground Water Pressure | `"WP"` |
| 33 | Fluid Pressure | `"FP"` | 34 | Stream Flow Pressure | `"SF"` |
| 35 | Wave Pressure | `"WPR"` | 36 | Wind Load on Structure | `"W"` |
| 37 | Wind Load on Live Load | `"WL"` | 38 | Settlement | `"STL"` |
| 39 | Creep | `"CR"` | 40 | Shrinkage | `"SH"` |
| 41 | Temperature | `"T"` | 42 | Temperature Gradient | `"TPG"` |
| 43 | Collision Load | `"CO"` | 44 | Vehicular Collision Force | `"CT"` |
| 45 | Vessel Collision Force | `"CV"` | 46 | Earthquake | `"E"` |
| 47 | Friction | `"FR"` | 48 | Ice Pressure | `"IP"` |
| 49 | Construction Stage Load | `"CS"` | 50 | Erection Load | `"ER"` |
| 51 | Rib Shortening | `"RS"` | 52 | Grade Effect | `"GE"` |
| 53 | Roof Live Load | `"LR"` | 54 | Snow Load | `"S"` |
| 55 | Rain Load | `"R"` | 56 | Longitudinal Force | `"LF"` |
| 57 | Raking Force | `"RF"` | 58 | Movement of Foundation | `"GD"` |
| 59 | Soil Heaving | `"SHV"` | 60 | Derailment Load | `"DRL"` |
| 61 | Across Wind Load | `"WA"` | 62 | Torsional Wind Load | `"WT"` |
| 63 | Vertical Earthquake | `"EVT"` | 64 | Earthquake Earth Pressure | `"EEP"` |
| 65 | Explosion Load | `"EX"` | 66 | Imperfection Load | `"I"` |
| 67 | Earthquake for Elastic | `"EE"` | | | |

### Python 示例

```python
# 创建静力荷载工况（POST）
stld_data = {
    "Assign": {
        "1": {"NAME": "DL",   "TYPE": "D",   "DESC": "Dead Load"},
        "2": {"NAME": "LL",   "TYPE": "L",   "DESC": "Live Load"},
        "3": {"NAME": "WX",   "TYPE": "W",   "DESC": "Wind Load X"},
        "4": {"NAME": "EX",   "TYPE": "E",   "DESC": "Earthquake X"},
        "5": {"NAME": "PS",   "TYPE": "PS",  "DESC": "Prestress"},
    }
}
result = midas_api("POST", "/db/STLD", stld_data)

# 查询全部（GET）
all_cases = midas_api("GET", "/db/STLD")

# 修改特定工况（PUT）
update_data = {
    "Assign": {
        "2": {"NAME": "LL",   "TYPE": "L",   "DESC": "Live Load (Revised)"}
    }
}
midas_api("PUT", "/db/STLD", update_data)

# 删除特定工况（DELETE）
midas_api("DELETE", "/db/STLD", {"Assign": {"5": {}}})
```

---

## 2. /db/BODF — Self-Weight

> 将自重(Self-Weight)施加到指定荷载工况。`FV` 数组为 [X, Y, Z] 方向的自重系数，通常使用 `[0, 0, -1]`。

**Input URI:** `{base url}/db/BODF`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "2": {
      "LCNAME": "D",
      "GROUP_NAME": "",
      "FV": [0, 0, -1]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 3 | Self-Weight Factor [X, Y, Z] | `"FV"` | Array \[Number, 3\] | - | Required |

### Python 示例

```python
# 施加自重（POST）— 无结构组，-Z 方向全部自重
bodf_data = {
    "Assign": {
        "1": {
            "LCNAME": "DL",      # 荷载工况名（在 STLD 中定义）
            "GROUP_NAME": "",    # 无结构组（整体结构）
            "FV": [0, 0, -1]     # X=0, Y=0, Z=-1（重力方向）
        }
    }
}
result = midas_api("POST", "/db/BODF", bodf_data)

# 查询
all_bodf = midas_api("GET", "/db/BODF")

# 修改 — 仅施加于特定结构组
update_data = {
    "Assign": {
        "1": {
            "LCNAME": "DL",
            "GROUP_NAME": "MainStructure",
            "FV": [0, 0, -1]
        }
    }
}
midas_api("PUT", "/db/BODF", update_data)

# 删除
midas_api("DELETE", "/db/BODF", {"Assign": {"1": {}}})
```

---

## 3. /db/CNLD — Nodal Loads

> 直接向节点施加集中力/力矩。键(key)为**节点编号**。

**Input URI:** `{base url}/db/CNLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "8": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "D",
          "GROUP_NAME": "",
          "FX": 10,
          "FY": 20,
          "FZ": 30,
          "MX": -40,
          "MY": -50,
          "MZ": -60
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Nodal Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Nodal Load – FX | `"FX"` | Number | 0 | Optional |
| (5) | Nodal Load – FY | `"FY"` | Number | 0 | Optional |
| (6) | Nodal Load – FZ | `"FZ"` | Number | 0 | Optional |
| (7) | Nodal Load – MX | `"MX"` | Number | 0 | Optional |
| (8) | Nodal Load – MY | `"MY"` | Number | 0 | Optional |
| (9) | Nodal Load – MZ | `"MZ"` | Number | 0 | Optional |

### Python 示例

```python
# 施加节点集中荷载（POST）
# 键 = 节点编号，用 ITEMS 数组可同时输入多个荷载工况
cnld_data = {
    "Assign": {
        "8": {   # 节点 8号
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "LL",   # 活荷载工况
                    "GROUP_NAME": "",
                    "FX": 0.0,
                    "FY": 0.0,
                    "FZ": -50.0,      # 50 kN (downward)
                    "MX": 0.0,
                    "MY": 0.0,
                    "MZ": 0.0
                }
            ]
        },
        "12": {   # 节点 12号
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "WX",
                    "GROUP_NAME": "",
                    "FX": 100.0,      # X方向风荷载
                    "FY": 0.0,
                    "FZ": 0.0,
                    "MX": 0.0,
                    "MY": 0.0,
                    "MZ": 0.0
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/CNLD", cnld_data)

# 查询
all_cnld = midas_api("GET", "/db/CNLD")

# 删除（删除节点 8号的集中荷载）
midas_api("DELETE", "/db/CNLD", {"Assign": {"8": {}}})
```

---

## 4. /db/BMLD — Beam Loads

> 向梁单元施加均布荷载·集中荷载·压力荷载等。键(key)为**单元编号**。

**Input URI:** `{base url}/db/BMLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构（均布荷载示例）

```json
{
  "Assign": {
    "115": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "L",
          "GROUP_NAME": "",
          "CMD": "BEAM",
          "TYPE": "UNILOAD",
          "DIRECTION": "GZ",
          "USE_PROJECTION": false,
          "USE_ECCEN": false,
          "D": [0, 1, 0, 0],
          "P": [-50, -50, 0, 0]
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Beam Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Load Classification (`"BEAM"` / `"LINE"` / `"TYPICAL"`) | `"CMD"` | String | - | Required |
| (5) | Load Type (`"CONLOAD"` / `"CONMOMENT"` / `"UNILOAD"` / `"UNIMOMENT"` / `"PRESSURE"`) | `"TYPE"` | String | - | Required |
| (6) | Direction (`"LX"` / `"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"`) | `"DIRECTION"` | String | - | Required |
| (7) | Projection | `"USE_PROJECTION"` | Boolean | false | Optional |
| (8) | Distance [x1, x2, x3, x4] | `"D"` | Array \[Number, 4\] | 0 | Optional |
| (9) | Load [v1, v2, v3, v4] | `"P"` | Array \[Number, 4\] | 0 | Optional |
| (10) | Eccentricity | `"USE_ECCEN"` | Boolean | false | Optional |
| (11) | Eccentricity Type (0=Centroid, 1=Offset) | `"ECCEN_TYPE"` | Integer | 0 | Optional |
| (12) | Eccentricity Direction (`"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"`) | `"ECCEN_DIR"` | String | - | Required |
| (13) | Distance I-End | `"I_END"` | Number | 0 | Optional |
| (14) | J-End Option | `"USE_J_END"` | Boolean | false | Optional |
| (15) | Distance J-End | `"J_END"` | Number | 0 | Optional |
| (16) | Additional H from Top Option | `"USE_ADDITIONAL"` | Boolean | false | Optional |
| (17) | Distance I-End (additional) | `"ADDITIONAL_I_END"` | Number | 0 | Optional |
| (18) | J-End Option (additional) | `"USE_ADDITIONAL_J_END"` | Boolean | false | Optional |
| (19) | Distance J-End (additional) | `"ADDITIONAL_J_END"` | Number | 0 | Optional |

### Python 示例

```python
# 施加梁单元荷载（POST）— 均布荷载与集中荷载
bmld_data = {
    "Assign": {
        "115": {   # 单元 115号
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "LL",
                    "GROUP_NAME": "",
                    "CMD": "BEAM",           # 一般梁单元
                    "TYPE": "UNILOAD",       # 均布荷载
                    "DIRECTION": "GZ",       # 整体坐标系 Z方向
                    "USE_PROJECTION": False,
                    "USE_ECCEN": False,
                    "D": [0, 1, 0, 0],       # 全长区段 [0~1（比例）]
                    "P": [-30.0, -30.0, 0, 0]  # -30 kN/m 均布
                }
            ]
        },
        "120": {   # 单元 120号 — 集中荷载
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "LL",
                    "GROUP_NAME": "",
                    "CMD": "BEAM",
                    "TYPE": "CONLOAD",       # 集中荷载
                    "DIRECTION": "GZ",
                    "USE_PROJECTION": False,
                    "USE_ECCEN": False,
                    "D": [0.5, 0, 0, 0],    # 单元中点（比例 0.5）
                    "P": [-100.0, 0, 0, 0]  # -100 kN
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/BMLD", bmld_data)

# 查询
all_bmld = midas_api("GET", "/db/BMLD")

# 删除
midas_api("DELETE", "/db/BMLD", {"Assign": {"115": {}}})
```

---

## 5. /db/SDSP — Specified Displacements of Support

> 定义支座强制位移（Settlement/Prescribed displacement）。键(key)为**节点编号**。

**Input URI:** `{base url}/db/SDSP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "LL",
          "GROUP_NAME": "",
          "VALUES": [
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 1.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 0.5},
            {"OPT_FLAG": true, "DISPLACEMENT": 0.5}
          ]
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Specified Displacement items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Displacements (Local) [Dx, Dy, Dz, Rx, Ry, Rz] | `"VALUES"` | Array \[Object, 6\] | Blank | Optional |
| i. | Usage Flag | `"OPT_FLAG"` | Boolean | false | Optional |
| ii. | Displacement Value | `"DISPLACEMENT"` | Real | 0 | Optional |

### Python 示例

```python
# 施加支座强制位移（POST）
# VALUES 数组：6 个元素 = [Dx, Dy, Dz, Rx, Ry, Rz]
sdsp_data = {
    "Assign": {
        "10": {   # 节点 10号
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "STL",        # 沉降荷载工况
                    "GROUP_NAME": "",
                    "VALUES": [
                        {"OPT_FLAG": True,  "DISPLACEMENT": -0.025},  # Dx = -25mm
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Dy（不使用）
                        {"OPT_FLAG": True,  "DISPLACEMENT": -0.050},  # Dz = -50mm
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Rx（不使用）
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Ry（不使用）
                        {"OPT_FLAG": False, "DISPLACEMENT": 0.0},      # Rz（不使用）
                    ]
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/SDSP", sdsp_data)

# 查询
all_sdsp = midas_api("GET", "/db/SDSP")

# 删除
midas_api("DELETE", "/db/SDSP", {"Assign": {"10": {}}})
```

---

## 6. /db/NMAS — Nodal Masses

> 在节点上定义集中质量。键(key)为**节点编号**。

**Input URI:** `{base url}/db/NMAS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "mX": 1,
      "mY": 2,
      "mZ": 3,
      "rmX": 4,
      "rmY": 5,
      "rmZ": 6
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Translational Mass – GCS X | `"mX"` | Number | - | Required |
| 2 | Translational Mass – GCS Y | `"mY"` | Number | 0 | Optional |
| 3 | Translational Mass – GCS Z | `"mZ"` | Number | 0 | Optional |
| 4 | Rotational Mass Moment of Inertia – X-axis | `"rmX"` | Number | 0 | Optional |
| 5 | Rotational Mass Moment of Inertia – Y-axis | `"rmY"` | Number | 0 | Optional |
| 6 | Rotational Mass Moment of Inertia – Z-axis | `"rmZ"` | Number | 0 | Optional |

### Python 示例

```python
# 定义节点质量（POST）
nmas_data = {
    "Assign": {
        "1":  {"mX": 500.0, "mY": 500.0, "mZ": 500.0, "rmX": 0.0, "rmY": 0.0, "rmZ": 0.0},
        "5":  {"mX": 750.0, "mY": 750.0, "mZ": 750.0, "rmX": 0.0, "rmY": 0.0, "rmZ": 0.0},
        "10": {"mX": 1000.0, "mY": 1000.0, "mZ": 1000.0,
               "rmX": 250.0, "rmY": 250.0, "rmZ": 500.0},
    }
}
result = midas_api("POST", "/db/NMAS", nmas_data)

# 查询
all_nmas = midas_api("GET", "/db/NMAS")

# 删除
midas_api("DELETE", "/db/NMAS", {"Assign": {"5": {}}})
```

---

## 7. /db/LTOM — Loads to Masses

> 将已有荷载工况的荷载转换为质量的设置。

**Input URI:** `{base url}/db/LTOM`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "DIR": "XYZ",
      "bNODAL": true,
      "bBEAM": true,
      "bFLOOR": true,
      "bPRES": true,
      "GRAV": 9.806,
      "vLC": [
        {"LCNAME": "D",  "FACTOR": 1.0},
        {"LCNAME": "L",  "FACTOR": 0.5}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Mass Direction (`"X"` / `"Y"` / `"Z"` / `"XY"` / `"YZ"` / `"XZ"` / `"XYZ"`) | `"DIR"` | String | - | Required |
| 2 | Nodal Load | `"bNODAL"` | Boolean | false | Optional |
| 3 | Beam Load | `"bBEAM"` | Boolean | false | Optional |
| 4 | Floor Load | `"bFLOOR"` | Boolean | false | Optional |
| 5 | Pressure (Hydrostatic) | `"bPRES"` | Boolean | false | Optional |
| 6 | Gravity Acceleration | `"GRAV"` | Number | 0 | Optional |
| 7 | Load Case List | `"vLC"` | Array \[Object\] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | - | Required |

### Python 示例

```python
# 荷载→质量转换设置（POST）
ltom_data = {
    "Assign": {
        "1": {
            "DIR": "XYZ",        # 3方向转换
            "bNODAL": True,      # 含节点集中荷载
            "bBEAM": True,       # 含梁单元荷载
            "bFLOOR": True,      # 含楼面荷载
            "bPRES": False,      # 除外水压力
            "GRAV": 9.806,       # 重力加速（m/s²）
            "vLC": [
                {"LCNAME": "DL", "FACTOR": 1.0},   # 恒荷载 100%
                {"LCNAME": "LL", "FACTOR": 0.25},  # 活荷载 25%
            ]
        }
    }
}
result = midas_api("POST", "/db/LTOM", ltom_data)

# 查询
all_ltom = midas_api("GET", "/db/LTOM")

# 删除
midas_api("DELETE", "/db/LTOM", {"Assign": {"1": {}}})
```

---

## 8. /db/NBOF — Nodal Body Force

> 由节点集中质量·荷载→质量·结构质量计算并施加惯性力（体积力）。

**Input URI:** `{base url}/db/NBOF`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构（节点列表方式）

```json
{
  "Assign": {
    "1": {
      "LCNAME": "E",
      "OPT_USE_GROUP": false,
      "KEY_NODE_ITEMS": [12, 42, 39, 40, 11, 41],
      "OPT_NODAL_MASS": true,
      "OPT_LOAD_TO_MASS": true,
      "OPT_STRUCT_MASS": true,
      "X": 10,
      "Y": 20,
      "Z": 30
    }
  }
}
```

### 请求体结构（结构组方式）

```json
{
  "Assign": {
    "2": {
      "LCNAME": "E",
      "OPT_USE_GROUP": true,
      "GROUP_NAME": "CrossBeam",
      "OPT_NODAL_MASS": true,
      "OPT_LOAD_TO_MASS": true,
      "OPT_STRUCT_MASS": true,
      "X": 10,
      "Y": 0,
      "Z": 0
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Nodal Mass | `"OPT_NODAL_MASS"` | Boolean | false | Optional |
| 3 | Load to Mass | `"OPT_LOAD_TO_MASS"` | Boolean | false | Optional |
| 4 | Structure Mass | `"OPT_STRUCT_MASS"` | Boolean | false | Optional |
| 5 | X-dir. Force Factor | `"X"` | Number | - | Required |
| 6 | Y-dir. Force Factor | `"Y"` | Number | 0 | Optional |
| 7 | Z-dir. Force Factor | `"Z"` | Number | 0 | Optional |
| 8 | Structure Group Option | `"OPT_USE_GROUP"` | Boolean | false | Optional |
| **OPT_USE_GROUP = true** | | | | | |
| 9 | Structure Group Name | `"GROUP_NAME"` | String | - | - |
| **OPT_USE_GROUP = false** | | | | | |
| 9 | Node No. List | `"KEY_NODE_ITEMS"` | Array \[Integer\] | - | - |

### Python 示例

```python
# 施加节点体积力（POST）
nbof_data = {
    "Assign": {
        "1": {
            "LCNAME": "EX",              # 地震作用工况
            "OPT_USE_GROUP": False,
            "KEY_NODE_ITEMS": [1, 2, 3, 4, 5],  # 应用节点列表
            "OPT_NODAL_MASS": True,
            "OPT_LOAD_TO_MASS": True,
            "OPT_STRUCT_MASS": True,
            "X": 1.0,    # X方向系数（地震加速系数）
            "Y": 0.0,
            "Z": 0.0
        }
    }
}
result = midas_api("POST", "/db/NBOF", nbof_data)

# 查询
all_nbof = midas_api("GET", "/db/NBOF")

# 删除
midas_api("DELETE", "/db/NBOF", {"Assign": {"1": {}}})
```

---

## 9. /db/PSLT — Define Pressure Load Type

> 定义作用于单元面/边的压力荷载类型。随后通过 `/db/PRES` 分配给单元。

**Input URI:** `{base url}/db/PSLT`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构（Plate Face – Uniform）

```json
{
  "Assign": {
    "1": {
      "NAME": "PlateUniform",
      "DESC": "Plate/PlaneStress(Face)",
      "ELEM_TYPE": "Plate/PlaneStress(Face)",
      "PRESSURE_LOAD_ITEMS": [
        {"LOADCASENAME": "DC", "LOADTYPE": "Uniform", "LOAD_P1": -20},
        {"LOADCASENAME": "DW", "LOADTYPE": "Linear",
         "LOAD_P1": -1, "LOAD_P2": -2, "LOAD_P3": -3, "LOAD_P4": -4}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Pressure Load Type Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | - | Required |
| 3 | Element Type | `"ELEM_TYPE"` | String | - | Required |
| 4 | Pressure Load items | `"PRESSURE_LOAD_ITEMS"` | Array \[Object\] | - | Required |
| (1) | Load Case Name | `"LOADCASENAME"` | String | - | Required |
| (2) | Load Type (`"Uniform"` / `"Linear"`) | `"LOADTYPE"` | String | - | Required |
| (3) | Load P1 ¹⁾ | `"LOAD_P1"` | Number | - | Required |
| (4) | Load P2 ¹⁾ | `"LOAD_P2"` | Number | 0 | Optional |
| (5) | Load P3 ¹⁾ | `"LOAD_P3"` | Number | 0 | Optional |
| (6) | Load P4 ¹⁾ | `"LOAD_P4"` | Number | 0 | Optional |

> ¹⁾ 各 Element Type 对 P1~P4 的可用情况（O=可用，-=不使用）：

| Element Type | Load Type | P1 | P2 | P3 | P4 |
|---|---|:---:|:---:|:---:|:---:|
| `"Plate/Plane Stress (Face)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | O | O |
| `"Plate/Plane Stress (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |
| `"Solid (Face)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | O | O |
| `"Plane Strain (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |
| `"Axisymmetric (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |
| `"Wall (Edge)"` | `"Uniform"` | O | - | - | - |
| | `"Linear"` | O | O | - | - |

### Python 示例

```python
# 定义压力荷载类型（POST）
pslt_data = {
    "Assign": {
        "1": {
            "NAME": "WaterPressure",
            "DESC": "Hydrostatic water pressure on wall",
            "ELEM_TYPE": "Plate/PlaneStress(Face)",
            "PRESSURE_LOAD_ITEMS": [
                {
                    "LOADCASENAME": "WP",   # Ground Water Pressure 工况
                    "LOADTYPE": "Uniform",
                    "LOAD_P1": -25.0        # -25 kN/m²
                }
            ]
        },
        "2": {
            "NAME": "EarthPressureWall",
            "DESC": "Linear earth pressure on retaining wall (edge)",
            "ELEM_TYPE": "Plate/PlaneStress(Edge)",
            "PRESSURE_LOAD_ITEMS": [
                {
                    "LOADCASENAME": "EP",
                    "LOADTYPE": "Linear",
                    "LOAD_P1": 0.0,         # 顶部 (top) 压力
                    "LOAD_P2": -40.0        # 底部 (bottom) 压力
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/PSLT", pslt_data)

# 查询
all_pslt = midas_api("GET", "/db/PSLT")

# 删除
midas_api("DELETE", "/db/PSLT", {"Assign": {"2": {}}})
```

---

## 10. /db/PRES — Assign Pressure Loads

> 将 `/db/PSLT` 中定义的压力荷载类型分配给实际单元。键(key)为**单元编号**。

**Input URI:** `{base url}/db/PRES`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构（Plate Face）

```json
{
  "Assign": {
    "116": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Element_Type1",
          "GROUP_NAME": "",
          "CMD": "PRES",
          "ELEM_TYPE": "PLATE",
          "FACE_EDGE_TYPE": "FACE",
          "DIRECTION": "LZ",
          "FORCES": [-10, 0, 0, 0, 0]
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Pressure Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Command Type (`"PRES"`) | `"CMD"` | String | `"PRES"` | Optional |
| (5) | Element Type (`"PLATE"` / `"SOLID"` / `"PLANE"`) | `"ELEM_TYPE"` | String | `"PLATE"` | Optional |
| (6) | Pressure Type (`"FACE"` / `"EDGE"` / `"PRES"`) | `"FACE_EDGE_TYPE"` | String | - | Required |
| (7) | Direction (`"NORMAL"` / `"LX"` / `"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"` / `"VECTOR"`) | `"DIRECTION"` | String | `"NORMAL"` | Optional |
| (8) | Vector [X, Y, Z] (if DIRECTION="VECTOR") | `"VECTORS"` | Array \[Number, 3\] | - | Optional |
| (9) | Projection (GX/GY/GZ only) | `"OPT_PROJECTION"` | Boolean | false | Optional |
| (10) | Face/Edge Number (Solid: 1~6, Plate/Plane: 1~4) | `"EDGE_FACE"` | Integer | - | Required |
| **FACE_EDGE_TYPE = "FACE" or "PRES"** | | | | | |
| (11) | Forces [PU,0,0,0,0] or [0,P1,P2,P3,P4] | `"FORCES"` | Array \[Number, 5\] | - | Required |
| **FACE_EDGE_TYPE = "EDGE"** | | | | | |
| (11) | Edge Loads [EPU,0,0] or [0,EP1,EP2] | `"EDGE_LOADS"` | Array \[Number, 3\] | - | Required |

> Direction 支持矩阵：

| ELEM_TYPE | FACE_EDGE_TYPE | NORMAL | LX | LY | LZ | GX | GY | GZ | VECTOR |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"PLATE"` | `"FACE"` | - | O | O | O | O | O | O | O |
| `"PLATE"` | `"EDGE"` | O | O | O | O | O | O | O | O |
| `"SOLID"` | `"PRES"` | O | O | O | O | O | O | O | O |
| `"PLANE"` | `"EDGE"` | O | O | O | O | - | - | - | O |

### Python 示例

```python
# 分配压力荷载（POST）
pres_data = {
    "Assign": {
        "116": {   # 单元 116号（Plate 单元）
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "WP",
                    "GROUP_NAME": "",
                    "CMD": "PRES",
                    "ELEM_TYPE": "PLATE",
                    "FACE_EDGE_TYPE": "FACE",
                    "DIRECTION": "NORMAL",   # 面法线方向
                    "EDGE_FACE": 1,
                    "FORCES": [-25.0, 0, 0, 0, 0]  # 均布 -25 kN/m²
                }
            ]
        },
        "320": {   # Solid 单元
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "EP",
                    "GROUP_NAME": "",
                    "CMD": "PRES",
                    "ELEM_TYPE": "SOLID",
                    "FACE_EDGE_TYPE": "PRES",
                    "DIRECTION": "NORMAL",
                    "EDGE_FACE": 1,          # Face #1
                    "FORCES": [0, -10, -30, -30, -10]  # 线性压力
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/PRES", pres_data)

# 查询
all_pres = midas_api("GET", "/db/PRES")

# 删除
midas_api("DELETE", "/db/PRES", {"Assign": {"116": {}}})
```

---

## 11. /db/PNLD — Define Plane Load Type

> 定义平面荷载类型（点·线·面）。随后通过 `/db/PNLA` 分配给单元。

**Input URI:** `{base url}/db/PNLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构（Point Load）

```json
{
  "Assign": {
    "1": {
      "NAME": "Point_examples",
      "DESC": "API_example",
      "LTYPE": "POINT",
      "POINTLOAD": [
        {"X": 0, "Y": 0, "F": -10},
        {"X": 1, "Y": -1, "F": 10.5}
      ],
      "COPY_X": [5, 5, 5],
      "COPY_Y": [3, 3]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Type Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Load Type (`"POINT"` / `"LINE"` / `"AREA"`) | `"LTYPE"` | String | - | Required |
| 4 | Copy in X-Direction | `"COPY_X"` | Array \[Number\] | - | Required |
| 5 | Copy in Y-Direction | `"COPY_Y"` | Array \[Number\] | - | Required |
| 6 | Sequence Number (Unique) | `"SEQ"` | Integer | Auto | Optional |
| **LTYPE = "POINT"** | | | | | |
| 7 | Point Loads | `"POINTLOAD"` | Array \[Object\] | - | Required |
| (1) | Point X | `"X"` | Number | 0 | Optional |
| (2) | Point Y | `"Y"` | Number | 0 | Optional |
| (3) | Force | `"F"` | Number | 0 | Optional |
| **LTYPE = "LINE"** | | | | | |
| 7 | Line Loads | `"LINELOAD"` | Object | - | Required |
| (1) | Uniform (true) / Trapezoidal (false) | `"bUNIFORM"` | Boolean | true | Optional |
| (2) | Coordinates of X1, X2 | `"X"` | Array \[Number, 2\] | 0 | Optional |
| (3) | Coordinates of Y1, Y2 | `"Y"` | Array \[Number, 2\] | 0 | Optional |
| (4) | Force (Uniform: [F1] / Trap: [F1, F2]) | `"F"` | Array \[Number, 2\] | 0 | Optional |
| **LTYPE = "AREA"** | | | | | |
| 7 | Area Loads | `"AREALOAD"` | Object | - | Required |
| (1) | Uniform (true) / Trapezoidal (false) | `"bUNIFORM"` | Boolean | false | Optional |
| (2) | 3 Points (true) / 4 Points (false) | `"b3PNT"` | Boolean | false | Optional |
| (3) | Coordinates X1~X4 | `"X"` | Array \[Number, 4\] | 0 | Optional |
| (4) | Coordinates Y1~Y4 | `"Y"` | Array \[Number, 4\] | 0 | Optional |
| (5) | Load (Uniform: [F1] / Trap: [F1,F2,F3,F4]) | `"LOAD"` | Array \[Number, 4\] | 0 | Optional |

### Python 示例

```python
# 定义平面荷载类型（POST）— 均布面荷载
pnld_data = {
    "Assign": {
        "1": {
            "NAME": "UniformAreaLoad",
            "DESC": "Uniform load on floor area",
            "LTYPE": "AREA",
            "COPY_X": [0],    # 无复制
            "COPY_Y": [0],
            "AREALOAD": {
                "bUNIFORM": True,    # 均布荷载
                "b3PNT": False,      # 由4点定义
                "X": [0, 5, 5, 0],  # 横向 5m
                "Y": [0, 0, 4, 4],  # 纵向 4m
                "LOAD": [-5.0, -5.0, -5.0, -5.0]  # -5 kN/m²
            }
        },
        "2": {
            "NAME": "LineLoadOnEdge",
            "DESC": "Line load along beam edge",
            "LTYPE": "LINE",
            "COPY_X": [0],
            "COPY_Y": [0],
            "LINELOAD": {
                "bUNIFORM": True,
                "X": [0, 6],     # X: 0~6m
                "Y": [0, 0],     # Y: 固定
                "F": [-10.0]     # -10 kN/m 均布
            }
        }
    }
}
result = midas_api("POST", "/db/PNLD", pnld_data)

# 查询
all_pnld = midas_api("GET", "/db/PNLD")

# 删除
midas_api("DELETE", "/db/PNLD", {"Assign": {"2": {}}})
```

---

## 12. /db/PNLA — Assign Plane Loads

> 将 `/db/PNLD` 中定义的平面荷载类型按坐标系分配给实际单元。

**Input URI:** `{base url}/db/PNLA`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "LCNAME": "AssignPlaneExample",
      "PNLD_KEY": 1,
      "ELEM_TYPE": "PLATE",
      "POINT_ORIGIN": [18, 2, 0],
      "AXIS_X": [19, 2, 0],
      "AXIS_Y": [19, 3, 0],
      "TOL": 0.0009144,
      "SELECT_TYPE": "ON_PLANE",
      "LOAD_DIR": "GLOBAL_Z",
      "PROJECT_TYPE": "NO"
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Load Group Name | `"LOAD_GROUP"` | String | - | Required |
| 3 | Defined Plane Load Key | `"PNLD_KEY"` | Integer | - | Required |
| 4 | Element Type (`"PLATE"` / `"SOLID"`) | `"ELEM_TYPE"` | String | - | Required |
| 5 | First Point / Origin [x, y, z] | `"POINT_ORIGIN"` | Array \[Number, 3\] | - | Required |
| 6 | Second Point / on x-Axis [x, y, z] | `"AXIS_X"` | Array \[Number, 3\] | - | Required |
| 7 | Third Point / on x-y Plane [x, y, z] | `"AXIS_Y"` | Array \[Number, 3\] | - | Required |
| 8 | Tolerance | `"TOL"` | Number | - | Required |
| 9 | Element Selection (`"ON_PLANE"` / `"IN_GROUP"`) | `"SELECT_TYPE"` | String | - | Required |
| 10 | Load Direction (`"NORMAL_PLANE"` / `"NORMAL_ELEM"` / `"GLOBAL_X"` / `"GLOBAL_Y"` / `"GLOBAL_Z"`) | `"LOAD_DIR"` | String | - | Required |
| 11 | Projection Type (`"NO"` / `"LOAD_DIR"` / `"LOAD_PLANE"`) | `"PROJECT_TYPE"` | String | - | Required |
| 12 | Description | `"DESC"` | String | Blank | Optional |
| **ELEM_TYPE = "PLATE"** | | | | | |
| 13 | Node Defining Loading Area | `"bDEFINE_NODE"` | Boolean | false | Optional |
| 14 | Loading Boundary Connecting Node | `"CONNECT_NODE"` | Array \[Integer, 15\] | - | Optional |
| **SELECT_TYPE = "IN_GROUP"** | | | | | |
| 13 | Element Group Name | `"ELEM_GROUP"` | String | - | Optional |
| **ELEM_TYPE = "SOLID"** | | | | | |
| 14 | Solid Face No. (1~6) | `"FACE_NO"` | Integer | - | Optional |

> ✅ **2026-09-06 部分解决确认：** 原文该条件的 Key 曾误记为 `"SELECT_TYPE"`，
> 经 2026-09-01 更新更正为 `"ELEM_TYPE"`，已与上表写法一致（应为 2026-08-27 错误提报
> Jira `MAPI-2484` 的反映结果）。
>
> ⚠️ 但同一行的**说明文字仍为 `Element Select Type`**（原文照录：
> `When Element Select Type, "ELEM_TYPE" is "SOLID"`）。同一张表的第一个条件行
> 正确写为 `When Element Type, "ELEM_TYPE" is "PLATE"`，可见仅说明文字尚未更正 —
> 属剩余错误提报对象。

### Python 示例

```python
# 分配平面荷载（POST）
pnla_data = {
    "Assign": {
        "1": {
            "LCNAME": "LL",
            "LOAD_GROUP": "LiveLoadGroup",
            "PNLD_KEY": 1,                   # 在 PNLD 中定义的键
            "ELEM_TYPE": "PLATE",
            "POINT_ORIGIN": [0.0, 0.0, 3.0], # 荷载平面原点
            "AXIS_X":       [1.0, 0.0, 3.0], # 定义 x轴方向的点
            "AXIS_Y":       [1.0, 1.0, 3.0], # 定义 x-y 平面的点
            "TOL": 0.001,
            "SELECT_TYPE": "ON_PLANE",
            "LOAD_DIR": "GLOBAL_Z",
            "PROJECT_TYPE": "NO",
            "DESC": "3层楼面活荷载"
        }
    }
}
result = midas_api("POST", "/db/PNLA", pnla_data)

# 查询
all_pnla = midas_api("GET", "/db/PNLA")

# 删除
midas_api("DELETE", "/db/PNLA", {"Assign": {"1": {}}})
```

---

## 13. /db/FBLD — Define Floor Load Type

> 定义楼面荷载类型(Floor Load Type)。按各荷载工况存放面荷载取值。

**Input URI:** `{base url}/db/FBLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "NAME": "Floor_example",
      "DESC": "",
      "ITEM": [
        {"LCNAME": "DC",  "FLOOR_LOAD": 10, "OPT_SUB_BEAM_WEIGHT": true},
        {"LCNAME": "DW",  "FLOOR_LOAD": 20, "OPT_SUB_BEAM_WEIGHT": true}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Floor Load Type Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Floor Load items | `"ITEM"` | Array \[Object\] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Floor Load (kN/m² or equivalent) | `"FLOOR_LOAD"` | Number | - | Required |
| (3) | Consider Sub Beam Weight | `"OPT_SUB_BEAM_WEIGHT"` | Boolean | false | Optional |

### Python 示例

```python
# 定义楼面荷载类型（POST）
fbld_data = {
    "Assign": {
        "1": {
            "NAME": "TypicalFloor",
            "DESC": "一般层恒荷载 + 活荷载",
            "ITEM": [
                {"LCNAME": "DL", "FLOOR_LOAD": 4.0,  "OPT_SUB_BEAM_WEIGHT": True},
                {"LCNAME": "LL", "FLOOR_LOAD": 2.5,  "OPT_SUB_BEAM_WEIGHT": False},
            ]
        },
        "2": {
            "NAME": "RoofFloor",
            "DESC": "屋面荷载",
            "ITEM": [
                {"LCNAME": "DL", "FLOOR_LOAD": 3.5,  "OPT_SUB_BEAM_WEIGHT": True},
                {"LCNAME": "LL", "FLOOR_LOAD": 1.0,  "OPT_SUB_BEAM_WEIGHT": False},
                {"LCNAME": "S",  "FLOOR_LOAD": 0.5,  "OPT_SUB_BEAM_WEIGHT": False},
            ]
        }
    }
}
result = midas_api("POST", "/db/FBLD", fbld_data)

# 查询
all_fbld = midas_api("GET", "/db/FBLD")

# 删除
midas_api("DELETE", "/db/FBLD", {"Assign": {"2": {}}})
```

---

## 14. /db/FBLA — Assign Floor Loads

> 将 `/db/FBLD` 中定义的楼面荷载类型分配给由节点构成的区域。

**Input URI:** `{base url}/db/FBLA`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构（One-Way 分配）

```json
{
  "Assign": {
    "1": {
      "FLOOR_LOAD_TYPE_NAME": "Floor_example",
      "FLOOR_DIST_TYPE": 1,
      "LOAD_ANGLE": 0,
      "SUB_BEAM_NUM": 2,
      "SUB_BEAM_ANGLE": 90,
      "UNIT_SELF_WEIGHT": 10,
      "DIR": "GZ",
      "OPT_PROJECTION": false,
      "DESC": "",
      "OPT_EXCLUDE_INNER_ELEM_AREA": true,
      "GROUP_NAME": "LoadGroup2",
      "NODES": [508, 509, 511, 510]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Floor Load Type Name | `"FLOOR_LOAD_TYPE_NAME"` | String | - | Required |
| 2 | Distribution Type (1=One Way / 2=Two Way / 3=Polygon-Centroid / 4=Polygon-Length) | `"FLOOR_DIST_TYPE"` | Integer | - | Required |
| 3 | Load Direction (`"LX"` / `"LY"` / `"LZ"` / `"GX"` / `"GY"` / `"GZ"`) | `"DIR"` | String | `"LX"` | Optional |
| 4 | Projection | `"OPT_PROJECTION"` | Boolean | false | Optional |
| 5 | Description | `"DESC"` | String | Blank | Optional |
| 6 | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 7 | Nodes defining Loading Area | `"NODES"` | Array \[Integer\] | - | Required |
| **FLOOR_DIST_TYPE = 1** | | | | | |
| 8 | Load Angle (A1) | `"LOAD_ANGLE"` | Number | 0 | Optional |
| **FLOOR_DIST_TYPE = 2** | | | | | |
| 8 | Allow Polygon Type Unit Area | `"OPT_ALLOW_POLYGON_TYPE_UNIT_AREA"` | Boolean | false | Optional |
| **FLOOR_DIST_TYPE = 1 or 2** | | | | | |
| 9 | Exclude Inner Element of Area | `"OPT_EXCLUDE_INNER_ELEM_AREA"` | Boolean | false | Optional |
| 10 | No. of Sub Beams | `"SUB_BEAM_NUM"` | Integer | 0 | Optional |
| 11 | Sub-Beam Angle (A2) | `"SUB_BEAM_ANGLE"` | Number | 0 | Optional |
| 12 | Unit Self Weight | `"UNIT_SELF_WEIGHT"` | Number | 0 | Optional |

### Python 示例

```python
# 分配楼面荷载（POST）
fbla_data = {
    "Assign": {
        "1": {
            "FLOOR_LOAD_TYPE_NAME": "TypicalFloor",  # 在 FBLD 中定义的名称
            "FLOOR_DIST_TYPE": 2,    # Two Way 分配
            "DIR": "GZ",
            "OPT_PROJECTION": False,
            "DESC": "3层楼面区域",
            "GROUP_NAME": "FloorLoads",
            "NODES": [101, 102, 103, 104],  # 楼面区域节点
            "SUB_BEAM_NUM": 0,
            "UNIT_SELF_WEIGHT": 0.0
        },
        "2": {
            "FLOOR_LOAD_TYPE_NAME": "RoofFloor",
            "FLOOR_DIST_TYPE": 3,    # Polygon-Centroid
            "DIR": "GZ",
            "OPT_PROJECTION": False,
            "DESC": "屋面区域",
            "GROUP_NAME": "RoofLoads",
            "NODES": [201, 202, 203, 204, 205]
        }
    }
}
result = midas_api("POST", "/db/FBLA", fbla_data)

# 查询
all_fbla = midas_api("GET", "/db/FBLA")

# 删除
midas_api("DELETE", "/db/FBLA", {"Assign": {"2": {}}})
```

---

## 15. /db/FMLD — Finishing Material Loads

> 定义柱/梁单元周围的面层材料荷载(Finishing Material Load)。键(key)为**单元编号**。

**Input URI:** `{base url}/db/FMLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "448": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "FMLD_examples",
          "GROUP_NAME": "LoadGroups",
          "COVERING_TYPE": "ENVELOP",
          "COVERING_RANGE": ["HALF", "HALF", "FULL", "FULL"],
          "THICKNESS": 0.2,
          "DENSITY": 24.5,
          "DIR": "GZ",
          "SCALE_FACTOR": 1.0
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Finishing Material Load items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Covering Type (`"ENVELOP"` / `"FILL"` / `"SURROUND"`) | `"COVERING_TYPE"` | String | `"ENVELOP"` | Optional |
| (5) | Covering Range [+x, -y, -x, +y] (`"FULL"` / `"HALF"`) | `"COVERING_RANGE"` | Array \[String, 4\] | - | Required |
| (6) | Covering Thickness (d) | `"THICKNESS"` | Number | 0 | Optional |
| (7) | Filling Property (Density) | `"DENSITY"` | Number | 0 | Optional |
| (8) | Direction (`"GX"` / `"GY"` / `"GZ"`) | `"DIR"` | String | `"GZ"` | Optional |
| (9) | Scale Factor | `"SCALE_FACTOR"` | Number | 0 | Required |

### Python 示例

```python
# 定义面层材料荷载（POST）
fmld_data = {
    "Assign": {
        "200": {   # 单元 200号（柱）
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "DL",
                    "GROUP_NAME": "",
                    "COVERING_TYPE": "ENVELOP",   # 外覆型
                    "COVERING_RANGE": ["FULL", "FULL", "FULL", "FULL"],  # 4面全部
                    "THICKNESS": 0.05,     # 50mm 面层
                    "DENSITY": 20.0,       # 20 kN/m³
                    "DIR": "GZ",
                    "SCALE_FACTOR": 1.0
                }
            ]
        }
    }
}
result = midas_api("POST", "/db/FMLD", fmld_data)

# 查询
all_fmld = midas_api("GET", "/db/FMLD")

# 删除
midas_api("DELETE", "/db/FMLD", {"Assign": {"200": {}}})
```

---

## 16. /db/POSP — Parameter of Soil Properties

> 定义土压力计算所用地基特性参数。

**Input URI:** `{base url}/db/POSP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "NAME": "Soil-1",
      "DESC": "",
      "OPT_USE_N": false,
      "GROUND_LEVEL": 6,
      "BEDROCK_LEVEL": -21,
      "FOOTING_LEVEL": -17.5,
      "ITEMS": [
        {"HEIGHT": 7,  "ANGLE_OR_N": 30, "DENSITY": 17, "VS": 160, "KH": 11449, "DISP": 0.001},
        {"HEIGHT": 1,  "ANGLE_OR_N": 30, "DENSITY": 17, "VS": 160, "KH": 11449, "DISP": 0.001}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Soil Properties Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Use N Value (true=N值 / false=内摩擦角) | `"OPT_USE_N"` | Number | false | Optional |
| 4 | Level of Ground Surface | `"GROUND_LEVEL"` | Number | - | Required |
| 5 | Level of Bedrock | `"BEDROCK_LEVEL"` | Number | - | Required |
| 6 | Level of Footing Bottom | `"FOOTING_LEVEL"` | Number | - | Required |
| 7 | Soil Characteristic items | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Soil Layer Thickness | `"HEIGHT"` | Number | - | Required |
| (2) | Internal Friction Angle or N Value | `"ANGLE_OR_N"` | Number | - | Required |
| (3) | Unit Volume Weight of Soil | `"DENSITY"` | Number | - | Required |
| (4) | Shear Wave Velocity | `"VS"` | Number | - | Required |
| (5) | Coeff. of Horizontal Ground Reaction | `"KH"` | Number | - | Required |
| (6) | Relative Displacement | `"DISP"` | Number | - | Required |

### Python 示例

```python
# 定义地基特性参数（POST）
posp_data = {
    "Assign": {
        "1": {
            "NAME": "SiteA-Soil",
            "DESC": "A 场地地基特性",
            "OPT_USE_N": False,       # 以内摩擦角为准
            "GROUND_LEVEL": 0.0,      # GL±0
            "BEDROCK_LEVEL": -25.0,   # 基岩 GL-25m
            "FOOTING_LEVEL": -10.0,   # 基础底面 GL-10m
            "ITEMS": [
                # [土层厚度, 内摩擦角(°), 单位重(kN/m³), 剪切波速, 水平地基反力系数, 相对位移]
                {"HEIGHT": 5.0,  "ANGLE_OR_N": 28, "DENSITY": 17.0, "VS": 150, "KH": 10000, "DISP": 0.001},
                {"HEIGHT": 5.0,  "ANGLE_OR_N": 32, "DENSITY": 18.0, "VS": 200, "KH": 20000, "DISP": 0.001},
                {"HEIGHT": 15.0, "ANGLE_OR_N": 35, "DENSITY": 19.0, "VS": 300, "KH": 50000, "DISP": 0.001},
            ]
        }
    }
}
result = midas_api("POST", "/db/POSP", posp_data)

# 查询
all_posp = midas_api("GET", "/db/POSP")

# 删除
midas_api("DELETE", "/db/POSP", {"Assign": {"1": {}}})
```

---

## 17. /db/EPST — Static Earth Pressure

> 计算静力土压力并施加到墙单元。

**Input URI:** `{base url}/db/EPST`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "LOADCASE": "HsX(+)",
      "DIR": "XY",
      "ANGLE": 0,
      "IN_PT": [5000, 0, 0],
      "SF": 1,
      "EP_TYPE": "AT_REST",
      "SURCHARGE_LOAD": 16,
      "WATER_LEVEL": -4.7,
      "SOIL_PROP": "Soil-1",
      "SEL_TYPE": "GRUP",
      "ELEM_TYPE": "FRAME",
      "LOADING_AREA_GROUP": 1,
      "PRES_PROFILE_ITEMS": [
        {"LEVEL": 6,   "SOIL_PRES": 8,   "ADD_PRES": 0},
        {"LEVEL": -1,  "SOIL_PRES": 12,  "ADD_PRES": 0}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LOADCASE"` | String | - | Required |
| 2 | Load Direction (`"XY"` / `"NORMAL"`) | `"DIR"` | String | `"XY"` | Optional |
| 3 | Static Earth Pressure Angle | `"ANGLE"` | Number | - | Required |
| 4 | Inner Point | `"IN_PT"` | Array \[Number\] | - | Optional |
| 5 | Scale Factor | `"SF"` | Number | - | Required |
| 6 | EP Type (`"AT_REST"` / `"ACTIVE"`) | `"EP_TYPE"` | String | - | Required |
| 7 | Surcharge Load | `"SURCHARGE_LOAD"` | Number | - | Required |
| 8 | Water Level | `"WATER_LEVEL"` | Number | - | Required |
| 9 | Soil Properties Name | `"SOIL_PROP"` | String | - | Required |
| 10 | Selection Type (`"GRUP"` / `"ELEMENT"`) | `"SEL_TYPE"` | String | - | Required |
| 11 | Element Type (`"FRAME"` / `"PLANAR"`) | `"ELEM_TYPE"` | String | - | Required |
| 12 | Node List | `"NODE_LIST"` | Array \[Integer\] | - | Optional |
| 13 | Element List | `"ELEM_LIST"` | Array \[Integer\] | - | Optional |
| 14 | Loading Area Group Name | `"LOADING_AREA_GROUP"` | Integer | - | Optional |
| 15 | Pressure Profile items | `"PRES_PROFILE_ITEMS"` | Array \[Object\] | - | Optional |
| (1) | Level of pressure profile point | `"LEVEL"` | Number | - | Required |
| (2) | Soil pressure at level | `"SOIL_PRES"` | Number | - | Required |
| (3) | Additional pressure at level | `"ADD_PRES"` | Number | - | Required |

### Python 示例

```python
# 施加静力土压力（POST）
epst_data = {
    "Assign": {
        "1": {
            "LOADCASE": "EP",
            "DIR": "XY",
            "ANGLE": 0.0,
            "IN_PT": [0, 0, 0],
            "SF": 1.0,
            "EP_TYPE": "AT_REST",         # 静止土压力
            "SURCHARGE_LOAD": 10.0,       # 超载 10 kN/m²
            "WATER_LEVEL": -5.0,          # 地下水位 GL-5m
            "SOIL_PROP": "SiteA-Soil",    # 在 POSP 中定义
            "SEL_TYPE": "ELEMENT",
            "ELEM_TYPE": "FRAME",
            "ELEM_LIST": [501, 502, 503, 504],  # 目标单元
            "PRES_PROFILE_ITEMS": [
                {"LEVEL": 0.0,  "SOIL_PRES": 0.0,  "ADD_PRES": 5.0},
                {"LEVEL": -5.0, "SOIL_PRES": 42.5, "ADD_PRES": 5.0},
                {"LEVEL": -10.0,"SOIL_PRES": 90.0, "ADD_PRES": 5.0},
            ]
        }
    }
}
result = midas_api("POST", "/db/EPST", epst_data)

# 查询
all_epst = midas_api("GET", "/db/EPST")

# 删除
midas_api("DELETE", "/db/EPST", {"Assign": {"1": {}}})
```

---

## 18. /db/EPSE — Seismic Earth Pressure

> 计算地震时的动力土压力并施加到墙单元。

**Input URI:** `{base url}/db/EPSE`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "LOADCASE": "HaX(+)",
      "DIR": "XY",
      "ANGLE": 0,
      "IN_PT": [0, 0, 0],
      "SF": 1,
      "CODE": "KDS(41-17-00:2019)",
      "SEIS_LOAD": "KDS(2019)",
      "LAYER_PARAM": "SINGLE",
      "LAYER_LV": 0,
      "SOIL_PROP": "Soil-1",
      "SEL_TYPE": "ELEMENT",
      "ELEM_TYPE": "PLANAR",
      "NODE_LIST": [3461, 3831, 4856, 5597],
      "ELEM_LIST": [18451],
      "PRES_PROFILE_ITEMS": []
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LOADCASE"` | String | - | Required |
| 2 | Load Direction (`"XY"` / `"NORMAL"`) | `"DIR"` | String | `"XY"` | Optional |
| 3 | Seismic Earth Pressure Angle | `"ANGLE"` | Number | 0 | Optional |
| 4 | Inner Point | `"IN_PT"` | Number | - | Optional |
| 5 | Scale Factor | `"SF"` | Number | - | Optional |
| 6 | Design Code | `"CODE"` | String | - | Optional |
| 7 | Seismic Load Name | `"SEIS_LOAD"` | String | - | Required |
| 8 | Soil Layer Parameter (`"SINGLE"` / `"DOUBLE"`) | `"LAYER_PARAM"` | String | `"SINGLE"` | Optional |
| 9 | Soil Second Layer Level (Double Cosine) | `"LAYER_LV"` | Number | 0 | Optional |
| 10 | Soil Properties Name | `"SOIL_PROP"` | String | - | Required |
| 11 | Selection Type (`"GROUP"` / `"ELEMENT"`) | `"SEL_TYPE"` | String | - | Required |
| 12 | Element Type (`"FRAME"` / `"PLANAR"`) | `"ELEM_TYPE"` | String | `"ELEM"` | Optional |
| 13 | Node List | `"NODE_LIST"` | Array \[Integer\] | - | Optional |
| 14 | Element List | `"ELEM_LIST"` | Array \[Integer\] | - | Optional |
| 15 | Loading Area Group Name | `"LOADING_AREA_GROUP"` | Integer | - | Optional |
| 16 | Pressure Profile items | `"PRES_PROFILE_ITEMS"` | Array \[Object\] | - | Optional |
| (1) | Level | `"LEVEL"` | Number | - | Required |
| (2) | Horizontal Coefficient KH | `"KH"` | Number | - | Required |
| (3) | Relative Displacement | `"REL_DISP"` | Number | - | Required |
| (4) | Seismic Pressure | `"SEIS_PRES"` | Number | - | Required |
| (5) | Additional Pressure | `"ADD_PRES"` | Number | - | Optional |

### Python 示例

```python
# 施加地震土压力（POST）
epse_data = {
    "Assign": {
        "1": {
            "LOADCASE": "EEP",             # 地震土压力荷载工况
            "DIR": "XY",
            "ANGLE": 0.0,
            "IN_PT": [0, 0, 0],
            "SF": 1.0,
            "CODE": "KDS(41-17-00:2019)",
            "SEIS_LOAD": "KDS(2019)",       # 在 POSL 中定义的名称
            "LAYER_PARAM": "SINGLE",
            "LAYER_LV": 0.0,
            "SOIL_PROP": "SiteA-Soil",
            "SEL_TYPE": "ELEMENT",
            "ELEM_TYPE": "FRAME",
            "ELEM_LIST": [501, 502, 503],
            "PRES_PROFILE_ITEMS": [
                {"LEVEL": 0.0,  "KH": 0.15, "REL_DISP": 0.01, "SEIS_PRES": 12.5, "ADD_PRES": 0.0},
                {"LEVEL": -10.0,"KH": 0.15, "REL_DISP": 0.01, "SEIS_PRES": 37.5, "ADD_PRES": 0.0},
            ]
        }
    }
}
result = midas_api("POST", "/db/EPSE", epse_data)

# 查询
all_epse = midas_api("GET", "/db/EPSE")

# 删除
midas_api("DELETE", "/db/EPSE", {"Assign": {"1": {}}})
```

---

## 19. /db/POSL — Parameter of Seismic Loads

> 定义静力地震作用计算所需的地震作用参数（基于 KDS 41-17-00:2019）。

**Input URI:** `{base url}/db/POSL`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "NAME": "KDS(2019)",
      "CODE": "KDS(41-17-00:2019)",
      "METHOD": "RES_DISP",
      "SZ": "1",
      "EPA": 0.22,
      "SC": "S1",
      "FA": 1.12,
      "FV": 0.84,
      "SDS": 0.41066666666666674,
      "SD1": 0.12319999999999999,
      "USER_GROUP": "1",
      "IF": 1.2,
      "RMF": 3
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"NAME"` | String | - | Required |
| 2 | Seismic Load Code | `"CODE"` | String | - | Optional |
| 3 | Seismic Calculation Method (`"RES_DISP"` / `"EQV_STATIC"`) | `"METHOD"` | String | - | Optional |
| 4 | Seismic Zone | `"SZ"` | String | - | Required |
| 5 | Effective Peak Ground Acceleration | `"EPA"` | Number | - | Required |
| 6 | Site Class | `"SC"` | String | - | Required |
| 7 | Short-period Site Coefficient | `"FA"` | Number | - | Required |
| 8 | Long-period Site Coefficient | `"FV"` | Number | - | Required |
| 9 | Design Spectral Acceleration at Short Period | `"SDS"` | Number | - | Required |
| 10 | Design Spectral Acceleration at 1-sec Period | `"SD1"` | Number | - | Required |
| 11 | Seismic User Group | `"USER_GROUP"` | String | - | Optional |
| 12 | Importance Factor | `"IF"` | Number | - | Required |
| 13 | Response Modification Factor | `"RMF"` | Number | - | Required |

### Python 示例

```python
# 定义地震作用参数（POST）— KDS 41-17-00:2019
posl_data = {
    "Assign": {
        "1": {
            "NAME": "KDS2019",
            "CODE": "KDS(41-17-00:2019)",
            "METHOD": "EQV_STATIC",    # 等效静力法
            "SZ": "1",                 # 地震分区 I
            "EPA": 0.22,               # 有效峰值地面加速度
            "SC": "S2",                # 场地类别（S2）
            "FA": 1.0,                 # 短周期场地放大系数
            "FV": 1.4,                 # 长周期场地放大系数
            "SDS": 0.2933,             # 短周期设计反应谱
            "SD1": 0.1467,             # 1秒设计反应谱
            "USER_GROUP": "1",         # 抗震等级 I
            "IF": 1.5,                 # 重要性系数
            "RMF": 3.0                 # 反应修正系数
        }
    }
}
result = midas_api("POST", "/db/POSL", posl_data)

# 查询
all_posl = midas_api("GET", "/db/POSL")

# 删除
midas_api("DELETE", "/db/POSL", {"Assign": {"1": {}}})
```

---

## 20. /db/SWIND — Static Wind Load

> 定义基于 KDS 41-12:2022 的静力风荷载。按 `INPUT_METHOD` 的取值选择 Simplified / General / Vortex Shedding 方法。将 `WIND_CODE` 指定为 `"USER TYPE"` 时，也可使用直接输入逐层风压的方式（见下方 ADDITIONAL 参考）。

**Input URI:** `{base url}/db/SWIND`  
**Active Methods:** `POST, GET, PUT, DELETE`

> **参考：** URL 路径中使用 `DB/SWIND`（大写）。

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Wind Load Code (`"KDS(41-12: 2022)"`) | `"WIND_CODE"` | string (enum) | - | Required |
| 2 | Description | `"DESC"` | string | `""` | Optional |
| 3 | Scale Factor X | `"SCALE_FACTOR_X"` | number | - | Required |
| 4 | Scale Factor Y | `"SCALE_FACTOR_Y"` | number | - | Required |
| 5 | KDS(41-12:2022) Parameters | `"PARAMETERS"` | object | - | Required |
| (1) | Input Method (0=Simplified / 1=General / 2=General+Vortex) | `"INPUT_METHOD"` | integer (enum) | - | Required |
| **INPUT_METHOD = 0 (Simplified)** | | | | | |
| | Basic Wind Speed | `"WIND_SPEED"` | number | - | Required |
| | Roof Height | `"ROOF_HEIGHT"` | number | system | Optional |
| | Exposure Coefficient CE | `"CE"` | number | 1 | Optional |
| **INPUT_METHOD = 1 (General)** | | | | | |
| | Exposure Category (0=A / 1=B / 2=C / 3=D) | `"EXP_CATEGORY"` | integer (enum) | - | Required |
| | Basic Wind Speed | `"WIND_SPEED"` | number | - | Required |
| | Importance Factor | `"IMPORTANCE_FACTOR"` | number | - | Required |
| | Roof Height | `"ROOF_HEIGHT"` | number | system | Optional |
| | Topographic Effect | `"TOPOGRAPHIC_EFFECT"` | object | - | Optional |
| a | Use Topographic Effect | `"OPT_USE"` | boolean | false | Optional |
| a | Topographic Factor KZT (OPT_USE=true) | `"KZT"` | number | - | Conditional |
| | Direction Factor X | `"DIRECTION_FACTOR_X"` | number | 1 | Optional |
| | Direction Factor Y | `"DIRECTION_FACTOR_Y"` | number | 1 | Optional |
| | Rigidity Classification | `"RIGIDITY"` | integer | - | Required |
| | Gust Factor X | `"GUST_FACTOR_X"` | number | - | Required |
| | Gust Factor Y | `"GUST_FACTOR_Y"` | number | - | Required |
| | Force Coefficient | `"FORCE_COEF"` | object | - | Optional |
| a | Use User-defined Force Coefficient | `"OPT_USE"` | boolean | false | Optional |
| a | Force Coefficient Value (OPT_USE=true) | `"FORCE_COEF"` | number | - | Conditional |
| | Building Type (0=Middle Low Rise / 1=High Rise) | `"BUILDING_TYPE"` | integer (enum) | - | Optional |
| | Vibration Parameters | `"VIBRATION_PARAMS"` | object | - | Optional |
| a | Across-wind Vibration | `"ACROSS_WIND"` | boolean | false | Optional |
| b | Torsional-wind Vibration | `"TORSIONAL_WIND"` | boolean | false | Optional |
| c | Wind Response | `"WIND_RESPONSE"` | boolean | false | Optional |
| d | Building Length X | `"BL_X"` | number | - | Required |
| e | Building Length Y | `"BL_Y"` | number | - | Required |
| f | Natural Frequency X | `"NO_X"` | number | - | Required |
| g | Natural Frequency Y | `"NO_Y"` | number | - | Required |
| h | Torsional Natural Frequency | `"NO_T"` | number | - | Required |
| i | Mass | `"M"` | number | system | Optional |
| j | Mass in X direction | `"MX"` | number | system | Optional |
| k | Mass in Y direction | `"MY"` | number | system | Optional |
| l | Mass Moment of Inertia | `"MI"` | number | system | Optional |
| m | Damping Ratio | `"ZF"` | number | - | Required |
| n | Vibration Mode Coefficient | `"VIBRATION_MODE"` | number | - | Required |
| **INPUT_METHOD = 2 (General + Vortex Shedding)** | | | | | |
| | Roof Height | `"ROOF_HEIGHT"` | number | system | Optional |
| | Vortex Shedding DM | `"DM"` | number | - | Required |
| | Vortex Shedding DB | `"DB"` | number | - | Required |
| | Natural Frequency for Vortex | `"N"` | number | - | Required |
| | Mass for Vortex Check | `"M"` | number | system | Optional |
| | Damping Ratio for Vortex | `"ZF"` | number | - | Required |
| 6 | Additional Story-level Wind Load | `"ADDITIONAL_LOAD"` | array \[object\] | - | Optional |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Along-wind Load X | `"ALONG_X"` | number | - | Optional |
| (3) | Along-wind Load Y | `"ALONG_Y"` | number | - | Optional |
| (4) | Across-wind Load X | `"ACROSS_X"` | number | - | Optional |
| (5) | Across-wind Load Y | `"ACROSS_Y"` | number | - | Optional |
| (6) | Torsional Wind Load RZ | `"TORSIONAL_RZ"` | number | - | Optional |
| (7) | Torsional Wind Load RZ X | `"TORSIONAL_RZ_X"` | number | - | Optional |
| (8) | Torsional Wind Load RZ Y | `"TORSIONAL_RZ_Y"` | number | - | Optional |

### Python 示例

```python
# 定义静力风荷载（POST）— INPUT_METHOD=0: Simplified
swind_simplified = {
    "Assign": {
        "1": {
            "WIND_CODE": "KDS(41-12: 2022)",
            "DESC": "Simplified Method",
            "SCALE_FACTOR_X": 1.0,
            "SCALE_FACTOR_Y": 1.0,
            "PARAMETERS": {
                "INPUT_METHOD": 0,          # Simplified Method
                "WIND_SPEED": 30.0,         # 基本风速 30 m/s
                "ROOF_HEIGHT": 45.0,        # 建筑高度 45m
                "CE": 1.0                   # 暴露系数
            }
        }
    }
}
result = midas_api("POST", "/db/SWIND", swind_simplified)

# General Method (INPUT_METHOD=1)
swind_general = {
    "Assign": {
        "2": {
            "WIND_CODE": "KDS(41-12: 2022)",
            "DESC": "General Method",
            "SCALE_FACTOR_X": 1.0,
            "SCALE_FACTOR_Y": 1.0,
            "PARAMETERS": {
                "INPUT_METHOD": 1,
                "EXP_CATEGORY": 1,          # 暴露类别 B
                "WIND_SPEED": 30.0,
                "IMPORTANCE_FACTOR": 1.1,
                "ROOF_HEIGHT": 45.0,
                "TOPOGRAPHIC_EFFECT": {"OPT_USE": False},
                "DIRECTION_FACTOR_X": 1.0,
                "DIRECTION_FACTOR_Y": 1.0,
                "RIGIDITY": 1,              # 刚度分类
                "GUST_FACTOR_X": 1.8,
                "GUST_FACTOR_Y": 1.8,
                "BUILDING_TYPE": 1          # 高层建筑
            }
        }
    }
}
midas_api("POST", "/db/SWIND", swind_general)

# 查询
all_swind = midas_api("GET", "/db/SWIND")

# 删除
midas_api("DELETE", "/db/SWIND", {"Assign": {"1": {}}})
```

### ADDITIONAL — `WIND_CODE = "USER TYPE"` 变体（2026-08-07 官方已反映）

> 本方式不使用 KDS(41-12:2022) 的计算式，而是直接输入逐层风压。将 `WIND_CODE` 指定为
> `"USER TYPE"` 时，使用 `STORY_WIND_PRESSURE` 数组代替上述 `PARAMETERS` 对象。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Wind Load Code (`"USER TYPE"`) | `"WIND_CODE"` | string (enum) | - | Required |
| 2 | Description | `"DESC"` | string | `""` | Optional |
| 3 | Wind Eccentricity Option X (0=Positive / 1=Negative / 2=None) | `"WIND_ECCEN_X"` | integer (enum) | `2` | Optional |
| 4 | Wind Eccentricity Option Y (0=Positive / 1=Negative / 2=None) | `"WIND_ECCEN_Y"` | integer (enum) | `2` | Optional |
| 5 | Scale Factor X | `"SCALE_FACTOR_X"` | number | - | Required |
| 6 | Scale Factor Y | `"SCALE_FACTOR_Y"` | number | - | Required |
| 7 | User-defined Story-level Wind Pressure | `"STORY_WIND_PRESSURE"` | array [object] | - | Required |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Wind Pressure X | `"PRESS_X"` | number | - | Required |
| (3) | Wind Pressure Y | `"PRESS_Y"` | number | - | Required |
| 8 | Additional Story-level Wind Load | `"ADDITIONAL_LOAD"` | array [object] | - | Optional |
| (1) | Story Name | `"STORY_NAME"` | string | - | Optional |
| (2) | Along-wind Load X | `"ALONG_X"` | number | - | Optional |
| (3) | Along-wind Load Y | `"ALONG_Y"` | number | - | Optional |
| (4) | Torsional Wind Load RZ | `"TORSIONAL_RZ"` | number | - | Optional |

> ⚠️ `ELEV`、`LOAD_H`、`LOAD_BX`、`LOAD_BY` 等仅出现在 GET 响应中的楼层几何字段，按原文
> JSON Schema 的规定属于不得在请求负载中发送的项，故未列入上表。

```json
{
  "Assign": {
    "1": {
      "LC_NAME": "WX",
      "WIND_CODE": "USER TYPE",
      "DESC": "",
      "WIND_ECCEN_X": 2,
      "WIND_ECCEN_Y": 2,
      "SCALE_FACTOR_X": 1,
      "SCALE_FACTOR_Y": 1,
      "STORY_WIND_PRESSURE": [
        {"STORY_NAME": "RF", "PRESS_X": 1.2, "PRESS_Y": 1},
        {"STORY_NAME": "3F", "PRESS_X": 1, "PRESS_Y": 0.8},
        {"STORY_NAME": "2F", "PRESS_X": 0.8, "PRESS_Y": 0.6},
        {"STORY_NAME": "1F", "PRESS_X": 0.6, "PRESS_Y": 0.4}
      ],
      "ADDITIONAL_LOAD": [
        {"STORY_NAME": "RF", "ALONG_X": 10, "ALONG_Y": 8, "TORSIONAL_RZ": 2.5},
        {"STORY_NAME": "3F", "ALONG_X": 7, "ALONG_Y": 5, "TORSIONAL_RZ": 1.5}
      ]
    }
  }
}
```

---

## 21. /db/SSEIS — Static Seismic Load

> 定义基于 KDS 41-17-00:2019 的等效静力地震作用。将 `SEIS_CODE` 指定为 `"USER TYPE"` 时，也可使用直接输入逐层地震力的方式（见下方 ADDITIONAL 参考）。

**Input URI:** `{base url}/db/SSEIS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Seismic Load Code (`"KDS(41-17-00:2019)"`) | `"SEIS_CODE"` | string (enum) | - | Required |
| 2 | Description | `"DESC"` | string | `""` | Optional |
| 3 | Scale Factor X | `"SCALE_FACTOR_X"` | number | - | Required |
| 4 | Scale Factor Y | `"SCALE_FACTOR_Y"` | number | - | Required |
| 5 | Accidental Eccentricity X (0=Positive / 1=Negative / 2=None) | `"ACCIDENT_ECCEN_X"` | integer (enum) | 0 | Optional |
| 6 | Accidental Eccentricity Y (0=Positive / 1=Negative / 2=None) | `"ACCIDENT_ECCEN_Y"` | integer (enum) | 0 | Optional |
| 7 | Consider Accidental Torsion | `"ACCIDENT_TORSION"` | boolean | false | Optional |
| 8 | KDS(41-17-00:2019) Parameters | `"PARAMETERS"` | object | - | Required |
| (1) | Seismic Zone (0=Zone1 / 1=Zone2) | `"SEIS_ZONE"` | integer (enum) | - | Required |
| (2) | Effective Peak Acceleration | `"EPA"` | number | - | Required |
| (3) | Site Class (0=S1 / 1=S2 / 2=S3 / 3=S4 / 4=S5 / 5=S6) | `"SITE_CLASS"` | integer (enum) | - | Required |
| (4) | Short-period Site Coefficient FA | `"FA"` | number | system | Optional |
| (5) | Long-period Site Coefficient FV | `"FV"` | number | system | Optional |
| (6) | Design Spectral Acceleration at Short Period SDS | `"SDS"` | number | system | Optional |
| (7) | Design Spectral Acceleration at 1-sec SD1 | `"SD1"` | number | system | Optional |
| (8) | Seismic Use Group (0=Special / 1=I / 2=II) | `"SEIS_USE_GROUP"` | integer (enum) | - | Required |
| (9) | Importance Factor | `"IMPORTANCE_FACTOR"` | number | - | Required |
| (10) | Period Method (0=Analytical / 1=Approximate) | `"PERIOD_METHOD"` | integer (enum) | - | Required |
| **PERIOD_METHOD = 0** | | | | | |
| | Analytical Period X | `"PERIOD_ANALYSIS_X"` | number | - | Required |
| | Analytical Period Y | `"PERIOD_ANALYSIS_Y"` | number | - | Required |
| | Approximate Period X | `"PERIOD_APPR_X"` | number | - | Required |
| | Approximate Period Y | `"PERIOD_APPR_Y"` | number | - | Required |
| **PERIOD_METHOD = 1** | | | | | |
| | Approximate Period X | `"PERIOD_APPR_X"` | number | - | Required |
| | Approximate Period Y | `"PERIOD_APPR_Y"` | number | - | Required |
| | Response Modification Factor X | `"RESPONSE_MOD_FACTOR_X"` | number | - | Required |
| | Response Modification Factor Y | `"RESPONSE_MOD_FACTOR_Y"` | number | - | Required |
| 9 | Additional Story-level Seismic Load | `"ADDITIONAL_LOAD"` | object | - | Optional |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Additional Seismic Load X | `"ALONG_X"` | number | - | Required |
| (3) | Additional Seismic Load Y | `"ALONG_Y"` | number | - | Required |
| (4) | Additional Torsional Seismic Load RZ | `"TORSIONAL_RZ"` | number | - | Required |

### Python 示例

```python
# 定义等效静力地震作用（POST）— KDS 41-17-00:2019
sseis_data = {
    "Assign": {
        "1": {
            "SEIS_CODE": "KDS(41-17-00:2019)",
            "DESC": "X方向地震作用",
            "SCALE_FACTOR_X": 1.0,
            "SCALE_FACTOR_Y": 0.0,         # 仅施加X方向
            "ACCIDENT_ECCEN_X": 0,          # X方向偶然偏心（+）
            "ACCIDENT_ECCEN_Y": 2,          # Y方向无偶然偏心
            "ACCIDENT_TORSION": True,
            "PARAMETERS": {
                "SEIS_ZONE": 0,             # 地震分区 I
                "EPA": 0.22,
                "SITE_CLASS": 1,            # S2 场地
                "FA": 1.0,
                "FV": 1.4,
                "SDS": 0.2933,
                "SD1": 0.1467,
                "SEIS_USE_GROUP": 1,        # 抗震等级 I
                "IMPORTANCE_FACTOR": 1.5,
                "PERIOD_METHOD": 1,         # 近似周期法
                "PERIOD_APPR_X": 1.2,       # X方向近似周期（秒）
                "PERIOD_APPR_Y": 1.0,       # Y方向近似周期（秒）
                "RESPONSE_MOD_FACTOR_X": 5.0,  # X方向反应修正系数
                "RESPONSE_MOD_FACTOR_Y": 5.0   # Y方向反应修正系数
            }
        },
        "2": {
            "SEIS_CODE": "KDS(41-17-00:2019)",
            "DESC": "Y方向地震作用",
            "SCALE_FACTOR_X": 0.0,
            "SCALE_FACTOR_Y": 1.0,
            "ACCIDENT_ECCEN_X": 2,
            "ACCIDENT_ECCEN_Y": 0,
            "ACCIDENT_TORSION": True,
            "PARAMETERS": {
                "SEIS_ZONE": 0,
                "EPA": 0.22,
                "SITE_CLASS": 1,
                "FA": 1.0,
                "FV": 1.4,
                "SEIS_USE_GROUP": 1,
                "IMPORTANCE_FACTOR": 1.5,
                "PERIOD_METHOD": 1,
                "PERIOD_APPR_X": 1.2,
                "PERIOD_APPR_Y": 1.0,
                "RESPONSE_MOD_FACTOR_X": 5.0,
                "RESPONSE_MOD_FACTOR_Y": 5.0
            }
        }
    }
}
result = midas_api("POST", "/db/SSEIS", sseis_data)

# 查询
all_sseis = midas_api("GET", "/db/SSEIS")

# 删除
midas_api("DELETE", "/db/SSEIS", {"Assign": {"2": {}}})
```

### ADDITIONAL — `SEIS_CODE = "USER TYPE"` 变体（2026-08-07 官方已反映）

> 本方式不使用 KDS(41-17-00:2019) 的计算式，而是直接输入逐层地震力。将 `SEIS_CODE`
> 指定为 `"USER TYPE"` 时，使用 `SEISMIC_FORCE` 数组代替上述 `PARAMETERS` 对象。

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 1 | Seismic Load Code (`"USER TYPE"`) | `"SEIS_CODE"` | string (enum) | - | Required |
| 2 | Description | `"DESC"` | string | `""` | Optional |
| 3 | Scale Factor X | `"SCALE_FACTOR_X"` | number | - | Required |
| 4 | Scale Factor Y | `"SCALE_FACTOR_Y"` | number | - | Required |
| 5 | Accidental Eccentricity X (0=Positive / 1=Negative / 2=None) | `"ACCIDENT_ECCEN_X"` | integer (enum) | `0` | Optional |
| 6 | Accidental Eccentricity Y (0=Positive / 1=Negative / 2=None) | `"ACCIDENT_ECCEN_Y"` | integer (enum) | `0` | Optional |
| 7 | Consider Accidental Torsion | `"ACCIDENT_TORSION"` | boolean | `false` | Optional |
| 8 | Consider Inherent Torsion | `"INHERENT_TORSION"` | boolean | `false` | Optional |
| 9 | User-defined Story-level Seismic Force | `"SEISMIC_FORCE"` | array [object] | - | Required |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Seismic Force X | `"FORCE_X"` | number | - | Required |
| (3) | Seismic Force Y | `"FORCE_Y"` | number | - | Required |
| 10 | Additional Story-level Seismic Load | `"ADDITIONAL_LOAD"` | object | - | Optional |
| (1) | Story Name | `"STORY_NAME"` | string | - | Required |
| (2) | Additional Seismic Load X | `"ALONG_X"` | number | - | Required |
| (3) | Additional Seismic Load Y | `"ALONG_Y"` | number | - | Required |
| (4) | Additional Torsional Seismic Load RZ | `"TORSIONAL_RZ"` | number | - | Required |

> ⚠️ **原文 ko locale 污染（2026-09-06 确认）。** 此前（2026-08-25 确认）原文 Request Example 将
> `"INHERENT_TORSION"` 误写为 `"NHERENT_TORSION"`（漏掉首字母 I），故已在下方示例中更正，
> 但 2026-09-01 更新后该示例本身已从原文中消失。
>
> 这项更正有效 — 2026-09-18 在线验证中，误写键 `IINHERENT_TORSION`·`NHERENT_TORSION`
> **虽返回 HTTP 201 但被静默忽略**，响应中该键消失，GET 中仅保留正常字段
> `INHERENT_TORSION` 且为默认值 `false`。原样复制误写键发送的用户会误以为该选项已开启。用正常键发送时，`true` 会被如实保存。
>
> 当前状态（注意各 locale 正文不同）：
>
> | 文章 | locale | 最后编辑 | Schema `SEIS_CODE` |
> | --- | --- | --- | --- |
> | KDS (`58908676674585`) | **en-us** | 2026-06-18 | `const: "KDS(41-17-00:2019)"`（正常） |
> | KDS (`58908676674585`) | **ko** | 2026-09-01 | `const: "USER TYPE"`（污染） |
> | User Type (`58908928576153`) | ko / en-us | 2026-09-01 | `const: "USER TYPE"` |
>
> 此外 **ko 正文的复制用示例中 `"SEIS_CODE": "KDS(41-17-00: 2019)"` 在冒号后多了一个空格**
> （en-us 无空格）。同一 ko 页面的 Specifications 表是无空格写法，因此页面内部就不一致。不过 **实际使用不受影响** — 2026-09-18 在线验证（Gen NX 2026
> v2.1, Build 09/15/2026）确认带空格的取值也被接受，POST 响应与 GET 存储值均**规范化**为无空格的
> `"KDS(41-17-00:2019)"`。因此这只是统一写法层面的问题。本仓库以 en-us 为准，故上述示例采用无空格的写法。
>
> ⚠️ 2026-09-18 此处曾写「因为是 `const`，原样复制 ko 示例发送就会 Schema 校验失败」，
> **这是错的。** 那只是仅凭 Schema 中的 `const` 就断定服务器同样会拒绝的推断，已被在线验证推翻。**文档上的 `const`/`enum` 标注并不等于服务器的拒绝行为** — 要以实际行为为依据时，
> 必须取得在线验证结果。
>
> ⚠️ 若认为在 en-us Schema 中也见到过这个空格，那是**语法高亮的假象。** 高亮器把字符串内的数字错误地
> 切分为 `"KDS(41-17-00: <span class="manual-json-n">2019</span>)"`，去掉标签后便出现空格。判定必须以复制用的 `<textarea id="copyRawJson_…">` 原文为准
> （2026-09-18 就据此误判过一次）。
>
> 即 **ko locale 下两篇文章的正文已完全相同（56,247 字符）**，该正文处于 USER TYPE Schema 与
> KDS 示例·Specifications 表混杂的状态（表要求 `PARAMETERS` 为 Required，Schema 中却没有该属性；
> 反之 Schema 以 required 指定的 `SEISMIC_FORCE`·`INHERENT_TORSION` 在表中没有对应行）。
> 同一篇文章未经改动的 en-us 译本仍完整保留正确的 KDS Schema，因此判断这是编辑事故而非有意合并
> （Schema 中没有 `oneOf`/`if` 分支，目录中两项也仍各自独立存在）。
>
> 下表与示例仍由 **USER TYPE JSON Schema**（`SEISMIC_FORCE` 数组，`INHERENT_TORSION` boolean
> 默认值 `false`）支撑，故保持原样。此项属错误提报对象，原文恢复后需重新对账。
> `scripts/manual_sync` 只抓取 `SYNC_LOCALE`(= **en-us**) 正文，因此该污染不会出现在抓取到的正文中 — 文章级 `updated_at` 取各 locale 时间戳的最大值，
> 仅 ko 编辑也会置起 changed 标记，由此才被发现。`check_diff.py` 的 `locale_note`
> 会给出 `en-us did NOT` 判定，此类情况必须直接打开 ko 页面对照。

```json
{
  "Assign": {
    "1": {
      "SEIS_CODE": "USER TYPE",
      "DESC": "",
      "SCALE_FACTOR_X": 1,
      "SCALE_FACTOR_Y": 1,
      "ACCIDENT_ECCEN_X": 0,
      "ACCIDENT_ECCEN_Y": 0,
      "ACCIDENT_TORSION": false,
      "INHERENT_TORSION": false,
      "SEISMIC_FORCE": [
        {"STORY_NAME": "Roof", "FORCE_X": 1250.5, "FORCE_Y": 1180.75},
        {"STORY_NAME": "Story3", "FORCE_X": 980.25, "FORCE_Y": 925.5},
        {"STORY_NAME": "Story2", "FORCE_X": 710, "FORCE_Y": 665.25},
        {"STORY_NAME": "Story1", "FORCE_X": 420.75, "FORCE_Y": 390.5}
      ],
      "ADDITIONAL_LOAD": {
        "STORY_NAME": "Roof",
        "ALONG_X": 35.5,
        "ALONG_Y": 28.25,
        "TORSIONAL_RZ": 12.75
      }
    }
  }
}
```

---

## 完整工作流示例

以下是向典型建筑结构批量输入静力荷载数据的完整示例。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}

# ─── Step 1: 定义静力荷载工况 ───────────────────────────────
stld_data = {
    "Assign": {
        "1": {"NAME": "DL",  "TYPE": "D",  "DESC": "恒荷载"},
        "2": {"NAME": "LL",  "TYPE": "L",  "DESC": "活荷载"},
        "3": {"NAME": "WX",  "TYPE": "W",  "DESC": "风荷载 +X"},
        "4": {"NAME": "WY",  "TYPE": "W",  "DESC": "风荷载 +Y"},
        "5": {"NAME": "EX",  "TYPE": "E",  "DESC": "地震作用 X"},
        "6": {"NAME": "EY",  "TYPE": "E",  "DESC": "地震作用 Y"},
        "7": {"NAME": "EP",  "TYPE": "EP", "DESC": "土压力"},
        "8": {"NAME": "STL", "TYPE": "STL","DESC": "支座沉降"},
    }
}
midas_api("POST", "/db/STLD", stld_data)

# ─── Step 2: 自重 (Self-Weight) ──────────────────────────────────
midas_api("POST", "/db/BODF", {
    "Assign": {
        "1": {"LCNAME": "DL", "GROUP_NAME": "", "FV": [0, 0, -1]}
    }
})

# ─── Step 3: 荷载→质量转换 ──────────────────────────────────────
midas_api("POST", "/db/LTOM", {
    "Assign": {
        "1": {
            "DIR": "XYZ",
            "bNODAL": True, "bBEAM": True, "bFLOOR": True, "bPRES": False,
            "GRAV": 9.806,
            "vLC": [
                {"LCNAME": "DL", "FACTOR": 1.0},
                {"LCNAME": "LL", "FACTOR": 0.25},
            ]
        }
    }
})

# ─── Step 4: 节点集中荷载 ────────────────────────────────────────
midas_api("POST", "/db/CNLD", {
    "Assign": {
        "50": {   # 节点50号
            "ITEMS": [{"ID": 1, "LCNAME": "LL", "GROUP_NAME": "",
                       "FX": 0, "FY": 0, "FZ": -200.0, "MX": 0, "MY": 0, "MZ": 0}]
        }
    }
})

# ─── Step 5: 梁均布荷载 ──────────────────────────────────────────
midas_api("POST", "/db/BMLD", {
    "Assign": {
        "100": {   # 单元100号
            "ITEMS": [{"ID": 1, "LCNAME": "LL", "GROUP_NAME": "",
                       "CMD": "BEAM", "TYPE": "UNILOAD", "DIRECTION": "GZ",
                       "USE_PROJECTION": False, "USE_ECCEN": False,
                       "D": [0, 1, 0, 0], "P": [-25.0, -25.0, 0, 0]}]
        }
    }
})

# ─── Step 6: 定义楼面荷载类型后分配 ────────────────────────
midas_api("POST", "/db/FBLD", {
    "Assign": {
        "1": {
            "NAME": "TypFloor",
            "DESC": "",
            "ITEM": [
                {"LCNAME": "DL", "FLOOR_LOAD": 3.5, "OPT_SUB_BEAM_WEIGHT": True},
                {"LCNAME": "LL", "FLOOR_LOAD": 2.5, "OPT_SUB_BEAM_WEIGHT": False},
            ]
        }
    }
})
midas_api("POST", "/db/FBLA", {
    "Assign": {
        "1": {
            "FLOOR_LOAD_TYPE_NAME": "TypFloor",
            "FLOOR_DIST_TYPE": 2,           # Two Way
            "DIR": "GZ",
            "OPT_PROJECTION": False,
            "GROUP_NAME": "FloorGroup",
            "NODES": [11, 12, 13, 14],      # 楼面区域节点
        }
    }
})

# ─── Step 7: 地基参数 + 静力土压力 ──────────────────────────
midas_api("POST", "/db/POSP", {
    "Assign": {
        "1": {
            "NAME": "SiteA",
            "OPT_USE_N": False,
            "GROUND_LEVEL": 0.0,
            "BEDROCK_LEVEL": -20.0,
            "FOOTING_LEVEL": -8.0,
            "ITEMS": [
                {"HEIGHT": 8.0, "ANGLE_OR_N": 30, "DENSITY": 18.0,
                 "VS": 200, "KH": 20000, "DISP": 0.001},
                {"HEIGHT": 12.0,"ANGLE_OR_N": 35, "DENSITY": 19.0,
                 "VS": 350, "KH": 60000, "DISP": 0.001},
            ]
        }
    }
})
midas_api("POST", "/db/EPST", {
    "Assign": {
        "1": {
            "LOADCASE": "EP",
            "DIR": "XY", "ANGLE": 0, "IN_PT": [0, 0, 0], "SF": 1.0,
            "EP_TYPE": "AT_REST",
            "SURCHARGE_LOAD": 10.0, "WATER_LEVEL": -3.0,
            "SOIL_PROP": "SiteA",
            "SEL_TYPE": "ELEMENT", "ELEM_TYPE": "FRAME",
            "ELEM_LIST": [201, 202, 203],
            "PRES_PROFILE_ITEMS": [
                {"LEVEL": 0.0,  "SOIL_PRES": 0.0,  "ADD_PRES": 5.0},
                {"LEVEL": -8.0, "SOIL_PRES": 72.0, "ADD_PRES": 5.0},
            ]
        }
    }
})

# ─── Step 8: 地震作用参数 + 静力地震作用 ──────────────────
midas_api("POST", "/db/POSL", {
    "Assign": {
        "1": {
            "NAME": "KDS2019",
            "CODE": "KDS(41-17-00:2019)",
            "METHOD": "EQV_STATIC",
            "SZ": "1", "EPA": 0.22, "SC": "S2",
            "FA": 1.0, "FV": 1.4,
            "SDS": 0.2933, "SD1": 0.1467,
            "USER_GROUP": "1", "IF": 1.5, "RMF": 5.0
        }
    }
})
midas_api("POST", "/db/SSEIS", {
    "Assign": {
        "1": {
            "SEIS_CODE": "KDS(41-17-00:2019)",
            "DESC": "EX", "SCALE_FACTOR_X": 1.0, "SCALE_FACTOR_Y": 0.0,
            "ACCIDENT_ECCEN_X": 0, "ACCIDENT_ECCEN_Y": 2, "ACCIDENT_TORSION": True,
            "PARAMETERS": {
                "SEIS_ZONE": 0, "EPA": 0.22, "SITE_CLASS": 1,
                "SEIS_USE_GROUP": 1, "IMPORTANCE_FACTOR": 1.5,
                "PERIOD_METHOD": 1,
                "PERIOD_APPR_X": 1.2, "PERIOD_APPR_Y": 1.0,
                "RESPONSE_MOD_FACTOR_X": 5.0, "RESPONSE_MOD_FACTOR_Y": 5.0
            }
        }
    }
})

# ─── Step 9: 静力风荷载 (KDS 41-12:2022) ───────────────────────
midas_api("POST", "/db/SWIND", {
    "Assign": {
        "1": {
            "WIND_CODE": "KDS(41-12: 2022)",
            "DESC": "Wind X+Y", "SCALE_FACTOR_X": 1.0, "SCALE_FACTOR_Y": 1.0,
            "PARAMETERS": {
                "INPUT_METHOD": 0,       # Simplified
                "WIND_SPEED": 30.0,
                "ROOF_HEIGHT": 45.0,
                "CE": 1.0
            }
        }
    }
})

print("静力荷载数据输入完成")
```

---

*[06_DB_Static_Loads.md] 撰写完成 — 下一个文件 [07_DB_Temperature_Prestress.md] 已可开始推进。*
