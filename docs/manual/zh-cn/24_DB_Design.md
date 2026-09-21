# 24. DB – Design (设计输入)

> **适用产品：** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **认证头：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../24_DB_Design.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本章介绍在执行设计之前必须向模型输入的**设计输入DB**。内容涵盖RC/钢结构设计代码、验算用钢筋输入、未支撑长度、设计构件指定、框架定义、长细比限制、构件类型及标记修改，以及梁/柱/墙体/支撑的钢筋数据修改，共计**13个端点**。

> **参考1 — Load Combination（设计用荷载组合）：** Concrete / Steel / SRC / Composite / Seismic Design 荷载组合相关端点不在本章，而在**第13章(Load Combinations)**中介绍。本章仅说明定义设计计算所需 "输入记录(input DB)" 的CRUD端点。
>
> **参考2 — `/db/MEMB` 与 `/ope/MEMB`：** 本章的 `/db/MEMB`(第5个)是保存·查询设计构件指定信息的**DB记录(CRUD)**。另一方面，对单元实际执行构件指定的**作业(operation)**端点 `/ope/MEMB` 在**第15章(OPE)**中介绍。两个端点的URI相似，但彼此不同。

> **公共约定 — `"Assign"` 包装：** POST/PUT 请求始终在最上层放置 `"Assign"` 对象，其内以对象ID(单元·截面·墙体ID等)作为**字符串键**收纳各条记录。GET 响应的最上层键会变为该端点的模式名称(例：`REBB`、`LTSR`)，并以相同结构返回。

---

## Endpoint 列表

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/DCON`](#1-dbdcon--rc-design-code-rc设计代码) | RC设计代码 | POST, GET, PUT, DELETE |
| 2 | [`/db/DSTL`](#2-dbdstl--design-steel-code-钢结构设计代码) | 钢结构(Steel)设计代码 | POST, GET, PUT, DELETE |
| 3 | [`/db/RCHK`](#3-dbrchk--rebar-input-for-checking---beamcolumn-验算用钢筋输入) | 验算用钢筋输入 (Beam/Column) | POST, GET, PUT, DELETE |
| 4 | [`/db/LENG`](#4-dbleng--unbraced-length-未支撑长度) | 未支撑长度 (Unbraced Length) | POST, GET, PUT, DELETE |
| 5 | [`/db/MEMB`](#5-dbmemb--member-assignment-设计构件指定) | 设计构件指定 (Member Assignment) | POST, GET, PUT, DELETE |
| 6 | [`/db/DCTL`](#6-dbdctl--definition-of-frame-框架定义) | 框架定义 (Definition of Frame) | POST, GET, PUT, DELETE |
| 7 | [`/db/LTSR`](#7-dbltsr--limiting-slenderness-ratio-长细比限制) | 长细比限制 (Limiting Slenderness Ratio) | POST, GET, PUT, DELETE |
| 8 | [`/db/MBTP`](#8-dbmbtp--modify-member-type-构件类型修改) | 构件类型修改 (Modify Member Type) | POST, GET, PUT, DELETE |
| 9 | [`/db/WMAK`](#9-dbwmak--modify-wall-mark-design-墙体标记设计修改) | 墙体标记设计修改 (Modify Wall Mark) | POST, GET, PUT, DELETE |
| 10 | [`/db/REBB`](#10-dbrebb--modify-beam-rebar-data-梁钢筋数据修改) | 梁钢筋数据修改 (Modify Beam Rebar) | POST, GET, PUT, DELETE |
| 11 | [`/db/REBC`](#11-dbrebc--modify-column-rebar-data-柱钢筋数据修改) | 柱钢筋数据修改 (Modify Column Rebar) | **POST** |
| 12 | [`/db/REBW`](#12-dbrebw--modify-wall-rebar-data-墙体钢筋数据修改) | 墙体钢筋数据修改 (Modify Wall Rebar) | POST, GET, PUT, DELETE |
| 13 | [`/db/REBR`](#13-dbrebr--modify-brace-rebar-data-支撑钢筋数据修改) | 支撑钢筋数据修改 (Modify Brace Rebar) | POST, GET, PUT, DELETE |

> ⚠️ **`/db/REBC`(第11个)仅支持POST(生成/设置)**。其余12个端点支持POST · GET · PUT · DELETE 全部(CRUD)。

---

## 1. `/db/DCON` — RC Design Code (RC设计代码)

> **功能：** 指定RC(钢筋混凝土)构件设计所用的设计标准(Design Code)。以字符串设置 KDS·KCI·ACI·Eurocode·AASHTO 等各类国家/版本代码。

### Input URI

```
{base url}/db/DCON
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "DCON": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "DGNCODE": { "description": "Design Code", "type": "string" }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | RC设计代码名称（下表字符串之一） | `"DGNCODE"` | String | — | **必填** |

**主要 `DGNCODE` 值（部分摘录 — 按原文共计64种）：**

| Design Code | DGNCODE |
|-------------|---------|
| KDS 24 14 21 : 2021 | `"KDS 24 14 21 : 2021"` |
| KDS 41 30 : 2018 | `"KDS 41 30 : 2018"` |
| KSCE-LSD15 | `"KSCE-LSD15"` |
| KCI-USD12 | `"KCI-USD12"` |
| KCI-USD07 | `"KCI-USD07"` |
| ACI318-19 / ACI318M-19 | `"ACI318-19"` / `"ACI318M-19"` |
| ACI318-14 / ACI318M-14 | `"ACI318-14"` / `"ACI318M-14"` |
| Eurocode2-2:05 / Eurocode2:04 / Eurocode2 | `"Eurocode2-2:05"` / `"Eurocode2:04"` / `"Eurocode2"` |
| AASHTO-LRFD20(US) | `"AASHTO-LRFD20"` |
| CSA-S6-19 | `"CSA-S6-19"` |
| GB/T50010-10 | `"GB/T50010-10"` |
| IS456:2000 | `"IS456:2000"` |
| NSCP 2015 | `"NSCP 2015"` |
| AREMA-2023 | `"AREMA-2023"` |

