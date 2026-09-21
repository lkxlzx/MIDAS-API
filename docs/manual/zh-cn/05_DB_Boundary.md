# 05 · DB – Boundary

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:** `https://moa-engineers.midasit.com:443/gen`  
> **认证：** 所有请求都必须带 `MAPI-Key: <your-key>` 头  
> **出处：** [MIDAS API Online Manual – Boundary](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../05_DB_Boundary.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | [`/db/CONS`](#1-dbcons--constraint-support) | Constraint Support (节点支承条件) |
| 2 | [`/db/NSPR`](#2-dbnspr--point-spring) | Point Spring (点弹簧) |
| 3 | [`/db/GSTP`](#3-dbgstp--define-general-spring-type) | Define General Spring Type (定义一般弹簧类型) |
| 4 | [`/db/GSPR`](#4-dbgspr--assign-general-spring-supports) | Assign General Spring Supports (指定一般弹簧支承) |
| 5 | [`/db/SSPS`](#5-dbssps--surface-spring) | Surface Spring (面弹簧) |
| 6 | [`/db/ELNK`](#6-dbelnk--elastic-link) | Elastic Link |
| 7 | [`/db/RIGD`](#7-dbrigd--rigid-link) | Rigid Link |
| 8 | [`/db/NLLP`](#8-dbnllp--general-link-properties) | General Link Properties (定义一般连接属性) |
| 9 | [`/db/NLNK`](#9-dbnlnk--general-link) | General Link (指定一般连接) |
| 10 | [`/db/NLNK-M1`](#10-dbnlnk-m1--general-link-hyper-s) | General Link – Hyper-S |
| 11 | [`/db/CGLP`](#11-dbcglp--change-general-link-property) | Change General Link Property |
| 12 | [`/db/FRLS`](#12-dbfrls--beam-end-release) | Beam End Release (梁端释放) |
| 13 | [`/db/OFFS`](#13-dboffs--beam-end-offsets) | Beam End Offsets (梁端偏移) |
| 14 | [`/db/PRLS`](#14-dbprls--plate-end-release) | Plate End Release (板端释放) |
| 15 | [`/db/MLFC`](#15-dbmlfc--force-deformation-function) | Force-Deformation Function (定义非线性函数) |
| 16 | [`/db/SDVI`](#16-dbsdvi--seismic-device--viscousoil-damper) | Seismic Device – Viscous/Oil Damper |
| 17 | [`/db/SDVE`](#17-dbsdve--seismic-device--viscoelastic-damper) | Seismic Device – Viscoelastic Damper |
| 18 | [`/db/SDST`](#18-dbsdst--seismic-device--steel-damper) | Seismic Device – Steel Damper |
| 19 | [`/db/SDHY`](#19-dbsdhy--seismic-device--hysteretic-isolator-mss) | Seismic Device – Hysteretic Isolator (MSS) |
| 20 | [`/db/SDIS`](#20-dbsdis--seismic-device--isolator-mss) | Seismic Device – Isolator (MSS) |
| 21 | [`/db/MCON`](#21-dbmcon--linear-constraints) | Linear Constraints (线性约束条件) |
| 22 | [`/db/PZEF`](#22-dbpzef--panel-zone-effects) | Panel Zone Effects |
| 23 | [`/db/CLDR`](#23-dbcldr--define-constraints-label-direction) | Define Constraints Label Direction |
| 24 | [`/db/DRLS`](#24-dbdrls--diaphragm-disconnect) | Diaphragm Disconnect (隔板解除) |

---

## 公共 Python 辅助函数

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"

def midas_api(method: str, endpoint: str, body=None):
    """MIDAS NX API 调用辅助函数"""
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/db/CONS` — Constraint Support

为节点指定支承条件（固定·销·滚动等）。  
`CONSTRAINT` 字符串共7位，顺序为 `[DX, DY, DZ, RX, RY, RZ, RW]`，`1`=约束，`0`=自由。  
RW 是 Warping Torsion（翘曲扭转）自由度。

**Endpoint:** `{base url}/db/CONS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Constraint Supports (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Constraint `[DX,DY,DZ,RX,RY,RZ,RW]` · `1`=约束, `0`=自由 | `"CONSTRAINT"` | String(7) | — | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        { "ID": 1, "GROUP_NAME": "Support", "CONSTRAINT": "1111111" }
      ]
    },
    "2": {
      "ITEMS": [
        { "ID": 2, "GROUP_NAME": "Support", "CONSTRAINT": "1110000" }
      ]
    },
    "5": {
      "ITEMS": [
        { "ID": 5, "GROUP_NAME": "Support", "CONSTRAINT": "1111000" }
      ]
    }
  }
}
```

### Python 示例

```python
# --- CONS: 设置节点支承条件 ---
# CONSTRAINT 代码表
# "1111111" → 完全固定 (Fixed)
# "1110000" → 销支承 (Pin: DX DY DZ 约束, 旋转自由)
# "1111000" → 一般铰 (DX DY DZ RX 约束)
# "1010000" → 滚动 (仅 DY 约束)

cons_data = {
    "Assign": {
        # 节点1: 完全固定
        "1": {"ITEMS": [{"ID": 1, "GROUP_NAME": "Foundation", "CONSTRAINT": "1111111"}]},
        # 节点5: 销支承
        "5": {"ITEMS": [{"ID": 5, "GROUP_NAME": "Foundation", "CONSTRAINT": "1110000"}]},
        # 节点10: Y方向滚动
        "10": {"ITEMS": [{"ID": 10, "GROUP_NAME": "Foundation", "CONSTRAINT": "0110000"}]},
    }
}

# 输入支承条件
result = midas_api("POST", "/db/CONS", cons_data)

# 全部查询
all_cons = midas_api("GET", "/db/CONS")

# 修改特定节点(ID=5)
update_data = {
    "Assign": {
        "5": {"ITEMS": [{"ID": 5, "GROUP_NAME": "Foundation", "CONSTRAINT": "1111000"}]}
    }
}
midas_api("PUT", "/db/CONS", update_data)

# 解除特定节点(ID=10)的支承
midas_api("DELETE", "/db/CONS", {"Assign": {"10": {}}})
```

---

## 2. `/db/NSPR` — Point Spring

为节点指定点弹簧。支持 Linear / Compression-Only / Tension-Only / Multi-Linear 四种类型。

**Endpoint:** `{base url}/db/NSPR`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核后全面更正。** 旧版本把 COMP/TENS/MULTI 三种类型混为一谈，
> 误记为 `DIR`(1~4)·`DV`·以及不存在的 `"SK"` 字段（article id
> `35945908301081`）。实际上 **COMP/TENS 使用 `STIFF`（单一刚度值）**、**MULTI 使用
> `FUNCTION`（MLFC 函数 ID）**，`DIR` 是 0~6（含 Vector）的 enum，`DV` 是仅在 `DIR=6`
> （Vector）时使用的方向向量。LINEAR 类型的 `Cr`（阻尼系数数组）也曾遗漏。

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | Point Spring (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Spring Type · `"LINEAR"` / `"COMP"` / `"TENS"` / `"MULTI"` | `"TYPE"` | String | — | Required |
| (3) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Create Function Type · 0=点弹簧函数, 1=面弹簧函数 | `"FormType"` | Integer | 0 | Optional |

#### LINEAR 专用

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| (5) | Spring Stiffness `[SDx, SDy, SDz, SRx, SRy, SRz]` | `"SDR"` | Array[Number,6] | — | Required |
| (6) | Fixed Option `[SDx, SDy, SDz, SRx, SRy, SRz]` | `"F_S"` | Array[Boolean,6] | false | Optional |
| (7) | 是否使用 Damping Constant | `"DAMPING"` | Boolean | false | Optional |
| (8) | Damping `[Cx, Cy, Cz, CRx, CRy, CRz]` | `"Cr"` | Array[Number,6] | 0 | Optional |

#### COMP(Compression-Only) / TENS(Tension-Only) 专用

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| (5) | Stiffness | `"STIFF"` | Number | — | Required |
| (6) | Direction · Dx(+):0 / Dx(–):1 / Dy(+):2 / Dy(–):3 / Dz(+):4 / Dz(–):5 / Vector:6 | `"DIR"` | Integer | — | Required |
| (7) | 法向向量(`DIR`=6 时) | `"DV"` | Array[Number,3] | 0 | Optional |

#### MULTI(Multi-Linear) 专用

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| (5) | Force-Deformation 函数 ID(在 `/db/MLFC` 中定义) | `"FUNCTION"` | Integer | — | Required |
| (6) | Direction · Dx(+):0 / Dx(–):1 / Dy(+):2 / Dy(–):3 / Dz(+):4 / Dz(–):5 / Vector:6 | `"DIR"` | Integer | — | Required |
| (7) | 法向向量(`DIR`=6 时) | `"DV"` | Array[Number,3] | 0 | Optional |

#### By Surface Spring Function 专用(`FormType`=1 时公共追加)

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| (9) | Width of Frame | `"EFFAREA"` | Number | 0 | Optional |
| (10) | Modulus of Subgrade Reaction `[Kx, Ky, Kz]` | `"DK"` | Array[Number,3] | 0 | Optional |

### 请求体示例

```json
{
  "Assign": {
    "2": {
      "ITEMS": [{
        "ID": 1, "TYPE": "LINEAR", "GROUP_NAME": "Service",
        "SDR": [33000, 34000, 35000, 33000000, 34000000, 35000000],
        "F_S": [false, false, false, false, false, false],
        "DAMPING": true,
        "Cr": [1, 2, 3, 4, 5, 6]
      }]
    },
    "4": {
      "ITEMS": [{
        "ID": 1, "TYPE": "COMP", "GROUP_NAME": "Service",
        "DIR": 4, "DV": [0, 0, 0], "STIFF": 1000000
      }]
    },
    "6": {
      "ITEMS": [{
        "ID": 1, "TYPE": "TENS", "GROUP_NAME": "Service",
        "DIR": 6, "DV": [0, -1, -1], "STIFF": 1000000
      }]
    },
    "8": {
      "ITEMS": [{
        "ID": 1, "TYPE": "MULTI", "GROUP_NAME": "Service",
        "DIR": 4, "DV": [0, 0, 0], "FUNCTION": 1
      }]
    }
  }
}
```

### Python 示例

```python
# --- NSPR: 指定点弹簧 ---

# 节点2: 线性弹簧（水平 Kx=33000, Ky=34000, Kz=35000 kN/m）
nspr_linear = {
    "Assign": {
        "2": {
            "ITEMS": [{
                "ID": 2,
                "TYPE": "LINEAR",
                "GROUP_NAME": "Foundation_Spring",
                "SDR": [33000.0, 34000.0, 35000.0, 33000000.0, 34000000.0, 35000000.0],
                "F_S": [False, False, False, False, False, False]
            }]
        }
    }
}

# 节点4: 只压弹簧 — DIR=6(Vector), 用 DV 指定方向（土压方向）
nspr_comp = {
    "Assign": {
        "4": {
            "ITEMS": [{
                "ID": 4,
                "TYPE": "COMP",
                "GROUP_NAME": "Soil_Spring",
                "DIR": 6,            # Vector 方式
                "DV": [0.0, -1.0, -1.0],
                "STIFF": 2000000.0
            }]
        }
    }
}

midas_api("POST", "/db/NSPR", nspr_linear)
midas_api("POST", "/db/NSPR", nspr_comp)

# 全部查询
all_nspr = midas_api("GET", "/db/NSPR")
```

---

## 3. `/db/GSTP` — Define General Spring Type

定义可自定义全部 6×6 刚度·质量·阻尼矩阵的一般弹簧类型。  
`SPRING`、`MASS`、`DAMPING` 数组由**上三角矩阵**的21个项构成。

**Endpoint:** `{base url}/db/GSTP`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核更正。** 21项数组的下标-矩阵位置映射，实际是按「先排6个对角项，
> 其后非对角项按行顺序」的方式排列（article id `35946004118169`, footnote
> ¹⁾）。这与旧版本所写的标准上三角(K11,K12,K13,...,K22,K23,...)顺序不同，因此若按那个
> 顺序填充数组，值会落到完全不同的弹簧位置上 —— 属于对实务影响很大的
> 更正，故下面的表与示例已按原文替换。

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | General Spring Name | `"NAME"` | String | — | Required |
| 2 | Stiffness Matrix Option | `"OPT_STIFFNESS"` | Boolean | false | Optional |
| 3 | Stiffness Matrix (21项) ¹⁾ | `"SPRING"` | Array[Number,21] | 0 | Optional |
| 4 | Mass Matrix Option | `"OPT_MASS"` | Boolean | false | Optional |
| 5 | Mass Matrix (21项) ¹⁾ | `"MASS"` | Array[Number,21] | 0 | Optional |
| 6 | Damping Matrix Option | `"OPT_DAMPING"` | Boolean | false | Optional |
| 7 | Damping Matrix (21项) ¹⁾ | `"DAMPING"` | Array[Number,21] | 0 | Optional |

> **注意：** `SPRING`/`MASS`/`DAMPING` 数组仅在对应的选项标志为 `true` 时才有效。

#### ¹⁾ 21项数组下标 ↔ 矩阵位置(Row, Column) 映射 (1-based)

| 下标(0-based) | 位置 | 下标 | 位置 | 下标 | 位置 |
| --- | --- | --- | --- | --- | --- |
| 0 | (1,1) | 7 | (1,3) | 14 | (2,6) |
| 1 | (2,2) | 8 | (1,4) | 15 | (3,4) |
| 2 | (3,3) | 9 | (1,5) | 16 | (3,5) |
| 3 | (4,4) | 10 | (1,6) | 17 | (3,6) |
| 4 | (5,5) | 11 | (2,3) | 18 | (4,5) |
| 5 | (6,6) | 12 | (2,4) | 19 | (4,6) |
| 6 | (1,2) | 13 | (2,5) | 20 | (5,6) |

对角项(1,1)~(6,6) 6个排在前面，其后从 (1,2) 开始按行顺序接续非对角项。

### 请求体示例

```json
{
  "Assign": {
    "3": {
      "NAME": "GS_Damping",
      "SPRING": [1, 7, 12, 16, 19, 21, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 17, 18, 20],
      "MASS": [1, 7, 12, 16, 19, 21, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 17, 18, 20]
    }
  }
}
```

> 上例与原文一致，值本身就是表示数组内位置的占位符(placeholder)，
> `OPT_STIFFNESS`/`OPT_MASS`/`OPT_DAMPING` 选项标志在原文示例中并不存在 —— 实际使用时
> 必须把所用矩阵对应的选项以 `true` 一并发出。

### Python 示例

```python
# --- GSTP: 定义一般弹簧类型 ---
# 21项顺序(0-based): 0~5=对角项(1,1)~(6,6), 6~10=(1,2)~(1,6),
#                     11~14=(2,3)~(2,6), 15~17=(3,4)~(3,6),
#                     18~19=(4,5)~(4,6), 20=(5,6)

gstp_data = {
    "Assign": {
        "1": {
            "NAME": "Foundation_GS",
            "OPT_STIFFNESS": True,
            # 仅对角项有值(非对角项全部为0): idx0~5 = Kxx,Kyy,Kzz,Krxrx,Kryry,Krzrz
            "SPRING": [
                1000, 800, 800, 0, 0, 0,   # 对角项: Kx=1000, Ky=800, Kz=800, 旋转 0
                0, 0, 0, 0, 0,              # (1,2)~(1,6)
                0, 0, 0, 0,                 # (2,3)~(2,6)
                0, 0, 0,                    # (3,4)~(3,6)
                0, 0,                       # (4,5)~(4,6)
                0                           # (5,6)
            ]
        }
    }
}

midas_api("POST", "/db/GSTP", gstp_data)
```

---

## 4. `/db/GSPR` — Assign General Spring Supports

将在 GSTP 中定义的一般弹簧类型指定给节点。

**Endpoint:** `{base url}/db/GSPR`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | General Spring (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Defined General Spring Name (在 GSTP 中定义的名称) | `"TYPE_NAME"` | String | — | Required |

### 请求体示例

```json
{
  "Assign": {
    "14": {
      "ITEMS": [
        { "ID": 14, "GROUP_NAME": "Service", "TYPE_NAME": "Foundation_GS" }
      ]
    }
  }
}
```

### Python 示例

```python
# --- GSPR: 指定一般弹簧支承 ---
# 前提条件: GSTP 中必须已定义 "Foundation_GS" 类型

gspr_data = {
    "Assign": {
        "10": {"ITEMS": [{"ID": 10, "GROUP_NAME": "Pile_Cap", "TYPE_NAME": "Foundation_GS"}]},
        "11": {"ITEMS": [{"ID": 11, "GROUP_NAME": "Pile_Cap", "TYPE_NAME": "Foundation_GS"}]},
        "12": {"ITEMS": [{"ID": 12, "GROUP_NAME": "Pile_Cap", "TYPE_NAME": "Foundation_GS"}]},
    }
}

midas_api("POST", "/db/GSPR", gspr_data)
```

---

## 5. `/db/SSPS` — Surface Spring

在单元（框架·板·实体）的面或边上指定基于地基反力系数的弹簧。

**Endpoint:** `{base url}/db/SSPS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Surface Spring (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Element Type · `"FRAME"` / `"PLANAR(FACE)"` / `"PLANAR(EDGE)"` / `"SOLID"` | `"ELEM_TYPE"` | String | — | Required |
| (4) | Edge/Face 选择 · FRAME: Local x=2, y=0, z=1 · PLANAR/SOLID: Edge#1∼4=0∼3 | `"EDGE_FACE"` | Integer | 0 | Optional |
| (5) | Spring Type · 0=Linear, 1=Comp.-Only, 2=Tens.-Only | `"SPRING_TYPE"` | Integer | 0 | Optional |
| (6) | Modulus of Subgrade Reaction Ks | `"MODULUS"` | Number | — | Required |
| (7) | Width(仅 FRAME) | `"WIDTH"` | Number | — | Required(FRAME) |

### 请求体示例 (FRAME / PLANAR / SOLID)

```json
{
  "Assign": {
    "1": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Soil", "ELEM_TYPE": "FRAME",
        "EDGE_FACE": 1, "WIDTH": 1.2, "SPRING_TYPE": 0, "MODULUS": 500
      }]
    },
    "21": {
      "ITEMS": [{
        "ID": 21, "GROUP_NAME": "Soil", "ELEM_TYPE": "PLANAR(FACE)",
        "SPRING_TYPE": 0, "MODULUS": 500
      }]
    },
    "41": {
      "ITEMS": [{
        "ID": 41, "GROUP_NAME": "Soil", "ELEM_TYPE": "SOLID",
        "EDGE_FACE": 4, "SPRING_TYPE": 0, "MODULUS": 500
      }]
    }
  }
}
```

### Python 示例

```python
# --- SSPS: 指定面弹簧 ---
# 板单元(PLANAR)地基弹簧 - 用于地下外墙/基础楼板建模

ssps_data = {
    "Assign": {
        # 板单元 ID 5: 在基础楼板面上指定线性地基反力弹簧 Ks=30000 kN/m³
        "5": {
            "ITEMS": [{
                "ID": 5,
                "GROUP_NAME": "Foundation_Slab",
                "ELEM_TYPE": "PLANAR(FACE)",
                "SPRING_TYPE": 0,   # 0 = Linear
                "MODULUS": 30000.0  # Ks (kN/m³)
            }]
        },
        # 框架单元 ID 3: 在桩侧面指定只压水平弹簧
        "3": {
            "ITEMS": [{
                "ID": 3,
                "GROUP_NAME": "Pile_Side",
                "ELEM_TYPE": "FRAME",
                "EDGE_FACE": 0,     # Local y 方向
                "WIDTH": 1.0,
                "SPRING_TYPE": 1,   # 1 = Compression-Only
                "MODULUS": 10000.0  # Ks (kN/m³)
            }]
        }
    }
}

midas_api("POST", "/db/SSPS", ssps_data)
```

---

## 6. `/db/ELNK` — Elastic Link

在两个节点之间指定弹性连接。连接类型由 `LINK` 键区分，共支持7种。

**Endpoint:** `{base url}/db/ELNK`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 公共参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Node Numbers `[i-node, j-node]` | `"NODE"` | Array[Integer,2] | — | Required |
| 2 | Boundary Group Name | `"BNGR_NAME"` | String | Blank | Optional |
| 3 | Beta Angle (°) | `"ANGLE"` | Number | 0 | Optional |
| 4 | Link Type | `"LINK"` | String | — | Required |

### 按 LINK 类型的附加参数

> ⚠️ 原文 Specifications 表把 `"LINK"` 的值写作 `"MULTI LINEAR"`·`"RAIL INTERACT"`（含空格），
> 但 JSON Schema 与 Request Example 都使用不含空格的 `"MULTILINEAR"`·`"RAILINTERACT"`
> （示例优先于表）。下列为正确写法，请勿回改（article id `35946439146649`，
> 2026-08-25 确认 —— 错误举报对象）。

| LINK 值 | 说明 | 附加 Key |
|---------|------|---------|
| `"GEN"` | 一般 (6自由度弹簧) | `SDR[6]`, `R_S[6]`, `bSHEAR`, `DR[2]` |
| `"RIGID"` | 刚体连接 | (无) |
| `"SADDLE"` | 鞍座 (桥梁支座专用) | (无) |
| `"TENS"` | 只拉 Tension-Only | `SDR[6]` (仅 Dx 有效) |
| `"COMP"` | 只压 Compression-Only | `SDR[6]` (仅 Dx 有效) |
| `"MULTILINEAR"` | 多线形 Multi-Linear | `DIR`(0=Dx/1=Dy/2=Dz/3=Rx/4=Ry/5=Rz), `MLFC`(函数 ID), `bSHEAR`, `DRENDI` |
| `"RAILINTERACT"` | 轨道相互作用 Rail Track Interaction | `DIR`(**仅 1=Dy/2=Dz 有效** — 与 Multi-Linear 的 enum 范围不同), `RLFC`(函数 ID), `bSHEAR`, `DRENDI` |

`SDR` / `R_S` 数组顺序: `[SDx, SDy, SDz, SRx, SRy, SRz]`  
`DIR` 取值: 0=Dx, 1=Dy, 2=Dz, 3=Rx, 4=Ry, 5=Rz

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "NODE": [1, 2], "LINK": "GEN", "ANGLE": 0,
      "SDR": [1000, 500, 500, 0, 0, 0],
      "R_S": [false, false, false, false, false, false],
      "bSHEAR": false, "DR": [0, 0]
    },
    "3": { "NODE": [3, 4], "LINK": "RIGID", "ANGLE": 0, "BNGR_NAME": "Service" },
    "5": { "NODE": [5, 6], "LINK": "COMP", "ANGLE": 0, "SDR": [1100, 0, 0, 0, 0, 0] },
    "6": {
      "NODE": [6, 7], "LINK": "MULTILINEAR", "ANGLE": 0,
      "BNGR_NAME": "Service", "DIR": 1, "MLFC": 1, "DRENDI": 0.5
    }
  }
}
```

### Python 示例

```python
# --- ELNK: 指定弹性连接 ---

elnk_data = {
    "Assign": {
        # GEN 类型: 6自由度独立弹簧
        "1": {
            "NODE": [1, 2],
            "LINK": "GEN",
            "ANGLE": 0.0,
            "SDR": [5000.0, 3000.0, 3000.0, 0.0, 0.0, 0.0],  # kN/m
            "R_S": [False, False, False, False, False, False],
            "bSHEAR": False,
            "DR": [0.0, 0.0]
        },
        # RIGID 类型: 刚体连接
        "2": {
            "NODE": [3, 4],
            "LINK": "RIGID",
            "ANGLE": 0.0,
            "BNGR_NAME": "Seismic_Links"
        },
        # TENS 类型: 只拉
        "3": {
            "NODE": [5, 6],
            "LINK": "TENS",
            "ANGLE": 0.0,
            "SDR": [2000.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        },
        # MULTILINEAR 类型: 参照非线性函数 (需要 MLFC ID=1)
        "4": {
            "NODE": [7, 8],
            "LINK": "MULTILINEAR",
            "ANGLE": 0.0,
            "BNGR_NAME": "Nonlinear_Links",
            "DIR": 1,       # Dy 方向
            "MLFC": 1,      # Force-Deformation 函数 ID
            "DRENDI": 0.5   # 剪切弹簧位置比例
        }
    }
}

midas_api("POST", "/db/ELNK", elnk_data)
```

---

## 7. `/db/RIGD` — Rigid Link

在 Master 节点与多个 Slave 节点之间指定刚体连接。  
`DOF` 整数的每一位 `1`=刚体，`0`=自由，位数顺序为 DX↔6th, DY↔5th, DZ↔4th, RX↔3rd, RY↔2nd, RZ↔1st。

**Endpoint:** `{base url}/db/RIGD`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Rigid Link (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number (Master 节点 ID) | `"ID"` | Integer | 0 | Optional |
| (2) | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Degree of Freedom (整数: 每一位对应 DX∼RZ) | `"DOF"` | Integer | — | Required |
| (4) | Slave Node ID Numbers | `"S_NODE"` | Array[Integer] | — | Required |

**DOF 示例:**  
`110001` → DX(=1), DY(=1), DZ(=0), RX(=0), RY(=0), RZ(=1) 约束

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Diaphragm",
        "DOF": 110001,
        "S_NODE": [2, 3, 4, 5, 6, 7, 8]
      }]
    }
  }
}
```

### Python 示例

```python
# --- RIGD: 刚体连接 (用于楼层隔板建模) ---

rigd_data = {
    "Assign": {
        # Master 节点1: DX, DY, RZ 约束 (平面隔板)
        # DOF = 110001 → 6th(DX)=1, 5th(DY)=1, 4th(DZ)=0, 3rd(RX)=0, 2nd(RY)=0, 1st(RZ)=1
        "1": {
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "Floor_Diaphragm",
                "DOF": 110001,
                "S_NODE": [2, 3, 4, 5, 6, 7, 8, 9, 10]
            }]
        }
    }
}

midas_api("POST", "/db/RIGD", rigd_data)
```

---

## 8. `/db/NLLP` — General Link Properties

定义用于一般连接(General Link)的非线性属性。以 `APPLICATION_TYPE` + `APPLICATION_TYPE_D` 组合指定装置类型。

**Endpoint:** `{base url}/db/NLLP`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### APPLICATION_TYPE 组合表

| APPLICATION_TYPE | APPLICATION_TYPE_D | 说明 |
|------------------|--------------------|------|
| `"ELEMENT"` | `"SPG"` | Spring (弹簧) |
| `"ELEMENT"` | `"DSP"` | Linear Dashpot |
| `"ELEMENT"` | `"SLD"` | Spring & Linear Dashpot |
| `"ELEMENT2"` | `"VI"` | Viscous/Oil Damper → 内部参照 SDVI |
| `"ELEMENT2"` | `"VE"` | Viscoelastic Damper → 内部参照 SDVE |
| `"ELEMENT2"` | `"ST"` | Steel Damper → 内部参照 SDST |
| `"ELEMENT2"` | `"HY"` | Hysteretic Isolator → 内部参照 SDHY |
| `"ELEMENT2"` | `"IS"` | Isolator (MSS) → 内部参照 SDIS |
| `"FORCE"` | `"VD"` | Force-Type Viscoelastic Damper |
| `"FORCE"` | `"GAP"` | Gap |
| `"FORCE"` | `"HOOK"` | Hook |
| `"FORCE"` | `"HS"` | Hysteretic System |
| `"FORCE"` | `"LRBI"` | Lead Rubber Bearing Isolator |
| `"FORCE"` | `"FPSI"` | Friction Pendulum System Isolator |
| `"FORCE"` | `"TFPSI"` | Triple Friction Pendulum System Isolator |

### 请求参数（公共）

> ⚠️ **2026-08-25 复核补强：** 公共字段之后遗漏了 `DIST_RATIO_DY`/`DIST_RATIO_DZ`/
> `COUPLED_INPUT_METHOD` 3个（article id `35946764618905`）。该原文按
> `APPLICATION_TYPE`/`APPLICATION_TYPE_D` 的14种组合各有独立的参数集（各装置
> 的详细物性），是6000行以上的庞大文档，因此本文只按上方「APPLICATION_TYPE 组合表」所整理的
> 概要级别处理，各组合的详细字段（除经 SDVI/SDVE/SDST/SDHY/SDIS 参照者之外
> 的 FORCE 系列 GAP/HOOK/HS/LRBI/FPSI/TFPSI 等）不作全量记载（与 SECT/TDMT/FIMP
> 同一原则）。

| No. | 说明 | Key | 类型 | 必填 |
|-----|------|----|------|------|
| 1 | General Link Property Name | `"PROPERTY_NAME"` | String | Required |
| 2 | Description | `"DESC"` | String | Optional |
| 3 | Application Type | `"APPLICATION_TYPE"` | String | Required |
| 4 | Property/Devices Type | `"APPLICATION_TYPE_D"` | String | Required |
| 5 | Self-Weight (Total) | `"TOTAL_WEIGHT"` | Number | Optional |
| 6 | Lumped Weight Ratio | `"L_WEIGHT_RATIO"` | Number | Optional |
| 7 | Use Mass Option | `"OPT_USE_MASS"` | Boolean | Optional |
| 8 | Mass (Total) | `"TOTAL_MASS"` | Number | Optional |
| 9 | Lumped Mass Ratio | `"L_MASS_RATIO"` | Number | Optional |
| 10 | Shear Spring Location Option | `"OPT_SHEAR_SPR_LOC"` | Boolean | Optional |
| 11 | Distance Ratio from End I (Dy) | `"DIST_RATIO_DY"` | Number | Optional |
| 12 | Distance Ratio from End I (Dz) | `"DIST_RATIO_DZ"` | Number | Optional |
| 13 | Coupled Input Method | `"COUPLED_INPUT_METHOD"` | Integer | Optional |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "PROPERTY_NAME": "GL_Spring01", "APPLICATION_TYPE": "ELEMENT",
      "APPLICATION_TYPE_D": "SPG", "DESC": "Foundation Spring",
      "TOTAL_WEIGHT": 0, "OPT_USE_MASS": false
    },
    "11": {
      "PROPERTY_NAME": "GL_ViscousDamper01", "APPLICATION_TYPE": "ELEMENT2",
      "APPLICATION_TYPE_D": "VI", "DESC": "Seismic Viscous Damper"
    }
  }
}
```

### Python 示例

```python
# --- NLLP: 定义一般连接属性 ---

nllp_data = {
    "Assign": {
        # 弹簧类型一般连接
        "1": {
            "PROPERTY_NAME": "GL_Isolator_Spring",
            "DESC": "Base Isolation Spring",
            "APPLICATION_TYPE": "ELEMENT",
            "APPLICATION_TYPE_D": "SPG",
            "TOTAL_WEIGHT": 0.0,
            "OPT_USE_MASS": False
        },
        # 隔震装置 (铅芯橡胶支座 - ELEMENT2 + IS)
        # 实际装置数据在 SDIS 中另行定义
        "2": {
            "PROPERTY_NAME": "GL_LRB_01",
            "DESC": "Lead Rubber Bearing",
            "APPLICATION_TYPE": "ELEMENT2",
            "APPLICATION_TYPE_D": "IS"
        }
    }
}

midas_api("POST", "/db/NLLP", nllp_data)
```

---

## 9. `/db/NLNK` — General Link

将在 NLLP 中定义的一般连接属性指定到两个节点之间。按坐标系（单元系/全局系）不同，方向指定方法有三种。

**Endpoint:** `{base url}/db/NLNK`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Node 1 ID | `"NODE1"` | Integer | — | Required |
| 2 | Node 2 ID | `"NODE2"` | Integer | — | Required |
| 3 | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 4 | General Link Property Name | `"PROP_NAME"` | String | — | Required |
| 5 | Inelastic Hinge Property Name | `"IEHP_NAME"` | String | Blank | Optional |
| 6 | Reference Coordinate System · 0=Element, 1=Global | `"REF_SYSTEM"` | Integer | — | Required |
| — | **REF_SYSTEM=0 (单元系)** | | | | |
| 7 | Beta Angle (°) | `"BETA_ANGLE"` | Number | 0 | Optional |
| — | **REF_SYSTEM=1 (全局系) – Angle 方式** | | | | |
| 7 | Input Method · 0=Angle | `"INPUT_METHOD"` | Integer | — | Required |
| 8 | Angle Values `[about X, about y', about z'']` | `"ANGLE_VALUES"` | Array[Object] | — | Required |
| — | **REF_SYSTEM=1 (全局系) – 3Points 方式** | | | | |
| 7 | Input Method · 1=3 Points | `"INPUT_METHOD"` | Integer | — | Required |
| 8 | Point Values `[P0[3], P1[3], P2[3]]` | `"POINT_VALUES"` | Array[Object,3] | — | Required |
| — | **REF_SYSTEM=1 (全局系) – Vector 方式** | | | | |
| 7 | Input Method · 2=Vector | `"INPUT_METHOD"` | Integer | — | Required |
| 8 | Vector Points `[V1[3], V2[3]]` | `"VECTOR_VALUES"` | Array[Object,2] | — | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "NODE1": 10, "NODE2": 11,
      "PROP_NAME": "GL_LRB_01", "REF_SYSTEM": 0, "BETA_ANGLE": 0,
      "GROUP_NAME": "Isolation_Layer"
    },
    "2": {
      "NODE1": 11, "NODE2": 12, "PROP_NAME": "GL_LRB_01",
      "REF_SYSTEM": 1, "INPUT_METHOD": 0,
      "ANGLE_VALUES": [{ "VALUE": [0, 0, 30] }]
    }
  }
}
```

### Python 示例

```python
# --- NLNK: 指定一般连接 ---
# 前提条件: NLLP 中必须已定义 "GL_LRB_01" 属性

nlnk_data = {
    "Assign": {
        # 以单元坐标系为基准, Beta 角 0度
        "1": {
            "NODE1": 10, "NODE2": 11,
            "PROP_NAME": "GL_LRB_01",
            "IEHP_NAME": "",
            "REF_SYSTEM": 0,
            "BETA_ANGLE": 0.0,
            "GROUP_NAME": "Isolation_Level_1"
        },
        # 以全局坐标系为基准, 角度方式
        "2": {
            "NODE1": 12, "NODE2": 13,
            "PROP_NAME": "GL_LRB_01",
            "REF_SYSTEM": 1,
            "INPUT_METHOD": 0,
            "ANGLE_VALUES": [{"VALUE": [0.0, 0.0, 0.0]}],
            "GROUP_NAME": "Isolation_Level_1"
        }
    }
}

midas_api("POST", "/db/NLNK", nlnk_data)
```

---

## 10. `/db/NLNK-M1` — General Link (Hyper-S)

Hyper-S 求解器专用的一般连接指定 Endpoint。

> ⚠️ **2026-08-25 复核全面补强。** 旧版本写有「官方站点没有 JSON Schema 示例」，
> 并停留在只有3个字段的占位版本，但实际在 article id `56511465190937`(928行)
> 中有完整的规格 —— 本次定期复核比对时发现。结构与第9节 `/db/NLNK` 几乎相同
> （连坐标系·输入方式分支也相同），只是没有 `IEHP_NAME`（非线性铰属性）。

**Endpoint:** `{base url}/db/NLNK-M1`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | General Link Property Name | `"PROP_NAME"` | String | — | Required |
| 2 | Node 1 ID | `"NODE1"` | Integer | — | Required |
| 3 | Node 2 ID | `"NODE2"` | Integer | — | Required |
| 4 | Reference Coordinate System · 0=Element, 1=Global | `"REF_SYSTEM"` | Integer | — | Required |
| 5 (REF_SYSTEM=0) | Beta Angle | `"BETA_ANGLE"` | Number | 0 | Required |
| 6 (REF_SYSTEM=1) | Input Method · 0=Angle, 1=3 Points, 2=Vector | `"INPUT_METHOD"` | Integer | — | Required |
| 7 (INPUT_METHOD=0) | Angle Values `[about X, about y', about z'']` | `"ANGLE_VALUES"` | Array[Object] | — | Required |
| 8 (INPUT_METHOD=1) | Point Values `[P0[3], P1[3], P2[3]]` | `"POINT_VALUES"` | Array[Object] | — | Required |
| 9 (INPUT_METHOD=2) | Vector Values `[V1[3], V2[3]]` | `"VECTOR_VALUES"` | Array[Object] | — | Required |
| 10 | Boundary Group Name | `"GROUP_NAME"` | String | — | Optional |

各 `ANGLE_VALUES`/`POINT_VALUES`/`VECTOR_VALUES` 数组元素均为 `{"VALUE": [x, y, z]}` 形式的
object（与 NLNK 相同）。

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "PROP_NAME": "NLL_PROP_1",
      "NODE1": 101,
      "NODE2": 102,
      "REF_SYSTEM": 0,
      "BETA_ANGLE": 0,
      "GROUP_NAME": "Boundary Group 1"
    },
    "2": {
      "PROP_NAME": "NLL_PROP_1",
      "NODE1": 101,
      "NODE2": 102,
      "REF_SYSTEM": 1,
      "INPUT_METHOD": 0,
      "ANGLE_VALUES": [{ "VALUE": [0, 0, 0] }],
      "GROUP_NAME": "Boundary Group 1"
    }
  }
}
```

### Python 示例

```python
# --- NLNK-M1: Hyper-S 专用一般连接指定 ---
# 仅在使用 Hyper-S 求解器时有效, 结构与 /db/NLNK 相同(IEHP_NAME 除外)

nlnk_m1_data = {
    "Assign": {
        "1": {
            "PROP_NAME": "GL_HyperS_Prop",
            "NODE1": 20,
            "NODE2": 21,
            "REF_SYSTEM": 0,
            "BETA_ANGLE": 0,
            "GROUP_NAME": "Isolation_Level_1"
        }
    }
}

midas_api("POST", "/db/NLNK-M1", nlnk_m1_data)
```

---

## 11. `/db/CGLP` — Change General Link Property

把特定一般连接单元的属性更改为另一个 NLLP 属性。

**Endpoint:** `{base url}/db/CGLP`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | General Link ID Number | `"GLINK_KEY"` | Integer | — | Required |
| 2 | Change Property Name (在 NLLP 中定义的名称) | `"CHANGE_PROPERTY_NAME"` | String | — | Required |
| 3 | Boundary Group Name | `"GROUP_NAME"` | String | Blank | Optional |

### 请求体示例

```json
{
  "Assign": {
    "1": { "GLINK_KEY": 1, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "Stage2" },
    "2": { "GLINK_KEY": 2, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "Stage2" }
  }
}
```

### Python 示例

```python
# --- CGLP: 更改一般连接属性 (用于按施工阶段替换属性) ---

cglp_data = {
    "Assign": {
        # 把一般连接单元 1, 2 的属性替换为 "GL_LRB_02"
        "1": {"GLINK_KEY": 1, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "PostTension"},
        "2": {"GLINK_KEY": 2, "CHANGE_PROPERTY_NAME": "GL_LRB_02", "GROUP_NAME": "PostTension"},
    }
}

midas_api("POST", "/db/CGLP", cglp_data)
```

---

## 12. `/db/FRLS` — Beam End Release

释放梁单元的端部自由度。`FLAG_I`/`FLAG_J` 是7位字符串 `[Fx, Fy, Fz, Mx, My, Mz, Mb]`，`1`=释放，`0`=连接。  
`bVALUE=true` 时，把部分固结度(Partial Fixity)数值输入到 `VALUE_I`/`VALUE_J`。

**Endpoint:** `{base url}/db/FRLS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Beam End Release (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Input Method · false=Relative, true=Value | `"bVALUE"` | Boolean | false | Optional |
| (4) | Release i-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"FLAG_I"` | String(7) | — | Required |
| (5) | Partial Fixity for i-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"VALUE_I"` | Array[Number,7] | 0 | Optional |
| (6) | Release j-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"FLAG_J"` | String(7) | — | Required |
| (7) | Partial Fixity for j-Node `[Fx,Fy,Fz,Mx,My,Mz,Mb]` | `"VALUE_J"` | Array[Number,7] | 0 | Optional |

### 请求体示例

```json
{
  "Assign": {
    "9": {
      "ITEMS": [{
        "ID": 9, "GROUP_NAME": "Service", "bVALUE": false,
        "FLAG_I": "0000100", "VALUE_I": [0, 0, 0, 0, 0, 0, 0],
        "FLAG_J": "0000100", "VALUE_J": [0, 0, 0, 0, 0, 0, 0]
      }]
    }
  }
}
```

### Python 示例

```python
# --- FRLS: 释放梁端弯矩 (模拟铰接) ---
# FLAG 代码: "0000110" → 释放 My, Mz (铰接)
# FLAG 代码: "0000010" → 仅释放 Mz (2D 销)
# FLAG 代码: "0001110" → 释放 Mx, My, Mz (完全铰)

frls_data = {
    "Assign": {
        # 梁单元9: 两端释放 My (简支梁竖直面内铰接)
        "9": {
            "ITEMS": [{
                "ID": 9,
                "GROUP_NAME": "Pin_Beam",
                "bVALUE": False,
                "FLAG_I": "0000100",   # 释放 My
                "VALUE_I": [0, 0, 0, 0, 0, 0, 0],
                "FLAG_J": "0000100",   # 释放 My
                "VALUE_J": [0, 0, 0, 0, 0, 0, 0]
            }]
        },
        # 梁单元12: i端完全销接, j端弯矩连续
        "12": {
            "ITEMS": [{
                "ID": 12,
                "GROUP_NAME": "Pin_Beam",
                "bVALUE": False,
                "FLAG_I": "0001110",   # 释放 Mx, My, Mz
                "VALUE_I": [0, 0, 0, 0, 0, 0, 0],
                "FLAG_J": "0000000",   # 完全连续
                "VALUE_J": [0, 0, 0, 0, 0, 0, 0]
            }]
        }
    }
}

midas_api("POST", "/db/FRLS", frls_data)
```

---

## 13. `/db/OFFS` — Beam End Offsets

对梁单元端部施加偏心（偏移）。按全局坐标系(GLOBAL)或单元坐标系(ELEMENT)为基准输入。

**Endpoint:** `{base url}/db/OFFS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Beam End Offsets (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Reference CS · `"GLOBAL"` / `"ELEMENT"` | `"TYPE"` | String | — | Required |
| — | **GLOBAL 专用** | | | | |
| (4) | i端 X方向偏移 (GCS) | `"RGDXi"` | Number | 0 | Optional |
| (5) | i端 Y方向偏移 (GCS) | `"RGDYi"` | Number | 0 | Optional |
| (6) | i端 Z方向偏移 (GCS) | `"RGDZi"` | Number | 0 | Optional |
| (7) | j端 X方向偏移 (GCS) | `"RGDXj"` | Number | 0 | Optional |
| (8) | j端 Y方向偏移 (GCS) | `"RGDYj"` | Number | 0 | Optional |
| (9) | j端 Z方向偏移 (GCS) | `"RGDZj"` | Number | 0 | Optional |
| — | **ELEMENT 专用** | | | | |
| (4) | i端 y方向偏移 (ECS) | `"RGDYi"` | Number | 0 | Optional |
| (5) | i端 z方向偏移 (ECS) | `"RGDZi"` | Number | 0 | Optional |
| (6) | j端 y方向偏移 (ECS) | `"RGDYj"` | Number | 0 | Optional |
| (7) | j端 z方向偏移 (ECS) | `"RGDZj"` | Number | 0 | Optional |

### 请求体示例

```json
{
  "Assign": {
    "8": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "TYPE": "GLOBAL",
        "RGDXi": 0.11, "RGDYi": 0.12, "RGDZi": 0.13,
        "RGDXj": 0.21, "RGDYj": 0.22, "RGDZj": 0.23
      }]
    },
    "7": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "TYPE": "ELEMENT",
        "RGDYi": 0.11, "RGDZi": 0.12, "RGDYj": 0.21, "RGDZj": 0.22
      }]
    }
  }
}
```

### Python 示例

```python
# --- OFFS: 梁端偏移 (楼板·主梁偏心建模) ---

offs_data = {
    "Assign": {
        # 单元5: 反映楼板与主梁中性轴之差 (单元坐标系)
        # z方向偏移 0.15m (楼板上端 - 主梁中性轴距离)
        "5": {
            "ITEMS": [{
                "ID": 5,
                "GROUP_NAME": "Slab_Offset",
                "TYPE": "ELEMENT",
                "RGDYi": 0.0,
                "RGDZi": 0.15,  # m 单位, 楼板-主梁偏心
                "RGDYj": 0.0,
                "RGDZj": 0.15
            }]
        }
    }
}

midas_api("POST", "/db/OFFS", offs_data)
```

---

## 14. `/db/PRLS` — Plate End Release

释放板单元各节点位置处的自由度。N1∼N4 是板各顶点的节点，数组值 `1`=释放，`0`=连接。  
数组顺序: `[Fx, Fy, Fz, Mx, My]`

**Endpoint:** `{base url}/db/PRLS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Plate End Release (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | Position N1 `[Fx,Fy,Fz,Mx,My]` · 1=释放 | `"N1"` | Array[Integer,5] | — | Required |
| (4) | Position N2 `[Fx,Fy,Fz,Mx,My]` | `"N2"` | Array[Integer,5] | — | Required |
| (5) | Position N3 `[Fx,Fy,Fz,Mx,My]` | `"N3"` | Array[Integer,5] | — | Required |
| (6) | Position N4 `[Fx,Fy,Fz,Mx,My]` | `"N4"` | Array[Integer,5] | — | Required |

### 请求体示例

```json
{
  "Assign": {
    "21": {
      "ITEMS": [{
        "ID": 21, "GROUP_NAME": "Service",
        "N1": [1, 0, 1, 0, 1],
        "N2": [1, 0, 1, 0, 1],
        "N3": [1, 0, 1, 0, 1],
        "N4": [1, 0, 1, 0, 1]
      }]
    }
  }
}
```

### Python 示例

```python
# --- PRLS: 板端释放 ---
# N1~N4: 按板单元4个节点的顺序指定释放条件
# [Fx, Fy, Fz, Mx, My] = 1 即释放

prls_data = {
    "Assign": {
        "21": {
            "ITEMS": [{
                "ID": 21,
                "GROUP_NAME": "Slab_Release",
                "N1": [0, 0, 0, 0, 0],  # 完全连续
                "N2": [0, 0, 0, 0, 0],
                "N3": [0, 0, 0, 0, 1],  # 释放 My
                "N4": [0, 0, 0, 0, 1]   # 释放 My
            }]
        }
    }
}

midas_api("POST", "/db/PRLS", prls_data)
```

---

## 15. `/db/MLFC` — Force-Deformation Function

定义被 Elastic Link (MULTILINEAR) 或 General Link (FORCE 类型) 参照的非线性力-位移函数。

**Endpoint:** `{base url}/db/MLFC`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Function Name | `"NAME"` | String | — | Required |
| 2 | Type · `"FORCE"` (力-位移) / `"MOMENT"` (弯矩-转角) | `"TYPE"` | String | `"MOMENT"` | Optional |
| 3 | Symmetric · true=对称, false=非对称 | `"SYMM"` | Boolean | false | Optional |
| 4 | Function ID | `"FUNC_ID"` | Integer | 0 | Optional |
| 5 | Function Data (X=位移/转角, Y=力/弯矩) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | X-Axis (Displacement m / Radian) | `"X"` | Number | — | Required |
| (2) | Y-Axis (Force kN / Moment kN·m) | `"Y"` | Number | — | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "NAME": "Force_Deform_Isolator",
      "TYPE": "FORCE", "SYMM": false, "FUNC_ID": 0,
      "ITEMS": [
        { "X": -0.20, "Y": -1200 },
        { "X": -0.05, "Y": -500 },
        { "X":  0.00, "Y":    0 },
        { "X":  0.05, "Y":  500 },
        { "X":  0.20, "Y": 1200 }
      ]
    },
    "2": {
      "NAME": "Moment_Radian_Hinge",
      "TYPE": "MOMENT", "SYMM": true, "FUNC_ID": 0,
      "ITEMS": [
        { "X": 0.00, "Y":    0 },
        { "X": 0.01, "Y":  500 },
        { "X": 0.03, "Y":  800 },
        { "X": 0.10, "Y":  900 }
      ]
    }
  }
}
```

### Python 示例

```python
# --- MLFC: 定义力-位移函数 ---
# ELNK MULTILINEAR 类型或 NLLP FORCE 类型会参照 MLFC ID

mlfc_data = {
    "Assign": {
        "1": {
            "NAME": "Bilinear_Isolator_FD",
            "TYPE": "FORCE",
            "SYMM": False,          # 非对称 (拉/压不同时)
            "FUNC_ID": 0,
            "ITEMS": [
                {"X": -0.200, "Y": -1200.0},   # 最大压缩
                {"X": -0.050, "Y":  -300.0},   # 屈服前
                {"X":  0.000, "Y":     0.0},   # 原点
                {"X":  0.050, "Y":   300.0},   # 屈服后
                {"X":  0.200, "Y":  1200.0}    # 最大拉伸
            ]
        }
    }
}

midas_api("POST", "/db/MLFC", mlfc_data)
```

---

## 16. `/db/SDVI` — Seismic Device – Viscous/Oil Damper

定义抗震用粘滞阻尼器(Viscous Damper)或油阻尼器(Oil Damper)的物性。  
由 NLLP 的 `APPLICATION_TYPE_D="VI"` 参照。

**Endpoint:** `{base url}/db/SDVI`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 必填 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| (1) | Name | `"NAME"` | String | Required |
| (2) | Description | `"DESC"` | String | Optional |
| (3) | Input Method · 0=用户输入, 1=参照 DB | `"INPUT_METHOD"` | Integer | Required |
| (4) | Company | `"COMPANY"` | String | Required |
| (5) | Product Name | `"PRODUCT_NAME"` | String | Required |
| (6) | Type Number | `"TYPE_NUMBER"` | String | Required |
| 2 | Device Type | `"DEVICE_TYPE"` | String | Optional |
| 3 | Damper Model · 0=Single Dashpot, 1=Kelvin(Voigt), 2=Maxwell | `"DAMPER_TYPE"` | Integer | Required |
| 4 | Dashpot Type · 0=Linear Elastic, 1=Bilinear, 2=Exponential | `"DASHPOT_TYPE"` | Integer | Required |
| 5 | Input Type · 0=阻尼比 α₁, 1=阻尼常数 C₁ | `"INPUT_TYPE"` | Integer | Required |
| 6 | Input Type (供 Exponential Function Type 使用) | `"INPUT_TYPE_EXFN"` | Integer | Required |
| 7 | Property Data (按 DOF 6个条目) | `"ITEM"` | Array[Object,6] | Required |
| (1) | 是否启用 DOF | `"OPT_DOF"` | Boolean | Required |
| (2) | 初始阻尼系数 CE | `"CE"` | Number | Required |
| (3) | 最大阻尼力 P₁ | `"P1"` | Number | Required |
| (4) | 二次阻尼系数 C₁ | `"C1"` | Number | Required |
| (5) | 阻尼折减系数 α₁ | `"ALPHA1"` | Number | Required |
| (6) | 初始刚度 K₀ | `"K0"` | Number | Required |
| (7) | 阻尼力(Exponential, Damping Force) | `"EXFN_PY"` | Number | Required |
| (8) | 基准速度(Exponential, Reference Velocity) | `"EXFN_VY"` | Number | Required |
| (9) | 阻尼指数(Exponential, Damping Exponent) | `"EXFN_DE"` | Number | Required |
| (10) | 阻尼系数(Exponential, Damping Coefficient) | `"EXFN_DC"` | Number | Required |
| (11) | 是否使用 Exponential 初始阻尼系数 | `"OPT_EXFN_CE"` | Boolean | Required |
| (12) | Exponential 初始阻尼系数值 | `"EXFN_CE"` | Number | Required |

> ⚠️ **2026-08-25 复核补强：** 遗漏了 `INPUT_TYPE_EXFN`(最上级)和 `ITEM[]` 的 (7)~(12) 6个
> Exponential Function Type(`DASHPOT_TYPE=2`) 专用字段。查看原文 Request
> Example 可见，与 `DASHPOT_TYPE` 取值无关，`ITEM[]` 的每个元素始终包含全部12个字段
> 一并发送（article id `35947995586713`）。

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "ViscousDamper_D01", "DESC": "",
        "INPUT_METHOD": 0, "COMPANY": "", "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 0,
      "INPUT_TYPE": 0,
      "INPUT_TYPE_EXFN": 0,
      "ITEM": [
        { "OPT_DOF": true, "CE": 13000, "P1": 0, "C1": 0, "ALPHA1": 0, "K0": 0,
          "EXFN_PY": 1, "EXFN_VY": 1, "EXFN_DE": 0.3, "EXFN_DC": 1,
          "OPT_EXFN_CE": false, "EXFN_CE": 1 },
        { "OPT_DOF": false, "CE": 0, "P1": 0, "C1": 0, "ALPHA1": 0, "K0": 0,
          "EXFN_PY": 1, "EXFN_VY": 1, "EXFN_DE": 0.3, "EXFN_DC": 1,
          "OPT_EXFN_CE": false, "EXFN_CE": 1 }
      ]
    }
  }
}
```

### Python 示例

```python
# --- SDVI: 定义粘滞阻尼器物性 ---
# ITEM 数组顺序: Dx, Dy, Dz, Rx, Ry, Rz
# 与 DASHPOT_TYPE 取值无关, ITEM 的每个元素都必须发送全部12个字段

def make_dof_item(active, CE=0, P1=0, C1=0, alpha1=1.0, K0=0,
                   exfn_py=1, exfn_vy=1, exfn_de=0.3, exfn_dc=1,
                   opt_exfn_ce=False, exfn_ce=1):
    return {
        "OPT_DOF": active, "CE": CE, "P1": P1, "C1": C1, "ALPHA1": alpha1, "K0": K0,
        "EXFN_PY": exfn_py, "EXFN_VY": exfn_vy, "EXFN_DE": exfn_de, "EXFN_DC": exfn_dc,
        "OPT_EXFN_CE": opt_exfn_ce, "EXFN_CE": exfn_ce
    }

sdvi_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "OilDamper_500kN",
                "DESC": "Seismic Oil Damper 500kN",
                "INPUT_METHOD": 0,
                "COMPANY": "SUMITOMO",
                "PRODUCT_NAME": "OD-500",
                "TYPE_NUMBER": "OD500-A"
            },
            "DEVICE_TYPE": "",
            "DAMPER_TYPE": 2,       # Maxwell 模型
            "DASHPOT_TYPE": 2,      # 指数函数类型
            "INPUT_TYPE": 0,        # 阻尼比 α₁ 输入
            "INPUT_TYPE_EXFN": 0,
            "ITEM": [
                make_dof_item(True,  CE=500, P1=1000, C1=200, alpha1=0.5),  # Dx 激活
                make_dof_item(False),   # Dy 非激活
                make_dof_item(False),   # Dz
                make_dof_item(False),   # Rx
                make_dof_item(False),   # Ry
                make_dof_item(False),   # Rz
            ]
        }
    }
}

midas_api("POST", "/db/SDVI", sdvi_data)
```

---

## 17. `/db/SDVE` — Seismic Device – Viscoelastic Damper

定义粘弹性阻尼器(Viscoelastic Damper)的物性。  
由 NLLP 的 `APPLICATION_TYPE_D="VE"` 参照。

**Endpoint:** `{base url}/db/SDVE`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核全面补强。** 旧版本只有 `COMMON`/`MATERIAL_TYPE`/`SHEAR_AREA` 3个
> 字段，但原文（article id `35948062417049`）的实际 Request Example 还额外发送了下列14个
> 字段 —— 只看表无从得知，只能通过 Request Example 确认。

| No. | 说明 | Key | 类型 | 必填 |
|-----|------|----|------|------|
| 1 | Common Data (与 SDVI 结构相同) | `"COMMON"` | Object | Required |
| 2 | Material Type · `"GR100"` / `"GR300"` / `"SR05"` / `"GR400"` / `"CST"` / `"TRC"` | `"MATERIAL_TYPE"` | String | Required |
| 3 | Shear Area | `"SHEAR_AREA"` | Number | Required |
| 4 | Thickness | `"THICKNESS"` | Number | Required |
| 5 | Multiplier | `"MULTIPL"` | Number | Required |
| 6 | Direction(`"Dx"`/`"Dy"`/`"Dz"` 等) | `"DIR"` | String | Required |
| 7 | Frequency | `"FREQ"` | Number | Required |
| 8 | Stiffness Factor | `"STIFF_FACTOR"` | Number | Required |
| 9 | Damping Factor | `"DAMP_FACTOR"` | Number | Required |
| 10 | Reference Temperature | `"REF_T"` | Number | Required |
| 11 | Limit Deformation | `"LIMIT_DEF"` | Number | Required |
| 12 | Effective Stiffness | `"EFF_STIFF"` | Number | Required |
| 13 | Equivalent Damping | `"EQUI_DAMP"` | Number | Required |
| 14 | Use Mount Stiffness | `"OPT_MOUNT_STIFF"` | Boolean | Required |
| 15 | Mount Stiffness | `"MOUNT_STIFF"` | Number | Required |
| 16 | Use Kinetic Friction | `"OPT_KINETIC_FRIC"` | Boolean | Required |
| 17 | Kinetic Friction | `"KINETIC_FRIC"` | Number | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "Viscoelastic01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "GR100",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dx",
      "FREQ": 0,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.3,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 1200,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    }
  }
}
```

### Python 示例

```python
# --- SDVE: 定义粘弹性阻尼器物性 ---

sdve_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "VE_Damper_GR100",
                "DESC": "Viscoelastic Damper - SUMITOMO GR100",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "GR100-Series",
                "TYPE_NUMBER": "GR100-200"
            },
            "MATERIAL_TYPE": "GR100",   # SUMITOMO GR100 材料
            "SHEAR_AREA": 0.2,          # 剪切面积 (m²)
            "THICKNESS": 0.02,          # 厚度 (m)
            "MULTIPL": 1,               # 倍数(层叠数量等)
            "DIR": "Dx",
            "FREQ": 0,
            "STIFF_FACTOR": 1,
            "DAMP_FACTOR": 1,
            "REF_T": 20,                # 基准温度 (°C)
            "LIMIT_DEF": 0.3,           # 极限变形
            "EFF_STIFF": 0,
            "EQUI_DAMP": 0,
            "OPT_MOUNT_STIFF": True,
            "MOUNT_STIFF": 1200,
            "OPT_KINETIC_FRIC": False,
            "KINETIC_FRIC": 0
        }
    }
}

midas_api("POST", "/db/SDVE", sdve_data)
```

---

## 18. `/db/SDST` — Seismic Device – Steel Damper

定义钢材阻尼器(Steel Damper)的物性。  
由 NLLP 的 `APPLICATION_TYPE_D="ST"` 参照。

**Endpoint:** `{base url}/db/SDST`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核全面更正。** 原文 Specifications 表把本 Endpoint 写为存在
> `MATERIAL_TYPE`（SUMITOMO GR100 等）·`MULTIPL` 字段，但这**应是第17节 SDVE（粘弹性
> 阻尼器）页面的内容误混入** —— 无论 JSON Schema 还是实际 Request
> Example 中都没有 `MATERIAL_TYPE`。实际使用的是 `K0`/`P1`/`ALPHA1`/`KB` 以及按
> 滞后模型区分的下级对象（`BL2`/`LY2`/`LY3`/`IK2`）（article id `35948150053529`, 错误举报对象）。

| No. | 说明 | Key | 类型 | 必填 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Direction | `"DIR"` | String | Required |
| 3 | Hysteresis Model · Degrading Bilinear: `"BL2"` / Low Yielding Steel(LY2): `"LY2"` / Low Yielding Steel(LY3): `"LY3"` / Isotropic-Kinematic(IK2): `"IK2"` | `"SDST_HYS_MODEL"` | String | Required |
| 4 | Initial Stiffness (K0) | `"K0"` | Number | Required |
| 5 | Yield Strength (P1) | `"P1"` | Number | Required |
| 6 | Stiffness Factor (α1) | `"ALPHA1"` | Number | Required |
| 7 | Mounting Parts Stiffness (Kb) | `"KB"` | Number | Required |

#### 按 `SDST_HYS_MODEL` 的下级对象

| Model | Key | 下级字段 |
| --- | --- | --- |
| `"BL2"` | `"BL2"` | `BETA`(Exponent in Unloading Stiffness Calculation) |
| `"LY2"` | `"LY2"` | `ALPHA2`(Stiffness Factor), `THETA`(Strength Factor) |
| `"LY3"` | `"LY3"` | `ALPHA2`, `THETA`, `GAMMA`(Stiffness Ratio) |
| `"IK2"` | `"IK2"` | `GAMMA`(Isotropic Factor) |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "SteelDamper01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "BL2",
      "K0": 1000,
      "P1": 100,
      "ALPHA1": 0.2,
      "KB": 2000,
      "BL2": { "BETA": 0 }
    }
  }
}
```

### Python 示例

```python
# --- SDST: 定义钢材阻尼器物性 ---

sdst_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "SteelDamper_Dx_300kN",
                "DESC": "Steel Damper 300kN Bilinear",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "SD-300",
                "TYPE_NUMBER": "SD300-B"
            },
            "DIR": "Dx",
            "SDST_HYS_MODEL": "BL2",     # Degrading Bilinear 滞后模型
            "K0": 1000,                  # 初始刚度
            "P1": 100,                   # 屈服强度
            "ALPHA1": 0.2,               # 刚度系数
            "KB": 2000,                  # 安装部件刚度
            "BL2": {"BETA": 0}           # BL2 模型专用参数
        }
    }
}

midas_api("POST", "/db/SDST", sdst_data)
```

---

## 19. `/db/SDHY` — Seismic Device – Hysteretic Isolator (MSS)

定义滞后型隔震装置（多剪切弹簧模型, MSS）的物性。  
由 NLLP 的 `APPLICATION_TYPE_D="HY"` 参照。

**Endpoint:** `{base url}/db/SDHY`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核补强。** 遗漏了 `P1`/`P2`/`ALPHA1`/`ALPHA2`/`BETA`/`Phi`/`LAMBDA` 7个
> 字段（article id `35948292269977`）。原文表中另有 `MULTIPL`(Multiplier)，但在 JSON Schema·Request Example 中
> 均未出现（判断为与 SDST/SDVE 表中反复发现的同类原文错误），故未列入下表。

| No. | 说明 | Key | 类型 | 必填 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Hysteresis Model · `"DegradingBiLinear"` 等 | `"SDHY_HYS_MODEL"` | String | Required |
| 3 | Number of Shear Springs (MSS 剪切弹簧数量) | `"MSS"` | Integer | Required |
| 4 | K0 Initial Stiffness | `"K0"` | Number | Required |
| 5 | P1 Yield Strength | `"P1"` | Number | Required |
| 6 | P2 Yield Strength | `"P2"` | Number | Required |
| 7 | Alpha1 Stiffness Factor | `"ALPHA1"` | Number | Required |
| 8 | Alpha2 Stiffness Factor | `"ALPHA2"` | Number | Required |
| 9 | Beta(Exponent in Unloading Stiffness Calculation) | `"BETA"` | Number | Required |
| 10 | Phi | `"Phi"` | Number | Required |
| 11 | Lambda | `"LAMBDA"` | Number | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "HystereticIsolator01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "SDHY_HYS_MODEL": "DegradingBiLinear",
      "MSS": 8,
      "K0": 1000,
      "P1": 100,
      "P2": 0,
      "ALPHA1": 1,
      "ALPHA2": 0,
      "BETA": 0.5,
      "Phi": 0,
      "LAMBDA": 8
    }
  }
}
```

### Python 示例

```python
# --- SDHY: 定义滞后型隔震装置物性 ---

sdhy_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "HI_DegBilinear_500",
                "DESC": "Hysteretic Isolator - Degrading Bilinear",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "HI-500",
                "TYPE_NUMBER": "HI500-A"
            },
            "SDHY_HYS_MODEL": "DegradingBiLinear",
            "MSS": 8,           # 剪切弹簧分割数量
            "K0": 5000.0,       # 初始刚度 (kN/m)
            "P1": 100.0,        # 一次屈服强度
            "P2": 0.0,          # 二次屈服强度
            "ALPHA1": 1.0,
            "ALPHA2": 0.0,
            "BETA": 0.5,
            "Phi": 0.0,
            "LAMBDA": 8.0
        }
    }
}

midas_api("POST", "/db/SDHY", sdhy_data)
```

---

## 20. `/db/SDIS` — Seismic Device – Isolator (MSS)

定义基于 MSS 的隔震装置（铅芯橡胶 LRB / 天然橡胶 NRB / 滑动 SB）的物性。  
由 NLLP 的 `APPLICATION_TYPE_D="IS"` 参照。

**Endpoint:** `{base url}/db/SDIS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核全面更正。** 旧版本 (1) 把 `SDIS_DEV_TYPE` 的第三个值误记为 `"SB"`
> （实际为 **`"SLD"`**，只有数据对象的键是 `"SB"`），(2) 把 LRB 的 `DX`/`OPT_CONS_NONL`/
> `BETA`/`ALPHA`/`SIGMA_V` 误记为彼此同级的兄弟字段（实际是 **`DX` 作为承载
> `{OPT_CONS_NONL, BETA, ALPHA, SIGMA_V}` 的下级对象**），(3) 遗漏了 LRB 的 `KE`·`K0`（名称相近但互不相同的两个初始刚度字段）中的
> `K0`，(4) 把 NRB Data 误记为只有 `KH` 一项（实际是 `AR`/`TR`/`KH`/`DX{...}` 4+4个），(5) 遗漏了 SB Data 的 `QD`(Index)·`Pi_VALUE`。
> 已对照原文 JSON Schema + Request Example 全面重写
> （article id `35948330042649`, 错误举报对象）。

| No. | 说明 | Key | 类型 | 必填 |
|-----|------|----|------|------|
| 1 | Common Data | `"COMMON"` | Object | Required |
| 2 | Device Type · `"LRB"` / `"NRB"` / `"SLD"`(数据放入 `"SB"` 对象) | `"SDIS_DEV_TYPE"` | String | Required |
| 3 | Number of Shear Springs | `"MSS"` | Integer | Required |
| 4 | Adjustment Parameter τk | `"TAU_K"` | Number | Required |
| 5 | Adjustment Parameter τq | `"TAU_Q"` | Number | Required |
| 6 | Vertical Stiffness Kv | `"KV"` | Number | Required |
| 7 | LRB Data (`SDIS_DEV_TYPE`="LRB" 时) | `"LRB"` | Object | Required |
| 8 | NRB Data (`SDIS_DEV_TYPE`="NRB" 时) | `"NRB"` | Object | Required |
| 9 | SB Data (`SDIS_DEV_TYPE`="SLD" 时) | `"SB"` | Object | Required |

**`LRB` 对象**

| No. | 说明 | Key | 类型 | 必填 |
| --- | --- | --- | --- | --- |
| (1) | Hysteresis Model | `"SDIS_HYS_MODEL"` | String | Required |
| (2) | Initial Stiffness Ke | `"KE"` | Number | Required |
| (3) | Rubber Cross Section Area AR | `"AR"` | Number | Required |
| (4) | Total Thickness of Rubber TR | `"TR"` | Number | Required |
| (5) | Initial Stiffness K0(与 KE 是不同的字段) | `"K0"` | Number | Required |
| (6) | 2nd Stiffness K2 | `"K2"` | Number | Required |
| (7) | Characteristic Strength QD | `"QD"` | Number | Required |
| (8) | Vertical Direction Properties | `"DX"` | Object | Optional |
| (8)-i | 是否考虑竖向非线性(`DX` 下级) | `"OPT_CONS_NONL"` | Boolean | Optional |
| (8)-ii | 拉伸刚度折减系数 β(`DX` 下级) | `"BETA"` | Number | Optional |
| (8)-iii | 拉伸刚度折减比 α(`DX` 下级) | `"ALPHA"` | Number | Optional |
| (8)-iv | 拉伸极限强度(`DX` 下级) | `"SIGMA_V"` | Number | Optional |

**`NRB` 对象**

| No. | 说明 | Key | 类型 | 必填 |
| --- | --- | --- | --- | --- |
| (1) | Rubber Cross Section Area AR | `"AR"` | Number | Required |
| (2) | Total Thickness of Rubber TR | `"TR"` | Number | Required |
| (3) | Horizontal Stiffness KH | `"KH"` | Number | Required |
| (4) | Vertical Direction Properties(`DX`, 与 LRB 结构相同) | `"DX"` | Object | Optional |

**`SB` 对象**(SDIS_DEV_TYPE=`"SLD"`)

| No. | 说明 | Key | 类型 | 必填 |
| --- | --- | --- | --- | --- |
| (1) | Area of Sliding Head AS | `"AS"` | Number | Required |
| (2) | Initial Stiffness K0 | `"K0"` | Number | Required |
| (3) | Index Qd | `"QD"` | Integer | Required |
| (4) | Pi | `"Pi_VALUE"` | Number | Required |
| (5) | Frictional Factor μ0 | `"MU0"` | Number | Required |

### 请求体示例 (LRB / NRB / SLD)

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "LRB_Isolator_01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "LRB-500", "TYPE_NUMBER": "LRB500-A"
      },
      "SDIS_DEV_TYPE": "LRB", "MSS": 8,
      "TAU_K": 1.0, "TAU_Q": 1.0, "KV": 150000,
      "LRB": {
        "SDIS_HYS_MODEL": "BiLinear",
        "KE": 20000, "AR": 0.196, "TR": 0.15, "K0": 20000, "K2": 2000, "QD": 80,
        "DX": { "OPT_CONS_NONL": false, "BETA": 0.1, "ALPHA": 0.5, "SIGMA_V": 3000 }
      }
    },
    "3": {
      "COMMON": {
        "NAME": "NRB_Isolator_01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "NRB", "MSS": 8,
      "TAU_K": 1.0, "KV": 150000,
      "NRB": { "AR": 0.196, "TR": 0.15, "KH": 1200 }
    },
    "4": {
      "COMMON": {
        "NAME": "SlidingBearing_01", "DESC": "", "INPUT_METHOD": 0,
        "PRODUCT_NAME": "", "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "SLD", "MSS": 8,
      "TAU_K": 1.0, "TAU_Q": 1.0, "KV": 150000,
      "SB": { "AS": 0.05, "K0": 100000, "QD": 2, "Pi_VALUE": 0, "MU0": 0.05 }
    }
  }
}
```

### Python 示例

```python
# --- SDIS: 定义隔震装置物性 (LRB) ---
# LRB: Lead Rubber Bearing (铅芯橡胶支座)
# 铅芯橡胶支座是非线性时程分析中不可或缺的隔震装置

sdis_lrb_data = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "LRB_500kN",
                "DESC": "Lead Rubber Bearing 500kN",
                "INPUT_METHOD": 0,
                "PRODUCT_NAME": "LRB-500",
                "TYPE_NUMBER": "LRB500-Standard"
            },
            "SDIS_DEV_TYPE": "LRB",
            "MSS": 8,               # 剪切弹簧分割数量
            "TAU_K": 1.0,           # 刚度修正系数
            "TAU_Q": 1.0,           # 屈服力修正系数
            "KV": 150000.0,         # 竖向刚度 (kN/m)
            "LRB": {
                "SDIS_HYS_MODEL": "BiLinear",   # 滞后模型
                "KE": 20000.0,  # 初始刚度 Ke (kN/m)
                "AR": 0.196,    # 橡胶截面积 (m²)
                "TR": 0.150,    # 橡胶总厚度 (m)
                "K0": 20000.0,  # 初始刚度 K0 (与 KE 是不同的字段, kN/m)
                "K2": 2000.0,   # 二次刚度 (kN/m)
                "QD": 80.0,     # 特性强度 (kN)
                "DX": {                  # 竖向特性(可选)
                    "OPT_CONS_NONL": False,
                    "BETA": 0.1,
                    "ALPHA": 0.5,
                    "SIGMA_V": 3000.0    # 拉伸强度极限 (kN/m²)
                }
            }
        }
    }
}

midas_api("POST", "/db/SDIS", sdis_lrb_data)
```

---

## 21. `/db/MCON` — Linear Constraints

设置节点间的线性从属约束条件（等位移、加权位移等）。  
`SLAVE_TYPE` 6位按 `[DX,DY,DZ,RX,RY,RZ]` 顺序，`1`=约束启用。

**Endpoint:** `{base url}/db/MCON`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

> ⚠️ **2026-08-25 复核更正。** `SLAVES[]` 的字段依 `TYPE` 而不同 —— 旧版本把两种
> 类型都误记为使用 `COEFF`，但实际是 **只有 `"EX"` 使用 `COEFF`+`DOF`
> 组合**（每个元素单独指定 DOF），**`"WD"` 只使用 `WEIGHT"` 一项**（article id
> `35948507217689`）。

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Linear Constraints (以数组形式插入) | `"ITEMS"` | Array[Object] | — | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (3) | DOF of Constraint Node (6位: DX∼RZ) | `"SLAVE_TYPE"` | String(6) | — | Required |
| (4) | Constraint Type · `"EX"`=Explicit, `"WD"`=Weighted Displacement | `"TYPE"` | String | — | Required |
| (5) | Independent Nodes | `"SLAVES"` | Array[Object] | — | Required |

**`TYPE="EX"`(Explicit) 时的 `SLAVES[]`**

| No. | 说明 | Key | 类型 | 必填 |
| --- | --- | --- | --- | --- |
| i | Node ID | `"NODE_KEY"` | Integer | Required |
| ii | Coefficient | `"COEFF"` | Number | Required |
| iii | Degree of Freedom · DX:0/DY:1/DZ:2/RX:3/RY:4/RZ:5 | `"DOF"` | Integer | Required |

**`TYPE="WD"`(Weighted Displacement) 时的 `SLAVES[]`**

| No. | 说明 | Key | 类型 | 必填 |
| --- | --- | --- | --- | --- |
| i | Node ID | `"NODE_KEY"` | Integer | Required |
| ii | Weight | `"WEIGHT"` | Number | Required |

### 请求体示例

```json
{
  "Assign": {
    "21": {
      "ITEMS": [{
        "ID": 1, "GROUP_NAME": "Service", "SLAVE_TYPE": "100000",
        "TYPE": "EX",
        "SLAVES": [
          { "NODE_KEY": 22, "COEFF": 0.5, "DOF": 0 },
          { "NODE_KEY": 23, "COEFF": 0.5, "DOF": 1 }
        ]
      }]
    }
  }
}
```

### Python 示例

```python
# --- MCON: 线性约束条件 (楼层隔板约束的替代方案) ---
# EX 类型: 用 NODE_KEY+COEFF+DOF 组合实现等位移/加权约束 (DOF 按元素单独指定)
# WD 类型: 仅使用 NODE_KEY+WEIGHT (坡屋顶、不规则结构等)

mcon_data = {
    "Assign": {
        # 将节点5、10的 DX 位移按相同值约束
        "1": {
            "ITEMS": [{
                "ID": 1,
                "GROUP_NAME": "Diaphragm_Constraint",
                "SLAVE_TYPE": "100000",   # 仅激活 DX
                "TYPE": "EX",
                "SLAVES": [
                    {"NODE_KEY": 5,  "COEFF":  1.0, "DOF": 0},
                    {"NODE_KEY": 10, "COEFF": -1.0, "DOF": 0}
                ]
            }]
        },
        # 加权位移约束 (WD): D_node5 = 0.5 * D_node10 + 0.5 * D_node15
        "2": {
            "ITEMS": [{
                "ID": 2,
                "GROUP_NAME": "Weighted_Constraint",
                "SLAVE_TYPE": "110001",   # DX, DY, RZ
                "TYPE": "WD",
                "SLAVES": [
                    {"NODE_KEY": 10, "WEIGHT": 0.5},
                    {"NODE_KEY": 15, "WEIGHT": 0.5}
                ]
            }]
        }
    }
}

midas_api("POST", "/db/MCON", mcon_data)
```

---

## 22. `/db/PZEF` — Panel Zone Effects

设置梁-柱节点域的 Panel Zone（面板区）变形效应。

**Endpoint:** `{base url}/db/PZEF`  
**Methods:** `POST` · `GET` · `PUT`  
*(不支持 DELETE)*

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Auto Calculate Panel Zone Offset Distances | `"OPT_OFFSET"` | Boolean | — | Required |
| 2 | Offset Factor | `"OFFS_FACTOR"` | Number | — | Required |
| 3 | Output Position | `"OUTPUT_POSITION"` | Integer | — | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {
      "OPT_OFFSET": true,
      "OFFS_FACTOR": 1.0,
      "OUTPUT_POSITION": 1
    }
  }
}
```

### Python 示例

```python
# --- PZEF: 设置面板区效应 ---
# 在梁-柱节点域使用刚体偏移自动计算

