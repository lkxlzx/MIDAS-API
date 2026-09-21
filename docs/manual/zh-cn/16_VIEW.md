# 16. VIEW

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../16_VIEW.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

`VIEW` 部分是控制模型视图(View)的函数，涵盖选择状态查询、画面截图、视点(Viewpoint)调整、激活(Active)控制、显示(Display)选项、结果图形(Result Graphic)显示。`CAPTURE` 可以把 `ANGLE`·`ACTIVE`·`DISPLAY`·`RESULTGRAPHIC` 选项合并在一个请求中使用。

---

## Endpoint 列表

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/view/SELECT`](#1-viewselect--select) | 查询所选节点/单元 ID | GET |
| 2 | [`/view/CAPTURE`](#2-viewcapture--capture) | 模型画面截图 (保存图像) | POST |
| 3 | [`/view/PRECAPTURE`](#3-viewprecapture--dialog-capture) | 对话框(预处理)截图 | POST |
| 4 | [`/view/ANGLE`](#4-viewangle--viewpoint) | 视点(Viewpoint)角度设置 | POST |
| 5 | [`/view/ACTIVE`](#5-viewactive--active) | 激活(Active)对象控制 | POST |
| 6 | [`/view/DISPLAY`](#6-viewdisplay--display) | 显示(Display)选项设置 | POST |
| 7 | [`/view/RESULTGRAPHIC`](#7-viewresultgraphic--result-graphic) | 结果图形显示设置 | POST |

---

## 1. `/view/SELECT` — Select

> **功能：** 查询当前模型视图中用户所选节点(Node)与单元(Element)的 ID 列表。为仅响应(GET)的端点。

### Input URI

```
{base url}/view/SELECT
```

### Active Methods

`GET`

### Response JSON

```json
{
  "SELECT": {
    "NODE_LIST": [67, 130, 171, 172, 173, 178, 179],
    "ELEM_LIST": [92, 93, 99, 106, 235, 308, 313, 314, 315, 316, 317, 323, 324, 325, 335, 336, 337, 338, 339, 340]
  }
}
```

### Parameters

为仅响应(GET)的端点，没有请求体。

| No. | 说明 | Key | 值类型 |
|-----|------|-----|-----------|
| 1 | 所选节点 ID 列表 | `"NODE_LIST"` | Array [Integer] |
| 2 | 所选单元 ID 列表 | `"ELEM_LIST"` | Array [Integer] |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── GET: 查询当前所选节点/单元 ────────────────────────────────
resp = requests.get(f"{BASE_URL}/view/SELECT", headers=HEADERS)
sel = resp.json().get("SELECT", {})
print(f"所选节点 {len(sel.get('NODE_LIST', []))} 个: {sel.get('NODE_LIST')}")
print(f"所选单元 {len(sel.get('ELEM_LIST', []))} 个: {sel.get('ELEM_LIST')}")
```

---

## 2. `/view/CAPTURE` — Capture

> **功能：** 将当前模型视图截图并保存为图像文件。可将视点(`ANGLE`)、激活(`ACTIVE`)、显示(`DISPLAY`)、结果图形(`RESULT_GRAPHIC`)选项合并在一个请求中指定。支持 Smart(Dynamic) Report 模式与 User Setting 模式。

### Input URI

```
{base url}/view/CAPTURE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "CAPTURE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "FIGURE_NAME": { "type": "string" },
          "EXPORT_PATH": { "type": "string" },
          "WIDTH": { "type": "integer" },
          "HEIGHT": { "type": "integer" },
          "STAGE_NAME": { "type": "string" },
          "SET_MODE": { "type": "string" },
          "SET_HIDDEN": { "type": "boolean" },
          "ACTIVE": { "type": "object", "description": "View/Active" },
          "ANGLE": { "type": "object", "description": "View/Angle" },
          "DISPLAY": { "type": "object", "description": "View/Display" },
          "RESULT_GRAPHIC": { "type": "object", "description": "View/Result Graphic" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 分组 | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|------|-----|-----------|--------|------|
| 1 | Smart Report | 图像文件保存路径及文件名 | `"EXPORT_PATH"` | String | — | **Required** |
| 2 | Smart Report | Smart Report 图像名称 | `"FIGURE_NAME"` | String | — | **Required** |
| 1 | User Setting | 图像文件保存路径及文件名 | `"EXPORT_PATH"` | String | — | **Required** |
| 2 | User Setting | 施工阶段名称 | `"STAGE_NAME"` | String | — | Optional |
| 3 | User Setting | 分析模式选择 · Pre-Mode: `"pre"` / Post-Mode: `"post"` | `"SET_MODE"` | String | — | Optional |
| 4 | User Setting | 隐藏线(Hidden)选项 · Hidden: `true` / Not Hidden: `false` | `"SET_HIDDEN"` | Boolean | `false` | Optional |
| 5 | User Setting | 图像高度像素尺寸 | `"HEIGHT"` | Integer | — | Optional |
| 6 | User Setting | 图像宽度像素尺寸 | `"WIDTH"` | Integer | — | Optional |
| 7 | User Setting | 视点 (参照 `view/ANGLE` 手册) | `"ANGLE"` | Object | — | Optional |
| 8 | User Setting | 激活 (参照 `view/ACTIVE` 手册) | `"ACTIVE"` | Object | — | Optional |
| 9 | User Setting | 显示 (参照 `view/DISPLAY` 手册) | `"DISPLAY"` | Object | — | Optional |
| 10 | User Setting | 透视(Perspective) | `"PERSPECTIVE"` | Boolean | `false` | Optional |
| 11 | User Setting | 缩放级别 · Zoom Out: `25 ≤ value < 100` / Zoom Fit: `100` / Zoom In: `100 < value < 200` | `"ZOOM_LEVEL"` | Number | `100` | Optional |
| 12 | User Setting | 上方背景色 | `"BGCOLOR_TOP"` | Object | — | Optional |
| 12-1 | | └ Red | `BGCOLOR_TOP.R` | Integer | — | Optional |
| 12-2 | | └ Green | `BGCOLOR_TOP.G` | Integer | — | Optional |
| 12-3 | | └ Blue | `BGCOLOR_TOP.B` | Integer | — | Optional |
| 13 | User Setting | 下方背景色 | `"BGCOLOR_BOTTOM"` | Object | — | Optional |
| 13-1 | | └ Red | `BGCOLOR_BOTTOM.R` | Integer | — | Optional |
| 13-2 | | └ Green | `BGCOLOR_BOTTOM.G` | Integer | — | Optional |
| 13-3 | | └ Blue | `BGCOLOR_BOTTOM.B` | Integer | — | Optional |
| 14 | User Setting | 结果显示 (参照 `view/RESULTGRAPHIC` 手册) | `"RESULT_GRAPHIC"` | Object | — | Optional |

> **参考：** `PERSPECTIVE`、`ZOOM_LEVEL`、`BGCOLOR_TOP`、`BGCOLOR_BOTTOM` 在示例 JSON 中是包含在 `DISPLAY` 对象内部传递的(见下方 Request 示例)。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SET_MODE": "post",
    "SET_HIDDEN": false,
    "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\image.jpg",
    "HEIGHT": 1000,
    "WIDTH": 1000,
    "ACTIVE": {
      "ACTIVE_MODE": "Active",
      "N_LIST": [104, 125, 151, 153],
      "E_LIST": [196, 228, 229, 231, 232, 269, 270, 279, 280, 291, 292, 349, 350]
    },
    "ANGLE": {
      "HORIZONTAL": 45,
      "VERTICAL": 60
    },
    "DISPLAY": {
      "NODE": { "NODE": true, "NODE_NUMBER": true },
      "PERSPECTIVE": true,
      "ZOOM_LEVEL": 150,
      "BGCOLOR_TOP": { "R": 255, "G": 125, "B": 125 }
    },
    "RESULT_GRAPHIC": {
      "CURRENT_MODE": "beam diagrams",
      "LOAD_CASE_COMB": { "TYPE": "ST", "NAME": "DL" },
      "COMPONENTS": { "PART": "total", "COMP": "Fx" },
      "DISPLAY_OPTIONS": { "FIDELITY": "Exact", "FILL": "line fill", "SCALE": 1.0 },
      "TYPE_OF_DISPLAY": {
        "CONTOUR": { "OPT_CHECK": true },
        "DEFORM": { "OPT_CHECK": true },
        "LEGEND": { "OPT_CHECK": true },
        "VALUES": { "OPT_CHECK": true }
      },
      "OUTPUT_SECT_LOCATION": { "OPT_I": true, "OPT_CENTER_MID": true, "OPT_J": true }
    }
  }
}
```

**POST Response Body**