> 上表仅摘录了代表性取值。此外还支持 KSCE-USD·AIK·BS·IRC·TWN·SNiP·SP 系列等大量代码。准确字符串请参考在线手册的 "Available Design Code" 表。

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KCI-USD12"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCON": {
    "1": {
      "DGNCODE": "KCI-USD12"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 1) 设置RC设计代码（生成/设置）
payload = {
    "Assign": {
        "1": {"DGNCODE": "KCI-USD12"}   # RC设计标准
    }
}
res = requests.post(f"{BASE_URL}/db/DCON", headers=HEADERS, json=payload)
print("POST 结果:", res.status_code, res.json())

# 2) 查询已设置的RC设计代码
res = requests.get(f"{BASE_URL}/db/DCON", headers=HEADERS)
print("当前设计代码:", res.json())

# 3) 修改代码 (PUT) / 删除 (DELETE)
# requests.put(f"{BASE_URL}/db/DCON", headers=HEADERS,
#              json={"Assign": {"1": {"DGNCODE": "ACI318-19"}}})
# requests.delete(f"{BASE_URL}/db/DCON", headers=HEADERS)
```

---

## 2. `/db/DSTL` — Design Steel Code (钢结构设计代码)

> **功能：** 指定钢结构(Steel)构件设计所用的设计标准。以字符串设置 KDS·KSSC·AISC·Eurocode3·AASHTO 等。

### Input URI

```
{base url}/db/DSTL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "DGNCODE": { "description": "Design Code", "type": "string" }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 钢结构设计代码名称（下表字符串之一） | `"DGNCODE"` | String | — | **必填** |

**主要 `DGNCODE` 值（部分摘录 — 按原文共计66种）：**

| Design Code | DGNCODE |
|-------------|---------|
| KDS 41 30 : 2022 | `"KDS 41 30 : 2022"` |
| KDS 24 14 31 : 2018 | `"KDS 24 14 31 : 2018"` |
| KSSC-LSD16 | `"KSSC-LSD16"` |
| KSSC-ASD03 | `"KSSC-ASD03"` |
| AISC(16th)-LRFD22 / AISC(16th)-ASD22 | `"AISC(16th)-LRFD22"` / `"AISC(16th)-ASD22"` |
| AISC(15th)-LRFD16 / AISC(15th)-ASD16 | `"AISC(15th)-LRFD16"` / `"AISC(15th)-ASD16"` |
| AISC-LRFD93 / AISC-ASD89 | `"AISC-LRFD93"` / `"AISC-ASD89"` |
| Eurocode3-2:05 / Eurocode3:05 / Eurocode3 | `"Eurocode3-2:05"` / `"Eurocode3:05"` / `"Eurocode3"` |
| AASHTO-LRFD20(US) | `"AASHTO-LRFD20(US)"` |
| CSA-S6-19 | `"CSA-S6-19"` |
| GB50017-03 | `"GB50017-03"` |
| IS:800-2007 | `"IS:800-2007"` |
| SP 16.13330.2017 | `"SP 16.13330.2017"` |

> 上表仅摘录了代表性取值。此外还支持 KSCE·AIK·BS5950·JTJ·TWN·NSCP·Japan Road 系列等大量代码。

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "Eurocode3-2:05"
    }
  }
}
```

**GET Response Body**

```json
{
  "DSTL": {
    "1": {
      "DGNCODE": "Eurocode3-2:05"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 设置钢结构设计代码
payload = {"Assign": {"1": {"DGNCODE": "AISC(16th)-LRFD22"}}}
res = requests.post(f"{BASE_URL}/db/DSTL", headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 查询
print("当前钢结构代码:", requests.get(f"{BASE_URL}/db/DSTL", headers=HEADERS).json())
```

---

## 3. `/db/RCHK` — Rebar Input for Checking - Beam/Column (验算用钢筋输入)

> **功能：** 按构件(单元)输入设计验算(Checking)时使用的实际配筋信息。依据 `MEMBTYPE` 填充 **BEAM(梁)** 或 **COLUMN(柱)** 两个分支之一，其中详细承载主筋层·副筋(剪力/扭转/束筋)信息。

### Input URI

```
{base url}/db/RCHK
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "RCHK": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "MEMBTYPE": { "description": "MEMBTYPE (BEAM / COLUMN)", "type": "string" },
      "ENVTYPE":  { "description": "Environment Type (crack checking)", "type": "integer" },
      "BEAM": {
        "description": "BEAM (MEMBTYPE == BEAM 일 때)",
        "type": "object",
        "properties": {
          "vMAIN": {
            "description": "Main Rebar Datas [I, M, J]",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "SECTOR": { "type": "string" },
                "POS_TOP_LAYERS": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "LAYER":     { "type": "integer" },
                      "dD":        { "type": "number" },
                      "BAR_NUM":   { "type": "integer" },
                      "BAR_NAME1": { "type": "string" },
                      "BAR_NAME2": { "type": "string" }
                    }
                  }
                },
                "POS_BOT_LAYERS": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "LAYER":     { "type": "integer" },
                      "dD":        { "type": "number" },
                      "BAR_NUM":   { "type": "integer" },
                      "BAR_NAME1": { "type": "string" },
                      "BAR_NAME2": { "type": "string" }
                    }
                  }
                }
              }
            }
          },
          "vSUB_BAR": {
            "description": "Sub Rebar Data [I, M, J]",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "SECTOR":          { "type": "string" },
                "dSUB_BARNUM":     { "type": "number" },
                "SUB_BARNAME":     { "type": "string" },
                "dSUB_BARDIST":    { "type": "number" },
                "dSUB_BARANGLE":   { "type": "number" },
                "bTORSIONAL_BAR":  { "type": "boolean" },
                "sTRTORBARNA":     { "type": "string" },
                "dTORBAR_SPACING": { "type": "number" },
                "bBUNDLEDBAR":     { "type": "boolean" },
                "dBUNDLEDBARNUM":  { "type": "number" },
                "LONGIBARNA":      { "type": "string" },
                "dLONGIBARNUM":    { "type": "number" }
              }
            }
          }
        }
      },
      "COLM": {
        "description": "COLM (MEMBTYPE == COLUMN 일 때)",
        "type": "object",
        "properties": {
          "vLAYER": {
            "description": "Main Rebar Layers",
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "INDEX": { "type": "integer" },
                "dDc":   { "type": "number" },
                "vPOSITION": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "POSITION":  { "type": "string" },
                      "BAR_NUM":   { "type": "integer" },
                      "BAR_NAME1": { "type": "string" },
                      "BAR_NAME2": { "type": "string" }
                    }
                  }
                }
              }
            }
          },
          "SUB_BAR": {
            "type": "object",
            "properties": {
              "SUBBAR_NAME":   { "type": "string" },
              "SUBBAR_DIST":   { "type": "number" },
              "SUBBAR_NUM":    { "type": "number" },
              "SUBBAR_NAME_Y": { "type": "string" },
              "SUBBAR_NAME_Z": { "type": "string" },
              "SUBBAR_NUM_Y":  { "type": "number" },
              "SUBBAR_NUM_Z":  { "type": "number" }
            }
          }
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 构件类型 · 梁: `"BEAM"` / 柱: `"COLUMN"` | `"MEMBTYPE"` | String | — | **必填** |
| 2 | 裂缝验算(暴露环境) · Class 1: `0` / Class 2: `1` | `"ENVTYPE"` | Integer | — | **必填** |

**MEMBTYPE == `"BEAM"` 时 — `"BEAM"` 对象**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 纵向钢筋（按区段 [I, J, M] 的对象数组） | `"vMAIN"` | Array[Object] | — | **必填** |
| i | 区段 · I端: `"I"` / J端: `"J"` / 跨中: `"M"` | `"SECTOR"` | String | — | **必填** |
| ii | 顶部钢筋层信息¹⁾ | `"POS_TOP_LAYERS"` | Array[Object] | — | **必填** |
| iii | 底部钢筋层信息¹⁾ | `"POS_BOT_LAYERS"` | Array[Object] | — | **必填** |
| (2) | 横向(剪力/扭转)钢筋（按区段 [I, J, M]） | `"vSUB_BAR"` | Array[Object] | — | **必填** |
| i | 区段 · `"I"` / `"J"` / `"M"` | `"SECTOR"` | String | — | **必填** |
| ii | 钢筋根数 | `"dSUB_BARNUM"` | Integer | — | **必填** |
| iii | 钢筋规格 | `"SUB_BARNAME"` | String | — | **必填** |
| iv | 钢筋间距 | `"dSUB_BARDIST"` | Number | — | **必填** |
| v | 与构件的角度 | `"dSUB_BARANGLE"` | Number | — | **必填** |
| vi | 是否使用扭转钢筋 | `"bTORSIONAL_BAR"` | Boolean | — | 可选 |
| vii | 扭转钢筋规格 | `"sTRTORBARNA"` | String | — | 可选 |
| viii | 扭转钢筋间距 | `"dTORBAR_SPACING"` | Number | — | 可选 |
| ix | 是否使用束筋(Bundled) | `"bBUNDLEDBAR"` | Boolean | — | 可选 |
| x | 束筋根数 | `"dBUNDLEDBARNUM"` | Number | — | 可选 |
| xi | 纵向钢筋规格 | `"LONGIBARNA"` | String | — | 可选 |
| xii | 纵向钢筋根数 | `"dLONGIBARNUM"` | Number | — | 可选 |