pzef_data = {
    "Assign": {
        "1": {
            "OPT_OFFSET": True,     # 使用自动计算
            "OFFS_FACTOR": 1.0,     # 偏移系数 (1.0 = 全部适用)
            "OUTPUT_POSITION": 1    # 结果输出位置
        }
    }
}

# 设置面板区效应 (项目全局设置)
midas_api("POST", "/db/PZEF", pzef_data)

# 查询当前设置
current_pzef = midas_api("GET", "/db/PZEF")

# 修改设置
pzef_data["Assign"]["1"]["OFFS_FACTOR"] = 0.8
midas_api("PUT", "/db/PZEF", pzef_data)
```

---

## 23. `/db/CLDR` — Define Constraints Label Direction

按节点指定约束条件标签的显示方向。

**Endpoint:** `{base url}/db/CLDR`  
**Methods:** `POST` · `GET` · `PUT`  
*(不支持 DELETE)*

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Constraint Label Direction | `"DIR"` | Integer | — | Required |

**DIR 取值:**

| 值 | 方向 |
|----|------|
| 0 | Local x (+) |
| 1 | Local x (–) |
| 2 | Local y (+) |
| 3 | Local y (–) |
| 4 | Local z (+) |
| 5 | Local z (–) |

### 请求体示例

```json
{
  "Assign": {
    "53": { "DIR": 0 },
    "55": { "DIR": 1 },
    "57": { "DIR": 2 },
    "59": { "DIR": 3 },
    "61": { "DIR": 4 },
    "63": { "DIR": 5 }
  }
}
```

### Python 示例

```python
# --- CLDR: 设置约束标签方向 ---
# 键: 节点 ID, 值: DIR(0~5)

