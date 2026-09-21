# DB – Temperature / Prestress

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:** `https://moa-engineers.midasit.com:443/gen`  
> **认证：** 所有请求必须携带 `MAPI-Key: <key>` 头部  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../07_DB_Temperature_Prestress.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | [/db/ETMP](#1-dbetmp--element-temperature) | Element Temperature |
| 2 | [/db/GTMP](#2-dbgtmp--temperature-gradient) | Temperature Gradient |
| 3 | [/db/BTMP](#3-dbbtmp--beam-section-temperature) | Beam Section Temperature |
| 4 | [/db/STMP](#4-dbstmp--system-temperature) | System Temperature |
| 5 | [/db/NTMP](#5-dbntmp--nodal-temperature) | Nodal Temperature |
| 6 | [/db/TDNT](#6-dbtdnt--tendon-property) | Tendon Property |
| 7 | [/db/TDNA](#7-dbtdna--tendon-profile) | Tendon Profile |
| 8 | [/db/TDCS](#8-dbtdcs--tendon-location-for-composite-section) | Tendon Location for Composite Section |
| 9 | [/db/TDPL](#9-dbtdpl--tendon-prestress) | Tendon Prestress |
| 10 | [/db/PRST](#10-dbprst--prestress-beam-loads) | Prestress Beam Loads |
| 11 | [/db/PTNS](#11-dbptns--pretension-loads) | Pretension Loads |
| 12 | [/db/EXLD](#12-dbexld--external-type-load-case-for-pretension) | External Type Load Case for Pretension |

---

## 通用 Python 辅助函数

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

## 1. /db/ETMP — Element Temperature

> 对单元（Element）施加均温荷载。键（key）为 **单元编号**，可通过 `ITEMS` 数组同时输入多个荷载工况。

**Input URI:** `{base url}/db/ETMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TEMP": 35
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TEMP": -20
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Element Temperature（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Temperature | `"TEMP"` | Number | - | Required |

### Python 示例

```python
# 施加单元温度荷载（POST）
# 键 = 单元编号，通过 ITEMS 数组可同时输入多个荷载工况
etmp_data = {
    "Assign": {
        "1": {   # 单元 1
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMP": 35},
                {"ID": 2, "LCNAME": "Temp(-)", "GROUP_NAME": "", "TEMP": -20},
            ]
        },
        "5": {   # 单元 5
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMP": 35},
            ]
        },
    }
}
result = midas_api("POST", "/db/ETMP", etmp_data)

# 查询全部（GET）
all_etmp = midas_api("GET", "/db/ETMP")

# 修改（PUT）
update_data = {
    "Assign": {
        "1": {"ITEMS": [{"ID": 1, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMP": 40}]}
    }
}
midas_api("PUT", "/db/ETMP", update_data)

# 删除（DELETE）
midas_api("DELETE", "/db/ETMP", {"Assign": {"1": {}}})
```

---

## 2. /db/GTMP — Temperature Gradient

> 对梁（Beam）或板（Plate）单元施加温度梯度荷载。梁单元可同时指定 z 方向与 y 方向梯度。

**Input URI:** `{base url}/db/GTMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

**Beam 类型示例：**

```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TYPE": 1,
          "TZ": 10,
          "USE_HZ": true,
          "TY": -10,
          "USE_HY": true
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TYPE": 1,
          "TZ": 10,
          "USE_HZ": false,
          "HZ": 1.2,
          "TY": -10,
          "USE_HY": false,
          "HY": 0.5
        }
      ]
    }
  }
}
```

**Plate 类型示例：**

```json
{
  "Assign": {
    "21": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TYPE": 2,
          "TZ": 10,
          "USE_HZ": true
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TYPE": 2,
          "TZ": 10,
          "USE_HZ": false,
          "HZ": 0.2
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Temperature Gradient（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Element Type · Beam: `1` · Plate: `2` | `"TYPE"` | Integer | - | Required |
| (5) | T2z − T1z | `"TZ"` | Number | - | Required |
| (6) | Use Section Hz | `"USE_HZ"` | Boolean | `false` | Optional |
| (7) | Hz value（`USE_HZ` = false 时使用） | `"HZ"` | Number | - | Optional |
| (8) | T2y − T1y（仅 Beam 类型） | `"TY"` | Number | - | Required (Beam) |
| (9) | Use Section Hy（仅 Beam 类型） | `"USE_HY"` | Boolean | `false` | Optional |
| (10) | Hy value（`USE_HY` = false 时使用，仅 Beam） | `"HY"` | Number | - | Optional |

### Python 示例

```python
# 对梁单元施加温度梯度（POST）
gtmp_beam = {
    "Assign": {
        "2": {   # 单元 2（梁）
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(+)",
                    "GROUP_NAME": "",
                    "TYPE": 1,      # Beam
                    "TZ": 10,       # z 方向温度差 (T2z - T1z)
                    "USE_HZ": True, # 使用截面 Hz
                    "TY": -10,      # y 方向温度差 (T2y - T1y)
                    "USE_HY": True, # 使用截面 Hy
                },
            ]
        }
    }
}
midas_api("POST", "/db/GTMP", gtmp_beam)

# 对板单元施加温度梯度（POST）
gtmp_plate = {
    "Assign": {
        "21": {   # 单元 21（板）
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(+)",
                    "GROUP_NAME": "",
                    "TYPE": 2,       # Plate
                    "TZ": 10,
                    "USE_HZ": False,
                    "HZ": 0.2,       # 直接输入 Hz
                },
            ]
        }
    }
}
midas_api("POST", "/db/GTMP", gtmp_plate)
```

---

## 3. /db/BTMP — Beam Section Temperature

> 分段定义梁截面的温度分布。支持一般截面（General）与 PSC/组合截面（PSC/Composite）两种模式。

**Input URI:** `{base url}/db/BTMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

> ⚠️ MIDAS Civil NX 专用功能

### 请求体结构

**General – 自动引用截面材料 (Elements)：**

```json
{
  "Assign": {
    "51": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Centroid",
          "NUM": 1,
          "bPSC": false,
          "vSECTTMP": [
            {
              "TYPE": "ELEMENT",
              "VAL_B": 0.2,
              "VAL_H1": 0.1,
              "VAL_H2": 0.2,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
          ]
        }
      ]
    }
  }
}
```

**General – 直接输入材料 (User Input)：**

```json
{
  "Assign": {
    "51": {
      "ITEMS": [
        {
          "ID": 2,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Centroid",
          "NUM": 1,
          "bPSC": false,
          "vSECTTMP": [
            {
              "TYPE": "INPUT",
              "ELAST": 34800000,
              "THERMAL": 1e-05,
              "VAL_B": 0.2,
              "VAL_H1": 0.1,
              "VAL_H2": 0.2,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
          ]
        }
      ]
    }
  }
}
```

**PSC/Composite – 自动引用截面材料 (Elements)：**

```json
{
  "Assign": {
    "56": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Top",
          "NUM": 1,
          "bPSC": true,
          "vSECTTMP": [
            {
              "TYPE": "ELEMENT",
              "REF": 0,
              "OPT_B": 1,
              "VAL_B": 0.3,
              "OPT_H1": 3,
              "VAL_H1": 0.2,
              "OPT_H2": 3,
              "VAL_H2": 0.4,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
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
| 1 | Beam Section Temperature（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Direction · Local-y: `"LY"` · Local-z: `"LZ"` | `"DIR"` | String | `"LZ"` | Optional |
| (5) | Ref. Position · `"Centroid"` · `"+End(Top)"` → `"Top"` · `"-End(Bot)"` → `"Bot"` | `"REF"` | String | `"Centroid"` | Optional |
| (6) | Number of Section Temperature（`vSECTTMP` 项数） | `"NUM"` | Integer | - | Required |
| (7) | Section Type · General: `false` · PSC/Composite: `true` | `"bPSC"` | Boolean | `false` | Optional |
| (8) | Section Temperature List | `"vSECTTMP"` | Array \[Object\] | - | Required |
| i | Material Type · Element: `"ELEMENT"` · Input: `"INPUT"` | `"TYPE"` | String | `"ELEMENT"` | Optional |
| ii | B Value | `"VAL_B"` | Number | 0 | Optional |
| iii | H1 Value | `"VAL_H1"` | Number | - | Optional |
| iv | H2 Value | `"VAL_H2"` | Number | - | Optional |
| v | T1 Value | `"VAL_T1"` | Number | 0 | Optional |
| vi | T2 Value | `"VAL_T2"` | Number | 0 | Optional |
| vii | Modulus of Elasticity（当 `TYPE` = `"INPUT"` 时） | `"ELAST"` | Number | - | Optional |
| viii | Thermal Coefficient（当 `TYPE` = `"INPUT"` 时） | `"THERMAL"` | Number | - | Optional |
| ix | Ref.（`bPSC` = true） · Top: `0` · Bottom: `1` | `"REF"` | Integer | 0 | Optional |
| x | B-Type（`bPSC` = true） · Section: `0` · Value: `1` | `"OPT_B"` | Integer | 1 | Optional |
| xi | H1-Type（`bPSC` = true） · Z1:`0` · Z2:`1` · Z3:`2` · Value:`3` | `"OPT_H1"` | Integer | 3 | Optional |
| xii | H2-Type（`bPSC` = true） · Z1:`0` · Z2:`1` · Z3:`2` · Value:`3` | `"OPT_H2"` | Integer | 3 | Optional |

### Python 示例

```python
# 定义一般梁截面温度分布（POST）— 自动引用截面材料
btmp_general = {
    "Assign": {
        "51": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(+)",
                    "GROUP_NAME": "",
                    "DIR": "LZ",
                    "REF": "Centroid",
                    "NUM": 1,
                    "bPSC": False,
                    "vSECTTMP": [
                        {"TYPE": "ELEMENT", "VAL_B": 0.2, "VAL_H1": 0.1, "VAL_H2": 0.2, "VAL_T1": 3, "VAL_T2": 12.4}
                    ],
                }
            ]
        }
    }
}
midas_api("POST", "/db/BTMP", btmp_general)

# 定义 PSC/组合截面温度分布（POST）
btmp_psc = {
    "Assign": {
        "56": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "Temp(-)",
                    "GROUP_NAME": "",
                    "DIR": "LZ",
                    "REF": "Top",
                    "NUM": 1,
                    "bPSC": True,
                    "vSECTTMP": [
                        {
                            "TYPE": "ELEMENT",
                            "REF": 0,
                            "OPT_B": 1, "VAL_B": 0.3,
                            "OPT_H1": 3, "VAL_H1": 0.2,
                            "OPT_H2": 3, "VAL_H2": 0.4,
                            "VAL_T1": 3, "VAL_T2": 12.4,
                        }
                    ],
                }
            ]
        }
    }
}
midas_api("POST", "/db/BTMP", btmp_psc)
```

---

## 4. /db/STMP — System Temperature

> 对整个结构物（系统）施加统一的温度变化。键（key）为 **序号**，在一个条目中直接填写荷载工况与温度值。

**Input URI:** `{base url}/db/STMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "TEMPER": 12.5,
      "LCNAME": "Temp(+)",
      "GROUP_NAME": "LoadGroup1"
    },
    "2": {
      "TEMPER": -32.3,
      "LCNAME": "Temp(-)",
      "GROUP_NAME": "LoadGroup2"
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | - | Required |
| 2 | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| 3 | System Temperature | `"TEMPER"` | Number | 0 | Optional |

### Python 示例

```python
# 施加系统温度荷载（POST）
stmp_data = {
    "Assign": {
        "1": {"TEMPER": 12.5,  "LCNAME": "Temp(+)", "GROUP_NAME": ""},
        "2": {"TEMPER": -32.3, "LCNAME": "Temp(-)", "GROUP_NAME": ""},
    }
}
midas_api("POST", "/db/STMP", stmp_data)

# 查询（GET）
midas_api("GET", "/db/STMP")

# 修改（PUT）
midas_api("PUT", "/db/STMP", {
    "Assign": {"1": {"TEMPER": 15.0, "LCNAME": "Temp(+)", "GROUP_NAME": ""}}
})

# 删除（DELETE）
midas_api("DELETE", "/db/STMP", {"Assign": {"2": {}}})
```

---

## 5. /db/NTMP — Nodal Temperature

> 对节点（Node）直接施加温度荷载。键（key）为 **节点编号**，可通过 `ITEMS` 数组同时输入多个荷载工况。

**Input URI:** `{base url}/db/NTMP`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "190": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "LoadGroup2", "TEMPER": -3},
        {"ID": 3, "LCNAME": "Temp(+)", "GROUP_NAME": "LoadGroup1", "TEMPER":  2}
      ]
    },
    "234": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "LoadGroup2", "TEMPER": -5},
        {"ID": 3, "LCNAME": "Temp(+)", "GROUP_NAME": "LoadGroup1", "TEMPER":  3}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Nodal Temperature（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Temperature | `"TEMPER"` | Number | - | Required |