```json
{
  "CAPTURE": {
    "message": "Success"
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

# ── POST: 将梁构件内力(Fx)图形截图为图像 ─────────────────
payload = {
    "Argument": {
        "SET_MODE": "post",
        "SET_HIDDEN": False,
        "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\beam_Fx.jpg",
        "HEIGHT": 1000,
        "WIDTH": 1000,
        "ACTIVE": {"ACTIVE_MODE": "All"},
        "ANGLE": {"HORIZONTAL": 45, "VERTICAL": 60},
        "DISPLAY": {
            "PERSPECTIVE": True,
            "ZOOM_LEVEL": 100,
            "BGCOLOR_TOP": {"R": 255, "G": 255, "B": 255}
        },
        "RESULT_GRAPHIC": {
            "CURRENT_MODE": "beam diagrams",
            "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DL"},
            "COMPONENTS": {"PART": "total", "COMP": "Fx"},
            "DISPLAY_OPTIONS": {"FIDELITY": "Exact", "FILL": "line fill", "SCALE": 1.0},
            "TYPE_OF_DISPLAY": {
                "CONTOUR": {"OPT_CHECK": True},
                "LEGEND": {"OPT_CHECK": True},
                "VALUES": {"OPT_CHECK": True}
            }
        }
    }
}
resp = requests.post(f"{BASE_URL}/view/CAPTURE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 3. `/view/PRECAPTURE` — Dialog Capture

> **功能：** 将特定对话框(预处理预览)画面截图为图像文件。目前支持纤维截面(Fiber Division of Section)预览。

### Input URI

```
{base url}/view/PRECAPTURE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "CAPTURE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "EXPORT_PATH": { "description": "Save Path", "type": "string" },
          "VIEW_TYPE": { "description": "Preview Picture Type", "type": "string", "enum": ["FIBR"] },
          "OPTION": {
            "description": "Option for Capture",
            "type": "object",
            "properties": {
              "ID": { "description": "Picture Type ID Number", "type": "integer" }
            }
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
| 1 | 图像文件保存路径及文件名 | `"EXPORT_PATH"` | String | — | **Required** |
| 2 | 预览图形类型 · 截面纤维分割: `"FIBR"` | `"VIEW_TYPE"` | String | — | **Required** |
| 3 | 截图选项 | `"OPTION"` | Object | — | **Required** |
| 3-1 | └ 图形类型 ID 编号 | `OPTION.ID` | Integer | — | **Required** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\Test.jpg",
    "VIEW_TYPE": "FIBR",
    "OPTION": { "ID": 1 }
  }
}
```

**POST Response Body**

```json
{
  "CAPTURE": {
    "message": "Success"
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

# ── POST: 截图纤维截面(Fiber)预览对话框 ────────────────
payload = {
    "Argument": {
        "EXPORT_PATH": "C:\\MIDAS\\CaptureTest\\fiber_sect_1.jpg",
        "VIEW_TYPE": "FIBR",      # Fiber Division of Section
        "OPTION": {"ID": 1}       # 截面 ID 1 号
    }
}
resp = requests.post(f"{BASE_URL}/view/PRECAPTURE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 4. `/view/ANGLE` — Viewpoint

> **功能：** 按水平/垂直角度设置模型视图的视点(Viewpoint)。

### Input URI

```
{base url}/view/ANGLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "ANGLE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "HORIZONTAL": { "type": "number" },
          "VERTICAL": { "type": "number" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 水平视点角度 | `"HORIZONTAL"` | Number | `0` | Optional |
| 2 | 垂直视点角度 | `"VERTICAL"` | Number | `0` | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "HORIZONTAL": 30,
    "VERTICAL": 15
  }
}
```

**POST Response Body**

```json
{
  "ANGLE": {
    "message": "Success"
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

# ── POST: 将视点设为水平 30°、垂直 15° ─────────────────────────
payload = {"Argument": {"HORIZONTAL": 30, "VERTICAL": 15}}
resp = requests.post(f"{BASE_URL}/view/ANGLE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 5. `/view/ACTIVE` — Active

> **功能：** 指定模型视图中要激活(Active)的对象。支持全部(All)、指定节点/单元(Active)、指定 Identity 组(Identity) 3 种模式。

### Input URI

```
{base url}/view/ACTIVE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "ACTIVE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "ACTIVE_MODE": {
            "type": "string",
            "description": "ActiveModeType",
            "enum": ["All", "Active", "Identity"]
          },
          "N_LIST": {
            "type": "array",
            "items": { "type": "integer" },
            "description": "NodeNumberList"
          },
          "E_LIST": {
            "type": "array",
            "items": { "type": "integer" },
            "description": "ElementNumberList"
          },
          "IDENTITY_TYPE": {
            "type": "string",
            "description": "IdentityType",
            "enum": ["Group", "NamedPlane", "LoadGroup", "BoundaryGroup", "STORY"]
          },
          "IDENTITY_LIST": {
            "type": "array",
            "items": { "type": "string" }
          },
          "STORY_ACTIVE": {
            "type": "string",
            "description": "StoryActiveType (IDENTITY_TYPE=\"STORY\"일 때 사용)",
            "enum": ["FLOOR", "ABOVE", "BELOW", "BOTH"]
          }
        }
      }
    }
  }
}
```

> ⚠️ 2026-08-26 确认 (article id `35523395368985`): 官方原文新增了 `IDENTITY_TYPE="STORY"`(按楼层
> 激活)模式，但原文 JSON Schema 本身未更新，缺少 `STORY`/`STORY_ACTIVE`
> (Specifications 表与 Request Example 中存在)——已以示例·表为准补入 Schema。
> `IDENTITY_TYPE` 的取值在表中写作 `"Story"`，而实际 Request Example 使用 `"STORY"`(全部
> 大写)，故以示例为准采用。

### Parameters

| No. | 模式 | 说明 | Key | 值类型 | 必填 |
|-----|------|------|-----|-----------|------|
| 1 | All | 激活模式 · 全部激活: `"All"` | `"ACTIVE_MODE"` | String | **Required** |
| 1 | Active | 激活模式 · 指定节点/单元: `"Active"` | `"ACTIVE_MODE"` | String | **Required** |
| 2 | Active | 节点编号列表 | `"N_LIST"` | Array [Integer] | **Required** |
| 3 | Active | 单元编号列表 | `"E_LIST"` | Array [Integer] | **Required** |
| 1 | Identity | 激活模式 · 指定 Identity: `"Identity"` | `"ACTIVE_MODE"` | String | **Required** |
| 2 | Identity | Identity 类型 · 结构组: `"Group"` / 命名平面: `"NamedPlane"` / 荷载组: `"LoadGroup"` / 边界组: `"BoundaryGroup"` / 楼层: `"STORY"` | `"IDENTITY_TYPE"` | String | **Required** |
| 3 | Identity | Identity 名称列表(`IDENTITY_TYPE="STORY"` 时为楼层名称列表) | `"IDENTITY_LIST"` | Array [String] | **Required** |
| 4 | Identity | 楼层激活方式(仅 `IDENTITY_TYPE="STORY"` 时) · 仅该层: `"FLOOR"` / 含上方: `"ABOVE"` / 含下方: `"BELOW"` / 上下均含: `"BOTH"` | `"STORY_ACTIVE"` | String | 条件 **Required** |

### Request / Response JSON

**POST Request Body — Mode 1: All**

```json
{
  "Argument": {
    "ACTIVE_MODE": "All"
  }
}
```

**POST Request Body — Mode 2: Active by Node/Element**

```json
{
  "Argument": {
    "ACTIVE_MODE": "Active",
    "N_LIST": [469, 770, 772, 773],
    "E_LIST": [1631, 1646, 1654]
  }
}
```

**POST Request Body — Mode 3: Active by Identity**

```json
{
  "Argument": {
    "ACTIVE_MODE": "Identity",
    "IDENTITY_TYPE": "BoundaryGroup",
    "IDENTITY_LIST": ["Support", "Support2", "Support3"]
  }
}
```

**POST Request Body — Mode 3: Active by Identity (Story)**

```json
{
  "Argument": {
    "ACTIVE_MODE": "Identity",
    "IDENTITY_TYPE": "STORY",
    "IDENTITY_LIST": ["ROOF", "3F", "1F"],
    "STORY_ACTIVE": "BELOW"
  }
}
```

**POST Response Body**

```json
{
  "ACTIVE": {
    "message": "Success"
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

# ── POST: Mode 2 - 仅激活特定节点/单元 ────────────────────────
payload_active = {
    "Argument": {
        "ACTIVE_MODE": "Active",
        "N_LIST": [469, 770, 772, 773],
        "E_LIST": [1631, 1646, 1654]
    }
}
resp = requests.post(f"{BASE_URL}/view/ACTIVE", json=payload_active, headers=HEADERS)
print("POST (Active):", resp.status_code, resp.json())

# ── POST: Mode 3 - 按边界组激活 ─────────────────────────────
payload_identity = {
    "Argument": {
        "ACTIVE_MODE": "Identity",
        "IDENTITY_TYPE": "BoundaryGroup",
        "IDENTITY_LIST": ["Support", "Support2", "Support3"]
    }
}
resp = requests.post(f"{BASE_URL}/view/ACTIVE", json=payload_identity, headers=HEADERS)
print("POST (Identity):", resp.status_code, resp.json())

# ── POST: Mode 1 - 全部激活(重置) ─────────────────────────────
resp = requests.post(f"{BASE_URL}/view/ACTIVE", json={"Argument": {"ACTIVE_MODE": "All"}}, headers=HEADERS)
print("POST (All):", resp.status_code, resp.json())
```

---

## 6. `/view/DISPLAY` — Display

> **功能：** 批量控制模型窗口中显示的节点(Node)·单元(Element)·特性(Property)·边界条件(Boundary)·荷载(Load)·其他(Misc)·视图(View) 各项的显示与否及显示选项(编号、名称、局部轴、荷载值格式等)。本端点仅支持 `POST`，在 `"Argument"` 下只选择性传递要控制的分组对象。

### Input URI

```
{base url}/view/DISPLAY
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "DISPLAY": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "NODE": {
            "type": "object",
            "properties": {
              "NODE": { "type": "boolean" },
              "NODE_NUMBER": { "type": "boolean" },
              "STORY_NAME": { "type": "boolean" },
              "NODE_LOCAL_AXIS": { "type": "boolean" }
            }
          },
          "ELEMENT": {
            "type": "object",
            "properties": {
              "ELEM_NUMBER": { "type": "boolean" },
              "ELEM_NUMBER_WITH_BORDER": { "type": "boolean" },
              "ELEM_TYPE_NUMBER": { "type": "boolean" },
              "ELEM_TYPE_NAME": { "type": "boolean" },
              "WALL_ID": { "type": "boolean" },
              "GAP": { "type": "boolean" },
              "HOOK": { "type": "boolean" },
              "CABLE": { "type": "boolean" },
              "LOCAL_AXIS": { "type": "boolean" },
              "LOCAL_AXIS_LABEL": { "type": "boolean" },
              "LOCAL_DIRECTION": { "type": "boolean" },
              "SUB_DOMAIN_REBAR_DIRECTION": { "type": "boolean" }
            }
          },
          "PROPERTY": {
            "type": "object",
            "properties": {
              "MATERIAL_NUMBER": { "type": "boolean" },
              "MATERIAL_NAME": { "type": "boolean" },
              "PROPERTY_NUMBER": { "type": "boolean" },
              "PROPERTY_NAME": { "type": "boolean" },
              "SECTION_SHAPE": { "type": "boolean" },
              "TAPERED_SECTION_GROUP": { "type": "boolean" },
              "TIME_DEPENDENT_MATERIAL_LINK": { "type": "boolean" },
              "INELASTIC_HINGE_NAME": { "type": "boolean" },
              "INELASTIC_HINGE_SYMBOL": { "type": "boolean" },
              "REINFORCEMENT_OF_SECTIONS": { "type": "boolean" },
              "VIRTUAL_SECTION_LOCAL_AXIS": { "type": "boolean" }
            }
          },
          "GROUP_SELECTION": {
            "type": "array",
            "items": { "type": "string" }
          },
          "BOUNDARY": {
            "type": "object",
            "properties": {
              "SUPPORT": { "type": "boolean" },
              "SUPPORT_BY_DIRECTION": { "type": "boolean" },
              "POINT_SPRING_SUPPORT": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_COMP_TENS": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_MULTI_LINEAR": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_BY_DIRECTION": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_BY_DIRECTION_COMP_TENS": { "type": "boolean" },
              "POINT_SPRING_SUPPORT_BY_DIRECTION_MULTI_LINEAR": { "type": "boolean" },
              "SURFACE_SPRING_SUPPORT_TYPE": { "type": "boolean" },
              "SURFACE_SPRING_SUPPORT_LINEAR": { "type": "boolean" },
              "SURFACE_SPRING_SUPPORT_COMP_TENS": { "type": "boolean" },
              "GENERAL_SPRING_SUPPORT": { "type": "boolean" },
              "ELASTIC_LINK": { "type": "boolean" },
              "ELASTIC_LINK_LOCAL_AXIS": { "type": "boolean" },
              "ELASTIC_LINK_TYPE": { "type": "boolean" },
              "ELASTIC_LINK_NUMBER": { "type": "boolean" },
              "GENERAL_LINK": { "type": "boolean" },
              "GENERAL_LINK_NUMBER": { "type": "boolean" },
              "GENERAL_LINK_LOCAL_AXIS": { "type": "boolean" },
              "GENERAL_LINK_TYPE": { "type": "boolean" },
              "CHANGE_GENERAL_LINK_PROPERTIES": { "type": "boolean" },
              "BEAM_END_RELEASE_SYMBOL": { "type": "boolean" },
              "BEAM_END_RELEASE_DIGIT": { "type": "boolean" },
              "BEAM_END_OFFSET_SYMBOL": { "type": "boolean" },
              "BEAM_END_OFFSET_DIGIT": { "type": "boolean" },
              "PLATE_END_RELEASE_SYMBOL": { "type": "boolean" },
              "PLATE_END_RELEASE_DIGIT": { "type": "boolean" },
              "RIGID_LINK": { "type": "boolean" },
              "LINEAR_CONSTRAINTS": { "type": "boolean" },
              "REACTION_POSITION": { "type": "boolean" },
              "STORY_DIAPHRAGM": { "type": "boolean" },
              "DIAPHRAGM_DISCONNECT": { "type": "boolean" }
            }
          },
          "LOAD": {
            "type": "object",
            "properties": {
              "CASE_SELECTION": {
                "type": "object",
                "properties": {
                  "TYPE": { "type": "string" },
                  "NAME": { "type": "string" }
                }
              },
              "GROUP_SELECTION": {
                "type": "array",
                "items": { "type": "string" }
              },
              "LOAD_VALUE": {
                "type": "object",
                "properties": {
                  "FORMAT": { "type": "string" },
                  "PLACE": { "type": "integer" }
                }
              },
              "NODAL_BODY_FORCE": { "type": "boolean" },
              "NODAL_LOAD": { "type": "boolean" },
              "SPECIFIED_DISPLACEMENT": { "type": "boolean" },
              "BEAM_LOAD": { "type": "boolean" },
              "PRESTRESS_LOAD": { "type": "boolean" },
              "PRETENSION_LOAD": { "type": "boolean" },
              "FLOOR_LOAD": { "type": "boolean" },
              "FLOOR_LOAD_NAME": { "type": "boolean" },
              "FLOOR_LOAD_AREA": { "type": "boolean" },
              "LOADING_AREA_PLANE": { "type": "boolean" },
              "FINISHING_MATERIAL_LOAD": { "type": "boolean" },
              "PRESSURE_LOAD": { "type": "boolean" },
              "AREA_PRESSURE_LOADS": { "type": "boolean" },
              "PLANE_LOAD": { "type": "boolean" },
              "PLANE_LOAD_NAME": { "type": "boolean" },
              "NODAL_TEMPERATURE": { "type": "boolean" },
              "ELEMENT_TEMPERATURE": { "type": "boolean" },
              "TEMPERATURE_GRADIENT": { "type": "boolean" },
              "BEAM_SECTION_TEMPERATURE": { "type": "boolean" },
              "TENDON_PRESTRESS": { "type": "boolean" },
              "WIND_LOAD": { "type": "boolean" },
              "AREA_WIND_PRESSURE": { "type": "boolean" },
              "AREA_WIND_PRESSURE_NAME": { "type": "boolean" },
              "BEAM_WIND_PRESSURE": { "type": "boolean" },
              "NODAL_WIND_PRESSURE": { "type": "boolean" },
              "FUNCTION_WIND_PRESSURE": { "type": "boolean" },
              "FUNCTION_WIND_PRESSURE_NAME": { "type": "boolean" },
              "SEISMIC_EARTH_PRESSURE": { "type": "boolean" },
              "STATIC_EARTH_PRESSURE": { "type": "boolean" },
              "SEISMIC_LOAD": { "type": "boolean" },
              "DYNAMIC_NODAL_LOAD": { "type": "boolean" },
              "MULTIPLE_SUPPORT_EXCITATION": { "type": "boolean" },
              "MULTIPLE_SUPPORT_EXCITATION_FUNCTION_NAME": { "type": "boolean" },
              "DIR_X": { "type": "boolean" },
              "DIR_Y": { "type": "boolean" },
              "DIR_Z": { "type": "boolean" }
            }
          },
          "MISC": {
            "type": "object",
            "properties": {
              "NODAL_MASS": { "type": "boolean" },
              "LOAD_TO_MASS": { "type": "boolean" },
              "TENDON_PROFILE_NAMES": { "type": "boolean" },
              "TENDON_PROFILE_POINT": { "type": "boolean" },
              "INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS": { "type": "boolean" },
              "SETTLEMENT_GROUP": { "type": "boolean" },
              "SETTLEMENT_GROUP_VALUE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_VALUE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_FUNC_NAME": { "type": "boolean" },
              "HEAT_OF_HYDRATION_ELEMENT_CONVECTION_BOUNDARY": { "type": "boolean" },
              "HEAT_OF_HYDRATION_PRESCRIBED_TEMPERATURE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_HEAT_SOURCE": { "type": "boolean" },
              "HEAT_OF_HYDRATION_PIPE_COOLING_ELEMENT": { "type": "boolean" },
              "GRID_MODEL_LOAD_LINE": { "type": "boolean" }
            }
          },
          "VIEW": {
            "type": "object",
            "properties": {
              "UCS_AXIS": { "type": "boolean" },
              "VIEWPORT_GIZMO": { "type": "boolean" },
              "VIEW_POINT": { "type": "boolean" },
              "DESCRIPTION": { "type": "string" },
              "LABEL_ORIENTATION": { "type": "integer" }
            }
          }
        }
      }
    }
  }
}
```

> **参考：** 原始 Schema 中缺少 `MISC.GRID_MODEL_LOAD_LINE`，但示例与 Specifications 中都有，故已包含(`GRID_MODEL_LOAD_LINE` 为 MIDAS CIVIL NX JP 版本专用)。另外原始 Schema/示例中的 `VIEWPPORT_GIZMO` 为拼写错误，正式 Key 是 `VIEWPORT_GIZMO`。
>
> ⚠️ 2026-08-26 确认 (article id `35996157533977`): 原文 Examples 中有 Node/Element/**Property**/
> Boundary/Load/**MISC**/View 7 类示例，但旧版文档缺失 Property·MISC 两类，已补全。
> Boundary/Load 示例的原文把全部字段都列为 `true`(不过这是原文示例自身的问题，与表中的
> 相互排斥(ˢ#⁾)脚注矛盾，可作为错误反馈对象)，本地文档按既有惯例只摘录部分代表性字段
> (取值全部准确)。

### Parameters

#### 1) Node Display — `Argument.NODE` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 节点显示选项分组 | `NODE` | Object | - | Optional |
| (1) | 节点(Node)显示 | `NODE.NODE` | Boolean | false | Optional |
| (2) | 节点编号(Node Number) | `NODE.NODE_NUMBER` | Boolean | false | Optional |
| (3) | 节点局部坐标轴(Node Local Axis) | `NODE.NODE_LOCAL_AXIS` | Boolean | false | Optional |
| (4) | 楼层名称(Story Name) ᴳ⁾ | `NODE.STORY_NAME` | Boolean | false | Optional |

#### 2) Element Display — `Argument.ELEMENT` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 2 | 单元显示选项分组 | `ELEMENT` | Object | - | Optional |
| (1) | 单元编号(Element Number) | `ELEMENT.ELEM_NUMBER` | Boolean | false | Optional |
| (2) | 带边框的单元编号 | `ELEMENT.ELEM_NUMBER_WITH_BORDER` | Boolean | false | Optional |
| (3) | 单元类型编号 | `ELEMENT.ELEM_TYPE_NUMBER` | Boolean | false | Optional |
| (4) | 单元类型名称 | `ELEMENT.ELEM_TYPE_NAME` | Boolean | false | Optional |
| (5) | 墙 ID(Wall ID) ᴳ⁾ | `ELEMENT.WALL_ID` | Boolean | false | Optional |
| (6) | 间隙单元(Gap) | `ELEMENT.GAP` | Boolean | false | Optional |
| (7) | 钩单元(Hook) | `ELEMENT.HOOK` | Boolean | false | Optional |
| (8) | 拉索(Cable) | `ELEMENT.CABLE` | Boolean | false | Optional |
| (9) | 局部坐标轴(Local Axis) | `ELEMENT.LOCAL_AXIS` | Boolean | false | Optional |
| (10) | 局部轴标签 (Local Axis 为 True 时) | `ELEMENT.LOCAL_AXIS_LABEL` | Boolean | false | Optional |
| (11) | 局部方向(Local Direction) | `ELEMENT.LOCAL_DIRECTION` | Boolean | false | Optional |
| (12) | 子域钢筋方向 | `ELEMENT.SUB_DOMAIN_REBAR_DIRECTION` | Boolean | false | Optional |

#### 3) Property Display — `Argument.PROPERTY` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 3 | 特性显示选项分组 | `PROPERTY` | Object | - | Optional |
| (1) | 材料编号(Material Number) ˢ¹⁾ | `PROPERTY.MATERIAL_NUMBER` | Boolean | false | Optional |
| (2) | 材料名称(Material Name) ˢ¹⁾ | `PROPERTY.MATERIAL_NAME` | Boolean | false | Optional |
| (3) | 特性编号(Property Number) ˢ¹⁾ | `PROPERTY.PROPERTY_NUMBER` | Boolean | false | Optional |
| (4) | 特性名称(Property Name) ˢ¹⁾ | `PROPERTY.PROPERTY_NAME` | Boolean | false | Optional |
| (5) | 截面形状(Section Shape) | `PROPERTY.SECTION_SHAPE` | Boolean | false | Optional |
| (6) | 变截面组(Tapered Section Group) ˢ¹⁾ | `PROPERTY.TAPERED_SECTION_GROUP` | Boolean | false | Optional |
| (7) | 时间相关材料链接 ˢ¹⁾ | `PROPERTY.TIME_DEPENDENT_MATERIAL_LINK` | Boolean | false | Optional |
| (8) | 非弹性铰名称 ˢ²⁾ | `PROPERTY.INELASTIC_HINGE_NAME` | Boolean | false | Optional |
| (9) | 非弹性铰符号 ˢ²⁾ | `PROPERTY.INELASTIC_HINGE_SYMBOL` | Boolean | false | Optional |
| (10) | 截面配筋(Reinforcement of Sections) | `PROPERTY.REINFORCEMENT_OF_SECTIONS` | Boolean | false | Optional |
| (11) | 虚拟截面局部轴 | `PROPERTY.VIRTUAL_SECTION_LOCAL_AXIS` | Boolean | false | Optional |

#### 4) Boundary Display — `Argument.GROUP_SELECTION` / `Argument.BOUNDARY`

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 4 | 边界组选择 | `GROUP_SELECTION` | Array[String] | All | Optional |
| 5 | 边界条件显示选项分组 | `BOUNDARY` | Object | - | Optional |
| (1) | 支座(Support) ˢ³⁾ | `BOUNDARY.SUPPORT` | Boolean | false | Optional |
| (2) | 按方向的支座 ˢ³⁾ | `BOUNDARY.SUPPORT_BY_DIRECTION` | Boolean | false | Optional |
| (3) | 点弹簧支座 ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT` | Boolean | false | Optional |
| (4) | 点弹簧支座(受压/受拉) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_COMP_TENS` | Boolean | false | Optional |
| (5) | 点弹簧支座(多重线性) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_MULTI_LINEAR` | Boolean | false | Optional |
| (6) | 按方向的点弹簧支座 ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_BY_DIRECTION` | Boolean | false | Optional |
| (7) | 按方向的点弹簧支座(受压/受拉) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_BY_DIRECTION_COMP_TENS` | Boolean | false | Optional |
| (8) | 按方向的点弹簧支座(多重线性) ˢ⁴⁾ | `BOUNDARY.POINT_SPRING_SUPPORT_BY_DIRECTION_MULTI_LINEAR` | Boolean | false | Optional |
| (9) | 面弹簧支座类型 | `BOUNDARY.SURFACE_SPRING_SUPPORT_TYPE` | Boolean | false | Optional |
| (10) | 面弹簧支座(线性) | `BOUNDARY.SURFACE_SPRING_SUPPORT_LINEAR` | Boolean | false | Optional |
| (11) | 面弹簧支座(受压/受拉) | `BOUNDARY.SURFACE_SPRING_SUPPORT_COMP_TENS` | Boolean | false | Optional |
| (12) | 一般弹簧支座 | `BOUNDARY.GENERAL_SPRING_SUPPORT` | Boolean | false | Optional |
| (13) | 弹性连接(Elastic Link) | `BOUNDARY.ELASTIC_LINK` | Boolean | false | Optional |
| (14) | 弹性连接局部轴 (Elastic Link 为 True 时) | `BOUNDARY.ELASTIC_LINK_LOCAL_AXIS` | Boolean | false | Optional |
| (15) | 弹性连接类型 (Elastic Link 为 True 时) | `BOUNDARY.ELASTIC_LINK_TYPE` | Boolean | false | Optional |
| (16) | 弹性连接编号 (Elastic Link 为 True 时) | `BOUNDARY.ELASTIC_LINK_NUMBER` | Boolean | false | Optional |
| (17) | 一般连接(General Link) ˢ⁵⁾, ˢ⁶⁾ | `BOUNDARY.GENERAL_LINK` | Boolean | false | Optional |
| (18) | 一般连接编号 ˢ⁷⁾, ˢ⁸⁾ | `BOUNDARY.GENERAL_LINK_NUMBER` | Boolean | false | Optional |
| (19) | 一般连接局部轴 ˢ⁵⁾, ˢ⁸⁾ | `BOUNDARY.GENERAL_LINK_LOCAL_AXIS` | Boolean | false | Optional |
| (20) | 一般连接类型 ˢ⁶⁾, ˢ⁷⁾ | `BOUNDARY.GENERAL_LINK_TYPE` | Boolean | false | Optional |
| (21) | 一般连接特性变更 | `BOUNDARY.CHANGE_GENERAL_LINK_PROPERTIES` | Boolean | false | Optional |
| (22) | 梁端释放符号 ˢ⁹⁾ | `BOUNDARY.BEAM_END_RELEASE_SYMBOL` | Boolean | false | Optional |
| (23) | 梁端释放数值 ˢ⁹⁾ | `BOUNDARY.BEAM_END_RELEASE_DIGIT` | Boolean | false | Optional |
| (24) | 梁端偏移符号 | `BOUNDARY.BEAM_END_OFFSET_SYMBOL` | Boolean | false | Optional |
| (25) | 梁端偏移数值 | `BOUNDARY.BEAM_END_OFFSET_DIGIT` | Boolean | false | Optional |
| (26) | 板端释放符号 ˢ¹⁰⁾ | `BOUNDARY.PLATE_END_RELEASE_SYMBOL` | Boolean | false | Optional |
| (27) | 板端释放数值 ˢ¹⁰⁾ | `BOUNDARY.PLATE_END_RELEASE_DIGIT` | Boolean | false | Optional |
| (28) | 刚性连接(Rigid Link) | `BOUNDARY.RIGID_LINK` | Boolean | false | Optional |
| (29) | 线性约束(Linear Constraints) | `BOUNDARY.LINEAR_CONSTRAINTS` | Boolean | false | Optional |
| (30) | 反力位置(Reaction Position) | `BOUNDARY.REACTION_POSITION` | Boolean | false | Optional |
| (31) | 楼层刚性隔板(Story Diaphragm) ᴳ⁾ | `BOUNDARY.STORY_DIAPHRAGM` | Boolean | false | Optional |
| (32) | 刚性隔板分离(Diaphragm Disconnect) ᴳ⁾ | `BOUNDARY.DIAPHRAGM_DISCONNECT` | Boolean | false | Optional |