cldr_data = {
    "Assign": {
        "10": {"DIR": 4},   # 以 Local z (+) 方向显示标签
        "11": {"DIR": 4},
        "12": {"DIR": 4},
        "20": {"DIR": 0},   # Local x (+) 方向
    }
}

midas_api("POST", "/db/CLDR", cldr_data)
```

---

## 24. `/db/DRLS` — Diaphragm Disconnect

把特定节点从隔板中排除（解除）。  
`Assign` 的键是**节点 ID**，值是空对象 `{}`。

**Endpoint:** `{base url}/db/DRLS`  
**Methods:** `POST` · `GET` · `PUT` · `DELETE`

### 请求参数

| No. | 说明 | Key | 类型 | 默认值 | 必填 |
|-----|------|----|------|--------|------|
| 1 | Assign Object · 键=节点编号, 值=空对象 | `"Assign"` | Object | `{}` | Required |

### 请求体示例

```json
{
  "Assign": {
    "1": {},
    "2": {},
    "5": {}
  }
}
```

### Python 示例

```python
# --- DRLS: 隔板解除 ---
# 以要从隔板分离的节点 ID 作为键
# 例: 将竖向构件、核心筒连接节点等从隔板中排除

drls_data = {
    "Assign": {
        "5": {},    # 将节点5从隔板解除
        "12": {},   # 解除节点12
        "18": {},   # 解除节点18
    }
}

