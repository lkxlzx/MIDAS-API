# 23. POST – Design Tables (设计结果表格)

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../23_POST_Design.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分介绍用于提取**设计(Design)结果**的 POST Endpoint，包括设计代码检查(钢结构)、P-M 相关曲线(Concrete/SRC)，以及 RC·钢·SRC·冷弯薄壁型钢构件的**设计用构件内力(Design Forces)** 表格。

设计结果 Endpoint 分为**三种 URI 模式**。

| # | Endpoint | URI | 方法 | 请求形式 |
|---|-----------|-----|--------|-----------|
| 1 | [P-M Interaction Diagram](#1-p-m-interaction-diagram) | `post/PM` | POST | 空 `Argument` |
| 2 | [Steel Code Check](#2-steel-code-check) | `post/STEELCODECHECK` | POST | 空 `Argument` |
| 3 | [Concrete Design – Beam Design Forces](#3-concrete-design--beam-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=BEAMDESIGNFORCES` |
| 4 | [Concrete Design – Column Design Forces](#4-concrete-design--column-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=COLUMNDESIGNFORCES` |
| 5 | [Concrete Design – Brace Design Forces](#5-concrete-design--brace-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=BRACEDESIGNFORCES` |
| 6 | [Concrete Design – Wall Design Forces](#6-concrete-design--wall-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=WALLDESIGNFORCES` |
| 7 | [Steel Design – Steel Member Design Forces](#7-steel-design--steel-member-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=STEELMEMBERDESIGNFORCES` |
| 8 | [SRC Design – SRC Beam Design Forces](#8-src-design--src-beam-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=SRCBEAMDESIGNFORCES` |
| 9 | [SRC Design – SRC Column Design Forces](#9-src-design--src-column-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=SRCCOLUMNDESIGNFORCES` |
| 10 | [Cold Formed Design – Cold Formed Steel Member Design Forces](#10-cold-formed-design--cold-formed-steel-member-design-forces) | `post/TABLE` | POST | `TABLE_TYPE=COLDFORMEDSTEELMEMBERDESIGNFORCES` |

> **前置条件：** 查询设计结果前，必须已完成分析(Analysis)与**设计(Design)**。设计代码·构件·钢筋等设置见 **[24_DB_Design.md](./24_DB_Design.md)**。

---

## 通用事项 (Design Forces 表格, #3~#10)

使用 `post/TABLE` 的 8 个设计用构件内力表格(#3~#10)采用**与第 19 章 (Analysis Result Tables) 相同的通用请求结构**。在请求体的 `"Argument"` 对象中以 `TABLE_TYPE` 选择表格，并共同支持以下参数。

### Input URI

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 通用 Request 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 响应表格标题 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表格类型 (各表格固定值，见各节) | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表格保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 力(Force) | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 长度(Length) | `UNIT.DIST` | String | — | Optional |
| 5 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 数字格式 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 小数位数 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 指定构件位置(端部) · `"PartI"` / `"PartJ"` 等 | `"PARTS"` | Array [String] | All | Optional |
| 7 | 结果表格显示列 | `"COMPONENTS"` | Array [String] | All | Optional |
| 8 | 指定单元/构件 (以下 3 种方式之一) | `"NODE_ELEMS"` | Object | All | Optional |
| 8-1 | 方式1: 分别指定 ID (例: `[1, 2, 3]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 8-2 | 方式2: 指定 ID 范围 (例: `"1 to 5"`) | `NODE_ELEMS.TO` | String | — | Optional |
| 8-3 | 方式3: 指定结构组名 (例: `"SG1"`) | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |

### 通用 Response 结构

```json
{
  "<TABLE_TYPE>": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

> **`Type` 列：** 设计用构件内力表格的 `Type` 列表示荷载组合极值类型(`Max` / `Min`)，`LComName` 列是设计荷载组合名称。

---

## 1. P-M Interaction Diagram

> **功能：** 提取 RC/SRC 柱·构件的 **P-M 相关曲线(轴力–弯矩相关曲线)** 数据。无需额外参数，返回当前模型的全部设计结果。

### Input URI

```
{base url}/post/PM
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "PM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "argument": {
        "type": "object",
        "properties": {}
      }
    }
  }
}
```

### Request / Response JSON

请求体的 `"Argument"` 是**空对象**。不做过滤，返回当前设计结果的 P-M 相关曲线数据集。

**POST Request Body**

```json
{
  "Argument": {}
}
```

> **参考：** 手册未公开固定的 `HEAD`/`DATA` 响应示例。响应中包含按构件/截面的 P-M 相关曲线坐标及所需强度点数据。实际响应键结构取决于运行环境的设计代码设置。

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "在此填入_已获取的密钥",
    "Content-Type": "application/json",
}

# 提取 P-M 相关曲线数据（无参数，查询全部）
payload = {"Argument": {}}

res = requests.post(f"{BASE_URL}/post/PM", json=payload, headers=HEADERS)
res.raise_for_status()

pm_data = res.json()
print("P-M Interaction Diagram 响应键:", list(pm_data.keys()))
```

---

## 2. Steel Code Check

> **功能：** 提取钢构件的**设计代码检查结果**(按截面·单元的组合强度比、长细比、挠度、允许挠度)。

### Input URI

```
{base url}/post/STEELCODECHECK
```

### Active Methods

`POST`

### Response 字段

| No. | 说明 | Key | 值类型 |
|-----|------|-----|-----------|
| 1 | 截面数据数组 | `"vSECT"` | Array [Object] |
| 1-(1) | └ 截面 ID | `SECT` | Number |
| 1-(2) | └ 组合强度比 (Combined Strength Ratio) | `RAT` | Number |
| 1-(3) | └ 长细比 (Slenderness Ratio) | `SLN` | Number |
| 1-(4) | └ 挠度 (Deflection) | `DEF` | Number |
| 1-(5) | └ 允许挠度 (Allowable Deflection) | `DEFA` | Number |
| 2 | 单元数据数组 | `"vELEM"` | Array [Object] |
| 2-(1) | └ 单元 ID | `ELEM` | Integer |
| 2-(2) | └ 组合强度比 | `RAT` | Number |
| 2-(3) | └ 长细比 | `SLN` | Number |
| 2-(4) | └ 挠度 | `DEF` | Number |
| 2-(5) | └ 允许挠度 | `DEFA` | Number |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {}
}
```

**Response Body**

```json
{
  "vSECT": [
    {
      "SECT": 1,
      "RAT": 0.611917806624809,
      "SLN": 0.07680554887655298,
      "DEF": -0.0006249514999156769,
      "DEFA": 0.02279999999996812
    },
    {
      "SECT": 2,
      "RAT": 0.4296192038079335,
      "SLN": 0.04946798063250228,
      "DEF": -0.0006016184741690078,
      "DEFA": 0.02279999999995198
    },
    {
      "SECT": 3,
      "RAT": 0.5268570141827795,
      "SLN": 0.06909209873374429,
      "DEF": 0,
      "DEFA": 0.0014103010198308647
    }
  ],
  "vELEM": [
    {
      "ELEM": 10,
      "RAT": 0.12369675848216558,
      "SLN": 0.0023911209516698797,
      "DEF": 1.0658046060985082e-07,
      "DEFA": 0.0011020776874479453
    },
    {
      "ELEM": 11,
      "RAT": 0.13438019223768993,
      "SLN": 0.04707685968078899,
      "DEF": -0.0001707694272293503,
      "DEFA": 0.021697922312579977
    },
    {
      "ELEM": 12,
      "RAT": 0.20046527423634042,
      "SLN": 0.0494679806323982,
      "DEF": -0.000402594921254891,
      "DEFA": 0.022799999999999952
    }
  ]
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "在此填入_已获取的密钥",
    "Content-Type": "application/json",
}

# 查询钢结构设计代码检查结果（无参数）
res = requests.post(f"{BASE_URL}/post/STEELCODECHECK", json={"Argument": {}}, headers=HEADERS)
res.raise_for_status()
data = res.json()

# 筛选强度比(RAT)≥1.0 的超设计(N.G.)截面/单元
ng_sect = [s for s in data.get("vSECT", []) if s["RAT"] >= 1.0]
ng_elem = [e for e in data.get("vELEM", []) if e["RAT"] >= 1.0]

print(f"审查截面数: {len(data.get('vSECT', []))}, N.G. 截面: {len(ng_sect)}")
print(f"审查单元数: {len(data.get('vELEM', []))}, N.G. 单元: {len(ng_elem)}")

# 输出最大强度比的单元
if data.get("vELEM"):
    worst = max(data["vELEM"], key=lambda e: e["RAT"])
    print(f"最大强度比单元: ELEM {worst['ELEM']}, RAT = {worst['RAT']:.3f}")
```

---

## 3. Concrete Design – Beam Design Forces

> **功能：** 提取 RC 设计用的**梁(Beam)构件设计力**。提供受弯设计基准下的轴力·扭转·正/负弯矩。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BEAMDESIGNFORCES"` | RC 梁设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"]`

| 列 | 含义 |
|----|------|
| `Memb` | 构件编号 |
| `Part` | 构件端部/位置 (I、J 等) |
| `LComName` | 设计荷载组合名称 |
| `Type` | 极值类型 (`Max`/`Min`) |
| `Fz` | 剪力 |
| `Mx` | 扭矩 |
| `My(-)` / `My(+)` | 负(−)/正(+)弯矩 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "BEAMDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [1, 2, 3]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"]
  }
}
```

**Response Body**

```json
{
  "BEAMDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"],
    "DATA": [
      ["1", "1", "I", "Strength", "Max", "41.454", "0.000", "73.244", "36.622"]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "在此填入_已获取的密钥",
    "Content-Type": "application/json",
}

def get_design_table(table_type, keys=None, parts=None, components=None):
    """设计用构件内力表格通用查询辅助函数"""
    arg = {
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
    }
    if keys is not None:
        arg["NODE_ELEMS"] = {"KEYS": keys}
    if parts is not None:
        arg["PARTS"] = parts
    if components is not None:
        arg["COMPONENTS"] = components
    res = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    res.raise_for_status()
    return res.json()[table_type]

# 查询 RC 梁设计用构件内力（构件 1,2,3 的两端）
beam = get_design_table(
    "BEAMDESIGNFORCES",
    keys=[1, 2, 3],
    parts=["PartI", "PartJ"],
)
print("HEAD:", beam["HEAD"])
for row in beam["DATA"]:
    print(row)
```

---

## 4. Concrete Design – Column Design Forces

> **功能：** 提取 RC 设计用的**柱(Column)构件设计力**(三轴力·弯矩)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"COLUMNDESIGNFORCES"` | RC 柱设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

| 列 | 含义 |
|----|------|
| `Fx` / `Fy` / `Fz` | 轴力及剪力 (构件坐标系) |
| `Mx` / `My` / `Mz` | 扭矩及 2 轴弯矩 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "COLUMNDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [56]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "COLUMNDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "56", "I", "Strength", "Max", "2510.159", "9.161", "0.271", "0.000", "13.114", "15.975"]
    ]
  }
}
```

### Python 示例

```python
# 复用第 3 节示例的 get_design_table() 辅助函数
column = get_design_table(
    "COLUMNDESIGNFORCES",
    keys=[56],
    parts=["PartI", "PartJ"],
)
print("HEAD:", column["HEAD"])
for row in column["DATA"]:
    print(row)
```

---

## 5. Concrete Design – Brace Design Forces

> **功能：** 提取 RC 设计用的**支撑(Brace)构件设计力**(三轴力·弯矩)。响应结构与柱相同。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BRACEDESIGNFORCES"` | RC 支撑设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "BRACEDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [52]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "BRACEDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "52", "I", "Strength", "Max", "2510.159", "9.161", "0.271", "0.000", "13.114", "15.975"]
    ]
  }
}
```

### Python 示例

```python
# 查询支撑设计用构件内力
brace = get_design_table("BRACEDESIGNFORCES", keys=[52], parts=["PartI", "PartJ"])
print("HEAD:", brace["HEAD"])
for row in brace["DATA"]:
    print(row)
```

---

## 6. Concrete Design – Wall Design Forces

> **功能：** 提取 RC 设计用的**墙(Wall)构件设计力**。增加了墙 ID(`WID`)与楼层(`Story`)信息。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"WALLDESIGNFORCES"` | RC 墙设计用构件内力 |

### Response HEAD

`["Index", "WID", "Story", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

| 列 | 含义 |
|----|------|
| `WID` | 墙 ID |
| `Story` | 楼层名称 |
| `Part` | 墙位置 (`Top`/`Bottom` 等) |

### ADDITIONAL — `STORY_NAMES` 请求参数 (2026-08-05 官方已反映)

新增了按楼层名称过滤结果的 `STORY_NAMES` 参数。它不在 `#3~#10` 的通用
参数表(上方 "通用事项" 一节)中，是 **Wall Design Forces 专用**参数。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 9 | 指定楼层名称 (例: `["1F", "2F"]`) | `"STORY_NAMES"` | Array [String] | All | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "WALLDESIGNFORCES",
    "TABLE_TYPE": "WALLDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [1]
    },
    "COMPONENTS": ["Index", "WID", "Story", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "WALLDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "WID", "Story", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "1", "1F", "Top", "Strength", "Max", "3314.580", "0.000", "19.717", "0.000", "11.341", "0.000"]
    ]
  }
}
```

### Python 示例

```python
# 查询墙设计用构件内力 (以 WID 指定)
wall = get_design_table("WALLDESIGNFORCES", keys=[1])
print("HEAD:", wall["HEAD"])
for row in wall["DATA"]:
    print(row)
```

---

## 7. Steel Design – Steel Member Design Forces

> **功能：** 提取钢结构设计用的**构件设计力**(三轴力·弯矩)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"STEELMEMBERDESIGNFORCES"` | 钢构件设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [1]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "STEELMEMBERDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "1", "I", "sLCB1", "Max", "-17.635", "-0.009", "0.489", "0.000", "-0.000", "-0.000"]
    ]
  }
}
```

### Python 示例

```python
# 查询钢构件设计用构件内力 (全部单元)
steel = get_design_table("STEELMEMBERDESIGNFORCES", parts=["PartI", "PartJ"])
print("HEAD:", steel["HEAD"])
print(f"共 {len(steel['DATA'])} 行")
for row in steel["DATA"][:5]:
    print(row)
```

---

## 8. SRC Design – SRC Beam Design Forces

> **功能：** 提取 SRC(型钢钢筋混凝土组合)设计用的**梁构件设计力**。响应列构成与 RC 梁类似，但注意正/负弯矩列的顺序(`My(+)`, `My(-)`)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SRCBEAMDESIGNFORCES"` | SRC 梁设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(+)", "My(-)"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [316]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(+)", "My(-)"]
  }
}
```

**Response Body**

```json
{
  "SRCBEAMDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(+)", "My(-)"],
    "DATA": [
      ["1", "316", "I", "rLCB6", "Max", "152.087", "0.000", "72.164", "244.627"]
    ]
  }
}
```

### Python 示例

```python
# 查询 SRC 梁设计用构件内力
src_beam = get_design_table("SRCBEAMDESIGNFORCES", keys=[316], parts=["PartI", "PartJ"])
print("HEAD:", src_beam["HEAD"])
for row in src_beam["DATA"]:
    print(row)