#### 5) Load Display — `Argument.LOAD` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 6 | 荷载显示选项分组 | `LOAD` | Object | - | Optional |
| (1) | 按荷载工况选择荷载 | `LOAD.CASE_SELECTION` | Object | All | Optional |
| i. | 荷载工况类型 (静力荷载: `"ST"`) | `LOAD.CASE_SELECTION.TYPE` | String | - | Required |
| ii. | 荷载工况名称 | `LOAD.CASE_SELECTION.NAME` | String | - | Required |
| (2) | 荷载组选择 | `LOAD.GROUP_SELECTION` | Array[String] | All | Optional |
| (3) | 荷载值(Load Value) | `LOAD.LOAD_VALUE` | Object | - | Optional |
| i. | 显示格式 (`"Default"` / `"Fixed"` / `"Scientific"`) | `LOAD.LOAD_VALUE.FORMAT` | String | - | Required |
| ii. | 小数点后位数 | `LOAD.LOAD_VALUE.PLACE` | Integer | - | Required |
| (4) | 节点体积力(Nodal Body Force) | `LOAD.NODAL_BODY_FORCE` | Boolean | false | Optional |
| (5) | 节点荷载(Nodal Load) | `LOAD.NODAL_LOAD` | Boolean | false | Optional |
| (6) | 强制位移(Specified Displacement) | `LOAD.SPECIFIED_DISPLACEMENT` | Boolean | false | Optional |
| (7) | 梁单元荷载(Beam Load) | `LOAD.BEAM_LOAD` | Boolean | false | Optional |
| (8) | 预应力荷载 | `LOAD.PRESTRESS_LOAD` | Boolean | false | Optional |
| (9) | 先张荷载 | `LOAD.PRETENSION_LOAD` | Boolean | false | Optional |
| (10) | 楼面荷载(Floor Load) | `LOAD.FLOOR_LOAD` | Boolean | false | Optional |
| (11) | 楼面荷载名称 | `LOAD.FLOOR_LOAD_NAME` | Boolean | false | Optional |
| (12) | 楼面荷载面积 | `LOAD.FLOOR_LOAD_AREA` | Boolean | false | Optional |
| (13) | 荷载施加平面(Loading Area Plane) ᴳ⁾ | `LOAD.LOADING_AREA_PLANE` | Boolean | false | Optional |
| (14) | 饰面材料荷载(Finishing Material Load) ᴳ⁾ | `LOAD.FINISHING_MATERIAL_LOAD` | Boolean | false | Optional |
| (15) | 压力荷载(Pressure Load) | `LOAD.PRESSURE_LOAD` | Boolean | false | Optional |
| (16) | 面积压力荷载(Area Pressure Loads) | `LOAD.AREA_PRESSURE_LOADS` | Boolean | false | Optional |
| (17) | 平面荷载(Plane Load) | `LOAD.PLANE_LOAD` | Boolean | false | Optional |
| (18) | 平面荷载名称 | `LOAD.PLANE_LOAD_NAME` | Boolean | false | Optional |
| (19) | 节点温度(Nodal Temperature) | `LOAD.NODAL_TEMPERATURE` | Boolean | false | Optional |
| (20) | 单元温度(Element Temperature) | `LOAD.ELEMENT_TEMPERATURE` | Boolean | false | Optional |
| (21) | 温度梯度(Temperature Gradient) | `LOAD.TEMPERATURE_GRADIENT` | Boolean | false | Optional |
| (22) | 梁截面温度 | `LOAD.BEAM_SECTION_TEMPERATURE` | Boolean | false | Optional |
| (23) | 预应力束预应力 | `LOAD.TENDON_PRESTRESS` | Boolean | false | Optional |
| (24) | 风荷载(Wind Load) ᴳ⁾ | `LOAD.WIND_LOAD` | Boolean | false | Optional |
| (25) | 面积风压(Area Wind Pressure) ᴳ⁾ | `LOAD.AREA_WIND_PRESSURE` | Boolean | false | Optional |
| (26) | 面积风压名称 ᴳ⁾ | `LOAD.AREA_WIND_PRESSURE_NAME` | Boolean | false | Optional |
| (27) | 梁风压(Beam Wind Pressure) ᴳ⁾ | `LOAD.BEAM_WIND_PRESSURE` | Boolean | false | Optional |
| (28) | 节点风压(Nodal Wind Pressure) ᴳ⁾ | `LOAD.NODAL_WIND_PRESSURE` | Boolean | false | Optional |
| (29) | 函数风压(Function Wind Pressure) ᴳ⁾ | `LOAD.FUNCTION_WIND_PRESSURE` | Boolean | false | Optional |
| (30) | 函数风压名称 ᴳ⁾ | `LOAD.FUNCTION_WIND_PRESSURE_NAME` | Boolean | false | Optional |
| (31) | 地震土压力(Seismic Earth Pressure) ᴳ⁾ | `LOAD.SEISMIC_EARTH_PRESSURE` | Boolean | false | Optional |
| (32) | 静力土压力(Static Earth Pressure) ᴳ⁾ | `LOAD.STATIC_EARTH_PRESSURE` | Boolean | false | Optional |
| (33) | 地震作用(Seismic Load) ᴳ⁾ | `LOAD.SEISMIC_LOAD` | Boolean | false | Optional |
| (34) | 动力节点荷载 | `LOAD.DYNAMIC_NODAL_LOAD` | Boolean | false | Optional |
| (35) | 多点地震输入(Multiple Support Excitation) | `LOAD.MULTIPLE_SUPPORT_EXCITATION` | Boolean | false | Optional |
| (36) | 多点地震输入函数名称 | `LOAD.MULTIPLE_SUPPORT_EXCITATION_FUNCTION_NAME` | Boolean | false | Optional |
| (37) | X 方向 (激励函数名称为 True 时) | `LOAD.DIR_X` | Boolean | false | Optional |
| (38) | Y 方向 (激励函数名称为 True 时) | `LOAD.DIR_Y` | Boolean | false | Optional |
| (39) | Z 方向 (激励函数名称为 True 时) | `LOAD.DIR_Z` | Boolean | false | Optional |

