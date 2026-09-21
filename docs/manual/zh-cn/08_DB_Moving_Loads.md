# DB – Moving Loads

> **适用产品：** MIDAS Civil NX（移动荷载为 Civil NX 专用）
> **Base URL:** `https://moa-engineers.midasit.com:443/civil`
> **认证：** 所有请求必须携带 `MAPI-Key: <key>` 头部
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../08_DB_Moving_Loads.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

> ⚠️ **本节所有 Endpoint 均为 MIDAS Civil NX 专用。**

---

## 目录

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | [/db/MVCD](#1-dbmvcd--moving-load-code) | Moving Load Code |
| 2 | [/db/LLAN](#2-dbllan--traffic-line-lanes) | Traffic Line Lanes |
| 3 | [/db/LLANch](#3-dbllanch--traffic-line-lanes--china) | Traffic Line Lanes – China |
| 4 | [/db/LLANid](#4-dbllanid--traffic-line-lanes--india) | Traffic Line Lanes – India |
| 5 | [/db/LLANtr](#5-dbllantr--traffic-line-lanes--transverse) | Traffic Line Lanes – Transverse |
| 6 | [/db/LLANop](#6-dbllanop--traffic-line-lanes--moving-load-optimization) | Traffic Line Lanes – Moving Load Optimization |
| 7 | [/db/SLAN](#7-dbslan--traffic-surface-lanes) | Traffic Surface Lanes |
| 8 | [/db/SLANch](#8-dbslanch--traffic-surface-lanes--china) | Traffic Surface Lanes – China |
| 9 | [/db/SLANop](#9-dbslanop--traffic-surface-lanes--moving-load-optimization) | Traffic Surface Lanes – Moving Load Optimization |
| 10 | [/db/MVHL](#10-dbmvhl--vehicles) | Vehicles (AASHTO / LRFD / Canada / BS / Eurocode / Korea 等) |
| 11 | [/db/MVHLtr](#11-dbmvhltr--vehicles--transverse) | Vehicles – Transverse |
| 12 | [/db/MVLD](#12-dbmvld--moving-load-cases) | Moving Load Cases |
| 13 | [/db/MVLDch](#13-dbmvldch--moving-load-cases--china) | Moving Load Cases – China |
| 14 | [/db/MVLDid](#14-dbmvldid--moving-load-cases--india) | Moving Load Cases – India |
| 15 | [/db/MVLDbs](#15-dbmvldbs--moving-load-cases--bs) | Moving Load Cases – BS |
| 16 | [/db/MVLDeu](#16-dbmvldeu--moving-load-cases--eurocode) | Moving Load Cases – Eurocode |
| 17 | [/db/MVLDpl](#17-dbmvldpl--moving-load-cases--poland) | Moving Load Cases – Poland |
| 18 | [/db/MVLDtr](#18-dbmvldtr--moving-load-cases--transverse) | Moving Load Cases – Transverse |
| 19 | [/db/CRGR](#19-dbcrgr--concurrent-reaction-group) | Concurrent Reaction Group |
| 20 | [/db/CJFG](#20-dbcjfg--concurrent-joint-force-group) | Concurrent Joint Force Group |
| 21 | [/db/MVHC](#21-dbmvhc--vehicle-classes) | Vehicle Classes |
| 22 | [/db/SINF](#22-dbsinf--plate-element-for-influence-surface) | Plate Element for Influence Surface |
| 23 | [/db/MLSP](#23-dbmlsp--lane-support--negative-moments-at-interior-piers) | Lane Support – Negative Moments at Interior Piers |
| 24 | [/db/MLSR](#24-dbmlsr--lane-support--reactions-at-interior-piers) | Lane Support – Reactions at Interior Piers |
| 25 | [/db/DYLA](#25-dbdyla--dynamic-load-allowance) | Dynamic Load Allowance |
| 26 | [/db/IMPF](#26-dbimpf--additional-impact-factor) | Additional Impact Factor |
| 27 | [/db/DYFG](#27-dbdyfg--railway-dynamic-factor) | Railway Dynamic Factor |
| 28 | [/db/DYNF](#28-dbdynf--railway-dynamic-factor-by-element) | Railway Dynamic Factor by Element |

---

## 通用 Python 辅助函数

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "<YOUR_MAPI_KEY>",
}

def mv_get(endpoint: str) -> dict:
    res = requests.get(f"{BASE_URL}/db/{endpoint}", headers=HEADERS)
    res.raise_for_status()
    return res.json()

def mv_post(endpoint: str, assign: dict) -> dict:
    body = {"Assign": assign}
    res = requests.post(f"{BASE_URL}/db/{endpoint}", headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()

def mv_put(endpoint: str, assign: dict) -> dict:
    body = {"Assign": assign}
    res = requests.put(f"{BASE_URL}/db/{endpoint}", headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()

def mv_delete(endpoint: str, keys: list) -> dict:
    body = {"Assign": {k: {} for k in keys}}
    res = requests.delete(f"{BASE_URL}/db/{endpoint}", headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()
```

---

## 1. /db/MVCD – Moving Load Code

> 设置移动荷载分析使用的设计基准代码。

**Input URI:** `{base url}/db/MVCD`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "CODE": "KSCE-LSD15"
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Moving Load Code ¹⁾ | `"CODE"` | String | – | Required |

**¹⁾ Moving Load Code 值表**

| 标准代码 | CODE 值 |
|-----------|---------|
| KSCE-LSD15 (韩国) | `"KSCE-LSD15"` |
| Korea (KS-RB / KS2005) | `"KOREA"` |
| AASHTO Standard | `"AASHTO STANDARD"` |
| AASHTO LRFD | `"AASHTO LRFD"` |
| PENNDOT | `"AASHTO LRFD(PENDOT)"` |
| China | `"CHINA"` |
| India | `"INDIA"` |
| Taiwan | `"TAIWAN"` |
| Canada | `"CANADA"` |
| BS | `"BS"` |
| Eurocode | `"EUROCODE"` |
| Australia | `"AUSTRALIA"` |
| Poland | `"POLAND"` |
| Russia | `"RUSSIA"` |
| South Africa | `"SOUTH AFRICA"` |
| Transverse | `"TRANS"` |

### Python 示例

```python
# 将移动荷载代码设置为 KSCE-LSD15
result = mv_post("MVCD", {
    "1": {"CODE": "KSCE-LSD15"}
})
print(result)
```

---

## 2. /db/LLAN – Traffic Line Lanes

> 定义基于桥梁主梁单元（Beam Element）的车道移动路径。

**Input URI:** `{base url}/db/LLAN`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "FORWARD",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5},
        {"ELEM": 2, "ECC": -1.5},
        {"ELEM": 3, "ECC": -1.5}
      ]
    }
  }
}
```

### Parameters – COMMON

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Line Lane | `"LL_NAME"` | String | – | Required |
| 2 | Lane Width ¹⁾ | `"WIDTH"` | Number | – | Required |
| 3 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 4 | Transverse Lane Optimization ²⁾ | `"OPT_AUTO_LANE"` | Boolean | false | Optional |
| 5 | Allow Width for Optimization ²⁾ | `"ALLOW_WIDTH"` | Number | – | Optional |
| 6 | Load Distribution (`"LANE"` / `"CROSS"`) | `"LOAD_DIST"` | String | – | Required |
| 7 | Name of Structure Group ³⁾ | `"GROUP_NAME"` | String | `""` | Optional |
| 8 | Skew Start ³⁾ | `"SKEW_START"` | Number | 0 | Optional |
| 9 | Skew End ³⁾ | `"SKEW_END"` | Number | 0 | Optional |
| 10 | Moving Direction (`"FORWARD"` / `"BACKWARD"` / `"BOTH"`) | `"MOVING"` | String | – | Required |

> ¹⁾ 仅在 Eurocode、Australia、Poland、BS、Russia、South Africa 下有效  
> ²⁾ Taiwan 不可使用  
> ³⁾ 仅当 Load Distribution 为 Cross Beam 时使用

### Parameters – LANE_ITEMS（按代码的附加字段）

| 代码 | 附加 Key | 说明 |
|------|----------|------|
| KSCE-LSD15, Canada, BS, Russia, South Africa | `"ECC"` | 偏心率（Eccentricity，可选） |
| Korea, AASHTO Standard, Taiwan | `"ECC"`, `"FACT"`, `"SPAN_START"` | ECC·冲击系数·跨径起点 |
| AASHTO LRFD | `"ECC"`, `"SPAN_START"`, `"CENT_F"` | ECC·跨径起点·离心力系数 |
| PENNDOT | `"ECC"`, `"SPAN_START"` | ECC·跨径起点 |
| Eurocode | `"ECC"`, `"ECCEN_VERT_LOAD"` | ECC·考虑超高的竖向偏心 |
| Australia, Poland | `"ECC"`, `"SPAN_START"` | ECC·跨径起点 |

### Python 示例

```python
# 按 KSCE-LSD15 标准定义车道（Lane Element 方式）
result = mv_post("LLAN", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01",
            "LOAD_DIST": "LANE",
            "GROUP_NAME": "",
            "SKEW_START": 0,
            "SKEW_END": 0,
            "MOVING": "FORWARD",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 3,
            "OPT_AUTO_LANE": True,
            "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": 1, "ECC": -1.5},
            {"ELEM": 2, "ECC": -1.5},
            {"ELEM": 3, "ECC": -1.5},
        ],
    },
    "2": {
        "COMMON": {
            "LL_NAME": "LL_02",
            "LOAD_DIST": "CROSS",
            "GROUP_NAME": "CrossBeam",
            "SKEW_START": 10,
            "SKEW_END": 10,
            "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 3,
            "OPT_AUTO_LANE": True,
            "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": 163, "ECC": -1.5},
            {"ELEM": 164, "ECC": -1.5},
            {"ELEM": 165, "ECC": -1.55},
        ],
    },
})
print(result)
```

---

## 3. /db/LLANch – Traffic Line Lanes – China

> 基于 China 标准的车道移动路径。单独指定中国城市桥梁·高速公路桥的冲击系数。

**Input URI:** `{base url}/db/LLANch`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5, "SPAN": 12, "SPAN_START": true, "SCALE_FACTOR": 1.1}
      ]
    }
  }
}
```

### Parameters – COMMON

与 LLAN 的 COMMON 结构相同（`"LL_NAME"`、`"LOAD_DIST"`、`"MOVING"` 等）

### Parameters – LANE_ITEMS

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Element No. | `"ELEM"` | Integer | – | Required |
| 2 | Eccentricity | `"ECC"` | Number | 0 | Optional |
| 3 | Span Length | `"SPAN"` | Number | 0 | Optional |
| 4 | Span Start | `"SPAN_START"` | Boolean | false | Optional |
| 5 | Scale Factor | `"SCALE_FACTOR"` | Number | 0 | Optional |

### Python 示例

```python
result = mv_post("LLANch", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01",
            "LOAD_DIST": "LANE",
            "GROUP_NAME": "",
            "SKEW_START": 0,
            "SKEW_END": 0,
            "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 3,
            "OPT_AUTO_LANE": True,
            "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": 1,   "ECC": -1.5, "SPAN": 12, "SPAN_START": True,  "SCALE_FACTOR": 1.1},
            {"ELEM": 2,   "ECC": -1.5, "SPAN": 12, "SPAN_START": False, "SCALE_FACTOR": 1.1},
            {"ELEM": 3,   "ECC": -1.5, "SPAN": 12, "SPAN_START": False, "SCALE_FACTOR": 1.1},
        ],
    }
})
print(result)
```

---

## 4. /db/LLANid – Traffic Line Lanes – India

> 基于 India (IRC) 标准的车道。以 IF/CDA 或跨径长度方式指定冲击系数。

**Input URI:** `{base url}/db/LLANid`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 0,
        "OPT_AUTO_LANE": false,
        "ALLOW_WIDTH": 0
      },
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5, "SPAN": 12, "IMPACT_SPAN": 1, "IMPACT_FACTOR": 0}
      ]
    }
  }
}
```

### Parameters – LANE_ITEMS

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Element No. | `"ELEM"` | Integer | – | Required |
| 2 | Eccentricity | `"ECC"` | Number | 0 | Optional |
| 3 | Option (0=IF/CDA, 1=Span Length) | `"IMPACT_SPAN"` | Integer | 0 | Optional |
| 4 | Scale Factor (when IMPACT_SPAN=0) | `"IMPACT_FACTOR"` | Number | 0 | Optional |
| 5 | Span Length (when IMPACT_SPAN=1) | `"SPAN"` | Number | 0 | Optional |

### Python 示例

```python
result = mv_post("LLANid", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01",
            "LOAD_DIST": "LANE",
            "GROUP_NAME": "",
            "SKEW_START": 0,
            "SKEW_END": 0,
            "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8,
            "WIDTH": 0,
            "OPT_AUTO_LANE": False,
            "ALLOW_WIDTH": 0,
        },
        "LANE_ITEMS": [
            {"ELEM": 1, "ECC": -1.5, "SPAN": 12, "IMPACT_SPAN": 1, "IMPACT_FACTOR": 0},
            {"ELEM": 2, "ECC": -1.5, "SPAN": 12, "IMPACT_SPAN": 1, "IMPACT_FACTOR": 0},
        ],
    }
})
print(result)
```

---

## 5. /db/LLANtr – Traffic Line Lanes – Transverse

> 用于 Transverse 移动荷载代码的车道。仅定义各单元的荷载系数。

**Input URI:** `{base url}/db/LLANtr`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LL_NAME": "LL_01",
      "LANE_ITEMS": [
        {"ELEM": 1, "FACTOR": 1.1},
        {"ELEM": 2, "FACTOR": 1.1},
        {"ELEM": 3, "FACTOR": 1.1}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Line Lane | `"LL_NAME"` | String | – | Required |
| 2 | Lane Items | `"LANE_ITEMS"` | Array[Object] | – | Required |
| (1) | Element ID | `"ELEM"` | Integer | – | Required |
| (2) | Factor | `"FACTOR"` | Number | – | Required |

### Python 示例

```python
result = mv_post("LLANtr", {
    "1": {
        "LL_NAME": "LL_01",
        "LANE_ITEMS": [
            {"ELEM": 1, "FACTOR": 1.1},
            {"ELEM": 2, "FACTOR": 1.1},
            {"ELEM": 3, "FACTOR": 1.1},
        ],
    }
})
print(result)
```

---

## 6. /db/LLANop – Traffic Line Lanes – Moving Load Optimization

> 定义移动荷载优化（Moving Load Optimization）专用车道。  
> 自动搜索车道宽度内的最优位置。

**Input URI:** `{base url}/db/LLANop`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LL_NAME": "LL_01",
      "LOAD_DIST": "LANE",
      "GROUP_NAME": "",
      "SKEW_START": 0,
      "SKEW_END": 0,
      "MOVING": "BOTH",
      "OPTIM_WIDTH": 5,
      "LANE_WIDTH": 3,
      "OFFSET_TYPE": 0,
      "DIVIDE_NUM": 2,
      "ANAL_LANE_OFFSET": 1,
      "WHEEL_SPACE": 1.8288,
      "MARGIN": 0.1,
      "LANE_ITEMS": [
        {"ELEM": 1, "ECC": -1.5, "FACT": 1.25, "SPAN_START": true},
        {"ELEM": 2, "ECC": -1.5, "FACT": 1.25, "SPAN_START": false}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Line Lane | `"LL_NAME"` | String | – | Required |
| 2 | Load Distribution (`"LANE"` / `"CROSS"`) | `"LOAD_DIST"` | String | – | Required |
| 3 | Structure Group Name | `"GROUP_NAME"` | String | `""` | Optional |
| 4 | Skew Start | `"SKEW_START"` | Number | 0 | Optional |
| 5 | Skew End | `"SKEW_END"` | Number | 0 | Optional |
| 6 | Moving Direction | `"MOVING"` | String | – | Required |
| 7 | Optimization Width | `"OPTIM_WIDTH"` | Number | – | Required |
| 8 | Lane Width | `"LANE_WIDTH"` | Number | – | Required |
| 9 | Offset Type (0=Fixed, 1=Division) | `"OFFSET_TYPE"` | Integer | – | Required |
| 10 | Number of Division | `"DIVIDE_NUM"` | Integer | – | Optional |
| 11 | Analysis Lane Offset | `"ANAL_LANE_OFFSET"` | Number | – | Optional |
| 12 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 13 | Margin | `"MARGIN"` | Number | 0 | Optional |
| 14 | Lane Items（ELEM、ECC 及按代码的附加字段） | `"LANE_ITEMS"` | Array[Object] | – | Required |

### Python 示例

```python
result = mv_post("LLANop", {
    "1": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "OPTIM_WIDTH": 5,
        "LANE_WIDTH": 3,
        "OFFSET_TYPE": 0,
        "DIVIDE_NUM": 2,
        "ANAL_LANE_OFFSET": 1,
        "WHEEL_SPACE": 1.8288,
        "MARGIN": 0.1,
        "LANE_ITEMS": [
            {"ELEM": 1, "ECC": -1.5, "SPAN_START": True, "CENT_F": 0.5},
            {"ELEM": 2, "ECC": -1.5, "SPAN_START": False, "CENT_F": 0.5},
        ],
    }
})
print(result)
```

---

## 7. /db/SLAN – Traffic Surface Lanes

> 基于板单元（Plate Element）的面车道移动路径。以节点为基准定义车道路径。

**Input URI:** `{base url}/db/SLAN`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "LL_01",
      "WIDTH": 3,
      "WHEEL_SPACE": 1.8,
      "SKEW_START": 10,
      "SKEW_END": 15,
      "bOPTIMIZE": true,
      "ALLOW_WIDTH": 3,
      "MV_DIR": "BOTH",
      "LANE_ITEMS": [
        {"NODE": 1, "OFFSET": -1.5},
        {"NODE": 2, "OFFSET": -1.5},
        {"NODE": 3, "OFFSET": -1.5},
        {"NODE": 4, "OFFSET": -1.5}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Name of Surface Lane | `"NAME"` | String | – | Required |
| 2 | Lane Width | `"WIDTH"` | Number | – | Required |
| 3 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 4 | Skew Start | `"SKEW_START"` | Number | 0 | Optional |
| 5 | Skew End | `"SKEW_END"` | Number | 0 | Optional |
| 6 | Transverse Lane Optimization ¹⁾ | `"bOPTIMIZE"` | Boolean | false | Optional |
| 7 | Allow Width for Optimization ¹⁾ | `"ALLOW_WIDTH"` | Number | 0 | Optional |
| 8 | Moving Direction (`"FORWARD"` / `"BACKWARD"` / `"BOTH"`) | `"MV_DIR"` | String | – | Required |
| 9 | Sequence Number (Unique) | `"SEQ"` | Integer | 1 | Optional |
| 10 | Lane Items | `"LANE_ITEMS"` | Array[Object] | – | Required |

> ¹⁾ India、Taiwan 不可使用

### Parameters – LANE_ITEMS（按代码的附加字段）

| 代码 | 附加 Key | 说明 |
|------|----------|------|
| KSCE-LSD15, Canada, BS, Russia, South Africa | `"NODE"`, `"OFFSET"` | 节点·偏心 |
| Korea, AASHTO Standard, Taiwan | `"NODE"`, `"OFFSET"`, `"IMPACT_FACTOR"`, `"bSPAN_START"` | +冲击系数·跨径起点 |
| AASHTO LRFD | `"NODE"`, `"OFFSET"`, `"bSPAN_START"`, `"CENTRI_FORCE"` | +跨径起点·离心力系数 |
| PENNDOT, Australia, Poland | `"NODE"`, `"OFFSET"`, `"bSPAN_START"` | +跨径起点 |
| India | `"NODE"`, `"OFFSET"`, `"IMPACT_SPAN_TYPE"`, `"IMPACT_FACTOR_INDIA"`, `"SPAN_LENGTH"` | 冲击系数方式分支 |
| Eurocode | `"NODE"`, `"OFFSET"`, `"ECCEN_VERT_LOAD"` | +考虑超高的竖向偏心 |

### Python 示例

```python
# 按 KSCE-LSD15 标准定义面车道
result = mv_post("SLAN", {
    "1": {
        "NAME": "SL_01",
        "WIDTH": 3,
        "WHEEL_SPACE": 1.8,
        "SKEW_START": 0,
        "SKEW_END": 0,
        "bOPTIMIZE": True,
        "ALLOW_WIDTH": 3,
        "MV_DIR": "BOTH",
        "LANE_ITEMS": [
            {"NODE": 1, "OFFSET": -1.5},
            {"NODE": 2, "OFFSET": -1.5},
            {"NODE": 3, "OFFSET": -1.5},
            {"NODE": 4, "OFFSET": -1.5},
        ],
    }
})
print(result)
```

---

## 8. /db/SLANch – Traffic Surface Lanes – China

> 基于 China 标准的面车道。为各节点额外指定跨径长度（`SPAN_LENGTH`）。

**Input URI:** `{base url}/db/SLANch`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "LL_01",
      "WIDTH": 3,
      "WHEEL_SPACE": 1.8,
      "SKEW_START": 10,
      "SKEW_END": 15,
      "bOPTIMIZE": true,
      "ALLOW_WIDTH": 3,
      "MV_DIR": "BOTH",
      "LANE_ITEMS": [
        {"NODE": 1, "OFFSET": -1.5, "SPAN_LENGTH": 12},
        {"NODE": 2, "OFFSET": -1.5, "SPAN_LENGTH": 12}
      ]
    }
  }
}
```

### Parameters – LANE_ITEMS

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Node No. | `"NODE"` | Integer | – | Required |
| 2 | Offset Distance to Lane Center | `"OFFSET"` | Number | 0 | Optional |
| 3 | Span Length | `"SPAN_LENGTH"` | Number | 0 | Optional |

### Python 示例

```python
result = mv_post("SLANch", {
    "1": {
        "NAME": "SL_01",
        "WIDTH": 3,
        "WHEEL_SPACE": 1.8,
        "SKEW_START": 0,
        "SKEW_END": 0,
        "bOPTIMIZE": True,
        "ALLOW_WIDTH": 3,
        "MV_DIR": "BOTH",
        "LANE_ITEMS": [
            {"NODE": 1, "OFFSET": -1.5, "SPAN_LENGTH": 12},
            {"NODE": 2, "OFFSET": -1.5, "SPAN_LENGTH": 12},
        ],
    }
})
print(result)
```

---

## 9. /db/SLANop – Traffic Surface Lanes – Moving Load Optimization

> 移动荷载优化专用面车道。搜索车道宽度内的最优位置。

**Input URI:** `{base url}/db/SLANop`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LANE_NAME": "LL_01",
      "SKEW_START": 10,
      "SKEW_END": 15,
      "MOVING": "BOTH",
      "OPTIMIZE_WIDTH": 4,
      "LANE_WIDTH": 3,
      "WHEEL_SPACE": 1.8288,
      "MARGIN": 0.1,
      "OFFSET_TYPE": 0,
      "DIVIDE_NUM": 2,
      "ITEMS": [
        {"NODE_KEY": 1, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": true},
        {"NODE_KEY": 2, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": false}
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Lane Name | `"LANE_NAME"` | String | – | Required |
| 2 | Skew Start | `"SKEW_START"` | Number | 0 | Optional |
| 3 | Skew End | `"SKEW_END"` | Number | 0 | Optional |
| 4 | Moving Direction | `"MOVING"` | String | – | Required |
| 5 | Optimization Width | `"OPTIMIZE_WIDTH"` | Number | – | Required |
| 6 | Lane Width | `"LANE_WIDTH"` | Number | – | Required |
| 7 | Wheel Spacing | `"WHEEL_SPACE"` | Number | 0 | Optional |
| 8 | Margin | `"MARGIN"` | Number | 0 | Optional |
| 9 | Offset Type (0=Fixed, 1=Division) | `"OFFSET_TYPE"` | Integer | – | Required |
| 10 | Number of Division | `"DIVIDE_NUM"` | Integer | – | Optional |
| 11 | Analysis Lane Offset | `"ANALYSIS_LANE_OFFSET"` | Number | – | Optional |
| 12 | Items | `"ITEMS"` | Array[Object] | – | Required |
| (1) | Node Key | `"NODE_KEY"` | Integer | – | Required |
| (2) | Offset | `"OFFSET"` | Number | 0 | Optional |
| (3) | Impact Factor / Centrifugal Force | `"FACTOR"` / `"CENT_F"` | Number | 0 | Optional |
| (4) | Span Start | `"SPAN_START"` | Boolean | false | Optional |

### Python 示例

```python
result = mv_post("SLANop", {
    "1": {
        "LANE_NAME": "SL_OP_01",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "OPTIMIZE_WIDTH": 4,
        "LANE_WIDTH": 3,
        "WHEEL_SPACE": 1.8288,
        "MARGIN": 0.1,
        "OFFSET_TYPE": 0,
        "DIVIDE_NUM": 2,
        "ITEMS": [
            {"NODE_KEY": 1, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": True},
            {"NODE_KEY": 2, "OFFSET": -1.5, "FACTOR": 1.25, "SPAN_START": False},
        ],
    }
})
print(result)
```

---

## 10. /db/MVHL – Vehicles

> 定义移动荷载车辆。通过 `STANDARD_CODE` 字段区分设计标准，同时支持预定义车辆（`VEHICLE_TYPE_NAME`）与自定义车辆（`USER_LOAD_TYPE`）。

**Input URI:** `{base url}/db/MVHL`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body – AASHTO Standard

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_H20-44",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H20-44",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    }
  }
}
```

### Request Body – AASHTO LRFD

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 2,
      "VEHICLE_LOAD_NAME": "US(ALL)_HL-93TRK",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HL-93TRK",
      "STANDARD_CODE": "AASHTO-LRFD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 25,
        "CENT_F": true
      }
    }
  }
}
```

### Request Body – Korea (KS-RB)

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 6,
      "VEHICLE_LOAD_NAME": "KR(SRB)_DB-24",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "DB-24",
      "STANDARD_CODE": "KS-RB",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    }
  }
}
```

### Parameters – 公共

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Moving Load Code (Integer) | `"MVLD_CODE"` | Integer | – | Required |
| 2 | Vehicular Load Name（用户指定） | `"VEHICLE_LOAD_NAME"` | String | – | Required |
| 3 | Vehicular Load Number | `"VEHICLE_LOAD_NUM"` | Integer | – | Required |
| 4 | Vehicular Type Name（标准车辆名称） | `"VEHICLE_TYPE_NAME"` | String | – | Required |
| 5 | Standard Code ¹⁾ | `"STANDARD_CODE"` | String | – | Required |
| 6 | User Load Type（自定义时） | `"USER_LOAD_TYPE"` | String | – | Optional |
| 7 | Default Parameters | `"VEH_DEFAULT"` | Object | – | Required |
| 8 | Load Items（自定义轴重数组） | `"LOAD_ITEMS"` | Array[Object] | – | Optional |

> ¹⁾ STANDARD_CODE 主要取值：`"AASHTO-STD"`, `"AASHTO-LRFD"`, `"KS-RB"`, `"KS2005"`, `"KSCE-LSD15"`, `"BS"`, `"EUROCODE"`, `"CANADA"`, `"AUSTRALIA"`, `"CHINA"`, `"INDIA"`, `"TAIWAN"`, `"POLAND"`, `"RUSSIA"`, `"SOUTH_AFRICA"`

### Parameters – VEH_DEFAULT（公共字段）

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Uniform Load | `"UNIFORM_LOAD"` | Number | – | Optional |
| 2 | Dynamic Load Allowance (%) | `"DYN_LOAD_ALLOWANCE"` | Number | – | Optional |
| 3 | Width 1 (W1) | `"W1"` | Number | – | Optional |
| 4 | Width 2 (W2) | `"W2"` | Number | – | Optional |
| 5 | Distance 1 (D1) | `"D1"` | Number | – | Optional |
| 6 | Distance 2 (D2) | `"D2"` | Number | – | Optional |
| 7 | Point Load (PL) | `"PL"` | Number | – | Optional |
| 8 | PLM | `"PLM"` | Number | – | Optional |
| 9 | PLV | `"PLV"` | Number | – | Optional |
| 10 | Add Centrifugal Force | `"CENT_F"` | Boolean | false | Optional |

### Parameters – LOAD_ITEMS（自定义车辆）

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Point Load | `"POINT_LOAD"` | Number | – | Required |
| 2 | Point Distance | `"POINT_DIST"` | Number | – | Required |

### Parameters – VEH_KSCE_LSD15（仅 `STANDARD_CODE: "KSCE-LSD15"` 使用）

> ℹ️ **2026-07-30 反映。** 当 `STANDARD_CODE` 为 `"KSCE-LSD15"` 时，不使用 `VEH_DEFAULT`，而使用本专用对象（官方手册中另有独立文章 ["Vehicles - KSCE-LSD15"](https://support.midasuser.com/hc/en-us/articles/35958367637273-Vehicles-KSCE-LSD15) 记载，故此前版本一直遗漏）。官方 Specifications 表按标准车辆（Standard）·自定义 Truck/Lane（1st·2nd Model）·Train·Lane 这 5 种情形区分必填/可选，因此下表以 JSON Schema 为准整合列出全部字段 — 实际必填与否随 `USER_LOAD_TYPE`/`LENGTH_LANE` 组合而变化，请参考示例。

| No. | Description | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | Load Type ¹⁾ — `0`=75% of Design Load / `1`=25% of Design Load | `"LOAD_TYPE"` | Integer | `0` | Optional |
| 2 | Lane Loaded Length（仅 User Defined Truck/Lane） | `"LOADED_LENGTH"` | Number | `60` | Optional |
| 3 | Distribution Load Not Exceeding Loaded Length | `"W1"` | Number | `12.7` | Optional |
| 4 | Distribution Load Exceeding Loaded Length | `"W2"` | Number | `12.7` | Optional |
| 5 | Spacing dD1（仅 User Defined Train） | `"D1"` | Number | `0` | Optional |
| 6 | Spacing dD2（仅 User Defined Train） | `"D2"` | Number | `0` | Optional |
| 7 | Exponent to Calculate Distribution Load of W2 | `"EXP"` | Number | `0.1` | Optional |
| 8 | Dynamic Load Allowance (%) | `"DYN_LOAD_ALLOWANCE"` | Number | `0` | Optional |
| 9 | Length of Lane Load · `0`=1st Model / `1`=2nd Model | `"LENGTH_LANE"` | Integer | — | Required |
| 10 | Length of Lane Load(User) — 当 `LENGTH_LANE: 0` 时 | `"LENGTH_LANE_USER"` | Number | `0` | Optional |
| 11 | Convert Point Load to Distributed Load | `"CONVERT_DIST_LOAD"` | Boolean | `false` | Optional |
| 12 | Number of Uniform Load（仅 Lane）· 若为 N 个则取 N-1 | `"UNIFORM_LOAD_NUM"` | Number | `0` | Optional |
| 13 | Uniform Load Distance（仅 Lane） | `"UNIFORM_LOAD_DIST"` | Number | `0` | Optional |
| 14 | Uniform Load（仅 Lane） | `"UNIFORM_LOAD_W"` | Number | — | Required |
| 15 | Uniform Load Length（仅 Lane） | `"UNIFORM_LOAD_LOAD_LENGTH_L"` | Number | — | Required |
| 16 | 轴重数组 | `"POINT_ITEMS"` | Array [Object] | — | Required |
| 16-1 | └ 荷载(Load) | `POINT_ITEMS[].POINT_LOAD` | Number | — | Required |
| 16-2 | └ 间距(Spacing) | `POINT_ITEMS[].POINT_DIST` | Number | — | Required |
| 16-3 | └ 等分布折算长度 — 当 `CONVERT_DIST_LOAD: true` 时 | `POINT_ITEMS[].POINT_DIST2` | Number | `0` | Optional |

> ¹⁾ 官方 Specifications 表中写有 `LOAD_TYPE` 仅适用于 `"KL-510LNE"`，但官方 Request Examples 在 `KL-510TRK`·`KL-510FTG` 标准车辆示例中同样包含 `"LOAD_TYPE": 0`。该字段本身在所有标准车辆请求中都会出现（默认值 `0`），只是取值 `1`（25% of Design Load）实际仅在 `KL-510LNE` 下有意义 — 按 CLAUDE.md 原则以示例为准反映。

**请求示例 — 标准车辆（Standard）**

```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 13,
      "VEHICLE_LOAD_NAME": "ST_KL-510TRK",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "KL-510TRK",
      "STANDARD_CODE": "KSCE-LSD15",
      "VEH_KSCE_LSD15": {
        "LOAD_TYPE": 0,
        "DYN_LOAD_ALLOWANCE": 25,
        "LENGTH_LANE": 0,
        "LENGTH_LANE_USER": 0,
        "CONVERT_DIST_LOAD": false,
        "POINT_ITEMS": [
          { "POINT_LOAD": 48, "POINT_DIST": 3.6 },
          { "POINT_LOAD": 135, "POINT_DIST": 1.2 },
          { "POINT_LOAD": 135, "POINT_DIST": 7.2 },
          { "POINT_LOAD": 192, "POINT_DIST": 0 }
        ]
      }
    }
  }
}
```

**请求示例 — 自定义（User Defined）Truck/Lane**

```json
{
  "Assign": {
    "8": {
      "MVLD_CODE": 13,
      "VEHICLE_LOAD_NAME": "UD_Truck/Lane1",
      "VEHICLE_LOAD_NUM": 2,
      "USER_LOAD_TYPE": "Truck/Lane",
      "VEH_KSCE_LSD15": {
        "LOADED_LENGTH": 60,
        "W1": 12.7,
        "W2": 12.7,
        "EXP": 0.1,
        "DYN_LOAD_ALLOWANCE": 25,
        "LENGTH_LANE": 0,
        "LENGTH_LANE_USER": 1.5,
        "CONVERT_DIST_LOAD": true,
        "POINT_ITEMS": [
          { "POINT_LOAD": 100, "POINT_DIST": 0.2, "POINT_DIST2": 0.45 }
        ]
      }
    }
  }
}
```

### Parameters – 各国专用 VEH_XX 对象

> ⚠️ **2026-08-25 确认。** 此前文档把 `VEH_DEFAULT` 写成对所有 `STANDARD_CODE` 通用，  
> 但实际上仅 AASHTO Standard/LRFD·PENNDOT·Korea(KS-RB)·Taiwan 这 5 个代码使用  
> `VEH_DEFAULT`，其余国家各自使用专用对象（`VEH_CA`/`VEH_BS`/`VEH_EUROCODE`/`VEH_AU`/  
> `VEH_PL`/`VEH_RU`/`VEH_ZA`/`VEH_CN`/`VEH_IN`），与 KSCE-LSD15 的 `VEH_KSCE_LSD15` 为同一  
> 模式。以下补充各国 Schema。Canada/Australia/South Africa/China/Poland 列出全部下级  
> 模式，BS/Eurocode/Russia/India 因原文本身极为庞大（多标准·10 个以上下级模式混在），  
> 仅文档化代表模式（与 SECT/TDMT 相同的“代表示例”原则）— 全部下级模式请参考  
> 各文档的原文链接。

**VEH_CA (Canada, `STANDARD_CODE: "CANADA"`)** — [原文](https://support.midasuser.com/hc/en-us/articles/35957455014041)

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 标准车辆公共 | | | | | |
| 1 | Dynamic Load Allowance Option · Auto:`0` · User:`1` | `"DYNA_FACTOR"`（`DYNA` 下级） | Integer | `0` | Optional |
| 2 | Dynamic Load Factor — 仅 1 轴时使用 | `"DYNA_FACT_1_AXLE"`(`DYNA` 下级) | Number | 0 | Optional |
| 3 | Dynamic Load Factor — 2 轴或 1·2·3 轴时使用 | `"DYNA_FACT_2_AXLE"`(`DYNA` 下级) | Number | 0 | Optional |
| 4 | Dynamic Load Factor — 3 轴及以上（不含 1·2·3 轴组合）时使用 | `"DYNA_FACT_3_AXLE"`(`DYNA` 下级) | Number | 0 | Optional |
| User Defined Vehicle - Truck/Lane 附加 | | | | | |
| 5 | Uniform Distribution Load | `"UNIFORM_LOAD"` | Number | 0 | Optional |
| 6 | 轴重数组 · `POINT_LOAD`/`POINT_DIST` | `"LOAD_ITEMS"` | Array [Object] | - | Optional |
| User Defined Vehicle - Permit Truck 附加 | | | | | |
| 7 | Permit Load | `"PERMIT_LOAD"` | Object | - | Required |
| (1) | └ Impact Factor | `PERMIT_LOAD.IMPACT_FACTOR` | Number | 0 | Optional |
| (2) | └ Axle Types 数组 · `AXLE_TYPE`/`EVENLY_DIST_LOAD`/`SYMMETRIC_VEHICLE`/`POINT_ITEMS`(`POINT_LOAD`/`POINT_DIST`) | `PERMIT_LOAD.AXLE_TYPES` | Array [Object] | - | Required |
| (3) | └ Permit Load 数组 · `AXLE_TYPE`/`SPACING`/`EQUAL_J_NVSIDX` | `PERMIT_LOAD.PERMIT_LOADS` | Array [Object] | - | Required |

```python
# Canada 标准车辆（CL-625 Truck, Auto Dynamic Load）
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 8,
        "VEHICLE_LOAD_NAME": "CA(Auto)_CL-625Truck",
        "VEHICLE_LOAD_NUM": 1,
        "VEHICLE_TYPE_NAME": "CL-625Truck",
        "STANDARD_CODE": "CANADA",
        "VEH_CA": {"DYN_LOAD_ALLOWANCE": 0, "DYNA": {"DYNA_FACTOR": 0}},
    }
})
```

**VEH_AU (Australia, `STANDARD_CODE: "AUSTRALIA"`)** — [原文](https://support.midasuser.com/hc/en-us/articles/35957830747033)

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| AS 5100.2 - Road Traffic | | | | | |
| 1 | Dynamic Load Allowance | `"DYN_LOAD_ALLOWANCE"` | Number | 0 | Optional |
| 2 | Fatigue Option（仅 `"M1600 without UDL"`） | `"FATIGUE"` | Boolean | `false` | Optional |
| AS 5100.2 - Rail Traffic Load | | | | | |
| 3 | Dynamic Load Allowance — Bending Moment | `"DYN_LOAD_ALLOWANCE"` | Number | 0 | Optional |
| 4 | Dynamic Load Allowance — All Other Effects | `"DYN_LOAD_ALLOWANCE2"` | Number | 0 | Optional |
| 5 | Increment of Distance | `"INCRE_LENGTH"` | Number | - | Required |
| AS 5100.2 - Heavy Load Platform & Rating Vehicles | | | | | |
| 6 | Uniform Distribution Load（`"L44 Lane Load"`，加载长度超过 150m 时） | `"W2"` | Number | 0 | Optional |
| User Defined - Truck/Lane | | | | | |
| 7 | Variable Spacing(D6~D7) Option | `"VAR_SPACING"` | Boolean | `false` | Optional |
| 8 | Fatigue Option | `"FATIGUE"` | Boolean | `false` | Optional |
| 9 | Uniform Distribution Load（当 `"FATIGUE"=true` 时） | `"UNIFORM_LOAD"` | Number | 0 | Optional |
| 10 | 轴重数组 · `POINT_LOAD`/`POINT_DIST` | `"LOAD_ITEMS"` | Array [Object] | - | Optional |
| User Defined - Train | | | | | |
| 11 | Uniform Distribution Load | `"W1"` | Number | 0 | Optional |
| 12 | Loaded Length | `"D1"` | Number | 0 | Optional |
| User Defined - Rail Traffic Load | | | | | |
| 13 | Group Number | `"GROUP_NUM"` | Integer | - | Required |
| User Defined - Permit Truck | | | | | |
| 14 | Permit Load（结构与 VEH_CA 相同） | `"PERMIT_LOAD"` | Object | - | Required |

```python
# Australia AS 5100.2 Road Traffic (M1600)
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 14,
        "VEHICLE_LOAD_NAME": "AU(Road)_M1600",
        "VEHICLE_LOAD_NUM": 1,
        "VEHICLE_TYPE_NAME": "M1600",
        "STANDARD_CODE": "ROAD TRAFFIC",
        "VEH_AU": {"DYN_LOAD_ALLOWANCE": 0.3},
    }
})
```

**VEH_ZA (South Africa, `STANDARD_CODE: "NA"`/`"NB"`/`"NC"`)** — [原文](https://support.midasuser.com/hc/en-us/articles/35958066812057)

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| NA Type | | | | | |
| 1 | Unit Length for Loaded Length Increment Option | `"INCRE_LENGTH"` | Boolean | `false` | Optional |
| 2 | Increment Length | `"INCRE_LENGTH_VALUE"` | Number | 0 | Optional |
| NB Type | | | | | |
| 3 | Number of Unit（36 或 24） | `"UNIT_NUM"` | Number | - | Required(标准)/Integer,Required(自定义) |
| NC Type | | | | | |
| 4 | Consider Load Area Giving Opposite Contribution | `"OPPOSITE"` | Boolean | `false` | Optional |
| User Defined - NA Type 附加 | | | | | |
| 5 | Uniform Distribution Load(加载长度以下) | `"W1"` | Number | - | Required |
| 6 | Uniform Distribution Load(加载长度超过) | `"W2"` | Number | - | Required |
| 7 | Uniform Distribution Load(加载长度超过，附加) | `"W3"` | Number | - | Required |
| 8 | Loaded Length | `"LOADED_LENGTH"` | Number | - | Required |
| 9 | Axle Load(Pa) | `"PA"` | Number | 0 | Optional |
| User Defined - NB Type 附加 | | | | | |
| 10 | Axle Load(Pb) | `"PB"` | Number | - | Required |
| 11 | Distance between Axle Load(End) | `"D1"` | Number | 0 | Optional |
| 12 | Distance between Axle Load(Middle) | `"D2"` | Number | 0 | Optional |
| 13 | Factor to Calculate D3~D6 | `"DELTA"` | Number | 0 | Optional |
| User Defined - NC Type 附加 | | | | | |
| 14 | Uniform Distribution Load | `"PRESSURE_LOAD"` | Number | - | Required |
| 15 | Number of Load [a,b,c] | `"NUM_LOAD_ARRAY"` | Array [Integer, 3] | - | Required |
| 16 | Different Discrete Lengths | `"POINT_DIST_ARRAY"` | Array [Object, 3] | - | Required |
| User Defined - Permit Truck 附加 | | | | | |
| 17 | Permit Load（结构与 VEH_CA 相同） | `"PERMIT_LOAD"` | Object | - | Required |

```python
# South Africa NA Type 标准车辆
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 16,
        "VEHICLE_LOAD_NAME": "ZA(TMH7)_NA",
        "VEHICLE_LOAD_NUM": 1,
        "VEHICLE_TYPE_NAME": "TMH7",
        "STANDARD_CODE": "NA",
        "VEH_ZA": {"INCRE_LENGTH": False},
    }
})
```

**VEH_CN (China, `STANDARD_CODE` 为 JTG/JTJ/CJJ/TB 等，参见原文 ¹⁾ 表)** — [原文](https://support.midasuser.com/hc/en-us/articles/35958523379353)

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| 标准车辆公共 | | | | | |
| 1 | Impact Factor (z) | `"IMPACT_COEF"` | Number | 0 | Optional |
| 2 | Width | `"CROWD_WIDTH"` | Number | 0 | Optional |
| 3 | Distance Between Center of Vehicles | `"DD"` | Number | 0 | Optional |
| User Defined - Truck/Lane 公共 | | | | | |
| 4 | Truck/Lane Type · Crawler:`1` · Lane1:`0` · GC:`2` · Lane2:`5` | `"TRUCK_TYPE"` | Integer | - | Required |
| 5 | Axle Load(P)，仅 Lane1 | `"P_"` | Number | 0 | Optional |
| 6 | Distribution Load 1(Qm)，仅 Lane1 | `"QM"` | Number | 0 | Optional |
| 7 | Distribution Load 2(Qq)/Uniform Load(qk)，Lane1·2 | `"QQ"` | Number | 0 | Optional |
| 8 | Axle Load(Pk) L≤，仅 Lane2 | `"PA"` | Number | 0 | Optional |
| 9 | Loaded Length(L≤)，仅 Lane2 | `"D1"` | Number | 0 | Optional |
| 10 | Axle Load(Pk) L≥，仅 Lane2 | `"PB"` | Number | 0 | Optional |
| 11 | Loaded Length(L≥)，仅 Lane2 | `"D2"` | Number | 0 | Optional |
| 12 | Uniform Distribution Load(dW1)，仅 Crawler | `"W_TRAILER"` | Number | 0 | Optional |
| 13 | Loaded Length(dD1)，仅 Crawler | `"D_TRAILER"` | Number | 0 | Optional |
| 14 | 轴重数组 · `POINT_LOAD`/`POINT_DIST` | `"LOAD_ITEMS"` | Array [Object] | - | Optional |
| User Defined - Train/Exceptional | | | | | |
| 15 | Train/Exceptional Type · Type1:`1` · Type2:`2` · Type3:`3` · Subway:`4` | `"TRAIN_TYPE"` | Integer | - | Required |
| 16 | Distribution Load dW1/dW2，仅 Type1·3 | `"W1"`/`"W2"` | Number | 0 | Optional |
| 17 | Spacing dD1/dD2，仅 Type1·3 | `"D1"`/`"D2"` | Number | 0 | Optional |
| 18 | Distance to Front/Rear of Heavy Vehicle，仅 Type2 | `"FD"`/`"BD"` | Number | 0 | Optional |
| 19 | Impact Factor Reduction Coefficient，仅 Subway | `"IMPACT_COEF"` | Number | 0 | Optional |
| 20 | Axle Load[P1~P4]/Distance[D1~D3]，仅 Subway | `"P_SUBWAY"`/`"D_SUBWAY"` | Array [Number,4]/[Number,3] | 0 | Optional |
| 21 | Distance between Carriages(dD)/Number of Carriage(1~15)，仅 Subway | `"CARRIAGE_DIST"`/`"NUM_CARRIAGE"` | Number/Integer | 0/- | Optional/Required |
| 22 | Axle load for Negative Influence Line(Po)，仅 Subway | `"P_OPPOSITE"` | Number | 0 | Optional |
| 23 | 附加轴重数组（用于 Type2 Heavy Vehicle） · `POINT_LOAD`/`POINT_DIST` | `"LOAD_ITEMS2"` | Array [Object] | - | Optional |
| User Defined - Crowd | | | | | |
| 24 | Crowd Load Type1 | `"VEHICLE_LOAD_USER_NUM"` | Integer | - | Required |
| 25 | Uniform Distribution Load(Type1) | `"W_CROWD"` | Number | 0 | Optional |
| 26 | Distribution Load dW/Loaded Length(Type2) | `"W_PRES_1"`/`"D1"`, `"W_PRES_2"`/`"D2"` | Number | 0 | Optional |
| 27 | Width(Type2) | `"DB"` | Number | 0 | Optional |

```python
# China Lane Load 1（Truck/Lane 自定义）
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 3,
        "VEHICLE_LOAD_NAME": "CN_UD_Lane1",
        "VEHICLE_LOAD_NUM": 2,
        "USER_LOAD_TYPE": "Truck/Lane",
        "VEH_CN": {"TRUCK_TYPE": 0, "P_": 130, "QM": 10.5, "QQ": 7},
    }
})
```

**VEH_PL (Poland, `STANDARD_CODE` 参见原文 ¹⁾ 表)** — [原文](https://support.midasuser.com/hc/en-us/articles/35957893970457)

| No. | Description | Key | Value Type | Default | Required |
| --- | --- | --- | --- | --- | --- |
| PN-85/S-10030 Road Bridge & User Truck/Lane 公共 | | | | | |
| 1 | Select Vehicle / Load Type · Vehicle S:`0` · K:`1` · 2S:`2` · Walkway:`3` | `"SEL_VEHICLE"`(标准)/`"SUB_TYPE"`(自定义) | String/Integer | - | Required |
| 2 | Uniform Distribution Pressure Load(用于 K·S 车辆) | `"PRESSURE_LOAD"` | Number | -(标准,Read Only)/0(自定义) | - |
| 3 | Horizontal Distance(仅 2S 车辆) | `"DSPACE"` | Number | -(标准,Read Only)/0(自定义) | - |
| 4 | Dynamic Amplification Factor Option | `"DYNAMIC_AMP_FACTOR"` | Boolean | `false` | Optional |
| 5 | Factor Type · Auto:`false` · User Input:`true` | `"USER_INPUT"` | Boolean | `false` | Optional |
| 6 | Factor Value | `"AMP"` | Number | 0 | Optional |
| 7 | 轴重数组 · `POINT_LOAD`/`POINT_DIST` | `"LOAD_ITEMS"` | Array [Object] | - | Optional |
| Military Load Class 公共 | | | | | |
| 8 | Select Vehicle(标准) / Load Type(自定义：Tracked=`0`，Wheeled=`1`) | `"SEL_VEHICLE"`/`"SUB_TYPE"` | String/Integer | - | Required |
| 9 | Nose to Tail Distance | `"NOSE_TAIL_DIST"` | Number | 0 | Optional |
| 10 | Number of Vehicle | `"NUM_VEHICLE"` | Integer/Number | 0 | Optional |
| 11 | Total Load(P)/Tracked Length(D)，仅 Tracked Vehicle | `"TOTAL_LOAD"`/`"TRACKED_LENGTH"` | Number | 0 | Optional |
| 12 | Wheel Spacing | `"WHEEL_SPACING"` | Number | 0 | Optional |
| User Defined - Permit Truck | | | | | |
| 13 | Permit Load（结构与 VEH_CA 相同） | `"PERMIT_LOAD"` | Object | - | Required |

```python
# Poland 标准 Vehicle K (PN-85/S-10030 Road Bridge)
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 15,
        "VEHICLE_LOAD_NAME": "PL_VehicleK",
        "VEHICLE_LOAD_NUM": 1,
        "VEHICLE_TYPE_NAME": "Vehicle K",
        "STANDARD_CODE": "PN-85/S-10030 - RoadBridge",
        "VEH_PL": {"SEL_VEHICLE": "Vehicle K", "DYNAMIC_AMP_FACTOR": False},
    }
})
```

**BS·Eurocode·Russia·India — 仅文档化代表模式。** 以下 4 个代码的原文本身涵盖多个标准（例如 BS 混有
BD37/01·BD21/01·BS5400·CS454·CS458，Russia 有 AK/SK/N14/N11/Subway Trains/Tramcars/NK-80/
NG-60/Walkway 等 10 个以上下级模式），因此仅以字段表保留最具代表性的模式，其余内容
以原文链接引导。

| 国家 | VEH_XX | 代表模式 | 代表模式主要字段 | 原文 |
| --- | --- | --- | --- | --- |
| BS | `VEH_BS` | HA(BD37/01·BD21/01) | `"LANE_FACTOR"`(0=BD37/01, 1=BD21/01, 2=User), `"ADD_DATA_BD2101"`(Boolean), `"ADD_DATA_AL"`(Number,Required), `"ADD_DATA_CATEGORY"`/`"ADD_DATA_LOAD_LEVEL"`(Integer), `"LANE_FACTOR_ARRAY"`(Array[Number,4], 仅 User) — HB 仅额外添加 `"UNIT_NUM"`(Number,Required) | [Vehicles - BS](https://support.midasuser.com/hc/en-us/articles/35957522468889) |
| Eurocode | `VEH_EUROCODE` | EN 1991-2:2003 Load Model 1 | `"SUB_TYPE"`(Integer,Required, Standard Code), `"TANDEM_ADJUST_VALUES"`(Array[Number,3]), `"UDL_ADJUST_VALUES"`(Array[Number,4]), `"AMP_VALUES"`(Array[Number,2], [Tandem,UDL] ψ系数) | [Vehicles - Eurocode](https://support.midasuser.com/hc/en-us/articles/35957725805977) |
| Russia | `VEH_RU` | Road/Railway Bridge (AK) | `"SUB_TYPE"`(Integer,Required), `"RUSSIA_K"`(Integer,Required), `"FATIGUE"`(Boolean), `"SAME_LOADED_L"`(Boolean), `"DYNA_FACTOR"`(0=Auto/1=User), `"DYNA_FACTOR_VALUE"`/`"DYNA_FACTOR_UDL_VALUE"`(User 时 Required), `"LOAD_FACTOR"`(0=Auto/1=User), `"LOAD_FACTOR_VALUE"`/`"LOAD_FACTOR_UDL_VALUE"`(User 时 Required), `"LANE_FACTORS_1"`/`"LANE_FACTORS_1_UDL"`(Array[Number,3]) | [Vehicles - Russia](https://support.midasuser.com/hc/en-us/articles/35958016039577) |
| India | `VEH_IN` | IRC:6 Standard Load | 多数标准车辆（Class A/B/AA/70R/40R 等）无需 `VEH_IN`，仅以 `STANDARD_CODE` 即可定义。仅 Footway 类型需额外添加 `"FOOTWAY"`(Number,Required)·`"FOOTWAY_WIDTH"`(Number,Required) | [Vehicles - India](https://support.midasuser.com/hc/en-us/articles/35958578983065) |

```python
# BS BD37/01 HA 标准车辆
mv_post("MVHL", {"1": {
    "MVLD_CODE": 10, "VEHICLE_LOAD_NAME": "BS_(BD37)_HA", "VEHICLE_LOAD_NUM": 1,
    "VEHICLE_TYPE_NAME": "HA", "STANDARD_CODE": "BSBD37/01",
    "VEH_BS": {"LANE_FACTOR": 0},
}})

# Eurocode EN1991-2 Load Model 1
mv_post("MVHL", {"1": {
    "MVLD_CODE": 11, "VEHICLE_LOAD_NAME": "EU_(R)_LoadModel1", "VEHICLE_LOAD_NUM": 1,
    "VEHICLE_TYPE_NAME": "LoadModel1",
    "VEH_EUROCODE": {"SUB_TYPE": 19, "AMP_VALUES": [0.75, 0.4],
                      "TANDEM_ADJUST_VALUES": [1, 1, 1], "UDL_ADJUST_VALUES": [1, 1, 1, 1]},
}})

# Russia AK (Auto Dynamic/Load Factor)
mv_post("MVHL", {"1": {
    "MVLD_CODE": 12, "VEHICLE_LOAD_NAME": "RU_(RB)_AK_Auto", "VEHICLE_LOAD_NUM": 1,
    "VEHICLE_TYPE_NAME": "AK",
    "VEH_RU": {"SUB_TYPE": 1, "RUSSIA_K": 14, "DYNA_FACTOR": 0, "FATIGUE": True,
               "LOAD_FACTOR": 0, "LANE_FACTORS_1": [1, 0.6, 0.3],
               "LANE_FACTORS_1_UDL": [1, 0.6, 0.3], "SAME_LOADED_L": True},
    "LOAD_ITEMS": [{"POINT_LOAD": 10, "POINT_DIST": 1.5}, {"POINT_LOAD": 10, "POINT_DIST": 0}],
}})

# India IRC:6 Class A（无需 VEH_IN）/ Footway（需要 VEH_IN）
mv_post("MVHL", {
    "1": {"MVLD_CODE": 7, "VEHICLE_LOAD_NAME": "IN(IRC6)_ClassA", "VEHICLE_LOAD_NUM": 1,
          "VEHICLE_TYPE_NAME": "ClassA", "STANDARD_CODE": "IRC:6-2000"},
    "6": {"MVLD_CODE": 7, "VEHICLE_LOAD_NAME": "IN(IRC6)_Footway", "VEHICLE_LOAD_NUM": 1,
          "VEHICLE_TYPE_NAME": "Footway", "STANDARD_CODE": "IRC:6-2000",
          "VEH_IN": {"FOOTWAY": 4.903325, "FOOTWAY_WIDTH": 3}},
})
```

### Python 示例

```python
# KSCE-LSD15 标准的预定义车辆 — MVLD_CODE 使用 KSCE-LSD15 专用代码(13)
result = mv_post("MVHL", {
    "1": {
        "MVLD_CODE": 13,   # KSCE-LSD15 代码
        "VEHICLE_LOAD_NAME": "KL-510FTG",
        "VEHICLE_LOAD_NUM": 1,
        "VEHICLE_TYPE_NAME": "ST_KL-510FTG",
        "STANDARD_CODE": "KSCE-LSD15",
        "VEH_KSCE_LSD15": {
            "LOAD_TYPE": 0,
            "DYN_LOAD_ALLOWANCE": 15,
            "LENGTH_LANE": 0,
            "LENGTH_LANE_USER": 0,
            "CONVERT_DIST_LOAD": False,
            "POINT_ITEMS": [
                {"POINT_LOAD": 38.4, "POINT_DIST": 3.6},
                {"POINT_LOAD": 108, "POINT_DIST": 1.2},
                {"POINT_LOAD": 108, "POINT_DIST": 7.2},
                {"POINT_LOAD": 153.6, "POINT_DIST": 0},
            ],
        },
    }
})
print(result)
```

---

## 11. /db/MVHLtr – Vehicles – Transverse

> 用于 Transverse 移动荷载代码的车辆。定义横桥向布置参数。

**Input URI:** `{base url}/db/MVHLtr`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "Trans",
      "P": 120,
      "W": 2.3,
      "LW": 10,
      "NUM": 4,
      "DW": 0.3,
      "DV": 0.4,
      "DE": 0.5,
      "OPT_MEDIAN_STRIP": false
    },
    "2": {
      "NAME": "Trans_Medians",
      "P": 120,
      "W": 2.3,
      "LW": 10,
      "NUM": 4,
      "DW": 0.3,
      "DV": 0.4,
      "DE": 0.5,
      "OPT_MEDIAN_STRIP": true,
      "ML": 15,
      "MW": 1,
      "LEFT_LANES": 2
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Vehicular Load Name | `"NAME"` | String | – | Required |
| 2 | Wheel Load (P) | `"P"` | Number | – | Required |
| 3 | Distribution Width | `"W"` | Number | – | Required |
| 4 | Longitudinal Width | `"LW"` | Number | – | Required |
| 5 | Max. Number of Lanes (n) | `"NUM"` | Integer | – | Required |
| 6 | Distance between Wheels (Dw) | `"DW"` | Number | – | Required |
| 7 | Min. Distance between Vehicle (Dv) | `"DV"` | Number | – | Required |
| 8 | Edge Distance of Wheel Loads (De) | `"DE"` | Number | 0 | Optional |
| 9 | Median Strip Option | `"OPT_MEDIAN_STRIP"` | Boolean | false | Optional |
| 10 | Location (Ml) | `"ML"` | Number | – | Required (if OPT_MEDIAN_STRIP=true) |
| 11 | Width (Mw) | `"MW"` | Number | – | Required (if OPT_MEDIAN_STRIP=true) |
| 12 | Max. Number of Left Lanes (n1) | `"LEFT_LANES"` | Integer | – | Required (if OPT_MEDIAN_STRIP=true) |

### Python 示例

```python
result = mv_post("MVHLtr", {
    "1": {
        "NAME": "Trans_Basic",
        "P": 120,
        "W": 2.3,
        "LW": 10,
        "NUM": 4,
        "DW": 0.3,
        "DV": 0.4,
        "DE": 0.5,
        "OPT_MEDIAN_STRIP": False,
    }
})
print(result)
```

---

## 12. /db/MVLD – Moving Load Cases

> 定义移动荷载工况。支持 General Load、Permit Vehicle、Moving Load Optimization 三种类型，且结构随移动荷载代码而异。

**Input URI:** `{base url}/db/MVLD`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body – KSCE-LSD15 (General Load)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "TYPE": 0,
      "DEFAULT": {
        "SCALE_FACTORS": [1, 0.9, 0.8, 0.7, 0.65, 0.65],
        "COMB_OPTION": "COMBINED",
        "LANE_FACTOR_TYPE": 1,
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_TYPE": "VL",
            "VEHICLE_NAME": "ST_KL-510FTG",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": ["LL_01", "LL_02"]
          }
        ]
      }
    }
  }
}
```

### Request Body – AASHTO LRFD (Permit Vehicle)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Permit",
      "DESC": "",
      "TYPE": 1,
      "PERMIT_LOAD": {
        "VEHICLE_LOAD_NAME": "UD_PermitTruck",
        "REF_LANE": "LL_01",
        "SCALE_FACTOR": 1
      }
    }
  }
}
```

### Request Body – Moving Load Optimization

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Optimize",
      "DESC": "",
      "TYPE": 2,
      "AUTO_OPTIMIZE": {
        "LANE_NAME": "LL_01",
        "SCALE_FACTORS": [1.2, 1, 0.85, 0.65, 0.65, 0.65],
        "MIN_VEHL_DIST": 1,
        "MIN_NUM_VEHICLE": 1,
        "MAX_NUM_VEHICLE": 2,
        "OPTIMIZE_ITEMS": [
          {"VEHICLE_TYPE": "VL", "VEHICLE_NAME": "HL-93TRK", "SCALE_FACTOR": 1}
        ]
      }
    }
  }
}
```

### Parameters – 公共

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Load Type (0=General, 1=Permit, 2=Optimization) | `"TYPE"` | Integer | – | Required |

### Parameters – DEFAULT (General Load, KSCE-LSD15 / AASHTO STD / LRFD / PENNDOT / Taiwan / Canada)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Lane Factor Type (1=Multiple Presence Factor) | `"LANE_FACTOR_TYPE"` | Integer | – | Required |
| 2 | Multiple Presence Factor [L1~L6+] | `"SCALE_FACTORS"` | Array[Number, 6] | – | Required |
| 3 | Loading Effect (`"COMBINED"` / `"INDEPENDENT"`) | `"COMB_OPTION"` | String | – | Required |
| 4 | Sub Load Cases | `"SUB_LOAD_DATAS"` | Array[Object] | – | Required |
| (i) | Vehicle Type (`"VL"` / `"VC"`) | `"VEHICLE_TYPE"` | String | – | Required |
| (ii) | Vehicle Name | `"VEHICLE_NAME"` | String | – | Required |
| (iii) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |
| (iv) | Min. Number of Loaded Lane | `"MIN_LOADED_LANE"` | Integer | – | Required |
| (v) | Max. Number of Loaded Lane | `"MAX_LOADED_LANE"` | Integer | – | Required |
| (vi) | Selected Lanes | `"LANE_NAMES"` | Array[String] | – | Required |

### Parameters – DEFAULT（Korea – 附加字段）

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Lane Factor Type (0=Multi-Lane KS Rail, 1=MPF) | `"LANE_FACTOR_TYPE"` | Integer | Required |
| 2 | 2-Lane Factor L1 | `"_2_LANE_FACTOR_1"` | Number | Required |
| 3 | 2-Lane Factor L2 | `"_2_LANE_FACTOR_2"` | Number | Required |
| 4~7 | 3+ Lane Factors (L1~L4) | `"_3_LANE_FACTOR_1"` ~ `"_3_LANE_FACTOR_4"` | Number | Required |

> ⚠️ 2026-08-25 确认：上表原文只有 Value Type 列而无 Required 列，此前文档也一并省略，但
> 重新核对 Specifications 表原文后发现 4 个字段均标注为 Required，故予以补充（原文文章
> [Moving Load Cases](https://support.midasuser.com/hc/en-us/articles/35959068573209)）。

### Parameters – DEFAULT（Australia – 附加字段）

> ⚠️ 2026-08-25 确认：此前文档默认为 Australia 也与 KSCE-LSD15/AASHTO 系列结构相同，
> 但实际额外增加 `LOAD_MODEL`(0~3)·`LOAD_COMB_TYPE`(荷载系数种类)·`FATIGUE`(Load Model 1
> 专用) 3 个字段，且 Heavy Load Platform(`LOAD_MODEL=2`) 不使用/同时使用独立的
> `ASL` 对象。

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Select Load Model · General:`0` · Fatigue:`1` · Heavy Load Platform:`2` · Rail Traffic Load:`3` | `"LOAD_MODEL"` | Integer | Required |
| 2 | Load Factor Type for Design Combination · Ultimate:`0` · Serviceability:`1` | `"LOAD_COMB_TYPE"` | Integer | Required |
| 3 | Fatigue Option（仅 `LOAD_MODEL`=1 Load Model Fatigue） | `"FATIGUE"` | Boolean | Required |

**ASL（Australia Heavy Load Platform 并用，`LOAD_MODEL`=2）**

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Unobstructed Lane Scale Factor(例：0.5) | `"MULTIPLE_FACTOR"` | Number | Required |
| 2 | Load Case Data — Heavy Load 车辆名称 | `"VEHICLE_LOAD_NAME"` | String | Required |
| 3 | Load Case Data — M1600/S1600 车辆名称 | `"VEHICLE_LOAD_NAME2"` | String | Required |
| 4 | Min. Number of Loaded Lanes | `"MIN_LOADED_LANE"` | Integer | Required |
| 5 | Max. Number of Loaded Lanes | `"MAX_LOADED_LANE"` | Integer | Required |
| 6 | Defined Lane | `"LINE_ITEMS"` | Object | Required |
| (1) | └ Selected Lanes | `LINE_ITEMS.NA_LLAN_NAMES` | Array[String] | Required |
| (2) | └ Heavy Load Lanes Start | `LINE_ITEMS.STRAD_LLAN1_NAMES` | Array[String] | Required |
| (3) | └ Heavy Load Lanes End | `LINE_ITEMS.STRAD_LLAN2_NAMES` | Array[String] | Required |

### Parameters – DEFAULT（Russia – 附加字段）

> ⚠️ 2026-08-25 确认：Russia 没有 `LANE_FACTOR_TYPE`/`SCALE_FACTORS`，取而代之增加 `LOAD_COMB_TYPE`
> （极限状态群组）。

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Load Combination Type · Limit State Group I:`0` · Group I - Fatigue:`1` · Group II:`2` | `"LOAD_COMB_TYPE"` | Integer | Required |

### Parameters – PERMIT_LOAD (TYPE=1)

> 仅 AASHTO LRFD·Canada·Australia 支持。

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Vehicle Load Name | `"VEHICLE_LOAD_NAME"` | String | Required |
| 2 | Reference Lane | `"REF_LANE"` | String | Required |
| 3 | Scale Factor | `"SCALE_FACTOR"` | Number | Required |

### Parameters – AUTO_OPTIMIZE (TYPE=2)

> 支持 AASHTO Standard/LRFD·PENNDOT·Canada·Australia·Russia。`LOAD_MODEL`·`FATIGUE` 为
> Australia 专用附加字段（⚠️ 2026-08-25 补充）。

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Multiple Presence Factor | `"SCALE_FACTORS"` | Array[Number, 6] | Required |
| 2 | Min. Vehicle Distance | `"MIN_VEHL_DIST"` | Number | Required |
| 3 | Loaded Lane Name | `"LANE_NAME"` | String | Required |
| 4 | Min. Number of Vehicle | `"MIN_NUM_VEHICLE"` | Integer | Required |
| 5 | Max. Number of Vehicle | `"MAX_NUM_VEHICLE"` | Integer | Required |
| 6 | Select Load Model（Australia 专用，取值与 DEFAULT 的 LOAD_MODEL 相同） | `"LOAD_MODEL"` | Integer | Optional |
| 7 | Fatigue Option（Australia 专用） | `"FATIGUE"` | Boolean | Optional |
| 8 | Optimize Items · `VEHICLE_TYPE`("VL"/"VC")/`VEHICLE_NAME`/`SCALE_FACTOR` | `"OPTIMIZE_ITEMS"` | Array[Object] | Required |

### 按代码支持的 Load Type ¹⁾

| 代码 | General Load | Load Case for Permit Vehicle | Moving Load Optimization |
| --- | --- | --- | --- |
| KSCE-LSD15 | O | - | - |
| Korea | O | - | - |
| AASHTO Standard | O | - | O |
| AASHTO LRFD | O | O | O |
| PENNDOT | O | - | O |
| Taiwan | O | - | - |
| Canada | O | O | O |
| Australia | O | O | O |
| Russia | O | - | O |

### Python 示例

```python
# KSCE-LSD15 General Load Case
result = mv_post("MVLD", {
    "1": {
        "LCNAME": "MV_KSCE_1",
        "DESC": "",
        "TYPE": 0,
        "DEFAULT": {
            "SCALE_FACTORS": [1, 0.9, 0.8, 0.7, 0.65, 0.65],
            "COMB_OPTION": "COMBINED",
            "LANE_FACTOR_TYPE": 1,
            "SUB_LOAD_DATAS": [
                {
                    "VEHICLE_TYPE": "VL",
                    "VEHICLE_NAME": "ST_KL-510FTG",
                    "SCALE_FACTOR": 1,
                    "MIN_LOADED_LANE": 1,
                    "MAX_LOADED_LANE": 2,
                    "LANE_NAMES": ["LL_01", "LL_02"],
                }
            ],
        },
    }
})
print(result)
```

---

## 13. /db/MVLDch – Moving Load Cases – China

> China 移动荷载工况。按桥梁类型单独指定车道系数。

**Input URI:** `{base url}/db/MVLDch`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "OPT_AUTO_OPTIMIZE": false,
      "BRIDGE_TYPE": 2,
      "SCALE_FACTOR_O": [1, 1, 0.8, 0.67, 0.6, 0.55, 0.55, 0.55],
      "SCALE_FACTOR_N": [1, 1, 0.78, 0.67, 0.6, 0.55, 0.52, 0.5],
      "SCALE_FACTOR_JTG": [1.2, 1, 0.78, 0.67, 0.6, 0.55, 0.52, 0.5],
      "LOADING_EFFECT": 1,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": ["LL_01", "LL_02"]
        }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Moving Load Optimization | `"OPT_AUTO_OPTIMIZE"` | Boolean | false | Optional |
| 4 | Bridge Type (0=Old Urban, 1=Highway/New Urban, 2=JTG B01-2014) | `"BRIDGE_TYPE"` | Integer | – | Required |
| 5 | Scale Factor for Old Urban Bridge [1~7, ≥8] | `"SCALE_FACTOR_O"` | Array[Number, 8] | – | Required |
| 6 | Scale Factor for Highway/New Urban Bridge | `"SCALE_FACTOR_N"` | Array[Number, 8] | – | Required |
| 7 | Scale Factor for JTG B01-2014 | `"SCALE_FACTOR_JTG"` | Array[Number, 8] | – | Required |
| 8 | Combination Option (0=Combined, 1=Independent) | `"LOADING_EFFECT"` | Integer | – | Required |
| General Load(`OPT_AUTO_OPTIMIZE`=false) | | | | | |
| 9 | Sub-Load Cases | `"SUB_LOAD_ITEMS"` | Array[Object] | – | Required |
| (i) | Vehicle Type (`"VL"` / `"VC"`) | `"VEHICLE_TYPE"` | String | – | Required |
| (ii) | Vehicle Class Name | `"VEHICLE_CLASS"` | String | – | Required |
| (iii) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |
| (iv) | Min. Number of Loaded Lanes | `"MIN_NUM_LOADED_LANES"` | Integer | – | Required |
| (v) | Max. Number of Loaded Lanes | `"MAX_NUM_LOADED_LANES"` | Integer | – | Required |
| (vi) | Selected Lanes | `"SELECTED_LANES"` | Array[String] | – | Required |
| Moving Load Optimization(`OPT_AUTO_OPTIMIZE`=true) | | | | | |
| 9 | Min. Vehicle Distance | `"MIN_VEHICLE_DIST"` | Number | – | Required |
| 10 | Loaded Lane Name | `"LOADED_LANE_NAME"` | String | – | Required |
| 11 | Min. Number of Vehicle | `"MIN_NUM_VEHICLE"` | Integer | – | Required |
| 12 | Max. Number of Vehicle | `"MAX_NUM_VEHICLE"` | Integer | – | Required |
| 13 | Assignment Vehicle | `"AUTO_OPTIMIZE_ITEMS"` | Array[Object] | – | Required |
| (i) | Vehicle Type (`"VL"` / `"VC"`) | `"VEHICLE_TYPE"` | String | – | Required |
| (ii) | Vehicle Class Name | `"VEHICLE_NAME"` | String | – | Required |
| (iii) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |

> ⚠️ 2026-08-25 确认：此前文档仅介绍 `OPT_AUTO_OPTIMIZE` 字段，实际取其 `true` 时使用的
> Moving Load Optimization 字段 5 个（`MIN_VEHICLE_DIST`~`AUTO_OPTIMIZE_ITEMS`）曾被遗漏
> （原文 [Moving Load Cases - China](https://support.midasuser.com/hc/en-us/articles/35960417354649)）。

### Python 示例

```python
# General Load
result = mv_post("MVLDch", {
    "1": {
        "LCNAME": "MV_China_1",
        "DESC": "",
        "OPT_AUTO_OPTIMIZE": False,
        "BRIDGE_TYPE": 2,
        "SCALE_FACTOR_O":   [1, 1, 0.80, 0.67, 0.60, 0.55, 0.55, 0.55],
        "SCALE_FACTOR_N":   [1, 1, 0.78, 0.67, 0.60, 0.55, 0.52, 0.50],
        "SCALE_FACTOR_JTG": [1.2, 1, 0.78, 0.67, 0.60, 0.55, 0.52, 0.50],
        "LOADING_EFFECT": 1,
        "SUB_LOAD_ITEMS": [
            {
                "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
                "VEHICLE_TYPE": "VL",
                "SCALE_FACTOR": 1,
                "MIN_NUM_LOADED_LANES": 1,
                "MAX_NUM_LOADED_LANES": 2,
                "SELECTED_LANES": ["LL_01", "LL_02"],
            }
        ],
    }
})
print(result)

# Moving Load Optimization
mv_post("MVLDch", {
    "2": {
        "LCNAME": "MV_China_Opt",
        "DESC": "",
        "OPT_AUTO_OPTIMIZE": True,
        "BRIDGE_TYPE": 2,
        "SCALE_FACTOR_O":   [1, 1, 0.80, 0.67, 0.60, 0.55, 0.55, 0.55],
        "SCALE_FACTOR_N":   [1, 1, 0.78, 0.67, 0.60, 0.55, 0.52, 0.50],
        "SCALE_FACTOR_JTG": [1.2, 1, 0.78, 0.67, 0.60, 0.55, 0.52, 0.50],
        "MIN_VEHICLE_DIST": 1,
        "LOADED_LANE_NAME": "LL_01",
        "MAX_NUM_VEHICLE": 2,
        "LOADING_EFFECT": 0,
        "AUTO_OPTIMIZE_ITEMS": [
            {"VEHICLE_NAME": "CH(CJJ11)_C-CD(A/B)", "VEHICLE_TYPE": "VL", "SCALE_FACTOR": 1},
            {"VEHICLE_NAME": "CH(CJJ11)_C-CL(A)", "VEHICLE_TYPE": "VL", "SCALE_FACTOR": 1},
        ],
    }
})
```

---

## 14. /db/MVLDid – Moving Load Cases – India

> India (IRC) 移动荷载工况。支持 Auto Live Load Combinations 与 Permit Vehicle。

**Input URI:** `{base url}/db/MVLDid`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_India_1",
      "DESC": "",
      "SCALE_FACTOR": [1, 0.9, 0.8, 0.8],
      "NUM_LOADED_LANES": 2,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS_1": "IN(IRC)_(25t1)_BroadGauge-1676mm",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": ["LL_01", "LL_02"]
        }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Multiple Presence Factor [1-2, 3, 4, ≥5] | `"SCALE_FACTOR"` | Array[Number, 4] | – | Required |
| 4 | Auto Live Load Combinations | `"OPT_AUTO_LL"` | Boolean | false | Optional |
| 5 | Load Cases for Permit Vehicle | `"OPT_LC_FOR_PERMIT_LOAD"` | Boolean | false | Optional |
| **General Load** | | | | | |
| 6 | Number of Loaded Lanes | `"NUM_LOADED_LANES"` | Integer | – | Required |
| 7 | Sub-Load Cases | `"SUB_LOAD_ITEMS"` | Array[Object] | – | Required |
| (i) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |
| (ii) | Min. Number of Loaded Lanes | `"MIN_NUM_LOADED_LANES"` | Integer | – | Required |
| (iii) | Max. Number of Loaded Lanes | `"MAX_NUM_LOADED_LANES"` | Integer | – | Required |
| (iv) | Vehicle | `"VEHICLE_CLASS_1"` | String | – | Required |
| (v) | Selected Lanes | `"SELECTED_LANES"` | Array[String] | – | Required |
| **Auto Live Load Combinations (OPT_AUTO_LL=true)** | | | | | |
| 6 | Number of Loaded Lanes | `"NUM_LOADED_LANES"` | Integer | – | Required |
| 7 | Sub-Load Cases | `"SUB_LOAD_ITEMS"` | Array[Object] | – | Required |
| (i) | Scale Factor | `"SCALE_FACTOR"` | Number | – | Required |
| (ii) | Vehicle Class I | `"VEHICLE_CLASS_1"` | String | – | Required |
| (iii) | Vehicle Class II | `"VEHICLE_CLASS_2"` | String | – | Required |
| (iv) | Vehicle Footway | `"FOOTWAY"` | String | – | Required |
| (v) | Carriageway Width | `"CARRIAGE_WAY_WIDTH"` | Number | – | Read Only |
| (vi) | Carriageway Loading | `"CARRIAGE_WAY_LOADING"` | Number | – | Read Only |
| (vii) | Selected Lanes for Carriageway | `"SELECTED_LANES"` | Array[String] | – | Required |
| (viii) | Selected Lanes for Footway | `"SELECTED_FOOTWAY_LANES"` | Array[String] | – | Required |
| **Permit Vehicle (OPT_LC_FOR_PERMIT_LOAD=true)** | | | | | |
| 6 | Permit Vehicle ID | `"PERMIT_VEHICLE"` | Integer | – | Required |
| 7 | Reference Lane ID | `"REF_LANE"` | Integer | – | Required |
| 8 | Eccentricity | `"ECCEN"` | Number | – | Required |
| 9 | Scale Factor | `"PERMIT_SCALE_FACTOR"` | Number | – | Required |

> ⚠️ 2026-08-25 确认：此前文档把 `SUB_LOAD_ITEMS` 仅标注为 "Array[Object]"，其实际下级字段全部
> 遗漏（General Load 与 Auto Live Load Combinations 两种模式使用互不相同的下级结构）。
> 按原文 [Moving Load Cases - India](https://support.midasuser.com/hc/en-us/articles/35961164029593)
> 予以补充。

### Python 示例

```python
result = mv_post("MVLDid", {
    "1": {
        "LCNAME": "MV_India_1",
        "DESC": "",
        "SCALE_FACTOR": [1, 0.9, 0.8, 0.8],
        "NUM_LOADED_LANES": 2,
        "SUB_LOAD_ITEMS": [
            {
                "VEHICLE_CLASS_1": "IN(IRC6)_ClassA",
                "SCALE_FACTOR": 1,
                "MIN_NUM_LOADED_LANES": 1,
                "MAX_NUM_LOADED_LANES": 2,
                "SELECTED_LANES": ["LL_01", "LL_02"],
            }
        ],
    }
})
print(result)

# Auto Live Load Combinations
mv_post("MVLDid", {
    "2": {
        "LCNAME": "MV_India_AutoLL",
        "DESC": "",
        "OPT_AUTO_LL": True,
        "SCALE_FACTOR": [1, 0.9, 0.8, 0.8],
        "NUM_LOADED_LANES": 2,
        "SUB_LOAD_ITEMS": [
            {
                "VEHICLE_CLASS_1": "IN(IRC6)_ClassA",
                "VEHICLE_CLASS_2": "IN(IRC6)_Class40R",
                "FOOTWAY": "IN(IRC6)_Footway",
                "SCALE_FACTOR": 1,
                "CARRIAGE_WAY_WIDTH": 0,
                "CARRIAGE_WAY_LOADING": 0,
                "SELECTED_LANES": ["LL_01", "LL_02"],
                "SELECTED_FOOTWAY_LANES": ["LL_03"],
            }
        ],
    }
})
```

---

## 15. /db/MVLDbs – Moving Load Cases – BS

> BS (British Standard) 移动荷载工况。

**Input URI:** `{base url}/db/MVLDbs`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_BS_1",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "STANDER",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_STANDARD": {
        "LOADINGEFFECT": "INDEPEND",
        "SUBLOADDATA": [
          {
            "SCALEFACTOR": 1,
            "NUMLOADEDLANE": 4,
            "VEHICLE_NAME": "BS_(BD21)_HA&HB(Auto)",
            "SELECTEDLANES": ["LL_01", "LL_02", "LL_03", "LL_04"],
            "STRAD_LANE": [
              {"STARDD_LANE_1": "LL_03", "STARDD_LANE_2": "LL_04"}
            ]
          }
        ]
      }
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Moving Load Optimization | `"bAUTOOPTIMIZE"` | Boolean | false | Optional |
| 4 | Load Model · Standard(BD37/01,BS5400):`"STANDER"` · Special(BD86/11):`"SPECAIL"` · CS454 ALL Mode1:`"ALL_MODE_1"` · CS454 ALL Mode2:`"ALL_MODE_2"` | `"LOADMODEL"` | String | – | Required |
| 5 | Auto Live Load Combination | `"bAUTOLIVELOADCOMB"` | Boolean | false | Optional |
| 6 | Design Combination Factor Type · 当 `"bAUTOLIVELOADCOMB"`=true 时 · Ultimate:`"ULTIMATE"` · Serviceability:`"SERVICEABIL"` | `"DGNCOMBFACTORTYPE"` | String | – | Required |
| 7 | Combination Method · 当 `"bAUTOLIVELOADCOMB"`=true 时 · Comb.1:`"COMB_1"` · Comb.2/3:`"COMB_2_3"` | `"COMBMETHOD"` | String | – | Required |
| 8 | Standard Load Case Data(General, `LOADMODEL`="STANDER") | `"LCDATA_STANDARD"` | Object | – | Required |
| 9 | Special Load Case Data(General, `LOADMODEL`="SPECAIL") | `"LCDATA_SPECIAL"` | Object | – | Required |
| 10 | CS 454 Assessment Data(General, `LOADMODEL`="ALL_MODE_1"/"ALL_MODE_2") | `"LCDATA_ALLMODE"` | Object | – | Required |
| 11 | Standard Load Case Data(Optimization, `bAUTOOPTIMIZE`=true & `LOADMODEL`="STANDER") | `"LCDATA_STANDARD_OPTI"` | Object | – | Required |
| 12 | Special Load Case Data(Optimization, `LOADMODEL`="SPECAIL") | `"LCDATA_SPECIAL_OPTI"` | Object | – | Required |
| 13 | CS 454 Assessment Data(Optimization, `LOADMODEL`="ALL_MODE_1"/"ALL_MODE_2") | `"LCDATA_ALLMODE_OPTI"` | Object | – | Required |

**LCDATA_STANDARD（`LOADMODEL`="STANDER"，General Load 时的代表示例）**

| No. | Description | Key | Value Type | Required |
| --- | --- | --- | --- | --- |
| 1 | Loading Effect(`"INDEPEND"`) | `"LOADINGEFFECT"` | String | Required |
| 2 | Sub-Load Cases | `"SUBLOADDATA"` | Array [Object] | Required |
| (1) | └ Scale Factor | `SUBLOADDATA[].SCALEFACTOR` | Number | Required |
| (2) | └ Number of Loaded Lanes | `SUBLOADDATA[].NUMLOADEDLANE` | Integer | Required |
| (3) | └ Vehicle Name | `SUBLOADDATA[].VEHICLE_NAME` | String | Required |
| (4) | └ Selected Lanes | `SUBLOADDATA[].SELECTEDLANES` | Array [String] | Required |
| (5) | └ HB Straddling Two Lanes(`STARDD_LANE_1`/`STARDD_LANE_2`) | `SUBLOADDATA[].STRAD_LANE` | Array [Object] | Required |

> ⚠️ 2026-08-25 确认：此前文档缺少 `LOADMODEL` 的第 4 个取值 `"ALL_MODE_2"`，
> 且 `LCDATA_STANDARD`/`LCDATA_SPECIAL`/`LCDATA_ALLMODE` 的下级字段全部以及 Moving Load Optimization
> 专用的 3 个对象（`LCDATA_STANDARD_OPTI`/`LCDATA_SPECIAL_OPTI`/`LCDATA_ALLMODE_OPTI`）完全遗漏。
> 原文本身是一篇涵盖 4 个 Load Model × General/Optimization 2 种模式 = 接近 8 种组合的大型文章
> （与 SECT/TDMT 同一原则），故仅对最具代表性的 `LCDATA_STANDARD` 列出全部字段，其余 5 个对象
> 以下方摘要表整理 — 全部字段请参考原文
> [Moving Load Cases - BS](https://support.midasuser.com/hc/en-us/articles/35961459443737)。

| 对象 | 使用条件 | 主要字段 |
| --- | --- | --- |
| `LCDATA_SPECIAL` | General, `LOADMODEL`="SPECAIL" | `VEHICLE_NAME`(标准车辆)·`SPECIAL_VIHICLE_NAME`(特殊车辆)·`SELECTEDLANES`·`STRAD_LANE`(均为 String/Array[String]/Array[Object], Required) |
| `LCDATA_ALLMODE` | General, `LOADMODEL`="ALL_MODE_1"/"ALL_MODE_2" | 与 `LCDATA_SPECIAL` 相同的 4 个字段 + `REMAINING_LANE`(Array[String]，仅 ALL_MODE_1) |
| `LCDATA_STANDARD_OPTI` | Optimization, `LOADMODEL`="STANDER" | `LOADINGEFFECT` + `OPTI_BASE`(`MINVEHLDIST`/`ASSIGN_LANE`/`NUMLOADEDLANES`) + `OPTI_VEHICLE_BASE`(Array, `VEHICLE_TYPE`"VL"/"VC"·`VEHICLE_NAME`·`SCALE_FACTOR`) |
| `LCDATA_SPECIAL_OPTI` | Optimization, `LOADMODEL`="SPECAIL" | `VEHICLE_NAME`·`SPECIAL_VIHICLE_NAME` + `OPTI_BASE`(同上 3 个字段) |
| `LCDATA_ALLMODE_OPTI` | Optimization, `LOADMODEL`="ALL_MODE_1"/"ALL_MODE_2" | 与 `LCDATA_SPECIAL_OPTI` 相同 + `REMAINING_LANE`(仅 ALL_MODE_1) |

### Python 示例

```python
result = mv_post("MVLDbs", {
    "1": {
        "LCNAME": "MV_BS_Standard",
        "DESC": "",
        "bAUTOOPTIMIZE": False,
        "LOADMODEL": "STANDER",
        "bAUTOLIVELOADCOMB": True,
        "DGNCOMBFACTORTYPE": "ULTIMATE",
        "COMBMETHOD": "COMB_1",
        "LCDATA_STANDARD": {
            "LOADINGEFFECT": "INDEPEND",
            "SUBLOADDATA": [
                {
                    "SCALEFACTOR": 1,
                    "NUMLOADEDLANE": 4,
                    "VEHICLE_NAME": "BS_(BD21)_HA&HB(Auto)",
                    "SELECTEDLANES": ["LL_01", "LL_02", "LL_03", "LL_04"],
                    "STRAD_LANE": [
                        {"STARDD_LANE_1": "LL_03", "STARDD_LANE_2": "LL_04"}
                    ],
                }
            ],
        },
    }
})
print(result)
```

---

## 16. /db/MVLDeu – Moving Load Cases – Eurocode

> Eurocode (EN 1991-2) 移动荷载工况。支持 5 种 Load Model 类型（`TYPE_LOADMODEL`），且各类型均有 **General Load** / **Moving Load Optimization**（`OPT_AUTO_OPTIMIZE`）两种输入模式。

**Input URI:** `{base url}/db/MVLDeu`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body – LM 1 / FLM 1 / Footbridge (TYPE_LOADMODEL = 1, General Load)

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 1,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(FF)_Uniformload(Road)",
      "OPT_LEADING": false,
      "SLN_LIST": ["LL_01", "LL_02"],
      "SRA_LIST": ["LL_04"],
      "FLN_LIST": ["LL_03"]
    }
  }
}
```

### Request Body – LM 2/3/4, FLM 2/3/4, Permit Truck (TYPE_LOADMODEL = 2, General Load)

```json
{
  "Assign": {
    "2": {
      "LCNAME": "MV_Case2",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 2,
      "DESC": "",
      "OPT_COMB": 1,
      "OPT_LEADING": true,
      "SUB_LOAD_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_ConcentratedLoad",
          "SCALE_FACTOR": 1,
          "MIN_LOAD_LANE_TYPE": 1,
          "MAX_LOAD_LANE_TYPE": 4,
          "SLN_LIST": ["LL_01", "LL_02", "LL_03", "LL_04"]
        }
      ]
    }
  }
}
```

### Request Body – LM 1 & 3 Multi (TYPE_LOADMODEL = 3, General Load)

```json
{
  "Assign": {
    "3": {
      "LCNAME": "MV_Case3",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 3,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "UD_LoadModel3",
      "OPT_LEADING": false,
      "SLN_LIST": ["LL_01", "LL_02"],
      "SRA_LIST": ["LL_04"]
    }
  }
}
```

### Request Body – LM 1 & 3 Multi (Straddling) (TYPE_LOADMODEL = 4, General Load)

```json
{
  "Assign": {
    "4": {
      "LCNAME": "MV_Case4",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 4,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(R)_LoadModel3(UKNA)_SOV250_Auto",
      "OPT_LEADING": false,
      "SLN_LIST": ["LL_01", "LL_03", "LL_04"],
      "SRA_LIST": ["LL_02"],
      "STL_LIST": [
        {"NAME1": "LL_03", "NAME2": "LL_04"}
      ]
    }
  }
}
```

### Request Body – Railway Bridge (TYPE_LOADMODEL = 5, General Load)

```json
{
  "Assign": {
    "5": {
      "LCNAME": "MV_Case5",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 5,
      "DESC": "",
      "OPT_COMB": 1,
      "SCALE_FACTOR1": 0.8,
      "SCALE_FACTOR2": 0.7,
      "SCALE_FACTOR3": 0.6,
      "OPT_PSI_FACTOR": false,
      "MULTI_FACTOR1": 1,
      "MULTI_FACTOR2": 1,
      "MULTI_FACTOR3": 0.75,
      "SUB_LOAD_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(RFL)_HSLMB",
          "SCALE_FACTOR": 1,
          "MIN_LOAD_LANE_TYPE": 1,
          "MAX_LOAD_LANE_TYPE": 4,
          "SLN_LIST": ["LL_01", "LL_02", "LL_03", "LL_04"]
        }
      ]
    }
  }
}
```

### Request Body – Moving Load Optimization（OPT_AUTO_OPTIMIZE = true，例：LM 1）

```json
{
  "Assign": {
    "6": {
      "LCNAME": "MV_Case6",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 1,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(FF)_Uniformload(Road)",
      "OPT_LEADING": false,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_01",
      "LOADEDLANE": 3,
      "SLN_LIST": ["LL_01", "LL_03", "LL_04"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Load Model Type ¹⁾ | `"TYPE_LOADMODEL"` | Integer | – | Required |
| 4 | Moving Load Optimization (General Load: `false` / Optimization: `true`) | `"OPT_AUTO_OPTIMIZE"` | Boolean | false | Optional |
| 5 | Ignore ψ(1) factor | `"OPT_LEADING"` | Boolean | – | Required (LM1/3/4, General·Optimization) |
| 6 | Load Case – Vehicle | `"VHLNAME1"` | String | – | Required (LM1/3/4) |
| 7 | Load Case – Footway | `"VHLNAME2"` | String | – | Optional (LM1) / Required (LM3/4, Optimization) |
| 8 | Selected Lanes | `"SLN_LIST"` | Array[String] | – | Required (LM1/3/4) |
| 9 | Remaining Area | `"SRA_LIST"` | Array[String] | – | Required (LM1/3/4) |
| 10 | Footway Lanes (LM1) | `"FLN_LIST"` | Array[String] | – | Required (LM1) |
| 11 | Straddling Lanes — `(1)` Start Lane `"NAME1"`, `(2)` End Lane `"NAME2"` | `"STL_LIST"` | Array[Object] | – | Required (LM4) |
| 12 | Loading Effect (Combined: `0` / Independent: `1`) | `"OPT_COMB"` | String | – | Required (LM2/5) |
| 13 | Sub-Load Cases — `(1)` Vehicle Load Type ²⁾ `"TYPE"`, `(2)` Name `"NAME"`, `(3)` Scale Factor `"SCALE_FACTOR"`, `(4)` Min. Loaded Lanes `"MIN_LOAD_LANE_TYPE"`, `(5)` Max. Loaded Lanes `"MAX_LOAD_LANE_TYPE"`, `(6)` Selected Lanes `"SLN_LIST"` | `"SUB_LOAD_LIST"` | Array[Object] | – | Required (LM2/5, General) |
| 14 | Ignore ψ1 factor | `"OPT_PSI_FACTOR"` | Boolean | – | Required (LM5) |
| 15 | ψ1 factor for Lane 1/2/3+ | `"SCALE_FACTOR1"/"SCALE_FACTOR2"/"SCALE_FACTOR3"` | Number | – | Required (LM5) |
| 16 | Multi Presence Factor for Lane 1/2/3+ | `"MULTI_FACTOR1"/"MULTI_FACTOR2"/"MULTI_FACTOR3"` | Number | – | Required (LM5) |
| 17 | Min. Vehicle Distance | `"MINVHLDIST"` | Number | – | Required (Optimization) |
| 18 | Assignment Lane | `"OPTIMIZE_LANE_NAME"` | String | – | Required (Optimization) |
| 19 | Number of Loaded Lane | `"LOADEDLANE"` | Integer | – | Required (Optimization, LM1/3/4) |
| 20 | Min./Max. Number of Vehicle | `"MIN_NUM_VHL"/"MAX_NUM_VHL"` | Integer | – | Required (Optimization, LM2/5) |
| 21 | Sub-Load Cases for Optimization — `(1)` Type `"TYPE"`, `(2)` Name `"NAME"`, `(3)` Scale Factor `"SCALE_FACTOR"` | `"OPTIMIZE_LIST"` | Array[Object] | – | Required (Optimization, LM2/5) |

> ¹⁾ TYPE_LOADMODEL:  
> 1 = LM 1, FLM 1 / Footbridge  
> 2 = LM 2, 3, 4 / FLM 2, 3, 4 / Footbridge / Permit Truck  
> 3 = LM 1 & 3 Multi  
> 4 = LM 1 & 3 Multi (Straddling)  
> 5 = Railway Bridge
>
> ²⁾ Vehicle Load Type(`"TYPE"`)：Vehicle Class = `1`（Eurocode 不使用）/ Vehicle Load = `2`（Eurocode 固定值）

### Python 示例

```python
result = mv_post("MVLDeu", {
    "1": {
        "LCNAME": "MV_Case1",
        "OPT_AUTO_OPTIMIZE": False,
        "TYPE_LOADMODEL": 1,
        "DESC": "",
        "VHLNAME1": "EU_(R)_LoadModel1",
        "VHLNAME2": "EU_(FF)_Uniformload(Road)",
        "OPT_LEADING": False,
        "SLN_LIST": ["LL_01", "LL_02"],
        "SRA_LIST": ["LL_04"],
        "FLN_LIST": ["LL_03"],
    }
})
print(result)
```

---

## 17. /db/MVLDpl – Moving Load Cases – Poland

> Poland 移动荷载工况。支持 3 种 Load Model（Vehicle S、Vehicle K、Military）。

**Input URI:** `{base url}/db/MVLDpl`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV1",
      "DESC": "",
      "LOAD_MODEL": 1,
      "bAUTO_OPTIMIZE": false,
      "bPERMIT_LOAD": false,
      "DEFAULT": {
        "COMB_OPTION": "INDEPENDENT",
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_NAME": "VehicleS",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": ["L1", "L2"]
          }
        ]
      }
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Moving Load Optimization | `"bAUTO_OPTIMIZE"` | Boolean | false | Optional |
| 4 | Load Case for Permit Vehicle | `"bPERMIT_LOAD"` | Boolean | false | Optional |
| 5 | Load Model (1=Vehicle S/2S/Permit, 2=Vehicle K, 3=Military) | `"LOAD_MODEL"` | Integer | – | Required |
| **General Load(`bAUTO_OPTIMIZE`=false, `bPERMIT_LOAD`=false)** | | | | | |
| 6 | Sub-Load Cases | `"DEFAULT"` | Object | – | Required |
| **Vehicle S/2S/Permit(LOAD_MODEL=1)** | | | | | |
| (1) | Loading Effect(`"COMBINED"`/`"INDEPENDENT"`) | `DEFAULT.COMB_OPTION` | String | – | Required |
| (2) | Sub-Load Data | `DEFAULT.SUB_LOAD_DATAS` | Array[Object] | – | Required |
| (2-i) | └ Vehicle Name | `SUB_LOAD_DATAS[].VEHICLE_NAME` | String | – | Required |
| (2-ii) | └ Scale Factor | `SUB_LOAD_DATAS[].SCALE_FACTOR` | Number | – | Required |
| (2-iii) | └ Min. Number of Loaded Lane | `SUB_LOAD_DATAS[].MIN_LOADED_LANE` | Integer | – | Required |
| (2-iv) | └ Max. Number of Loaded Lane | `SUB_LOAD_DATAS[].MAX_LOADED_LANE` | Integer | – | Required |
| (2-v) | └ Selected Lanes | `SUB_LOAD_DATAS[].LANE_NAMES` | Array[String] | – | Required |
| **Vehicle K/Military(LOAD_MODEL=2/3)** | | | | | |
| (1) | Vehicle Name | `DEFAULT.VEHICLE_LOAD_NAME` | String | – | Required |
| (2) | Sub-Load Data | `DEFAULT.SUB_LOAD_DATAS` | Array[Object] | – | Required |
| (2-i) | └ Selected Lanes | `SUB_LOAD_DATAS[].LANE_NAMES` | Array[String] | – | Required |
| **Moving Load Optimization(`bAUTO_OPTIMIZE`=true)** | | | | | |
| 6 | Sub-Load Cases | `"AUTO_OPTIMIZE"` | Object | – | Required |
| **Vehicle S/2S(LOAD_MODEL=1)** | | | | | |
| (1) | Min. Vehicle Distance | `AUTO_OPTIMIZE.MIN_VEHL_DIST` | Number | – | Required |
| (2) | Loaded Lane | `AUTO_OPTIMIZE.LANE_NAME` | String | – | Required |
| (3) | Min. Number of Vehicle | `AUTO_OPTIMIZE.MIN_NUM_VEHICLE` | Integer | – | Required |
| (4) | Max. Number of Vehicle | `AUTO_OPTIMIZE.MAX_NUM_VEHICLE` | Integer | – | Required |
| (5) | Loading Effect(`"COMBINED"`/`"INDEPENDENT"`) | `AUTO_OPTIMIZE.COMB_OPTION` | String | – | Required |
| (6) | Sub-Load Cases | `AUTO_OPTIMIZE.OPTIMIZE_ITEMS` | Array[Object] | – | Required |
| (6-i) | └ Vehicle Type(`"VL"`/`"VC"`) | `OPTIMIZE_ITEMS[].VEHICLE_TYPE` | String | – | Required |
| (6-ii) | └ Vehicle Name | `OPTIMIZE_ITEMS[].VEHICLE_NAME` | String | – | Required |
| (6-iii) | └ Scale Factor | `OPTIMIZE_ITEMS[].SCALE_FACTOR` | Number | – | Required |
| **Vehicle K/Military(LOAD_MODEL=2/3)** | | | | | |
| (1) | Vehicle Name | `AUTO_OPTIMIZE.VEHICLE_LOAD_NAME` | String | – | Required |
| (2) | Min. Vehicle Distance | `AUTO_OPTIMIZE.MIN_VEHL_DIST` | Number | – | Required |
| (3) | Loaded Lane | `AUTO_OPTIMIZE.LANE_NAME` | String | – | Required |
| (4) | Number of Loaded Lanes | `AUTO_OPTIMIZE.NUM_LOADED_LANES` | Integer | – | Required |
| **Load Case for Permit Vehicle(`bPERMIT_LOAD`=true)** | | | | | |
| 5 | Permit Vehicle | `"PERMIT_LOAD"` | Object | – | Required |
| (1) | Vehicle Name | `PERMIT_LOAD.VEHICLE_LOAD_NAME` | String | – | Required |
| (2) | Reference Lane | `PERMIT_LOAD.REF_LANE` | String | – | Required |
| (3) | Eccentricity | `PERMIT_LOAD.ECC` | Number | – | Required |
| (4) | Scale Factor | `PERMIT_LOAD.SCALE_FACTOR` | Number | – | Required |

> ⚠️ 2026-08-25 确认：此前文档连 General Load（`DEFAULT`）的下级字段都未列入表中，仅在示例中
> 隐含暗示，而 Moving Load Optimization（`AUTO_OPTIMIZE`）与 Permit Vehicle（`PERMIT_LOAD`）
> 对象则完全遗漏。按原文
> [Moving Load Cases - Poland](https://support.midasuser.com/hc/en-us/articles/35961922701209)
> 全部补充。

### Python 示例

```python
result = mv_post("MVLDpl", {
    "1": {
        "LCNAME": "MV_PL_VehicleS",
        "DESC": "",
        "LOAD_MODEL": 1,
        "bAUTO_OPTIMIZE": False,
        "bPERMIT_LOAD": False,
        "DEFAULT": {
            "COMB_OPTION": "INDEPENDENT",
            "SUB_LOAD_DATAS": [
                {
                    "VEHICLE_NAME": "VehicleS",
                    "SCALE_FACTOR": 1,
                    "MIN_LOADED_LANE": 1,
                    "MAX_LOADED_LANE": 2,
                    "LANE_NAMES": ["L1", "L2"],
                }
            ],
        },
    }
})
print(result)

# Moving Load Optimization (Vehicle K)
mv_post("MVLDpl", {
    "2": {
        "LCNAME": "MV_PL_Opt_VehicleK",
        "DESC": "",
        "LOAD_MODEL": 2,
        "bAUTO_OPTIMIZE": True,
        "bPERMIT_LOAD": False,
        "AUTO_OPTIMIZE": {
            "VEHICLE_LOAD_NAME": "VehicleK",
            "MIN_VEHL_DIST": 1,
            "LANE_NAME": "L1",
            "NUM_LOADED_LANES": 2,
        },
    }
})

# Load Case for Permit Vehicle
mv_post("MVLDpl", {
    "3": {
        "LCNAME": "MV_PL_Permit",
        "DESC": "",
        "LOAD_MODEL": 1,
        "bAUTO_OPTIMIZE": False,
        "bPERMIT_LOAD": True,
        "PERMIT_LOAD": {
            "VEHICLE_LOAD_NAME": "UD_PermitTruck",
            "REF_LANE": "L1",
            "ECC": 1.2,
            "SCALE_FACTOR": 1,
        },
    }
})
```

---

## 18. /db/MVLDtr – Moving Load Cases – Transverse

> Transverse 移动荷载代码专用荷载工况。

**Input URI:** `{base url}/db/MVLDtr`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "MVHL_NAME": "Trans",
      "SCALEFACTOR": 1,
      "LLAN_NAME": "LL_01",
      "NUM_LANE": 3,
      "ITEMS": [1, 1, 0.9, 0.75]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case Name | `"LCNAME"` | String | – | Required |
| 2 | Description | `"DESC"` | String | `""` | Optional |
| 3 | Vehicle Name | `"MVHL_NAME"` | String | – | Required |
| 4 | Scale Factor | `"SCALEFACTOR"` | Number | – | Required |
| 5 | Line Lane | `"LLAN_NAME"` | String | – | Required |
| 6 | Number of Loaded Lanes | `"NUM_LANE"` | Integer | – | Required |
| 7 | Factors (Length: NUM_LANE + 1) | `"ITEMS"` | Array[Number] | – | Required |

### Python 示例

```python
result = mv_post("MVLDtr", {
    "1": {
        "LCNAME": "MV_Trans_1",
        "DESC": "",
        "MVHL_NAME": "Trans",
        "SCALEFACTOR": 1,
        "LLAN_NAME": "LL_01",
        "NUM_LANE": 3,
        "ITEMS": [1, 1, 0.9, 0.75],
    }
})
print(result)
```

---

## 19. /db/CRGR – Concurrent Reaction Group

> 定义移动荷载分析时同时提取反力的结构群组。

**Input URI:** `{base url}/db/CRGR`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "GROUPS": ["Main3", "Main4", "Main5"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Structure Group Names | `"GROUPS"` | Array[String] | – | Required |

### Python 示例

```python
result = mv_post("CRGR", {
    "1": {"GROUPS": ["Main3", "Main4", "Main5"]},
    "2": {"GROUPS": ["Pier1", "Pier2"]},
})
print(result)
```

---

## 20. /db/CJFG – Concurrent Joint Force Group

> 定义移动荷载分析时同时提取节点力的结构群组。

**Input URI:** `{base url}/db/CJFG`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

### Request Body

```json
{
  "Assign": {
    "1": {
      "GROUPS": ["Main1", "Main2", "Main3", "Main4"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Structure Group Names | `"GROUPS"` | Array[String] | – | Required |

### Python 示例

```python
result = mv_post("CJFG", {
    "1": {"GROUPS": ["Main1", "Main2", "Main3", "Main4"]},
})
print(result)
```

---

## 21. /db/MVHC – Vehicle Classes

> 将多辆车辆归为一个类别，在 Moving Load Case 中作为组使用。

**Input URI:** `{base url}/db/MVHC`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的移动荷载代码：AASHTO Standard, AASHTO LRFD, PENNDOT, Canada, Australia, Russia, Korea, KSCE-LSD15, China, Taiwan

### Request Body

```json
{
  "Assign": {
    "1": {
      "VEHICLE_CLS_NAME": "VCN1",
      "VEHICLE_LD_NAMES": ["DB-18"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Vehicle Class Name | `"VEHICLE_CLS_NAME"` | String | – | Required |
| 2 | Selected Vehicle List | `"VEHICLE_LD_NAMES"` | Array[String] | – | Required |

### Python 示例

```python
result = mv_post("MVHC", {
    "1": {
        "VEHICLE_CLS_NAME": "Heavy_Trucks",
        "VEHICLE_LD_NAMES": ["DB-18", "DB-24", "HL-93TRK"],
    }
})
print(result)
```

---

## 22. /db/SINF – Plate Element for Influence Surface

> 指定影响面（Influence Surface）分析要使用的板单元列表。

**Input URI:** `{base url}/db/SINF`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：AASHTO Standard, AASHTO LRFD, PENNDOT, Canada, BS, Eurocode, South Africa, Korea, KSCE-LSD15, China, Taiwan

### Request Body

```json
{
  "Assign": {
    "1": {
      "ELEM_LISTS": [438, 439, 444, 462, 463]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Assigned Element List | `"ELEM_LISTS"` | Array[Integer] | – | Required |

### Python 示例

```python
result = mv_post("SINF", {
    "1": {"ELEM_LISTS": [438, 439, 440, 441, 442, 443, 444]},
})
print(result)
```

---

## 23. /db/MLSP – Lane Support – Negative Moments at Interior Piers

> 指定连续梁桥内支点处负(-)弯矩的车道支承位置。

**Input URI:** `{base url}/db/MLSP`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：AASHTO Standard, AASHTO LRFD, PENNDOT, Korea, Taiwan

### Request Body – Auto Input

```json
{
  "Assign": {
    "1": {
      "TYPE": "AutoInput",
      "GROUP_NAME": "CrossBeam"
    }
  }
}
```

### Request Body – User Input (Beam)

```json
{
  "Assign": {
    "1": {
      "TYPE": "UserInput",
      "ELEMENT_NO": 179,
      "ELEMENT_TYPE": "BEAM",
      "POSITION": "Both"
    },
    "2": {
      "TYPE": "UserInput",
      "ELEMENT_NO": 180,
      "ELEMENT_TYPE": "BEAM",
      "POSITION": "End-I"
    }
  }
}
```

### Request Body – User Input (Plate)

```json
{
  "Assign": {
    "1": {
      "TYPE": "UserInput",
      "ELEMENT_NO": 540,
      "ELEMENT_TYPE": "PLATE"
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Input Type (`"AutoInput"` / `"UserInput"`) ¹⁾ | `"TYPE"` | String | – | Required |
| 2 | Structure Group Name（仅 AutoInput） | `"GROUP_NAME"` | String | – | Required (AutoInput) |
| 3 | Element ID | `"ELEMENT_NO"` | Integer | – | Required (UserInput) |
| 4 | Element Type (`"BEAM"` / `"PLATE"`) | `"ELEMENT_TYPE"` | String | – | Required (UserInput) |
| 5 | Position (`"Both"` / `"End-I"` / `"End-J"`，仅 BEAM) | `"POSITION"` | String | – | Required (BEAM) |

> ¹⁾ AutoInput 仅可在 AASHTO LRFD 下使用

### Python 示例

```python
# Auto Input（仅 AASHTO LRFD）
result = mv_post("MLSP", {
    "1": {
        "TYPE": "AutoInput",
        "GROUP_NAME": "CrossBeam",
    }
})

# User Input (Beam Element)
result2 = mv_post("MLSP", {
    "1": {"TYPE": "UserInput", "ELEMENT_NO": 179, "ELEMENT_TYPE": "BEAM", "POSITION": "Both"},
    "2": {"TYPE": "UserInput", "ELEMENT_NO": 180, "ELEMENT_TYPE": "BEAM", "POSITION": "End-I"},
    "3": {"TYPE": "UserInput", "ELEMENT_NO": 540, "ELEMENT_TYPE": "PLATE"},
})
print(result, result2)
```

---

## 24. /db/MLSR – Lane Support – Reactions at Interior Piers

> 指定连续梁桥内支点处反力的车道支承节点。

**Input URI:** `{base url}/db/MLSR`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：AASHTO LRFD, PENNDOT

### Request Body

```json
{
  "Assign": {
    "60":  {"NODE": 0},
    "201": {"NODE": 0},
    "202": {"NODE": 0},
    "203": {"NODE": 0}
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Fixed Value: 0（Key 为 Node ID） | `"NODE"` | Integer | – | Required |

> **参考：** `"Assign"` 对象的键值即支承节点 ID，取值 `{"NODE": 0}` 为固定值。

### Python 示例

```python
# 指定内支点节点 60、201、202
result = mv_post("MLSR", {
    "60":  {"NODE": 0},
    "201": {"NODE": 0},
    "202": {"NODE": 0},
})
print(result)
```

---

## 25. /db/DYLA – Dynamic Load Allowance

> 按结构群组设置冲击系数（Dynamic Load Allowance, IM）。

**Input URI:** `{base url}/db/DYLA`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：AASHTO LRFD, PENNDOT, KSCE-LSD15

### Request Body

```json
{
  "Assign": {
    "1": {
      "FACTOR": 15,
      "ITEMS": ["Main4", "Main5", "Main6"]
    },
    "2": {
      "FACTOR": 10,
      "ITEMS": ["Main1", "Main2", "Main7"]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Impact Factor (%) | `"FACTOR"` | Number | – | Required |
| 2 | Selected Structure Group List | `"ITEMS"` | Array[String] | – | Required |

### Python 示例

```python
result = mv_post("DYLA", {
    "1": {"FACTOR": 33, "ITEMS": ["Deck_Joints"]},
    "2": {"FACTOR": 25, "ITEMS": ["All_Other_Components"]},
    "3": {"FACTOR": 15, "ITEMS": ["Fatigue"]},
})
print(result)
```

---

## 26. /db/IMPF – Additional Impact Factor

> 按车道、按单元类型设置附加冲击系数或有效跨径长度。

**Input URI:** `{base url}/db/IMPF`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：Korea

### Request Body – Line Lane (Impact Factor)

```json
{
  "Assign": {
    "82": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "LINE",
          "LANE_NAME": "LL_01",
          "FACT_TYPE": "IMPACT_FACT",
          "FACTOR": 0.3
        }
      ]
    }
  }
}
```

### Request Body – Line Lane (Effective Span Length – Auto Calculation)

```json
{
  "Assign": {
    "163": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "LINE",
          "LANE_NAME": "LL_01",
          "ELEMTYPE": "BEAM",
          "FACT_TYPE": "EFF_SPAN_LEN_AUTO",
          "FACTOR": 0,
          "PARTS": [true, true, true, true, true],
          "COMPONENTS": [true, true, true, true, true, true, false, false]
        }
      ]
    }
  }
}
```

### Request Body – Surface Lane

```json
{
  "Assign": {
    "527": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "SURFACE",
          "LANE_NAME": "SL_01",
          "FACT_TYPE": "IMPACT_FACT",
          "FACTOR": 0.3
        }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Additional Impact Factor Items | `"ITEMS"` | Array[Object] | – | Required |

**Line Lane / Surface Lane (Impact Factor, Effective Span Length – User Input)**

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Serial Number | `"ID"` | Integer | Required |
| 2 | Lane Type (`"LINE"` / `"SURFACE"`) | `"LANE_TYPE"` | String | Required |
| 3 | Lane Name | `"LANE_NAME"` | String | Required |
| 4 | Factor Type (`"IMPACT_FACT"` / `"EFF_SPAN_LEN_USER"`) | `"FACT_TYPE"` | String | Required |
| 5 | Factor | `"FACTOR"` | Number | Required |

**Line Lane (Effective Span Length – Auto Calculation)**

| No. | Description | Key | Value Type | Required |
|-----|-------------|-----|-----------|----------|
| 1 | Serial Number | `"ID"` | Integer | Required |
| 2 | Lane Type: `"LINE"` | `"LANE_TYPE"` | String | Required |
| 3 | Lane Name | `"LANE_NAME"` | String | Required |
| 4 | Element Type (`"BEAM"` / `"TRUSS"` / `"PLATE"`) | `"ELEMTYPE"` | String | Required |
| 5 | Factor Type: `"EFF_SPAN_LEN_AUTO"` | `"FACT_TYPE"` | String | Required |
| 6 | Parts (Beam: [i, 1/4, 1/2, 3/4, j] / Plate: [cent, i, j, k, l]) | `"PARTS"` | Array[Boolean] | Required (仅 Beam/Plate — ⚠️ Truss 示例中根本没有 `PARTS` 字段，2026-08-25 确认) |
| 7 | Components (Beam: [My_max, My_min, Mz_max, Mz_min, Fx_max, Fx_min] / Truss: [Max, Min] / Plate: [Mxx_max, Mxx_min, Myy_max, Myy_min, Fxx_max, Fxx_min, Fyy_max, Fyy_min]) | `"COMPONENTS"` | Array[Boolean] | Required |

### Python 示例

```python
# 梁单元自动计算有效跨径长度
result = mv_post("IMPF", {
    "163": {
        "ITEMS": [
            {
                "ID": 1,
                "LANE_TYPE": "LINE",
                "LANE_NAME": "LL_01",
                "ELEMTYPE": "BEAM",
                "FACT_TYPE": "EFF_SPAN_LEN_AUTO",
                "FACTOR": 0,
                "PARTS": [True, True, True, True, True],
                "COMPONENTS": [True, True, True, True, True, True, False, False],
            }
        ]
    }
})
print(result)
```

---

## 27. /db/DYFG – Railway Dynamic Factor

> 对整体模型应用基于 Eurocode 的铁路动力系数(φ)。

**Input URI:** `{base url}/db/DYFG`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：Eurocode

### Request Body – Auto Input

```json
{
  "Assign": {
    "1": {
      "INPUT_TYPE": 0,
      "LENGTH": 12,
      "MAINTAIN_TYPE": 0,
      "OPT_REDUCE_EFF": true,
      "HEIGHT_COVER": 1
    }
  }
}
```

### Request Body – User Input

```json
{
  "Assign": {
    "1": {
      "INPUT_TYPE": 1,
      "DYN_FACTOR": 1.2611627362707665
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Input Type (0=Auto, 1=User) | `"INPUT_TYPE"` | Integer | – | Required |
| 2 | Determinant Length (Lφ) | `"LENGTH"` | Number | – | Required (Auto) |
| 3 | Quality of Track Maintenance (0=Carefully, 1=Standard) | `"MAINTAIN_TYPE"` | Integer | – | Required (Auto) |
| 4 | Consider Reduced Dynamic Effect | `"OPT_REDUCE_EFF"` | Boolean | false | Optional |
| 5 | Height of Cover (h)（OPT_REDUCE_EFF=true 时） | `"HEIGHT_COVER"` | Number | – | Required |
| 6 | Dynamic Factor (φ)（INPUT_TYPE=1 时） | `"DYN_FACTOR"` | Number | – | Required (User) |

### Python 示例

```python
# Auto Input（整体模型）
result = mv_post("DYFG", {
    "1": {
        "INPUT_TYPE": 0,
        "LENGTH": 12,
        "MAINTAIN_TYPE": 0,
        "OPT_REDUCE_EFF": True,
        "HEIGHT_COVER": 1,
    }
})
print(result)
```

---

## 28. /db/DYNF – Railway Dynamic Factor by Element

> 以单元为单位应用基于 Eurocode 的铁路动力系数(φ)。  
> 结构与 DYFG 相同，但 `"Assign"` 的键值为单元 ID。

**Input URI:** `{base url}/db/DYNF`

**Active Methods:** `POST`, `GET`, `PUT`, `DELETE`

> ¹⁾ 可使用的代码：Eurocode

### Request Body – Auto Input

```json
{
  "Assign": {
    "249": {
      "INPUT_TYPE": 0,
      "LENGTH": 12,
      "MAINTAIN_TYPE": 1,
      "OPT_REDUCE_EFF": true,
      "HEIGHT_COVER": 1
    }
  }
}
```

### Request Body – User Input

```json
{
  "Assign": {
    "88": {
      "INPUT_TYPE": 1,
      "DYN_FACTOR": 1.3
    }
  }
}
```

### Parameters

与 DYFG 相同的参数结构。`"Assign"` 的键值为各单元 ID。

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Input Type (0=Auto, 1=User) | `"INPUT_TYPE"` | Integer | – | Required |
| 2 | Determinant Length (Lφ) | `"LENGTH"` | Number | – | Required (Auto) |
| 3 | Quality of Track Maintenance (0=Carefully, 1=Standard) | `"MAINTAIN_TYPE"` | Integer | – | Required (Auto) |
| 4 | Consider Reduced Dynamic Effect | `"OPT_REDUCE_EFF"` | Boolean | false | Optional |
| 5 | Height of Cover (h) | `"HEIGHT_COVER"` | Number | – | Required (OPT_REDUCE_EFF=true) |
| 6 | Dynamic Factor (φ) | `"DYN_FACTOR"` | Number | – | Required (User) |

### Python 示例

```python
# 按单元的 Auto Input
result = mv_post("DYNF", {
    "249": {
        "INPUT_TYPE": 0,
        "LENGTH": 12,
        "MAINTAIN_TYPE": 1,
        "OPT_REDUCE_EFF": True,
        "HEIGHT_COVER": 1,
    },
    "88": {
        "INPUT_TYPE": 1,
        "DYN_FACTOR": 1.3,
    },
})
print(result)
```

---

## 移动荷载建模工作流示例

> 桥梁移动荷载分析的完整设置顺序（以 KSCE-LSD15 为准）

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "<YOUR_MAPI_KEY>",
}

def post(ep, assign):
    r = requests.post(f"{BASE_URL}/db/{ep}", headers=HEADERS, json={"Assign": assign})
    r.raise_for_status()
    print(f"  ✓ {ep}: {r.status_code}")
    return r.json()

# Step 1: 设置移动荷载代码
post("MVCD", {"1": {"CODE": "KSCE-LSD15"}})

# Step 2: 定义车道（Lane Element 方式）
post("LLAN", {
    "1": {
        "COMMON": {
            "LL_NAME": "LL_01", "LOAD_DIST": "LANE", "GROUP_NAME": "",
            "SKEW_START": 0, "SKEW_END": 0, "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8, "WIDTH": 3, "OPT_AUTO_LANE": True, "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": i, "ECC": -1.5} for i in range(1, 11)
        ],
    },
    "2": {
        "COMMON": {
            "LL_NAME": "LL_02", "LOAD_DIST": "LANE", "GROUP_NAME": "",
            "SKEW_START": 0, "SKEW_END": 0, "MOVING": "BOTH",
            "WHEEL_SPACE": 1.8, "WIDTH": 3, "OPT_AUTO_LANE": True, "ALLOW_WIDTH": 3,
        },
        "LANE_ITEMS": [
            {"ELEM": i, "ECC": 1.5} for i in range(1, 11)
        ],
    },
})

# Step 3: 定义车辆（KSCE-LSD15 标准车辆 — 使用 MVLD_CODE 13 + VEH_KSCE_LSD15 结构）
post("MVHL", {
    "1": {
        "MVLD_CODE": 13, "VEHICLE_LOAD_NAME": "KL-510FTG",
        "VEHICLE_LOAD_NUM": 1, "VEHICLE_TYPE_NAME": "KL-510FTG",
        "STANDARD_CODE": "KSCE-LSD15",
        "VEH_KSCE_LSD15": {
            "LOAD_TYPE": 0, "DYN_LOAD_ALLOWANCE": 15,
            "LENGTH_LANE": 0, "LENGTH_LANE_USER": 0, "CONVERT_DIST_LOAD": False,
            "POINT_ITEMS": [
                {"POINT_LOAD": 38.4, "POINT_DIST": 3.6},
                {"POINT_LOAD": 108, "POINT_DIST": 1.2},
                {"POINT_LOAD": 108, "POINT_DIST": 7.2},
                {"POINT_LOAD": 153.6, "POINT_DIST": 0},
            ],
        },
    }
})

# Step 4: 定义移动荷载工况
post("MVLD", {
    "1": {
        "LCNAME": "MV_KSCE_1", "DESC": "", "TYPE": 0,
        "DEFAULT": {
            "SCALE_FACTORS": [1, 0.9, 0.8, 0.7, 0.65, 0.65],
            "COMB_OPTION": "COMBINED",
            "LANE_FACTOR_TYPE": 1,
            "SUB_LOAD_DATAS": [{
                "VEHICLE_TYPE": "VL", "VEHICLE_NAME": "KL-510FTG",
                "SCALE_FACTOR": 1, "MIN_LOADED_LANE": 1, "MAX_LOADED_LANE": 2,
                "LANE_NAMES": ["LL_01", "LL_02"],
            }],
        },
    }
})

# Step 5: 设置冲击系数（使用 AASHTO LRFD 时）
# post("DYLA", {"1": {"FACTOR": 33, "ITEMS": ["Deck"]}})

print("移动荷载建模完成！")
```