```

---

## 9. SRC Design – SRC Column Design Forces

> **功能：** 提取 SRC 设计用的**柱构件设计力**(三轴力·弯矩)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"SRCCOLUMNDESIGNFORCES"` | SRC 柱设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [365]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "SRCCOLUMNDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "365", "I", "rLCB6", "Max", "-3960.926", "40.952", "4.948", "0.000", "19.165", "69.926"]
    ]
  }
}
```

### Python 示例

```python
# 查询 SRC 柱设计用构件内力
src_col = get_design_table("SRCCOLUMNDESIGNFORCES", keys=[365], parts=["PartI", "PartJ"])
print("HEAD:", src_col["HEAD"])
for row in src_col["DATA"]:
    print(row)
```

---

## 10. Cold Formed Design – Cold Formed Steel Member Design Forces

> **功能：** 提取冷弯薄壁型钢(Cold Formed Steel)设计用的**构件设计力**(三轴力·弯矩)。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"COLDFORMEDSTEELMEMBERDESIGNFORCES"` | 冷弯薄壁型钢构件设计用构件内力 |

### Response HEAD

`["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "COLDFORMEDSTEELMEMBERDESIGNFORCES",
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [313]
    },
    "PARTS": ["PartI", "PartJ"],
    "COMPONENTS": ["Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"]
  }
}
```