#### 6) Miscellaneous Display — `Argument.MISC` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 7 | 其他显示选项分组 | `MISC` | Object | - | Optional |
| (1) | 节点质量(Nodal Mass) | `MISC.NODAL_MASS` | Boolean | false | Optional |
| (2) | 荷载转质量(Load to Mass) | `MISC.LOAD_TO_MASS` | Boolean | false | Optional |
| (3) | 预应力束线形名称 | `MISC.TENDON_PROFILE_NAMES` | Boolean | false | Optional |
| (4) | 预应力束线形点 | `MISC.TENDON_PROFILE_POINT` | Boolean | false | Optional |
| (5) | 几何刚度初始力 | `MISC.INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS` | Boolean | false | Optional |
| (6) | 沉降组(Settlement Group) | `MISC.SETTLEMENT_GROUP` | Boolean | false | Optional |
| (7) | 沉降组取值 (Settlement Group 为 True 时) | `MISC.SETTLEMENT_GROUP_VALUE` | Boolean | false | Optional |
| (8) | 水化热取值 | `MISC.HEAT_OF_HYDRATION_VALUE` | Boolean | false | Optional |
| (9) | 水化热函数名称 | `MISC.HEAT_OF_HYDRATION_FUNC_NAME` | Boolean | false | Optional |
| (10) | 水化热单元对流边界 | `MISC.HEAT_OF_HYDRATION_ELEMENT_CONVECTION_BOUNDARY` | Boolean | false | Optional |
| (11) | 水化热规定温度 | `MISC.HEAT_OF_HYDRATION_PRESCRIBED_TEMPERATURE` | Boolean | false | Optional |
| (12) | 水化热热源(Heat Source) | `MISC.HEAT_OF_HYDRATION_HEAT_SOURCE` | Boolean | false | Optional |
| (13) | 水化热冷却管单元 | `MISC.HEAT_OF_HYDRATION_PIPE_COOLING_ELEMENT` | Boolean | false | Optional |
| (14) | 网格模型荷载线(Grid Model Load Line) ᴶ⁾ | `MISC.GRID_MODEL_LOAD_LINE` | Boolean | false | Optional |

