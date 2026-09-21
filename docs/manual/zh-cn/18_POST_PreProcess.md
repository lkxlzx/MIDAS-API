# 18. POST – Pre-Process Tables

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头部：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../18_POST_PreProcess.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

`POST` 部分用于提取前处理·后处理表。本部分（前处理表）的所有端点**均使用通用 URI `{base url}/post/TABLE`**，且仅支持 `POST` 方法。由请求体中 `"Argument"` 对象的 `TABLE_TYPE` 值决定提取哪张表。

---

## 通用事项

### Input URI（前处理表通用）

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 通用 Request 结构

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "<테이블별 고유 값>",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON"
  }
}
```

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 响应表标题（Response Table Title） | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型（各 Endpoint 取值不同） | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径（JSON） | `"EXPORT_PATH"` | String | — | Optional |

> **参考：** 部分表（例如 `ELEMENTWEIGHT`，而非 `NODALBODYFORCE`）可用 `NODE_ELEMS` 指定目标范围，Story 系列表额外支持 `UNIT`·`STYLES`·`COMPONENTS`。详见各节。

### 通用 Response 结构

所有响应均以 `TABLE_NAME`（请求时指定的名称）为键，具有 `FORCE`·`DIST`（单位）、`HEAD`（列名数组）、`DATA`（行数组）的结构。

```json
{
  "<TABLE_NAME>": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

## Endpoint（表）列表

| No. | 表 | `TABLE_TYPE` | 对象指定 |
|-----|--------|--------------|-----------|
| 1 | [Element Weight Table](#1-element-weight-table) | `ELEMENTWEIGHT` | `NODE_ELEMS`（3种方式） |
| 2 | [Nodal Body Force Table](#2-nodal-body-force-table) | `NODALBODYFORCE` | 全部 |
| 3 | [Mass Summary Table](#3-mass-summary-table) | `MASS_SUMMARY_X/Y/Z` | 全部 |
| 4 | [Load Summary Table](#4-load-summary-table) | `LOAD_SUMMARY_X/Y/Z` | 全部 |
| 5 | [Material Table](#5-material-table) | `MATERIAL` | 全部 |
| 6 | [Section Table](#6-section-table) | `SECTIONALL` 及其他9种 | 全部 |
| 7 | [Restraint Supports Table](#7-restraint-supports-table) | `SUPPORTS` | 全部 |
| 8 | [Story Mass Summary Table](#8-story-mass-summary-table) | `STORY_MASS` / `_X/_Y/_Z` | `UNIT`·`STYLES`·`COMPONENTS` |
| 9 | [Story Load Summary Table](#9-story-load-summary-table) | `STORY_LOAD_SUMMARY_X/Y/Z` | 全部 |
| 10 | [Story Weight Table](#10-story-weight-table) | `STORYWEIGHT` | 全部 |

---

## 1. Element Weight Table

> **功能：** 提取各单元的重量（单位重量·总重量等）。可用 `NODE_ELEMS` 以下列3种方式之一指定目标单元，省略时目标为全部单元。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ElementWeightTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "NODE_ELEMS": {
            "type": "object",
            "properties": {
              "TO": { "type": "string" },
              "KEYS": { "type": "array", "items": { "type": "integer" } },
              "STRUCTURE_GROUP_NAME": { "type": "string" }
            },
            "anyOf": [
              { "required": ["TO"] },
              { "required": ["KEYS"] },
              { "required": ["STRUCTURE_GROUP_NAME"] },
              { "not": { "required": ["TO", "KEYS", "STRUCTURE_GROUP_NAME"] } }
            ]
          }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · `"ELEMENTWEIGHT"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 指定节点/单元（下列3种方式仅用其一） | `"NODE_ELEMS"` | Object | All | Optional |
| 4-1 | 方式1：逐个指定 ID（例：`[101, 102, 103]`） | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 4-2 | 方式2：指定 ID 范围（例：`"101 to 105"`） | `NODE_ELEMS.TO` | String | — | Optional |
| 4-3 | 方式3：指定结构组名（例：`"SG1"`） | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "ELEMENTWEIGHT",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Elementweight_all_Output.JSON",
    "NODE_ELEMS": { "TO": "1to5" }
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "No", "Type", "No", "Name", "No", "Name", "No", "Name", "Type", "Value", "UnitWeight", "TotalWeight"],
    "DATA": [
      ["1", "1", "BEAM", "1", "SS235", "1208", "H300x150x6.5/9", "-", "-", "L", "4.0000", "76980.0000", "1440.4500"],
      ["2", "2", "BEAM", "1", "SS235", "1208", "H300x150x6.5/9", "-", "-", "L", "4.0000", "76980.0000", "1440.4500"],
      ["3", "3", "BEAM", "1", "SS235", "1104", "H300x150x6.5/9", "-", "-", "L", "2.0615", "76980.0000", "742.3910"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取1~5号单元的重量表 ────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "ElemWeight",
        "TABLE_TYPE": "ELEMENTWEIGHT",
        "NODE_ELEMS": {"TO": "1to5"}   # 方式2：指定范围
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("ElemWeight", {})
print("HEAD:", table.get("HEAD"))
for row in table.get("DATA", []):
    print(row)

# ── 其他目标指定方式示例 ───────────────────────────────────────
# 方式1：{"KEYS": [1, 2, 3]}
# 方式3：{"STRUCTURE_GROUP_NAME": "SG1"}
# 省略时目标为全部单元
```

---

## 2. Nodal Body Force Table

> **功能：** 按荷载工况提取节点体积力（Nodal Body Force, FX/FY/FZ）。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "NodalBodyForceTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · `"NODALBODYFORCE"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "NODALBODYFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\NodalBodyForce_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "LoadCase", "Node", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "EX", "1", "26.8158", "0.0000", "0.0000"],
      ["2", "EX", "2", "31.0746", "0.0000", "0.0000"],
      ["3", "EX", "3", "86.5800", "0.0000", "0.0000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取节点体积力表 ──────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "NodalBodyForce",
        "TABLE_TYPE": "NODALBODYFORCE"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("NodalBodyForce", {})
print("HEAD:", table.get("HEAD"))
print(f"共 {len(table.get('DATA', []))} 行")
```

---

## 3. Mass Summary Table

> **功能：** 按 X/Y/Z 方向提取各节点的质量汇总（节点质量·荷载质量·结构质量·合计）。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "MassSummaryTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · X方向：`"MASS_SUMMARY_X"` / Y方向：`"MASS_SUMMARY_Y"` / Z方向：`"MASS_SUMMARY_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body（X 方向）**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "MASS_SUMMARY_X",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Mass_Summary_X_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "Node", "NodalMass", "LoadToMass", "StructureMass", "Sum"],
    "DATA": [
      ["1", "1", "200.0000", "0.0000", "73.4631", "273.4631"],
      ["2", "2", "200.0000", "0.0000", "116.8933", "316.8933"],
      ["3", "3", "200.0000", "515.4224", "167.5067", "882.9290"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：分别提取 X/Y/Z 三个方向的质量汇总表 ─────────────────
for direction in ["X", "Y", "Z"]:
    payload = {
        "Argument": {
            "TABLE_NAME": f"Mass_{direction}",
            "TABLE_TYPE": f"MASS_SUMMARY_{direction}"
        }
    }
    resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
    table = resp.json().get(f"Mass_{direction}", {})
    total = sum(float(row[-1]) for row in table.get("DATA", []))
    print(f"{direction}方向质量合计：{total:.4f}")
```

---

## 4. Load Summary Table

> **功能：** 按 X/Y/Z 方向提取各荷载工况的荷载汇总（集中·梁·楼面·压力·自重·合计）。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "LoadSummaryTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · X方向：`"LOAD_SUMMARY_X"` / Y方向：`"LOAD_SUMMARY_Y"` / Z方向：`"LOAD_SUMMARY_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body（Z 方向）**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "LOAD_SUMMARY_Z",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Load_Summary_Z_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "N",
    "DIST": "m",
    "HEAD": ["Index", "Load", "Concent", "Beam", "Floor", "Pressure", "SelfWeight", "Sum"],
    "DATA": [
      ["1", "DL", "-9.000e+02", "0.000e+00", "-6.469e+05", "0.000e+00", "-1.005e+05", "-7.483e+05"],
      ["2", "LL", "-7.200e+02", "0.000e+00", "-1.294e+06", "0.000e+00", "0.000e+00", "-1.295e+06"],
      ["9", "DW", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "-1.005e+05", "-1.005e+05"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取Z方向荷载汇总表 ──────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Load_Z",
        "TABLE_TYPE": "LOAD_SUMMARY_Z"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Load_Z", {})
for row in table.get("DATA", []):
    print(f"  荷载工况 {row[1]}: Sum={row[-1]}")
```

---

## 5. Material Table

> **功能：** 提取材料特性表（弹性模量·泊松比·热膨胀系数·密度·质量密度等）。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "MaterialTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · `"MATERIAL"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "MATERIAL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Material_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "ID", "Name", "Type", "Standard", "Code", "DB", "UseMassDensity", "Elasticity", "Poisson", "Thermal", "Density", "MassDensity", "Standard2", "Code2", "DB2", "Elasticity2", "Poisson2", "Thermal2", "Density2", "MassDensity2", "PlasticMatl.", "Sp.Heat", "HeatCo.", "MaterialType", "ShearMod._xy", "Elasticity_y", "Thermal_y", "ShearMod._xz", "Poisson_xz", "Elasticity_z", "Thermal_z", "ShearMod._yz", "Poisson_yz"],
    "DATA": [
      ["1", "1", "st", "Concrete", "KSCE-LSD15(RC)", "", "C45", "O", "3.1185e+07", "0.18", "1.0000e-05", "2.4517e+01", "2.5000e+00", "", "", "", "", "", "", "", "", "None", "0.0000", "0.0000", "Isotropic", "0.0000", "0.0000", "0.0000", "0.0000", "0", "0.0000", "0.0000", "0.0000", "0"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取材料特性表 ────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Materials",
        "TABLE_TYPE": "MATERIAL"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Materials", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    mat = dict(zip(head, row))
    print(f"  [{mat['ID']}] {mat['Name']} ({mat['Type']}) E={mat['Elasticity']}")
```

---

## 6. Section Table

> **功能：** 提取截面特性表（面积·剪切面积·惯性矩·截面模量·周长等）。用 `TABLE_TYPE` 选择截面种类。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "SectionTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型（下列10种之一） | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

**`TABLE_TYPE` 值列表**

| 值 | 说明 |
|----|------|
| `"SECTIONALL"` | 全部截面 |
| `"SECTIONCOMBINED"` | Combined 截面 |
| `"SECTIONCOMPOSITE"` | Composite 截面 |
| `"SECTIONCONSTRUCTION"` | Construction 截面 |
| `"SECTIONDB/USER"` | DB/User 截面 |
| `"SECTIONPSC"` | PSC 截面 |
| `"SECTIONSRC"` | SRC 截面 |
| `"SECTIONSTEELGIRDER"` | Steel Girder 截面 |
| `"SECTIONTAPERED"` | Tapered（变截面） |
| `"SECTIONVALUE"` | Value 截面 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "SECTIONALL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Section_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "ID", "Type", "Shape", "Name", "Area", "Asy", "Asz", "Ixx", "Iyy", "Izz", "Cyp", "Cym", "Czp", "Czm", "Qyb", "Qzb", "Peri.(Out)", "Peri.(In)"],
    "DATA": [
      ["1", "1", "DB/User", "L", "Angle_DB", "0.0002", "0.0001", "0.0001", "0.0000", "0.0000", "0.0000", "0.0216", "0.0084", "0.0086", "0.0214", "0.0002", "0.0002", "0.1200", "0.0000"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取全部截面特性表 ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Sections",
        "TABLE_TYPE": "SECTIONALL"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Sections", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    sect = dict(zip(head, row))
    print(f"  [{sect['ID']}] {sect['Name']} ({sect['Shape']}) Area={sect['Area']}")
```

---

## 7. Restraint Supports Table

> **功能：** 提取支座约束条件表（Dx/Dy/Dz/Rx/Ry/Rz/Rw 约束情况、边界组）。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "SupportsTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · `"SUPPORTS"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "Example",
    "TABLE_TYPE": "SUPPORTS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Supports_Output.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz", "Rw", "Group"],
    "DATA": [
      ["1", "2", "0", "0", "1", "0", "0", "0", "0", "Default"],
      ["2", "7", "1", "0", "1", "0", "0", "0", "0", "Default"],
      ["3", "9", "1", "0", "1", "0", "0", "0", "0", "Default"]
    ]
  }
}
```

> **参考：** 在 `Dx`~`Rw` 值中，`1` 表示约束（Fixed），`0` 表示自由（Free）。

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取支座约束条件表 ───────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Supports",
        "TABLE_TYPE": "SUPPORTS"
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Supports", {})
for row in table.get("DATA", []):
    node, dx, dy, dz = row[1], row[2], row[3], row[4]
    print(f"  Node {node}: Dx={dx} Dy={dy} Dz={dz}")
```

---

## 8. Story Mass Summary Table

> **功能：** 提取各楼层的质量汇总。可选 `STORY_MASS`（方向叠加）或 `STORY_MASS_X/Y/Z`（按方向），并可用 `UNIT`·`STYLES`·`COMPONENTS` 控制单位·格式·显示列。

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · `"STORY_MASS"` / `"STORY_MASS_X"` / `"STORY_MASS_Y"` / `"STORY_MASS_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 力单位 | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 长度单位 | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 热单位 | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 温度单位 | `UNIT.TEMP` | String | — | Optional |
| 5 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 数字格式 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 小数位数（0~15） | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 结果表显示列 | `"COMPONENTS"` | Array [String] | All | Optional |

### Request / Response JSON

**POST Request Body — STORY_MASS（方向叠加）**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Mass",
    "TABLE_TYPE": "STORY_MASS",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Story", "Level", "X-DIR", "Y-DIR", "Rotational Mass", "X-Coord", "Y-Coord"]
  }
}
```

**POST Response Body — STORY_MASS**

```json
{
  "Story Mass": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Story", "Level", "X-DIR", "Y-DIR", "Rotational Mass", "X-Coord", "Y-Coord"],
    "DATA": [
      ["1", "Roof", "9.500", "1056.318", "1056.318", "221794.676", "17.930", "14.172"],
      ["2", "2F", "5.500", "1076.719", "1076.719", "226809.725", "18.021", "14.187"],
      ["3", "1F", "0.000", "0.000", "0.000", "0.000", "0.000", "0.000"],
      ["4", "", "Total", "11322.131", "11322.131", "", "", ""]
    ]
  }
}
```

**POST Request Body — STORY_MASS_X（按方向）**

```json
{
  "Argument": {
    "TABLE_NAME": "Story Mass X",
    "TABLE_TYPE": "STORY_MASS_X",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Story", "Level", "NodalMass", "LoadToMass", "DiaphragmMass", "StructureMass", "Sum"]
  }
}
```

**POST Response Body — STORY_MASS_X**

```json
{
  "Story Mass X": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Story", "Level", "NodalMass", "LoadToMass", "DiaphragmMass", "StructureMass", "Sum"],
    "DATA": [
      ["1", "Roof", "9.500", "0.000", "541.887", "0.000", "514.431", "1056.318"],
      ["2", "2F", "5.500", "0.000", "541.887", "0.000", "534.832", "1076.719"],
      ["3", "1F", "0.000", "0.000", "0.000", "0.000", "147.850", "147.850"],
      ["4", "", "Total", "0.000", "6047.119", "0.000", "5422.862", "11469.981"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取楼层质量汇总（方向叠加） ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Story Mass",
        "TABLE_TYPE": "STORY_MASS",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "COMPONENTS": ["Story", "Level", "X-DIR", "Y-DIR", "Rotational Mass", "X-Coord", "Y-Coord"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Story Mass", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['Story'] or d['Level']}: X-DIR={d.get('X-DIR')}, Y-DIR={d.get('Y-DIR')}")
```

---

## 9. Story Load Summary Table

> **功能：** 按 X/Y/Z 方向提取各楼层的荷载汇总（集中·梁·楼面·压力·自重·合计）。
>
> ⚠️ **2026-08-25 复核后更正：** 先前版本（2026-08-05 记载）将原文与第8项 Story Mass Summary
> Table 混淆，误记了 `UNIT`·`STYLES`·`COMPONENTS`·`LOAD_CASE_NAMES` 参数与 `TABLE_TYPE` 值
> `"STORY_LOAD_X/Y/Z"`。直接重新抓取原文（article id `49514148775705`，`updated_at`
> 2026-08-05T07:40:56Z — 与本次复核时点为同一版本）进行比对后，确认
> Specifications 表中只有 `TABLE_NAME`·`TABLE_TYPE`·`EXPORT_PATH` 3 个参数，且 Request
> 示例3种（X/Y/Z）的 `TABLE_TYPE` 值均为 `"STORY_LOAD_SUMMARY_X/Y/Z"`，故已全面更正以下内容。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "StoryLoadSummaryTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 表名称 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · X方向：`"STORY_LOAD_SUMMARY_X"` / Y方向：`"STORY_LOAD_SUMMARY_Y"` / Z方向：`"STORY_LOAD_SUMMARY_Z"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径 | `"EXPORT_PATH"` | String | — | Optional |

### Request / Response JSON

**POST Request Body（Z 方向）**

```json
{
  "Argument": {
    "TABLE_NAME": "StoryLoadZ",
    "TABLE_TYPE": "STORY_LOAD_SUMMARY_Z",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\story_load_summary_z_Out.JSON"
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Load", "Story", "Level", "Concent", "Beam", "Floor", "Pressure", "SelfWeight", "Sum"],
    "DATA": [
      ["1", "DL", "Roof", "9.500", "0.000", "-248.400", "-5730.624", "0.000", "-5044.509", "-10358.253"],
      ["2", "DL", "2F", "5.000", "0.000", "-248.400", "-5065.344", "0.000", "-5244.565", "-10558.309"],
      ["3", "DL", "1F", "0.000", "0.000", "0.000", "0.000", "0.000", "-1449.815", "-1449.815"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：分别提取 X/Y/Z 三个方向的楼层荷载汇总表 ──────────────
for direction in ["X", "Y", "Z"]:
    payload = {
        "Argument": {
            "TABLE_NAME": f"StoryLoad_{direction}",
            "TABLE_TYPE": f"STORY_LOAD_SUMMARY_{direction}",
            "EXPORT_PATH": f"C:\\\\MIDAS\\\\Result\\\\story_load_summary_{direction.lower()}_Out.JSON"
        }
    }
    resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
    table = resp.json().get(f"StoryLoad_{direction}", {})
    print(f"{direction}方向：{len(table.get('DATA', []))} 行")
```

---

## 10. Story Weight Table

> **功能：** 按单元类型（桁架·梁·膜单元·板·墙·实体·合计）提取各楼层的重量。
>
> ⚠️ **2026-08-05 原文更新已反映：** 额外暴露了 `UNIT`·`STYLES`·`COMPONENTS` 参数（结构与第8项 Story Mass
> Summary Table 相同）。`TABLE_TYPE` 值（`"STORYWEIGHT"`）本身
> 未变更。

### JSON Schema

```json
{
  "TABLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "StoryWeightTable",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TABLE_NAME": { "type": "string" },
          "TABLE_TYPE": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "UNIT": { "type": "object" },
          "STYLES": { "type": "object" },
          "COMPONENTS": { "type": "array" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 表名称（输出标题） | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表类型 · `"STORYWEIGHT"` | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表保存路径（JSON） | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 力单位 | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 长度单位 | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 热单位 | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 温度单位 | `UNIT.TEMP` | String | — | Optional |
| 5 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 数字格式 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 小数位数（0~15） | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 结果表显示列 | `"COMPONENTS"` | Array [String] | All | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "STORYWEIGHT",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": ["Story", "Level", "Truss", "Beam", "Membrane", "Plate", "Wall", "Solid", "Sum"]
  }
}
```

**POST Response Body**

```json
{
  "Example": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": ["Index", "Story", "Level", "Truss", "Beam", "Membrane", "Plate", "Wall", "Solid", "Sum"],
    "DATA": [
      ["1", "Roof", "5.600", "0.000", "56.912", "0.000", "0.000", "104.321", "0.000", "161.233"],
      ["2", "2F", "2.800", "0.000", "70.257", "0.000", "0.000", "208.642", "0.000", "278.898"],
      ["3", "1F", "0.000", "0.000", "13.345", "0.000", "0.000", "104.321", "0.000", "117.666"]
    ]
  }
}
```

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST：提取楼层重量表 ──────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_TYPE": "STORYWEIGHT",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "COMPONENTS": ["Story", "Level", "Truss", "Beam", "Membrane", "Plate", "Wall", "Solid", "Sum"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Example", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  {d['Story']} (Lv.{d['Level']}): 合计重量 = {d['Sum']}")
```

---

## End-to-End Workflow

以下为执行分析后批量提取前处理汇总表的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_table(table_type, name, extra=None):
    """提取前处理表的通用函数"""
    arg = {"TABLE_NAME": name, "TABLE_TYPE": table_type}
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    return resp.json().get(name, {})

# ── STEP 1：确认材料·截面 ─────────────────────────────────────────
mat = get_table("MATERIAL", "Mat")
print(f"STEP1 材料 {len(mat.get('DATA', []))}种")
sect = get_table("SECTIONALL", "Sect")
print(f"      截面 {len(sect.get('DATA', []))}种")

# ── STEP 2：确认支座约束条件 ────────────────────────────────────
sup = get_table("SUPPORTS", "Sup")
print(f"STEP2 支座 {len(sup.get('DATA', []))}个")

# ── STEP 3：质量·荷载汇总（X/Y/Z） ─────────────────────────────────
for d in ["X", "Y", "Z"]:
    m = get_table(f"MASS_SUMMARY_{d}", f"Mass{d}")
    l = get_table(f"LOAD_SUMMARY_{d}", f"Load{d}")
    print(f"STEP3 {d}方向：质量 {len(m.get('DATA', []))}行，荷载 {len(l.get('DATA', []))}行")

# ── STEP 4：各楼层汇总（质量·荷载·重量） ─────────────────────────────
story_mass = get_table("STORY_MASS", "StoryMass",
                        extra={"UNIT": {"FORCE": "KN", "DIST": "M"},
                               "STYLES": {"FORMAT": "Fixed", "PLACE": 3}})
print(f"STEP4 楼层质量 {len(story_mass.get('DATA', []))}行")
story_weight = get_table("STORYWEIGHT", "StoryWeight")
print(f"      楼层重量 {len(story_weight.get('DATA', []))}行")

# ── STEP 5：单元重量（全部） ───────────────────────────────────────
elem_w = get_table("ELEMENTWEIGHT", "ElemW")
print(f"STEP5 单元重量 {len(elem_w.get('DATA', []))}行")
```