**Response Body**

```json
{
  "COLDFORMEDSTEELMEMBERDESIGNFORCES": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
    "DATA": [
      ["1", "313", "I", "cfLCB1", "Max", "-0.000", "0.000", "-58.761", "0.000", "-116.465", "0.000"]
    ]
  }
}
```

### Python 示例

```python
# 查询冷弯薄壁型钢构件设计用构件内力
cf = get_design_table("COLDFORMEDSTEELMEMBERDESIGNFORCES", keys=[313], parts=["PartI", "PartJ"])
print("HEAD:", cf["HEAD"])
for row in cf["DATA"]:
    print(row)
```

---

## End-to-End Workflow

分析·设计完成后，一次性收集钢结构代码检查结果与各 RC 构件设计力的示例。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "MAPI-Key": "在此填入_已获取的密钥",
    "Content-Type": "application/json",
}


def post_table(table_type, **arg_extra):
    """post/TABLE 设计构件内力通用查询"""
    arg = {
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
    }
    arg.update(arg_extra)
    res = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    res.raise_for_status()
    return res.json()[table_type]


def steel_code_check():
    """钢结构设计代码检查结果"""
    res = requests.post(f"{BASE_URL}/post/STEELCODECHECK", json={"Argument": {}}, headers=HEADERS)
    res.raise_for_status()
    return res.json()