#### 7) View Display — `Argument.VIEW` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 8 | 视图显示选项分组 | `VIEW` | Object | - | Optional |
| (1) | UCS 轴(UCS Axis) | `VIEW.UCS_AXIS` | Boolean | false | Optional |
| (2) | 动态视图控制(Viewport Gizmo) | `VIEW.VIEWPORT_GIZMO` | Boolean | false | Optional |
| (3) | 视点(View Point) | `VIEW.VIEW_POINT` | Boolean | false | Optional |
| (4) | 说明(Description) | `VIEW.DESCRIPTION` | String | Blank | Optional |
| (5) | 标签方向(Label Orientation) | `VIEW.LABEL_ORIENTATION` | Integer | 0 | Optional |

> **脚注(Footnotes)**
> - ˢ#⁾ : 相互排斥选项。同一 `#` 组内只能选择一项。
> - ᴳ⁾ : MIDAS GEN NX 专用
> - ᴶ⁾ : MIDAS CIVIL NX JP 版本专用

### Request / Response JSON

**POST Request Body — Node Display**

```json
{
  "Argument": {
    "NODE": {
      "NODE": false,
      "NODE_NUMBER": false,
      "STORY_NAME": false,
      "NODE_LOCAL_AXIS": false
    }
  }
}
```

**POST Request Body — Element Display**

```json
{
  "Argument": {
    "ELEMENT": {
      "ELEM_NUMBER": true,
      "ELEM_NUMBER_WITH_BORDER": true,
      "ELEM_TYPE_NUMBER": true,
      "ELEM_TYPE_NAME": true,
      "WALL_ID": true,
      "GAP": true,
      "HOOK": true,
      "CABLE": true,
      "LOCAL_AXIS": true,
      "LOCAL_AXIS_LABEL": true,
      "LOCAL_DIRECTION": true,
      "SUB_DOMAIN_REBAR_DIRECTION": true
    }
  }
}
```

**POST Request Body — Property Display**

```json
{
  "Argument": {
    "PROPERTY": {
      "MATERIAL_NUMBER": true,
      "MATERIAL_NAME": true,
      "PROPERTY_NUMBER": true,
      "PROPERTY_NAME": true,
      "SECTION_SHAPE": true,
      "TAPERED_SECTION_GROUP": true,
      "TIME_DEPENDENT_MATERIAL_LINK": true,
      "INELASTIC_HINGE_NAME": true,
      "INELASTIC_HINGE_SYMBOL": true,
      "REINFORCEMENT_OF_SECTIONS": true,
      "VIRTUAL_SECTION_LOCAL_AXIS": true
    }
  }
}
```

**POST Request Body — Boundary Display**

```json
{
  "Argument": {
    "GROUP_SELECTION": ["Bndr Group 1"],
    "BOUNDARY": {
      "SUPPORT": true,
      "SUPPORT_BY_DIRECTION": true,
      "POINT_SPRING_SUPPORT": true,
      "ELASTIC_LINK": true,
      "ELASTIC_LINK_LOCAL_AXIS": true,
      "GENERAL_LINK": true,
      "RIGID_LINK": true,
      "REACTION_POSITION": true,
      "STORY_DIAPHRAGM": true,
      "DIAPHRAGM_DISCONNECT": true
    }
  }
}
```

**POST Request Body — Load Display**

```json
{
  "Argument": {
    "LOAD": {
      "CASE_SELECTION": {
        "TYPE": "st",
        "NAME": "DL"
      },
      "GROUP_SELECTION": ["Load Group 1", "Load Group 2", "Load Group 3"],
      "LOAD_VALUE": {
        "FORMAT": "Fixed",
        "PLACE": 1
      },
      "NODAL_LOAD": true,
      "BEAM_LOAD": true,
      "PRESSURE_LOAD": true,
      "WIND_LOAD": true,
      "SEISMIC_LOAD": true
    }
  }
}
```

**POST Request Body — MISC Display**

```json
{
  "Argument": {
    "MISC": {
      "NODAL_MASS": true,
      "LOAD_TO_MASS": true,
      "TENDON_PROFILE_NAMES": true,
      "TENDON_PROFILE_POINT": true,
      "INITIAL_FORCES_FOR_GEOMETRIC_STIFFNESS": true,
      "SETTLEMENT_GROUP": true,
      "SETTLEMENT_GROUP_VALUE": true,
      "HEAT_OF_HYDRATION_VALUE": true,
      "HEAT_OF_HYDRATION_FUNC_NAME": true,
      "HEAT_OF_HYDRATION_ELEMENT_CONVECTION_BOUNDARY": true,
      "HEAT_OF_HYDRATION_PRESCRIBED_TEMPERATURE": true,
      "HEAT_OF_HYDRATION_HEAT_SOURCE": true,
      "HEAT_OF_HYDRATION_PIPE_COOLING_ELEMENT": true,
      "GRID_MODEL_LOAD_LINE": true
    }
  }
}
```

**POST Request Body — View Display**

```json
{
  "Argument": {
    "VIEW": {
      "UCS_AXIS": true,
      "VIEWPORT_GIZMO": true,
      "VIEW_POINT": true,
      "DESCRIPTION": "Test",
      "LABEL_ORIENTATION": 15
    }
  }
}
```

**POST Response Body**