# 登记隔板解除节点
midas_api("POST", "/db/DRLS", drls_data)

# 查询当前解除列表
current_drls = midas_api("GET", "/db/DRLS")

# 取消特定节点(ID=5)的解除
midas_api("DELETE", "/db/DRLS", {"Assign": {"5": {}}})
```

---

## 完整 Boundary 设置示例 (工作流)

下面是在一般 RC 建筑模型中按顺序输入 Boundary 数据的实务示例。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    r = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{r.status_code}] {method.upper()} {endpoint}")
    return r.json() if r.text else {}

# ── STEP 1: 输入支承条件 ──────────────────────────────────────
# 1层柱底部节点(1~4)完全固定
cons_data = {
    "Assign": {
        str(n): {
            "ITEMS": [{"ID": n, "GROUP_NAME": "Foundation", "CONSTRAINT": "1111111"}]
        }
        for n in range(1, 5)
    }
}
midas_api("POST", "/db/CONS", cons_data)

# ── STEP 2: 定义力-位移函数 (供非线性连接使用) ────────────────────
mlfc_data = {
    "Assign": {
        "1": {
            "NAME": "Isolator_FD",
            "TYPE": "FORCE", "SYMM": True, "FUNC_ID": 0,
            "ITEMS": [
                {"X": 0.00, "Y":    0},
                {"X": 0.05, "Y":  300},
                {"X": 0.15, "Y":  500},
                {"X": 0.30, "Y":  600}
            ]
        }
    }
}
midas_api("POST", "/db/MLFC", mlfc_data)

# ── STEP 3: 刚体连接 (楼层隔板) ────────────────────────────
rigd_data = {
    "Assign": {
        "100": {
            "ITEMS": [{
                "ID": 100,
                "GROUP_NAME": "Floor_Diaphragm",
                "DOF": 110001,           # DX, DY, RZ 约束
                "S_NODE": list(range(5, 25))  # 5∼24 号 Slave 节点
            }]
        }
    }
}
midas_api("POST", "/db/RIGD", rigd_data)

# ── STEP 4: 梁端释放 (铰接梁) ────────────────────────────
frls_data = {
    "Assign": {
        str(eid): {
            "ITEMS": [{
                "ID": eid,
                "GROUP_NAME": "Pin_Beams",
                "bVALUE": False,
                "FLAG_I": "0000110",   # 释放 My, Mz
                "VALUE_I": [0]*7,
                "FLAG_J": "0000110",
                "VALUE_J": [0]*7
            }]
        }
        for eid in [101, 102, 103, 104]
    }
}
midas_api("POST", "/db/FRLS", frls_data)

# ── STEP 5: 面板区效应 ──────────────────────────────────────
midas_api("POST", "/db/PZEF", {
    "Assign": {"1": {"OPT_OFFSET": True, "OFFS_FACTOR": 1.0, "OUTPUT_POSITION": 1}}
})

print("Boundary 设置完成")
```

---

> **[05_DB_Boundary.md] 已完成 — 下一个文件 [06_DB_Static_Loads.md] 已可开始推进。**