### Python 示例

```python
# 施加节点温度荷载（POST）
ntmp_data = {
    "Assign": {
        "190": {
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "", "TEMPER": -3},
                {"ID": 2, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMPER":  2},
            ]
        },
        "234": {
            "ITEMS": [
                {"ID": 1, "LCNAME": "Temp(-)", "GROUP_NAME": "", "TEMPER": -5},
                {"ID": 2, "LCNAME": "Temp(+)", "GROUP_NAME": "", "TEMPER":  3},
            ]
        },
    }
}
midas_api("POST", "/db/NTMP", ntmp_data)

# 查询（GET）
midas_api("GET", "/db/NTMP")

# 删除（DELETE）
midas_api("DELETE", "/db/NTMP", {"Assign": {"190": {}}})
```

---

## 6. /db/TDNT — Tendon Property

> 定义预应力束的材料性（材料编号、截面积、松弛特性、摩擦系数等）。可用参数随预应力束类型（INTERNAL/EXTERNAL）与张拉方式（PRE/POST）而异。

**Input URI:** `{base url}/db/TDNT`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

**Magura 松弛系数示例（内部/外部）：**

```json
{
  "Assign": {
    "1": {
      "NAME": "In_Pre_Magura",
      "TYPE": "INTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "D_AREA": 0.0152,
      "RM": 0,
      "RV": 45,
      "US": 1860000,
      "YS": 1570000,
      "LT": "PRE"
    },
    "2": {
      "NAME": "In_Post_Magura",
      "TYPE": "INTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "D_AREA": 0.1,
      "RM": 0,
      "RV": 45,
      "US": 1860000,
      "YS": 1570000,
      "LT": "POST",
      "ASB": 0.006,
      "ASE": 0.006,
      "bBONDED": true,
      "FF": 0.3,
      "WF": 0.0066
    },
    "3": {
      "NAME": "Ext_Magura",
      "TYPE": "EXTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "RM": 0,
      "RV": 10,
      "US": 1860000,
      "YS": 1570000,
      "ASB": 0.006,
      "ASE": 0.006,
      "ALPHA": 3000,
      "FF": 0.3
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Name | `"NAME"` | String | - | Required |
| 2 | Tendon Type · Internal: `"INTERNAL"` · External: `"EXTERNAL"` | `"TYPE"` | String | `"EXTERNAL"` | Optional |
| 3 | Tensioning Type · Post-Tension: `"POST"` · Pre-Tension: `"PRE"` · External: 不使用 | `"LT"` | String | `"PRE"` | Optional |
| 4 | Tendon Material No. | `"MATL"` | Integer | - | Required |
| 5 | Total Tendon Area | `"AREA"` | Number | - | Required |
| 6 | Diameter · Post: 管道直径 · Pre: 钢绞线直径 · External: 不使用 | `"D_AREA"` | Number | - | Required |
| 7 | Anchorage Slip - Begin（仅 Post/External） | `"ASB"` | Number | 0 | Optional |
| 8 | Anchorage Slip - End（仅 Post/External） | `"ASE"` | Number | 0 | Optional |
| 9 | Bond Type（仅 Post） | `"bBONDED"` | Boolean | `false` | Optional |
| 10 | External Cable Moment Magnifier（仅 External） | `"ALPHA"` | Number | 0 | Optional |
| 11 | Relaxation Coefficient – Code ¹⁾ | `"RM"` | Integer | - | Required |
| 12 | Relaxation Coefficient – Factor ¹⁾ | `"RV"` | Integer | - | Required |
| 13 | Ultimate Strength | `"US"` | Number | 0 | Optional |
| 14 | Yield Strength | `"YS"` | Number | 0 | Optional |
| 15 | Curvature Friction Factor（仅 Post/External） | `"FF"` | Number | 0 | Optional |
| 16 | Wobble Friction Factor（仅 Post，Magura/IRC/KSCE/IRC112 代码） | `"WF"` | Number | 0 | Optional |
| 16 | Wobble Type（CEB-FIP/European 代码） · Fraction Factor: `0` · Unintentional Angular: `1` | `"W_TYPE"` | Integer | 0 | Optional |
| 17 | Wobble Fraction Factor (`W_TYPE`=0) | `"WF"` | Number | 0 | Optional |
| 17 | Unintentional Angular Disp. (`W_TYPE`=1) | `"W_ANGLE"` | Number | 0 | Optional |
| 18 | Relaxation Coefficient Class（仅 CEB-FIP 2010） | `"TDMFK"` | Integer | 1 | Optional |
| — | Relaxation Factor ξ (TB05/TB10092/Q-CR/AS/JTJ/JTG 代码) | `"FT"` | Number | - | Required |
| — | Low Relaxation (TB05/TB10092/Q-CR 代码) | `"LR"` | Boolean | `false` | Optional |
| — | 应用 Overstress Reduction Factor (TB05/TB10092/Q-CR/JTG 代码) | `"bOSRF"` | Boolean | `false` | Optional |
| — | Characteristic Strength fpk (TB05/TB10092/Q-CR/JTJ/JTG 代码) | `"FPK"` | Number | - | Required |
| — | Relaxation Function Name (User Defined) | `"TDMFNAME"` | String | - | Required |

> ¹⁾ **松弛系数代码（RM）与系数（RV/FT/TDMFK）表**

| Standard | RM | RV | FT | TDMFK |
|----------|----|----|-----|-------|
| Magura | `0` | `10` or `45` | - | - |
| IRC:18-2000 | `4` | Normal:`1` / Row:`2` | - | - |
| KSCE LSD15 | `6` | Ordinary:`1` / Low:`2` / Hot-rolled:`3` | - | - |
| IRC:112-2011 | `7` | Normal:`1` / Row:`2` | - | - |
| CEB-FIP 1978 | `1` | Number | - | - |
| European | `5` | Ordinary:`1` / Low:`2` / Hot-rolled:`3` | - | - |
| CEB-FIP 1990 | `8` | Number | - | - |
| CEB-FIP 2010 | `9` | Number | - | Class1-Slow:`1` / Class2-Mean:`2` / Class3-Rapid:`3` |
| TB05 | `3` | - | Number | - |
| TB10092-17 | `10` | - | Number | - |
| Q/CR 9300-18 | `12` | - | Number | - |
| AS 5100.5-2017 | `11` | - | Number | - |
| JTJ023-85 | `13` | - | Number | - |
| JTG18/JTG04 | `2` | - | `1` or `0.3` | - |
| User Defined | `100` | - | - | - |

### Python 示例

```python
# 定义预应力束材料性（POST）— 以 KSCE LSD15 为准，内部 Post-Tension
tdnt_data = {
    "Assign": {
        "1": {
            "NAME": "T1_Post_KSCE",
            "TYPE": "INTERNAL",
            "MATL": 1,
            "AREA": 0.00504,     # 预应力束总面积 (m²)
            "D_AREA": 0.1,       # 管道直径 (m)
            "RM": 6,             # KSCE LSD15
            "RV": 2,             # Low relaxation
            "US": 1860000,       # 极限强度 (kN/m²)
            "YS": 1570000,       # 屈服强度 (kN/m²)
            "LT": "POST",
            "ASB": 0.006,        # 起点锚具位移量 (m)
            "ASE": 0.006,        # 终点锚具位移量 (m)
            "bBONDED": True,     # 灌浆（粘结）
            "FF": 0.3,           # 曲率摩擦系数
            "WF": 0.0066,        # 摇摆摩擦系数
        }
    }
}
midas_api("POST", "/db/TDNT", tdnt_data)