```json
{
  "DISPLAY": "Display settings updated."
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

# ── POST: 设置单元显示项 + 荷载显示 + 视图选项 ────────────────
payload = {
    "Argument": {
        "ELEMENT": {
            "ELEM_NUMBER": True,          # 显示单元编号
            "ELEM_TYPE_NAME": True,       # 显示单元类型名称
            "LOCAL_AXIS": True,           # 显示局部坐标轴
            "LOCAL_AXIS_LABEL": True      # 局部轴标签(LOCAL_AXIS 为 True 时)
        },
        "LOAD": {
            "CASE_SELECTION": {"TYPE": "st", "NAME": "DL"},   # 静力荷载工况
            "GROUP_SELECTION": ["Load Group 1"],              # 要显示的荷载组
            "LOAD_VALUE": {"FORMAT": "Fixed", "PLACE": 1},    # 固定小数点 1 位
            "NODAL_LOAD": True,           # 显示节点荷载
            "BEAM_LOAD": True             # 显示梁单元荷载
        },
        "VIEW": {
            "UCS_AXIS": True,             # 显示 UCS 轴
            "VIEWPORT_GIZMO": True,       # 动态视图控制 gizmo
            "LABEL_ORIENTATION": 15       # 标签方向(角度)
        }
    }
}
resp = requests.post(f"{BASE_URL}/view/DISPLAY", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 7. `/view/RESULTGRAPHIC` — Result Graphic

> **功能：** 控制反力/位移/梁图/平面·板应力/实体应力等分析结果在模型窗口中的图形显示方式。除当前结果模式(`CURRENT_MODE`)、荷载工况/组合(`LOAD_CASE_COMB`)、分量(`COMPONENTS`)外，还在 `TYPE_OF_DISPLAY` 对象下细设置云图(Contour)·数值(Values)·图例(Legend)·变形(Deform)·显示选项·对称镜像·切割图/切割面·施加荷载·等值面(IsoSurface)等。本端点仅支持 `POST`。

### Input URI

```
{base url}/view/RESULTGRAPHIC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "RESULTGRAPHIC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "ArgumentSchema",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TYPE_OF_DISPLAY": {
            "type": "object",
            "description": "TypeofDisplay",
            "properties": {
              "CONTOUR": {
                "type": "object",
                "description": "ContourDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "NUM_OF_COLOR": { "type": "integer", "description": "SelecttheNumberofColortoDrawtheContour" },
                  "COLOR_TYPE": {
                    "type": "string",
                    "description": "SelecttheTypeofColors",
                    "enum": ["vrgb", "rgb", "brg", "grayscaled"]
                  },
                  "OPTIONS": {
                    "type": "object",
                    "description": "SpecifyOptionsforContourRepresentation",
                    "properties": {
                      "CONTOUR_FILL": { "type": "boolean", "description": "SelecttheTypeofFill" },
                      "GRADIENT_FILL": { "type": "boolean", "description": "GradientFill" }
                    }
                  }
                }
              },
              "VALUES": {
                "type": "object",
                "description": "ValuesOutputDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "VALUE_EXP": { "type": "boolean", "description": "SelectExponentialorFixedValue" },
                  "DECIMAL_PT": { "type": "integer", "description": "SelecttheNumberofDecimalPlacestoDisplay" },
                  "SET_ORIENT": { "type": "integer", "description": "SetstheOrientationoftheValue" },
                  "MINMAX_ONLY": {
                    "type": "object",
                    "description": "Enable'MinMaxOnly'",
                    "properties": {
                      "MAXMIN": {
                        "type": "string",
                        "description": "MinMaxTypeofValues",
                        "enum": ["Min&Max", "AbsMax", "Max", "Min"]
                      },
                      "LIMIT_SCALE": { "type": "integer", "description": "LimitScale" }
                    }
                  }
                }
              },
              "LEGEND": {
                "type": "object",
                "description": "LegendDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "POSITION": {
                    "type": "string",
                    "description": "Positionofthelegendinthedisplaywindow",
                    "enum": ["right", "left"]
                  },
                  "VALUE_EXP": { "type": "boolean", "description": "SelectExponentialorFixedValue" },
                  "DECIMAL_PT": { "type": "integer", "description": "SelecttheNumberofDecimalPlacestoDisplay" }
                }
              },
              "DEFORM": {
                "type": "object",
                "description": "DeformationDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "SCALE_FACTOR": { "type": "number", "description": "DeformationScaleFactor" },
                  "REAL_DEFORM": { "type": "boolean", "description": "DeformationType" },
                  "REL_DISP": { "type": "boolean", "description": "RelativeDeformation" },
                  "REAL_DISP": { "type": "boolean", "description": "RealStructuralDeformation" }
                }
              },
              "DISP_OPT": {
                "type": "object",
                "description": "DisplayOptionDetails",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "ELEMENT_CENTER": { "type": "boolean", "description": "PlaceContourinElementCenter" },
                  "VALUE_MAX": { "type": "boolean", "description": "SelectShowingValuesofMaximumorElementCenter" }
                }
              },
              "MIRRORED": {
                "type": "object",
                "description": "SymmetricModelMirrorDetail",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "MIRROR_BY_1": {
                    "type": "object",
                    "description": "MirrorByHalfModel",
                    "properties": {
                      "DIRECTION": {
                        "type": "string",
                        "description": "MirrorByDirection(Half)",
                        "enum": ["XY", "YZ", "XZ"]
                      },
                      "OFFSET": { "type": "number", "description": "MirrorByOffsetDistance(Half)" }
                    }
                  },
                  "MIRROR_BY_2": {
                    "type": "object",
                    "description": "MirrorByHalfModel",
                    "properties": {
                      "DIRECTION": {
                        "type": "string",
                        "description": "MirrorByDirection(Quarter)",
                        "enum": ["XY", "YZ", "XZ"]
                      },
                      "OFFSET": { "type": "number", "description": "MirrorByOffsetDistance(Quarter)" }
                    }
                  }
                }
              },
              "CUTTING_DIAGRAM": {
                "type": "object",
                "description": "CuttingDiagram",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "CUTTING_MODE": {
                    "type": "string",
                    "description": "CuttingDiagramMode",
                    "enum": ["line", "plane"]
                  },
                  "CUTTING_NAME": {
                    "type": "array",
                    "description": "SelectCuttingLineorPlane",
                    "items": { "type": "string" }
                  },
                  "NORMAL_TO_PLANE": { "type": "boolean", "description": "DisplaytheGraphDirectionOptionofPlateElements" },
                  "SCALE_FACTOR": { "type": "number", "description": "ScaleFactorforDiagramOutputRatio" },
                  "REVERSE": { "type": "boolean", "description": "ExpresstheDiagramintheReverseDirection" },
                  "VALUE_OUTPUT": { "type": "boolean", "description": "ProducetheOutputinValues" },
                  "MINMAX_ONLY": { "type": "boolean", "description": "ShowonlytheMaximumandMinimumvalues" }
                }
              },
              "CUTTING_PLANE": {
                "type": "object",
                "description": "CuttingPlaneDetailDialog",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "PLANE_NAME": {
                    "type": "array",
                    "description": "SelecttheCuttingPlanes",
                    "items": { "type": "string" }
                  },
                  "FREE_EDGE": { "type": "boolean", "description": "DrawtheOutlineOption" }
                }
              },
              "APPLIED_LOADS": {
                "type": "object",
                "description": "AppliedLoads(MovingLoadTracerDetail)",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "SCALE_FACTOR": { "type": "number", "description": "LoadScaleFactor" },
                  "OPT_LOAD_VALUES": { "type": "boolean", "description": "ShowLoadValues" },
                  "VALUE_TYPE": {
                    "type": "string",
                    "description": "SelecttheValueOutputType",
                    "enum": ["Exponential", "Fixed"]
                  },
                  "VALUE_DECIMAL_PT": { "type": "integer", "description": "ValueOutputDecimalPoint" }
                }
              },
              "ISO_SURFACE": {
                "type": "object",
                "description": "IsoSurfaceDetailDialog",
                "properties": {
                  "OPT_CHECK": { "type": "boolean", "description": "ControltheTypeofDisplay" },
                  "DRAW_POLYLINE": { "type": "boolean", "description": "DrawPolygonOutline" },
                  "TRANSPARENCY": { "type": "number", "description": "Transparent(ScreenOnly)" },
                  "FREE_EDGE": { "type": "boolean", "description": "Outline(highlight)theSolidElementMode" },
                  "VALUE_MODE": {
                    "type": "object",
                    "description": "SelecttheValuestobeDisplayedforStress",
                    "properties": {
                      "VALUE_TYPE": {
                        "type": "string",
                        "enum": ["relative", "values"],
                        "description": "IsoSurfaceValuesType"
                      },
                      "VALUE": {
                        "type": "array",
                        "items": { "type": "number" },
                        "description": "IsoSurfaceValues"
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
}
```

> **参考：** 上述 JSON Schema 只详细定义了 `Argument.TYPE_OF_DISPLAY` 的下级。实际请求中会与 `TYPE_OF_DISPLAY` 一起传递用于指定结果模式的顶层键(`CURRENT_MODE`、`LOAD_CASE_COMB`、`COMPONENTS`、`DISPLAY_OPTIONS`、`OPTIONS`、`OUTPUT_SECT_LOCATION` 等)。每个结果项(模式)可用的键不同，请参照相应项的手册。此外 Specifications 中还定义了 Schema 里没有的额外 `TYPE_OF_DISPLAY` 下级键(`UNDEFORMED`、`ARROW_SCALE_FACTOR`、`OPT_CUR_STEP_DISPLACEMENT` 等)，已全部纳入下方参数表。

### Parameters

#### 1) Type of Display — `Argument.TYPE_OF_DISPLAY` (Object, Optional)

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 显示类型(Type of Display) | `TYPE_OF_DISPLAY` | Object | System | Optional |
| (1) | 云图详情(Contour Details) | `TYPE_OF_DISPLAY.CONTOUR` | Object | - | Optional |
| (2) | 数值输出详情(Values Output Details) | `TYPE_OF_DISPLAY.VALUES` | Object | - | Optional |
| (3) | 图例详情(Legend Details) | `TYPE_OF_DISPLAY.LEGEND` | Object | - | Optional |
| (4) | 变形详情(Deformation Details) | `TYPE_OF_DISPLAY.DEFORM` | Object | - | Optional |
| (5) | 显示选项详情(Display Option Details) | `TYPE_OF_DISPLAY.DISP_OPT` | Object | - | Optional |
| (6) | 对称模型镜像详情(Symmetric Model Mirror) | `TYPE_OF_DISPLAY.MIRRORED` | Object | - | Optional |
| (7) | 切割图(Cutting Diagram) | `TYPE_OF_DISPLAY.CUTTING_DIAGRAM` | Object | - | Optional |
| (8) | 切割面详情(Cutting Plane Detail) | `TYPE_OF_DISPLAY.CUTTING_PLANE` | Object | - | Optional |
| (9) | 施加荷载(Applied Loads, 移动荷载追踪) | `TYPE_OF_DISPLAY.APPLIED_LOADS` | Object | - | Optional |
| (10) | 等值面详情(IsoSurface Detail) | `TYPE_OF_DISPLAY.ISO_SURFACE` | Object | - | Optional |
| (11) | 显示未变形形状(Display Undeformed Shape) | `TYPE_OF_DISPLAY.UNDEFORMED` | Object | - | Optional |
| (12) | 箭头比例系数(Arrow Scale Factor) | `TYPE_OF_DISPLAY.ARROW_SCALE_FACTOR` | Number | 1 | Optional |
| (13) | 当前步位移 | `TYPE_OF_DISPLAY.OPT_CUR_STEP_DISPLACEMENT` | Boolean | false | Optional |
| (14) | 阶段/步骤实际位移 | `TYPE_OF_DISPLAY.OPT_STAGE_STEP_REAL_DISPLACEMENT` | Boolean | false | Optional |
| (15) | 包含预拱度位移 | `TYPE_OF_DISPLAY.OPT_INCLUDING_CAMBER_DISPLACEMENT` | Boolean | false | Optional |
| (16) | 当前步力(Current Step Force) | `TYPE_OF_DISPLAY.OPT_CUR_STEP_FORCE` | Boolean | false | Optional |
| (17) | 屈服点(Yield Point) | `TYPE_OF_DISPLAY.YIELD_POINT` | Object | - | Optional |
| (18) | 包含冲击系数(Include Impact Factor) | `TYPE_OF_DISPLAY.OPT_INCLUDE_IMPACT_FACTOR` | Boolean | false | Optional |
| (19) | 振型(Mode Shape) | `TYPE_OF_DISPLAY.MODE_SHAPE` | Object | - | Optional |
| (20) | 比例系数(Scale Factor) | `TYPE_OF_DISPLAY.SCALE_FACTOR` | Number | 1 | Optional |
| (21) | 三次插值(Cubic Interpolation) | `TYPE_OF_DISPLAY.OPT_CUBIC_INTERPOLATION` | Boolean | false | Optional |
| (22) | 三次插值系数(Cubic Interpolation Factor) | `TYPE_OF_DISPLAY.CUBIC_INTERPOLATION_FACTOR` | Number | 0.5 | Optional |

#### 2) Contour Details — `TYPE_OF_DISPLAY.CONTOUR`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 云图详情 | `CONTOUR` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `CONTOUR.OPT_CHECK` | Boolean | false | Optional |
| (2) | 云图颜色数量 (6 / 12 / 18 / 24) | `CONTOUR.NUM_OF_COLOR` | Integer | 12 | Optional |
| (3) | 颜色类型 (V→R→G→B: `"vrgb"`, R→G→B: `"rgb"`, R→B→G: `"rbg"`, Gray Scaled: `"gray scaled"`) | `CONTOUR.COLOR_TYPE` | String | `"vrgb"` | Optional |
| (4) | 云图表达选项 | `CONTOUR.OPTIONS` | Object | - | Optional |
| i. | 填充方式 (Contour Fill: true / 仅绘制线条: false) | `CONTOUR.OPTIONS.CONTOUR_FILL` | Boolean | true | Optional |
| ii. | 渐变填充 (`CONTOUR_FILL` 为 true 时) | `CONTOUR.OPTIONS.GRADIENT_FILL` | Boolean | false | Optional |

> Schema `enum` 定义值：`COLOR_TYPE` = `["vrgb", "rgb", "brg", "grayscaled"]` (与 Specifications 的标注不一致，以 Specifications 为准的取值是 `"vrgb"`/`"rgb"`/`"rbg"`/`"gray scaled"`)。

#### 3) Values Output Details — `TYPE_OF_DISPLAY.VALUES`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 数值输出详情 | `VALUES` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `VALUES.OPT_CHECK` | Boolean | false | Optional |
| (2) | 指数/固定记法选择 (指数: true / 固定: false) | `VALUES.VALUE_EXP` | Boolean | false | Optional |
| (3) | 小数点后位数 | `VALUES.DECIMAL_PT` | Integer | 0 | Optional |
| (4) | 数值方向(0~180，以 15 为步长递增) | `VALUES.SET_ORIENT` | Integer | 0 | Optional |
| (5) | 激活 "MinMax Only" | `VALUES.MINMAX_ONLY` | Object | - | Optional |
| i. | MinMax 类型 (Min.&Max.: `"Min & Max"`, Abs Max.: `"Abs Max"`, Max: `"Max"`, Min: `"Min"`) | `VALUES.MINMAX_ONLY.MAXMIN` | String | `"Min & Max"` | Optional |
| ii. | 限值比例(Limit Scale, 0~100) | `VALUES.MINMAX_ONLY.LIMIT_SCALE` | Integer | 0 | Optional |

> Schema `enum` 定义值：`MAXMIN` = `["Min&Max", "AbsMax", "Max", "Min"]`。

#### 4) Legend Details — `TYPE_OF_DISPLAY.LEGEND`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 图例详情 | `LEGEND` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `LEGEND.OPT_CHECK` | Boolean | false | Optional |
| (2) | 图例位置 (右侧: `"right"`, 左侧: `"left"`) | `LEGEND.POSITION` | String | `"left"` | Optional |
| (3) | 指数/固定记法选择 (指数: true / 固定: false) | `LEGEND.VALUE_EXP` | Boolean | true | Optional |
| (4) | 小数点后位数 (`VALUE_EXP` 为 false 时) | `LEGEND.DECIMAL_PT` | Integer | 0 | Optional |

#### 5) Deformation Details — `TYPE_OF_DISPLAY.DEFORM`

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 变形详情 | `DEFORM` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `DEFORM.OPT_CHECK` | Boolean | false | Optional |
| (2) | 变形比例系数(位移放大/缩小) | `DEFORM.SCALE_FACTOR` | Number | 0 | Optional |
| (3) | 变形类型 (Real Deform.: true / Nodal Deform: false) | `DEFORM.REAL_DEFORM` | Boolean | false | Optional |
| (4) | 相对变形(Relative Deformation) | `DEFORM.REL_DISP` | Boolean | false | Optional |
| (5) | 实际结构变形 (不缩放显示: true / 自动缩放: false) | `DEFORM.REAL_DISP` | Boolean | false | Optional |

#### 6) Display Option Details — `TYPE_OF_DISPLAY.DISP_OPT`

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 显示选项详情 | `DISP_OPT` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `DISP_OPT.OPT_CHECK` | Boolean | false | Optional |
| (2) | 在单元中心放置云图 (显示: true / 隐藏: false) | `DISP_OPT.ELEMENT_CENTER` | Boolean | false | Optional |
| (3) | 选择显示最大值/单元中心值 (最大值: true / 单元中心值: false) | `DISP_OPT.VALUE_MAX` | Boolean | false | Optional |

#### 7) Symmetric Model Mirror Detail — `TYPE_OF_DISPLAY.MIRRORED`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 对称模型镜像详情 | `MIRRORED` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `MIRRORED.OPT_CHECK` | Boolean | false | Optional |
| (2) | 半模型镜像(Half) | `MIRRORED.MIRROR_BY_1` | Object | - | Required |
| i. | 镜像方向(Half) (XY-Plane at Z: `"XY"`, YZ-Plane at X: `"YZ"`, XZ-Plane at Y: `"XZ"`) | `MIRRORED.MIRROR_BY_1.DIRECTION` | String | - | Required |
| ii. | 镜像偏移距离(Half) | `MIRRORED.MIRROR_BY_1.OFFSET` | Number | - | Required |
| (3) | 1/4 模型镜像(Quarter) | `MIRRORED.MIRROR_BY_2` | Object | - | Optional |
| i. | 镜像方向(Quarter) (`"XY"` / `"YZ"` / `"XZ"`) | `MIRRORED.MIRROR_BY_2.DIRECTION` | String | - | Required |
| ii. | 镜像偏移距离(Quarter) | `MIRRORED.MIRROR_BY_2.OFFSET` | Number | - | Required |

#### 8) Cutting Diagram — `TYPE_OF_DISPLAY.CUTTING_DIAGRAM`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 切割图 | `CUTTING_DIAGRAM` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `CUTTING_DIAGRAM.OPT_CHECK` | Boolean | false | Optional |
| (2) | 切割模式 (Cutting Line: `"line"`, Cutting Plane: `"plane"`) | `CUTTING_DIAGRAM.CUTTING_MODE` | String | `"line"` | Optional |
| (3) | 切割线/切割面选择 (已定义的 Cutting Line 名称 ᶜᵁᵀᴸ⁾，或 Current UCS 平面 `"XY"`/`"XZ"`/`"YZ"`，或命名平面唯一键 db/NPLN) | `CUTTING_DIAGRAM.CUTTING_NAME` | Array[String] | - | Required |
| (4) | 板单元图形方向选项 (法线方向: true / 面内方向: false) | `CUTTING_DIAGRAM.NORMAL_TO_PLANE` | Boolean | true | Optional |
| (5) | 图形输出比例系数 | `CUTTING_DIAGRAM.SCALE_FACTOR` | Number | 0 | Optional |
| (6) | 图形反向表达 (Reverse: true / Normal: false) | `CUTTING_DIAGRAM.REVERSE` | Boolean | false | Optional |
| (7) | 以数值输出 (激活: true / 非激活: false) | `CUTTING_DIAGRAM.VALUE_OUTPUT` | Boolean | false | Optional |
| (8) | 仅显示最大/最小值 (`VALUE_OUTPUT` 为 true 时) | `CUTTING_DIAGRAM.MINMAX_ONLY` | Boolean | false | Optional |

> ᶜᵁᵀᴸ⁾ : 以 Cutting Line Function(db/CUTL) 定义的切割线。

#### 9) Cutting Plane Detail Dialog — `TYPE_OF_DISPLAY.CUTTING_PLANE`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 切割面详情 | `CUTTING_PLANE` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `CUTTING_PLANE.OPT_CHECK` | Boolean | false | Optional |
| (2) | 切割面选择 (Current UCS x-y: `"XY"`, x-z: `"XZ"`, y-z: `"YZ"`, 或命名平面唯一键 db/NPLN) | `CUTTING_PLANE.PLANE_NAME` | Array[String] | - | Required |
| (3) | 外轮廓绘制选项 (Free Edge: true / Free Face: false) | `CUTTING_PLANE.FREE_EDGE` | Boolean | true | Optional |

#### 10) Applied Loads (Moving Load Tracer Detail) — `TYPE_OF_DISPLAY.APPLIED_LOADS`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 施加荷载(移动荷载追踪)详情 | `APPLIED_LOADS` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `APPLIED_LOADS.OPT_CHECK` | Boolean | false | Optional |
| (2) | 荷载比例系数 | `APPLIED_LOADS.SCALE_FACTOR` | Number | 0 | Optional |
| (3) | 显示荷载值 (激活: true / 非激活: false) | `APPLIED_LOADS.OPT_LOAD_VALUES` | Boolean | false | Optional |
| (4) | 数值输出类型 (`OPT_LOAD_VALUES` 为 true 时 — 指数: `"Exponential"`, 固定: `"Fixed"`) | `APPLIED_LOADS.VALUE_TYPE` | String | `"Exponential"` | Optional |
| (5) | 数值输出小数位数 (`OPT_LOAD_VALUES` 为 true 时，0 以上) | `APPLIED_LOADS.VALUE_DECIMAL_PT` | Integer | 0 | Optional |

#### 11) IsoSurface Detail Dialog — `TYPE_OF_DISPLAY.ISO_SURFACE`

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 等值面(IsoSurface)详情 | `ISO_SURFACE` | Object | - | Optional |
| (1) | 显示类型控制 (显示: true / 隐藏: false) | `ISO_SURFACE.OPT_CHECK` | Boolean | false | Optional |
| (2) | 绘制多边形外轮廓 (激活: true / 非激活: false) | `ISO_SURFACE.DRAW_POLYLINE` | Boolean | false | Optional |
| (3) | 透明度(仅屏幕，最大 255 / 最小 0) | `ISO_SURFACE.TRANSPARENCY` | Number | 255 | Optional |
| (4) | 实体单元外轮廓高亮 (Free Face: true / Free Edge: false) | `ISO_SURFACE.FREE_EDGE` | Boolean | true | Optional |
| (5) | 选择应力显示值 | `ISO_SURFACE.VALUE_MODE` | Object | - | Optional |
| i. | 等值面取值类型 (Relative: `"relative"`, Values: `"values"`) | `ISO_SURFACE.VALUE_MODE.VALUE_TYPE` | String | `"relative"` | Optional |
| ii. | 等值面取值 (Relative Type: 最大 1 / 最小 0) | `ISO_SURFACE.VALUE_MODE.VALUE` | Array[Number] | - | Required |

### Request / Response JSON

**POST Request Body — Contour Details (梁单元图结果)**

```json
{
  "Argument": {
    "CURRENT_MODE": "beamdiagrams",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "PART": "total",
      "COMP": "Fx"
    },
    "DISPLAY_OPTIONS": {
      "FIDELITY": "Exact",
      "FILL": "line",
      "SCALE": 1.0
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "OPTIONS": {
          "GRADIENT_FILL": false,
          "CONTOUR_FILL": false
        }
      }
    },
    "OUTPUT_SECT_LOCATION": {
      "OPT_I": true,
      "OPT_CENTER_MID": true,
      "OPT_J": true
    }
  }
}
```

**POST Request Body — Values Output Details (反力结果)**

```json
{
  "Argument": {
    "CURRENT_MODE": "reactionforces/moments",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "COMP": "Fxyz",
      "OPT_LOCAL_CHECK": true
    },
    "TYPE_OF_DISPLAY": {
      "VALUES": {
        "OPT_CHECK": true,
        "DECIMAL_PT": 5,
        "VALUE_EXP": true,
        "MINMAX_ONLY": {
          "MAXMIN": "absmax",
          "LIMIT_SCALE": 5
        },
        "SET_ORIENT": 15
      },
      "ARROW_SCALE_FACTOR": 1.0
    }
  }
}
```

**POST Request Body — Deformation Details (变形 + 云图)**

```json
{
  "Argument": {
    "CURRENT_MODE": "beamdiagrams",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL"
    },
    "COMPONENTS": {
      "PART": "total",
      "COMP": "Fx"
    },
    "DISPLAY_OPTIONS": {
      "FIDELITY": "Exact",
      "FILL": "line",
      "SCALE": 1.0
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 6,
        "COLOR_TYPE": "rgb",
        "OPTIONS": {
          "GRADIENT_FILL": false,
          "CONTOUR_FILL": false
        }
      },
      "DEFORM": {
        "OPT_CHECK": true,
        "SCALE_FACTOR": 2.0,
        "REL_DISP": true,
        "REAL_DISP": true,
        "REAL_DEFORM": true
      }
    },
    "OUTPUT_SECT_LOCATION": {
      "OPT_I": true,
      "OPT_CENTER_MID": true,
      "OPT_J": true
    }
  }
}
```

**POST Request Body — Symmetric Model Mirror (平面/板应力)**

```json
{
  "Argument": {
    "CURRENT_MODE": "Plane-Stress/PlateStresses",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "SelfWeight",
      "STEP_INDEX": 1
    },
    "OPTIONS": {
      "LOCAL_UCS": {
        "TYPE": "UCS",
        "UCS_NAME": "CurrentUCS"
      },
      "AVERAGE_NODAL": {
        "TYPE": "Avg.Nodal"
      },
      "SURFACE": "Top"
    },
    "COMPONENTS": {
      "COMP": "Sig-eff"
    },
    "TYPE_OF_DISPLAY": {
      "MIRRORED": {
        "OPT_CHECK": true,
        "MIRROR_BY_1": {
          "DIRECTION": "YZ",
          "OFFSET": 3
        },
        "MIRROR_BY_2": {
          "DIRECTION": "XZ",
          "OFFSET": 5
        }
      }
    }
  }
}
```

**POST Request Body — IsoSurface Detail (实体应力)**

```json
{
  "Argument": {
    "CURRENT_MODE": "solidstresses",
    "LOAD_CASE_COMB": {
      "TYPE": "ST",
      "NAME": "DL",
      "STEP_INDEX": 1
    },
    "OPTIONS": {
      "LOCAL_UCS": {
        "TYPE": "UCS",
        "UCS_NAME": "CurrentUCS"
      },
      "AVERAGE_NODAL": {
        "TYPE": "Avg.Nodal"
      }
    },
    "COMPONENTS": {
      "COMP": "Sig-eff"
    },
    "TYPE_OF_DISPLAY": {
      "ISO_SURFACE": {
        "OPT_CHECK": true,
        "DRAW_POLYLINE": true,
        "FREE_EDGE": false,
        "TRANSPARENCY": 50,
        "VALUE_MODE": {
          "VALUE_TYPE": "relative",
          "VALUE": [0, 0.25, 0.5, 0.75, 1]
        }
      }
    }
  }
}
```

**POST Response Body**

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
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

# ── POST: 以数值 + 图例显示反力(Reaction)结果 ─────────────────
def show_reaction_values():
    payload = {
        "Argument": {
            "CURRENT_MODE": "reactionforces/moments",   # 结果模式：反力/弯矩
            "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DL"},
            "COMPONENTS": {"COMP": "Fxyz", "OPT_LOCAL_CHECK": True},
            "TYPE_OF_DISPLAY": {
                "VALUES": {
                    "OPT_CHECK": True,
                    "VALUE_EXP": True,
                    "DECIMAL_PT": 5,
                    "SET_ORIENT": 15,
                    "MINMAX_ONLY": {"MAXMIN": "AbsMax", "LIMIT_SCALE": 5}
                },
                "LEGEND": {"OPT_CHECK": True, "POSITION": "right", "VALUE_EXP": True, "DECIMAL_PT": 2},
                "ARROW_SCALE_FACTOR": 1.0
            }
        }
    }
    resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
    print("反力显示:", resp.status_code, resp.json())


# ── POST: 以云图 + 变形显示梁单元图结果 ──────────────
def show_beam_contour_with_deform():
    payload = {
        "Argument": {
            "CURRENT_MODE": "beamdiagrams",             # 结果模式：梁单元图
            "LOAD_CASE_COMB": {"TYPE": "ST", "NAME": "DL"},
            "COMPONENTS": {"PART": "total", "COMP": "Fx"},
            "DISPLAY_OPTIONS": {"FIDELITY": "Exact", "FILL": "line", "SCALE": 1.0},
            "TYPE_OF_DISPLAY": {
                "CONTOUR": {
                    "OPT_CHECK": True,
                    "NUM_OF_COLOR": 6,
                    "COLOR_TYPE": "rgb",
                    "OPTIONS": {"CONTOUR_FILL": False, "GRADIENT_FILL": False}
                },
                "DEFORM": {
                    "OPT_CHECK": True,
                    "SCALE_FACTOR": 2.0,
                    "REAL_DEFORM": True,
                    "REL_DISP": True,
                    "REAL_DISP": True
                }
            },
            "OUTPUT_SECT_LOCATION": {"OPT_I": True, "OPT_CENTER_MID": True, "OPT_J": True}
        }
    }
    resp = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
    print("梁云图+变形显示:", resp.status_code, resp.json())


show_reaction_values()
show_beam_contour_with_deform()
```

