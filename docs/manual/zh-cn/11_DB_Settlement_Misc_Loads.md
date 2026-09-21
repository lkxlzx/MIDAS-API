# 11. DB – Settlement / Miscellaneous Loads

沉降荷载（Settlement Loads）及其他荷载（Miscellaneous Loads）相关的数据库 API。

> **Base URL**
> - Civil NX : `https://moa-engineers.midasit.com:443/civil`
> - Gen NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **认证头部** ：所有请求必须包含 `MAPI-Key: <your_api_key>` 头部

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../11_DB_Settlement_Misc_Loads.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

### Settlement Loads（2 个）

| No. | Endpoint | 说明 |
|-----|----------|------|
| 1 | [/db/SMPT](#1-dbsmpt--settlement-group) | Settlement Group |
| 2 | [/db/SMLC](#2-dbsmlc--settlement-load-cases) | Settlement Load Cases |

### Miscellaneous Loads（7 个）

| No. | Endpoint | 说明 |
|-----|----------|------|
| 3 | [/db/PLCB](#3-dbplcb--pre-composite-section) | Pre-composite Section |
| 4 | [/db/LDSQ](#4-dbldsq--load-sequence-for-nonlinear) | Load Sequence for Nonlinear |
| 5 | [/db/WVLD](#5-dbwvld--wave-loads) | Wave Loads |
| 6 | [/db/IELC](#6-dbielc--ignore-elements-for-load-cases) | Ignore Elements for Load Cases |
| 7 | [/db/IFGS](#7-dbifgs--large-displacement--initial-forces-for-geometric-stiffness) | Large Displacement – Initial Forces for Geometric Stiffness |
| 8 | [/db/EFCT](#8-dbefct--small-displacement--initial-force-control-data) | Small Displacement – Initial Force Control Data |
| 9 | [/db/INMF](#9-dbinmf--small-displacement--initial-element-force) | Small Displacement – Initial Element Force |

---

## 1. /db/SMPT — Settlement Group

定义支点沉降群组。存储施加沉降位移的节点列表与沉降量。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/SMPT` | 创建沉降群组 |
| GET | `{base_url}/db/SMPT` | 查询全部沉降群组 |
| GET | `{base_url}/db/SMPT/{id}` | 查询特定沉降群组 |
| PUT | `{base_url}/db/SMPT/{id}` | 修改沉降群组 |
| DELETE | `{base_url}/db/SMPT/{id}` | 删除沉降群组 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Settlement Group Name | `"NAME"` | String | - | Required |
| 2 | Settlement Displacement | `"SETTLE"` | Number | - | Required |
| 3 | Node List | `"ITEMS"` | Array [Integer] | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "NAME": "SG1",
      "SETTLE": 25,
      "ITEMS": [100, 101]
    },
    "2": {
      "NAME": "SG2",
      "SETTLE": 15,
      "ITEMS": [102, 103]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# 创建沉降群组
def create_settlement_groups():
    payload = {
        "Assign": {
            "1": {
                "NAME": "SG1",   # 沉降群组名称
                "SETTLE": 25,    # 沉降量 (mm)
                "ITEMS": [100, 101]  # 施加的节点列表
            },
            "2": {
                "NAME": "SG2",
                "SETTLE": 15,
                "ITEMS": [102, 103]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/SMPT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Settlement Groups created:", resp.json())

# 查询全部沉降群组
def get_all_settlement_groups():
    resp = requests.get(f"{BASE_URL}/db/SMPT", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

create_settlement_groups()
```

---

## 2. /db/SMLC — Settlement Load Cases

定义沉降荷载工况（Settlement Load Cases）。引用沉降群组，设定最少/最多群组数量与缩放系数。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/SMLC` | 创建沉降荷载工况 |
| GET | `{base_url}/db/SMLC` | 查询全部 |
| GET | `{base_url}/db/SMLC/{id}` | 查询特定工况 |
| PUT | `{base_url}/db/SMLC/{id}` | 修改 |
| DELETE | `{base_url}/db/SMLC/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Settlement Load Case No. (Assign Key) | `"KEY"` | Integer | - | Required |
| 2 | Settlement Load Case Name | `"NAME"` | String | - | Required |
| 3 | Description | `"DESC"` | String | - | Required |
| 4 | Settlement Scale Factor | `"FACTOR"` | Number | - | Required |
| 5 | Settlement – Min. Group Nos. | `"MIN"` | Integer | - | Required |
| 6 | Settlement – Max. Group Nos. | `"MAX"` | Integer | - | Required |
| 7 | Selected Settlement Group Names | `"ST_GROUPS"` | Array [String] | - | Required |

> **参考**：`MIN` / `MAX` 表示该荷载工况所包含沉降群组的最少/最多数量。

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "NAME": "SMLC1",
      "DESC": "",
      "FACTOR": 1.2,
      "MIN": 1,
      "MAX": 1,
      "ST_GROUPS": ["SG1", "SG2"]
    },
    "2": {
      "NAME": "SMLC2",
      "DESC": "",
      "FACTOR": 1.0,
      "MIN": 1,
      "MAX": 1,
      "ST_GROUPS": ["SG1", "SG2"]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# 创建沉降荷载工况
def create_settlement_load_cases():
    payload = {
        "Assign": {
            "1": {
                "NAME": "SMLC1",
                "DESC": "Settlement Load Case 1",
                "FACTOR": 1.2,      # 缩放系数
                "MIN": 1,           # 最少群组数
                "MAX": 1,           # 最多群组数
                "ST_GROUPS": ["SG1", "SG2"]  # 引用的沉降群组列表
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/SMLC", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Settlement Load Cases created:", resp.json())

create_settlement_load_cases()
```

---

## 3. /db/PLCB — Pre-composite Section

指定组合前（Pre-composite）阶段施加的静力荷载工况列表。在组合结构分析中，设定由浇筑楼板前的主梁单独承受的荷载工况。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/PLCB` | 设置 Pre-composite 荷载工况 |
| GET | `{base_url}/db/PLCB` | 查询全部 |
| GET | `{base_url}/db/PLCB/{id}` | 查询特定条目 |
| PUT | `{base_url}/db/PLCB/{id}` | 修改 |
| DELETE | `{base_url}/db/PLCB/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Static Load Case Names | `"LCNAME_ITEM"` | Array [String] | - | Required |

> **参考**：Assign Key `"1"` 是唯一记录，整个系统只持有一份 Pre-composite 列表。

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": ["DL(BC)1", "DL(BC)3"]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# 设置 Pre-composite 荷载工况
def set_precomposite_load_cases():
    payload = {
        "Assign": {
            "1": {
                # 组合前阶段的静力荷载工况列表
                "LCNAME_ITEM": ["DL(BC)1", "DL(BC)3"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/PLCB", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Pre-composite Load Cases set:", resp.json())

# 修改 (PUT)
def update_precomposite_load_cases():
    payload = {
        "LCNAME_ITEM": ["DL(BC)1", "DL(BC)2", "DL(BC)3"]
    }
    resp = requests.put(f"{BASE_URL}/db/PLCB/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Updated:", resp.json())

set_precomposite_load_cases()
```

---

## 4. /db/LDSQ — Load Sequence for Nonlinear

定义非线性分析所采用的荷载顺序（Load Sequence）。控制非线性分析中荷载的施加次序。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/LDSQ` | 创建非线性荷载顺序 |
| GET | `{base_url}/db/LDSQ` | 查询全部 |
| GET | `{base_url}/db/LDSQ/{id}` | 查询特定条目 |
| PUT | `{base_url}/db/LDSQ/{id}` | 修改 |
| DELETE | `{base_url}/db/LDSQ/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Case Names（顺序数组） | `"LCNAME_ITEM"` | Array [String] | - | Required |

> **参考**：Assign Key 为荷载顺序集编号。`LCNAME_ITEM` 数组的次序即为非线性分析中的荷载施加次序。

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": ["DL(BC)4", "DL(AC)"]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# 创建非线性荷载顺序
def create_load_sequence():
    payload = {
        "Assign": {
            "1": {
                # 非线性分析的荷载施加次序（按数组次序施加）
                "LCNAME_ITEM": ["DL(BC)4", "DL(AC)"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/LDSQ", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Load Sequence created:", resp.json())

create_load_sequence()
```

---

## 5. /db/WVLD — Wave Loads

定义海洋结构物所承受的波浪荷载（Wave Loads）。基于 Morison 方程，包含拖曳力·惯性力系数、波浪特性、海流剖面、海生物附着等。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/WVLD` | 创建波浪荷载 |
| GET | `{base_url}/db/WVLD` | 查询全部 |
| GET | `{base_url}/db/WVLD/{id}` | 查询特定波浪荷载 |
| PUT | `{base_url}/db/WVLD/{id}` | 修改 |
| DELETE | `{base_url}/db/WVLD/{id}` | 删除 |

### Parameters — 基本设置

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Wave Load Name | `"NAME"` | String | - | Required |
| 2 | Description | `"DESC"` | String | Blank | Optional |
| 3 | Use Static Load Generation | `"bSTLD"` | Boolean | false | Optional |
| 4 | Use Time History Load Generation | `"bTHIS"` | Boolean | false | Optional |
| 5 | Time History Load Case Name | `"NAME_THIS"` | String | - | Optional |
| 6 | Vertical Coordinate (`"GLOBAL_X"`(⚠️ 未确认) / `"GLOBAL_Y"` / `"GLOBAL_Z"`) | `"VERT_COORD"` | String | `"GLOBAL_Z"` | Required |
| 7 | Water Weight Density | `"DENSITY"` | Number | - | Required |
| 8 | Water Depth | `"DEPTH"` | Number | - | Required |
| 9 | Use Self Weight | `"bSELFW"` | Boolean | false | Optional |
| 10 | Use Buoyancy Load | `"bBUOYANT"` | Boolean | false | Optional |

> ⚠️ **2026-08-25 确认：** 原文 Specifications 表对 `VERT_COORD` 的选项仅以项目符号列出 `"GLOBAL_Y"`/`"GLOBAL_Z"`
> 这 2 个（JSON Schema 与示例中也无 enum 列表），`"GLOBAL_X"` 在原文任何位置都无
> 依据。考虑到该值实际存在的可能性很高（按 X/Y/Z 三轴的构造惯例），故未删除而仅保留未确认
> 标注（文章 id `35988728179097`）。

### Parameters — COEF 对象（拖曳力·惯性力系数）

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Type (`"CONST"`(Constant) / ⚠️未确认（Linear Interpolation，原文未公开字面值）) | `"TYPE"` | String | Required |
| 2 | Coefficients – Slender Element Array | `"COEF_S"` | Array [Object] | Optional |
| 3 | Coefficients – Rigid Element Array | `"COEF_R"` | Array [Object] | Optional |
| 4 | Override Coefficients with Structure Group | `"bOVER"` | Boolean | Optional |
| 5 | Override Slender Element Array | `"OVER_S"` | Array [Object] | Optional |
| 6 | Override Rigid Element Array | `"OVER_R"` | Array [Object] | Optional |

> ⚠️ **2026-08-25 确认：** 原文 Specifications 表对 `TYPE` 的两个选项只给出 "Constant"/"Linear
> Interpolation" 的说明，字面字符串在表与 JSON Schema 中都不存在。可由示例确认的
> 取值仅 `"CONST"` 一个，故删除此前文档中的 `"GROUP"` 写法（推测系与按结构群组重新定义的 `bOVER` 功能混淆），
> 并更正为未确认（文章 id `35988728179097`）。

**COEF_S / COEF_R / OVER_S / OVER_R 条目结构：**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"GRUP"` | String | Structure Group Name |
| `"DIA"` | Number | Diameter |
| `"DRAG_COEF_X"` | Number | Drag Coefficient X |
| `"DRAG_COEF_Y"` | Number | Drag Coefficient Y |
| `"DRAG_COEF_Z"` | Number | Drag Coefficient Z |
| `"INER_COEF_X"` | Number | Inertia Coefficient X |
| `"INER_COEF_Y"` | Number | Inertia Coefficient Y |
| `"INER_COEF_Z"` | Number | Inertia Coefficient Z |

### Parameters — CHAR 对象（波浪特性）

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Theory Type (`"AIRY"` / `"STOKES"` / `"STREAM"`) | `"THEORY"` | String | Required |
| 2 | Function Order（在 Stokes/Stream 理论中使用） | `"FUNC"` | Integer | Optional |
| 3 | Wave Direction (degrees) | `"DIR"` | Number | Required |
| 4 | Wave Height | `"HEIGHT"` | Number | Required |
| 5 | Wave Length / Wave Period 选择（`"LENGTH"` / `"PERIOD"`） | `"CHAR_TYPE"` | String | Required |
| 6 | Wave Length | `"LENGTH"` | Number | Optional |
| 7 | Wave Period | `"PERIOD"` | Number | Optional |
| 8 | Kinematics Factor | `"K_FACTOR"` | Number | Optional |
| 9 | Current Surface Velocity | `"SURFACE_V"` | Number | Optional |
| 10 | Current Bottom Velocity | `"BOTTOM_Y"` | Number | Optional |

### Parameters — PROF 对象（海流剖面）

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Current Direction (degrees) | `"CUR_DIR"` | Number | Optional |
| 2 | Current Blockage Factor | `"CUR_FACTOR"` | Number | Optional |
| 3 | Grid Data (elevation × velocity points) | `"GRID_DATA"` | Array [Object] | Optional |

**GRID_DATA 条目结构：**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"D"` | Number | Elevation |
| `"V"` | Number | Velocity |

### Parameters — 其他设置

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|------------|----------|
| 1 | Flood Condition (Structure Group Names) | `"FLOOD_GRUP"` | Array [String] | Optional |
| 2 | Marine Growth Data | `"GROWTH"` | Array [Object] | Optional |
| 3 | Grid X Size | `"GRID_X"` | Integer | Optional |
| 4 | Grid Y Size | `"GRID_Z"` | Integer | Optional |
| 5 | User Defined Grid Data (2D Array) | `"USERGRID"` | Array [Array [Object]] | Optional |
| 6 | Trajectory Grid Data (2D Array) | `"TRAJ"` | Array [Array [Object]] | Optional |
| 7 | Crest Critical Position（原文未公开字面值，示例确认值 `"MXM"`） | `"CREST"` | String | Optional |
| 8 | Crest Position Unit（原文未公开字面值，示例确认值 `"PHASE"`） | `"UNIT"` | String | Optional |
| 9 | Initial Position | `"INITAL_POS"` | Number | Optional |
| 10 | Increase Step | `"STEP"` | Number | Optional |
| 11 | Number of Positions | `"POS"` | Integer | Optional |

> ⚠️ **2026-08-25 确认：** Key `"GRID_Z"` 的说明在原文 Specifications 表与 JSON Schema 中
> 都一致写作 "Grid Y Size"（并非笔误，原文本身即如此命名），据此更正。`"CREST"`/
> `"UNIT"` 在原文表中没有选项项目符号，故确认此前文档的 `"MAX"`/`"MANUAL"`/`"m"` 写法
> 系无依据的推测 — 已按官方 Request Example 中实际出现的值（`"MXM"`/`"PHASE"`）
> 一并更正下方示例与 Python 代码（文章 id `35988728179097`）。

**GROWTH 条目结构：**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"Z"` | Number | Elevation |
| `"T"` | Number | Thickness |

**USERGRID / TRAJ 条目结构（各网格点）：**

| Key | Value Type | Description |
|-----|------------|-------------|
| `"X"` | Number | X 坐标 |
| `"Z"` | Number | Z 坐标 |
| `"ELEV"` | Number | Elevation |
| `"VX"` | Number | Velocity X |
| `"VCX"` | Number | Current Velocity X |
| `"VT"` | Number | Total Velocity |
| `"VZ"` | Number | Velocity Z |
| `"AX"` | Number | Acceleration X |
| `"AZ"` | Number | Acceleration Z |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "NAME": "WV_100Y",
      "DESC": "100-year return period wave",
      "bSTLD": true,
      "bTHIS": false,
      "NAME_THIS": "",
      "VERT_COORD": "GLOBAL_Z",
      "DENSITY": 10.05,
      "DEPTH": 30.0,
      "COEF": {
        "TYPE": "CONST",
        "COEF_S": [
          {
            "GRUP": "",
            "DIA": 0.5,
            "DRAG_COEF_X": 0.0,
            "DRAG_COEF_Y": 0.65,
            "DRAG_COEF_Z": 0.65,
            "INER_COEF_X": 0.0,
            "INER_COEF_Y": 2.0,
            "INER_COEF_Z": 2.0
          }
        ],
        "COEF_R": [],
        "bOVER": false,
        "OVER_S": [],
        "OVER_R": []
      },
      "CHAR": {
        "THEORY": "STOKES",
        "FUNC": 5,
        "DIR": 0.0,
        "HEIGHT": 12.5,
        "CHAR_TYPE": "PERIOD",
        "LENGTH": 0.0,
        "PERIOD": 14.0,
        "K_FACTOR": 1.0,
        "SURFACE_V": 0.5,
        "BOTTOM_Y": 0.1
      },
      "PROF": {
        "CUR_DIR": 0.0,
        "CUR_FACTOR": 0.9,
        "GRID_DATA": [
          {"D": 0.0,   "V": 0.5},
          {"D": -15.0, "V": 0.3},
          {"D": -30.0, "V": 0.1}
        ]
      },
      "FLOOD_GRUP": [],
      "GROWTH": [
        {"Z": 0.0,   "T": 0.05},
        {"Z": -10.0, "T": 0.08}
      ],
      "GRID_X": 10,
      "GRID_Z": 10,
      "bSELFW": true,
      "bBUOYANT": true,
      "CREST": "MXM",
      "UNIT": "PHASE",
      "INITAL_POS": 0.0,
      "STEP": 1.0,
      "POS": 10
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def create_wave_load():
    payload = {
        "Assign": {
            "1": {
                "NAME": "WV_100Y",
                "DESC": "100-year return period wave load",
                "bSTLD": True,          # 使用静力荷载生成
                "bTHIS": False,         # 不使用时程荷载生成
                "NAME_THIS": "",
                "VERT_COORD": "GLOBAL_Z",  # 竖直坐标轴
                "DENSITY": 10.05,       # 水的单位重度 (kN/m³)
                "DEPTH": 30.0,          # 水深 (m)
                # 拖曳力·惯性力系数
                "COEF": {
                    "TYPE": "CONST",    # 定值系数（CONST）或按结构群组（GROUP）
                    "COEF_S": [
                        {
                            "GRUP": "",
                            "DIA": 0.5,           # 构件直径
                            "DRAG_COEF_X": 0.0,
                            "DRAG_COEF_Y": 0.65,  # 拖曳力系数 Y
                            "DRAG_COEF_Z": 0.65,  # 拖曳力系数 Z
                            "INER_COEF_X": 0.0,
                            "INER_COEF_Y": 2.0,   # 惯性力系数 Y
                            "INER_COEF_Z": 2.0    # 惯性力系数 Z
                        }
                    ],
                    "COEF_R": [],
                    "bOVER": False,
                    "OVER_S": [],
                    "OVER_R": []
                },
                # 波浪特性
                "CHAR": {
                    "THEORY": "STOKES",  # Airy / Stokes / Stream
                    "FUNC": 5,           # Stokes 5 阶
                    "DIR": 0.0,          # 波浪传播方向 (°)
                    "HEIGHT": 12.5,      # 波高 (m)
                    "CHAR_TYPE": "PERIOD",
                    "LENGTH": 0.0,
                    "PERIOD": 14.0,      # 波周期 (s)
                    "K_FACTOR": 1.0,     # 运动学系数
                    "SURFACE_V": 0.5,    # 表面流速
                    "BOTTOM_Y": 0.1      # 底面流速
                },
                # 海流剖面
                "PROF": {
                    "CUR_DIR": 0.0,
                    "CUR_FACTOR": 0.9,
                    "GRID_DATA": [
                        {"D": 0.0,   "V": 0.5},
                        {"D": -15.0, "V": 0.3},
                        {"D": -30.0, "V": 0.1}
                    ]
                },
                "FLOOD_GRUP": [],
                # 海生物附着 (Marine Growth)
                "GROWTH": [
                    {"Z": 0.0,   "T": 0.05},
                    {"Z": -10.0, "T": 0.08}
                ],
                "GRID_X": 10,
                "GRID_Z": 10,
                "bSELFW": True,      # 包含自重
                "bBUOYANT": True,    # 包含浮力
                "CREST": "MXM",      # Crest Critical Position（原文示例确认值）
                "UNIT": "PHASE",     # Crest Position Unit（原文示例确认值）
                "INITAL_POS": 0.0,
                "STEP": 1.0,
                "POS": 10
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/WVLD", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Wave Load created:", resp.json())

create_wave_load()
```

---

## 6. /db/IELC — Ignore Elements for Load Cases

设置使指定单元在所给荷载工况中被忽略。在非线性分析等场景下控制特定单元不参与荷载传递。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/IELC` | 创建忽略单元设置 |
| GET | `{base_url}/db/IELC` | 查询全部 |
| GET | `{base_url}/db/IELC/{id}` | 查询特定条目 |
| PUT | `{base_url}/db/IELC/{id}` | 修改 |
| DELETE | `{base_url}/db/IELC/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Element ID | `"ELEMENT"` | Integer | - | Required |
| 2 | Load Case Name | `"LCNAME"` | String | - | Required |
| 3 | Ignore Option | `"OPT_IGNORE"` | Boolean | - | Required |

> **参考**：每条记录表示一个（单元，荷载工况）组合。若要在同一单元上忽略多个荷载工况，需注册多条记录。

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ELEMENT": 5,
      "LCNAME": "DL",
      "OPT_IGNORE": true
    },
    "2": {
      "ELEMENT": 5,
      "LCNAME": "LL",
      "OPT_IGNORE": true
    },
    "3": {
      "ELEMENT": 18,
      "LCNAME": "DL",
      "OPT_IGNORE": false
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_ignore_elements():
    payload = {
        "Assign": {
            "1": {
                "ELEMENT": 5,          # 单元 ID
                "LCNAME": "DL",        # 荷载工况名称
                "OPT_IGNORE": True     # true：在该荷载工况中忽略该单元
            },
            "2": {
                "ELEMENT": 5,
                "LCNAME": "LL",
                "OPT_IGNORE": True
            },
            "3": {
                "ELEMENT": 18,
                "LCNAME": "DL",
                "OPT_IGNORE": False    # false：解除忽略
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/IELC", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Ignore Elements set:", resp.json())

set_ignore_elements()
```

---

## 7. /db/IFGS — Large Displacement – Initial Forces for Geometric Stiffness

在大位移（Large Displacement）分析中，按单元定义用于几何刚度矩阵计算的初始力（Initial Force）。Assign Key 为单元（Element）ID。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/IFGS` | 创建初始力 |
| GET | `{base_url}/db/IFGS` | 查询全部 |
| GET | `{base_url}/db/IFGS/{element_id}` | 查询特定单元 |
| PUT | `{base_url}/db/IFGS/{element_id}` | 修改 |
| DELETE | `{base_url}/db/IFGS/{element_id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Direction (`"GX"` / `"GY"` / `"GZ"` / `"AXIAL"`) | `"DIR"` | String | - | Required |
| 2 | Initial Force | `"INIT_FORCE"` | Number | - | Required |

> **参考**：Assign Key 为单元编号（Element ID）。`"DIR"` 表示初始力的作用方向，`"AXIAL"` 表示轴向。

### Request Body (POST)

```json
{
  "Assign": {
    "9": {
      "DIR": "GY",
      "INIT_FORCE": 200
    },
    "16": {
      "DIR": "AXIAL",
      "INIT_FORCE": 10
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_initial_forces_geometric_stiffness():
    payload = {
        "Assign": {
            # Key = Element ID
            "9": {
                "DIR": "GY",         # 全局坐标系 Y 方向
                "INIT_FORCE": 200    # 初始力 (kN)
            },
            "16": {
                "DIR": "AXIAL",      # 构件轴向
                "INIT_FORCE": 10
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/IFGS", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Initial Forces (Geometric Stiffness) set:", resp.json())

set_initial_forces_geometric_stiffness()
```

---

## 8. /db/EFCT — Small Displacement – Initial Force Control Data

定义小位移（Small Displacement）分析中的初始力控制数据。将荷载工况或荷载组合设为初始力，并控制是否反映到几何刚度。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/EFCT` | 创建初始力控制数据 |
| GET | `{base_url}/db/EFCT` | 查询全部 |
| GET | `{base_url}/db/EFCT/{id}` | 查询特定条目 |
| PUT | `{base_url}/db/EFCT/{id}` | 修改 |
| DELETE | `{base_url}/db/EFCT/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Use Add Initial Force to Element Force | `"bADDLC"` | Boolean | false | Optional |
| 2 | Load Case Name | `"LCNAME"` | String | - | Required |
| 3 | Use Initial Force Combination | `"bUSECOMB"` | Boolean | false | Optional |
| 4 | Initial Force Combination Cases | `"COMB_LIST"` | Array [Object] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | - | Required |
| 5 | Check to Reflect Initial Axial Forces into Geometric Stiffness | `"bCHECK_GEOM_STIFF"` | Boolean | false | Optional |

> **参考**：
> - `bADDLC = true`：将初始力叠加到单元内力上。
> - `bUSECOMB = true`：不使用单一荷载工况（`LCNAME`），而以 `COMB_LIST` 的组合充当初始力。
> - `bCHECK_GEOM_STIFF = true`：将初始轴力反映到几何刚度矩阵中。

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "bADDLC": false,
      "LCNAME": "DL",
      "bUSECOMB": true,
      "COMB_LIST": [
        {
          "LCNAME": "DL",
          "FACTOR": 1.2
        },
        {
          "LCNAME": "LL",
          "FACTOR": 1.0
        }
      ],
      "bCHECK_GEOM_STIFF": false
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_initial_force_control():
    payload = {
        "Assign": {
            "1": {
                "bADDLC": False,        # 是否将初始力叠加到单元内力
                "LCNAME": "DL",         # 基准荷载工况
                "bUSECOMB": True,       # 是否使用组合
                "COMB_LIST": [
                    {
                        "LCNAME": "DL",
                        "FACTOR": 1.2   # 荷载工况缩放系数
                    },
                    {
                        "LCNAME": "LL",
                        "FACTOR": 1.0
                    }
                ],
                # 将初始轴力反映到几何刚度
                "bCHECK_GEOM_STIFF": False
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/EFCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Initial Force Control Data set:", resp.json())

set_initial_force_control()
```

---

## 9. /db/INMF — Small Displacement – Initial Element Force

在小位移分析中直接指定各单元的初始单元力（Initial Element Force）。力数组的大小随单元类型而异。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/INMF` | 创建初始单元力 |
| GET | `{base_url}/db/INMF` | 查询全部 |
| GET | `{base_url}/db/INMF/{id}` | 查询特定条目 |
| PUT | `{base_url}/db/INMF/{id}` | 修改 |
| DELETE | `{base_url}/db/INMF/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Element Type | `"ELEM_TYPE"` | String | - | Required |
| 2 | Element ID | `"ELEM_KEY"` | Integer | - | Required |
| 3 | Element Forces | `"ELEMENT_FORCES"` | Array [Number] | - | Required |

**ELEM_TYPE 取值：**

| Value | Description |
|-------|-------------|
| `"BEAM"` | 梁（Beam）单元 |
| `"TRUSS"` | 桁架（Truss）单元 |
| `"E-LINK"` | Elastic Link 单元 |
| `"G-LINK"` | 一般连接（General Link）单元 |

**ELEMENT_FORCES 数组结构（按单元类型）：**

| ELEM_TYPE | 数组大小 | 次序 |
|-----------|-----------|------|
| `"BEAM"` | 12 | Axial-i, Vy-i, Vz-i, Torsion-i, My-i, Mz-i, Axial-j, Vy-j, Vz-j, Torsion-j, My-j, Mz-j |
| `"TRUSS"` | 2 | Axial-i, Axial-j |
| `"E-LINK"` | 12 | Axial-i, Vy-i, Vz-i, Torsion-i, My-i, Mz-i, Axial-j, Vy-j, Vz-j, Torsion-j, My-j, Mz-j |
| `"G-LINK"` | 12 | Axial-i, Vy-i, Vz-i, Torsion-i, My-i, Mz-i, Axial-j, Vy-j, Vz-j, Torsion-j, My-j, Mz-j |

> ⚠️ **类型标注依据（2026-09-06 确认）。** 原文 Specifications 表第 3 项把 `"ELEMENT_FORCES"` 写作
> `Array [Number, 12]`（固定长度 12），但同一原文的第二个示例向
> `"ELEM_TYPE": "TRUSS"` 发送 `"ELEMENT_FORCES": [1, 2]`（2 个），二者互相矛盾。
> 按示例优先于表的原则，上表记为不限长度的 `Array [Number]`，实际
> 大小按单元类型整理于此 — 请勿回退。
> （TRUSS 的 `Axial-i, Axial-j` 次序系我方推测，原文仅说明 12 分量的次序。）

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ELEM_TYPE": "BEAM",
      "ELEM_KEY": 15,
      "ELEMENT_FORCES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    "2": {
      "ELEM_TYPE": "TRUSS",
      "ELEM_KEY": 112,
      "ELEMENT_FORCES": [1, 2]
    },
    "3": {
      "ELEM_TYPE": "E-LINK",
      "ELEM_KEY": 1,
      "ELEMENT_FORCES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    },
    "4": {
      "ELEM_TYPE": "G-LINK",
      "ELEM_KEY": 1,
      "ELEMENT_FORCES": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    }
  }
}
```

### Python Code Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def set_initial_element_forces():
    payload = {
        "Assign": {
            # Assign Key：记录序号（并非单元 ID）
            "1": {
                "ELEM_TYPE": "BEAM",  # 梁单元
                "ELEM_KEY": 15,       # 单元 ID
                # [Axial-i, Vy-i, Vz-i, T-i, My-i, Mz-i,
                #  Axial-j, Vy-j, Vz-j, T-j, My-j, Mz-j]
                "ELEMENT_FORCES": [100, 0, 50, 0, 200, 0, -100, 0, -50, 0, -200, 0]
            },
            "2": {
                "ELEM_TYPE": "TRUSS",  # 桁架单元
                "ELEM_KEY": 112,
                # [Axial-i, Axial-j]
                "ELEMENT_FORCES": [150, -150]
            },
            "3": {
                "ELEM_TYPE": "E-LINK",  # Elastic Link
                "ELEM_KEY": 1,
                "ELEMENT_FORCES": [10, 0, 0, 0, 0, 0, -10, 0, 0, 0, 0, 0]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/INMF", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Initial Element Forces set:", resp.json())

# 查询特定单元的初始力
def get_initial_element_force(record_id: int):
    resp = requests.get(f"{BASE_URL}/db/INMF/{record_id}", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

set_initial_element_forces()
```

---

## End-to-End 工作流示例

沉降分析与其他荷载设置的完整流程：**SMPT → SMLC → PLCB → LDSQ → WVLD → IELC → EFCT → INMF**

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

def post(endpoint, payload):
    resp = requests.post(f"{BASE_URL}{endpoint}", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print(f"[OK] POST {endpoint}")
    return resp.json()

# Step 1: 定义沉降群组
post("/db/SMPT", {"Assign": {
    "1": {"NAME": "SG1", "SETTLE": 25, "ITEMS": [100, 101]},
    "2": {"NAME": "SG2", "SETTLE": 15, "ITEMS": [102, 103]}
}})

# Step 2: 定义沉降荷载工况
post("/db/SMLC", {"Assign": {
    "1": {
        "NAME": "SLC1",
        "DESC": "",
        "FACTOR": 1.0,
        "MIN": 1,
        "MAX": 2,
        "ST_GROUPS": ["SG1", "SG2"]
    }
}})

# Step 3: 设置 Pre-composite 荷载工况
post("/db/PLCB", {"Assign": {
    "1": {"LCNAME_ITEM": ["DL(BC)1", "DL(BC)2"]}
}})

# Step 4: 设置非线性荷载顺序
post("/db/LDSQ", {"Assign": {
    "1": {"LCNAME_ITEM": ["DL", "LL", "SLC1"]}
}})

# Step 5: 定义波浪荷载
post("/db/WVLD", {"Assign": {
    "1": {
        "NAME": "WV_OPE",
        "DESC": "Operating wave",
        "bSTLD": True,
        "bTHIS": False,
        "NAME_THIS": "",
        "VERT_COORD": "GLOBAL_Z",
        "DENSITY": 10.05,
        "DEPTH": 30.0,
        "COEF": {
            "TYPE": "CONST",
            "COEF_S": [{"GRUP": "", "DIA": 0.5,
                        "DRAG_COEF_X": 0.0, "DRAG_COEF_Y": 0.65, "DRAG_COEF_Z": 0.65,
                        "INER_COEF_X": 0.0, "INER_COEF_Y": 2.0, "INER_COEF_Z": 2.0}],
            "COEF_R": [], "bOVER": False, "OVER_S": [], "OVER_R": []
        },
        "CHAR": {
            "THEORY": "AIRY", "FUNC": 1,
            "DIR": 0.0, "HEIGHT": 5.0,
            "CHAR_TYPE": "PERIOD", "LENGTH": 0.0, "PERIOD": 8.0,
            "K_FACTOR": 1.0, "SURFACE_V": 0.3, "BOTTOM_Y": 0.05
        },
        "PROF": {"CUR_DIR": 0.0, "CUR_FACTOR": 1.0, "GRID_DATA": []},
        "FLOOD_GRUP": [], "GROWTH": [],
        "GRID_X": 5, "GRID_Z": 5,
        "bSELFW": True, "bBUOYANT": True,
        "CREST": "MXM", "UNIT": "PHASE",
        "INITAL_POS": 0.0, "STEP": 1.0, "POS": 5
    }
}})

# Step 6: 设置特定单元忽略荷载工况
post("/db/IELC", {"Assign": {
    "1": {"ELEMENT": 5, "LCNAME": "WV_OPE", "OPT_IGNORE": True}
}})

# Step 7: 设置小位移初始力控制
post("/db/EFCT", {"Assign": {
    "1": {
        "bADDLC": False,
        "LCNAME": "DL",
        "bUSECOMB": False,
        "COMB_LIST": [],
        "bCHECK_GEOM_STIFF": True
    }
}})

# Step 8: 指定初始单元力
post("/db/INMF", {"Assign": {
    "1": {
        "ELEM_TYPE": "BEAM",
        "ELEM_KEY": 15,
        "ELEMENT_FORCES": [100, 0, 50, 0, 200, 0, -100, 0, -50, 0, -200, 0]
    }
}})

print("\nAll Settlement & Miscellaneous Load settings applied successfully.")
```

---

*下一部分：[12_DB_Analysis_Control.md](./12_DB_Analysis_Control.md)*