# 查询（GET）
midas_api("GET", "/db/TDNT")

# 删除（DELETE）
midas_api("DELETE", "/db/TDNT", {"Assign": {"1": {}}})
```

---

## 7. /db/TDNA — Tendon Profile

> 定义预应力束的布置路径（线形）。输入结构随 2D/3D 与 Spline/Round 的组合、基准轴类型（Element/Straight/Curve）而异。

**Input URI:** `{base url}/db/TDNA`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

**2D Spline 类型（以 Element 为基准）：**

```json
{
  "Assign": {
    "1": {
      "NAME": "2D/Spline/Element",
      "TDN_PROP": 1,
      "ELEM": [1101, 1102, 1103, 1104, 1105],
      "BELENG": 0,
      "ELENG": 0,
      "CURVE": "SPLINE",
      "INPUT": "2D",
      "TDN_GRUP": 1,
      "LENG_OPT": "AUTO2",
      "bTP": false,
      "SHAPE": "ELEMENT",
      "INS_PT": "END-I",
      "INS_ELEM": 1101,
      "AXIS_IJ": "I-J",
      "XAR_ANGLE": 0,
      "bPJ": true,
      "OFF_YZ": [0, 0],
      "PROFY": [
        {"PT": [0, -0.5], "bFIX": true, "R": 0},
        {"PT": [15, -0.3], "bFIX": false, "R": 0},
        {"PT": [30, -0.5], "bFIX": true, "R": 0}
      ],
      "PROFZ": [
        {"PT": [0, -0.6], "bFIX": true, "R": 0, "bBOTZ": false},
        {"PT": [15, -0.3], "bFIX": false, "R": 0, "bBOTZ": false},
        {"PT": [30, -0.6], "bFIX": true, "R": 0, "bBOTZ": false}
      ]
    }
  }
}
```

**3D Spline 类型（以 Element 为基准）：**

```json
{
  "Assign": {
    "3": {
      "NAME": "3D/Spline/Element",
      "TDN_PROP": 1,
      "ELEM": [1301, 1302, 1303, 1304, 1305],
      "BELENG": 0,
      "ELENG": 0,
      "CURVE": "SPLINE",
      "INPUT": "3D",
      "TDN_GRUP": 1,
      "LENG_OPT": "USER",
      "BLEN": 0,
      "ELEN": 0,
      "bTP": true,
      "CNT": 2,
      "DeBondBLEN": 1.2,
      "DeBondELEN": 1.2,
      "SHAPE": "ELEMENT",
      "INS_PT": "END-I",
      "INS_ELEM": 1301,
      "AXIS_IJ": "I-J",
      "XAR_ANGLE": 0,
      "bPJ": true,
      "OFF_YZ": [-0.5, 0],
      "PROF": [
        {"PT": [0, 0, -0.6], "bFIX": true, "R": [1.2, 1.2]},
        {"PT": [30, 0, -0.6], "bFIX": false, "R": [0, 0]}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Name | `"NAME"` | String | - | Required |
| 2 | Tendon Group No. | `"TDN_GRUP"` | Integer | 0 | Optional |
| 3 | Tendon Property No. | `"TDN_PROP"` | Integer | - | Required |
| 4 | Assigned Elements No. | `"ELEM"` | Array \[Integer\] | - | Required |
| 5 | Input Type · 2D: `"2D"` · 3D: `"3D"` | `"INPUT"` | String | - | Required |
| 6 | Curve Type · Spline: `"SPLINE"` · Round: `"ROUND"` | `"CURVE"` | String | - | Required |
| 7 | Straight Length – Begin（仅 Spline） | `"BELENG"` | Number | 0 | Optional |
| 8 | Straight Length – End（仅 Spline） | `"ELENG"` | Number | 0 | Optional |
| 9 | Typical Tendon | `"bTP"` | Boolean | `false` | Optional |
| 10 | No. of Tendons（`bTP` = true 时必填） | `"CNT"` | Number | - | Optional |
| 11 | Transfer Length Option · `"USER"` · `"AUTO1"` · `"AUTO2"` | `"LENG_OPT"` | String | - | Required |
| 12 | Transfer Length – Begin | `"BLEN"` | Number | 0 | Optional |
| 13 | Transfer Length – End | `"ELEN"` | Number | 0 | Optional |
| 14 | Debonded Length – Begin（仅 Pre-tensioning） | `"DeBondBLEN"` | Number | 0 | Optional |
| 15 | Debonded Length – End（仅 Pre-tensioning） | `"DeBondELEN"` | Number | 0 | Optional |
| 16 | Reference Axis · `"ELEMENT"` · `"STRAIGHT"` · `"CURVE"` | `"SHAPE"` | String | - | Required |

**当 SHAPE = "ELEMENT" 时的附加参数：**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 17 | Profile Insertion Point · `"END-I"` · `"END-J"` | `"INS_PT"` | String | - | Required |
| 18 | Profile Insertion Point Element No. | `"INS_ELEM"` | Integer | - | Required |
| 19 | x Axis Direction · `"I-J"` · `"J-I"` | `"AXIS_IJ"` | String | `"I-J"` | Optional |
| 20 | x Axis Rotation Angle | `"XAR_ANGLE"` | Number | 0 | Optional |
| 21 | Projection | `"bPJ"` | Boolean | `false` | Optional |
| 22 | Offset (y, z) | `"OFF_YZ"` | Array \[Number, 2\] | `[0,0]` | Optional |

**当 SHAPE = "STRAIGHT" 时的附加参数：**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 17 | Insertion Point \[x, y, z\] | `"IP"` | Array \[Number, 3\] | `[0,0,0]` | Optional |
| 18 | x Axis Direction · `"X"` · `"Y"` · `"VECTOR"` | `"AXIS"` | String | `"X"` | Optional |
| 19 | Vector \[x, y\] | `"VEC"` | Array \[Number, 2\] | `[0,0]` | Optional |
| 20 | x Axis Rotation Angle | `"XAR_ANGLE"` | Number | 0 | Optional |
| 21 | Projection | `"bPJ"` | Boolean | `false` | Optional |
| 22 | Grad. Rot. Angle Type · `"X"` · `"Y"` | `"GR_AXIS"` | String | `"Y"` | Optional |
| 23 | Grad. Rot. Angle | `"GR_ANGLE"` | Number | 0 | Optional |

**当 SHAPE = "CURVE" 时的附加参数：**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 17 | Insertion Point \[x, y, z\] | `"IP"` | Array \[Number, 3\] | `[0,0,0]` | Optional |
| 18 | Radius Center (X, Y) | `"RC"` | Array \[Number, 2\] | 0 | Optional |
| 19 | Offset | `"OFFSET"` | Number | 0 | Optional |
| 20 | Direction · CW: `"CW"` · CCW: `"CCW"` | `"DIR"` | String | `"CW"` | Optional |
| 20 | x Axis Rotation Angle | `"XAR_ANGLE"` | Number | 0 | Optional |
| 21 | Projection | `"bPJ"` | Boolean | `false` | Optional |
| 22 | Grad. Rot. Angle Type · `"X"` · `"Y"` | `"GR_AXIS"` | String | `"Y"` | Optional |
| 23 | Grad. Rot. Angle | `"GR_ANGLE"` | Number | 0 | Optional |

> ⚠️ **2026-09-06 例行检查补充：** `bPJ`(Projection) 行在此 CURVE 块中曾有遗漏，
> 现已补充 — 原文 JSON Schema（`"bPJ": {"description": "IsProjection?", "type": "boolean"}`）、
> CURVE 的全部 4 个示例（`"bPJ": true`）以及原文 Specifications 表中均存在该字段（同一字段
> 在 ELEMENT·STRAIGHT 块中早已列出）。编号 20 同时出现在 `DIR`·`XAR_ANGLE` 两行，
> 系原样照搬原文的编号错误（保持原文标注 — 请勿回退）。

**线形坐标（INPUT=2D，CURVE="SPLINE"）：**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 24 | Profile in x-y plane | `"PROFY"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y\] | `"PT"` | Array \[Number, 2\] | - | Required |
| (2) | Fix Option | `"bFIX"` | Boolean | `false` | Optional |
| (3) | Radius (degree) | `"R"` | Number | 0 | Optional |
| 25 | Profile in x-z plane | `"PROFZ"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y\] | `"PT"` | Array \[Number, 2\] | - | Required |
| (2) | Fix Option | `"bFIX"` | Boolean | `false` | Optional |
| (3) | Radius (degree) | `"R"` | Number | 0 | Optional |
| (4) | BOT Option（仅 ELEMENT 类型） | `"bBOTZ"` | Boolean | `false` | Optional |

**线形坐标（INPUT=2D，CURVE="ROUND"）：**

> ⚠️ 2025-08-25 确认：既有文档只涉及 Spline 类型的线形结构（`bFIX`/`R`），Round 类型结构
> 曾遗漏（通过与原文 [Tendon Profile](https://support.midasuser.com/hc/en-us/articles/35954555962137)
> 重新比对发现）。Round 类型不使用 `bFIX`/`R`，而使用 `RADIUS`·`OPT`·`ANGLE`·`HEIGHT`·`RADIUS2`。
> 原文 Specifications 表把 `RADIUS` 的 Value Type 标注为 "Boolean"，但这与示例（`RADIUS": 0, 20` 等
> 数值）矛盾，故依 CLAUDE.md 原则（示例优先）记为 Number。
>
> ✅ **2026-09-18 经实机验证确认（非推测）。** 在 Gen NX 2026 v2.1 · Civil NX 2026 v2.2
> (Build 09/15/2026) 两侧，`PROFY[].RADIUS = false` 均被拒绝并返回 `Wrong Field`，后续 GET
> 返回 `Not Found Key`。数值（`0`、`20`）在两个产品中均可正常创建并保留。原表的
> "Boolean" 标注有误，实际 wire type 为 `Number`。原文 JSON Schema 中 `PROFY`·`PROFZ`·`PROF`
> 三个分支也一致为 `"RADIUS": {"type": "number"}`。已按 Jira `MAPI-2485` B-2 报告。
>
> ⚠️ **本 API 会以 HTTP 201 返回错误正文。** 仅看状态码会误判为成功，
> 务必同时核查响应正文与后续 GET 的结果。

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 24 | Profile in x-y plane | `"PROFY"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y\] | `"PT"` | Array \[Number, 2\] | - | Required |
| (2) | Radius (length) | `"RADIUS"` | Number | 0 | Optional |
| (3) | Add Option · None: `"NONE"` · Left: `"LEFT"` · Right: `"RIGHT"` | `"OPT"` | String | `"NONE"` | Optional |
| (4) | Angle（`OPT`="LEFT"/"RIGHT" 时） | `"ANGLE"` | Number | 0 | Optional |
| (5) | Height（`OPT`="LEFT"/"RIGHT" 时） | `"HEIGHT"` | Number | 0 | Optional |
| (6) | Radius – length（`OPT`="LEFT"/"RIGHT" 时） | `"RADIUS2"` | Number | 0 | Optional |
| 25 | Profile in x-z plane | `"PROFZ"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y\] | `"PT"` | Array \[Number, 2\] | - | Required |
| (2) | Radius (length) | `"RADIUS"` | Number | 0 | Optional |
| (3) | Add Option · None: `"NONE"` · Left: `"LEFT"` · Right: `"RIGHT"` | `"OPT"` | String | `"NONE"` | Optional |
| (4) | BOT Option（仅 ELEMENT 类型） | `"bBOTZ"` | Boolean | `false` | Optional |
| (5) | Angle（`OPT`="LEFT"/"RIGHT" 时） | `"ANGLE"` | Number | 0 | Optional |
| (6) | Height（`OPT`="LEFT"/"RIGHT" 时） | `"HEIGHT"` | Number | 0 | Optional |
| (7) | Radius – length（`OPT`="LEFT"/"RIGHT" 时） | `"RADIUS2"` | Number | 0 | Optional |

**线形坐标（INPUT=3D，CURVE="SPLINE"）：**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 24 | 3D Profile | `"PROF"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y, z\] | `"PT"` | Array \[Number, 3\] | - | Required |
| (2) | Fix Option | `"bFIX"` | Boolean | `false` | Optional |
| (3) | Radius – degree \[Ry, Rz\] | `"R"` | Array \[Number, 2\] | 0 | Optional |

**线形坐标（INPUT=3D，CURVE="ROUND"）：**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 24 | 3D Profile | `"PROF"` | Array \[Object\] | - | Required |
| (1) | Coordinates \[x, y, z\] | `"PT"` | Array \[Number, 3\] | - | Required |
| (2) | Fix Option | `"bFIX"` | Boolean | `false` | Optional |
| (3) | Radius (length) | `"RADIUS"` | Number | 0 | Optional |

> ⚠️ **原表把本行的 Value Type 写为 "Array"，此处按 `Number` 记载。** 原文对同一个
> `"RADIUS"` 条目按区段标注了三种类型（2D x-y `Boolean` / 2D x-z `Number` / 3D `Array`），
> 而 JSON Schema 三个分支均为 `"type": "number"`，示例也全部是标量（`0`、`20`）。
>
> ✅ **2026-09-18 经实机验证确认。** `PROF[].RADIUS = [0, 20]` 在 Gen·Civil 两侧均被拒绝并返回
> `Wrong Field`，后续 GET 返回 `Not Found Key`（验证环境与 HTTP 201 的注意事项参见上文
> 2D Round 节的注释）。数值可正常创建并保留。请勿回退 — 已按 Jira `MAPI-2485`
> B-2 报告，原文更正后一并清理本注释。

### Python 示例

```python
# 定义 2D Spline 预应力束线形（POST）— 以 Element 为基准轴
tdna_data = {
    "Assign": {
        "1": {
            "NAME": "T1_Profile_2D",
            "TDN_PROP": 1,          # 在 TDNT 中定义的预应力束材料性编号
            "ELEM": [101, 102, 103, 104, 105],  # 布置单元列表
            "BELENG": 0,
            "ELENG": 0,
            "CURVE": "SPLINE",
            "INPUT": "2D",
            "TDN_GRUP": 1,
            "LENG_OPT": "AUTO2",
            "bTP": False,
            "SHAPE": "ELEMENT",
            "INS_PT": "END-I",
            "INS_ELEM": 101,
            "AXIS_IJ": "I-J",
            "XAR_ANGLE": 0,
            "bPJ": True,
            "OFF_YZ": [0, 0],
            "PROFY": [
                {"PT": [0,  -0.5], "bFIX": True,  "R": 0},
                {"PT": [15, -0.3], "bFIX": False, "R": 0},
                {"PT": [30, -0.5], "bFIX": True,  "R": 0},
            ],
            "PROFZ": [
                {"PT": [0,  -0.6], "bFIX": True,  "R": 0, "bBOTZ": False},
                {"PT": [15, -0.3], "bFIX": False, "R": 0, "bBOTZ": False},
                {"PT": [30, -0.6], "bFIX": True,  "R": 0, "bBOTZ": False},
            ],
        }
    }
}
midas_api("POST", "/db/TDNA", tdna_data)

# 查询（GET）
midas_api("GET", "/db/TDNA")
```

---

## 8. /db/TDCS — Tendon Location for Composite Section

> 指定施工阶段组合截面中预应力束线形所属的 Part 编号。

**Input URI:** `{base url}/db/TDCS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "TDNA": 1,
      "CSCS": 1,
      "PART_NUM": 1
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Profile No. | `"TDNA"` | Integer | - | Required |
| 2 | Composite Section for Construction Stage No. | `"CSCS"` | Integer | - | Required |
| 3 | Part Number | `"PART_NUM"` | Integer | - | Required |

### Python 示例

```python
# 指定组合截面的预应力束位置（POST）
tdcs_data = {
    "Assign": {
        "1": {
            "TDNA": 1,       # 预应力束线形编号 (TDNA)
            "CSCS": 1,       # 施工阶段组合截面编号
            "PART_NUM": 1,   # Part 编号
        }
    }
}
midas_api("POST", "/db/TDCS", tdcs_data)

# 查询（GET）
midas_api("GET", "/db/TDCS")

# 删除（DELETE）
midas_api("DELETE", "/db/TDCS", {"Assign": {"1": {}}})
```

---

## 9. /db/TDPL — Tendon Prestress

> 对预应力束线形施加预应力荷载。键（key）为 **预应力束线形编号（TDNA）**，以张力或应力值输入。

**Input URI:** `{base url}/db/TDPL`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "TENDON_NAME": "2D/Round/Element",
          "TYPE": "FORCE",
          "ORDER": "BOTH",
          "BEGIN": 1360000,
          "END": 1360000,
          "GROUTING": 1
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Tendon Prestress（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Tendon Profile Name | `"TENDON_NAME"` | String | - | Required |
| (5) | Prestress Load Type · Stress: `"STRESS"` · Force: `"FORCE"` | `"TYPE"` | String | `"STRESS"` | Optional |
| (6) | Jacking Step · Begin: `"BEGIN"` · End: `"END"` · Both: `"BOTH"` | `"ORDER"` | String | `"BEGIN"` | Optional |
| (7) | Jacking Force / Stress at Begin | `"BEGIN"` | Number | - | Required |
| (8) | Jacking Force / Stress at End | `"END"` | Number | - | Required |
| (9) | Grouting Stage | `"GROUTING"` | Integer | 0 | Optional |

### Python 示例

```python
# 施加预应力束预应力（POST）
tdpl_data = {
    "Assign": {
        "1": {   # 预应力束线形 1（TDNA 编号）
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "PS",
                    "GROUP_NAME": "",
                    "TENDON_NAME": "T1_Profile_2D",  # 在 TDNA 中定义的名称
                    "TYPE": "FORCE",     # 以张力输入
                    "ORDER": "BOTH",     # 起点·终点同时张拉
                    "BEGIN": 1360000,    # 起点张力 (kN/m²)
                    "END": 1360000,      # 终点张力
                    "GROUTING": 1,       # 灌浆施工阶段
                }
            ]
        }
    }
}
midas_api("POST", "/db/TDPL", tdpl_data)

# 查询（GET）
midas_api("GET", "/db/TDPL")

# 删除（DELETE）
midas_api("DELETE", "/db/TDPL", {"Assign": {"1": {}}})
```

---

## 10. /db/PRST — Prestress Beam Loads

> 直接在梁单元上施加预应力荷载（无需预应力束线形）。键（key）为 **单元编号**。

**Input URI:** `{base url}/db/PRST`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1101": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "DIR": 1,
          "TENSION": 1360,
          "DISTANCE_I": 0.2,
          "DISTANCE_M": 0.3,
          "DISTANCE_J": 0.4
        }
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Prestress Beam Loads（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Direction · Local y: `0` · Local z: `1` | `"DIR"` | Integer | 0 | Optional |
| (5) | Tension | `"TENSION"` | Number | - | Required |
| (6) | Distance – I (Di) | `"DISTANCE_I"` | Number | 0 | Optional |
| (7) | Distance – M (Dm) | `"DISTANCE_M"` | Number | 0 | Optional |
| (8) | Distance – J (Dj) | `"DISTANCE_J"` | Number | 0 | Optional |

### Python 示例

```python
# 施加梁预应力荷载（POST）
prst_data = {
    "Assign": {
        "1101": {   # 单元 1101
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "PS",
                    "GROUP_NAME": "",
                    "DIR": 1,             # Local z 方向
                    "TENSION": 1360,      # 张力
                    "DISTANCE_I": 0.2,    # i 端偏心距 (m)
                    "DISTANCE_M": 0.3,    # 跨中偏心距 (m)
                    "DISTANCE_J": 0.4,    # j 端偏心距 (m)
                }
            ]
        },
        "1102": {
            "ITEMS": [
                {"ID": 1, "LCNAME": "PS", "GROUP_NAME": "", "DIR": 1,
                 "TENSION": 1360, "DISTANCE_I": 0.2, "DISTANCE_M": 0.3, "DISTANCE_J": 0.4}
            ]
        },
    }
}
midas_api("POST", "/db/PRST", prst_data)

# 查询（GET）
midas_api("GET", "/db/PRST")

# 删除（DELETE）
midas_api("DELETE", "/db/PRST", {"Assign": {"1101": {}}})
```

---

## 11. /db/PTNS — Pretension Loads

> 为桁架/拉索单元施加先张力（初始张力）。键（key）为 **单元编号**。

**Input URI:** `{base url}/db/PTNS`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "3431": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "LoadGroup", "TENSION": 130}
      ]
    },
    "3432": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "LoadGroup", "TENSION": 130}
      ]
    },
    "3433": {
      "ITEMS": [
        {"ID": 1, "LCNAME": "PrS2", "GROUP_NAME": "LoadGroup", "TENSION": 130}
      ]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Pretension Loads（以数组对象输入） | `"ITEMS"` | Array \[Object\] | - | Required |
| (1) | Serial Number | `"ID"` | Integer | 0 | Optional |
| (2) | Load Case Name | `"LCNAME"` | String | - | Required |
| (3) | Load Group Name | `"GROUP_NAME"` | String | Blank | Optional |
| (4) | Pretension Load | `"TENSION"` | Number | - | Required |

### Python 示例

```python
# 施加先张荷载（POST）
# 荷载工况 PrS1 需在 EXLD 中另行指定为 External Type
ptns_data = {
    "Assign": {
        "3431": {
            "ITEMS": [{"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "", "TENSION": 130}]
        },
        "3432": {
            "ITEMS": [{"ID": 1, "LCNAME": "PrS1", "GROUP_NAME": "", "TENSION": 130}]
        },
        "3433": {
            "ITEMS": [{"ID": 1, "LCNAME": "PrS2", "GROUP_NAME": "", "TENSION": 130}]
        },
    }
}
midas_api("POST", "/db/PTNS", ptns_data)

# 查询（GET）
midas_api("GET", "/db/PTNS")

# 删除（DELETE）
midas_api("DELETE", "/db/PTNS", {"Assign": {"3431": {}}})
```

---

## 12. /db/EXLD — External Type Load Case for Pretension

> 将先张荷载使用的荷载工况指定为 External Type。PTNS 所引用的荷载工况名必须注册到本 Endpoint。

**Input URI:** `{base url}/db/EXLD`  
**Active Methods:** `POST, GET, PUT, DELETE`

### 请求体结构

```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": ["PrS1", "PrS2"]
    }
  }
}
```

### 参数

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name（仅输入含先张荷载的工况） | `"LCNAME_ITEM"` | Array \[String\] | - | Required |

### Python 示例

```python
# 注册先张用 External Type 荷载工况（POST）
# 在 STLD 中以 TYPE="PS" 等定义的工况中，把先张工况登记到此处
exld_data = {
    "Assign": {
        "1": {
            "LCNAME_ITEM": ["PrS1", "PrS2"]  # PTNS 中使用的荷载工况名
        }
    }
}
midas_api("POST", "/db/EXLD", exld_data)

# 查询（GET）
midas_api("GET", "/db/EXLD")

# 修改（PUT）— 添加荷载工况
midas_api("PUT", "/db/EXLD", {
    "Assign": {"1": {"LCNAME_ITEM": ["PrS1", "PrS2", "PrS3"]}}
})

# 删除（DELETE）
midas_api("DELETE", "/db/EXLD", {"Assign": {"1": {}}})
```

---

## 工作流示例 — 预应力混凝土梁建模

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "YOUR_MAPI_KEY_HERE"

def midas_api(method, endpoint, body=None):
    url = BASE_URL + endpoint
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    r = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{r.status_code}] {method.upper()} {endpoint}")
    return r.json() if r.text else {}