> ⚠️ 2026-08-26 确认 (article id `35993850335897`)：`vi`~`xii`（与扭转·束筋·纵向钢筋相关的
> 7个字段）在官方 JSON Schema 中存在，但官方 Specifications 表中完全未列出
>（表从 `dSUB_BARANGLE` 直接跳到 `COLM` 对象）。也没有 Required 的数组指定，
> 故视为 Optional 予以记载。

**MEMBTYPE == `"COLUMN"` 时 — `"COLM"` 对象**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 纵向钢筋层数组 | `"vLAYER"` | Array[Object] | — | **必填** |
| i | 层索引 (1~5) | `"INDEX"` | Integer | — | **必填** |
| ii | 表面~钢筋中心保护层距离 | `"dDc"` | Number | — | **必填** |
| iii | 钢筋层(按位置)²⁾ | `"vPOSITION"` | Array[Object] | — | **必填** |
| (2) | 横向钢筋 | `"SUB_BAR"` | Object | — | **必填** |
| i | 钢筋规格 | `"SUBBAR_NAME"` | String | — | **必填** |
| ii | 钢筋间距 | `"SUBBAR_DIST"` | Number | — | **必填** |
| iii | 钢筋根数 | `"SUBBAR_NUM"` | Integer | — | **必填** |
| iv | Y方向钢筋规格 | `"SUBBAR_NAME_Y"` | String | — | **必填** |
| v | Z方向钢筋规格 | `"SUBBAR_NAME_Z"` | String | — | **必填** |
| vi | Y方向钢筋根数 | `"SUBBAR_NUM_Y"` | Integer | — | **必填** |
| vii | Z方向钢筋根数 | `"SUBBAR_NUM_Z"` | Integer | — | **必填** |

**¹⁾ 梁钢筋层（`POS_TOP_LAYERS` / `POS_BOT_LAYERS` 条目结构）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 层编号 | `"LAYER"` | Integer | — | **必填** |
| (2) | 表面~钢筋中心保护层距离 | `"dD"` | Number | — | **必填** |
| (3) | 钢筋根数 | `"BAR_NUM"` | Integer | — | **必填** |
| (4) | 钢筋规格1 | `"BAR_NAME1"` | String | — | **必填** |
| (5) | 钢筋规格2 | `"BAR_NAME2"` | String | Blank | 可选 |

**²⁾ 柱钢筋层（`vPOSITION` 条目结构）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 表面位置 · 圆形: `"P1"` / 矩形: `"P1"`, `"P2"` | `"POSITION"` | String | — | **必填** |
| (2) | 钢筋根数 | `"BAR_NUM"` | Number | — | **必填** |
| (3) | 钢筋规格1 | `"BAR_NAME1"` | String | — | **必填** |
| (4) | 钢筋规格2 | `"BAR_NAME2"` | String | Blank | 可选 |

### Request / Response JSON

**POST / PUT Request Body（柱 + 梁 混合）**

```json
{
  "Assign": {
    "1": {
      "MEMBTYPE": "COLUMN",
      "ENVTYPE": 0,
      "COLM": {
        "vLAYER": [
          {
            "INDEX": 1,
            "dDc": 0.1,
            "vPOSITION": [
              { "POSITION": "P1", "BAR_NUM": 24, "BAR_NAME1": "#4", "BAR_NAME2": "" }
            ]
          },
          {
            "INDEX": 2,
            "dDc": 0.2,
            "vPOSITION": [
              { "POSITION": "P1", "BAR_NUM": 24, "BAR_NAME1": "#4", "BAR_NAME2": "" }
            ]
          }
        ],
        "SUB_BAR": {
          "SUBBAR_NAME": "#4",
          "SUBBAR_DIST": 0.1,
          "SUBBAR_NUM": 12,
          "SUBBAR_NAME_Y": "#4",
          "SUBBAR_NAME_Z": "#4",
          "SUBBAR_NUM_Y": 12,
          "SUBBAR_NUM_Z": 12
        }
      }
    },
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 1,
      "BEAM": {
        "vMAIN": [
          {
            "SECTOR": "I",
            "POS_TOP_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": "" }
            ],
            "POS_BOT_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": "" }
            ]
          },
          {
            "SECTOR": "M",
            "POS_TOP_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": "" }
            ],
            "POS_BOT_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": "" }
            ]
          },
          {
            "SECTOR": "J",
            "POS_TOP_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": "" }
            ],
            "POS_BOT_LAYERS": [
              { "LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": "" }
            ]
          }
        ],
        "vSUB_BAR": [
          { "SECTOR": "I", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6", "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90 },
          { "SECTOR": "M", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6", "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90 },
          { "SECTOR": "J", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6", "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90 }
        ]
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "RCHK": {
    "1": {
      "MEMBTYPE": "COLUMN",
      "ENVTYPE": 0,
      "COLM": {
        "vLAYER": [
          {
            "INDEX": 1,
            "dDc": 0.1,
            "vPOSITION": [
              { "POSITION": "P1", "BAR_NUM": 24, "BAR_NAME1": "#4", "BAR_NAME2": "" }
            ]
          }
        ],
        "SUB_BAR": {
          "SUBBAR_NAME": "#4",
          "SUBBAR_DIST": 0.1,
          "SUBBAR_NUM": 12,
          "SUBBAR_NAME_Y": "#4",
          "SUBBAR_NAME_Z": "#4",
          "SUBBAR_NUM_Y": 12,
          "SUBBAR_NUM_Z": 12
        }
      }
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 向单元2(梁)输入验算用钢筋
beam_rebar = {
    "Assign": {
        "2": {
            "MEMBTYPE": "BEAM",
            "ENVTYPE": 1,
            "BEAM": {
                "vMAIN": [
                    {
                        "SECTOR": "I",
                        "POS_TOP_LAYERS": [
                            {"LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#5", "BAR_NAME2": ""}
                        ],
                        "POS_BOT_LAYERS": [
                            {"LAYER": 1, "dD": 0.1, "BAR_NUM": 12, "BAR_NAME1": "#7", "BAR_NAME2": ""}
                        ],
                    }
                ],
                "vSUB_BAR": [
                    {"SECTOR": "I", "dSUB_BARNUM": 2, "SUB_BARNAME": "#6",
                     "dSUB_BARDIST": 0.1, "dSUB_BARANGLE": 90}
                ],
            },
        }
    }
}
res = requests.post(f"{BASE_URL}/db/RCHK", headers=HEADERS, json=beam_rebar)
print("POST:", res.status_code)

# 查询
print(requests.get(f"{BASE_URL}/db/RCHK", headers=HEADERS).json())
```

