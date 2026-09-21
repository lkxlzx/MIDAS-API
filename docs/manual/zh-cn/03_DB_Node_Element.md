# 03 DB — Node / Element

> **Source**: [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **Sync date**: 2026-06-29  
> **Endpoints covered**: `/db/NODE`, `/db/ELEM`, `/db/SKEW`, `/db/MADO`, `/db/SBDO`, `/db/DOEL`

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../03_DB_Node_Element.md) · **原文同步日期：** 2026-06-29  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## Table of Contents

| No. | Endpoint | 功能 | Methods |
|-----|----------|------|---------|
| 1 | [`/db/NODE`](#1-dbnode) | Node | POST, GET, PUT, DELETE |
| 2 | [`/db/ELEM`](#2-dbelem) | Element | POST, GET, PUT, DELETE |
| 3 | [`/db/SKEW`](#3-dbskew) | Node Local Axis | POST, GET, PUT, DELETE |
| 4 | [`/db/MADO`](#4-dbmado) | Define Domain | POST, GET, PUT, DELETE |
| 5 | [`/db/SBDO`](#5-dbsbdo) | Define Sub-Domain | POST, GET, PUT, DELETE |
| 6 | [`/db/DOEL`](#6-dbdoel) | Domain-Element | POST, GET, PUT, DELETE |

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

## 1. `/db/NODE`

> **Node** — 定义节点（Node）的全局坐标系（Global）坐标。

- **URL**: `{base url}/db/NODE`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Node ↗](https://support.midasuser.com/hc/en-us/articles/35806845654169)

### JSON Schema

```json
{
  "NODE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "X": { "description": "GLOBAL X-POSITION", "type": "number" },
      "Y": { "description": "GLOBAL Y-POSITION", "type": "number" },
      "Z": { "description": "GLOBAL Z-POSITION", "type": "number" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Coordinates - x | `"X"` | Number | 0 | Optional |
| 2 | Coordinates - y | `"Y"` | Number | 0 | Optional |
| 3 | Coordinates - z | `"Z"` | Number | 0 | Optional |

### Request Body (Assign)

```json
{
  "Assign": {
    "1": { "X": -1, "Y": -1, "Z": -1 },
    "2": { "X": -2, "Y": -2, "Z": -2 },
    "3": { "X": -3, "Y": -3, "Z": -3 }
  }
}
```

### Python 示例

```python
# --- GET: 查询全部节点 ---
result = midas_api("GET", "/db/NODE")
nodes = result.get("NODE", {})
print(f"节点总数: {len(nodes)}")

# --- POST: 创建节点 ---
# 以节点 ID 为键、坐标为值
node_data = {
    "Assign": {
        "1": {"X": 0.0, "Y": 0.0, "Z": 0.0},
        "2": {"X": 6.0, "Y": 0.0, "Z": 0.0},
        "3": {"X": 6.0, "Y": 0.0, "Z": 4.0},
        "4": {"X": 0.0, "Y": 0.0, "Z": 4.0},
    }
}
midas_api("POST", "/db/NODE", node_data)

# --- PUT: 修改节点 ---
update_data = {
    "Assign": {
        "2": {"X": 7.0, "Y": 0.0, "Z": 0.0}  # 变更 2 号节点的 X 坐标
    }
}
midas_api("PUT", "/db/NODE", update_data)

# --- DELETE: 删除节点 ---
delete_data = {"Assign": {"4": None}}
midas_api("DELETE", "/db/NODE", delete_data)
```

### 进阶示例 — 自动生成网格节点

```python
def create_grid_nodes(nx, ny, nz, dx, dy, dz, start_id=1):
    """
    生成三维网格节点
    
    Args:
        nx, ny, nz: X、Y、Z 方向的分割数（节点数 = (nx+1)*(ny+1)*(nz+1)）
        dx, dy, dz: X、Y、Z 方向的间距
        start_id: 起始节点编号
    
    Returns:
        Assign dict for /db/NODE
    """
    assign = {}
    node_id = start_id
    for k in range(nz + 1):
        for j in range(ny + 1):
            for i in range(nx + 1):
                assign[str(node_id)] = {
                    "X": i * dx,
                    "Y": j * dy,
                    "Z": k * dz
                }
                node_id += 1
    return {"Assign": assign}

# 示例：3跨 × 1跨 × 4层（6m 跨径，6m 跨径，3m 层高）
node_body = create_grid_nodes(nx=3, ny=1, nz=4, dx=6.0, dy=6.0, dz=3.0)
print(f"生成的节点数: {len(node_body['Assign'])}")  # (3+1)*(1+1)*(4+1) = 40
midas_api("POST", "/db/NODE", node_body)
```

---

## 2. `/db/ELEM`

> **Element** — 定义单元（构件）。支持 BEAM、TRUSS、TENSTR、COMPTR、PLATE、WALL、PLSTRS、PLSTRN、AXISYM、SOLID 等 10 种单元类型。

- **URL**: `{base url}/db/ELEM`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Element ↗](https://support.midasuser.com/hc/en-us/articles/35806934300825)

### JSON Schema

```json
{
  "ELEM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE":    { "description": "ELEMENT TYPE",            "type": "string" },
      "MATL":    { "description": "MATERIAL NUM",            "type": "integer" },
      "SECT":    { "description": "SECTION NUM",             "type": "integer" },
      "NODE":    { "description": "NODE NUM",                "type": "array", "items": { "type": "integer", "maxItems": 8 } },
      "ANGLE":   { "description": "ELEMENT ANGLE",          "type": "number" },
      "STYPE":   { "description": "ELEMENT SUBTYPE",        "type": "integer" },
      "TENS":    { "description": "TENS FORCE",              "type": "number" },
      "T_LIMIT": { "description": "TENS LIMIT",             "type": "number" },
      "T_bLMT":  { "description": "USE TENS LIMIT?",        "type": "boolean" },
      "NON_LEN": { "description": "NON LINEAR LENGTH",      "type": "number" },
      "CABLE":   { "description": "CABLE OPTION",           "type": "integer" },
      "C_RAT":   { "description": "CABLE LENGTH RATIO",     "type": "number" },
      "WALL":    { "description": "WALL ID",                "type": "integer" },
      "W_CON":   { "description": "CONNECTED NODE NUM",     "type": "integer" },
      "W_TYPE":  { "description": "WALL TYPE",              "type": "integer" },
      "LCAXIS":  { "description": "LOCAL AXIS",             "type": "integer" }
    }
  }
}
```

### Specifications

#### 公共键 (Common Keys) + Solid

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Element Type ¹⁾ | `"TYPE"` | String | `"BEAM"` | Optional |
| 2 | Material No. | `"MATL"` | Integer | - | **Required** |
| 3 | Section / Thickness No. | `"SECT"` | Integer | - | **Required** |
| 4 | Node No. ²⁾ | `"NODE"` | Array[Integer] | - | **Required** |

#### Beam, Truss, Plane Strain, Axisymmetric

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |

#### Tension only — Truss (STYPE: 1)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Truss: 1 | `"STYPE"` | Integer | - | **Required** |
| 7 | Allowable Compression (Negative Value Only) | `"TENS"` | Number | 0 | Optional |
| 8 | Tension Limit Value (Positive Value Only) | `"T_LIMIT"` | Number | 0 | Optional |
| 9 | Tension Limit | `"T_bLMT"` | Boolean | false | Optional |

#### Tension only — Hook (STYPE: 2)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Hook: 2 | `"STYPE"` | Integer | - | **Required** |
| 7 | Hook Length | `"NON_LEN"` | Number | 0 | Optional |

#### Tension only — Cable (STYPE: 3)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Cable: 3 | `"STYPE"` | Integer | - | **Required** |
| 7 | Cable Type • Pretension: 1 • Horizontal: 2 • Lu: 3 | `"CABLE"` | Integer | - | **Required** |
| 8 | Pretension / Horizontal | `"TENS"` | Number | 0 | Optional |
| 9 | Lu (Range: 0.5~1.5) | `"NON_LEN"` | Number | - | **Required** |

#### Compression only — Truss (STYPE: 1)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Truss: 1 | `"STYPE"` | Integer | - | **Required** |
| 7 | Allowable Tension (Positive Value Only) | `"TENS"` | Number | 0 | Optional |
| 8 | Compression Limit | `"T_bLMT"` | Boolean | false | Optional |
| 9 | Compression Limit Value (Negative Value Only) | `"T_LIMIT"` | Number | - | Optional |

#### Compression only — Gap (STYPE: 2)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Gap: 2 | `"STYPE"` | Integer | - | **Required** |
| 7 | Gap | `"NON_LEN"` | Number | 0 | Optional |

#### Wall

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Membrane: 1 • Plate: 2 | `"STYPE"` | Integer | - | **Required** |
| 7 | Wall ID | `"WALL"` | Integer | - | **Required** |
| 8 | Orientation • Beta Angle: 0 • Ref Point: 1 • Ref Vector: 2 | `"W_CON"` | Integer | - | **Required** |
| 9 | Wall Type • Plate base: 0 • CRB-Pin: 1 • CRB-Fixed: 2 | `"W_TYPE"` | Integer | 0 | Optional |

#### Plate

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Thick: 1 • Thin: 2 • Thick+Drilling DOF: 3 • Thin+Drilling DOF: 4 | `"STYPE"` | Integer | - | **Required** |

#### Plane Stress

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Beta Angle | `"ANGLE"` | Number | 0 | Optional |
| 6 | Element Subtype • Drilling DOF Inactive: 1 • Drilling DOF Active: 2 | `"STYPE"` | Integer | - | **Required** |

### 单元类型代码表 ¹⁾

| No. | Element Type | `"TYPE"` |
|-----|--------------|----------|
| 1 | General Beam / Tapered Beam | `"BEAM"` |
| 2 | Truss | `"TRUSS"` |
| 3 | Tension only / Hook / Cable | `"TENSTR"` |
| 4 | Compression only / Gap | `"COMPTR"` |
| 5 | Plate | `"PLATE"` |
| 6 | Wall | `"WALL"` |
| 7 | Plane stress | `"PLSTRS"` |
| 8 | Plane strain | `"PLSTRN"` |
| 9 | Axisymmetric | `"AXISYM"` |
| 10 | Solid | `"SOLID"` |

### 节点数小结 ²⁾

| Element Type | Min Nodes | Max Nodes | Notes |
|--------------|-----------|-----------|-------|
| BEAM, TRUSS, TENSTR, COMPTR | 2 | 2 | - |
| PLATE, PLSTRS, PLSTRN, AXISYM | 3 | 4 | Triangle or Quad |
| WALL | 4 | 4 | Quad only |
| SOLID | 4 | 8 | Tet(4), Wedge(6), Hex(8) |

### Request Body 示例

#### BEAM

```json
{
  "Assign": {
    "198": {
      "TYPE": "BEAM",
      "MATL": 1,
      "SECT": 1,
      "NODE": [30, 74],
      "ANGLE": 0
    }
  }
}
```

#### TRUSS

```json
{
  "Assign": {
    "13": {
      "TYPE": "TRUSS",
      "MATL": 1,
      "SECT": 1,
      "NODE": [24, 25],
      "ANGLE": 0
    }
  }
}
```

#### TENSTR (Cable)

```json
{
  "Assign": {
    "6": {
      "TYPE": "TENSTR",
      "MATL": 1,
      "SECT": 1,
      "NODE": [11, 12],
      "ANGLE": 0,
      "STYPE": 3,
      "TENS": 0.5,
      "CABLE": 1
    }
  }
}
```

#### COMPTR (Truss)

```json
{
  "Assign": {
    "22": {
      "TYPE": "COMPTR",
      "MATL": 1,
      "SECT": 1,
      "NODE": [50, 51],
      "ANGLE": 0,
      "STYPE": 1,
      "TENS": 27,
      "T_LIMIT": -15,
      "T_bLMT": true
    }
  }
}
```

#### PLATE (Quad, Thick)

```json
{
  "Assign": {
    "30": {
      "TYPE": "PLATE",
      "MATL": 1,
      "SECT": 1,
      "NODE": [56, 69, 70, 57],
      "ANGLE": 0,
      "STYPE": 1
    }
  }
}
```

#### WALL

```json
{
  "Assign": {
    "1": {
      "TYPE": "WALL",
      "MATL": 1,
      "SECT": 1,
      "NODE": [1, 2, 4, 3],
      "STYPE": 1,
      "WALL": 1,
      "W_CON": 0,
      "W_TYPE": 0
    }
  }
}
```

#### SOLID (Hexahedral, 8-node)

```json
{
  "Assign": {
    "42": {
      "TYPE": "SOLID",
      "MATL": 1,
      "SECT": 0,
      "NODE": [27, 6, 7, 28, 113, 107, 108, 114]
    }
  }
}
```

### Python 示例

```python
# --- GET: 查询全部单元 ---
result = midas_api("GET", "/db/ELEM")
elems = result.get("ELEM", {})
print(f"单元总数: {len(elems)}")

# 按单元类型统计
from collections import Counter
type_count = Counter(e["TYPE"] for e in elems.values())
print(dict(type_count))

# --- POST: 创建梁(BEAM)单元 ---
beam_data = {
    "Assign": {
        "1": {"TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0},
        "2": {"TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [3, 4], "ANGLE": 0},
    }
}
midas_api("POST", "/db/ELEM", beam_data)

# --- DELETE: 删除特定单元 ---
delete_data = {"Assign": {"5": None}}
midas_api("DELETE", "/db/ELEM", delete_data)
```

### 进阶示例 — 自动生成刚架

```python
def create_moment_frame(
    n_bays_x: int,
    n_stories: int,
    bay_width: float,
    story_height: float,
    col_matl: int,
    col_sect: int,
    beam_matl: int,
    beam_sect: int,
    node_start_id: int = 1,
    elem_start_id: int = 1
):
    """
    自动生成二维刚架 (Moment Frame) 的节点与梁/柱单元
    
    Args:
        n_bays_x: X 方向的跨径数
        n_stories: 层数
        bay_width: 跨径宽度 (m)
        story_height: 层高 (m)
        col_matl/col_sect: 柱的材料/截面编号
        beam_matl/beam_sect: 梁的材料/截面编号
    
    Returns:
        (node_body, elem_body) tuple for /db/NODE and /db/ELEM
    """
    n_cols = n_bays_x + 1  # 柱数 (X 方向)
    
    # 生成节点 (Y=0 平面)
    nodes = {}
    nid = node_start_id
    node_map = {}  # (i_col, i_story) -> node_id
    for i_story in range(n_stories + 1):  # 0 层 ~ n_stories 层
        for i_col in range(n_cols):
            nodes[str(nid)] = {
                "X": i_col * bay_width,
                "Y": 0.0,
                "Z": i_story * story_height
            }
            node_map[(i_col, i_story)] = nid
            nid += 1
    
    # 生成单元
    elems = {}
    eid = elem_start_id
    
    # 柱 (Column)：各层的竖向构件
    for i_story in range(n_stories):
        for i_col in range(n_cols):
            n_bot = node_map[(i_col, i_story)]
            n_top = node_map[(i_col, i_story + 1)]
            elems[str(eid)] = {
                "TYPE": "BEAM",
                "MATL": col_matl,
                "SECT": col_sect,
                "NODE": [n_bot, n_top],
                "ANGLE": 0
            }
            eid += 1
    
    # 梁 (Beam)：各层的水平构件
    for i_story in range(1, n_stories + 1):  # 1 层 ~ n_stories 层
        for i_bay in range(n_bays_x):
            n_left = node_map[(i_bay, i_story)]
            n_right = node_map[(i_bay + 1, i_story)]
            elems[str(eid)] = {
                "TYPE": "BEAM",
                "MATL": beam_matl,
                "SECT": beam_sect,
                "NODE": [n_left, n_right],
                "ANGLE": 0
            }
            eid += 1
    
    node_body = {"Assign": nodes}
    elem_body = {"Assign": elems}
    
    n_nodes = len(nodes)
    n_elems = len(elems)
    n_cols_total = n_cols * n_stories
    n_beams_total = n_bays_x * n_stories
    print(f"生成: 节点 {n_nodes}个, 单元 {n_elems}个 (柱 {n_cols_total}个, 梁 {n_beams_total}个)")
    
    return node_body, elem_body


# 使用示例: 3跨 × 5层刚架 (跨径 6m, 层高 3.5m)
node_body, elem_body = create_moment_frame(
    n_bays_x=3, n_stories=5,
    bay_width=6.0, story_height=3.5,
    col_matl=1, col_sect=1,
    beam_matl=1, beam_sect=2
)

midas_api("POST", "/db/NODE", node_body)
midas_api("POST", "/db/ELEM", elem_body)
```

---

## 3. `/db/SKEW`

> **Node Local Axis** — 定义节点局部坐标系。支持 4 种输入方法（Angle、3 Points、Vector、Line Vector）。

- **URL**: `{base url}/db/SKEW`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Node Local Axis ↗](https://support.midasuser.com/hc/en-us/articles/35807178748569)

### JSON Schema

```json
{
  "SKEW": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "iMETHOD": { "description": "Input method",       "type": "integer" },
      "ANGLE_X":  { "description": "Angle x",           "type": "number" },
      "ANGLE_Y":  { "description": "Angle y",           "type": "number" },
      "ANGLE_Z":  { "description": "Angle z",           "type": "number" },
      "P0X":      { "description": "Point Coordinate x", "type": "number" },
      "P0Y":      { "description": "Point Coordinate y", "type": "number" },
      "P0Z":      { "description": "Point Coordinate z", "type": "number" },
      "P1X":      { "description": "Point Coordinate x", "type": "number" },
      "P1Y":      { "description": "Point Coordinate y", "type": "number" },
      "P1Z":      { "description": "Point Coordinate z", "type": "number" },
      "P2X":      { "description": "Point Coordinate x", "type": "number" },
      "P2Y":      { "description": "Point Coordinate y", "type": "number" },
      "P2Z":      { "description": "Point Coordinate z", "type": "number" },
      "V1X":      { "description": "Direction Vector x", "type": "number" },
      "V1Y":      { "description": "Direction Vector y", "type": "number" },
      "V1Z":      { "description": "Direction Vector z", "type": "number" },
      "V2X":      { "description": "Direction Vector x", "type": "number" },
      "V2Y":      { "description": "Direction Vector y", "type": "number" },
      "V2Z":      { "description": "Direction Vector z", "type": "number" },
      "LV0X":     { "description": "Direction Vector x", "type": "number" },
      "LV0Y":     { "description": "Direction Vector y", "type": "number" },
      "LV0Z":     { "description": "Direction Vector z", "type": "number" },
      "LV1X":     { "description": "Direction Vector x", "type": "number" },
      "LV1Y":     { "description": "Direction Vector y", "type": "number" },
      "LV1Z":     { "description": "Direction Vector z", "type": "number" },
      "LV2X":     { "description": "Direction Vector x", "type": "number" },
      "LV2Y":     { "description": "Direction Vector y", "type": "number" },
      "LV2Z":     { "description": "Direction Vector z", "type": "number" },
      "REFTYPE":  { "description": "Reference Type",    "type": "integer" },
      "G_DIR":    { "description": "Global Direction",  "type": "integer" },
      "L_DIR":    { "description": "Local Direction",   "type": "integer" }
    }
  }
}
```

### Specifications

> ⚠️ 若省略 `iMETHOD`，按原文其默认值为 `1`（Angle）（2026-08-25 确认，文章 id
> `35807178748569`）。下方 4 个表按各方式分列整理，但实际上是由 `iMETHOD` 这一个
> 字段来选择 4 种方式。

#### iMETHOD = 1 (Angle)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • Angle: 1 | `"iMETHOD"` | Integer | - | Optional |
| 2 | About x | `"ANGLE_X"` | Number | 0 | Optional |
| 3 | About y | `"ANGLE_Y"` | Number | 0 | Optional |
| 4 | About z | `"ANGLE_Z"` | Number | 0 | Optional |

#### iMETHOD = 2 (3 Points)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • 3 Points: 2 | `"iMETHOD"` | Integer | - | Optional |
| 2~4 | P0 Coordinate (x, y, z) | `"P0X"` `"P0Y"` `"P0Z"` | Number | 0 | Optional |
| 5~7 | P1 Coordinate (x, y, z) | `"P1X"` `"P1Y"` `"P1Z"` | Number | 0 | Optional |
| 8~10 | P2 Coordinate (x, y, z) | `"P2X"` `"P2Y"` `"P2Z"` | Number | 0 | Optional |

#### iMETHOD = 3 (Vector)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • Vector: 3 | `"iMETHOD"` | Integer | - | Optional |
| 2~4 | Direction Vector V1 (x, y, z) | `"V1X"` `"V1Y"` `"V1Z"` | Number | 0 | Optional |
| 5~7 | Direction Vector V2 (x, y, z) | `"V2X"` `"V2Y"` `"V2Z"` | Number | 0 | Optional |

#### iMETHOD = 4 (Line Vector)

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Method • Line Vector: 4 | `"iMETHOD"` | Integer | - | Optional |
| 2~4 | Direction Vector V0 (x, y, z) | `"LV0X"` `"LV0Y"` `"LV0Z"` | Number | 0 | Optional |
| 5~7 | Direction Vector V1 (x, y, z) | `"LV1X"` `"LV1Y"` `"LV1Z"` | Number | 0 | Optional |
| 8~10 | Direction Vector V2 (x, y, z) | `"LV2X"` `"LV2Y"` `"LV2Z"` | Number | 0 | Optional |
| 11 | Reference Type • Ref. Point: 1 (P0, P1 required) • Global Direction: 2 (P0 required) | `"REFTYPE"` | Integer | - | **Required** |
| 12 | Global Direction • Global X: 0 • Global Y: 1 • Global Z: 2 | `"G_DIR"` | Integer | - | **Required** |
| 13 | Local Direction • Local x: 0 • Local y: 1 • Local z: 2 | `"L_DIR"` | Integer | - | **Required** |

### Request Body 示例

#### Method 1 — Angle

```json
{
  "Assign": {
    "1": {
      "iMETHOD": 1,
      "ANGLE_X": 45,
      "ANGLE_Y": 0,
      "ANGLE_Z": 90
    }
  }
}
```

#### Method 2 — 3 Points

```json
{
  "Assign": {
    "2": {
      "iMETHOD": 2,
      "P0X": 130, "P0Y": 3.35, "P0Z": 0,
      "P1X": 127, "P1Y": 3.35, "P1Z": 0,
      "P2X": 127, "P2Y": -3.35, "P2Z": 0
    }
  }
}
```

#### Method 3 — Vector

```json
{
  "Assign": {
    "3": {
      "iMETHOD": 3,
      "V1X": 0, "V1Y": -2.95, "V1Z": 0,
      "V2X": -3, "V2Y": 0, "V2Z": 0
    }
  }
}
```

### Python 示例

```python
# 设置节点局部坐标系 (Angle 方式)
# 使用示例：为倾斜的桥墩基础节点施加局部坐标系
skew_data = {
    "Assign": {
        "5": {
            "iMETHOD": 1,
            "ANGLE_X": 0,
            "ANGLE_Y": 0,
            "ANGLE_Z": 30  # 以 Z 轴为基准旋转 30°
        }
    }
}
midas_api("POST", "/db/SKEW", skew_data)

# 查询并确认
result = midas_api("GET", "/db/SKEW")
print(f"已定义的局部坐标系数: {len(result.get('SKEW', {}))}")
```

---

## 4. `/db/MADO`

> **Define Domain** — 定义网格域（Main Domain）。为 Plane Stress、Plate、Plane Strain、Axisymmetric 单元类型设置域。

- **URL**: `{base url}/db/MADO`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Define Domain ↗](https://support.midasuser.com/hc/en-us/articles/35807228332825)

### JSON Schema

```json
{
  "MADO": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "NAME":     { "description": "Domain Name",      "type": "string" },
      "TYPE":     { "description": "Element Type",     "type": "integer" },
      "MATL":     { "description": "Element Material", "type": "integer" },
      "PROP":     { "description": "Element Property", "type": "integer" },
      "SUB_TYPE": { "description": "Sub Type",         "type": "integer" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Domain Name | `"NAME"` | String | - | **Required** |
| 2 | Element Type • Plane Stress: 3 • Plate: 4 • Plane Strain: 6 • Axisymmetric: 7 | `"TYPE"` | Integer | - | **Required** |
| 3 | Material ID | `"MATL"` | Integer | - | **Required** |
| 4 | Element Property | `"PROP"` | Integer | - | **Required** |
| 5 | Sub Type | `"SUB_TYPE"` | Integer | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "1": {
      "NAME": "DM1",
      "TYPE": 4,
      "MATL": 0,
      "PROP": 0,
      "SUB_TYPE": 2
    }
  }
}
```

### Python 示例

```python
# 创建 Plate 域
domain_data = {
    "Assign": {
        "1": {
            "NAME": "SLAB_DOMAIN",
            "TYPE": 4,      # Plate
            "MATL": 1,      # 材料 1
            "PROP": 1,      # 厚度属性 1
            "SUB_TYPE": 1   # 子类型
        }
    }
}
midas_api("POST", "/db/MADO", domain_data)

# 查询全部域
result = midas_api("GET", "/db/MADO")
domains = result.get("MADO", {})
for did, d in domains.items():
    print(f"Domain {did}: {d['NAME']} (TYPE={d['TYPE']})")
```

---

## 5. `/db/SBDO`

> **Define Sub-Domain** — 定义域内的子域（Sub-Domain）。设置钢筋方向、构件类型、基本钢筋配筋等。**GEN NX** 与 **CIVIL NX** 的部分参数不同。

- **URL**: `{base url}/db/SBDO`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Define Sub-Domain ↗](https://support.midasuser.com/hc/en-us/articles/35807304820761)

### JSON Schema

```json
{
  "SBDO": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "SUB_DOMAIN_NAME":  { "description": "Sub Domain Name",       "type": "string" },
      "MEMBER_TYPE":      { "description": "Member Type",           "type": "integer" },
      "V1":               { "description": "V1",                    "type": "number" },
      "V2":               { "description": "V2",                    "type": "number" },
      "DOMAIN_NAME":      { "description": "Domain Name",          "type": "string" },
      "bUseMt":           { "description": "Use Mt",               "type": "boolean" },
      "THICKNESS":        { "description": "Thickness",            "type": "number" },
      "OPT_BASIC_REBAR":  { "description": "Basic Rebar Boolean",  "type": "boolean" },
      "TOP_REBAR_NAME_X": { "description": "Top Rebar Name: X-Dir","type": "string" },
      "TOP_REBAR_SPACE_X":{ "description": "Top Rebar Space: X-Dir","type": "number" },
      "BOTTOM_REBAR_NAME_X":  { "description": "Bottom Rebar Name: X-Dir",  "type": "string" },
      "BOTTOM_REBAR_SPACE_X": { "description": "Bottom Rebar Space: X-Dir", "type": "number" },
      "TOP_REBAR_NAME_Y": { "description": "Top Rebar Name: Y-Dir","type": "string" },
      "TOP_REBAR_SPACE_Y":{ "description": "Top Rebar Space: Y-Dir","type": "number" },
      "BOTTOM_REBAR_NAME_Y":  { "description": "Bottom Rebar Name: Y-Dir",  "type": "string" },
      "BOTTOM_REBAR_SPACE_Y": { "description": "Bottom Rebar Space: Y-Dir", "type": "number" },
      "AXIS_VECTOR":      { "description": "Axis Vector",          "type": "array", "items": { "type": "number" } },
      "OPT_REBAR_MATL":   { "description": "Rebar Material Boolean","type": "boolean" },
      "REBAR_MATL_KEY":   { "description": "Rebar Material Key",   "type": "integer" },
      "REBAR_AXIS_TYPE":  { "description": "Rebar Axis Type",      "type": "integer" },
      "STR_UCS":          { "description": "UCS",                  "type": "string" },
      "MEMB_TYPE_CIVIL":  { "description": "Member Type Civil",    "type": "integer" }
    }
  }
}
```

### Specifications

#### 公共键

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Sub Domain Name | `"SUB_DOMAIN_NAME"` | String | - | **Required** |
| 2 | Rebar Dir.1 | `"V1"` | Number | - | **Required** |
| 3 | Rebar Dir.2 | `"V2"` | Number | - | **Required** |
| 4 | Domain Name | `"DOMAIN_NAME"` | String | - | **Required** |

#### CIVIL NX Only

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Member Type Civil • None: 0 • Plate Beam (1D): 1 • Plate Column (1D): 2 • Shell: 3 | `"MEMB_TYPE_CIVIL"` | Integer | - | **Required** |
| 6 | Rebar Direction • Local: 0 • UCS: 1 • Reference Axis: 2 | `"REBAR_AXIS_TYPE"` | Integer | 0 | Optional |
| 7 | UCS（Rebar Direction 为 UCS 时） | `"STR_UCS"` | String | Blank | Optional |
| 8 | Axis Vector（Rebar Direction 为 Reference Axis 时） | `"AXIS_VECTOR"` | Number | 0 | Optional |

#### GEN NX Only

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 5 | Member Type • None: 0 • Slab: 1 • Mat: 2 | `"MEMBER_TYPE"` | Integer | - | **Required** |
| 6 | Basic Rebar Option | `"OPT_BASIC_REBAR"` | Boolean | false | Optional |
| 7 | Top Rebar Name (X-Dir) | `"TOP_REBAR_NAME_X"` | String | Blank | Optional |
| 8 | Top Rebar Space (X-Dir) | `"TOP_REBAR_SPACE_X"` | Number | 0 | Optional |
| 9 | Bottom Rebar Name (X-Dir) | `"BOTTOM_REBAR_NAME_X"` | String | Blank | Optional |
| 10 | Bottom Rebar Space (X-Dir) | `"BOTTOM_REBAR_SPACE_X"` | Number | 0 | Optional |
| 11 | Top Rebar Name (Y-Dir) | `"TOP_REBAR_NAME_Y"` | String | Blank | Optional |
| 12 | Top Rebar Space (Y-Dir) | `"TOP_REBAR_SPACE_Y"` | Number | 0 | Optional |
| 13 | Bottom Rebar Name (Y-Dir) | `"BOTTOM_REBAR_NAME_Y"` | String | Blank | Optional |
| 14 | Bottom Rebar Space (Y-Dir) | `"BOTTOM_REBAR_SPACE_Y"` | Number | 0 | Optional |
| 15 | Rebar Material Option | `"OPT_REBAR_MATL"` | Boolean | false | Optional |
| 16 | Rebar Material Key | `"REBAR_MATL_KEY"` | Integer | 0 | Optional |
| 17 | Use Mt | `"bUseMt"` | Boolean | - | **Required** |
| 18 | Thickness | `"THICKNESS"` | Number | - | **Required** |

### Request Body 示例

#### CIVIL NX

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN_NAME": "SDM1",
      "MEMBER_TYPE": 1,
      "V1": 0,
      "V2": 90,
      "DOMAIN_NAME": "DM1",
      "AXIS_VECTOR": [0, 0, 0, 0, 0, 0],
      "bUseMt": true,
      "STR_UCS": "",
      "MEMB_TYPE_CIVIL": 1
    }
  }
}
```

#### GEN NX（含基本钢筋配筋）

```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN_NAME": "SDM1",
      "MEMBER_TYPE": 1,
      "V1": 0,
      "V2": 90,
      "DOMAIN_NAME": "DM1",
      "bUseMt": true,
      "THICKNESS": 0,
      "OPT_BASIC_REBAR": false,
      "TOP_REBAR_NAME_X": "D10",
      "TOP_REBAR_SPACE_X": 0.4,
      "BOTTOM_REBAR_NAME_X": "D10",
      "BOTTOM_REBAR_SPACE_X": 0.4,
      "TOP_REBAR_NAME_Y": "D10",
      "TOP_REBAR_SPACE_Y": 0.4,
      "BOTTOM_REBAR_NAME_Y": "D10",
      "BOTTOM_REBAR_SPACE_Y": 0.4,
      "OPT_REBAR_MATL": false,
      "REBAR_MATL_KEY": 0
    }
  }
}
```

### Python 示例

```python
# 创建 GEN NX Sub-Domain（楼板）
sub_domain_data = {
    "Assign": {
        "1": {
            "SUB_DOMAIN_NAME": "SLAB_SUB",
            "MEMBER_TYPE": 1,       # Slab
            "V1": 0,                # X 方向钢筋 (0°)
            "V2": 90,               # Y 方向钢筋 (90°)
            "DOMAIN_NAME": "SLAB_DOMAIN",
            "bUseMt": True,
            "THICKNESS": 0.2,       # 厚度 200mm
            "OPT_BASIC_REBAR": True,
            "TOP_REBAR_NAME_X": "D13",
            "TOP_REBAR_SPACE_X": 0.15,
            "BOTTOM_REBAR_NAME_X": "D13",
            "BOTTOM_REBAR_SPACE_X": 0.15,
            "TOP_REBAR_NAME_Y": "D13",
            "TOP_REBAR_SPACE_Y": 0.15,
            "BOTTOM_REBAR_NAME_Y": "D13",
            "BOTTOM_REBAR_SPACE_Y": 0.15,
            "OPT_REBAR_MATL": False,
            "REBAR_MATL_KEY": 0
        }
    }
}
midas_api("POST", "/db/SBDO", sub_domain_data)
```

---

## 6. `/db/DOEL`

> **Domain-Element** — 将指定单元分配给 Main-Domain 或 Sub-Domain。

- **URL**: `{base url}/db/DOEL`
- **Methods**: `POST`, `GET`, `PUT`, `DELETE`
- **Source**: [Domain-Element ↗](https://support.midasuser.com/hc/en-us/articles/35807341514393)

### JSON Schema

```json
{
  "DOEL": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "TYPE":             { "description": "Domain Type",     "type": "integer" },
      "KEY_DOMAIN":       { "description": "Key Domain",      "type": "integer" },
      "MAIN_DOMAIN_NAME": { "description": "Main Domain Name","type": "string" }
    }
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Domain Type • Main-Domain: 0 • Sub-Domain: 1 | `"TYPE"` | Integer | - | **Required** |
| 2 | Key Domain | `"KEY_DOMAIN"` | Integer | - | **Required** |
| 3 | Main Domain Name | `"MAIN_DOMAIN_NAME"` | String | - | **Required** |

### Request Body

```json
{
  "Assign": {
    "163": { "TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "164": { "TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "165": { "TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "170": { "TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" },
    "171": { "TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1" }
  }
}
```

### Python 示例

```python
# 将单元分配到域
# 163、164 号单元 → Sub-Domain 1 ("DM1")
# 165、170 号单元 → Main-Domain 1 ("DM1")
doel_data = {
    "Assign": {
        "163": {"TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
        "164": {"TYPE": 1, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
        "165": {"TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
        "170": {"TYPE": 0, "KEY_DOMAIN": 1, "MAIN_DOMAIN_NAME": "DM1"},
    }
}
midas_api("POST", "/db/DOEL", doel_data)

# 查询全部 Domain-Element 分配
result = midas_api("GET", "/db/DOEL")
assignments = result.get("DOEL", {})
print(f"已分配单元总数: {len(assignments)}")

# 仅筛出分配到 Sub-Domain 的单元
sub_domain_elems = {k: v for k, v in assignments.items() if v["TYPE"] == 1}
print(f"分配到 Sub-Domain 的单元: {len(sub_domain_elems)}个")
```

---

## 完整工作流示例 — 3跨 × 5层 RC 刚架 + 楼板

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

# ── Step 1: 新建项目 ─────────────────────────────────
midas_api("POST", "/doc/NEW", {"Argument": {}})

# ── Step 2: 设置单位 (KN, M) ──────────────────────────────
midas_api("PUT", "/db/UNIT", {
    "Assign": {"1": {"FORCE": "KN", "DIST": "M", "HEAT": "KJ", "TEMPER": "C"}}
})

# ── Step 3: 生成节点 (刚架，Y=0 平面) ──────────────────
n_bays, n_stories = 3, 5
bay_w, story_h = 6.0, 3.5
n_cols = n_bays + 1
nodes = {}
node_map = {}
nid = 1
for i_s in range(n_stories + 1):
    for i_c in range(n_cols):
        nodes[str(nid)] = {"X": i_c * bay_w, "Y": 0.0, "Z": i_s * story_h}
        node_map[(i_c, i_s)] = nid
        nid += 1

midas_api("POST", "/db/NODE", {"Assign": nodes})

# ── Step 4: 生成单元 (柱 + 梁) ───────────────────────────
elems = {}
eid = 1
# 柱 (截面 1)
for i_s in range(n_stories):
    for i_c in range(n_cols):
        elems[str(eid)] = {
            "TYPE": "BEAM", "MATL": 1, "SECT": 1,
            "NODE": [node_map[(i_c, i_s)], node_map[(i_c, i_s + 1)]],
            "ANGLE": 0
        }
        eid += 1
# 梁 (截面 2)
for i_s in range(1, n_stories + 1):
    for i_b in range(n_bays):
        elems[str(eid)] = {
            "TYPE": "BEAM", "MATL": 1, "SECT": 2,
            "NODE": [node_map[(i_b, i_s)], node_map[(i_b + 1, i_s)]],
            "ANGLE": 0
        }
        eid += 1

midas_api("POST", "/db/ELEM", {"Assign": elems})

# ── Step 5: 保存 ─────────────────────────────────────────────
midas_api("POST", "/doc/SAVE", {"Argument": {}})

print("✓ RC 刚架模型生成完成")
print(f"  节点: {len(nodes)}个, 单元: {len(elems)}个")
print(f"  柱: {n_cols * n_stories}个, 梁: {n_bays * n_stories}个")
```

---

*[03_DB_Node_Element.md] 已完成 — 下一个文件 [04_DB_Properties.md] 已可开始。*