# 第 1 步：创建静力荷载工况（参见 STLD）
midas_api("POST", "/db/STLD", {
    "Assign": {
        "1": {"NAME": "PS",    "TYPE": "PS",  "DESC": "Prestress"},
        "2": {"NAME": "Temp+", "TYPE": "T",   "DESC": "Temperature +"},
        "3": {"NAME": "PrS1",  "TYPE": "PS",  "DESC": "Pretension LC1"},
    }
})

# 第 2 步：施加温度荷载
midas_api("POST", "/db/ETMP", {
    "Assign": {
        "1": {"ITEMS": [{"ID": 1, "LCNAME": "Temp+", "GROUP_NAME": "", "TEMP": 25}]}
    }
})

# 第 3 步：定义预应力束材料性
midas_api("POST", "/db/TDNT", {
    "Assign": {
        "1": {
            "NAME": "TD1_KSCE",
            "TYPE": "INTERNAL",
            "MATL": 1,
            "AREA": 0.00504,
            "D_AREA": 0.1,
            "RM": 6,         # KSCE LSD15
            "RV": 2,         # Low relaxation
            "US": 1860000,
            "YS": 1570000,
            "LT": "POST",
            "ASB": 0.006,
            "ASE": 0.006,
            "bBONDED": True,
            "FF": 0.3,
            "WF": 0.0066,
        }
    }
})