---

## End-to-End Workflow

以下为将分析结果连同视点·激活·显示选项一起截图为图像的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 确认选择状态 ─────────────────────────────────────────
r1 = requests.get(f"{BASE_URL}/view/SELECT", headers=HEADERS)
print(f"STEP1 SELECT: {r1.status_code}, {r1.json().get('SELECT', {})}")

# ── STEP 2: 设置视点 ──────────────────────────────────────────────
r2 = requests.post(f"{BASE_URL}/view/ANGLE",
                   json={"Argument": {"HORIZONTAL": 30, "VERTICAL": 15}}, headers=HEADERS)
print(f"STEP2 ANGLE: {r2.status_code}")

# ── STEP 3: 仅激活特定组 ─────────────────────────────────────
r3 = requests.post(f"{BASE_URL}/view/ACTIVE",
                   json={"Argument": {"ACTIVE_MODE": "Identity",
                                      "IDENTITY_TYPE": "Group",
                                      "IDENTITY_LIST": ["Girder"]}}, headers=HEADERS)
print(f"STEP3 ACTIVE: {r3.status_code}")

# ── STEP 4: 整合视点·激活·显示·结果图形进行图像截图 ─────
capture_payload = {
    "Argument": {
        "SET_MODE": "post",
        "EXPORT_PATH": "C:\\MIDAS\\report\\girder_moment.jpg",
        "WIDTH": 1600, "HEIGHT": 900,
        "ANGLE": {"HORIZONTAL": 30, "VERTICAL": 15},
        "ACTIVE": {"ACTIVE_MODE": "Identity", "IDENTITY_TYPE": "Group", "IDENTITY_LIST": ["Girder"]},
        "DISPLAY": {"PERSPECTIVE": True, "ZOOM_LEVEL": 100},
        "RESULT_GRAPHIC": {
            "CURRENT_MODE": "beam diagrams",
            "LOAD_CASE_COMB": {"TYPE": "CB", "NAME": "cLCB1"},
            "COMPONENTS": {"PART": "total", "COMP": "My"},
            "TYPE_OF_DISPLAY": {"CONTOUR": {"OPT_CHECK": True}, "LEGEND": {"OPT_CHECK": True}}
        }
    }
}
r4 = requests.post(f"{BASE_URL}/view/CAPTURE", json=capture_payload, headers=HEADERS)
print(f"STEP4 CAPTURE: {r4.status_code}")
```
