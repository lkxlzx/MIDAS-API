# 12. DB – Analysis Control

分析控制(Analysis Control)相关的数据库 API。定义主控制、P-Delta、屈曲、特征值、水化热、移动荷载、沉降、非线性、施工阶段、边界变更等分析选项。

> **Base URL**
> - Civil NX : `https://moa-engineers.midasit.com:443/civil`
> - Gen NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **认证头** ：所有请求都必须包含 `MAPI-Key: <your_api_key>` 头部。
>
> **Hyper-S (`-M1`) 端点** ：基于 MIDAS Engineering Core(MEC) 的新一代求解器的控制数据。采用嵌套对象结构与基于 `enum` 的字符串值，部分端点仅支持 `GET, PUT, DELETE`(不支持 POST)。

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../12_DB_Analysis_Control.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

| No. | Endpoint | 说明 | 备注 |
|-----|----------|------|------|
| 1 | [/db/ACTL](#1-dbactl--main-control-data) | Main Control Data | |
| 2 | [/db/ACTL-M1](#2-dbactl-m1--main-control-data-hyper-s) | Main Control Data | Hyper-S |
| 3 | [/db/PDEL](#3-dbpdel--p-delta-analysis-control) | P-Delta Analysis Control | |
| 4 | [/db/BUCK](#4-dbbuck--buckling-analysis-control) | Buckling Analysis Control | |
| 5 | [/db/EIGV](#5-dbeigv--eigenvalue-analysis-control) | Eigenvalue Analysis Control | |
| 6 | [/db/EIGV-M1](#6-dbeigv-m1--eigenvalue-analysis-control-hyper-s) | Eigenvalue Analysis Control | Hyper-S |
| 7 | [/db/HHCT](#7-dbhhct--heat-of-hydration-analysis-control) | Heat of Hydration Analysis Control | |
| 8 | [/db/HHCT-M1](#8-dbhhct-m1--heat-of-hydration-analysis-control-hyper-s) | Heat of Hydration Analysis Control | Hyper-S |
| 9 | [/db/MVCT](#9-dbmvct--moving-load-analysis-control) | Moving Load Analysis Control | |
| 10 | [/db/MVCTch](#10-dbmvctch--moving-load-analysis-control--china) | Moving Load Analysis Control – China | |
| 11 | [/db/MVCTid](#11-dbmvctid--moving-load-analysis-control--india) | Moving Load Analysis Control – India | |
| 12 | [/db/MVCTbs](#12-dbmvctbs--moving-load-analysis-control--bs) | Moving Load Analysis Control – BS | |
| 13 | [/db/MVCTtr](#13-dbmvcttr--moving-load-analysis-control--transverse) | Moving Load Analysis Control – Transverse | |
| 14 | [/db/SMCT](#14-dbsmct--settlement-analysis-control-data) | Settlement Analysis Control Data | |
| 15 | [/db/NLCT](#15-dbnlct--nonlinear-analysis-control-data) | Nonlinear Analysis Control Data | |
| 16 | [/db/NLCT-M1](#16-dbnlct-m1--nonlinear-analysis-control-hyper-s) | Nonlinear Analysis Control | Hyper-S |
| 17 | [/db/STCT](#17-dbstct--construction-stage-analysis-control-data) | Construction Stage Analysis Control Data | |
| 18 | [/db/STCT-M1](#18-dbstct-m1--construction-stage-analysis-control-data-hyper-s) | Construction Stage Analysis Control Data | Hyper-S |
| 19 | [/db/BCCT](#19-dbbcct--boundary-change-assignment) | Boundary Change Assignment | |
| 20 | [/db/BCGD-M1](#20-dbbcgd-m1--define-boundary-combination-hyper-s) | Define Boundary Combination | Hyper-S |
| 21 | [/db/BCGA-M1](#21-dbbcga-m1--assign-boundary-combination-hyper-s) | Assign Boundary Combination | Hyper-S |

---

## 1. /db/ACTL — Main Control Data

定义分析的基本控制数据。设置自动约束、迭代次数、收敛容差等。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/ACTL` | 创建主控制数据 |
| GET | `{base_url}/db/ACTL` | 查询 |
| PUT | `{base_url}/db/ACTL/{id}` | 修改 |
| DELETE | `{base_url}/db/ACTL/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Auto Rotational DOF Constraint for Truss / Plane Stress / Solid Elements | `"ARDC"` | Boolean | false | Optional |
| 2 | Auto Normal Rotation Constraint for Plate Elements | `"ANRC"` | Boolean | false | Optional |
| 3 | Consider Section Stiffness Scale Factor for Stress Calculation | `"CSECF"` | Boolean | false | Optional |
| 4 | Transfer Reactions of Slave Node to the Master Node | `"TRS"` | Boolean | false | Optional |
| 5 | Calculate Equivalent Beam Stresses (Von-Mises and Max-Shear) | `"BMSTRESS"` | Boolean | false | Optional |
| 6 | Consider Reinforcement for Section Stiffness Calculation | `"CRBAR"` | Boolean | false | Optional |
| 7 | Change Local Axis of Tapered Section for Force / Stress Calculation | `"CLATS"` | Boolean | false | Optional |
| 8 | Number of Iterations / Load Case | `"ITER"` | Number | - | Required |
| 9 | Convergence Tolerance | `"TOL"` | Number | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ARDC": true,
      "ANRC": true,
      "ITER": 20,
      "TOL": 0.001,
      "CSECF": false,
      "TRS": true,
      "CRBAR": false,
      "BMSTRESS": false,
      "CLATS": false
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

def set_main_control():
    payload = {
        "Assign": {
            "1": {
                "ARDC": True,      # 桁架/平面应力/实体单元自动旋转约束
                "ANRC": True,      # 板单元自动法线旋转约束
                "ITER": 20,        # 每荷载工况的迭代次数
                "TOL": 0.001,      # 收敛容差
                "CSECF": False,    # 应力计算时考虑截面刚度比例系数
                "TRS": True,       # 将从属节点的反力传递至主节点
                "CRBAR": False,    # 截面刚度计算时考虑钢筋
                "BMSTRESS": False, # 计算等效梁应力
                "CLATS": False     # 变截面局部轴变更
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/ACTL", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Main Control Data set:", resp.json())

set_main_control()
```

---

## 2. /db/ACTL-M1 — Main Control Data (Hyper-S)

用于 Hyper-S(MEC) 求解器的主控制数据。以嵌套对象形式包含拉/压桁架单元(Tension/Compression Truss)的高级非线性参数(`TCELEM`)。

> **Active Methods**：`GET, PUT, DELETE`(不支持 POST)。原文并未说明没有 POST 的原因
> — ⚠️ 2026-08-30 确认：此前曾附上"会自动生成默认记录"这一依据，但原文任何位置
> 都没有该说明，经确认属于无依据的推断，故删除。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| GET | `{base_url}/db/ACTL-M1` | 查询 |
| PUT | `{base_url}/db/ACTL-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/ACTL-M1/{id}` | 删除 |

### Parameters — 基本设置

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Auto Rotational DOF Constraint | `"ARCD"` | Boolean | true | Optional |
| 2 | Auto Normal Rotation Constraint | `"ANRC"` | Boolean | true | Optional |
| 3 | Consider Section Stiffness Scale Factor | `"CSECF"` | Boolean | false | Optional |
| 4 | Consider Reinforcement for Section Stiffness | `"CRBAR"` | Boolean | false | Optional |
| 5 | Transfer Reactions to Master Node | `"TRS"` | Boolean | true | Optional |
| 6 | Change Local Axis of Tapered Section | `"CLATS"` | Boolean | false | Optional |
| 7 | Calculate Equivalent Beam Stresses | `"BMSTRESS"` | Boolean | false | Optional |
| 8 | Classical Formula for Solid Element | `"CLFORM"` | Boolean | false | Optional |
| 9 | Beam Section Property Changes (`"CONSTANT"` / `"CHANGE"`) | `"BSCHG"` | String (enum) | "CHANGE" | Optional |
| 10 | Consider Initial Tension for Cable Element | `"CABINIT"` | Boolean | true | Optional |
| 11 | Tension/Compression Truss Element | `"TCELEM"` | Object | - | Optional |

### Parameters — TCELEM 对象（拉/压桁架）

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Number of Increments | `"NUMINC"` | Integer | 1 | Optional |
| 2 | Intermediate Output Request (`"EVERY"` / `"LAST"`) | `"INTOUT"` | String (enum) | "LAST" | Optional |
| 3 | Convergence Criteria | `"CONVERGENCE"` | Object | - | Optional |

**CONVERGENCE 对象** — `DISPL`(位移 U) / `LOAD`(荷载 P) / `WORK`(功 W) 各自：

| Key | Value Type | Description |
|-----|------------|-------------|
| `"OPT_USE"` | Boolean | 是否使用该项准则 |
| `"VALUE"` | Number | 容差 (OPT_USE = true 时必填) |

### Request Body (PUT)

```json
{
  "Assign": {
    "1": {
      "ARCD": true,
      "ANRC": true,
      "CSECF": false,
      "CRBAR": false,
      "TRS": true,
      "CLATS": false,
      "BMSTRESS": false,
      "CLFORM": false,
      "BSCHG": "CHANGE",
      "CABINIT": true,
      "TCELEM": {
        "NUMINC": 10,
        "INTOUT": "LAST",
        "CONVERGENCE": {
          "DISPL": { "OPT_USE": true, "VALUE": 0.001 },
          "LOAD":  { "OPT_USE": false },
          "WORK":  { "OPT_USE": false }
        }
      }
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

def update_main_control_m1():
    payload = {
        "Assign": {
            "1": {
                "ARCD": True,
                "ANRC": True,
                "CSECF": False,
                "CRBAR": False,
                "TRS": True,
                "CLATS": False,
                "BMSTRESS": False,
                "CLFORM": False,
                "BSCHG": "CHANGE",       # 梁截面物性变更方式
                "CABINIT": True,         # 考虑拉索初始张力
                "TCELEM": {              # 拉/压桁架单元控制
                    "NUMINC": 10,        # 增量数
                    "INTOUT": "LAST",    # 中间输出：仅最后一步
                    "CONVERGENCE": {
                        "DISPL": {"OPT_USE": True, "VALUE": 0.001},
                        "LOAD":  {"OPT_USE": False},
                        "WORK":  {"OPT_USE": False}
                    }
                }
            }
        }
    }
    # Hyper-S 端点以 PUT 修改
    resp = requests.put(f"{BASE_URL}/db/ACTL-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Main Control (Hyper-S) updated:", resp.json())

update_main_control_m1()
```

---

## 3. /db/PDEL — P-Delta Analysis Control

定义 P-Delta(二阶效应)分析控制数据。设置迭代次数、收敛容差、目标荷载工况。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/PDEL` | 创建 P-Delta 控制 |
| GET | `{base_url}/db/PDEL` | 查询 |
| PUT | `{base_url}/db/PDEL/{id}` | 修改 |
| DELETE | `{base_url}/db/PDEL/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Number of Iterations | `"ITER"` | Number | - | Required |
| 2 | Convergence Tolerance | `"TOL"` | Number | 0 | Optional |
| 3 | Load Cases | `"PDEL_CASES"` | Array [Object] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "ITER": 5,
      "TOL": 1e-05,
      "PDEL_CASES": [
        { "LCNAME": "A", "FACTOR": 1 },
        { "LCNAME": "B", "FACTOR": 1 }
      ]
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

def set_pdelta_control():
    payload = {
        "Assign": {
            "1": {
                "ITER": 5,           # 迭代次数
                "TOL": 1e-05,        # 收敛容差
                "PDEL_CASES": [      # 应用 P-Delta 的荷载工况
                    {"LCNAME": "DL", "FACTOR": 1.0},
                    {"LCNAME": "LL", "FACTOR": 1.0}
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/PDEL", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("P-Delta Control set:", resp.json())

set_pdelta_control()
```

---

## 4. /db/BUCK — Buckling Analysis Control

定义屈曲(Buckling)分析控制数据。设置振型数、荷载系数范围、Sturm Sequence 检查、屈曲组合。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/BUCK` | 创建屈曲控制 |
| GET | `{base_url}/db/BUCK` | 查询 |
| PUT | `{base_url}/db/BUCK/{id}` | 修改 |
| DELETE | `{base_url}/db/BUCK/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Number of Modes | `"MODE_NUM"` | Integer | - | Required |
| 2 | Load Factor Range Type (Positive Value Only: true / Search: false) | `"OPT_POSITIVE"` | Boolean | false | Optional |
| 3 | Search From (when `OPT_POSITIVE` is false) | `"LOAD_FACTOR_FROM"` | Number | 0 | Optional |
| 4 | Search To (when `OPT_POSITIVE` is false) | `"LOAD_FACTOR_TO"` | Number | 0 | Optional |
| 5 | Check Sturm Sequence | `"OPT_STURM_SEQ"` | Boolean | false | Optional |
| 6 | Frame Geometric Stiffness Option (Consider Axial Only) | `"OPT_CONSIDER_AXIAL_ONLY"` | Boolean | false | Optional |
| 7 | Load Cases (Buckling Combination) | `"ITEMS"` | Array [Object] | - | Required |
| (1) | Load Case Name | `"LCNAME"` | String | - | Required |
| (2) | Scale Factor | `"FACTOR"` | Number | 0 | Optional |
| (3) | Load Type (Variable: 0 / Constant: 1) | `"LOAD_TYPE"` | Integer | 0 | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "MODE_NUM": 12,
      "OPT_POSITIVE": true,
      "OPT_CONSIDER_AXIAL_ONLY": true,
      "LOAD_FACTOR_FROM": 0,
      "LOAD_FACTOR_TO": 0,
      "OPT_STURM_SEQ": true,
      "ITEMS": [
        { "LCNAME": "A", "FACTOR": 1, "LOAD_TYPE": 0 },
        { "LCNAME": "B", "FACTOR": 1, "LOAD_TYPE": 1 }
      ]
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

def set_buckling_control():
    payload = {
        "Assign": {
            "1": {
                "MODE_NUM": 12,                    # 屈曲振型数
                "OPT_POSITIVE": True,              # 仅使用正荷载系数
                "OPT_CONSIDER_AXIAL_ONLY": True,   # 仅考虑轴力
                "LOAD_FACTOR_FROM": 0,
                "LOAD_FACTOR_TO": 0,
                "OPT_STURM_SEQ": True,             # Sturm Sequence 检查
                "ITEMS": [
                    {"LCNAME": "DL", "FACTOR": 1, "LOAD_TYPE": 1},  # Constant
                    {"LCNAME": "LL", "FACTOR": 1, "LOAD_TYPE": 0}   # Variable
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BUCK", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Buckling Control set:", resp.json())

set_buckling_control()
```

---

## 5. /db/EIGV — Eigenvalue Analysis Control

定义特征值(Eigenvalue)分析控制数据。参数随分析类型(`TYPE`)而不同：Subspace Iteration(`EIGEN`)、Lanczos(`LANCZOS`)、Ritz Vectors(`RITZ`)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/EIGV` | 创建特征值控制 |
| GET | `{base_url}/db/EIGV` | 查询 |
| PUT | `{base_url}/db/EIGV/{id}` | 修改 |
| DELETE | `{base_url}/db/EIGV/{id}` | 删除 |

### Parameters — 通用

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Type of Analysis (Subspace Iteration: `"EIGEN"` / Lanczos: `"LANCZOS"` / Ritz Vectors: `"RITZ"`) | `"TYPE"` | String | - | Required |

### Parameters — Eigen Vectors (Subspace Iteration, `TYPE = "EIGEN"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Number of Frequencies | `"iFREQ"` | Integer | - | Required |
| 3 | Number of Iterations | `"iITER"` | Integer | - | Required |
| 4 | Subspace Dimension | `"iDIM"` | Integer | 0 | Optional |
| 5 | Convergence Tolerance | `"TOL"` | Number | 0 | Optional |

### Parameters — Eigen Vectors (Lanczos, `TYPE = "LANCZOS"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Number of Frequencies | `"iFREQ"` | Integer | - | Required |
| 3 | Frequency Range of Interest | `"bMINMAX"` | Boolean | false | Optional |
| 4 | Search From [cps] (when `bMINMAX` is true, `FRMIN` < `FRMAX`) | `"FRMIN"` | Number | - | Required |
| 5 | Search To [cps] (when `bMINMAX` is true) | `"FRMAX"` | Number | - | Required |
| 6 | Sturm Sequence Check | `"bSTRUM"` | Boolean | false | Optional |

### Parameters — Ritz Vectors (`TYPE = "RITZ"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Include GL-link Force Vectors | `"bINCNL"` | Boolean | false | Optional |
| 3 | Number of Generations for Each GL-link Force | `"iGNUM"` | Integer | - | Required |
| 4 | Load Cases | `"vRITZ"` | Array [Object] | - | Required |
| (1) | Load Case Type (Ground Acc.: `"GROUND"` / General: `"CASE"`) | `"KIND"` | String | - | Required |
| (2) | Load Case Name (`KIND="CASE"` 时) | `"CASE"` | String | - | Required |
| (3) | Ground Acc. 方向 (`KIND="GROUND"` 时，`"ACCX"`/`"ACCY"`/`"ACCZ"`) | `"GROUND"` | String | - | Required |
| (4) | Number of Generations | `"iNOG"` | Integer | Blank | Optional |

> ⚠️ **2026-08-25 确认：** 原文 Specifications 表把 (2) 项的 Key 只标注为 `"CASE"` 一个，
> 将 General/Ground Acc. 两个分支混为一谈，但 JSON Schema 把 `CASE` 与 `GROUND` 声明为独立
> 属性，并且原文示例与下方本地示例在 Ground Acc. 项中均使用 `"GROUND"` 键
>（该表连自己的示例也相矛盾）。按示例·schema 优先原则拆分该表予以更正（article id
> `35989224565273`）。

### Request Body — Subspace Iteration

```json
{
  "Assign": {
    "1": {
      "TYPE": "EIGEN",
      "iFREQ": 100,
      "iITER": 20,
      "iDIM": 1,
      "TOL": 1e-10,
      "bMINMAX": false,
      "FRMIN": 0,
      "FRMAX": 1600,
      "bSTRUM": false
    }
  }
}
```

### Request Body — Lanczos

```json
{
  "Assign": {
    "1": {
      "TYPE": "LANCZOS",
      "iFREQ": 100,
      "bMINMAX": false,
      "FRMIN": 0,
      "FRMAX": 0,
      "bSTRUM": false
    }
  }
}
```

> ⚠️ **2026-08-25 确认：** 此前的示例错误地混入了 Subspace Iteration(`TYPE="EIGEN"`) 专用字段 `iITER`/
> `iDIM`/`TOL`（上方 Lanczos 参数表中也没有的字段）。因原文 Lanczos 示例中
> 不存在这些字段，故删除（article id `35989224565273`）。

### Request Body — Ritz Vectors

```json
{
  "Assign": {
    "1": {
      "TYPE": "RITZ",
      "bINCNL": false,
      "iGNUM": 1,
      "vRITZ": [
        { "KIND": "GROUND", "GROUND": "ACCX", "iNOG": 30 },
        { "KIND": "GROUND", "GROUND": "ACCY", "iNOG": 30 },
        { "KIND": "GROUND", "GROUND": "ACCZ", "iNOG": 30 }
      ]
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

# 以 Lanczos 方式控制特征值分析
def set_eigenvalue_lanczos():
    payload = {
        "Assign": {
            "1": {
                "TYPE": "LANCZOS",   # Lanczos 方式
                "iFREQ": 30,         # 固有频率个数
                "bMINMAX": True,     # 使用关注频率范围
                "FRMIN": 0.1,        # 搜索起点 [cps]
                "FRMAX": 50,         # 搜索终点 [cps]
                "bSTRUM": True       # Sturm Sequence 检查
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/EIGV", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Eigenvalue (Lanczos) set:", resp.json())

# Ritz Vector 方式（基于地面加速度）
def set_eigenvalue_ritz():
    payload = {
        "Assign": {
            "1": {
                "TYPE": "RITZ",
                "bINCNL": False,
                "iGNUM": 1,
                "vRITZ": [
                    {"KIND": "GROUND", "GROUND": "ACCX", "iNOG": 30},
                    {"KIND": "GROUND", "GROUND": "ACCY", "iNOG": 30},
                    {"KIND": "GROUND", "GROUND": "ACCZ", "iNOG": 30}
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/EIGV", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Eigenvalue (Ritz) set:", resp.json())

set_eigenvalue_lanczos()
```

---

## 6. /db/EIGV-M1 — Eigenvalue Analysis Control (Hyper-S)

用于 Hyper-S(MEC) 求解器的特征值分析控制。UI 中的 Subspace Iteration 在 MEC 里已并入 Lanczos。分析类型为 `LANCZOS` 或 `RITZ`，采用嵌套对象(`FREQ_RANGE`、`GLINK_VECTOR`、`RITZ_LOAD`)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| GET | `{base_url}/db/EIGV-M1` | 查询 |
| PUT | `{base_url}/db/EIGV-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/EIGV-M1/{id}` | 删除 |

### Parameters — 通用

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Eigen Vectors (Lanczos: `"LANCZOS"` / Ritz Vectors: `"RITZ"`) | `"ANAL_TYPE"` | String (enum) | - | Required |

### Parameters — Lanczos (`ANAL_TYPE = "LANCZOS"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Number of Frequencies (1~1000) | `"FREQ_NO"` | Integer | - | Required |
| 3 | Frequency range of interest | `"FREQ_RANGE"` | Object | - | Optional |
| (1) | Use Option | `"OPT_USE"` | Boolean | false | Required |
| (2) | Search From (when `OPT_USE` true) | `"FREQ_MIN"` | Number | - | Required |
| (3) | To (when `OPT_USE` true) | `"FREQ_MAX"` | Number | - | Required |
| 4 | Sturm Sequence Check | `"STURM_SEQ"` | Boolean | false | Optional |

### Parameters — Ritz Vectors (`ANAL_TYPE = "RITZ"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 2 | Include GL-link Force Vectors | `"GLINK_VECTOR"` | Object | - | Optional |
| (1) | Use Option | `"OPT_USE"` | Boolean | - | Required |
| (2) | Number of Generations (when `OPT_USE` true) | `"GLINK_NUMBER"` | Integer | - | Required |
| 3 | Ritz Load Cases | `"RITZ_LOAD"` | Array [Object] | - | Required |
| (1) | Type (Ground Acc.: `"GROUND"` / Load: `"LOAD"`) | `"TYPE"` | String (enum) | - | Required |
| (2) | Load Name (`"ACCX"`/`"ACCY"`/`"ACCZ"` 或荷载工况名) | `"LOAD_NAME"` | String | - | Required |
| (3) | Number of Generations | `"NUM_OF_GEN"` | Integer | - | Required |

### Request Body — Lanczos

```json
{
  "Assign": {
    "1": {
      "ANAL_TYPE": "LANCZOS",
      "FREQ_NO": 30,
      "FREQ_RANGE": {
        "OPT_USE": true,
        "FREQ_MIN": 0.1,
        "FREQ_MAX": 50
      },
      "STURM_SEQ": true
    }
  }
}
```

### Request Body — Ritz Vectors

```json
{
  "Assign": {
    "1": {
      "ANAL_TYPE": "RITZ",
      "GLINK_VECTOR": {
        "OPT_USE": true,
        "GLINK_NUMBER": 3
      },
      "RITZ_LOAD": [
        { "TYPE": "GROUND", "LOAD_NAME": "ACCX", "NUM_OF_GEN": 5 },
        { "TYPE": "GROUND", "LOAD_NAME": "ACCY", "NUM_OF_GEN": 5 },
        { "TYPE": "GROUND", "LOAD_NAME": "ACCZ", "NUM_OF_GEN": 5 },
        { "TYPE": "LOAD", "LOAD_NAME": "DL", "NUM_OF_GEN": 3 },
        { "TYPE": "LOAD", "LOAD_NAME": "LL", "NUM_OF_GEN": 3 }
      ]
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

def update_eigenvalue_m1_ritz():
    payload = {
        "Assign": {
            "1": {
                "ANAL_TYPE": "RITZ",
                "GLINK_VECTOR": {
                    "OPT_USE": True,
                    "GLINK_NUMBER": 3
                },
                "RITZ_LOAD": [
                    {"TYPE": "GROUND", "LOAD_NAME": "ACCX", "NUM_OF_GEN": 5},
                    {"TYPE": "GROUND", "LOAD_NAME": "ACCY", "NUM_OF_GEN": 5},
                    {"TYPE": "GROUND", "LOAD_NAME": "ACCZ", "NUM_OF_GEN": 5},
                    {"TYPE": "LOAD", "LOAD_NAME": "DL", "NUM_OF_GEN": 3}
                ]
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/EIGV-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Eigenvalue (Hyper-S, Ritz) updated:", resp.json())

update_eigenvalue_m1_ritz()
```

---

## 7. /db/HHCT — Heat of Hydration Analysis Control

定义水化热(Heat of Hydration)分析控制数据。设置积分系数、初始温度、应力评估位置、徐变·干燥收缩选项。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/HHCT` | 创建水化热控制 |
| GET | `{base_url}/db/HHCT` | 查询 |
| PUT | `{base_url}/db/HHCT/{id}` | 修改 |
| DELETE | `{base_url}/db/HHCT/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage (Last Stage: true / Other Stage: false) | `"FINAL_STAGE"` | Boolean | false | Optional |
| 2 | Construction Stage for Hydration (when `FINAL_STAGE` false) | `"STAGE_NAME"` | String | - | Required |
| 3 | Integration Factor | `"THETA"` | Number | 0 | Optional |
| 4 | Initial Temperature | `"INIT_TEMP"` | Number | 0 | Optional |
| 5 | Element Stress Evaluation (`"CENTER"` / `"GAUSS"` / `"NODAL"`) | `"EVAL"` | String | "CENTER" | Optional |
| 6 | Creep & Shrinkage Option | `"OPT_IS_CREEP_SHRINKAGE"` | Boolean | false | Optional |
| 7 | Creep & Shrinkage 设置对象 | `"ITEM"` | Object | - | Optional |
| (1) | Type (Creep: `"CREEP"` / Shrinkage: `"SHRINK"` / Both: `"BOTH"`) | `"TYPE"` | String | "CREEP" | Optional |
| (2) | Creep Calculation Method (General: 0 / Effective Modulus: 1) | `"CREEP_CALC_METHOD"` | Integer | 0 | Optional |
| (3) | General Data (when method 0) | `"M_GENERAL"` | Object | - | Optional |
| i | Number of Iterations | `"ITER"` | Integer | 0 | Optional |
| ii | Tolerance | `"TOL"` | Number | 0 | Optional |
| (3) | Effective Modulus Data (when method 1) | `"M_EFF_MOD"` | Object | - | Required |
| i | Phi1 | `"PHI1"` | Number | - | Required |
| ii | Day1 | `"DAY1"` | Integer | - | Required |
| iii | Phi2 | `"PHI2"` | Number | - | Required |
| iv | Day2 | `"DAY2"` | Integer | - | Required |
| 8 | Use Equivalent Age by Time & Temperature | `"OPT_USE_EQUI_AGE"` | Boolean | false | Optional |
| 9 | Include Self-weight Load | `"OPT_INCL_SELF_WEIGHT"` | Boolean | false | Optional |
| 10 | Self-weight Factor | `"SELF_WEIGHT_FACTOR"` | Number | 0 | Optional |

### Request Body — General

```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": true,
      "STAGE_NAME": "",
      "THETA": 1,
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": false,
      "SELF_WEIGHT_FACTOR": -1,
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 0,
        "M_GENERAL": { "ITER": 20, "TOL": 0.001 }
      }
    }
  }
}
```

### Request Body — Effective Modulus

```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": true,
      "STAGE_NAME": "",
      "THETA": 1,
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": false,
      "SELF_WEIGHT_FACTOR": -1,
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 1,
        "M_EFF_MOD": { "PHI1": 0.73, "DAY1": 3, "PHI2": 1, "DAY2": 5 }
      }
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

def set_hydration_control():
    payload = {
        "Assign": {
            "1": {
                "FINAL_STAGE": True,          # 最后阶段
                "STAGE_NAME": "",
                "THETA": 1,                   # 积分系数
                "INIT_TEMP": 20,              # 初始温度 (°C)
                "EVAL": "GAUSS",              # 应力评估：Gauss point
                "OPT_USE_EQUI_AGE": True,     # 使用等效龄期
                "OPT_INCL_SELF_WEIGHT": False,
                "SELF_WEIGHT_FACTOR": -1,
                "OPT_IS_CREEP_SHRINKAGE": True,
                "ITEM": {
                    "TYPE": "BOTH",            # 徐变 + 干燥收缩
                    "CREEP_CALC_METHOD": 0,    # General 方式
                    "M_GENERAL": {"ITER": 20, "TOL": 0.001}
                }
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/HHCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Heat of Hydration Control set:", resp.json())

set_hydration_control()
```

---

## 8. /db/HHCT-M1 — Heat of Hydration Analysis Control (Hyper-S)

用于 Hyper-S(MEC) 求解器的水化热分析控制。新增了迭代次数(`ITER`)与收敛准则(`CONVERGENCE`)对象。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| GET | `{base_url}/db/HHCT-M1` | 查询 |
| PUT | `{base_url}/db/HHCT-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/HHCT-M1/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage (Last: true / Other: false) | `"FINAL_STAGE"` | Boolean | true | Optional |
| 2 | Stage Name (when `FINAL_STAGE` false) | `"STAGE_NAME"` | String | - | Required |
| 3 | Initial Temperature | `"INIT_TEMP"` | Number | 20 | Optional |
| 4 | Element Stress Evaluation (`"CENTER"`/`"GAUSS"`/`"NODAL"`) | `"EVAL"` | String (enum) | "GAUSS" | Optional |
| 5 | Creep & Shrinkage | `"OPT_IS_CREEP_SHRINKAGE"` | Boolean | true | Optional |
| 6 | Creep & Shrinkage Settings (when option true) | `"ITEM"` | Object | - | Required |
| (1) | Type (`"CREEP"`/`"SHRINKAGE"`/`"BOTH"`) | `"TYPE"` | String (enum) | "BOTH" | Optional |
| (2) | Creep Calculation Method (General: 0 / Effective Modulus: 1) | `"CREEP_CALC_METHOD"` | Integer (enum) | 0 | Optional |
| (3) | Effective Modulus Params (when method 1) | `"M_EFF_MOD"` | Object | - | Required |
| a | phi 1 | `"PHI1"` | Number | - | Required |
| b | day 1 | `"DAY1"` | Integer | - | Required |
| c | phi 2 | `"PHI2"` | Number | - | Required |
| d | day 2 | `"DAY2"` | Integer | - | Required |
| 7 | Use Equivalent Age by Time & Temperature | `"OPT_USE_EQUI_AGE"` | Boolean | true | Optional |
| 8 | Include Selfweight Load | `"OPT_INCL_SELF_WEIGHT"` | Boolean | false | Optional |
| 9 | Self Weight Factor (when option true) | `"SELF_WEIGHT_FACTOR"` | Number | - | Required |
| 10 | Max. No. of Iterations per Increment | `"ITER"` | Integer | 50 | Optional |
| 11 | Convergence Criteria (DISP/LOAD/WORK 中至少 1 个必填) | `"CONVERGENCE"` | Object | - | Optional |
| (1) | Displacement(U) | `"DISP"` | Object | - | Optional |
| (2) | Load(P) | `"LOAD"` | Object | - | Optional |
| (3) | Work(W) | `"WORK"` | Object | - | Optional |
| a | Use Option | `"OPT_CHECK"` | Boolean | - | Required |
| b | Tolerance (when `OPT_CHECK` true) | `"VALUE"` | Number | - | Required |

### Request Body (PUT)

```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": false,
      "STAGE_NAME": "Stage 1",
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 1,
        "M_EFF_MOD": { "PHI1": 1, "DAY1": 3, "PHI2": 2, "DAY2": 28 }
      },
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": true,
      "SELF_WEIGHT_FACTOR": 1,
      "ITER": 50,
      "CONVERGENCE": {
        "DISP": { "OPT_CHECK": true, "VALUE": 0.001 },
        "LOAD": { "OPT_CHECK": true, "VALUE": 0.001 },
        "WORK": { "OPT_CHECK": true, "VALUE": 0.001 }
      }
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

def update_hydration_control_m1():
    payload = {
        "Assign": {
            "1": {
                "FINAL_STAGE": False,
                "STAGE_NAME": "Stage 1",
                "INIT_TEMP": 20,
                "EVAL": "GAUSS",
                "OPT_IS_CREEP_SHRINKAGE": True,
                "ITEM": {
                    "TYPE": "BOTH",
                    "CREEP_CALC_METHOD": 1,             # Effective Modulus
                    "M_EFF_MOD": {"PHI1": 1, "DAY1": 3, "PHI2": 2, "DAY2": 28}
                },
                "OPT_USE_EQUI_AGE": True,
                "OPT_INCL_SELF_WEIGHT": True,
                "SELF_WEIGHT_FACTOR": 1,
                "ITER": 50,                             # 每增量最大迭代次数
                "CONVERGENCE": {                        # 收敛准则 (至少 1 个)
                    "DISP": {"OPT_CHECK": True, "VALUE": 0.001},
                    "LOAD": {"OPT_CHECK": True, "VALUE": 0.001},
                    "WORK": {"OPT_CHECK": True, "VALUE": 0.001}
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/HHCT-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Heat of Hydration (Hyper-S) updated:", resp.json())

update_hydration_control_m1()
```

---

## 9. /db/MVCT — Moving Load Analysis Control

定义移动荷载(Moving Load)分析控制数据。设置分析方法、影响线生成点、板/框架/连接各自的结果选项、计算过滤器(反力/位移/构件内力/连接)。

> **¹⁾** `METHOD`(Analysis Method) 为 MIDAS Civil NX 专用项。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/MVCT` | 创建移动荷载控制 |
| GET | `{base_url}/db/MVCT` | 查询 |
| PUT | `{base_url}/db/MVCT/{id}` | 修改 |
| DELETE | `{base_url}/db/MVCT/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Analysis Method ¹⁾ (Exact: `"EXACT"` / Pivot: `"PIVOT"` / Quick: `"QUICK"`) | `"METHOD"` | String | "EXACT" | Optional |
| 2 | Load Point Selection (Influence Line Dependent: `"INF"` / All Points: `"ALL"`) | `"POINT"` | String | - | Required |
| 3 | Influence Generating Points (Number/Line Element: 0 / Distance: 1) | `"iIGP"` | Integer | 0 | Optional |
| 4 | Number/Line Element (when `iIGP`=0) | `"iIGPN"` | Integer | - | Required |
| 5 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 6 | Plate Options (Center: `"CENTER"` / Center+Nodal: `"NODAL"`) | `"PLATE"` | String | - | Required |
| 7 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 8 | Plate – Concurrent Force | `"bCONCURRENT"` | Boolean | false | Optional |
| 9 | Frame Options (Normal: `"NORMAL"` / Normal+Concurrent: `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 10 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 11 | Link – Concurrent Force of Elastic/General Links | `"bCONCLINK"` | Boolean | false | Optional |
| 12 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 13 | Reactions Option (All: false / Structure Group: true) | `"bRG"` | Boolean | false | Optional |
| 14 | Reactions Group Name (when `bRG` true) | `"RGN"` | String | - | Required |
| 15 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 16 | Displacements Option (All: false / Structure Group: true) | `"bDG"` | Boolean | false | Optional |
| 17 | Displacements Group Name (when `bDG` true) | `"DGN"` | String | - | Required |
| 18 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 19 | Forces/Moments Option (All: false / Structure Group: true) | `"bFG"` | Boolean | false | Optional |
| 20 | Forces/Moments Group Name (when `bFG` true) | `"FGN"` | String | - | Required |
| 21 | Filter – Elastic/General Link | `"bL"` | Boolean | false | Optional |
| 22 | Link Option (All: false / Boundary Group: true) | `"bLG"` | Boolean | false | Optional |
| 23 | Link Group Name (when `bLG` true) | `"LGN"` | String | - | Required |

> 应用 **Russia 代码** 时的附加参数：`MATTYPE`、`BRIDGETYPE`、`AKMATTYPE`、`AKBRIDGETYPE`(Integer)、`MINFACTS2`(Number, 最小系数)、`MAXV`(Integer, 最大连续车辆数)、`INCV`(Integer, 车辆增量)、`MAXSPACE`(Number, 列车最大间距)。

### Request Body — General

```json
{
  "Assign": {
    "1": {
      "METHOD": "EXACT",
      "POINT": "INF",
      "iIGP": 0,
      "iIGPN": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "bCONCURRENT": true,
      "bCONCLINK": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true,
      "bRG": false,
      "RGN": "",
      "bDISP": true,
      "bDG": false,
      "DGN": "",
      "bFM": true,
      "bFG": false,
      "FGN": "",
      "bL": true,
      "bLG": false,
      "LGN": ""
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

def set_moving_load_control():
    payload = {
        "Assign": {
            "1": {
                "METHOD": "EXACT",       # 精确分析法
                "POINT": "INF",          # 影响线从属点
                "iIGP": 0,               # Number/Line Element 方式
                "iIGPN": 3,              # 每构件分割数
                "PLATE": "NODAL",        # 板：中心+节点
                "bSTRCALC": True,        # 板应力计算
                "bCONCURRENT": True,     # 板同时力
                "bCONCLINK": True,       # 连接同时力
                "FRAME": "AXIAL",        # 框架：Normal+同时力
                "bCSTRCALC": True,       # 组合应力
                "bREAC": True,  "bRG": False, "RGN": "",   # 反力 (整体)
                "bDISP": True,  "bDG": False, "DGN": "",   # 位移 (整体)
                "bFM": True,    "bFG": False, "FGN": "",   # 构件内力 (整体)
                "bL": True,     "bLG": False, "LGN": ""    # 连接 (整体)
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control set:", resp.json())

set_moving_load_control()
```

---

## 10. /db/MVCTch — Moving Load Analysis Control – China

中国代码(JTG 等)专用的移动荷载分析控制。包含冲击系数(`bIF`)、代码类型、固有频率方法、频率数据(`FREQ`)、桥梁数据(`BRIDGE1`)等。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTch` | 创建 |
| GET | `{base_url}/db/MVCTch` | 查询 |
| PUT | `{base_url}/db/MVCTch/{id}` | 修改 |
| DELETE | `{base_url}/db/MVCTch/{id}` | 删除 |

### Parameters — 基本（与 MVCT 通用的结果选项）

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Point (`"INF"` / `"ALL"`) | `"POINT"` | String | - | Required |
| 2 | Influence Generating Points (0/1) | `"iIGP"` | Integer | 0 | Optional |
| 3 | Number/Line Element (when `iIGP`=0) | `"UNUMT"` | Integer | - | Required |
| 4 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 5 | Plate Options (`"CENTER"` / `"NODAL"`) | `"PLATE"` | String | - | Required |
| 6 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 7 | Frame Options (`"NORMAL"` / `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 8 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 9 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 10 | Reactions Option (All/Group) | `"bRG"` | Boolean | false | Optional |
| 11 | Reactions Group Name | `"RGN"` | String | - | Required |
| 12 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 13 | Displacements Option (All/Group) | `"bDG"` | Boolean | false | Optional |
| 14 | Displacements Group Name | `"DGN"` | String | - | Required |
| 15 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 16 | Forces/Moments Option (All/Group) | `"bFG"` | Boolean | false | Optional |
| 17 | Forces/Moments Group Name | `"FGN"` | String | - | Required |
| 18 | Filter – Elastic/General Links | `"bL"` | Boolean | false | Optional |
| 19 | Links Option (All/Group) | `"bLG"` | Boolean | false | Optional |
| 20 | Links Group Name | `"LGN"` | String | - | Required |

### Parameters — 冲击系数 (Impact Factor)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 21 | Impact Factor 使用 | `"bIF"` | Boolean | false | Optional |
| 22 | Code Type (`0`=JTG D60-2015/JTG04 / `1`=Other Codes / `2`=TB 10002-2017 / `3`=Q/CR 9300-2018) | `"iCODETYPE"` | Integer | - | Required |
| 23 | Natural Frequency Method (`iCODETYPE`=0 时必填。`0`=User Input / `1`=Simple Beam / `2`=Continuous Beam / `3`=Arch Bridge / `4`=Cable Stayed Bridge / `5`=Suspension Bridge) | `"iNFM"` | Integer | - | Required（条件） |
| 24 | Span Length (`0`=Span Length by Lane Input / `1`=Loaded Length by Influence Line) | `"iSLCM"` | Integer | - | Required |
| 25 | Vehicle Load Class 使用 | `"bBC"` | Boolean | false | Optional |
| 26 | Vehicle Load Class Type (`0`=Class I / `1`=Class II) | `"iBC"` | Integer | 0 | Required |
| 27 | Frequency Data (`iCODETYPE`=0 时必填) | `"FREQ"` | Object | - | Required（条件） |
| 28 | Bridge Data — Other Codes (`iCODETYPE`=1 时必填) | `"BRIDGE1"` | Object | - | Required（条件） |
| 29 | Bridge Data — TB 10002-2017 / Q·CR 9300-2018 (`iCODETYPE`=2 或 3 时必填) | `"BRIDGE2"` | Object | - | Required（条件） |

> ⚠️ **2026-08-25 确认：** `iCODETYPE`/`iNFM`/`iSLCM`/`iBC` 这 4 个字段在原文 Specifications
> 表中都有 enum 值列表，但此前文档却全部遗漏，Required 属性实际为（条件）
> Required，却被误记为 Optional。`BRIDGE2` 对象(TB 10002-2017/Q·CR 9300-2018
> 代码专用)则整个缺失，故在下方以独立表格新增（article id `35989644995609`）。

**FREQ 对象主要键**（按桥梁形式计算频率的参数）：

| Key | 说明 | Key | 说明 |
|-----|------|-----|------|
| `"USER_F"` | f [Hz] | `"SBEM_L"`/`"SBEM_E"`/`"SBEM_IC"`/`"SBEM_MC"` | 简支梁 L/E/Ic/mc |
| `"CBEM_A"`/`"CBEM_B"`/`"CBEM_L"`/`"CBEM_E"`/`"CBEM_IC"`/`"CBEM_MC"` | 连续梁 a/b/L/E/Ic/mc | `"iARCH_TYPE"` | 拱桥形式 |
| `"ARCH_N"`/`"ARCH_F"`/`"ARCH_L"`/`"ARCH_E"`/`"ARCH_IC"`/`"ARCH_MC"` | 拱桥 n/f/L/E/Ic/mc | `"CABL_A"`/`"CABL_L"` | 斜拉桥 a/L |
| `"SUSP_L"`/`"SUSP_E"`/`"SUSP_I"`/`"SUSP_HG"`/`"SUSP_M"` | 悬索桥 L/E/I/Hg/m | | |

**BRIDGE1 对象 — 按 `"BTYPE"`(Bridge Type: `"RC"` / `"STEEL"` / `"MBRG"`(Old Urban Bridge) /
`"TRAIN"`(Train·Subway)) 的各自字段：**

| Key | 说明 | Value Type |
| --- | --- | --- |
| `"RC_C1L1"`/`"RC_C1F1"`/`"RC_C1L2"`/`"RC_C1F2"` | RC — Case 1 L1/F1/L2/F2 | Number |
| `"RC_bCASE2"` | RC — 是否使用 Case 2 | Boolean (默认 false) |
| `"RC_C2L1"`/`"RC_C2F1"`/`"RC_C2L2"`/`"RC_C2F2"` | RC — Case 2 L1/F1/L2/F2 (`RC_bCASE2`=true 时) | Number |
| `"RC_GROUP"` | RC — 结构组名称 | String |
| `"STL_C1V1"`/`"STL_C1V2"` | Steel — Case 1 V1/V2 | Number |
| `"STL_bCASE2"` | Steel — 是否使用 Case 2 | Boolean (默认 false) |
| `"STL_C2V1"`/`"STL_C2V2"` | Steel — Case 2 V1/V2 (`STL_bCASE2`=true 时) | Number |
| `"STL_GROUP"` | Steel — 结构组名称 | String |
| `"MBRG_RL1"`/`"MBRG_RF1"`/`"MBRG_RL2"`/`"MBRG_RF2"`/`"MBRG_RF3"`/`"MBRG_RF4"` | Old Urban Bridge — 车道荷载冲击系数 L1/F1/L2/F2/F3/F4 | Number |
| `"MBRG_CF1"`/`"MBRG_CF2"`/`"MBRG_CF3"` | Old Urban Bridge — 车辆荷载冲击系数 F1/F2/F3 | Number |
| `"TRAIN_SUB_TYPE"` | Train — Sub-Type(`"SIMPLE"`/`"COMPOSITE"`/`"RCCONC"`/`"RCARCH"`) | String |
| `"TRAIN_NUMERATOR"`/`"TRAIN_DENOMINATOR"` | Train — Value 1 / Value 2 | Number |
| `"TRAIN_H"` | Train — Surcharge Thickness (`TRAIN_SUB_TYPE="RCCONC"` 专用) | Number |
| `"TRAIN_bCLSL"` | Train — Apply Loaded Span Length (`RCCONC` 专用，`0`=不考虑/`1`=考虑) | Integer |
| `"TRAIN_LAMBDA"`/`"TRAIN_F"` | Train — Lambda / f (`RCARCH` 专用) | Number |
| `"TRAIN_bALSL"` | Train — Apply Loaded Span Length (`RCARCH` 专用，`0`=不考虑/`1`=考虑) | Integer |
| `"TRAIN_GROUP"` | Train — 结构组名称 | String |

**BRIDGE2 对象**（`iCODETYPE`=2 TB 10002-2017 / 3 Q·CR 9300-2018 专用）— 按 `"BTYPE"`(Bridge Type:
`"RAILWAY"`(Passenger-Freight Mixed Line·Heavy Haul Railway Bridge) / `"RAILBRG"`(High Speed·
Intercity Railway Bridge) / `"RAILCUL"`(High Speed·Intercity Railway Culvert)) 的各自字段：

| Key | 说明 | Value Type |
| --- | --- | --- |
| `"METHOD"` | RAILWAY — Sub-Type(`"SIMPLE"`/`"COMPOSITE"`/`"RCCONC"`/`"RCARCH"`) | String |
| `"SIMPLE_U"`/`"SIMPLE_L"` | RAILWAY(`METHOD="SIMPLE"`) — Value 1/2 | Number |
| `"COMPO_U"`/`"COMPO_L"` | RAILWAY(`METHOD="COMPOSITE"`) — Value 1/2 | Number |
| `"CONC_U"`/`"CONC_L"`/`"CONC_H"` | RAILWAY(`METHOD="RCCONC"`) — Value 1/2, Surcharge Thickness | Number |
| `"ARCH_U"`/`"ARCH_L"`/`"ARCH_LAMBDA"`/`"ARCH_F"` | RAILWAY(`METHOD="RCARCH"`) — Value 1/2, Lambda, f | Number |
| `"bCHECK"` | RAILWAY(`RCCONC`/`RCARCH`) — 是否 Apply Loaded Span Length | Boolean (默认 false) |
| `"GROUP"` | RAILWAY(`RCCONC`/`RCARCH`) — 结构组名称 | String |
| `"MU1"`/`"MU2"`/`"MU3"` | RAILBRG·RAILCUL 共通 — 计算 mu 用的 Value 1/2/3 | Number |
| `"bLFAI"` | RAILBRG·RAILCUL 共通 — 是否 Apply Loaded Span Length | Boolean (默认 false) |
| `"LFAI"` | RAILBRG·RAILCUL 共通 — Lfai (`bLFAI`=false 时) | Number |
| `"bCHECK"` | RAILBRG 专用 — Apply Loaded Span Length (`bLFAI`=true 时) | Boolean (默认 false) |
| `"bLENGTH"` | RAILCUL 专用 — Apply Loaded Span Length (`bLFAI`=true 时) | Boolean (默认 false) |
| `"MUR1"`/`"MUR2"`/`"MUR3"` | RAILCUL 专用 — 计算 mu Reduction 用的 Value 1/2/3 | Number |
| `"HC"` | RAILCUL 专用 — Surcharge Thickness | Number |
| `"GROUP"` | RAILBRG·RAILCUL 共通 — 结构组名称 | String |

> `BRIDGE2.bCHECK`/`GROUP` 键由 RAILWAY 分支与 RAILBRG 分支共用名称(原文表中亦以
> 相同 Key 复用) — 须以 `BTYPE` 区分支后进行解析。

### Request Body（摘要示例）

```json
{
  "Assign": {
    "1": {
      "POINT": "INF",
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true, "bRG": false, "RGN": "",
      "bDISP": true, "bDG": false, "DGN": "",
      "bFM": true, "bFG": false, "FGN": "",
      "bL": true, "bLG": false, "LGN": "",
      "bIF": true,
      "iCODETYPE": 0,
      "iNFM": 0,
      "bBC": false,
      "FREQ": {
        "USER_F": 0,
        "SBEM_L": 30, "SBEM_E": 3.0e10, "SBEM_IC": 0.5, "SBEM_MC": 2500
      }
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

def set_moving_load_china():
    payload = {
        "Assign": {
            "1": {
                "POINT": "INF", "iIGP": 0, "UNUMT": 3,
                "PLATE": "NODAL", "bSTRCALC": True,
                "FRAME": "AXIAL", "bCSTRCALC": True,
                "bREAC": True, "bRG": False, "RGN": "",
                "bDISP": True, "bDG": False, "DGN": "",
                "bFM": True,  "bFG": False, "FGN": "",
                "bL": True,   "bLG": False, "LGN": "",
                "bIF": True,           # 使用冲击系数
                "iCODETYPE": 0,        # 代码类型
                "iNFM": 0,             # 固有频率计算法
                "bBC": False,          # 不使用车辆荷载等级
                "FREQ": {              # 简支梁频率数据
                    "USER_F": 0,
                    "SBEM_L": 30, "SBEM_E": 3.0e10,
                    "SBEM_IC": 0.5, "SBEM_MC": 2500
                }
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTch", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (China) set:", resp.json())

set_moving_load_china()
```

---

## 11. /db/MVCTid — Moving Load Analysis Control – India

印度代码(IRC/IRS)专用的移动荷载分析控制。包含冲击/CDA 计算用桥梁类型、铁路桥信息(轨道、枕木宽度、填料高度)等。计算过滤器组键使用 `*GP` 后缀。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTid` | 创建 |
| GET | `{base_url}/db/MVCTid` | 查询 |
| PUT | `{base_url}/db/MVCTid/{id}` | 修改 |
| DELETE | `{base_url}/db/MVCTid/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Influence Generating Points (0/1) | `"iIGP"` | Integer | 0 | Optional |
| 2 | Number/Line Element (when `iIGP`=0) | `"UNUMT"` | Integer | - | Required |
| 3 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 4 | Plate Options (`"CENTER"` / `"NODAL"`) | `"PLATE"` | String | - | Required |
| 5 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 6 | Frame Options (`"NORMAL"` / `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 7 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 8 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 9 | Reactions Option (All/Group) | `"bRGP"` | Boolean | false | Optional |
| 10 | Reactions Group Name | `"RGP"` | String | - | Required |
| 11 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 12 | Displacements Option (All/Group) | `"bDGP"` | Boolean | false | Optional |
| 13 | Displacements Group Name | `"DGP"` | String | - | Required |
| 14 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 15 | Forces/Moments Option (All/Group) | `"bFGP"` | Boolean | false | Optional |
| 16 | Forces/Moments Group Name | `"FGP"` | String | - | Required |
| 17 | Filter – Elastic/General Links | `"bL"` | Boolean | false | Optional |
| 18 | Links Option (All/Group) | `"bLG"` | Boolean | false | Optional |
| 19 | Links Group Name | `"LGP"` | String | - | Required |
| 20 | Bridge Type for Impact/CDA (Steel: 0 / RC: 1) | `"BRIDGE"` | Integer | 0 | Optional |
| 21 | Track (Single: 0 / Double: 1 / Multiple: 2) | `"TRACKS"` | Integer | 0 | Optional |
| 22 | Sleeper Width Type (Type1: 0 / Type2: 1 / User: 2) | `"WIDTHTYPE"` | Integer | 0 | Optional |
| 23 | Sleeper Width for User | `"WIDTH"` | Number | 0 | Optional |
| 24 | Depth of Fill | `"DEPTH"` | Number | 0 | Optional |
| 25 | Maximum Successive Vehicles | `"VHMAX"` | Integer | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true, "bRGP": false, "RGP": "",
      "bDISP": true, "bDGP": false, "DGP": "",
      "bFM": true, "bFGP": false, "FGP": "",
      "bL": true, "bLG": false, "LGP": "",
      "BRIDGE": 0,
      "TRACKS": 0,
      "WIDTHTYPE": 0,
      "WIDTH": 0,
      "DEPTH": 10,
      "VHMAX": 10
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

def set_moving_load_india():
    payload = {
        "Assign": {
            "1": {
                "iIGP": 0, "UNUMT": 3,
                "PLATE": "NODAL", "bSTRCALC": True,
                "FRAME": "AXIAL", "bCSTRCALC": True,
                "bREAC": True, "bRGP": False, "RGP": "",
                "bDISP": True, "bDGP": False, "DGP": "",
                "bFM": True,  "bFGP": False, "FGP": "",
                "bL": True,   "bLG": False, "LGP": "",
                "BRIDGE": 0,        # Steel bridge
                "TRACKS": 0,        # Single track
                "WIDTHTYPE": 0,     # Type 1
                "WIDTH": 0,
                "DEPTH": 10,        # 填料高度
                "VHMAX": 10         # 最大连续车辆数
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTid", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (India) set:", resp.json())

set_moving_load_india()
```

---

## 12. /db/MVCTbs — Moving Load Analysis Control – BS

英国代码(BS 5400 / BD 37/01 / CS 454)专用的移动荷载分析控制。额外指定标准车道(Notional Lanes)数量。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTbs` | 创建 |
| GET | `{base_url}/db/MVCTbs` | 查询 |
| PUT | `{base_url}/db/MVCTbs/{id}` | 修改 |
| DELETE | `{base_url}/db/MVCTbs/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Influence Generating Points (0/1) | `"iIGP"` | Integer | 0 | Optional |
| 2 | Number/Line Element (when `iIGP`=0) | `"UNUMT"` | Integer | - | Required |
| 3 | Distance between Points (when `iIGP`=1) | `"DIST"` | Number | - | Required |
| 4 | Plate Options (`"CENTER"` / `"NODAL"`) | `"PLATE"` | String | - | Required |
| 5 | Plate – Stress | `"bSTRCALC"` | Boolean | false | Optional |
| 6 | Plate – Concurrent Force | `"bCONCURRENT"` | Boolean | false | Optional |
| 7 | Frame Options (`"NORMAL"` / `"AXIAL"`) | `"FRAME"` | String | - | Required |
| 8 | Frame – Combined Stress | `"bCSTRCALC"` | Boolean | false | Optional |
| 9 | Filter – Reactions | `"bREAC"` | Boolean | false | Optional |
| 10 | Reactions Option (All/Group) | `"bRGP"` | Boolean | false | Optional |
| 11 | Reactions Group Name | `"RGP"` | String | - | Required |
| 12 | Filter – Displacements | `"bDISP"` | Boolean | false | Optional |
| 13 | Displacements Option (All/Group) | `"bDGP"` | Boolean | false | Optional |
| 14 | Displacements Group Name | `"DGP"` | String | - | Required |
| 15 | Filter – Forces/Moments | `"bFM"` | Boolean | false | Optional |
| 16 | Forces/Moments Option (All/Group) | `"bFGP"` | Boolean | false | Optional |
| 17 | Forces/Moments Group Name | `"FGP"` | String | - | Required |
| 18 | Filter – Elastic/General Links | `"bL"` | Boolean | false | Optional |
| 19 | Links Option (All/Group) | `"bLG"` | Boolean | false | Optional |
| 20 | Links Group Name | `"LGP"` | String | - | Required |
| 21 | N for HA Lane Factor (BD/37/01) or ALL Model 2 (CS 454) — N < 6: 0 / N ≥ 6: 1 | `"NUMLANE"` | Integer | 0 | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "bCONCURRENT": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true, "bRGP": false, "RGP": "",
      "bDISP": true, "bDGP": false, "DGP": "",
      "bFM": true, "bFGP": false, "FGP": "",
      "bL": true, "bLG": false, "LGP": "",
      "NUMLANE": 0
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

def set_moving_load_bs():
    payload = {
        "Assign": {
            "1": {
                "iIGP": 0, "UNUMT": 3,
                "PLATE": "NODAL", "bSTRCALC": True, "bCONCURRENT": True,
                "FRAME": "AXIAL", "bCSTRCALC": True,
                "bREAC": True, "bRGP": False, "RGP": "",
                "bDISP": True, "bDGP": False, "DGP": "",
                "bFM": True,  "bFGP": False, "FGP": "",
                "bL": True,   "bLG": False, "LGP": "",
                "NUMLANE": 0     # N < 6
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTbs", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (BS) set:", resp.json())

set_moving_load_bs()
```

---

## 13. /db/MVCTtr — Moving Load Analysis Control – Transverse

横向(Transverse)移动荷载分析控制。设置单位荷载数、分析结果类型、结果选项(组合应力/反力/位移/构件内力)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/MVCTtr` | 创建 |
| GET | `{base_url}/db/MVCTtr` | 查询 |
| PUT | `{base_url}/db/MVCTtr/{id}` | 修改 |
| DELETE | `{base_url}/db/MVCTtr/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Point Selection (Influence Line Dependent: 1 / All Point: 2) | `"LOAD_POINT_SEL"` | Integer | - | Required |
| 2 | Influence Generation Method (Number/Line: 0 / Distance: 1) | `"INFL_GEN_POINT"` | Integer | 0 | Optional |
| 3 | Number/Line Element (when method 0) | `"NUM_UNIT_LOAD"` | Integer | - | Required |
| 4 | Distance between Points (when method 1) | `"DISTANCE"` | Number | - | Required |
| 5 | Analysis Results Type (Normal: 1 / Normal+Concurrent Force/Stress: 2) | `"ANALYSIS_RESULT"` | Integer | - | Required |
| 6 | Combined Stress | `"OPT_COMBINED_STR"` | Boolean | false | Optional |
| 7 | Reactions | `"OPT_REACTIONS"` | Boolean | false | Optional |
| 8 | Displacement | `"OPT_DISPLACEMENTS"` | Boolean | false | Optional |
| 9 | Forces/Moments | `"OPT_FORCE"` | Boolean | false | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "LOAD_POINT_SEL": 1,
      "INFL_GEN_POINT": 0,
      "NUM_UNIT_LOAD": 3,
      "ANALYSIS_RESULT": 2,
      "OPT_COMBINED_STR": true,
      "OPT_REACTIONS": true,
      "OPT_DISPLACEMENTS": true,
      "OPT_FORCE": false
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

def set_moving_load_transverse():
    payload = {
        "Assign": {
            "1": {
                "LOAD_POINT_SEL": 1,       # 影响线从属点
                "INFL_GEN_POINT": 0,       # Number/Line Element
                "NUM_UNIT_LOAD": 3,        # 单位荷载分割数
                "ANALYSIS_RESULT": 2,      # Normal + 同时力/应力
                "OPT_COMBINED_STR": True,  # 组合应力
                "OPT_REACTIONS": True,     # 反力
                "OPT_DISPLACEMENTS": True, # 位移
                "OPT_FORCE": False         # 构件内力/弯矩
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/MVCTtr", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Moving Load Control (Transverse) set:", resp.json())

set_moving_load_transverse()
```

---

## 14. /db/SMCT — Settlement Analysis Control Data

定义沉降(Settlement)分析控制数据。设置板/连接单元的同时力(Concurrent Force)计算是否启用。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/SMCT` | 创建 |
| GET | `{base_url}/db/SMCT` | 查询 |
| PUT | `{base_url}/db/SMCT/{id}` | 修改 |
| DELETE | `{base_url}/db/SMCT/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Plate Concurrent Force (Active: true / Inactive: false) | `"CONCURRENT_CALC"` | Boolean | false | Optional |
| 2 | Elastic / General Links Concurrent Force (Active: true / Inactive: false) | `"CONCURRENT_LINK"` | Boolean | false | Optional |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "CONCURRENT_CALC": true,
      "CONCURRENT_LINK": false
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

def set_settlement_control():
    payload = {
        "Assign": {
            "1": {
                "CONCURRENT_CALC": True,   # 板单元同时力计算
                "CONCURRENT_LINK": False   # 连接单元同时力计算
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/SMCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Settlement Control set:", resp.json())

set_settlement_control()
```

---

## 15. /db/NLCT — Nonlinear Analysis Control Data

定义非线性(Nonlinear)分析控制数据。依非线性类型、迭代法(Newton-Raphson/Arc-Length/Displacement-Control)，使用按荷载工况的控制项(`NEWTON_ITEMS`/`ARCLEN_ITEMS`/`DISPCT_ITEMS`)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/NLCT` | 创建 |
| GET | `{base_url}/db/NLCT` | 查询 |
| PUT | `{base_url}/db/NLCT/{id}` | 修改 |
| DELETE | `{base_url}/db/NLCT/{id}` | 删除 |

### Parameters — 通用

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Nonlinear Type (Geometry: `"GEOM"` / Material: `"MATL"` / Both: `"GEOM+MATL"`) | `"NONLINEAR_TYPE"` | String | "GEOM" | Optional |
| 2 | Iteration Method (Newton-Raphson: `"NEWTON"` / Arc-Length: `"ARC"` / Displacement-Control: `"DISP"`) | `"ITERATION_METHOD"` | String | "NEWTON" | Optional |
| 3 | Energy Norm 使用 | `"OPT_ENERGY_NORM"` | Boolean | false | Optional |
| 4 | Energy Norm | `"ENERGY_NORM"` | Number | - | Required |
| 5 | Displacement Norm 使用 | `"OPT_DISPLACEMENT_NORM"` | Boolean | false | Optional |
| 6 | Displacement Norm | `"DISPLACEMENT_NORM"` | Number | - | Required |
| 7 | Force Norm 使用 | `"OPT_FORCE_NORM"` | Boolean | false | Optional |
| 8 | Force Norm | `"FORCE_NORM"` | Number | - | Required |

### Parameters — Newton-Raphson (`ITERATION_METHOD = "NEWTON"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 9 | Number of Load Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| 10 | Maximum Number of Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| 11 | Load Case Specific Data | `"NEWTON_ITEMS"` | Array [Object] | - | Required |
| (1) | Iteration Method (`"NEWTON"`) | `"ITERATION_METHOD"` | String | "NEWTON" | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Number of Load Steps | `"NUMBER_STEPS"` | Number | - | Required |
| (4) | Max Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| (5) | Load Factor (Index: Step) | `"LOAD_FACTORS"` | Array [Number] | 1 | Optional |

### Parameters — Arc-Length (`ITERATION_METHOD = "ARC"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 9 | Number of Load Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| 10 | Maximum Number of Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| 11 | Initial Force Ratio for Unit Arc-Length | `"INITIAL_FORCE_RATIO_ARC_LEN"` | Number | - | Required |
| 12 | Maximum Displacement Bound | `"MAXIMUM_DISPLACEMENT"` | Number | 0 | Optional |
| 13 | Load Case Specific Data | `"ARCLEN_ITEMS"` | Array [Object] | - | Required |
| (1) | Iteration Method (`"ARC"`) | `"ITERATION_METHOD"` | String | "ARC" | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Initial Force Ratio for Unit Arc-Length | `"INITIAL_FORCE_RATIO_ARC_LEN"` | Number | - | Required |
| (4) | Number of Steps | `"NUMBER_STEPS"` | Number | - | Required |
| (5) | Max Iterations/Increment Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| (6) | Maximum Displacement | `"MAXIMUM_DISPLACEMENT"` | Number | 0 | Optional |

> ⚠️ **2026-08-25 确认：** `MAXIMUM_DISPLACEMENT`(上方 12 项、`ARCLEN_ITEMS`(6) 两处)在原文
> Specifications 表与示例中默认值均为 `0`/Optional，此前却被误记为 Required
> （article id `35990229420441`）。

### Parameters — Displacement-Control (`ITERATION_METHOD = "DISP"`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 9 | Number of Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| 10 | Max Iterations/Load Step | `"MAX_ITERATIONS"` | Integer | - | Required |
| 11 | Master Node ID | `"MASTER_NODE"` | Integer | - | Required |
| 12 | Direction (Dx: 0 / Dy: 1 / Dz: 2) | `"DIRECTION"` | Integer | 0 | Optional |
| 13 | Maximum Displacement | `"MAXIMUM_DISPLACEMENT"` | Number | - | Required |
| 14 | Load Case Specific Data | `"DISPCT_ITEMS"` | Array [Object] | - | Required |
| (1) | Iteration Method (`"DISP"`) | `"ITERATION_METHOD"` | String | "DISP" | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Number of Steps | `"NUMBER_STEPS"` | Integer | - | Required |
| (4) | Max Iterations/Load Step | `"MAX_ITERATIONS"` | Number | - | Required |
| (5) | Master Node ID | `"MASTER_NODE"` | Integer | - | Required |
| (6) | Direction (Dx: 0 / Dy: 1 / Dz: 2) | `"DIRECTION"` | Integer | 0 | Optional |
| (7) | Maximum Displacement | `"MAXIMUM_DISPLACEMENT"` | Number | - | Required |
| (8) | Master Node Displacement (Index: Step) | `"LOAD_FACTORS"` | Array [Number] | 1 | Optional |

### Request Body — Newton-Raphson

```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "NEWTON",
      "NUMBER_STEPS": 1,
      "MAX_ITERATIONS": 30,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "NEWTON_ITEMS": [
        {
          "ITERATION_METHOD": "NEWTON",
          "LCNAME": "A",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 30,
          "LOAD_FACTORS": [1]
        }
      ],
      "DISPCT_ITEMS": [
        {
          "ITERATION_METHOD": "DISP",
          "LCNAME": "B",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 10,
          "MASTER_NODE": 1,
          "DIRECTION": 0,
          "MAXIMUM_DISPLACEMENT": 0.1,
          "LOAD_FACTORS": [1]
        }
      ]
    }
  }
}
```

### Request Body — Arc-Length

```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "ARC",
      "NUMBER_STEPS": 100,
      "MAX_ITERATIONS": 10,
      "INITIAL_FORCE_RATIO_ARC_LEN": 5,
      "MAXIMUM_DISPLACEMENT": 0,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "ARCLEN_ITEMS": [
        {
          "ITERATION_METHOD": "ARC",
          "LCNAME": "A",
          "INITIAL_FORCE_RATIO_ARC_LEN": 5,
          "NUMBER_STEPS": 100,
          "MAX_ITERATIONS": 10,
          "MAXIMUM_DISPLACEMENT": 1
        }
      ]
    }
  }
}
```

### Request Body — Displacement-Control

```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "DISP",
      "NUMBER_STEPS": 1,
      "MAX_ITERATIONS": 10,
      "MASTER_NODE": 1,
      "DIRECTION": 0,
      "MAXIMUM_DISPLACEMENT": 0.1,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "DISPCT_ITEMS": [
        {
          "ITERATION_METHOD": "DISP",
          "LCNAME": "B",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 10,
          "MASTER_NODE": 1,
          "DIRECTION": 0,
          "MAXIMUM_DISPLACEMENT": 0.1,
          "LOAD_FACTORS": [1]
        }
      ]
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

def set_nonlinear_control_newton():
    payload = {
        "Assign": {
            "1": {
                "NONLINEAR_TYPE": "GEOM+MATL",     # 几何+材料非线性
                "ITERATION_METHOD": "NEWTON",      # Newton-Raphson
                "NUMBER_STEPS": 1,
                "MAX_ITERATIONS": 30,
                "OPT_ENERGY_NORM": True,  "ENERGY_NORM": 0.001,
                "OPT_DISPLACEMENT_NORM": True, "DISPLACEMENT_NORM": 0.001,
                "OPT_FORCE_NORM": True,   "FORCE_NORM": 0.001,
                "NEWTON_ITEMS": [
                    {
                        "ITERATION_METHOD": "NEWTON",
                        "LCNAME": "PUSH",
                        "NUMBER_STEPS": 10,
                        "MAX_ITERATIONS": 30,
                        "LOAD_FACTORS": [0.1, 0.2, 0.3, 0.4, 0.5,
                                         0.6, 0.7, 0.8, 0.9, 1.0]
                    }
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/NLCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Nonlinear Control (Newton-Raphson) set:", resp.json())

set_nonlinear_control_newton()
```

---

## 16. /db/NLCT-M1 — Nonlinear Analysis Control (Hyper-S)

用于 Hyper-S(MEC) 求解器的非线性分析控制。以 `LC_SCOPE` 指定适用范围，`LOAD_STEPS`(步模式/输出)与 `CONV_CRITERIA`(收敛准则)以嵌套对象使用。迭代法支持 Force Control(`FORCE`)、Arc Length(`ARC`)、Displacement Control(`DISP`)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| GET | `{base_url}/db/NLCT-M1` | 查询 |
| PUT | `{base_url}/db/NLCT-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/NLCT-M1/{id}` | 删除 |

### Parameters — 通用

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Load Case Scope (整体: `"ALL"` / 选择: `"SELECT"`, 默认 `"ALL"`) | `"LC_SCOPE"` | String (enum) | "ALL" | Optional |
| 6 | Load Case Name (`LC_SCOPE="SELECT"` 新建时必填。修改已有项时若未指定则保留原值) | `"LOAD_CASE"` | String | - | Required（条件） |
| 2 | Nonlinear Type (`"GEOM"` / `"MATL"` / `"GEOM_MATL"`) | `"NONLINEAR_TYPE"` | String (enum) | - | Required |
| 3 | Iteration Method (Force: `"FORCE"` / Arc Length: `"ARC"` / Displacement: `"DISP"`) | `"ITER_METHOD"` | String (enum) | - | Required |
| 4 | Load Steps 设置 | `"LOAD_STEPS"` | Object | - | Required |
| 5 | Convergence Criteria | `"CONV_CRITERIA"` | Object | - | Required |
| 7 | 高级设置 (未指定时应用服务器默认值) | `"ADVANCED"` | Object | - | Optional |

> ⚠️ **2026-08-25 确认：** `LOAD_CASE`(6 项)在此前文档中完全没有 — 它是按 `LC_SCOPE="SELECT"`
> 新建条目时必填的字段。`ADVANCED`(7 项)对象也整个缺失（article id
> `56506850582425`）。原文 JSON Schema 中附有异常详细的实现注释，即以其
> 为依据予以反映。

### Parameters — LOAD_STEPS 对象（随 `ITER_METHOD` 不同，所用字段也不同）

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"STEP_MODE"` | String (enum: `"AUTO"`/`"MANUAL"`) | - | 步模式 (Required)。`ITER_METHOD="ARC"` 时在 UI 上固定为 `"AUTO"` |
| `"NUMBER_STEPS"` | Integer (≥1) | 1 | 步数 (`STEP_MODE="AUTO"` 时必填) |
| `"OUTPUT"` | String (enum: `"EVERY"`/`"LAST"`) | "EVERY" | 中间输出 (`STEP_MODE="AUTO"` 时必填) |
| `"MANUAL_STEPS"` | Array [Number] (≥1个) | - | 用户自定义步列表 (`STEP_MODE="MANUAL"` 时) |
| `"MIN_ARC_RATIO"` | Number (>0) | 0.25 | (`ITER_METHOD="ARC"`) 最小弧长调整比例 |
| `"MAX_ARC_RATIO"` | Number (>0) | 4.0 | (`ITER_METHOD="ARC"`) 最大弧长调整比例 |
| `"MAX_ARC_INCREMENTS"` | Integer (≥1) | 100 | (`ITER_METHOD="ARC"`) 最大弧长增量数 |
| `"MASTER_NODE"` | Integer | 0 | (`ITER_METHOD="DISP"`) 主节点 ID |
| `"MAX_DISP"` | Number (禁止 0) | - | (`ITER_METHOD="DISP"`) 最大位移 — 若由服务器填 0 则校验失败，故必须给出显式值 |
| `"DIRECTION"` | String (enum: `"DX"`/`"DY"`/`"DZ"`) | "DX" | (`ITER_METHOD="DISP"`) 方向 |
| `"REF_NODE"` | Object | - | (`ITER_METHOD="DISP"`) 基准(相对)节点 — 下级 `OPT_USE`(Boolean, Required)/`NODE`(Integer, `OPT_USE=false` 时默认 0) |

### Parameters — CONV_CRITERIA 对象

分别对应 `DISP`(位移) / `LOAD`(荷载) / `WORK`(功) — 至少 1 个 `OPT_USE=true`:

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"OPT_USE"` | Boolean | - | 是否使用该项准则 (Required) |
| `"VALUE"` | Number (大于 0 小于 1) | 0.001 | 容差 (`OPT_USE=true` 时必填) |

### Parameters — ADVANCED 对象（高级非线性设置，全部 Optional — 未指定时使用服务器默认值）

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"OPT_USE_DEFAULT"` | Boolean | - | 是否使用默认设置 (Required — 为 true 时以下字段均可不指定) |
| `"STIFF_UPDATE_SCHEME"` | String (enum: `"CUSTOM"`/`"FULL_NEWTON_RAPHSON"`/`"INITIAL_STIFF"`) | - | 刚度更新方式 |
| `"ITER_BEFORE_STIFF_UPDATE"` | Integer | - | 刚度更新前的迭代次数 (非 `CUSTOM` 时按各方式应用服务器自动值) |
| `"OPT_TERMINATE_ON_FAILED_CONV"` | Boolean | false | 收敛失败时是否终止分析 |
| `"MAX_ITER_PER_INCREMENT"` | Integer | 50 | 每增量最大迭代次数 |
| `"MAX_BISECTION_LEVEL"` | Integer (0~20) | 5 | 最大二分(Bisection)层级 |
| `"OPT_SMART_BISECTION"` | Boolean | false | 是否使用 Smart Bisection |
| `"DIVERGENCE_THRESHOLD"` | Number | 3 | 发散判定阈值 |
| `"OPT_ENABLE_LINE_SEARCH"` | Boolean | true | 是否使用 Line Search |
| `"LINE_SEARCH_OPTION"` | String (enum: `"AUTO"`/`"MANUAL"`) | - | Line Search 方式 |
| `"MAX_LINE_SEARCH_PER_ITER"` | Integer | 4 | 每次迭代最大 Line Search 次数 |
| `"LINE_SEARCH_TOL"` | Number | 0.5 | Line Search 容差 |

### Request Body — Force Control

```json
{
  "Assign": {
    "1": {
      "LC_SCOPE": "ALL",
      "NONLINEAR_TYPE": "GEOM",
      "ITER_METHOD": "FORCE",
      "LOAD_STEPS": {
        "STEP_MODE": "AUTO",
        "NUMBER_STEPS": 10,
        "OUTPUT": "EVERY"
      },
      "CONV_CRITERIA": {
        "DISP": { "OPT_USE": true, "VALUE": 0.001 }
      }
    }
  }
}
```

### Request Body — Arc Length

```json
{
  "Assign": {
    "1": {
      "LC_SCOPE": "ALL",
      "NONLINEAR_TYPE": "GEOM_MATL",
      "ITER_METHOD": "ARC",
      "LOAD_STEPS": {
        "STEP_MODE": "AUTO",
        "NUMBER_STEPS": 20,
        "OUTPUT": "LAST",
        "MIN_ARC_RATIO": 0.25,
        "MAX_ARC_RATIO": 4,
        "MAX_ARC_INCREMENTS": 100
      },
      "CONV_CRITERIA": {
        "DISP": { "OPT_USE": true, "VALUE": 0.001 },
        "LOAD": { "OPT_USE": true, "VALUE": 0.001 }
      }
    }
  }
}
```

### Request Body — Displacement Control

```json
{
  "Assign": {
    "1": {
      "LC_SCOPE": "ALL",
      "NONLINEAR_TYPE": "MATL",
      "ITER_METHOD": "DISP",
      "LOAD_STEPS": {
        "STEP_MODE": "AUTO",
        "NUMBER_STEPS": 15,
        "OUTPUT": "EVERY",
        "MASTER_NODE": 101,
        "MAX_DISP": 0.05,
        "DIRECTION": "DX",
        "REF_NODE": { "OPT_USE": false }
      },
      "CONV_CRITERIA": {
        "WORK": { "OPT_USE": true, "VALUE": 0.001 }
      }
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

def update_nonlinear_control_m1_arc():
    payload = {
        "Assign": {
            "1": {
                "LC_SCOPE": "ALL",
                "NONLINEAR_TYPE": "GEOM_MATL",
                "ITER_METHOD": "ARC",           # Arc Length 方式
                "LOAD_STEPS": {
                    "STEP_MODE": "AUTO",
                    "NUMBER_STEPS": 20,
                    "OUTPUT": "LAST",
                    "MIN_ARC_RATIO": 0.25,
                    "MAX_ARC_RATIO": 4,
                    "MAX_ARC_INCREMENTS": 100
                },
                "CONV_CRITERIA": {
                    "DISP": {"OPT_USE": True, "VALUE": 0.001},
                    "LOAD": {"OPT_USE": True, "VALUE": 0.001}
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/NLCT-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Nonlinear Control (Hyper-S, Arc) updated:", resp.json())

update_nonlinear_control_m1_arc()
```

---

## 17. /db/STCT — Construction Stage Analysis Control Data

定义施工阶段(Construction Stage)分析控制数据。所用参数随分析类型(`iINC_NLA`: 线性/非线性/材料非线性)与阶段选项(`iNLA_TYPE`: 独立/累加)而不同。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/STCT` | 创建 |
| GET | `{base_url}/db/STCT` | 查询 |
| PUT | `{base_url}/db/STCT/{id}` | 修改 |
| DELETE | `{base_url}/db/STCT/{id}` | 删除 |

### Parameters — 通用 / 核心

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage Option (Last: true / Other: false) | `"bLAST_FINAL"` | Boolean | false | Optional |
| 2 | Construction Stage Name (when `bLAST_FINAL` false) | `"FINAL_STAGE"` | String | - | Required |
| 3 | Analysis Type (Linear: 0 / Nonlinear ¹⁾: 1 / Material Nonlinear ¹⁾: 2) | `"iINC_NLA"` | Integer | 0 | Optional |
| 4 | Stage Option (Independent: 0 / Accumulative: 1) | `"iNLA_TYPE"` | Integer | 0 | Optional |

> **¹⁾** 非线性/材料非线性分析为 MIDAS Civil NX 专用。

### Parameters — Erection Load (C.S. 输出用临时荷载区分)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 6 | Erection Load for Construction Stage | `"vEREC"` | Array [Object] | Empty | Optional |
| (1) | Erection Load Case Name | `"LTYPECC"` | String | - | Required |
| (2) | Load Type for C.S ⁴⁾ | `"EREC"` | String | - | Required |
| (3) | Load Case Name List | `"vLCNAME"` | Array [String] | - | Required |
| 8 | Secondary Dead Load Effect for Grid Model (MIDAS Civil NX JP 版本专用) | `"bSDLE"` | Boolean | false | Optional |
| 9 | Load Case Name List (Grid Analysis Load, JP 版本专用) | `"vSDLE"` | Array [String] | - | Required |

> **⁴⁾ `EREC` 值列表** (Erection Load Type for C.S.): Dead Load: `"D"` / Dead Load of Component
> and Attachments: `"DC"` / Dead Load of Wearing Surfaces and Utilities: `"DW"` / Earth Pressure:
> `"EP"` / Live Load: `"L"` / Wind Load on Structure: `"W"` / Temperature: `"T"` / Temperature
> Gradient: `"TPG"` / Earthquake: `"E"` / Erection Load: `"ER"`.
>
> ⚠️ **2026-08-25 确认：** `bSDLE`/`vSDLE`(9 项)与 `EREC` 的值列表(脚注 ⁴⁾)在此前文档中并不存在
> — `bSDLE`/`vSDLE` 在 STCT-M1 一节中已有，但在 STCT 本节中缺失（article id
> `35990281053465`）。

### Parameters — Cable-Pretension / Initial Force Control

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 7 | Cable-Pretension Force Type (Internal: `"INTERNAL"` / External: `"EXTERNAL"`) | `"CPFC"` | String | "INTERNAL" | Optional |
| - | External Force Type (是否替换) | `"bEXT_REPL"` | Boolean | false | Optional |
| 8 | Convert Final Stage Member Forces to Initial Forces for Post C.S | `"bCONV"` | Boolean | false | Optional |
| 9 | Truss (when `bCONV` true) | `"bTRUSS"` | Boolean | false | Optional |
| 10 | Beam (when `bCONV` true) | `"bBEAM"` | Boolean | false | Optional |
| 11 | Change Cable Element to Equivalent Truss for Post C.S. | `"bCHANGE_CABLE"` | Boolean | false | Optional |
| 12 | Apply Initial Member Force to C.S | `"bAPPLY_IMF"` | Boolean | false | Optional |

### Parameters — Initial Displacement / Camber / 其他

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| - | Initial Tangent Displacement 使用 | `"bITD"` | Boolean | false | Optional |
| - | Initial Tangent Displacement Type (All: `"ALL"` / Structure Group: `"GROUP"`) | `"ITD"` | String | "ALL" | Optional |
| - | Structure Group Name (`ITD`="GROUP" 时) | `"GROUP"` | String | - | Required（条件） |
| - | Lack-of-Fit Force Control 使用 | `"bLFFC"` | Boolean | false | Optional |
| - | Lack-of-Fit Group Name (`bLFFC`=true 时) | `"LFFGR"` | String | - | Required（条件） |
| - | Apply Camber Displacement to C.S. | `"bCAMBER"` | Boolean | false | Optional |
| - | Calculate Concurrent Forces of Frame | `"bCALC_CFF"` | Boolean | false | Optional |
| - | Calculate Output of Each Part of Composite Section | `"bCALC_CSP"` | Boolean | false | Optional |
| - | Self-constrained Forces & Stresses | `"bSELFCONS"` | Boolean | false | Optional |
| - | Save Output of Construction Stage | `"bSAVE_OCS"` | Boolean | false | Optional |
| - | Stress Decrease 使用 / 选项 / 常数 | `"bSD"` / `"iSDOPT"` / `"SDCONST"` | Boolean / Integer / Number | - | Optional |
| - | Beam Section Property Option (Constant: 0 / Change with Tendon: 1) | `"iBSC"` | Integer | 0 | Optional |

> ⚠️ **2026-08-25 确认：** `iBSC` 在此前文档中被误标为 "Bi-Section Control"(二分法迭代控制)，
> 但原文表为 "Beam Section Property Option"(梁截面物性变更方式，
> 0=Constant/1=Change with Tendon)，是完全不同的概念 — 二分法相关控制由另外的
> `BSSTEP`/`ADSTEP`(下方 Nonlinear Analysis 一节)承担。`ITD` 默认值亦由 `-`→`"ALL"`、
> `GROUP`/`LFFGR` 分别更正为条件 Required（article id `35990281053465`）。

### Parameters — Linear & Independent Stage

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Include P-Delta Effect ²⁾ | `"bINC_PDL"` | Boolean | false | Optional |
| - | Number of Iterations | `"iITER"` | Integer | - | Optional |
| - | Convergence Tolerance | `"TOL"` | Number | - | Optional |

### Parameters — Nonlinear Analysis (`iINC_NLA` = 1 或 2)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| - | Number of Load Steps | `"iLSTEP"` | Integer | - | Optional |
| - | Maximum Number of Iterations | `"iMAXITER"` | Integer | - | Optional |
| - | Convergence Failure 使用 | `"CF"` | Boolean | false | Optional |
| - | Max Bi-Section Level for a Load Step | `"BSSTEP"` | Integer | - | Optional |
| - | Max Allowable Diverged Steps | `"ADSTEP"` | Integer | - | Optional |
| - | Energy Norm 使用 / 值 | `"bENEG"` / `"EV"` | Boolean / Number | - | Optional |
| - | Displacement Norm 使用 / 值 | `"bDISP"` / `"DV"` | Boolean / Number | - | Optional |
| - | Force Norm 使用 / 值 | `"bFORC"` / `"FV"` | Boolean / Number | - | Optional |
| - | Include Equilibrium Element Nodal Forces | `"bIEMF"` | Boolean | false | Optional |

### Parameters — Time Dependent Effect (累加阶段，`iNLA_TYPE` = 1)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| - | Include Time Dependent Effect | `"bINC_TDE"` | Boolean | false | Optional |
| - | Creep & Shrinkage 使用 | `"bCNS"` | Boolean | false | Optional |
| - | Creep & Shrinkage Type (`"CREEP"`/`"SHRINK"`/`"BOTH"`) | `"TYPE"` | String | - | Optional |
| - | Number of Creep Iterations | `"iITER_CR"` | Integer | - | Optional |
| - | Creep Tolerance | `"TOL_CR"` | Number | 0 | Optional |
| - | Only User's Creep Coefficient | `"bOUCC"` | Boolean | false | Optional |
| - | Internal Time Step for Creep 使用 | `"bITS"` | Boolean | false | Optional |
| - | Internal Time Step for Creep 值 | `"iITS"` | Integer | - | Required |
| - | Auto Time Step Generation for Large Time Gap | `"bATS"` | Boolean | false | Optional |
| - | Time Gap Steps (T>10 / >100 / >1000 / >5000 / >10000) | `"iT10"` / `"iT100"` / `"iT1K"` / `"iT5K"` / `"iT10K"` | Integer | - | Optional |
| - | Tendon Tension Loss Effect (Creep&Shrinkage) | `"bTTLE_CS"` | Boolean | false | Optional |
| - | Consider Re-bar Confinement Effect | `"bRCE"` | Boolean | false | Optional |
| - | Variation of Comp. Strength | `"bVAR"` | Boolean | false | Optional |
| - | Tendon Tension Loss Effect (Elastic Shortening) 使用 / 类型 | `"bTTLE_ES"` / `"iTTLE_ES"` | Boolean / Integer | - | Optional |
| - | Apply Time Dependent Elastic Modulus to Post C.S | `"bAPPLY_ELA"` | Boolean | false | Optional |

> ⚠️ **2026-08-25 确认：** `TOL_CR` 默认值 `-`→`0`；`iITS` 在原文表中以与 `bITS` 分离的独立
> 行标注为 Required(此前将 `bITS`/`iITS` 合为一行，误记为 `-`/Optional)，故更正
> （article id `35990281053465`）。

### Request Body — Linear Analysis and Independent Stage

```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": false,
      "FINAL_STAGE": "CS1",
      "iINC_NLA": 0,
      "iNLA_TYPE": 0,
      "bINC_PDL": true,
      "iITER": 30,
      "TOL": 0.01,
      "vEREC": [
        { "LTYPECC": "Erection Load 1", "EREC": "D", "vLCNAME": ["A", "B"] },
        { "LTYPECC": "Erection Load 2", "EREC": "DC", "vLCNAME": ["C"] }
      ],
      "CPFC": "EXTERNAL",
      "bCONV": true,
      "bTRUSS": true,
      "bBEAM": true,
      "bCHANGE_CABLE": true,
      "bAPPLY_IMF": true,
      "bCAMBER": true,
      "bSD": true,
      "iSDOPT": 1,
      "SDCONST": 1,
      "iBSC": 0
    }
  }
}
```

### Request Body — Nonlinear Analysis and Accumulative Stage

```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": false,
      "FINAL_STAGE": "CS1",
      "iINC_NLA": 1,
      "iNLA_TYPE": 1,
      "iLSTEP": 1,
      "iMAXITER": 30,
      "CF": false,
      "BSSTEP": 5,
      "ADSTEP": 3,
      "bENEG": false, "EV": 0.01,
      "bDISP": true, "DV": 0.01,
      "bFORC": false, "FV": 0.01,
      "bINC_TDE": true,
      "bCNS": true,
      "TYPE": "BOTH",
      "iITER_CR": 5,
      "TOL_CR": 0.01,
      "bTTLE_CS": true,
      "bRCE": false,
      "bVAR": true,
      "bTTLE_ES": true,
      "iTTLE_ES": 0,
      "bAPPLY_ELA": false,
      "bOUCC": false,
      "bITS": false,
      "iITS": 2,
      "bATS": true,
      "iT10": 2, "iT100": 5, "iT1K": 7, "iT5K": 10, "iT10K": 20,
      "CPFC": "EXTERNAL",
      "bEXT_REPL": true,
      "bCONV": true,
      "bTRUSS": true,
      "bBEAM": true,
      "bCHANGE_CABLE": true,
      "bITD": true,
      "ITD": "GROUP",
      "GROUP": "Strt Group 1",
      "bLFFC": true,
      "LFFGR": "Strt Group 1",
      "bCAMBER": true,
      "iBSC": 1,
      "bCALC_CFF": true,
      "bCALC_CSP": true,
      "bSELFCONS": true,
      "bSAVE_OCS": false
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

def set_construction_stage_control():
    payload = {
        "Assign": {
            "1": {
                "bLAST_FINAL": False,
                "FINAL_STAGE": "CS1",   # 目标施工阶段
                "iINC_NLA": 0,          # 线性分析
                "iNLA_TYPE": 1,         # 累加阶段 (考虑时间相关效应)
                "bINC_PDL": True,
                "iITER": 30,
                "TOL": 0.01,
                "bINC_TDE": True,       # 包含时间相关效应
                "bCNS": True,           # 徐变 & 干燥收缩
                "TYPE": "BOTH",
                "iITER_CR": 5,
                "TOL_CR": 0.01,
                "CPFC": "EXTERNAL",     # 拉索预张力：外力
                "bCONV": True, "bTRUSS": True, "bBEAM": True,
                "bCHANGE_CABLE": True,
                "bCAMBER": True
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/STCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Construction Stage Control set:", resp.json())

set_construction_stage_control()
```

---

## 18. /db/STCT-M1 — Construction Stage Analysis Control Data (Hyper-S)

用于 Hyper-S(MEC) 求解器的施工阶段分析控制。按功能重构为嵌套对象(`ANAL_TYPE`、`RESTART_CS_ANAL`、`ERECTION_LOAD`、`TIME_DEP_CONTROL`、`CABLE_CONTROL`、`INITIAL_CONTROL`、`INITIAL_DISP`、`STRESS_DECREASE`)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| GET | `{base_url}/db/STCT-M1` | 查询 |
| PUT | `{base_url}/db/STCT-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/STCT-M1/{id}` | 删除 |

### Parameters — 最上层

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Final Stage Option (Last: true / Other: false) | `"bLAST_FINAL"` | Boolean | - | Optional |
| 2 | Analysis Type 设置 | `"ANAL_TYPE"` | Object | - | Required |
| 3 | Restart C.S. Analysis 设置 | `"RESTART_CS_ANAL"` | Object | - | Optional |
| 4 | Erection Load 列表 | `"ERECTION_LOAD"` | Array [Object] | - | Optional |
| 5 | Self-weight Dead Load for Erection 使用 / 列表 | `"bSDLE"` / `"vSDLE"` | Boolean / Array [String] | - | Optional |
| 6 | Time Dependent Control | `"TIME_DEP_CONTROL"` | Object | - | Optional |
| 7 | Cable Control | `"CABLE_CONTROL"` | Object | - | Optional |
| 8 | Initial Force Control | `"INITIAL_CONTROL"` | Object | - | Optional |
| 9 | Initial Displacement Control | `"INITIAL_DISP"` | Object | - | Optional |
| 10 | Stress Decrease Control | `"STRESS_DECREASE"` | Object | - | Optional |
| 11 | Beam Section Property Option (Constant: 0 / Change with Tendon: 1) | `"iBSC"` | Integer | 1 | Optional |
| 12 | Frame Output 设置 | `"FRAME_OUTPUT"` | Object | - | Optional |
| 13 | Save Output of Current Stage (Beam/Truss) | `"bSAVE_OCS"` | Boolean | false | Optional |
| 14 | Nonlinear Analysis Control (`iINC_NLA` ≠ 0 时) | `"NONL_CONTROL"` | Object | - | Optional |

> ⚠️ **2026-08-25 确认：** `iBSC`/`FRAME_OUTPUT`/`bSAVE_OCS`/`NONL_CONTROL` 4 个字段整体
> 缺失。尤其 `iBSC` 与遗留版 `STCT`(第 17 节)同名但**默认值不同**
> (STCT 为 0，STCT-M1 为 1)（article id `57053813627673`）。

### Parameters — ANAL_TYPE 对象

| Key | Value Type | Description |
|-----|------------|-------------|
| `"iINC_NLA"` | Integer | 分析类型 (Linear: 0 / Geometric Nonlinear: 1 / Material Nonlinear: 2 / Geometric+Material Nonlinear: 3) |
| `"iNLA_TYPE"` | Integer | 阶段选项 (Independent: 0 / Accumulative: 1) — `iINC_NLA`=2 或 3 时仅允许 `iNLA_TYPE`=1 |
| `"bIEMF"` | Boolean | Include Equilibrium Element Nodal Forces (仅当 `iINC_NLA`=1 & `iNLA_TYPE`=0 时) |
| `"bINC_PDL"` | Boolean | Include P-Delta Effect (仅当 `iINC_NLA`=0 时) |
| `"bINC_TDE"` | Boolean | Include Time Dependent Effect (仅当 `iNLA_TYPE`=1 & `iINC_NLA`∈{0,1} 时) |

> ⚠️ **2026-08-25 确认：** `iINC_NLA` 新增了第 4 个值(3 = 同时考虑 Geometric+Material Nonlinear)，
> 而 `bIEMF` 整体缺失（article id `57053813627673`）。

### Parameters — RESTART_CS_ANAL 对象

| Key | Value Type | Description |
|-----|------------|-------------|
| `"OPT_USE"` | Boolean | 是否使用 Restart 分析 |
| `"RESTART_STAGE"` | Array [String] | Restart 目标施工阶段列表 |

### Parameters — ERECTION_LOAD 条目

| Key | Value Type | Description |
|-----|------------|-------------|
| `"LTYPECC"` | String | Erection Load Case Name |
| `"EREC"` | String | Load Type for C.S (`"D"`, `"W"`, …) |
| `"vLCNAME"` | Array [String] | Load Case Name List |

### Parameters — TIME_DEP_CONTROL 对象

| Key | Value Type | Description |
|-----|------------|-------------|
| `"CREEP_SHRINKAGE"` | Object | 徐变·干燥收缩设置 |
| `"CREEP_SHRINKAGE.OPT_USE"` | Boolean | 是否使用 |
| `"CREEP_SHRINKAGE.TYPE"` | String | (`"CREEP"`/`"SHRINKAGE"`/`"BOTH"`) |
| `"CREEP_SHRINKAGE.bOUCC"` | Boolean | Only User's Creep Coefficient |
| `"CREEP_SHRINKAGE.INTERNAL_STEP"` | Object | `{ "OPT_USE": bool, "iITS": int }` |
| `"CREEP_SHRINKAGE.AUTO_TIME_STEP"` | Object | `{ "OPT_USE": bool, "iT10","iT100","iT1K","iT5K","iT10K": int }` |
| `"CREEP_SHRINKAGE.bTTLE_CS"` | Boolean | Tendon Tension Loss Effect |
| `"CREEP_SHRINKAGE.bRCE"` | Boolean | Re-bar Confinement Effect |
| `"bVAR"` | Boolean | Variation of Comp. Strength |
| `"bAPPLY_ELA"` | Boolean | Apply Time Dep. Elastic Modulus to Post C.S |
| `"bTTLE_ES"` / `"iTTLE_ES"` | Boolean / Integer | Tendon Tension Loss (Elastic Shortening) / Type |

> ⚠️ **2026-08-25 确认：** `CREEP_SHRINKAGE.TYPE` 的第二个 enum 值，与遗留版 `STCT`(第 17 节)的
> `"SHRINK"` 不同，在 STCT-M1 中标为 **`"SHRINKAGE"`** — 在原文 JSON Schema 与 Specifications
> 表两侧均一致确认（article id `57053813627673`）。此前文档与 STCT 相同，
> 误记为 `"SHRINK"`。

### Parameters — NONL_CONTROL 对象（`iINC_NLA` ≠ 0 时使用 — 对应遗留版 `NLCT`/`NLCT-M1`）

| Key | Value Type | Default | Description |
| --- | --- | --- | --- |
| `"iLSTEP"` | Integer (≥1) | - | 增量步数 |
| `"INTOUT"` | String (enum: `"EVERY"`/`"LAST"`) | "LAST" | 中间输出请求 |
| `"ADVANCED"` | Object | - | 高级设置 — 下级 `USE_DEF_SETTINGS`(Boolean, Required, 默认 true)/`STIFF_UPD_SCHEME`(Integer enum 0=Custom·1=Full Newton-Raphson·2=Initial Stiffness, `USE_DEF_SETTINGS=false` 时)/`ITER_BEF_UPDATE`(Integer, 仅 `STIFF_UPD_SCHEME=0` 时)/`TERMINATE_ON_FAIL_CONV`(Boolean)/`MAX_ITER_INCREMENT`(Integer)/`MAX_BISECT_LEVEL`(Integer)/`SMART_BISECT`(Boolean)/`DIVERG_THRESH`(Number)/`ENABLE_LINE_SEARCH`(Boolean, 默认 true)/`LINE_SEARCH`(Object, `ENABLE_LINE_SEARCH=true` 时必填 — 下级 `OPT_USE`(Boolean,Required)/`LINE_SEARCH_TYPE`(enum `"AUTO"`/`"USER"`, 默认 AUTO)/`MAX_LN_SRCH_ITER`(Integer, `LINE_SEARCH_TYPE="USER"` 时)/`LN_SEARCH_TOL`(Number, 同上)) |
| `"DISP"`/`"LOAD"`/`"WORK"` | Object | - | 位移/荷载/功收敛准则 — 各自下级 `OPT_USE`(Boolean, Required, 默认 false)/`VALUE`(Number >0, `OPT_USE=true` 时必填) |

> `ADVANCED` 的 Key 名称与 §16 `NLCT-M1` 的 `ADVANCED` 对象(`STIFF_UPDATE_SCHEME`/`ITER_BEFORE_STIFF_UPDATE`/…、字符串 enum)类似，但**名称与类型不同**
> (STCT-M1 为 `STIFF_UPD_SCHEME`/`ITER_BEF_UPDATE`/… 及整数 enum，`LINE_SEARCH` 亦为嵌套对象) —
> 即使概念相同，各端点的序列化也不同，勿混用（article id `57053813627673`）。

### Parameters — 其余对象

| Object | Key | Value Type | Description |
|--------|-----|------------|-------------|
| `CABLE_CONTROL` | `"CPFC"` | String | Cable-Pretension Force Type (`"INTERNAL"`/`"EXTERNAL"`) |
| `CABLE_CONTROL` | `"bEXT_REPL"` | Boolean | External Force Replace |
| `INITIAL_CONTROL` | `"bCONV"` | Boolean | Convert Final Stage Forces to Initial Forces |
| `INITIAL_CONTROL` | `"bTRUSS"` / `"bBEAM"` | Boolean | Truss / Beam |
| `INITIAL_CONTROL` | `"bCHANGE_CABLE"` | Boolean | Change Cable to Equivalent Truss |
| `INITIAL_CONTROL` | `"bAPPLY_IMF"` | Boolean | Apply Initial Member Force to C.S |
| `INITIAL_DISP` | `"ITD_CONTROL"` | Object | `{ "OPT_USE", "ITD", "GROUP", "LFFC_OPT_USE", "LFFGR" }` |
| `INITIAL_DISP` | `"bCAMBER"` | Boolean | Apply Camber Displacement |
| `STRESS_DECREASE` | `"OPT_USE"` / `"iSDOPT"` / `"SDCONST"` | Boolean / Integer / Number | Stress Decrease 使用 / 选项 / 常数 |

### Request Body (PUT)

```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": true,
      "ANAL_TYPE": {
        "iINC_NLA": 0,
        "iNLA_TYPE": 1,
        "bINC_PDL": true,
        "bINC_TDE": true
      },
      "RESTART_CS_ANAL": {
        "OPT_USE": true,
        "RESTART_STAGE": ["CS1", "CS2"]
      },
      "ERECTION_LOAD": [
        { "LTYPECC": "Erection Dead Load", "EREC": "D", "vLCNAME": ["Self Weight", "Deck Concrete"] },
        { "LTYPECC": "Erection Wind Load", "EREC": "W", "vLCNAME": ["Wind Load"] }
      ],
      "bSDLE": true,
      "vSDLE": ["Grid Dead Load", "Grid Wearing Surface"],
      "TIME_DEP_CONTROL": {
        "CREEP_SHRINKAGE": {
          "OPT_USE": true,
          "TYPE": "BOTH",
          "bOUCC": false,
          "INTERNAL_STEP": { "OPT_USE": true, "iITS": 5 },
          "AUTO_TIME_STEP": {
            "OPT_USE": true,
            "iT10": 2, "iT100": 5, "iT1K": 10, "iT5K": 20, "iT10K": 30
          },
          "bTTLE_CS": true,
          "bRCE": true
        },
        "bVAR": true,
        "bAPPLY_ELA": true,
        "bTTLE_ES": true,
        "iTTLE_ES": 0
      },
      "CABLE_CONTROL": {
        "CPFC": "EXTERNAL",
        "bEXT_REPL": true
      },
      "INITIAL_CONTROL": {
        "bCONV": true,
        "bTRUSS": true,
        "bBEAM": true,
        "bCHANGE_CABLE": true,
        "bAPPLY_IMF": true
      },
      "INITIAL_DISP": {
        "ITD_CONTROL": {
          "OPT_USE": true,
          "ITD": "GROUP",
          "GROUP": "Erected Structure Group",
          "LFFC_OPT_USE": true,
          "LFFGR": "Lack of Fit Group"
        },
        "bCAMBER": true
      },
      "STRESS_DECREASE": {
        "OPT_USE": true,
        "iSDOPT": 1,
        "SDCONST": 1
      },
      "iBSC": 1,
      "FRAME_OUTPUT": {
        "bCALC_CFF": true,
        "bCALC_CSP": true,
        "bSELFCONS": true
      },
      "bSAVE_OCS": true,
      "NONL_CONTROL": {
        "iLSTEP": 10,
        "INTOUT": "EVERY",
        "ADVANCED": {
          "USE_DEF_SETTINGS": false,
          "STIFF_UPD_SCHEME": 0,
          "ITER_BEF_UPDATE": 3,
          "TERMINATE_ON_FAIL_CONV": true,
          "MAX_ITER_INCREMENT": 30,
          "MAX_BISECT_LEVEL": 5,
          "SMART_BISECT": true,
          "DIVERG_THRESH": 10,
          "ENABLE_LINE_SEARCH": true,
          "LINE_SEARCH": {
            "OPT_USE": true,
            "LINE_SEARCH_TYPE": "USER",
            "MAX_LN_SRCH_ITER": 5,
            "LN_SEARCH_TOL": 0.8
          }
        },
        "DISP": { "OPT_USE": true, "VALUE": 0.001 },
        "LOAD": { "OPT_USE": true, "VALUE": 0.001 },
        "WORK": { "OPT_USE": true, "VALUE": 0.000001 }
      }
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

def update_construction_stage_control_m1():
    payload = {
        "Assign": {
            "1": {
                "bLAST_FINAL": True,
                "ANAL_TYPE": {
                    "iINC_NLA": 0,       # 线性
                    "iNLA_TYPE": 1,      # 累加阶段
                    "bINC_PDL": True,
                    "bINC_TDE": True     # 时间相关效应
                },
                "ERECTION_LOAD": [
                    {"LTYPECC": "Erection Dead Load", "EREC": "D",
                     "vLCNAME": ["Self Weight", "Deck Concrete"]}
                ],
                "TIME_DEP_CONTROL": {
                    "CREEP_SHRINKAGE": {
                        "OPT_USE": True,
                        "TYPE": "BOTH",
                        "bOUCC": False,
                        "INTERNAL_STEP": {"OPT_USE": True, "iITS": 5},
                        "AUTO_TIME_STEP": {
                            "OPT_USE": True,
                            "iT10": 2, "iT100": 5, "iT1K": 10,
                            "iT5K": 20, "iT10K": 30
                        },
                        "bTTLE_CS": True,
                        "bRCE": True
                    },
                    "bVAR": True,
                    "bAPPLY_ELA": True,
                    "bTTLE_ES": True,
                    "iTTLE_ES": 0
                },
                "CABLE_CONTROL": {"CPFC": "EXTERNAL", "bEXT_REPL": True},
                "INITIAL_CONTROL": {
                    "bCONV": True, "bTRUSS": True, "bBEAM": True,
                    "bCHANGE_CABLE": True, "bAPPLY_IMF": True
                },
                "iBSC": 1,               # Change with Tendon
                "FRAME_OUTPUT": {
                    "bCALC_CFF": True,
                    "bCALC_CSP": True,
                    "bSELFCONS": True
                },
                "bSAVE_OCS": True,
                "NONL_CONTROL": {        # iINC_NLA != 0 时使用 (对应遗留版 NLCT/NLCT-M1)
                    "iLSTEP": 10,
                    "INTOUT": "EVERY",
                    "ADVANCED": {
                        "USE_DEF_SETTINGS": False,
                        "STIFF_UPD_SCHEME": 0,       # Custom
                        "ITER_BEF_UPDATE": 3,
                        "TERMINATE_ON_FAIL_CONV": True,
                        "MAX_ITER_INCREMENT": 30,
                        "MAX_BISECT_LEVEL": 5,
                        "SMART_BISECT": True,
                        "DIVERG_THRESH": 10,
                        "ENABLE_LINE_SEARCH": True,
                        "LINE_SEARCH": {
                            "OPT_USE": True,
                            "LINE_SEARCH_TYPE": "USER",
                            "MAX_LN_SRCH_ITER": 5,
                            "LN_SEARCH_TOL": 0.8
                        }
                    },
                    "DISP": {"OPT_USE": True, "VALUE": 0.001},
                    "LOAD": {"OPT_USE": True, "VALUE": 0.001},
                    "WORK": {"OPT_USE": True, "VALUE": 0.000001}
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/STCT-M1/1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Construction Stage Control (Hyper-S) updated:", resp.json())

update_construction_stage_control_m1()
```

---

## 19. /db/BCCT — Boundary Change Assignment

定义边界变更(Boundary Change)分配数据。选择以哪种边界数据类型(支座/弹簧/连接/刚度系数/端部释放等)作为变更对象，并指定边界组组合(`vBOUNDARY`)与按分析/荷载工况的适用(`vLOADANAL`)。

> `bWSSF`、`bESSF` 等部分项可能为 Civil NX 或 Gen NX 专用。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/BCCT` | 创建 |
| GET | `{base_url}/db/BCCT` | 查询 |
| PUT | `{base_url}/db/BCCT/{id}` | 修改 |
| DELETE | `{base_url}/db/BCCT/{id}` | 删除 |

### Parameters — 数据选择标志

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Support | `"bSPT"` | Boolean | false | Optional |
| 2 | Point Spring Support | `"bSPR"` | Boolean | false | Optional |
| 3 | General Spring Support | `"bGSPR"` | Boolean | false | Optional |
| 4 | Change General Link Property | `"bCGLINK"` | Boolean | false | Optional |
| 5 | Section Stiffness Scale Factor | `"bSSSF"` | Boolean | false | Optional |
| 6 | Plate Stiffness Scale Factor | `"bPSSF"` | Boolean | false | Optional |
| 7 | Beam End Release | `"bRLS"` | Boolean | false | Optional |
| 8 | Wall Stiffness Scale Factor | `"bWSSF"` | Boolean | false | Optional |
| 9 | Element Stiffness Scale Factor | `"bESSF"` | Boolean | false | Optional |
| 12 | Constrain DOF associated with specified displacements / settlements by boundary group combinations | `"bCDOF"` | Boolean | false | Optional |

### Parameters — Boundary List (`vBOUNDARY`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 10 | Boundary List | `"vBOUNDARY"` | Array [Object] | - | Required |
| (1) | Boundary Group Combination Name | `"BGCNAME"` | String | - | Required |
| (2) | Boundary Group List | `"vBG"` | Array [String] | - | Required |

### Parameters — Load Cases & Analysis List (`vLOADANAL`)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 11 | Load Cases & Analysis List | `"vLOADANAL"` | Array [Object] | - | Optional |
| (1) | Load Cases & Analysis Type | `"TYPE"` | String | - | Required |
| (2) | Boundary Group Combination Name | `"BGCNAME"` | String | - | Required |
| (3) | Static Load Case | `"LCNAME"` | String | - | Required |

**`vLOADANAL.TYPE` 取值：**

| Value | Description |
|-------|-------------|
| `"ST"` | Static Load Case |
| `"ULAT"` | Unlisted Analysis Types |
| `"THRSEV"` | TH / RS Analysis / Eigenvalue |
| `"THNS"` | TH Nonlinear Static Analysis |
| `"PO"` | Pushover Analysis |
| `"MV"` | Moving Load Analysis |
| `"SM"` | Settlements Analysis |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "bSPT": true,
      "bSPR": true,
      "bGSPR": false,
      "bCGLINK": false,
      "bSSSF": true,
      "bPSSF": false,
      "bRLS": true,
      "bCDOF": false,
      "vBOUNDARY": [
        { "BGCNAME": "BGL1", "vBG": ["BG1", "BG2"] }
      ],
      "vLOADANAL": [
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC1" },
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC2" },
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC3" },
        { "TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC4" }
      ]
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

def set_boundary_change():
    payload = {
        "Assign": {
            "1": {
                "bSPT": True,      # 支座
                "bSPR": True,      # 点弹簧
                "bGSPR": False,
                "bCGLINK": False,
                "bSSSF": True,     # 截面刚度比例系数
                "bPSSF": False,
                "bRLS": True,      # 梁端部释放
                "bCDOF": False,
                "vBOUNDARY": [
                    {"BGCNAME": "BGL1", "vBG": ["BG1", "BG2"]}
                ],
                "vLOADANAL": [
                    {"TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC1"},
                    {"TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "LC2"}
                ]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BCCT", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Boundary Change Assignment set:", resp.json())

set_boundary_change()
```

---

## 20. /db/BCGD-M1 — Define Boundary Combination (Hyper-S)

定义用于 Hyper-S(MEC) 求解器的边界组组合(Boundary Group Combination)。指定组合名称与所包含的边界组列表。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/BCGD-M1` | 创建边界组合 |
| GET | `{base_url}/db/BCGD-M1` | 查询 |
| PUT | `{base_url}/db/BCGD-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/BCGD-M1/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Boundary Combination Name (1~20 字符，模型内唯一) | `"BCG_NAME"` | String | - | Required |
| 2 | Boundary Group List (所选边界组名称数组, 自动去重) | `"GROUP_LIST"` | Array [String] | - | Required |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "BCG_NAME": "Support_BCG",
      "GROUP_LIST": ["Fixed_Support", "Elastic_Link"]
    },
    "2": {
      "BCG_NAME": "Stage_BCG",
      "GROUP_LIST": ["Stage1_Boundary", "Stage2_Boundary", "Stage3_Boundary"]
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

def define_boundary_combination():
    payload = {
        "Assign": {
            "1": {
                "BCG_NAME": "Support_BCG",   # 组合名称 (1~20 字符)
                "GROUP_LIST": ["Fixed_Support", "Elastic_Link"]
            },
            "2": {
                "BCG_NAME": "Stage_BCG",
                "GROUP_LIST": ["Stage1_Boundary", "Stage2_Boundary", "Stage3_Boundary"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BCGD-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Boundary Combination defined:", resp.json())

define_boundary_combination()
```

---

## 21. /db/BCGA-M1 — Assign Boundary Combination (Hyper-S)

用于 Hyper-S(MEC) 求解器的边界组合分配数据。将边界组合(BCGD)分配给分析类型·荷载工况(`BC_ASSIGN`)，并指定要应用的边界变更项(`BC_SELECT`)。

### HTTP Methods

| Method | URL | 说明 |
|--------|-----|------|
| POST | `{base_url}/db/BCGA-M1` | 创建边界组合分配 |
| GET | `{base_url}/db/BCGA-M1` | 查询 |
| PUT | `{base_url}/db/BCGA-M1/{id}` | 修改 |
| DELETE | `{base_url}/db/BCGA-M1/{id}` | 删除 |

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Assign Boundary Combination to Analyses & Load Cases | `"BC_ASSIGN"` | Array [Object] | - | Required |
| (1) | Analysis Type | `"ANAL_TYPE"` | String (enum) | - | Required |
| (2) | Load Case Name (`ANAL_TYPE` ∈ {ST, NLTH, PO} 时必填) | `"LCNAME"` | String | - | Conditional |
| (3) | Boundary Group Combination Name (空字符串 = 无变更) | `"BGCNAME"` | String | "" | Optional |
| 2 | Apply to Boundary Change | `"BC_SELECT"` | Array [String (enum)] | - | Required |

**`BC_ASSIGN.ANAL_TYPE` 取值 (enum)：**

| Value | Description |
|-------|-------------|
| `"ST"` | Static |
| `"MV"` | Moving Load |
| `"SM"` | Settlement |
| `"EIGV"` | Eigenvalue |
| `"RS"` | Response Spectrum |
| `"LTH"` | Linear Time History |
| `"NLTH"` | Nonlinear Time History |
| `"PO"` | Pushover |

> **条件必填**：`ANAL_TYPE` 为 `ST`、`NLTH`、`PO` 时 `LCNAME` 为必填。其余分析类型为单一集合分析，因此无需 `LCNAME`。

**`BC_SELECT` 取值 (enum) — 要应用的边界变更项：**

| Value | Description | Value | Description |
|-------|-------------|-------|-------------|
| `"SECF"` | Section Stiffness Scale Factor | `"ESSF"` | Element Stiffness Scale Factor |
| `"EWSF"` | (Element) Wall Stiffness Scale Factor | `"PSSF"` | Plate Stiffness Scale Factor |
| `"WSSF"` | Wall Stiffness Scale Factor | `"CONS"` | Constraint |
| `"NSPR"` | Point (Nodal) Spring Support | `"GSPR"` | General Spring Support |
| `"SSPS"` | Surface Spring Support | `"ELNK"` | Elastic Link |
| `"RIGD"` | Rigid Link | `"NLNK"` | Nonlinear Link |
| `"CGLP"` | Change General Link Property | `"FRLS"` | Frame (Beam) End Release |
| `"OFFS"` | Beam Offset | `"PRLS"` | Plate End Release |
| `"MCON"` | Multi-Constraint | | |

### Request Body (POST)

```json
{
  "Assign": {
    "1": {
      "BC_ASSIGN": [
        { "ANAL_TYPE": "ST", "LCNAME": "DL", "BGCNAME": "Support_BCG" },
        { "ANAL_TYPE": "ST", "LCNAME": "LL", "BGCNAME": "Support_BCG" },
        { "ANAL_TYPE": "EIGV", "BGCNAME": "Stage_BCG" }
      ],
      "BC_SELECT": ["SECF", "NSPR", "ELNK", "FRLS"]
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

def assign_boundary_combination():
    payload = {
        "Assign": {
            "1": {
                "BC_ASSIGN": [
                    # Static 分析：LCNAME 必填
                    {"ANAL_TYPE": "ST", "LCNAME": "DL", "BGCNAME": "Support_BCG"},
                    {"ANAL_TYPE": "ST", "LCNAME": "LL", "BGCNAME": "Support_BCG"},
                    # Eigenvalue：无需 LCNAME
                    {"ANAL_TYPE": "EIGV", "BGCNAME": "Stage_BCG"}
                ],
                # 要应用的边界变更项
                "BC_SELECT": ["SECF", "NSPR", "ELNK", "FRLS"]
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/db/BCGA-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("Boundary Combination assigned:", resp.json())

assign_boundary_combination()
```

---

## End-to-End 工作流示例

分析控制数据设置的完整流程：**ACTL → EIGV → PDEL → BUCK → MVCT → NLCT → STCT → BCCT**

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

# Step 1: 主控制数据
post("/db/ACTL", {"Assign": {
    "1": {"ARDC": True, "ANRC": True, "ITER": 20, "TOL": 0.001,
          "CSECF": False, "TRS": True, "CRBAR": False,
          "BMSTRESS": False, "CLATS": False}
}})

# Step 2: 特征值分析 (Lanczos)
post("/db/EIGV", {"Assign": {
    "1": {"TYPE": "LANCZOS", "iFREQ": 30, "bMINMAX": False,
          "FRMIN": 0, "FRMAX": 0, "bSTRUM": True}
}})

# Step 3: P-Delta 分析
post("/db/PDEL", {"Assign": {
    "1": {"ITER": 5, "TOL": 1e-05,
          "PDEL_CASES": [{"LCNAME": "DL", "FACTOR": 1.0}]}
}})

# Step 4: 屈曲分析
post("/db/BUCK", {"Assign": {
    "1": {"MODE_NUM": 5, "OPT_POSITIVE": True,
          "OPT_CONSIDER_AXIAL_ONLY": True,
          "LOAD_FACTOR_FROM": 0, "LOAD_FACTOR_TO": 0,
          "OPT_STURM_SEQ": True,
          "ITEMS": [{"LCNAME": "DL", "FACTOR": 1, "LOAD_TYPE": 1}]}
}})

# Step 5: 移动荷载分析控制
post("/db/MVCT", {"Assign": {
    "1": {"METHOD": "EXACT", "POINT": "INF", "iIGP": 0, "iIGPN": 3,
          "PLATE": "NODAL", "bSTRCALC": True, "bCONCURRENT": True,
          "bCONCLINK": True, "FRAME": "AXIAL", "bCSTRCALC": True,
          "bREAC": True, "bRG": False, "RGN": "",
          "bDISP": True, "bDG": False, "DGN": "",
          "bFM": True, "bFG": False, "FGN": "",
          "bL": True, "bLG": False, "LGN": ""}
}})

# Step 6: 非线性分析控制 (Newton-Raphson)
post("/db/NLCT", {"Assign": {
    "1": {"NONLINEAR_TYPE": "GEOM+MATL", "ITERATION_METHOD": "NEWTON",
          "NUMBER_STEPS": 1, "MAX_ITERATIONS": 30,
          "OPT_ENERGY_NORM": True, "ENERGY_NORM": 0.001,
          "OPT_DISPLACEMENT_NORM": True, "DISPLACEMENT_NORM": 0.001,
          "OPT_FORCE_NORM": True, "FORCE_NORM": 0.001,
          "NEWTON_ITEMS": [{"ITERATION_METHOD": "NEWTON", "LCNAME": "DL",
                            "NUMBER_STEPS": 1, "MAX_ITERATIONS": 30,
                            "LOAD_FACTORS": [1]}]}
}})

# Step 7: 施工阶段分析控制 (线性、累加)
post("/db/STCT", {"Assign": {
    "1": {"bLAST_FINAL": True, "iINC_NLA": 0, "iNLA_TYPE": 1,
          "bINC_PDL": True, "iITER": 30, "TOL": 0.01,
          "bINC_TDE": True, "bCNS": True, "TYPE": "BOTH",
          "iITER_CR": 5, "TOL_CR": 0.01, "CPFC": "INTERNAL"}
}})

# Step 8: 边界变更分配
post("/db/BCCT", {"Assign": {
    "1": {"bSPT": True, "bSPR": True, "bSSSF": True, "bRLS": True,
          "vBOUNDARY": [{"BGCNAME": "BGL1", "vBG": ["BG1", "BG2"]}],
          "vLOADANAL": [{"TYPE": "ST", "BGCNAME": "BGL1", "LCNAME": "DL"}]}
}})

print("\nAll Analysis Control settings applied successfully.")
```

---

*下一部分：[13_DB_Load_Combinations.md](./13_DB_Load_Combinations.md)*