# 第 4 步：定义预应力束线形
midas_api("POST", "/db/TDNA", {
    "Assign": {
        "1": {
            "NAME": "TD1_Profile",
            "TDN_PROP": 1,
            "ELEM": [101, 102, 103, 104, 105],
            "BELENG": 0, "ELENG": 0,
            "CURVE": "SPLINE", "INPUT": "2D",
            "TDN_GRUP": 1, "LENG_OPT": "AUTO2",
            "bTP": False, "SHAPE": "ELEMENT",
            "INS_PT": "END-I", "INS_ELEM": 101,
            "AXIS_IJ": "I-J", "XAR_ANGLE": 0,
            "bPJ": True, "OFF_YZ": [0, 0],
            "PROFY": [
                {"PT": [0,  0],    "bFIX": True,  "R": 0},
                {"PT": [12, -0.5], "bFIX": False, "R": 0},
                {"PT": [24, 0],    "bFIX": True,  "R": 0},
            ],
            "PROFZ": [
                {"PT": [0,  -0.5], "bFIX": True,  "R": 0, "bBOTZ": False},
                {"PT": [12, -0.05],"bFIX": False, "R": 0, "bBOTZ": False},
                {"PT": [24, -0.5], "bFIX": True,  "R": 0, "bBOTZ": False},
            ],
        }
    }
})

# 第 5 步：施加预应力束预应力荷载
midas_api("POST", "/db/TDPL", {
    "Assign": {
        "1": {
            "ITEMS": [{
                "ID": 1,
                "LCNAME": "PS",
                "GROUP_NAME": "",
                "TENDON_NAME": "TD1_Profile",
                "TYPE": "FORCE",
                "ORDER": "BOTH",
                "BEGIN": 1360000,
                "END": 1360000,
                "GROUTING": 1,
            }]
        }
    }
})

# 第 6 步：注册先张 External Type（需要时）
midas_api("POST", "/db/EXLD", {
    "Assign": {"1": {"LCNAME_ITEM": ["PrS1"]}}
})

print("PSC 梁预应力荷载定义完成")
```