# 1) 钢结构代码检查 — 确认最大强度比的单元
scc = steel_code_check()
if scc.get("vELEM"):
    worst = max(scc["vELEM"], key=lambda e: e["RAT"])
    print(f"[Steel] 最大强度比单元 ELEM {worst['ELEM']}: RAT = {worst['RAT']:.3f}")

# 2) 批量收集 RC 梁/柱/墙设计力
for tt, label in [
    ("BEAMDESIGNFORCES", "RC 梁"),
    ("COLUMNDESIGNFORCES", "RC 柱"),
    ("WALLDESIGNFORCES", "RC 墙"),
]:
    tbl = post_table(tt, PARTS=["PartI", "PartJ"])
    print(f"[{label}] {len(tbl['DATA'])} 行 — HEAD: {tbl['HEAD']}")

# 3) SRC / 冷弯薄壁型钢构件设计力
for tt, label in [
    ("SRCBEAMDESIGNFORCES", "SRC 梁"),
    ("SRCCOLUMNDESIGNFORCES", "SRC 柱"),
    ("COLDFORMEDSTEELMEMBERDESIGNFORCES", "冷弯薄壁型钢"),
]:
    tbl = post_table(tt, PARTS=["PartI", "PartJ"])
    print(f"[{label}] {len(tbl['DATA'])} 行")
```

---

> **下一部分：** **[24_DB_Design.md](./24_DB_Design.md)** — 介绍 RC·Steel 设计代码设置、设计构件(Design Member)、未支撑长度(Unbraced Length)等设计输入用 DB Endpoint(11个)。