---

## 4. `/db/LENG` — Unbraced Length (未支撑长度)

> **功能：** 按单元输入构件屈曲验算所用的未支撑长度(Unbraced Length)。可指定强轴/弱轴(Ly, Lz)、侧向扭转屈曲长度(Lb, Lt)，也可设置按代码自动计算。

### Input URI

```
{base url}/db/LENG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "LY":        { "description": "Unbraced Length Ly", "type": "number" },
      "LZ":        { "description": "Unbraced Length Lz", "type": "number" },
      "LB":        { "description": "Laterally Unbraced Length", "type": "number" },
      "bNOTUSE":   { "description": "Do not consider", "type": "boolean" },
      "bAUTOCALC": { "description": "Calculate by Code", "type": "boolean" },
      "LT":        { "description": "Torsional Unbraced Length", "type": "number" }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 未支撑长度 Ly（强轴） | `"LY"` | Number | `0` | 可选 |
| 2 | 未支撑长度 Lz（弱轴） | `"LZ"` | Number | `0` | 可选 |
| 3 | 侧向未支撑长度 Lb | `"LB"` | Number | `0` | 可选 |
| 4 | 不考虑侧向未支撑长度 | `"bNOTUSE"` | Boolean | `false` | 可选 |
| 5 | 按代码自动计算 | `"bAUTOCALC"` | Boolean | `false` | 可选 |
| 6 | 扭转未支撑长度 Lt | `"LT"` | Number | `0` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "21": {
      "LY": 9.464111,
      "LZ": 4,
      "LB": 4,
      "bNOTUSE": false,
      "bAUTOCALC": false,
      "LT": 9.464111
    }
  }
}
```

**GET Response Body**

```json
{
  "LENG": {
    "21": {
      "LY": 9.464111,
      "LZ": 4,
      "LB": 4,
      "bNOTUSE": false,
      "bAUTOCALC": false,
      "LT": 9.464111
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 为单元21指定未支撑长度
payload = {
    "Assign": {
        "21": {"LY": 9.464111, "LZ": 4, "LB": 4,
               "bNOTUSE": False, "bAUTOCALC": False, "LT": 9.464111}
    }
}
res = requests.post(f"{BASE_URL}/db/LENG", headers=HEADERS, json=payload)
print("POST:", res.status_code)

# 查询 / 删除
print(requests.get(f"{BASE_URL}/db/LENG", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/LENG", headers=HEADERS)
```

---

## 5. `/db/MEMB` — Member Assignment (设计构件指定)

> **功能：** 将多个单元合并指定为一个设计构件(Design Member)。在 `AELEM` 中放入单元编号数组，必要时反转局部坐标方向(`bREVERSE`)。
>
> ⚠️ 这是**DB记录(CRUD)**。请勿与实际执行构件指定的作业端点 `/ope/MEMB`(第15章)混淆。

### Input URI

```
{base url}/db/MEMB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "AELEM": {
        "description": "Element Lists",
        "type": "array",
        "items": { "type": "integer" }
      },
      "bREVERSE": {
        "description": "Reverse Local Direction",
        "type": "boolean"
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 合并为设计构件的单元编号列表 | `"AELEM"` | Array[Integer] | — | **必填** |
| 2 | 反转局部坐标方向 | `"bREVERSE"` | Boolean | `false` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [36, 48, 46, 49, 47]
    },
    "2": {
      "AELEM": [32, 43],
      "bREVERSE": true
    }
  }
}
```

**GET Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [36, 48, 46, 49, 47],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [32, 43],
      "bREVERSE": true
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 设计构件指定（2个构件）
payload = {
    "Assign": {
        "1": {"AELEM": [36, 48, 46, 49, 47]},
        "2": {"AELEM": [32, 43], "bREVERSE": True},
    }
}
res = requests.post(f"{BASE_URL}/db/MEMB", headers=HEADERS, json=payload)
print("POST:", res.status_code)

# 查询
print(requests.get(f"{BASE_URL}/db/MEMB", headers=HEADERS).json())
```

---

## 6. `/db/DCTL` — Definition of Frame (框架定义)

> **功能：** 定义设计时框架的屈曲行为(侧向约束/非侧向约束)与有效屈曲长度系数(K)是否自动计算、设计平面(Design Type)。

### Input URI

```
{base url}/db/DCTL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "FRAMEX": { "description": "X-Direction of Frame", "type": "string" },
      "FRAMEY": { "description": "Y-Direction of Frame", "type": "string" },
      "bAUTOKF": { "description": "Auto Calculate Effective Length Factor", "type": "boolean" },
      "DT": { "description": "Design Type", "type": "string" }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 框架X方向 · 非侧向约束·Sway: `"Unbraced Sway"` / 侧向约束·Non-sway: `"Braced Non-sway"` | `"FRAMEX"` | String | `"Braced Non-sway"` | 可选 |
| 2 | 框架Y方向 · `"Unbraced Sway"` / `"Braced Non-sway"` | `"FRAMEY"` | String | `"Braced Non-sway"` | 可选 |
| 3 | 有效屈曲长度系数自动计算 | `"bAUTOKF"` | Boolean | `false` | 可选 |
| 4 | 设计类型 · 3-D: `"3D"` / X-Z平面: `"XZ"` / Y-Z平面: `"YZ"` / X-Y平面: `"XY"` | `"DT"` | String | `"3D"` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XY"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCTL": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XY"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {
            "FRAMEX": "Braced Non-sway",
            "FRAMEY": "Unbraced Sway",
            "bAUTOKF": True,
            "DT": "3D",
        }
    }
}
res = requests.post(f"{BASE_URL}/db/DCTL", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/DCTL", headers=HEADERS).json())
```

---

## 7. `/db/LTSR` — Limiting Slenderness Ratio (长细比限制)

> **功能：** 按单元指定构件的受压/受拉长细比限值(Limiting Slenderness Ratio)，或省略验算(`bNOTCHECK`)。

### Input URI

```
{base url}/db/LTSR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "Argument": {
    "type": "object",
    "properties": {
      "bNOTCHECK": { "description": "Do not check", "type": "boolean" },
      "COMP": { "description": "Compression", "type": "number" },
      "TENS": { "description": "Tension", "type": "number" }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 省略长细比验算 | `"bNOTCHECK"` | Boolean | `false` | 可选 |
| 2 | 受压极限长细比 | `"COMP"` | Number | — | **必填** |
| 3 | 受拉极限长细比 | `"TENS"` | Number | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

> 原文示例的最上层键使用 `"LTSR"`，此处建议与本章的公共约定(以及其他端点)一致，采用 `"Assign"` 包装。下方为整理成 `"Assign"` 形式的示例。

```json
{
  "Assign": {
    "602": { "bNOTCHECK": false, "COMP": 150, "TENS": 400 },
    "651": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 },
    "734": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 }
  }
}
```

**GET Response Body**

```json
{
  "LTSR": {
    "602": { "bNOTCHECK": false, "COMP": 150, "TENS": 400 },
    "651": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 },
    "734": { "bNOTCHECK": false, "COMP": 200, "TENS": 300 }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "602": {"bNOTCHECK": False, "COMP": 150, "TENS": 400},
        "651": {"bNOTCHECK": False, "COMP": 200, "TENS": 300},
    }
}
res = requests.post(f"{BASE_URL}/db/LTSR", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/LTSR", headers=HEADERS).json())
```

---

## 8. `/db/MBTP` — Modify Member Type (构件类型修改)

> **功能：** 指定·变更单元的设计构件类型(Column / Beam / Brace)。

### Input URI

```
{base url}/db/MBTP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "Argument": {
      "type": "object",
      "properties": {
        "TYPE": { "description": "Member Type", "type": "string" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 构件类型 · 柱: `"COLUMN"` / 梁: `"BEAM"` / 支撑: `"BRACE"` | `"TYPE"` | String | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "160": { "TYPE": "COLUMN" },
    "174": { "TYPE": "COLUMN" },
    "188": { "TYPE": "BEAM" },
    "306": { "TYPE": "BEAM" },
    "376": { "TYPE": "BRACE" },
    "377": { "TYPE": "BRACE" }
  }
}
```

**GET Response Body**

```json
{
  "MBTP": {
    "160": { "TYPE": "COLUMN" },
    "188": { "TYPE": "BEAM" },
    "376": { "TYPE": "BRACE" }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "160": {"TYPE": "COLUMN"},
        "188": {"TYPE": "BEAM"},
        "376": {"TYPE": "BRACE"},
    }
}
res = requests.post(f"{BASE_URL}/db/MBTP", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/MBTP", headers=HEADERS).json())
```

---

## 9. `/db/WMAK` — Modify Wall Mark Design (墙体标记设计修改)

> **功能：** 定义设计用墙体标记(Wall Mark)。指定标记名称及属于该标记的墙体ID列表。

### Input URI

```
{base url}/db/WMAK
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "WMAK": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "MARKNAME": { "description": "Wall Mark Name", "type": "string" },
      "WID_LIST": {
        "description": "Wall ID List",
        "type": "array",
        "items": { "type": "integer" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 墙体标记名称 | `"MARKNAME"` | String | — | **必填** |
| 2 | 墙体ID列表 | `"WID_LIST"` | Array[Integer] | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": { "MARKNAME": "W1", "WID_LIST": [1, 5, 8] },
    "2": { "MARKNAME": "W2", "WID_LIST": [2, 3, 4, 6, 7] },
    "3": { "MARKNAME": "W3", "WID_LIST": [9, 10, 11] }
  }
}
```

**GET Response Body**

```json
{
  "WMAK": {
    "1": { "MARKNAME": "W1", "WID_LIST": [1, 5, 8] },
    "2": { "MARKNAME": "W2", "WID_LIST": [2, 3, 4, 6, 7] }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {"MARKNAME": "W1", "WID_LIST": [1, 5, 8]},
        "2": {"MARKNAME": "W2", "WID_LIST": [2, 3, 4, 6, 7]},
    }
}
res = requests.post(f"{BASE_URL}/db/WMAK", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/WMAK", headers=HEADERS).json())
```

---

## 10. `/db/REBB` — Modify Beam Rebar Data (梁钢筋数据修改)

> **功能：** 按截面(section)编号修改混凝土梁的钢筋数据。各 `ITEMS` 条目包含 I·M·J 三个区段(`BAR_SECTOR_I/M/J`)的上·下部主筋、箍筋(剪力钢筋)、表面钢筋(skin bar)信息与保护层距离(`MAIN_BAR_DC_*`)。

### Input URI

```
{base url}/db/REBB
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 实际schema中每个钢筋规格 `NAME` 都重复罗列 `D4`~`D57` 的 enum 列表，体积很大。以下是摘要其有意义结构的schema(规格 enum 以 `D4`~`D57` 缩略)。

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 단면 번호 문자열 (예: \"211\")",
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "default": false },
                  "ID": { "type": "integer", "description": "Sub Section ID (read only)" },
                  "BAR_SECTOR_I": { "type": "object", "description": "I단 구간 철근" },
                  "BAR_SECTOR_M": { "type": "object", "description": "중앙(M) 구간 철근" },
                  "BAR_SECTOR_J": { "type": "object", "description": "J단 구간 철근" },
                  "MAIN_BAR_DC_TOP": { "type": "number", "description": "상단 피복 dT" },
                  "MAIN_BAR_DC_BOT": { "type": "number", "description": "하단 피복 dB" },
                  "bSAME_SIZE_TOP_BOT": { "type": "boolean" },
                  "bSAME_SIZE_IMJ": { "type": "boolean" },
                  "bSAME_SIZE_LAYER": { "type": "boolean" },
                  "ELEMS": {
                    "type": "object",
                    "description": "CREATE_SUB_SECTION=true 일 때. KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

各 `BAR_SECTOR_*` 对象(按区段的钢筋)结构：

```json
{
  "MAIN_BAR_TOP": {
    "LAYER1": { "NAME": "D19", "NUM": 4 },
    "LAYER2": { "NAME": "D16", "NUM": 2 }
  },
  "MAIN_BAR_BOT": {
    "LAYER1": { "NAME": "D19", "NUM": 4 },
    "LAYER2": { "NAME": "D16", "NUM": 2 }
  },
  "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
  "SKIN_BAR": { "NAME": "D10", "NUM": 2 }
}
```

### 参数

**Root / Item 通用**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 以截面编号字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 1 | 混凝土梁钢筋条目 (min 1) | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否创建子截面 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 可选 |
| (2) | I端区段钢筋 | `"BAR_SECTOR_I"` | Object | — | **必填** |
| (3) | 跨中(M)区段钢筋 | `"BAR_SECTOR_M"` | Object | — | **必填** |
| (4) | J端区段钢筋 | `"BAR_SECTOR_J"` | Object | — | **必填** |
| (5) | 顶部保护层距离 dT | `"DT"` (示例中为 `"MAIN_BAR_DC_TOP"`) | Number | — | **必填** |
| (6) | 底部保护层距离 dB | `"DB"` (示例中为 `"MAIN_BAR_DC_BOT"`) | Number | — | **必填** |

**`BAR_SECTOR_I/M/J` 区段对象 (a~d)**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| a | 顶部钢筋 | `"MAIN_BAR_TOP"` | Object | — | **必填** |
| a→(a) | 第1层 | `"LAYER1"` | Object | — | **必填** |
| a→(d) | 第2层 | `"LAYER2"` | Object | — | 可选 |
| — | 层内钢筋规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| — | 层内钢筋根数 | `"NUM"` | Integer | — | **必填** |
| b | 底部钢筋 | `"MAIN_BAR_BOT"` | Object (LAYER1/LAYER2) | — | **必填** |
| c | 箍筋(剪力钢筋) | `"SHEAR_BAR"` | Object | — | **必填** |
| c→ | 箍筋规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| c→ | 肢(leg)数 | `"LEG"` | Integer | — | **必填** |
| c→ | 箍筋间距 @ | `"DIST"` | Number | — | **必填** |
| d | 表面钢筋(skin bar) | `"SKIN_BAR"` | Object | — | 可选 |
| d→ | 表面钢筋规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| d→ | 表面钢筋根数 | `"NUM"` | Integer | — | **必填** |

**`CREATE_SUB_SECTION == true` 时**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 子截面ID (只读) | `"ID"` | Integer | — | 可选 |
| (2) | 单元列表 (KEYS / TO / STRUCTURE_GROUP_NAME 三选一) | `"ELEMS"` | Object | — | **必填** |
| a | 单元ID数组 | `"KEYS"` | Array[Integer] | — | 可选 |
| b | ID范围 (例：`"1to160"`) | `"TO"` | String | — | 可选 |
| c | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |

> 参考：Request/Response 示例中将各区段的上·下部主筋记为 `"vMAIN_BAR_TOP"` / `"vMAIN_BAR_BOT"` **数组**，保护层距离记为 `"MAIN_BAR_DC_TOP"` / `"MAIN_BAR_DC_BOT"`。实际发送时建议原样遵循下方示例格式。

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "211": {
      "ITEMS": [
        {
          "ID": 0,
          "BAR_SECTOR_I": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_M": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_J": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "MAIN_BAR_DC_TOP": 0.06999999999999999,
          "MAIN_BAR_DC_BOT": 0.06999999999999999,
          "bSAME_SIZE_TOP_BOT": true,
          "bSAME_SIZE_IMJ": true,
          "bSAME_SIZE_LAYER": true
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBB": {
    "211": {
      "ITEMS": [
        {
          "ID": 0,
          "BAR_SECTOR_I": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_M": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "BAR_SECTOR_J": {
            "vMAIN_BAR_TOP": [],
            "vMAIN_BAR_BOT": [],
            "SHEAR_BAR": { "NAME": "D10", "LEG": 2, "DIST": 0.1 },
            "SKIN_BAR_NAME": "",
            "SKIN_BAR_NUM": 2
          },
          "MAIN_BAR_DC_TOP": 0.06999999999999999,
          "MAIN_BAR_DC_BOT": 0.06999999999999999,
          "bSAME_SIZE_TOP_BOT": true,
          "bSAME_SIZE_IMJ": true,
          "bSAME_SIZE_LAYER": true
        }
      ]
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 修改截面211的梁钢筋数据
sector = {
    "vMAIN_BAR_TOP": [],
    "vMAIN_BAR_BOT": [],
    "SHEAR_BAR": {"NAME": "D10", "LEG": 2, "DIST": 0.1},
    "SKIN_BAR_NAME": "",
    "SKIN_BAR_NUM": 2,
}
payload = {
    "Assign": {
        "211": {
            "ITEMS": [
                {
                    "ID": 0,
                    "BAR_SECTOR_I": sector,
                    "BAR_SECTOR_M": sector,
                    "BAR_SECTOR_J": sector,
                    "MAIN_BAR_DC_TOP": 0.07,
                    "MAIN_BAR_DC_BOT": 0.07,
                    "bSAME_SIZE_TOP_BOT": True,
                    "bSAME_SIZE_IMJ": True,
                    "bSAME_SIZE_LAYER": True,
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBB", headers=HEADERS, json=payload)
print("POST:", res.status_code)

# 查询 (PUT/DELETE 亦支持相同URI)
print(requests.get(f"{BASE_URL}/db/REBB", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/REBB", headers=HEADERS)
```

---

## 11. `/db/REBC` — Modify Column Rebar Data (柱钢筋数据修改)

> **功能：** 按截面编号修改混凝土柱的钢筋数据。包含主筋(`MAIN_BAR`)、端部/中部剪力钢筋(`SHEAR_BAR_END`/`SHEAR_BAR_CEN`)、保护层距离(`DO`)、箍筋类型(`HOOP_TYPE`)、弯钩类型(`HOOK_TYPE`)。
>
> ⚠️ **本端点仅支持 `POST`。**(不支持 GET/PUT/DELETE)

### Input URI

```
{base url}/db/REBC
```

### Active Methods

`POST`

### JSON Schema

> 规格 enum(`D4`~`D57`) 已缩略。实际schema中每个 `NAME` 都列出完整规格列表。

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 단면 번호 문자열 (예: \"1\")",
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "Concrete column rebar items.",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["MAIN_BAR", "SHEAR_BAR_END", "SHEAR_BAR_CEN", "DO"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "default": false },
                  "ID": { "type": "integer", "description": "Sub Section ID (read only)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "CREATE_SUB_SECTION=true 일 때. KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "required": ["NAME", "NUM", "ROW", "USE_CORNER"],
                    "properties": {
                      "NAME": { "type": "string", "description": "Main rebar size (D4~D57)" },
                      "NUM": { "type": "integer", "description": "Total number of rebars" },
                      "ROW": { "type": "integer", "description": "Number of column row for rebar" },
                      "USE_CORNER": { "type": "boolean" },
                      "NAME_CORNER": { "type": "string", "description": "Corner rebar size (USE_CORNER=true 일 때)" }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "Hoop rebar size (D4~D57)" },
                      "LEG_Y": { "type": "integer", "description": "Number of leg (local Y dir.)" },
                      "LEG_Z": { "type": "integer", "description": "Number of leg (local Z dir.)" },
                      "DIST": { "type": "number", "description": "Distance between rebars" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "Hoop rebar size (D4~D57)" },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "Distance from concrete face to center of rebar" },
                  "HOOP_TYPE": {
                    "type": "string",
                    "default": "Ties",
                    "oneOf": [
                      { "title": "Ties", "const": "Ties" },
                      { "title": "Spirals", "const": "Spirals" }
                    ]
                  },
                  "HOOK_TYPE": {
                    "type": "integer",
                    "default": 0,
                    "oneOf": [
                      { "title": "90+(135 or 180)", "const": 0 },
                      { "title": "Both(135 or 180)", "const": 1 }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 参数

**Root / Item**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 以截面编号字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 1 | 混凝土柱钢筋条目 (min 1) | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否创建子截面 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 可选 |
| (2) | 子截面ID (只读) | `"ID"` | Integer | — | 可选 |
| (3) | 主筋 | `"MAIN_BAR"` | Object | — | **必填** |
| (4) | 端部剪力钢筋 | `"SHEAR_BAR_END"` | Object | — | **必填** |
| (5) | 中部剪力钢筋 | `"SHEAR_BAR_CEN"` | Object | — | **必填** |
| (6) | 混凝土面~钢筋中心距离 (do) | `"DO"` | Number | — | **必填** |
| (7) | 箍筋类型 · `"Ties"` / `"Spirals"` | `"HOOP_TYPE"` | String | `"Ties"` | 可选 |
| (8) | 弯钩类型 · `0`: 90+(135 or 180) / `1`: Both(135 or 180) | `"HOOK_TYPE"` | Enum(Integer) | `0` | 可选 |

**`MAIN_BAR` 对象**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| a | 主筋规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| b | 钢筋总根数 | `"NUM"` | Integer | — | **必填** |
| c | 排(row)数 | `"ROW"` | Integer | — | **必填** |
| d | 是否使用角筋 | `"USE_CORNER"` | Boolean | — | **必填** |
| a' | 角筋规格 (USE_CORNER=true 时) | `"NAME_CORNER"` | String | — | **必填** |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 对象 (端部·中部通用结构)**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| a | 箍筋规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| b | 肢数 (local Y) | `"LEG_Y"` | Integer | — | **必填** |
| c | 肢数 (local Z) | `"LEG_Z"` | Integer | — | **必填** |
| d | 钢筋间距 @ | `"DIST"` | Number | — | **必填** |

**`CREATE_SUB_SECTION == true` 时 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 三选一)**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| a | 单元ID数组 | `"KEYS"` | Array[Integer] | — | 可选 |
| b | ID范围 (例：`"1to160"`) | `"TO"` | String | — | 可选 |
| c | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |

### Request JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": false },
          "SHEAR_BAR_END": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100 },
          "SHEAR_BAR_CEN": { "NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200 },
          "DO": 40,
          "HOOP_TYPE": "Ties",
          "HOOK_TYPE": 0
        }
      ]
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

# 修改截面1的柱钢筋数据 (REBC仅支持POST)
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D19", "NUM": 8, "ROW": 3, "USE_CORNER": False},
                    "SHEAR_BAR_END": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 100},
                    "SHEAR_BAR_CEN": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 200},
                    "DO": 40,
                    "HOOP_TYPE": "Ties",
                    "HOOK_TYPE": 0,
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBC", headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# ※ REBC 为 POST 专用，因此不支持 GET/PUT/DELETE。
```

---

## 12. `/db/REBW` — Modify Wall Rebar Data (墙体钢筋数据修改)

> **功能：** 按墙体ID修改钢筋数据。包含竖直/水平钢筋、端部钢筋(End Rebar)、边缘构件(Boundary Element)水平钢筋、保护层距离(dw, de)、厚度及子墙体ID/楼层(Story)信息。

### Input URI

```
{base url}/db/REBW
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 规格 enum(`D4`~`D57`) 已缩略。

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 벽체 ID 문자열 (예: \"1\")",
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "properties": {
                  "CREATE_SUB_WALL_ID": { "type": "boolean", "default": false },
                  "SUB_WALL_ID": { "type": "integer", "description": "read only" },
                  "STORY": {
                    "type": "object",
                    "properties": {
                      "FROM": { "type": "string" },
                      "TO": { "type": "string" }
                    }
                  },
                  "VERTICAL_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "HORIZONTAL_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "USE_END_REBAR": { "type": "boolean", "default": false },
                  "END_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "NUM": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "BE_HORIZONTAL_REBAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "BOUNDARY_ELEMENT_LENGTH": { "type": "number", "default": 0 },
                  "CONCRETE_FACE_TO_CENTER_OF_REBAR": {
                    "type": "object",
                    "properties": {
                      "DW": { "type": "number" },
                      "DE": { "type": "number" }
                    }
                  },
                  "USE_MODEL_THICKNESS": { "type": "boolean", "default": true },
                  "THICKNESS": { "type": "number", "description": "USE_MODEL_THICKNESS=false 일 때" }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 以墙体ID字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 1 | 墙体钢筋条目 (min 1) | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否创建子墙体ID | `"CREATE_SUB_WALL_ID"` | Boolean | `false` | 可选 |
| (2) | 竖直钢筋 | `"VERTICAL_REBAR"` | Object | — | **必填** |
| (2)a | 规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| (2)b | 竖直钢筋间距 @ | `"DIST"` | Number | — | **必填** |
| (3) | 水平钢筋 | `"HORIZONTAL_REBAR"` | Object (NAME/DIST) | — | **必填** |
| (4) | 是否使用端部钢筋 | `"USE_END_REBAR"` | Boolean | `false` | 可选 |
| (5) | 边缘构件水平钢筋 | `"BE_HORIZONTAL_REBAR"` | Object (NAME/DIST) | — | 可选 |
| (6) | 边缘构件长度 | `"BOUNDARY_ELEMENT_LENGTH"` | Number | `0` | 可选 |
| (7) | 混凝土面~钢筋中心距离 (dw, de) | `"CONCRETE_FACE_TO_CENTER_OF_REBAR"` | Object | — | **必填** |
| (7)a | dw | `"DW"` | Number | — | **必填** |
| (7)b | de | `"DE"` | Number | — | **必填** |
| (8) | 使用模型厚度 | `"USE_MODEL_THICKNESS"` | Boolean | `true` | 可选 |

**`CREATE_SUB_WALL_ID == true` 时**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 子墙体ID (只读) | `"SUB_WALL_ID"` | Integer | — | **必填** |
| (2) | 楼层范围 | `"STORY"` | Object | — | **必填** |
| (2)a | 起始楼层 | `"FROM"` | String | — | **必填** |
| (2)b | 结束楼层 | `"TO"` | String | — | **必填** |

**`USE_END_REBAR == true` 时 — `END_REBAR`**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| a | 规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| b | 根数 | `"NUM"` | Integer | — | **必填** |
| c | 间距 @ | `"DIST"` | Number | — | **必填** |

**`USE_MODEL_THICKNESS == false` 时**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 厚度 | `"THICKNESS"` | Number | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_WALL_ID": true,
          "VERTICAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "HORIZONTAL_REBAR": { "NAME": "D16", "DIST": 200 },
          "USE_END_REBAR": true,
          "BE_HORIZONTAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "BOUNDARY_ELEMENT_LENGTH": 222,
          "CONCRETE_FACE_TO_CENTER_OF_REBAR": { "DW": 50, "DE": 50 },
          "USE_MODEL_THICKNESS": false,
          "END_REBAR": { "NAME": "D25", "NUM": 2, "DIST": 150 },
          "THICKNESS": 1000,
          "SUB_WALL_ID": 1,
          "STORY": { "FROM": "2F", "TO": "Roof" }
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBW": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_WALL_ID": true,
          "SUB_WALL_ID": 1,
          "STORY": { "FROM": "2F", "TO": "Roof" },
          "VERTICAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "HORIZONTAL_REBAR": { "NAME": "D16", "DIST": 200 },
          "USE_END_REBAR": true,
          "END_REBAR": { "NAME": "D25", "NUM": 2, "DIST": 150 },
          "BE_HORIZONTAL_REBAR": { "NAME": "D19", "DIST": 222 },
          "BOUNDARY_ELEMENT_LENGTH": 222,
          "CONCRETE_FACE_TO_CENTER_OF_REBAR": { "DW": 50, "DE": 50 },
          "USE_MODEL_THICKNESS": false,
          "THICKNESS": 1000
        }
      ]
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_WALL_ID": True,
                    "VERTICAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "HORIZONTAL_REBAR": {"NAME": "D16", "DIST": 200},
                    "USE_END_REBAR": True,
                    "END_REBAR": {"NAME": "D25", "NUM": 2, "DIST": 150},
                    "BE_HORIZONTAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "BOUNDARY_ELEMENT_LENGTH": 222,
                    "CONCRETE_FACE_TO_CENTER_OF_REBAR": {"DW": 50, "DE": 50},
                    "USE_MODEL_THICKNESS": False,
                    "THICKNESS": 1000,
                    "SUB_WALL_ID": 1,
                    "STORY": {"FROM": "2F", "TO": "Roof"},
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBW", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/REBW", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/REBW", headers=HEADERS)
```

---

## 13. `/db/REBR` — Modify Brace Rebar Data (支撑钢筋数据修改)

> **功能：** 按截面编号修改混凝土支撑(Brace)的钢筋数据。结构与柱(REBC)类似，但不含 `USE_CORNER`/`HOOK_TYPE`，由主筋(`MAIN_BAR`)、端部/中部剪力钢筋、保护层(`DO`)、箍筋类型(`HOOP_TYPE`)构成。

### Input URI

```
{base url}/db/REBR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 规格 enum(`D4`~`D57`) 已缩略。

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "키는 단면 번호 문자열 (예: \"1\")",
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "minItems": 1,
              "items": {
                "type": "object",
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "default": false },
                  "ID": { "type": "integer", "description": "read only" },
                  "ELEMS": {
                    "type": "object",
                    "description": "CREATE_SUB_SECTION=true 일 때. KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "NUM": { "type": "integer", "description": "min 4" },
                      "ROW": { "type": "integer" }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "properties": {
                      "NAME": { "type": "string", "description": "D4~D57" },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "Concrete face to center of rebar" },
                  "HOOP_TYPE": {
                    "type": "string",
                    "default": "Ties",
                    "oneOf": [
                      { "title": "Ties", "const": "Ties" },
                      { "title": "Spirals", "const": "Spirals" }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 以截面编号字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 1 | 混凝土支撑钢筋条目 (min 1) | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否创建子截面 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 可选 |
| (2) | 主筋 | `"MAIN_BAR"` | Object | — | **必填** |
| (2)a | 规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| (2)b | 根数 (min 4) | `"NUM"` | Integer | — | **必填** |
| (2)c | 排(row)数 | `"ROW"` | Integer | — | **必填** |
| (3) | 端部剪力钢筋 | `"SHEAR_BAR_END"` | Object | — | **必填** |
| (4) | 中部剪力钢筋 | `"SHEAR_BAR_CEN"` | Object | — | **必填** |
| (5) | 混凝土面~钢筋中心距离 (do) | `"DO"` | Number | — | **必填** |
| (6) | 箍筋类型 · `"Ties"` / `"Spirals"` | `"HOOP_TYPE"` | String | `"Ties"` | 可选 |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 对象 (通用结构)**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| a | 箍筋规格 · `D4`~`D57` | `"NAME"` | String | — | **必填** |
| b | 肢数 (local Y) | `"LEG_Y"` | Integer | — | **必填** |
| c | 肢数 (local Z) | `"LEG_Z"` | Integer | — | **必填** |
| d | 钢筋间距 @ | `"DIST"` | Number | — | **必填** |

**`CREATE_SUB_SECTION == true` 时 — `ELEMS` (KEYS / TO / STRUCTURE_GROUP_NAME 三选一)**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| (1) | 子截面ID (只读) | `"ID"` | Integer | — | 可选 |
| a | 单元ID数组 | `"KEYS"` | Array[Integer] | — | 可选 |
| b | ID范围 (例：`"1to160"`) | `"TO"` | String | — | 可选 |
| c | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D22", "NUM": 4, "ROW": 2 },
          "SHEAR_BAR_END": { "NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300 },
          "SHEAR_BAR_CEN": { "NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300 },
          "DO": 0.05,
          "HOOP_TYPE": "Spirals"
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "REBR": {
    "1": {
      "ITEMS": [
        {
          "CREATE_SUB_SECTION": false,
          "MAIN_BAR": { "NAME": "D22", "NUM": 4, "ROW": 2 },
          "SHEAR_BAR_END": { "NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300 },
          "SHEAR_BAR_CEN": { "NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300 },
          "DO": 0.05,
          "HOOP_TYPE": "Spirals"
        }
      ]
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}

payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D22", "NUM": 4, "ROW": 2},
                    "SHEAR_BAR_END": {"NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300},
                    "SHEAR_BAR_CEN": {"NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300},
                    "DO": 0.05,
                    "HOOP_TYPE": "Spirals",
                }
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/db/REBR", headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(requests.get(f"{BASE_URL}/db/REBR", headers=HEADERS).json())
# requests.delete(f"{BASE_URL}/db/REBR", headers=HEADERS)
```

---

## End-to-End Workflow

下方脚本展示了按顺序构建设计输入DB的典型流程：
**设置RC设计代码(DCON) → 设置钢结构设计代码(DSTL) → 设计构件指定(MEMB) → 设置未支撑长度(LENG) → 柱钢筋指定(REBC)**，随后重新查询(GET)其中一项进行验证。末尾还包含一个简单的 CRUD 辅助函数。

```python
import requests

# ─────────────────────────────────────────────
# 通用设置
# ─────────────────────────────────────────────
BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（桥梁：/civil）
HEADERS = {"MAPI-Key": "<已获取的密钥>", "Content-Type": "application/json"}


def api(method, uri, body=None):
    """用于DB端点的简单CRUD辅助函数。"""
    url = f"{BASE_URL}{uri}"
    res = requests.request(method, url, headers=HEADERS, json=body)
    print(f"[{method:6}] {uri:12} -> {res.status_code}")
    try:
        return res.json()
    except ValueError:
        return res.text


# ─────────────────────────────────────────────
# 1) 设置RC设计代码 (DCON)
# ─────────────────────────────────────────────
api("POST", "/db/DCON", {"Assign": {"1": {"DGNCODE": "KCI-USD12"}}})

# ─────────────────────────────────────────────
# 2) 设置钢结构设计代码 (DSTL)
# ─────────────────────────────────────────────
api("POST", "/db/DSTL", {"Assign": {"1": {"DGNCODE": "AISC(16th)-LRFD22"}}})

# ─────────────────────────────────────────────
# 3) 设计构件指定 (MEMB) — 将多个单元合并为一个设计构件
#    ※ 实际执行指定的“作业”是 /ope/MEMB (第15章)。此处保存DB记录。
# ─────────────────────────────────────────────
api("POST", "/db/MEMB", {
    "Assign": {
        "1": {"AELEM": [36, 48, 46, 49, 47]},
        "2": {"AELEM": [32, 43], "bREVERSE": True},
    }
})

# ─────────────────────────────────────────────
# 4) 设置未支撑长度 (LENG)
# ─────────────────────────────────────────────
api("POST", "/db/LENG", {
    "Assign": {
        "1": {"LY": 9.464111, "LZ": 4, "LB": 4,
              "bNOTUSE": False, "bAUTOCALC": False, "LT": 9.464111}
    }
})

# ─────────────────────────────────────────────
# 5) 柱钢筋指定 (REBC)
# ─────────────────────────────────────────────
api("POST", "/db/REBC", {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "ID": 0,
                    "vMAIN_BAR": [
                        {"NAME": "D19", "NUM": 8, "ROW": 3, "D0": 0.04,
                         "bUSE_CORNER": False, "NAME_CORNER": "D19"}
                    ],
                    "SHEAR_BAR_END": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 0.1},
                    "SHEAR_BAR_CEN": {"NAME": "D10", "LEG_Y": 2, "LEG_Z": 2, "DIST": 0.2},
                    "HOOP_TYPE": 1,
                    "bSAME_SPACE_END_CEN": False,
                    "NUM_BAR_BC_JOINT": 0,
                }
            ]
        }
    }
})

# ─────────────────────────────────────────────
# 6) 验证：重新查询柱钢筋记录
# ─────────────────────────────────────────────
result = api("GET", "/db/REBC")
print("验证结果 (REBC):", result)

# ─────────────────────────────────────────────
# (可选) CRUD 示例 — 修改/删除
# ─────────────────────────────────────────────
# api("PUT",    "/db/DCON", {"Assign": {"1": {"DGNCODE": "ACI318-19"}}})
# api("DELETE", "/db/LENG")
```
