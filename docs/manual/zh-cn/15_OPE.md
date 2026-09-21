# 15. OPE

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../15_OPE.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

`OPE`(Operation) 部分用于控制 GUI 或预处理计算值，处理**不存入 DB 的数据**。请求体以 `"Argument"` 键起始，大多以 `POST` 单一方法运行(部分查询型 Endpoint 也支持 `GET`)。

---

## Endpoint 列表

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/ope/PROJECTSTATUS`](#1-opeprojectstatus--project-status) | 查询项目现状 | GET |
| 2 | [`/ope/DIVIDEELEM`](#2-opedivideelem--divide-elements) | 单元划分 | POST |
| 3 | [`/ope/SECTPROP`](#3-opesectprop--section-properties-calculation-results) | 截面特性值计算结果 | GET |
| 4 | [`/ope/USLC`](#4-opeuslc--using-load-combinations) | 设置使用荷载组合 | POST |
| 5 | [`/ope/LINEBMLD`](#5-opelinebmld--line-beam-load) | 生成线性梁单元荷载 | POST |
| 6 | [`/ope/AUTOMESH`](#6-opeautomesh--auto-mesh-planar-area) | 平面区域自动划分网格 | POST |
| 7 | [`/ope/SSPS`](#7-opessps--surface-spring) | 面弹簧 → 点弹簧/弹性连接转换 | POST |
| 8 | [`/ope/EDMP`](#8-opeedmp--change-property) | 构件特性变更(收缩·徐变用) | POST |
| 9 | [`/ope/STOR`](#9-opestor--story-calculation) | 楼层计算选项 | POST |
| 10 | [`/ope/STORY_PARAM`](#10-opestory_param--story-check-parameter) | 楼层审查参数 | GET, POST |
| 11 | [`/ope/STORY_IRR_PARAM`](#11-opestory_irr_param--story-irregularity-check-parameter) | 楼层不规则性审查参数 | GET, POST |
| 12 | [`/ope/STORYPROP`](#12-opestoryprop--story-properties) | 楼层属性结果 | POST |
| 13 | [`/ope/MEMB`](#13-opememb--member-assignment) | 构件(Member)指派 | POST |
| 14 | [`/ope/GUSTFACTOR`](#14-opegustfactor--gust-factor-calculator) | 阵风影响系数计算器 | POST |
| 15 | [`/ope/LCOM-GEN`](#15-opelcom-gen--load-combination-general--kds2022--aik-src2k) | 荷载组合(一般)自动生成 | POST |
| 16 | [`/ope/LCOM-CONC`](#16-opelcom-conc--load-combination-concrete--kds-41-202022) | 荷载组合(混凝土)自动生成 | POST |
| 17 | [`/ope/LCOM-STEEL`](#17-opelcom-steel--load-combination-steel--kds-41-302022) | 荷载组合(钢结构)自动生成 | POST |
| 18 | [`/ope/LCOM-SRC`](#18-opelcom-src--load-combination-src--kds-41-src2022--aik-src2k) | 荷载组合(SRC)自动生成 | POST |
| 19 | [`/ope/GSBG`](#19-opegsbg--bridge-girder-diagram-image-generation) | 桥梁主梁图图像生成 | POST |

> **参考：** 依据 `DGNCODE` 取值，`/ope/LCOM-GEN`、`/ope/LCOM-SRC` 支持 **KDS:2022 系列**与 **AIK-SRC2K 系列**两种模式。本文以 KDS:2022 模式为主详细说明，AIK-SRC2K 变体另行一并标注。

---

## 1. `/ope/PROJECTSTATUS` — Project Status

> **功能：** 查询当前项目各类数据(节点·单元·材料·荷载工况等)的数量现状。不写入 DB，仅返回实时统计结果。

### Input URI

```
{base url}/ope/PROJECTSTATUS
```

### Active Methods

`GET`

### Response JSON

```json
{
  "PROJECTSTATUS": {
    "HEAD": ["Name", "Count", "LastNo."],
    "DATA": [
      ["StructureType", "1", "0"],
      ["NamedUCS", "0", "0"],
      ["NamedPlane", "0", "0"],
      ["LineGrid", "0", "0"],
      ["Group", "3", "0"],
      ["BoundaryGroup", "0", "0"],
      ["LoadGroup", "0", "0"],
      ["Node", "69", "69"],
      ["Element", "164", "164"],
      ["Material", "1", "1"],
      ["Section", "31", "9999"],
      ["Thickness", "0", "0"],
      ["Support", "24", "0"],
      ["NodalMass", "69", "0"]
    ],
    "HEAD_LOAD": ["Name", "Count"],
    "DATA_LOAD": [
      ["StaticLoadCase", "9"],
      ["SelfWeight", "2"],
      ["NodalLoad", "45"],
      ["BeamLoad", "76"],
      ["SpectrumFunction", "1"],
      ["SpectrumLoad", "2"],
      ["LoadComb(Concrete)", "37"]
    ]
  }
}
```

### Parameters

为仅响应(GET)的 Endpoint，没有请求体。

| No. | 说明 | Key | 值类型 |
|-----|------|-----|-----------|
| 1 | 模型数据现状表头 (Name, Count, LastNo.) | `"HEAD"` | Array [String] |
| 2 | 模型数据现状列表 (结构类型·节点·单元·材料·截面·支座等) | `"DATA"` | Array [Array] |
| 3 | 荷载数据现状表头 (Name, Count) | `"HEAD_LOAD"` | Array [String] |
| 4 | 荷载数据现状列表 (荷载工况·自重·节点荷载·梁单元荷载·反应谱·荷载组合等) | `"DATA_LOAD"` | Array [Array] |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── GET: 查询项目现状 ────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/PROJECTSTATUS", headers=HEADERS)
status = resp.json().get("PROJECTSTATUS", {})

print("=== 模型数据现状 ===")
for row in status.get("DATA", []):
    name, count, last_no = row
    if int(count) > 0:
        print(f"  {name}: {count} 个 (最终编号 {last_no})")

print("\n=== 荷载数据现状 ===")
for row in status.get("DATA_LOAD", []):
    name, count = row
    if int(count) > 0:
        print(f"  {name}: {count} 个")
```

---

## 2. `/ope/DIVIDEELEM` — Divide Elements

> **功能：** 将指定单元(线·平面·实体)以等分、非等分、比例分、平行支撑、按节点划分等多种方式细分。

### Input URI

```
{base url}/ope/DIVIDEELEM
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "DIVIDEELEM": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "TARGETS": { "type": "array", "items": { "type": "integer" } },
          "START_NUMBER": {
            "type": "object",
            "properties": {
              "NODE_NUMBER": {
                "type": "object",
                "properties": {
                  "NUMBER_OPTION": { "type": "string", "enum": ["Smallest", "Largest", "User"] },
                  "USER_NUM": { "type": "integer" }
                }
              },
              "ELEM_NUMBER": {
                "type": "object",
                "properties": {
                  "NUMBER_OPTION": { "type": "string", "enum": ["Smallest", "Largest", "User"] },
                  "USER_NUM": { "type": "integer" }
                }
              }
            }
          },
          "DIVIDE": {
            "type": "object",
            "properties": {
              "ELEM_TYPE": { "type": "string", "enum": ["Frame", "Wall", "Planar", "Solid"] },
              "DIV_METHOD": { "type": "string", "enum": ["Equal", "Unequal", "ParametricUnequal", "ParallelBracing", "DividebyNode"] },
              "OPTION": {
                "type": "object",
                "properties": {
                  "EQUAL_OPTION": {
                    "type": "object",
                    "properties": {
                      "NUM_X": { "type": "integer" },
                      "NUM_Y": { "type": "integer" },
                      "NUM_Z": { "type": "integer" }
                    }
                  },
                  "UNEQUAL_OPTION": {
                    "type": "object",
                    "properties": {
                      "DIST_X": { "type": "string" },
                      "DIST_Y": { "type": "string" },
                      "DIST_Z": { "type": "string" }
                    }
                  },
                  "PARAMETRIC_OPTION": {
                    "type": "object",
                    "properties": {
                      "RATIO_X": { "type": "string" },
                      "RATIO_Y": { "type": "string" },
                      "RATIO_Z": { "type": "string" }
                    }
                  },
                  "PARALLEL_OPTION": {
                    "type": "object",
                    "properties": {
                      "NUM_OF_DIVISIONS": { "type": "integer" },
                      "MAIN_POST_ELEM": { "type": "array", "items": { "type": "integer" } }
                    }
                  },
                  "BY_NODE_OPTION": {
                    "type": "object",
                    "properties": {
                      "ELEM_NUM": { "type": "integer" },
                      "NODE_NUM": { "type": "integer" }
                    }
                  }
                }
              },
              "SUBDIVIDE_ELEM": { "type": "boolean" },
              "MERGE_DUPLICATE_NODES": {
                "type": "object",
                "properties": {
                  "OPT_CHECK": { "type": "boolean" },
                  "TOLERANCE": { "type": "number" }
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

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 划分目标单元 ID | `"TARGETS"` | Array [Integer] | — | Optional |
| 2 | 起始节点/单元编号 | `"START_NUMBER"` | Object | System | Optional |
| 2-1 | └ 节点编号选项 · 最小未使用: `"Smallest"` / 最大+1: `"Largest"` / 用户指定: `"User"` | `START_NUMBER.NODE_NUMBER.NUMBER_OPTION` | String | — | Optional |
| 2-2 | └ 用户指定的节点编号 (`NUMBER_OPTION="User"` 时) | `START_NUMBER.NODE_NUMBER.USER_NUM` | Integer | — | Optional |
| 2-3 | └ 单元编号选项 (与节点相同的 enum) | `START_NUMBER.ELEM_NUMBER.NUMBER_OPTION` | String | — | Optional |
| 2-4 | └ 用户指定的单元编号 | `START_NUMBER.ELEM_NUMBER.USER_NUM` | Integer | — | Optional |
| 3 | 划分设置 | `"DIVIDE"` | Object | — | **Required** |
| 3-1 | └ 单元类型 · 线单元: `"Frame"` / 墙: `"Wall"` / 平面: `"Planar"` / 实体: `"Solid"` | `DIVIDE.ELEM_TYPE` | String | — | **Required** |
| 3-2 | └ 划分方法 · 等分: `"Equal"` / 非等分: `"Unequal"` / 比例分: `"ParametricUnequal"` / 平行支撑: `"ParallelBracing"` / 按节点: `"DividebyNode"` | `DIVIDE.DIV_METHOD` | String | — | **Required** |
| 3-3 | └ 划分选项 (按 DIV_METHOD 取对应下级对象之一) | `DIVIDE.OPTION` | Object | — | **Required** |
| — | Equal: X/Y/Z 方向划分数 (仅 Frame=X, Planar=X,Y, Wall=X,Z, Solid=X,Y,Z) | `OPTION.EQUAL_OPTION.{NUM_X,NUM_Y,NUM_Z}` | Integer | — | **Required** |
| — | Unequal: X/Y/Z 方向非等分距离字符串 (例: `"3@2.0"`) | `OPTION.UNEQUAL_OPTION.{DIST_X,DIST_Y,DIST_Z}` | String | — | **Required** |
| — | ParametricUnequal: X/Y/Z 方向比例字符串 (例: `"3@0.3"`) | `OPTION.PARAMETRIC_OPTION.{RATIO_X,RATIO_Y,RATIO_Z}` | String | — | **Required** |
| — | ParallelBracing: 划分数 / 基准立柱(Post)单元列表 | `OPTION.PARALLEL_OPTION.{NUM_OF_DIVISIONS,MAIN_POST_ELEM}` | Integer/Array | — | **Required** |
| — | DividebyNode: 目标单元号 / 划分基准节点号 | `OPTION.BY_NODE_OPTION.{ELEM_NUM,NODE_NUM}` | Integer | — | **Required** |
| 4 | 是否重分线单元 | `DIVIDE.SUBDIVIDE_ELEM` | Boolean | — | Optional |
| 5 | 重复节点合并 | `DIVIDE.MERGE_DUPLICATE_NODES` | Object | — | Optional |
| 5-1 | └ 是否启用 | `MERGE_DUPLICATE_NODES.OPT_CHECK` | Boolean | — | Optional |
| 5-2 | └ 合并容差 | `MERGE_DUPLICATE_NODES.TOLERANCE` | Number | — | Optional |

### Request / Response JSON

**POST Request Body — Frame 等分**

```json
{
  "Argument": {
    "TARGETS": [1],
    "DIVIDE": {
      "ELEM_TYPE": "Frame",
      "DIV_METHOD": "Equal",
      "OPTION": { "EQUAL_OPTION": { "NUM_X": 10 } }
    }
  }
}
```

**POST Request Body — Planar 非等分**

```json
{
  "Argument": {
    "TARGETS": [1],
    "DIVIDE": {
      "ELEM_TYPE": "Planar",
      "DIV_METHOD": "Unequal",
      "OPTION": { "UNEQUAL_OPTION": { "DIST_X": "2@2.5", "DIST_Y": "2@3.0" } }
    }
  }
}
```

**POST Request Body — Frame 平行支撑**

```json
{
  "Argument": {
    "DIVIDE": {
      "ELEM_TYPE": "Frame",
      "DIV_METHOD": "ParallelBracing",
      "OPTION": { "PARALLEL_OPTION": { "NUM_OF_DIVISIONS": 3, "MAIN_POST_ELEM": [1, 3] } }
    }
  }
}
```

**POST Response Body**

```json
{
  "DIVIDEELEM": {
    "1": {
      "TYPE": "PLATE",
      "MATL": 1,
      "SECT": 1,
      "NODE": [1, 5, 8, 7, 0, 0, 0, 0],
      "ANGLE": 0,
      "STYPE": 1
    }
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

# ── POST: 将 Frame 单元 10 等分 ──────────────────────────────────────
payload = {
    "Argument": {
        "TARGETS": [1],
        "DIVIDE": {
            "ELEM_TYPE": "Frame",
            "DIV_METHOD": "Equal",
            "OPTION": {"EQUAL_OPTION": {"NUM_X": 10}}
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/DIVIDEELEM", json=payload, headers=HEADERS)
print("POST (Equal):", resp.status_code, resp.json())

# ── POST: Solid 单元比例划分 ──────────────────────────────────────
payload2 = {
    "Argument": {
        "TARGETS": [1],
        "DIVIDE": {
            "ELEM_TYPE": "Solid",
            "DIV_METHOD": "ParametricUnequal",
            "OPTION": {
                "PARAMETRIC_OPTION": {
                    "RATIO_X": "3@0.3",
                    "RATIO_Y": "4@0.2",
                    "RATIO_Z": "0.1,0.2,0.3"
                }
            }
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/DIVIDEELEM", json=payload2, headers=HEADERS)
print("POST (ParametricUnequal):", resp.status_code, resp.json())
```

---

## 3. `/ope/SECTPROP` — Section Properties Calculation Results

> **功能：** 查询已注册截面的计算截面特性值(面积·惯性矩·截面模量等)。

### Input URI

```
{base url}/ope/SECTPROP
```

### Active Methods

`GET`

### Response JSON

```json
{
  "SECTPROP": {
    "1": {
      "HEAD": ["Property", "Value", "Unit"],
      "DATA": [
        ["Area", "0.011980", "m2"],
        ["Asy", "0.007500", "m2"],
        ["Asz", "0.003000", "m2"],
        ["Ixx", "0.000001", "m4"],
        ["Iyy", "0.000204", "m4"],
        ["Izz", "0.000068", "m4"],
        ["Cyp", "0.150000", "m"],
        ["Cym", "0.150000", "m"],
        ["Czp", "0.150000", "m"],
        ["Czm", "0.150000", "m"],
        ["Qyb", "0.073237", "m2"],
        ["Qzb", "0.011250", "m2"],
        ["Peri:O", "1.780000", "m"],
        ["Peri:I", "0.000000", "m"],
        ["Center:y", "0.150000", "m"],
        ["Center:z", "0.150000", "m"],
        ["y1", "-0.150000", "m"],
        ["z1", "0.150000", "m"],
        ["y2", "0.150000", "m"],
        ["z2", "0.150000", "m"],
        ["y3", "0.150000", "m"],
        ["z3", "-0.150000", "m"],
        ["y4", "-0.150000", "m"],
        ["z4", "-0.150000", "m"]
      ]
    }
  }
}
```

### Parameters

为仅响应(GET) 的 Endpoint。Key(`"1"`)为截面 ID。

| No. | 说明 | Key | 值类型 |
|-----|------|-----|-----------|
| 1 | 结果表头 (Property, Value, Unit) | `"HEAD"` | Array [String] |
| 2 | 截面特性值列表 (Area, Asy, Asz, Ixx, Iyy, Izz, Cyp/Cym/Czp/Czm, Qyb, Qzb, Peri:O/I, Center:y/z, 顶点坐标 y1~y4/z1~z4 等) | `"DATA"` | Array [Array] |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── GET: 查询全部截面特性值 ─────────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/SECTPROP", headers=HEADERS)
props = resp.json().get("SECTPROP", {})

for sect_id, result in props.items():
    print(f"[截面 {sect_id}]")
    for row in result["DATA"]:
        name, value, unit = row
        print(f"  {name} = {value} {unit}")
```

---

## 4. `/ope/USLC` — Using Load Combinations

> **功能：** 将已定义的荷载组合连同设计用前缀指定用于钢结构/混凝土/SRC 设计，并选择各荷载组合中包含的荷载种类。

### Input URI

```
{base url}/ope/USLC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "USLC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "PREFIX": { "type": "string" },
          "POSITION": { "type": "string", "enum": ["STEEL", "CONC", "SRC"] },
          "LCOM_LIST": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "TYPE": { "type": "string", "enum": ["GEN", "STEEL", "CONC", "SRC", "STLCOMP", "SEISMIC"] },
                "NAME": { "type": "string" }
              }
            }
          },
          "LOADS": {
            "type": "object",
            "properties": {
              "SELF_WEIGHT": { "type": "boolean", "default": true },
              "NODAL_BODY_FROCE": { "type": "boolean", "default": true },
              "NODAL_LOAD": { "type": "boolean", "default": true },
              "SPECIFIED_DISPLACEMENT": { "type": "boolean", "default": true },
              "BEAM_LOAD": { "type": "boolean", "default": true },
              "FLOOR_LOAD": { "type": "boolean", "default": true },
              "FINISHING_MATERIAL_LOAD": { "type": "boolean", "default": true },
              "PRESSURE_LOAD": { "type": "boolean", "default": true },
              "PLANE_LOAD": { "type": "boolean", "default": true },
              "SYSTEM_TEMPERATURE": { "type": "boolean", "default": true },
              "NODAL_TEMPERATURE": { "type": "boolean", "default": true },
              "ELEMENT_TEMPERATURE": { "type": "boolean", "default": true },
              "TEMPERATURE_GRADIENT": { "type": "boolean", "default": true },
              "BEAM_SECTION_TEMPERATURE": { "type": "boolean", "default": true },
              "PRESTRESS_LOAD": { "type": "boolean", "default": true },
              "PRETENSION_LOAD": { "type": "boolean", "default": true },
              "TENDON_PRESTRESS_LOAD": { "type": "boolean", "default": true }
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
| 1 | 荷载工况/设计组合名称前缀 | `"PREFIX"` | String | System | Optional |
| 2 | 设计组合生成位置 · 钢结构: `"STEEL"` / 混凝土: `"CONC"` / SRC: `"SRC"` | `"POSITION"` | String | — | **Required** |
| 3 | 已选组合列表 | `"LCOM_LIST"` | Array [Object] | — | **Required** |
| 3-1 | └ 荷载组合类型 · 一般: `"GEN"` / 钢结构: `"STEEL"` / 混凝土: `"CONC"` / SRC: `"SRC"` / 钢组合主梁: `"STLCOMP"` / 抗震: `"SEISMIC"` | `LCOM_LIST[].TYPE` | String | — | **Required** |
| 3-2 | └ 荷载组合名称 | `LCOM_LIST[].NAME` | String | — | **Required** |
| 4 | 所选荷载种类 | `"LOADS"` | Object | — | Optional |
| 4-1 | └ 自重 | `LOADS.SELF_WEIGHT` | Boolean | `true` | Optional |
| 4-2 | └ 节点体积力 | `LOADS.NODAL_BODY_FROCE` | Boolean | `true` | Optional |
| 4-3 | └ 节点荷载 | `LOADS.NODAL_LOAD` | Boolean | `true` | Optional |
| 4-4 | └ 指定位移 | `LOADS.SPECIFIED_DISPLACEMENT` | Boolean | `true` | Optional |
| 4-5 | └ 梁单元荷载 | `LOADS.BEAM_LOAD` | Boolean | `true` | Optional |
| 4-6 | └ 楼面荷载 | `LOADS.FLOOR_LOAD` | Boolean | `true` | Optional |
| 4-7 | └ 装修层荷载 | `LOADS.FINISHING_MATERIAL_LOAD` | Boolean | `true` | Optional |
| 4-8 | └ 压力荷载 | `LOADS.PRESSURE_LOAD` | Boolean | `true` | Optional |
| 4-9 | └ 平面荷载 | `LOADS.PLANE_LOAD` | Boolean | `true` | Optional |
| 4-10 | └ 系统温度 | `LOADS.SYSTEM_TEMPERATURE` | Boolean | `true` | Optional |
| 4-11 | └ 节点温度 | `LOADS.NODAL_TEMPERATURE` | Boolean | `true` | Optional |
| 4-12 | └ 单元温度 | `LOADS.ELEMENT_TEMPERATURE` | Boolean | `true` | Optional |
| 4-13 | └ 温度梯度 | `LOADS.TEMPERATURE_GRADIENT` | Boolean | `true` | Optional |
| 4-14 | └ 梁截面温度 | `LOADS.BEAM_SECTION_TEMPERATURE` | Boolean | `true` | Optional |
| 4-15 | └ 预应力荷载 | `LOADS.PRESTRESS_LOAD` | Boolean | `true` | Optional |
| 4-16 | └ 先张荷载 | `LOADS.PRETENSION_LOAD` | Boolean | `true` | Optional |
| 4-17 | └ 预应力束预应力荷载 | `LOADS.TENDON_PRESTRESS_LOAD` | Boolean | `true` | Optional |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "LCOM_LIST": [
      { "TYPE": "STEEL", "NAME": "sLCB1" }
    ],
    "PREFIX": "N",
    "POSITION": "STEEL",
    "LOADS": {
      "SELF_WEIGHT": true,
      "NODAL_BODY_FROCE": true,
      "NODAL_LOAD": true,
      "SPECIFIED_DISPLACEMENT": true,
      "BEAM_LOAD": true,
      "FLOOR_LOAD": true,
      "FINISHING_MATERIAL_LOAD": true,
      "PRESSURE_LOAD": true,
      "PLANE_LOAD": true,
      "SYSTEM_TEMPERATURE": true,
      "NODAL_TEMPERATURE": true,
      "ELEMENT_TEMPERATURE": true,
      "TEMPERATURE_GRADIENT": true,
      "BEAM_SECTION_TEMPERATURE": true,
      "PRESTRESS_LOAD": true,
      "PRETENSION_LOAD": true,
      "TENDON_PRESTRESS_LOAD": true
    }
  }
}
```

**POST Response Body**

```json
{
  "USLC": {
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

# ── POST: 指定钢结构设计荷载组合中使用的荷载 ────────────────────
payload = {
    "Argument": {
        "LCOM_LIST": [
            {"TYPE": "STEEL", "NAME": "sLCB1"},
            {"TYPE": "STEEL", "NAME": "sLCB2"}
        ],
        "PREFIX": "N",
        "POSITION": "STEEL",
        "LOADS": {
            "SELF_WEIGHT": True,
            "NODAL_LOAD": True,
            "BEAM_LOAD": True,
            "FLOOR_LOAD": True
            # 其余采用默认值(true)
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/USLC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 5. `/ope/LINEBMLD` — Line Beam Load

> **功能：** 将荷载作用的线(Line)用 2 个节点或所选单元定义，自动在该线穿过的构件上生成并分配集中/均布/梯形/曲线荷载。

### Input URI

```
{base url}/ope/LINEBMLD
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "LINEBMLD": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "LCNAME": { "type": "string" },
          "GROUP_NAME": { "type": "string" },
          "TYPE": { "type": "string" },
          "TARGET": {
            "type": "object",
            "properties": {
              "METHOD": { "type": "integer" },
              "ELEM": { "type": "array", "items": { "type": "integer" } },
              "NODE": { "type": "array", "items": { "type": "integer" } }
            }
          },
          "ECCEN": {
            "type": "object",
            "properties": {
              "USE": { "type": "boolean" },
              "TYPE": { "type": "integer" },
              "DIR": { "type": "string" },
              "I_END": { "type": "number" },
              "J_END": { "type": "number" },
              "USE_J_END": { "type": "boolean" }
            }
          },
          "ADD_H": {
            "type": "object",
            "properties": {
              "USE": { "type": "boolean" },
              "I_END": { "type": "number" },
              "J_END": { "type": "number" },
              "USE_J_END": { "type": "boolean" }
            }
          },
          "LOAD": {
            "type": "object",
            "properties": {
              "DIR": { "type": "string" },
              "USE_PROJECTION": { "type": "boolean" },
              "TYPE": { "type": "integer" },
              "D": { "type": "array", "items": { "type": "number" } },
              "P": { "type": "array", "items": { "type": "number" } },
              "A": { "type": "number" },
              "B": { "type": "number" },
              "C": { "type": "number" }
            }
          },
          "COPY": {
            "type": "object",
            "properties": {
              "USE": { "type": "boolean" },
              "AXIS": { "type": "string" },
              "DIST": { "type": "string" }
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
| 1 | 荷载工况名称 | `"LCNAME"` | String | — | **Required** |
| 2 | 荷载组名称 | `"GROUP_NAME"` | String | — | Optional |
| 3 | 荷载类型 · 集中荷载: `"CONLOAD"` / 集中弯矩: `"CONMOMENT"` / 均布荷载: `"UNILOAD"` / 均布弯矩: `"UNIMOMENT"` / 梯形荷载: `"TRALOAD"` / 梯形弯矩: `"TRAMOMENT"` / 均布压力: `"UNIPRESSURE"` / 梯形压力: `"TRAPRESSURE"` / 曲线荷载: `"CURVED"` | `"TYPE"` | String | — | **Required** |
| 4 | 荷载适用对象信息 | `"TARGET"` | Object | — | **Required** |
| 4-1 | └ 适用方法 · 荷载线上: `0` / 所选单元: `1` | `TARGET.METHOD` | Integer | — | **Required** |
| 4-2 | └ 适用对象单元列表 | `TARGET.ELEM` | Array [Integer] | — | **Required** |
| 4-3 | └ 荷载线定义节点 (2 个) | `TARGET.NODE` | Array [Integer, 2] | — | **Required** |
| 5 | 偏心选项(仅 `TYPE` 为 CONLOAD/UNILOAD/TRALOAD/CURVED 时可用) | `"ECCEN"` | Object | — | Optional |
| 5-1 | └ 启用 | `ECCEN.USE` | Boolean | `false` | — |
| 5-2 | └ 类型 · 形心: `0` / 偏心距: `1` | `ECCEN.TYPE` | Integer | — | — |
| 5-3 | └ 方向 · 局部y: `"LY"` / 局部z: `"LZ"` / 全局X: `"GX"` / 全局Y: `"GY"` / 全局Z: `"GZ"` | `ECCEN.DIR` | String | — | — |
| 5-4 | └ I 端偏心量 | `ECCEN.I_END` | Number | — | — |
| 5-5 | └ J 端偏心量(`USE_J_END=true` 时) | `ECCEN.J_END` | Number | — | — |
| 5-6 | └ J 端偏心启用 | `ECCEN.USE_J_END` | Boolean | — | — |
| 6 | 顶部附加高度选项(仅 `TYPE` 为 UNIPRESSURE/TRAPRESSURE 时可用) | `"ADD_H"` | Object | — | Optional |
| 6-1 | └ 启用 | `ADD_H.USE` | Boolean | `false` | — |
| 6-2 | └ I 端值 | `ADD_H.I_END` | Number | — | — |
| 6-3 | └ J 端值(`USE_J_END=true` 时) | `ADD_H.J_END` | Number | — | — |
| 6-4 | └ J 端启用 | `ADD_H.USE_J_END` | Boolean | — | — |
| 7 | 荷载值 | `"LOAD"` | Object | — | **Required** |
| 7-1 | └ 方向 · 局部x/y/z(`"LX"`/`"LY"`/`"LZ"`)，全局X/Y/Z(`"GX"`/`"GY"`/`"GZ"`); `UNIPRESSURE`/`TRAPRESSURE` 依 `ADD_H` 设置仅可用 `LY`/`LZ` | `LOAD.DIR` | String | — | **Required** |
| 7-2 | └ 是否投影 (METHOD=0→默认 false, METHOD=1→默认 true) | `LOAD.USE_PROJECTION` | Boolean | System | Optional |
| 7-3 | └ 距离类型(所有类型通用，含 `CURVED`) · 相对: `0` / 绝对: `1` | `LOAD.TYPE` | Integer | — | **Required** |
| 7-4 | └ 距离数组 [x1,x2,x3,x4] (`CURVED` 除外) | `LOAD.D` | Array [Number, 4] | — | **Required** |
| 7-5 | └ 大小数组 [P1,P2,P3,P4] (`CURVED` 除外) | `LOAD.P` | Array [Number, 4] | — | **Required** |
| 7-6 | └ 曲线方程系数 a (`CURVED` 专用) | `LOAD.A` | Number | — | **Required** |
| 7-7 | └ 曲线方程系数 b (`CURVED` 专用) | `LOAD.B` | Number | — | **Required** |
| 7-8 | └ 曲线方程系数 c (`CURVED` 专用) | `LOAD.C` | Number | — | **Required** |
| 8 | 复制选项 | `"COPY"` | Object | — | Optional |
| 8-1 | └ 启用 | `COPY.USE` | Boolean | `false` | — |
| 8-2 | └ 复制轴 · `"X"`/`"Y"`/`"Z"` | `COPY.AXIS` | String | — | — |
| 8-3 | └ 复制距离 (例: `"10@3.0"`) | `COPY.DIST` | String | — | — |

> ⚠️ 2026-08-26 确认 (article id `35994879160857`): `LOAD.TYPE`(7-3) 在旧版文档中写为 "`CURVED`
> 之外的所有类型"，但官方 Specifications 表中并无该例外，而是明确为适用于所有 `TYPE`
> 取值的公共字段，故予以更正。仅作为 `CURVED` 专用而被排除的是 `LOAD.D`/`LOAD.P`
> (7-4/7-5)，代之以 `LOAD.A`/`LOAD.B`/`LOAD.C`(7-6~7-8)。

### Request / Response JSON

**POST Request Body — 集中荷载**

```json
{
  "Argument": {
    "LCNAME": "CONLOAD_03",
    "GROUP_NAME": "LoadGroup1",
    "TYPE": "CONLOAD",
    "TARGET": { "METHOD": 0, "NODE": [23, 33] },
    "LOAD": {
      "DIR": "GZ",
      "TYPE": 1,
      "D": [0.75, 1.35, 1.95, 2.55],
      "P": [-1, -2, -3, -4]
    }
  }
}
```

**POST Request Body — 带偏心的集中荷载**

```json
{
  "Argument": {
    "LCNAME": "CONLOAD_14",
    "TYPE": "CONLOAD",
    "TARGET": { "METHOD": 0, "NODE": [56, 66] },
    "ECCEN": {
      "USE": true,
      "TYPE": 0,
      "DIR": "LZ",
      "I_END": -0.15,
      "J_END": 0.15,
      "USE_J_END": true
    },
    "LOAD": {
      "DIR": "GZ",
      "TYPE": 1,
      "D": [0.75, 1.35, 1.95, 2.55],
      "P": [-1, -2, -3, -4]
    }
  }
}
```

**POST Response Body**

```json
{
  "LINEBMLD": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "A",
          "GROUP_NAME": "",
          "CMD": "LINE",
          "TYPE": "CONLOAD",
          "DIRECTION": "GZ",
          "USE_PROJECTION": false,
          "USE_ECCEN": false,
          "D": [0.075, 0.135, 0.195, 0.255],
          "P": [-1, -2, -3, -4],
          "USE_ADDITIONAL": false,
          "ADDITIONAL_I_END": 0,
          "ADDITIONAL_J_END": 0,
          "USE_ADDITIONAL_J_END": false
        }
      ]
    }
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

# ── POST: 在节点线上生成梯形荷载 ───────────────────────────
payload = {
    "Argument": {
        "LCNAME": "TRALOAD_03",
        "GROUP_NAME": "LoadGroup1",
        "TYPE": "TRALOAD",
        "TARGET": {"METHOD": 0, "NODE": [23, 33]},
        "LOAD": {
            "DIR": "GZ",
            "USE_PROJECTION": True,
            "TYPE": 1,
            "D": [0.75, 1.35, 1.95, 2.55],
            "P": [-1, -2, -3, -4]
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/LINEBMLD", json=payload, headers=HEADERS)
print("POST (梯形):", resp.status_code, resp.json())

# ── POST: 均布荷载后沿 Y 轴方向复制 ──────────────────────────────
payload2 = {
    "Argument": {
        "LCNAME": "UNILOAD_17",
        "TYPE": "UNILOAD",
        "TARGET": {"METHOD": 0, "NODE": [78, 88]},
        "LOAD": {"DIR": "GZ", "TYPE": 0, "D": [0.25, 0.85], "P": [-3]},
        "COPY": {"USE": True, "AXIS": "Y", "DIST": "10@3.0"}
    }
}
resp = requests.post(f"{BASE_URL}/ope/LINEBMLD", json=payload2, headers=HEADERS)
print("POST (复制):", resp.status_code, resp.json())
```

---

## 6. `/ope/AUTOMESH` — Auto-Mesh Planar Area

> **功能：** 将节点·线单元·平面单元围成的区域自动划分为四边形/三角形网格，生成板(Plate)·平面应力·平面应变·轴对称单元。

### Input URI

```
{base url}/ope/AUTOMESH
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "AUTOMESH": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "MESHER": {
            "type": "object",
            "properties": {
              "METHOD": { "type": "string" },
              "TARGETS": { "type": "array", "items": { "type": "integer" } },
              "TYPE": { "type": "string" },
              "MESH_INNER_DOMAIN": { "type": "boolean" },
              "INCLUDE_INTERIOR_NODES": {
                "type": "object",
                "properties": {
                  "OPT_CHECK": { "type": "boolean" },
                  "OPTION": { "type": "string" },
                  "VALUE": { "type": "array", "items": { "type": "integer" } }
                }
              },
              "INCLUDE_INTERIOR_LINES": {
                "type": "object",
                "properties": {
                  "OPT_CHECK": { "type": "boolean" },
                  "OPTION": { "type": "string" },
                  "VALUE": { "type": "array", "items": { "type": "integer" } }
                }
              },
              "INCLUDE_BOUNDARY_CONNECTIVITY": { "type": "boolean" }
            }
          },
          "MESH_SIZE": {
            "type": "object",
            "properties": {
              "LENGTH": { "type": "integer" },
              "DIV": { "type": "integer" }
            }
          },
          "PROPERTY": {
            "type": "object",
            "properties": {
              "ELEMENT_TYPE": { "type": "string" },
              "ELEMENT_SUB_TYPE": {
                "type": "object",
                "properties": {
                  "TYPE": { "type": "string" },
                  "WITH_DRILLING_DOF": { "type": "boolean" }
                }
              },
              "MATERIAL": { "type": "integer" },
              "THICKNESS": { "type": "integer" }
            }
          },
          "DOMAIN_NAME": {
            "type": "object",
            "properties": { "NAME": { "type": "string" } }
          },
          "ADDITIONAL_OPTION": {
            "type": "object",
            "properties": {
              "DELETE_LINE_ELEM": { "type": "boolean" },
              "SUBDIVIDE_LINE_ELEM": { "type": "boolean" }
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
| 1 | 网格划分器设置 | `"MESHER"` | Object | — | **Required** |
| 1-1 | └ 自动网格方法 · 节点: `"Nodes"` / 线单元: `"LineElements"` / 平面单元: `"PlanarElements"` | `MESHER.METHOD` | String | `"LineElements"` | Optional |
| 1-2 | └ 网格目标单元/节点列表 | `MESHER.TARGETS` | Array [Integer] | — | **Required** |
| 1-3 | └ 网格形态 · 四边形: `"Quadrilateral"` / 四边形+三角形: `"Quadandtriangle"` / 三角形: `"Triangle"` | `MESHER.TYPE` | String | `"Quadrilateral"` | Optional |
| 1-4 | └ 是否生成内部域网格 | `MESHER.MESH_INNER_DOMAIN` | Boolean | `false` | Optional |
| 1-5 | └ 区域内节点考虑选项 | `MESHER.INCLUDE_INTERIOR_NODES` | Object | — | Optional |
| 1-5-a | 　└ 启用 | `INCLUDE_INTERIOR_NODES.OPT_CHECK` | Boolean | `true` | Optional |
| 1-5-b | 　└ 识别方式 · `"Auto"`/`"User"` | `INCLUDE_INTERIOR_NODES.OPTION` | String | `"Auto"` | Optional |
| 1-5-c | 　└ 包含的节点编号(User 时) | `INCLUDE_INTERIOR_NODES.VALUE` | Array [Integer] | — | **Required**(User 时) |
| 1-6 | └ 区域内线单元考虑选项 (结构与 1-5 相同) | `MESHER.INCLUDE_INTERIOR_LINES` | Object | — | Optional |
| 1-7 | └ 是否连接网格边界 | `MESHER.INCLUDE_BOUNDARY_CONNECTIVITY` | Boolean | `true` | Optional |
| 2 | 网格尺寸 | `"MESH_SIZE"` | Object | — | **Required** |
| 2-1 | └ 按长度基准 (不可与 `DIV` 同时使用) | `MESH_SIZE.LENGTH` | Number | — | **Required** |
| 2-2 | └ 按划分数基准 (不可与 `LENGTH` 同时使用) | `MESH_SIZE.DIV` | Number | — | **Required** |
| 3 | 单元属性 | `"PROPERTY"` | Object | — | **Required** |
| 3-1 | └ 单元类型 · `"Plate"`/`"PlaneStress"`/`"PlaneStrain"`/`"Axisymmetric"` | `PROPERTY.ELEMENT_TYPE` | String | `"Plate"` | Optional |
| 3-2 | └ 单元细分类型 | `PROPERTY.ELEMENT_SUB_TYPE` | Object | — | Optional |
| 3-2-a | 　└ 板厚度类型(`ELEMENT_TYPE="Plate"` 时) · `"Thick"`/`"Thin"` | `ELEMENT_SUB_TYPE.TYPE` | String | `"Thick"` | Optional |
| 3-2-b | 　└ 使用 Drilling DOF(`Plate`/`PlaneStress` 时) | `ELEMENT_SUB_TYPE.WITH_DRILLING_DOF` | Boolean | `true` | Optional |
| 3-3 | └ 材料编号 | `PROPERTY.MATERIAL` | Integer | — | **Required** |
| 3-4 | └ 厚度编号(`Plate`/`PlaneStress` 时) | `PROPERTY.THICKNESS` | Integer | — | Optional |
| 4 | 域名称 | `"DOMAIN_NAME"` | Object | — | **Required** |
| 4-1 | └ 名称 | `DOMAIN_NAME.NAME` | String | — | **Required** |
| 5 | 附加选项 | `"ADDITIONAL_OPTION"` | Object | — | Optional |
| 5-1 | └ 删除原线/边界单元 | `ADDITIONAL_OPTION.DELETE_LINE_ELEM` | Boolean | `false` | Optional |
| 5-2 | └ 重分原线/边界单元 | `ADDITIONAL_OPTION.SUBDIVIDE_LINE_ELEM` | Boolean | `true` | Optional |

> ⚠️ 2026-08-26 确认 (article id `35736427971225`): 官方 Specifications 表把 `MESHER.METHOD`/
> `MESHER.TYPE`/`PROPERTY.ELEMENT_TYPE` 的枚举值写成了便于阅读的加空格形式(例: `"Line Elements"`,
> `"Quad and Triangle"`, `"Plane Stress"`)，但实际 Request Example·Response 中使用的是
> 无空格的字面量(`"LineElements"`, `"Quadandtriangle"`, `"PlaneStress"`)。示例是真正可
> 运行的载荷，故以其为准进行更正。

### Request / Response JSON

**POST Request Body — 线单元基本网格划分**

```json
{
  "Argument": {
    "MESHER": { "TARGETS": [1400, 1397, 1398, 1399] },
    "MESH_SIZE": { "LENGTH": 1 },
    "PROPERTY": { "MATERIAL": 1, "THICKNESS": 1 },
    "DOMAIN_NAME": { "NAME": "frame" }
  }
}
```

**POST Request Body — 平面单元 + 四边/三角 + 指定内部节点/线 + 附加选项**

```json
{
  "Argument": {
    "MESHER": {
      "METHOD": "PlanarElements",
      "TARGETS": [1402],
      "TYPE": "Quadandtriangle",
      "MESH_INNER_DOMAIN": true,
      "INCLUDE_INTERIOR_NODES": { "OPT_CHECK": true, "OPTION": "User", "VALUE": [1] },
      "INCLUDE_INTERIOR_LINES": { "OPT_CHECK": true, "OPTION": "User", "VALUE": [2] },
      "INCLUDE_BOUNDARY_CONNECTIVITY": true
    },
    "MESH_SIZE": { "DIV": 3 },
    "PROPERTY": {
      "ELEMENT_TYPE": "Plate",
      "ELEMENT_SUB_TYPE": { "TYPE": "Thick", "WITH_DRILLING_DOF": true },
      "MATERIAL": 1,
      "THICKNESS": 1
    },
    "DOMAIN_NAME": { "NAME": "Plate2" },
    "ADDITIONAL_OPTION": { "DELETE_LINE_ELEM": false, "SUBDIVIDE_LINE_ELEM": true }
  }
}
```

**POST Response Body**

```json
{
  "AUTOMESH": {
    "1794": { "TYPE": "PLATE", "MATL": 1, "SECT": 1, "NODE": [1545, 1980, 1985, 1984, 0, 0, 0, 0], "ANGLE": 0, "STYPE": 3 },
    "1795": { "TYPE": "PLATE", "MATL": 1, "SECT": 1, "NODE": [1984, 1985, 1986, 1983, 0, 0, 0, 0], "ANGLE": 0, "STYPE": 3 }
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

# ── POST: 对节点围成区域自动划分网格 (平面应力, 四边+三角) ─────
payload = {
    "Argument": {
        "MESHER": {
            "METHOD": "Nodes",
            "TARGETS": [502, 503, 504],
            "TYPE": "Quadandtriangle",
            "MESH_INNER_DOMAIN": True,
            "INCLUDE_INTERIOR_NODES": {"OPT_CHECK": True, "OPTION": "User", "VALUE": [1]},
            "INCLUDE_INTERIOR_LINES": {"OPT_CHECK": True, "OPTION": "User", "VALUE": [2]},
            "INCLUDE_BOUNDARY_CONNECTIVITY": True
        },
        "MESH_SIZE": {"DIV": 3},
        "PROPERTY": {
            "ELEMENT_TYPE": "PlaneStress",
            "ELEMENT_SUB_TYPE": {"TYPE": "Thick", "WITH_DRILLING_DOF": True},
            "MATERIAL": 1,
            "THICKNESS": 1
        },
        "DOMAIN_NAME": {"NAME": "Plate2"},
        "ADDITIONAL_OPTION": {"DELETE_LINE_ELEM": False, "SUBDIVIDE_LINE_ELEM": True}
    }
}
resp = requests.post(f"{BASE_URL}/ope/AUTOMESH", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())
```

---

## 7. `/ope/SSPS` — Surface Spring

> **功能：** 将面弹簧(Surface Spring)边界条件转换为点弹簧(Point Spring)或弹性连接(Elastic Link)生成。支持按框架/平面/实体(面·节点)单元各自的转换方式。

### Input URI

```
{base url}/ope/SSPS
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "SSPS": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "CONVERT_TO": { "type": "string", "enum": ["POINT_SPRING", "ELASTIC_LINK"] },
          "GROUP_NAME": { "type": "string" },
          "NODE_ELEMS": {
            "type": "object",
            "properties": { "KEYS": { "type": "array", "items": { "type": "integer" } } }
          },
          "ELEMENT": {
            "type": "object",
            "properties": {
              "TYPE": { "type": "string", "enum": ["FRAME", "PLANAR", "SOLID_FACE", "SOLID_NODE"] },
              "FACE": { "type": "integer", "enum": [1, 2, 3, 4, 5, 6] },
              "WIDTH": { "type": "number" }
            }
          },
          "BOUNDARY": {
            "type": "object",
            "properties": {
              "TYPE": { "type": "string", "enum": ["LINEAR", "COMP", "TENS", "MULTI"] },
              "DIR": { "type": "integer", "enum": [0, 1, 2, 3, 4, 5, 6, 7] },
              "STIFF": { "type": "array", "items": { "type": "number" }, "maxItems": 3 },
              "PHU": { "type": "number" },
              "SUBGRADE": { "type": "number" },
              "LENGTH": { "type": "number" },
              "bDAMP": { "type": "boolean" },
              "DAMP": { "type": "array", "items": { "type": "number" }, "maxItems": 3 }
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
| 1 | 转换方式 · 点弹簧: `"POINT_SPRING"` / 弹性连接: `"ELASTIC_LINK"` | `"CONVERT_TO"` | String | — | **Required** |
| 2 | 边界组名称 | `"GROUP_NAME"` | String | `""` | Optional |
| 3 | 目标节点/单元编号列表 | `"NODE_ELEMS"` | Object | — | **Required** |
| 3-1 | └ 编号数组 | `NODE_ELEMS.KEYS` | Array [Integer] | — | **Required** |
| 4 | 单元类型信息 | `"ELEMENT"` | Object | — | **Required** |
| 4-1 | └ 类型 · 框架: `"FRAME"` / 平面: `"PLANAR"` / 实体(面): `"SOLID_FACE"` / 实体(节点): `"SOLID_NODE"` | `ELEMENT.TYPE` | String | — | **Required** |
| 4-2 | └ 宽度 (仅 `FRAME`) | `ELEMENT.WIDTH` | Number | — | **Required**(FRAME 时) |
| 4-3 | └ 面编号 1~6 (仅 `SOLID_FACE`) | `ELEMENT.FACE` | Integer | — | **Required**(SOLID_FACE 时) |
| 5 | 边界信息 | `"BOUNDARY"` | Object | — | **Required** |
| 5-1 | └ 边界类型 · 线性: `"LINEAR"` / 只压: `"COMP"` / 只拉: `"TENS"` / 多线性: `"MULTI"` | `BOUNDARY.TYPE` | String | — | **Required** |
| 5-2 | └ 刚度 [Kx,Ky,Kz] (`CONVERT_TO="POINT_SPRING"` 的 LINEAR/MULTI) | `BOUNDARY.STIFF` | Array [Number, 3] | — | **Required**(相应类型) |
| 5-3 | └ 是否考虑阻尼 (`CONVERT_TO="POINT_SPRING"` 的 LINEAR/MULTI) | `BOUNDARY.bDAMP` | Boolean | — | **Required**(相应类型) |
| 5-4 | └ 阻尼常数 [Cx,Cy,Cz] (`CONVERT_TO="POINT_SPRING"` 的 LINEAR/MULTI) | `BOUNDARY.DAMP` | Array [Number, 3] | — | **Required**(相应类型) |
| 5-5 | └ 边界方向(COMP/TENS/除点弹簧外的所有情况) · Normal(+): `0` / Normal(-): `1` / UCS-x(+): `2` / UCS-x(-): `3` / UCS-y(+): `4` / UCS-y(-): `5` / UCS-z(+): `6` / UCS-z(-): `7` | `BOUNDARY.DIR` | Integer | — | **Required**(相应类型) |
| 5-6 | └ 地基反力系数 (COMP/TENS/弹性连接全部) | `BOUNDARY.SUBGRADE` | Number | — | **Required**(相应类型) |
| 5-7 | └ 极限强度 (MULTI/弹性连接 MULTI) | `BOUNDARY.PHU` | Number | — | **Required**(相应类型) |
| 5-8 | └ 弹性连接长度 (`CONVERT_TO="ELASTIC_LINK"` 全部类型) | `BOUNDARY.LENGTH` | Number | — | **Required**(弹性连接) |

> **参考：** `BOUNDARY` 字段是否必填取决于 `CONVERT_TO`(点弹簧/弹性连接)与 `BOUNDARY.TYPE`(线性/只压/只拉/多线性)的组合。具体组合见上表 "必填" 列的条件。
>
> ⚠️ 2026-08-26 确认 (article id `39772183634329`): `BOUNDARY.STIFF`/`bDAMP`/`DAMP`(5-2~5-4)在
> 官方 Request Examples 中仅出现于 `CONVERT_TO="POINT_SPRING"`(点弹簧转换)时。
> `CONVERT_TO="ELASTIC_LINK"`(弹性连接)即使 `BOUNDARY.TYPE` 为 LINEAR 也不使用 `STIFF`/`bDAMP`/`DAMP`，
> 仅使用 `DIR`/`SUBGRADE`/`LENGTH`，故在旧版文档的 "(LINEAR/MULTI)" 条件中补明转换
> 方式的适用范围。

### Request / Response JSON

**POST Request Body — 点弹簧(框架)**

```json
{
  "Argument": {
    "CONVERT_TO": "POINT_SPRING",
    "GROUP_NAME": "B1",
    "NODE_ELEMS": { "KEYS": [61, 62, 63] },
    "ELEMENT": { "TYPE": "FRAME", "WIDTH": 10 },
    "BOUNDARY": {
      "TYPE": "LINEAR",
      "STIFF": [1000, 2000, 3000],
      "bDAMP": true,
      "DAMP": [1, 2, 3]
    }
  }
}
```

**POST Request Body — 弹性连接(实体面)**

```json
{
  "Argument": {
    "CONVERT_TO": "ELASTIC_LINK",
    "GROUP_NAME": "B1",
    "NODE_ELEMS": { "KEYS": [71, 72, 73] },
    "ELEMENT": { "TYPE": "SOLID_FACE", "FACE": 1 },
    "BOUNDARY": { "TYPE": "TENS", "DIR": 7, "SUBGRADE": 5000, "LENGTH": 0.5 }
  }
}
```

**POST Response Body**

```json
{
  "SSPS": {
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

# ── POST: 框架面弹簧 → 点弹簧(线性) 转换 ────────────────────
payload = {
    "Argument": {
        "CONVERT_TO": "POINT_SPRING",
        "GROUP_NAME": "B1",
        "NODE_ELEMS": {"KEYS": [61, 62, 63]},
        "ELEMENT": {"TYPE": "FRAME", "WIDTH": 10},
        "BOUNDARY": {
            "TYPE": "LINEAR",
            "STIFF": [1000, 2000, 3000],
            "bDAMP": True,
            "DAMP": [1, 2, 3]
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/SSPS", json=payload, headers=HEADERS)
print("POST (Point Spring):", resp.status_code, resp.json())

# ── POST: 实体(节点)面弹簧 → 弹性连接(多线性) 转换 ────────────
payload2 = {
    "Argument": {
        "CONVERT_TO": "ELASTIC_LINK",
        "GROUP_NAME": "B1",
        "NODE_ELEMS": {"KEYS": [56, 57, 58, 59, 60, 61, 62, 63]},
        "ELEMENT": {"TYPE": "SOLID_NODE"},
        "BOUNDARY": {"TYPE": "MULTI", "DIR": 7, "SUBGRADE": 5000, "PHU": 500, "LENGTH": 0.5}
    }
}
resp = requests.post(f"{BASE_URL}/ope/SSPS", json=payload2, headers=HEADERS)
print("POST (Elastic Link):", resp.status_code, resp.json())
```

---

## 8. `/ope/EDMP` — Change Property

> **功能：** 指定或自动计算收缩·徐变计算所需的构件名义尺寸(Notional Size of Member)或体积表面积比(Volume Surface Ratio)。

### Input URI

```
{base url}/ope/EDMP
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "EDMP": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "Argument": {
        "type": "object",
        "properties": {
          "NODE_ELEMS": {
            "type": "object",
            "properties": { "KEYS": { "type": "array", "items": { "type": "integer" } } }
          },
          "TYPE": { "description": "TYPE", "type": "string", "enum": ["NSM", "VSR"] },
          "AUTO": { "description": "Auto Calculate", "type": "boolean" },
          "CODE": {
            "description": "CODE",
            "type": "string",
            "enum": ["Korean Standard", "CEB-FIP(1990)", "Japanese Standard", "Chinese Standard"]
          },
          "PARAMETER": { "description": "Parameter Value(a)", "type": "number" },
          "H_VS": { "description": "Change Property Value h(v/s)", "type": "number" }
        }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 目标节点/单元编号 | `"NODE_ELEMS"` | Object | — | **Required** |
| 1-1 | └ 编号数组 (例: `[101, 102, 103]`) | `NODE_ELEMS.KEYS` | Array [Integer] | — | **Required** |
| 2 | 变更方法 · 名义尺寸: `"NSM"` / 体积表面积比: `"VSR"` | `"TYPE"` | String | `"NSM"` | Optional |
| 3 | 是否自动计算 (体积表面积比只能为 `false`) | `"AUTO"` | Boolean | `false` | Optional |
| 4 | 基准代码 · 韩国标准: `"Korean Standard"` / CEB-FIP(1990) / 日本标准 / 中国标准 (仅 `AUTO=true` 且 `TYPE="NSM"` 时使用) | `"CODE"` | String | `"Korean Standard"` | Optional |
| 5 | 参数值(a) (`AUTO=false` 时必填) | `"PARAMETER"` | Number | — | **Required**(AUTO=false) |
| 6 | 变更值 · 名义尺寸: h / 体积表面积比: v/s | `"H_VS"` | Number | — | **Required** |

### Request / Response JSON

**POST Request Body — 名义尺寸自动计算**

```json
{
  "Argument": {
    "NODE_ELEMS": { "KEYS": [1, 2, 3] },
    "TYPE": "NSM",
    "AUTO": true,
    "CODE": "Korean Standard",
    "PARAMETER": 0.5
  }
}
```

**POST Request Body — 体积表面积比手动输入**

```json
{
  "Argument": {
    "NODE_ELEMS": { "KEYS": [1, 2, 3] },
    "TYPE": "VSR",
    "AUTO": false,
    "H_VS": 1.0
  }
}
```

**POST Response Body**

```json
{
  "EDMP": {
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

# ── POST: 名义尺寸(Notional Size)自动计算 ─────────────────────────
payload = {
    "Argument": {
        "NODE_ELEMS": {"KEYS": [1, 2, 3]},
        "TYPE": "NSM",
        "AUTO": True,
        "CODE": "Korean Standard",
        "PARAMETER": 0.5
    }
}
resp = requests.post(f"{BASE_URL}/ope/EDMP", json=payload, headers=HEADERS)
print("POST (NSM):", resp.status_code, resp.json())

# ── POST: 直接输入体积表面积比(V/S) ─────────────────────────────────
payload2 = {
    "Argument": {
        "NODE_ELEMS": {"KEYS": [1, 2, 3]},
        "TYPE": "VSR",
        "AUTO": False,
        "H_VS": 1.0
    }
}
resp = requests.post(f"{BASE_URL}/ope/EDMP", json=payload2, headers=HEADERS)
print("POST (VSR):", resp.status_code, resp.json())
```

---

## 9. `/ope/STOR` — Story Calculation

> **功能：** 设置楼层(Story)计算时地震/风荷载偶然偏心(Accidental Eccentricity)的考虑与否及取值，并返回各层计算结果。

### Input URI

```
{base url}/ope/STOR
```

### Active Methods

`POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SEIS_ECC": { "INC_SEIS_ECC": false, "SEIS_ECC_VALUE": 5 },
    "WIND_ECC": { "INC_WIND_ECC": false, "WIND_ECC_VALUE": 15 }
  }
}
```

**POST Response Body**

```json
{
  "STOR": {
    "string": {
      "STORY_NAME": "string",
      "STORY_LEVEL": 0,
      "bFLOOR_DIAPHRAGM": false,
      "WIND_FLOOR_WIDTH_X": 0,
      "WIND_FLOOR_WIDTH_Y": 0,
      "WIND_CENTER_X": 0,
      "WIND_CENTER_Y": 0,
      "WIND_ECCENT_X": 0,
      "WIND_ECCENT_Y": 0,
      "SEIS_ACC_ECCENT_X": 0,
      "SEIS_ACC_ECCENT_Y": 0,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 0,
      "STORY_AREA_ITEMS": [{ "X": 0, "Y": 0, "Z": 0 }]
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 地震偶然偏心 | `"SEIS_ECC"` | Object | — | **Required** |
| 1-1 | └ 是否包含地震偶然偏心 | `SEIS_ECC.INC_SEIS_ECC` | Boolean | — | **Required** |
| 1-2 | └ 地震偶然偏心值(%) | `SEIS_ECC.SEIS_ECC_VALUE` | Number | — | **Required** |
| 2 | 风荷载偏心 | `"WIND_ECC"` | Object | — | **Required** |
| 2-1 | └ 是否包含风荷载偏心 | `WIND_ECC.INC_WIND_ECC` | Boolean | — | **Required** |
| 2-2 | └ 风荷载偏心值(%) | `WIND_ECC.WIND_ECC_VALUE` | Number | — | **Required** |

响应的各层(`"string"` 为楼层名称)项中包含楼层标高、是否为楼板刚性隔板、风荷载/地震偏心量、扭转放大系数、楼层面积坐标列表(`STORY_AREA_ITEMS`)。

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 设置楼层计算选项(偶然偏心)并查询结果 ─────────────────
payload = {
    "Argument": {
        "SEIS_ECC": {"INC_SEIS_ECC": True, "SEIS_ECC_VALUE": 5},
        "WIND_ECC": {"INC_WIND_ECC": True, "WIND_ECC_VALUE": 15}
    }
}
resp = requests.post(f"{BASE_URL}/ope/STOR", json=payload, headers=HEADERS)
stories = resp.json().get("STOR", {})
for name, info in stories.items():
    print(f"[{info['STORY_NAME']}] Level={info['STORY_LEVEL']}, Diaphragm={info['bFLOOR_DIAPHRAGM']}")
```

---

## 10. `/ope/STORY_PARAM` — Story Check Parameter

> **功能：** 设置或查询层间位移比、扭转等楼层审查所用的国家基准代码(Country Code)。

### Input URI

```
{base url}/ope/STORY_PARAM
```

### Active Methods

`GET` · `POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "COUNTRY_CODE": "NTC2012"
  }
}
```

**GET / POST Response Body**

```json
{
  "STORY_PARAM": {
    "COUNTRY_CODE": "NTC2012"
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 设置国家基准代码 · `"NTC2012"` / `"NTC2008"` / `"KBC2009"` / `"NSR-10"` / `"NTC2018"` / `"NTC2020"` / `"IS1893(2016)"` / `"IS16700(2023)"` | `"COUNTRY_CODE"` | String | — | **Required** |

> ⚠️ 2026-08-26 确认 (article id `49514705474457`): 旧版文档写作 `"NTCS2020"`，
> 官方 Specifications 表中为 `"NTC2020"`(无 S)，故予以更正。示例中未出现
> 该值，仅通过表格核实；而 `STORY_IRR_PARAM`(第 11 节)的 `COUNTRY_CODE` 列表中另存在
> `"NTCS2020"`/`"NTCS2023"`，因此两个 Endpoint 可能使用不同的字面量 ——
> 是误记还是确实是不同代码，需官方确认。

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 设置楼层审查基准代码 ────────────────────────────────────
payload = {"Argument": {"COUNTRY_CODE": "KBC2009"}}
resp = requests.post(f"{BASE_URL}/ope/STORY_PARAM", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询当前设置的基准代码 ─────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/STORY_PARAM", headers=HEADERS)
print("GET:", resp.json())
```

---

## 11. `/ope/STORY_IRR_PARAM` — Story Irregularity Check Parameter

> **功能：** 设置或查询楼层不规则性(扭转·刚度·强度)审查所需的国家基准代码、层间位移计算方法、楼层刚度计算方法、地震行为系数。

### Input URI

```
{base url}/ope/STORY_IRR_PARAM
```

### Active Methods

`GET` · `POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "COUNTRY_CODE": "NSR-10",
    "STORY_DRIFT_METHOD": "Max.DriftofOuterExtremePoints",
    "STORY_STIFFNESS_METHOD": "1/StoryDriftRatio",
    "SEISMIC_BEHAVIOR_FACTOR": "3orbelow"
  }
}
```

**GET / POST Response Body**

```json
{
  "STORY_IRR_PARAM": {
    "COUNTRY_CODE": "NSR-10",
    "STORY_DRIFT_METHOD": "Max.DriftofOuterExtremePoints",
    "STORY_STIFFNESS_METHOD": "1/StoryDriftRatio",
    "SEISMIC_BEHAVIOR_FACTOR": "3orbelow"
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 国家基准代码 · `"NTC2018"` / `"NTC2012"` / `"NTC2008"` / `"KBC2009"` / `"NSR-10"` / `"NTCS2020"` / `"NTCS2023"` / `"NSCP2015"` / `"IS1893(2016)"` / `"IS16700(2023)"` | `"COUNTRY_CODE"` | String | — | **Required** |
| 2 | 层间位移计算方法 · 质心位移: `"Drift at the Center of Mass"` / 最外缘点最大位移: `"Max. Drift of Outer Extreme Points"` / 全部竖向构件最大位移: `"Max. Drift of All Vertical Elements"` | `"STORY_DRIFT_METHOD"` | String | — | **Required** |
| 3 | 楼层刚度计算方法 · `"1 / Story Drift Ratio"` / `"Story Shear / Story Drift"` | `"STORY_STIFFNESS_METHOD"` | String | — | **Required** |
| 4 | 地震行为系数(仅 `COUNTRY_CODE` 为 `"NTCS2023"` 或 `"NTCS2020"` 时需要) · `"4"` / `"3 or below"` | `"SEISMIC_BEHAVIOR_FACTOR"` | String | — | 条件性 **Required** |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 设置楼层不规则性审查参数 ───────────────────────────
payload = {
    "Argument": {
        "COUNTRY_CODE": "NTCS2023",
        "STORY_DRIFT_METHOD": "Max.DriftofOuterExtremePoints",
        "STORY_STIFFNESS_METHOD": "1/StoryDriftRatio",
        "SEISMIC_BEHAVIOR_FACTOR": "3orbelow"   # 因 NTCS2023 而必填
    }
}
resp = requests.post(f"{BASE_URL}/ope/STORY_IRR_PARAM", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询当前设置 ────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/ope/STORY_IRR_PARAM", headers=HEADERS)
print("GET:", resp.json())
```

---

## 12. `/ope/STORYPROP` — Story Properties

> **功能：** 以指定单位·格式查询各层重量、标高、受荷高度、受荷宽度(Bx/By)等楼层属性计算结果。
>
> ⚠️ 2026-08-26 确认 (article id `49514773501721`): 旧版文档将 Endpoint 写作 `/ope/STORPROP`，
> 但官方 Input URI 为 `/ope/STORYPROP`(STORY+PROP)。响应体的键(`"STORYPROP"`)在
> 旧版中已正确地包含 "Y"，据此判断其与 URI 写法内部不一致，
> 故将 URI·标题·Python 示例更正为与响应键一致。此外示例的 `FORMAT` 值写作 `"Default"`，
> 该值在表的 enum(`"Fixed"`/`"Scientific"`)中也不存在，故更正为官方示例的 `"Fixed"`。
> `HEAD` 数组中的 `"LoadedH"`/`"LoadedBx"`/`"LoadedBy"` 也更正为含空格的官方字面量
> `"Loaded H"`/`"Loaded Bx"`/`"Loaded By"`(与第 6·7 节相反，此次是写法中
> 漏掉了空格)。不过 `PLACE` 的 Value 类型官方表标注为 "String"(示例为整数
> `4`)存在自相矛盾，故暂不下结论，保持表中标注值。

### Input URI

```
{base url}/ope/STORYPROP
```

### Active Methods

`POST`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "FORCE_UNIT": "KN",
    "LENGTH_UNIT": "M",
    "FORMAT": "Fixed",
    "PLACE": 4
  }
}
```

**POST Response Body**

```json
{
  "STORYPROP": {
    "FORCE": "KN",
    "LENGTH": "M",
    "HEAD": ["Story", "Weight", "Elev.", "Loaded H", "Loaded Bx", "Loaded By"],
    "DATA": [
      { "STORY": "Roof", "WEIGHT": "3256.1530", "ELEV": "50.0000", "LOADED_H": "2.0000", "LOADED_BX": "29.1000", "LOADED_BY": "36.0000" },
      { "STORY": "12F", "WEIGHT": "3984.8264", "ELEV": "46.0000", "LOADED_H": "4.0000", "LOADED_BX": "29.1000", "LOADED_BY": "36.0000" },
      { "STORY": "G.L.", "WEIGHT": "0.0000", "ELEV": "0.0000", "LOADED_H": "2.5000", "LOADED_BX": "27.6000", "LOADED_BY": "36.0000" }
    ]
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 力单位 · `"N"`/`"KN"`/`"KGF"`/`"TONF"`/`"LBF"`/`"KIPS"` | `"FORCE_UNIT"` | String | System | Optional |
| 2 | 长度单位 · `"M"`/`"CM"`/`"MM"`/`"FT"`/`"IN"` | `"LENGTH_UNIT"` | String | System | Optional |
| 3 | 响应数字格式 · `"Fixed"`/`"Scientific"` | `"FORMAT"` | String | System | Optional |
| 4 | 响应数字小数位数(0~15) | `"PLACE"` | String | System | Optional |

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 查询楼层属性结果(KN, M, 小数点后 4 位) ───────────────────
payload = {
    "Argument": {
        "FORCE_UNIT": "KN",
        "LENGTH_UNIT": "M",
        "FORMAT": "Fixed",
        "PLACE": 4
    }
}
resp = requests.post(f"{BASE_URL}/ope/STORYPROP", json=payload, headers=HEADERS)
result = resp.json().get("STORYPROP", {})
for row in result.get("DATA", []):
    print(f"{row['STORY']}: 重量={row['WEIGHT']}{result['FORCE']}, 标高={row['ELEV']}{result['LENGTH']}")
```

---

## 13. `/ope/MEMB` — Member Assignment

> **功能：** 将多个单元自动/手动指派为一个构件(Member)。用于设计审查时的构件单位审查。

### Input URI

```
{base url}/ope/MEMB
```

### Active Methods

`POST`

### Request / Response JSON

**POST Request Body — 手动指派**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "MANUAL",
    "SELECTION_TYPE": "SELECTION",
    "ELEM_LIST": [640, 692],
    "ALLOW_SINGLE": false
  }
}
```

**POST Request Body — 自动指派(全部单元)**

```json
{
  "Argument": {
    "ASSIGN_TYPE": "AUTO",
    "SELECTION_TYPE": "ALL",
    "ALLOW_SINGLE": true
  }
}
```

**POST Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [640, 692],
      "bREVERSE": false
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 指派类型 · 手动: `"MANUAL"` / 自动: `"AUTO"` | `"ASSIGN_TYPE"` | String | — | **Required** |
| 2 | 选择类型 · 全部: `"ALL"`(`ASSIGN_TYPE="AUTO"` 时可用) / 选择: `"SELECTION"` | `"SELECTION_TYPE"` | String | — | **Required** |
| 3 | 目标单元列表 (`SELECTION_TYPE="ALL"` 时忽略) | `"ELEM_LIST"` | Array | — | 条件性 **Required** |
| 4 | 是否允许单单元构件 | `"ALLOW_SINGLE"` | Boolean | — | **Required** |

> ⚠️ **韩文/英文页面不一致 — 以英文页面为准采用 `"ELEM_LIST"`(2026-09-06 确定)。**
> 原文文章(id `49514964272665`)**各 locale 正文不同。** en-us 页面的请求示例与
> Specifications 表均为 `ELEM_LIST`、仅响应示例为 `AELEM`，内部一致；而 ko
> 页面只有表为 `ELEM_LIST`、请求示例却是 `AELEM`，同一页面之内自相矛盾。
> (正文字符串计数 — en-us: `ELEM_LIST` 2 次 / `AELEM` 1 次，ko: `ELEM_LIST` 1 次 / `AELEM` 5 次。
> 该文章本身没有 JSON Schema 一节。)
>
> | 页面 | 请求示例 | Specifications 表第 3 行 | 响应示例 |
> | --- | --- | --- | --- |
> | [英文](https://support.midasuser.com/hc/en-us/articles/49514964272665) | `"ELEM_LIST": [640, 692]` | `"ELEM_LIST"` | `"AELEM"` |
> | [韩文](https://support.midasuser.com/hc/ko/articles/49514964272665) | `"AELEM": [1, 2]` | `"ELEM_LIST"` | `"AELEM"` |
>
> 即 **请求键为 `ELEM_LIST`，响应·存储记录键为 `AELEM`**，两者不同才是正常的。
> 同级 Endpoint [`/db/MEMB`](./24_DB_Design.md#5-dbmemb--member-assignment-设计构件指定) 之所以
> 全部使用 `AELEM`，是因为该端直接操作存储记录(CRUD)，不能作为本 Endpoint **请求**
> 键的依据。
>
> 关于「请将 ko 页面请求示例改为与 en-us 一致」的请求，已以 Jira `MAPI-2484` 后续评论(2026-09-06)
> 形式受理。原文表第 2 行的 `"SELETION_TYPE"` 误记(ko/en 均仍存在)也属同一工单 A-7 项，
> 上表已按 `SELECTION_TYPE` 更正记录。
>
> (沿革: 2026-09-06 曾**只看 ko 页面**，按"示例优先于表"原则改为 `AELEM`，
> 同日确认 en-us 页面后又改回。**在未先确认各 locale 正文是否分歧之前，不要套用示例
> 优先原则。** 请勿改回。)

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 将指定单元手动指派为一个构件 ────────────────────
payload = {
    "Argument": {
        "ASSIGN_TYPE": "MANUAL",
        "SELECTION_TYPE": "SELECTION",
        "ELEM_LIST": [640, 692],
        "ALLOW_SINGLE": False
    }
}
resp = requests.post(f"{BASE_URL}/ope/MEMB", json=payload, headers=HEADERS)
print("POST (手动):", resp.status_code, resp.json())

# ── POST: 全模型自动构件指派 ─────────────────────────────────
payload2 = {
    "Argument": {
        "ASSIGN_TYPE": "AUTO",
        "SELECTION_TYPE": "ALL",
        "ALLOW_SINGLE": True
    }
}
resp = requests.post(f"{BASE_URL}/ope/MEMB", json=payload2, headers=HEADERS)
print("POST (自动):", resp.status_code, resp.json())
```

---

## 14. `/ope/GUSTFACTOR` — Gust Factor Calculator

> **功能：** 依据 KDS 41 12:2022 风荷载标准，计算刚性/柔性结构的阵风影响系数(Gust Effect Factor)。

### Input URI

```
{base url}/ope/GUSTFACTOR
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "description": "GUSTFACTOR request item. STRUCTURE_TYPE controls whether RIGID_PARAM or FLEXIBLE_PARAM is required.",
      "required": ["WIND_CODE", "STRUCTURE_TYPE"],
      "properties": {
        "WIND_CODE": { "type": "string", "enum": ["KDS(41-12:2022)"] },
        "STRUCTURE_TYPE": { "type": "string", "enum": ["RIGID", "FLEXIBLE"], "description": "Structure type classification." },
        "RIGID_PARAM": {
          "type": "object",
          "required": ["EXP_CATEGORY", "ROOF_HEIGHT", "BREADTH_X", "BREADTH_Y"],
          "properties": {
            "EXP_CATEGORY": { "type": "string", "description": "Exposure category." },
            "ROOF_HEIGHT": { "type": "number", "minimum": 0, "description": "Roof height." },
            "BREADTH_X": { "type": "number", "minimum": 0, "description": "Plan breadth in global X direction." },
            "BREADTH_Y": { "type": "number", "minimum": 0, "description": "Plan breadth in global Y direction." }
          }
        },
        "FLEXIBLE_PARAM": {
          "type": "object",
          "required": [
            "EXP_CATEGORY", "BASIC_WIND_SPEED", "IMPORTANCE_FACTOR", "DIRECTION_FACTOR_X", "DIRECTION_FACTOR_Y",
            "BREADTH_X", "BREADTH_Y", "STORY_HEIGHT_MAX", "FREQUENCY_X", "FREQUENCY_Y", "DAMPING",
            "TOTAL_MASS", "MX", "MY", "VIBRATION"
          ],
          "properties": {
            "EXP_CATEGORY": { "type": "string", "description": "Exposure category." },
            "BASIC_WIND_SPEED": { "type": "number", "minimum": 0, "description": "Basic wind speed." },
            "IMPORTANCE_FACTOR": { "type": "number", "minimum": 0, "description": "Importance factor." },
            "TOPOGRAPHIC_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use topographic effect." },
                "KZT": { "type": "number", "minimum": 0, "description": "Topographic factor Kzt. Required only if OPT_USE=true." }
              },
              "description": "Optional. If omitted, treated as OPT_USE=false."
            },
            "DIRECTION_FACTOR_X": { "type": "number", "minimum": 0, "description": "Direction factor in X." },
            "DIRECTION_FACTOR_Y": { "type": "number", "minimum": 0, "description": "Direction factor in Y." },
            "BREADTH_X": { "type": "number", "minimum": 0, "description": "Plan breadth in global X direction." },
            "BREADTH_Y": { "type": "number", "minimum": 0, "description": "Plan breadth in global Y direction." },
            "STORY_HEIGHT_MAX": { "type": "number", "minimum": 0, "description": "Maximum story or roof height used for flexible response." },
            "FREQUENCY_X": { "type": "number", "minimum": 0, "description": "Fundamental frequency in X." },
            "FREQUENCY_Y": { "type": "number", "minimum": 0, "description": "Fundamental frequency in Y." },
            "DAMPING": { "type": "number", "minimum": 0, "description": "Damping ratio, for example 0.03." },
            "TOTAL_MASS": { "type": "number", "minimum": 0, "description": "Total mass." },
            "MX": { "type": "number", "minimum": 0, "description": "Mass term in X." },
            "MY": { "type": "number", "minimum": 0, "description": "Mass term in Y." },
            "VIBRATION": { "type": "number", "minimum": 0, "description": "Vibration-related factor or flag." }
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
| 1 | 风荷载基准代码 · `"KDS(41-12:2022)"` | `"WIND_CODE"` | String (enum) | — | **Required** |
| 2 | 结构物类型 · 刚性: `"RIGID"` / 柔性: `"FLEXIBLE"` | `"STRUCTURE_TYPE"` | String (enum) | — | **Required** |
| **STRUCTURE_TYPE = "RIGID" 时** |
| 3 | 刚性结构参数 | `"RIGID_PARAM"` | Object | — | 条件性 **Required** |
| 3-1 | └ 地面暴露类别 | `RIGID_PARAM.EXP_CATEGORY` | String | — | **Required** |
| 3-2 | └ 屋顶高度 | `RIGID_PARAM.ROOF_HEIGHT` | Number (≥0) | — | **Required** |
| 3-3 | └ 平面宽度(X 方向) | `RIGID_PARAM.BREADTH_X` | Number (≥0) | — | **Required** |
| 3-4 | └ 平面宽度(Y 方向) | `RIGID_PARAM.BREADTH_Y` | Number (≥0) | — | **Required** |
| **STRUCTURE_TYPE = "FLEXIBLE" 时** |
| 4 | 柔性结构参数 | `"FLEXIBLE_PARAM"` | Object | — | 条件性 **Required** |
| 4-1 | └ 地面暴露类别 | `FLEXIBLE_PARAM.EXP_CATEGORY` | String | — | **Required** |
| 4-2 | └ 基本风速(m/s) | `FLEXIBLE_PARAM.BASIC_WIND_SPEED` | Number (≥0) | — | **Required** |
| 4-3 | └ 重要性系数 | `FLEXIBLE_PARAM.IMPORTANCE_FACTOR` | Number (≥0) | — | **Required** |
| 4-4 | └ 地形效应考虑选项 | `FLEXIBLE_PARAM.TOPOGRAPHIC_EFFECT` | Object | — | Optional (省略时不使用) |
| 4-4-a | 　└ 是否使用 | `TOPOGRAPHIC_EFFECT.OPT_USE` | Boolean | `false` | **Required** |
| 4-4-b | 　└ 地形系数 Kzt (`OPT_USE=true` 时必填) | `TOPOGRAPHIC_EFFECT.KZT` | Number (≥0) | — | 条件性 **Required** |
| 4-5 | └ 方向系数(X) | `FLEXIBLE_PARAM.DIRECTION_FACTOR_X` | Number (≥0) | — | **Required** |
| 4-6 | └ 方向系数(Y) | `FLEXIBLE_PARAM.DIRECTION_FACTOR_Y` | Number (≥0) | — | **Required** |
| 4-7 | └ 平面宽度(X 方向) | `FLEXIBLE_PARAM.BREADTH_X` | Number (≥0) | — | **Required** |
| 4-8 | └ 平面宽度(Y 方向) | `FLEXIBLE_PARAM.BREADTH_Y` | Number (≥0) | — | **Required** |
| 4-9 | └ 最大层高/屋顶高度 | `FLEXIBLE_PARAM.STORY_HEIGHT_MAX` | Number (≥0) | — | **Required** |
| 4-10 | └ 固有频率(X, Hz) | `FLEXIBLE_PARAM.FREQUENCY_X` | Number (≥0) | — | **Required** |
| 4-11 | └ 固有频率(Y, Hz) | `FLEXIBLE_PARAM.FREQUENCY_Y` | Number (≥0) | — | **Required** |
| 4-12 | └ 阻尼比 | `FLEXIBLE_PARAM.DAMPING` | Number (≥0) | — | **Required** |
| 4-13 | └ 总质量 | `FLEXIBLE_PARAM.TOTAL_MASS` | Number (≥0) | — | **Required** |
| 4-14 | └ 质量项(X) | `FLEXIBLE_PARAM.MX` | Number (≥0) | — | **Required** |
| 4-15 | └ 质量项(Y) | `FLEXIBLE_PARAM.MY` | Number (≥0) | — | **Required** |
| 4-16 | └ 振动相关系数 | `FLEXIBLE_PARAM.VIBRATION` | Number (≥0) | — | **Required** |

### Request / Response JSON

**POST Request Body — 柔性结构**

```json
{
  "Argument": {
    "WIND_CODE": "KDS(41-12:2022)",
    "STRUCTURE_TYPE": "FLEXIBLE",
    "FLEXIBLE_PARAM": {
      "EXP_CATEGORY": "B",
      "BASIC_WIND_SPEED": 38,
      "IMPORTANCE_FACTOR": 1,
      "TOPOGRAPHIC_EFFECT": { "OPT_USE": true, "KZT": 1.1 },
      "DIRECTION_FACTOR_X": 0.85,
      "DIRECTION_FACTOR_Y": 0.85,
      "BREADTH_X": 32,
      "BREADTH_Y": 24,
      "STORY_HEIGHT_MAX": 72,
      "FREQUENCY_X": 0.42,
      "FREQUENCY_Y": 0.48,
      "DAMPING": 0.03,
      "TOTAL_MASS": 85000,
      "MX": 82000,
      "MY": 80500,
      "VIBRATION": 1
    }
  }
}
```

**POST Request Body — 刚性结构**

```json
{
  "Argument": {
    "WIND_CODE": "KDS(41-12:2022)",
    "STRUCTURE_TYPE": "RIGID",
    "RIGID_PARAM": {
      "EXP_CATEGORY": "C",
      "ROOF_HEIGHT": 30,
      "BREADTH_X": 20,
      "BREADTH_Y": 15
    }
  }
}
```

**POST Response Body**

```json
{
  "OPE_GUSTFACTOR_RESPONSE": {
    "GUST_FACTOR_X": 1.7400999942907864,
    "GUST_FACTOR_Y": 1.7513941589768178
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

# ── POST: 柔性结构阵风影响系数计算 ─────────────────────────────
payload = {
    "Argument": {
        "WIND_CODE": "KDS(41-12:2022)",
        "STRUCTURE_TYPE": "FLEXIBLE",
        "FLEXIBLE_PARAM": {
            "EXP_CATEGORY": "B",
            "BASIC_WIND_SPEED": 38,
            "IMPORTANCE_FACTOR": 1,
            "TOPOGRAPHIC_EFFECT": {"OPT_USE": True, "KZT": 1.1},
            "DIRECTION_FACTOR_X": 0.85,
            "DIRECTION_FACTOR_Y": 0.85,
            "BREADTH_X": 32,
            "BREADTH_Y": 24,
            "STORY_HEIGHT_MAX": 72,
            "FREQUENCY_X": 0.42,
            "FREQUENCY_Y": 0.48,
            "DAMPING": 0.03,
            "TOTAL_MASS": 85000,
            "MX": 82000,
            "MY": 80500,
            "VIBRATION": 1
        }
    }
}
resp = requests.post(f"{BASE_URL}/ope/GUSTFACTOR", json=payload, headers=HEADERS)
result = resp.json().get("OPE_GUSTFACTOR_RESPONSE", {})
print(f"阵风影响系数 Gx = {result['GUST_FACTOR_X']:.4f}")
print(f"阵风影响系数 Gy = {result['GUST_FACTOR_Y']:.4f}")
```

---

## 15. `/ope/LCOM-GEN` — Load Combination (General) – KDS:2022 / AIK-SRC2K

> **功能：** 依据设计基准(混凝土/钢结构/SRC)，指定反应谱缩放系数、风荷载组合、正交效应、特殊地震作用·竖向地震力·地下结构物荷载等选项，自动生成设计荷载组合。本 Endpoint 为 POST 专用，以向既有设计荷载组合追加(ADD)或整体替换(REPLACE)的方式运行。同一 Endpoint 也支持指定 `DGNCODE: "AIK-SRC2K"` 的更简化模式(`OPTION` + `DGNCODE` + `RS_SCALE_FACTOR`)，其在本文下方 "LCOM-GEN/SRC AIK-SRC2K 变体模式" 一节中说明。本节仅处理以 `CODE_SELECTION` 选择 CONCRETE/STEEL/SRC body 的 KDS:2022 变体。

### Input URI

```
{base url}/ope/LCOM-GEN
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "description": "LCOM-GEN item for KDS 2022. Body structure is selected by CODE_SELECTION.",
      "oneOf": [
        {
          "type": "object",
          "required": ["OPTION", "CODE_SELECTION", "DGNCODE", "RS_SCALE_FACTOR", "ORTHO_EFFECT", "ADDITIONAL_LOAD", "CS_ANALYSIS", "PRESTRESS_LOSS"],
          "properties": {
            "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
            "ADD_ENVELOPE": { "type": "boolean", "default": true, "description": "Add envelope option for LCOM-GEN" },
            "CODE_SELECTION": { "type": "string", "const": "CONCRETE", "description": "CONCRETE design code body" },
            "DGNCODE": { "type": "string", "const": "KDS 41 20 : 2022", "default": "KDS 41 20 : 2022", "description": "Concrete design code value. General group key: KDS_2022" },
            "RS_SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "WIND_LOAD_COMB": {
              "type": "object",
              "required": ["PARAMETERS"],
              "properties": {
                "PARAMETERS": {
                  "type": "array",
                  "description": "List of wind load combination sets",
                  "items": {
                    "type": "object",
                    "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                    "properties": {
                      "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                      "WIND_LOAD_CASE": {
                        "type": "object",
                        "properties": {
                          "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                          "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                          "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                        }
                      },
                      "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                      "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                    }
                  }
                },
                "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
              }
            },
            "ORTHO_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
                "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
                "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
              }
            },
            "ADDITIONAL_LOAD": {
              "type": "object",
              "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
              "properties": {
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Special Seismic Load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      }
                    }
                  }
                },
                "VERTICAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Vertical Seismic Forces" },
                    "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
                  }
                }
              }
            },
            "UNDERGROUND_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "description": "for Underground Load" },
                "SCALE_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                },
                "LOAD_CASE_LIST": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                      "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                      "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                      "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                    }
                  }
                },
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "Whether to use special load for underground load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      },
                      "description": "Over-strength factors for underground special load"
                    }
                  }
                }
              }
            },
            "CS_ANALYSIS": { "type": "boolean" },
            "PRESTRESS_LOSS": { "type": "boolean" }
          }
        },
        {
          "type": "object",
          "required": ["OPTION", "CODE_SELECTION", "DGNCODE", "RS_SCALE_FACTOR", "ORTHO_EFFECT", "ADDITIONAL_LOAD"],
          "properties": {
            "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
            "ADD_ENVELOPE": { "type": "boolean", "default": true, "description": "Add envelope option for LCOM-GEN" },
            "CODE_SELECTION": { "type": "string", "const": "STEEL", "description": "STEEL design code body" },
            "DGNCODE": { "type": "string", "const": "KDS 41 30 : 2022", "default": "KDS 41 30 : 2022", "description": "Steel design code value. General group key: KDS_2022" },
            "RS_SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "WIND_LOAD_COMB": {
              "type": "object",
              "required": ["PARAMETERS"],
              "properties": {
                "PARAMETERS": {
                  "type": "array",
                  "description": "List of wind load combination sets",
                  "items": {
                    "type": "object",
                    "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                    "properties": {
                      "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                      "WIND_LOAD_CASE": {
                        "type": "object",
                        "properties": {
                          "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                          "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                          "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                        }
                      },
                      "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                      "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                    }
                  }
                },
                "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
              }
            },
            "ORTHO_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
                "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
                "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
              }
            },
            "ADDITIONAL_LOAD": {
              "type": "object",
              "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
              "properties": {
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Special Seismic Load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      }
                    }
                  }
                },
                "VERTICAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Vertical Seismic Forces" },
                    "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
                  }
                }
              }
            },
            "UNDERGROUND_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "description": "for Underground Load" },
                "SCALE_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                },
                "LOAD_CASE_LIST": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                      "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                      "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                      "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                    }
                  }
                },
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "Whether to use special load for underground load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      },
                      "description": "Over-strength factors for underground special load"
                    }
                  }
                }
              }
            }
          }
        },
        {
          "type": "object",
          "required": ["OPTION", "CODE_SELECTION", "DGNCODE", "RS_SCALE_FACTOR", "WIND_LOAD_COMB", "ORTHO_EFFECT", "ADDITIONAL_LOAD", "UNDERGROUND_LOAD"],
          "properties": {
            "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
            "ADD_ENVELOPE": { "type": "boolean", "default": true, "description": "Add envelope option for LCOM-GEN" },
            "CODE_SELECTION": { "type": "string", "const": "SRC", "description": "SRC design code body" },
            "DGNCODE": { "type": "string", "const": "KDS 41 SRC : 2022", "default": "KDS 41 SRC : 2022", "description": "SRC design code value. General group key: KDS_2022" },
            "RS_SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "WIND_LOAD_COMB": {
              "type": "object",
              "required": ["PARAMETERS"],
              "properties": {
                "PARAMETERS": {
                  "type": "array",
                  "description": "List of wind load combination sets",
                  "items": {
                    "type": "object",
                    "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                    "properties": {
                      "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                      "WIND_LOAD_CASE": {
                        "type": "object",
                        "properties": {
                          "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                          "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                          "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                        }
                      },
                      "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                      "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                    }
                  }
                },
                "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
              }
            },
            "ORTHO_EFFECT": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
                "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
                "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
              }
            },
            "ADDITIONAL_LOAD": {
              "type": "object",
              "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
              "properties": {
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Special Seismic Load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      }
                    }
                  }
                },
                "VERTICAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "for Vertical Seismic Forces" },
                    "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
                  }
                }
              }
            },
            "UNDERGROUND_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "description": "for Underground Load" },
                "SCALE_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                },
                "LOAD_CASE_LIST": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                      "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                      "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                      "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                    }
                  }
                },
                "SPECIAL_LOAD": {
                  "type": "object",
                  "required": ["OPT_USE"],
                  "properties": {
                    "OPT_USE": { "type": "boolean", "description": "Whether to use special load for underground load" },
                    "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                    "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                    "OVER_STRENGTH_FACTOR": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "required": ["LOAD_CASE", "FACTOR"],
                        "properties": {
                          "LOAD_CASE": { "type": "string", "description": "Load Case" },
                          "FACTOR": { "type": "number", "description": "Scale Factor" }
                        }
                      },
                      "description": "Over-strength factors for underground special load"
                    }
                  }
                }
              }
            }
          }
        }
      ]
    }
  }
}
```

### Parameters

`Argument` 是随 `CODE_SELECTION` 取值(`CONCRETE` / `STEEL` / `SRC`)而采取互不相同 body 结构的 `oneOf` 模式。三个 body 共享大部分字段，差异已在表中注明(`DGNCODE` 的 const 值、`CS_ANALYSIS`/`PRESTRESS_LOSS` 字段有无、`WIND_LOAD_COMB`/`UNDERGROUND_LOAD` 的必填与否)。

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|---|---|---|---|---|---|
| 1 | OPTION – 是向既有组合追加还是整体替换 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 必填 |
| 2 | Add envelope option for LCOM-GEN (三个 body CONCRETE/STEEL/SRC 共通) | `ADD_ENVELOPE` | boolean | 默认值 `true` | 可选 |
| 3 | 设计类别选择 – body 结构分支键 | `CODE_SELECTION` | string (const) | `CONCRETE` \| `STEEL` \| `SRC` | 必填 |
| 4 | 设计基准代码值. `CODE_SELECTION="CONCRETE"` 时 const/默认值 `"KDS 41 20 : 2022"` | `DGNCODE` | string (const) | `KDS 41 20 : 2022` | 必填 (在 CONCRETE body 中) |
| 4' | 设计基准代码值. `CODE_SELECTION="STEEL"` 时 const/默认值 `"KDS 41 30 : 2022"` | `DGNCODE` | string (const) | `KDS 41 30 : 2022` | 必填 (在 STEEL body 中) |
| 4'' | 设计基准代码值. `CODE_SELECTION="SRC"` 时 const/默认值 `"KDS 41 SRC : 2022"` | `DGNCODE` | string (const) | `KDS 41 SRC : 2022` | 必填 (在 SRC body 中) |
| 5 | 反应谱荷载组合列表 | `RS_SCALE_FACTOR` | array [object] | - | 必填 (三个 body 全部) |
| 5-1 | 荷载工况名 (静力: `NAME(ST)`, 反应谱: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 5-2 | 缩放系数 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 6 | 风荷载组合集. SRC body 中 `WIND_LOAD_COMB` 本身必填，CONCRETE/STEEL body 中为可选 | `WIND_LOAD_COMB` | object | - | SRC: 必填 / CONCRETE·STEEL: 可选 |
| 6-1 | 风荷载组合集列表 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 必填 (WIND_LOAD_COMB 使用时) |
| 6-1-a | 风荷载组 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 必填 |
| 6-1-b | 按风荷载方向的工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 必填 |
| 6-1-b-1 | 顺风(Along)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 可选 |
| 6-1-b-2 | 横风(Across)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 可选 |
| 6-1-b-3 | 扭转(Torsion)荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 可选 |
| 6-1-c | 阵风系数(GD) | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 最小值 0 | 可选 |
| 6-1-d | Kappa 系数 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 最小值 0 | 可选 |
| 6-2 | 扭转风荷载方向 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (默认值 `BOTH`) | 可选 |
| 7 | 正交效应考虑选项 | `ORTHO_EFFECT` | object | - | 必填 (三个 body 全部) |
| 7-1 | 是否考虑正交效应 | `ORTHO_EFFECT.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 7-2 | 正交效应方式 – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 条件性必填 |
| 7-3 | 正交荷载工况对 (Load Case1, Load Case2) – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] (长度固定为 2, `minItems`/`maxItems`=2) | - | 条件性必填 |
| 8 | 附加荷载选项容器 | `ADDITIONAL_LOAD` | object | - | 必填 (三个 body 全部) |
| 8-1 | 特殊地震作用选项 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 必填 |
| 8-1-a | 是否使用特殊地震作用 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | - | 必填 |
| 8-1-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 8-1-c | Sds – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 8-1-d | 超强系数列表 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 8-1-d-1 | 荷载工况名 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 8-1-d-2 | 缩放系数 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |
| 8-2 | 竖向地震力选项 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 必填 |
| 8-2-a | 是否考虑竖向地震力 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | - | 必填 |
| 8-2-b | 竖向力系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 最小值 0 | 条件性必填 |
| 9 | 地下结构物荷载选项. SRC body 中 `UNDERGROUND_LOAD` 本身必填，CONCRETE/STEEL body 中并非 `ADDITIONAL_LOAD` 的下级，而是独立的顶层选项(可选) | `UNDERGROUND_LOAD` | object | - | SRC: 必填 / CONCRETE·STEEL: 可选 |
| 9-1 | 是否使用地下结构物荷载 | `UNDERGROUND_LOAD.OPT_USE` | boolean | - | 必填 (UNDERGROUND_LOAD 使用时) |
| 9-2 | 地下结构物荷载缩放系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 条件性必填 |
| 9-2-a | 荷载工况名 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 9-2-b | 缩放系数 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 9-3 | 地震荷载工况列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 条件性必填 |
| 9-3-a | 地震荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 必填 |
| 9-3-b | 地震荷载工况方向 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 必填 |
| 9-3-c | 土压力荷载工况 – 地震分量 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 必填 |
| 9-3-d | 土压力荷载工况 – 静力分量 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 必填 |
| 9-4 | 地下结构物特殊荷载使用选项 – 位于 `UNDERGROUND_LOAD` 内部，与顶层 `SPECIAL_LOAD` 分列 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 可选 |
| 9-4-a | 是否使用地下结构物特殊荷载 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | - | 必填 |
| 9-4-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 9-4-c | Sds – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 9-4-d | 地下结构物特殊荷载超强系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 9-4-d-1 | 荷载工况名 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 9-4-d-2 | 缩放系数 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |
| 10 | 是否反映施工阶段分析结果 (仅存在于 CONCRETE body) | `CS_ANALYSIS` | boolean | - | 必填 (在 CONCRETE body 中) |
| 11 | 是否反映预应力损失 (仅存在于 CONCRETE body) | `PRESTRESS_LOSS` | boolean | - | 必填 (在 CONCRETE body 中) |

> **参考 – 各 body 的 required 差异汇总**
> - `CODE_SELECTION="CONCRETE"`: `OPTION`、`CODE_SELECTION`、`DGNCODE`、`RS_SCALE_FACTOR`、`ORTHO_EFFECT`、`ADDITIONAL_LOAD`、`CS_ANALYSIS`、`PRESTRESS_LOSS` 为 required(`WIND_LOAD_COMB`、`UNDERGROUND_LOAD` 为可选)。
> - `CODE_SELECTION="STEEL"`: `OPTION`、`CODE_SELECTION`、`DGNCODE`、`RS_SCALE_FACTOR`、`ORTHO_EFFECT`、`ADDITIONAL_LOAD` 为 required(`WIND_LOAD_COMB`、`UNDERGROUND_LOAD`、`CS_ANALYSIS`、`PRESTRESS_LOSS` 不存在或为可选)。
> - `CODE_SELECTION="SRC"`: `OPTION`、`CODE_SELECTION`、`DGNCODE`、`RS_SCALE_FACTOR`、`WIND_LOAD_COMB`、`ORTHO_EFFECT`、`ADDITIONAL_LOAD`、`UNDERGROUND_LOAD` 为 required(`CS_ANALYSIS`、`PRESTRESS_LOSS` 不存在)。
>
> ⚠️ 2026-08-26 确认: 第 2 行(`ADD_ENVELOPE`)的说明在旧版中写作 "仅存在于 CONCRETE/STEEL body"，
> 但经官方原文(SRC 分支亦含)复核，上述 3 个 `oneOf` 分支(CONCRETE/STEEL/SRC)均
> 同样存在 `ADD_ENVELOPE` —— 更正为三个 body 的共通字段。
> (紧接上方的 "参考" 汇总本身并未把 `ADD_ENVELOPE` 作为 body 间差异项提及，
> 因而原本就与该错误相矛盾。)

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "ADD_ENVELOPE": true,
    "CODE_SELECTION": "CONCRETE",
    "DGNCODE": "KDS 41 20 : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false },
    "CS_ANALYSIS": false,
    "PRESTRESS_LOSS": false
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-GEN generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "CODE_SELECTION": "CONCRETE",
    "DGNCODE": "KDS 41 20 : 2022",
    "GENERATED_COMB_COUNT": 24
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

# ── POST: KDS 41 20:2022 混凝土设计荷载组合自动生成 ──────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "ADD_ENVELOPE": True,
        "CODE_SELECTION": "CONCRETE",
        "DGNCODE": "KDS 41 20 : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False},
        "CS_ANALYSIS": False,
        "PRESTRESS_LOSS": False
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-GEN", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## 16. `/ope/LCOM-CONC` — Load Combination (Concrete) – KDS 41 20:2022

> **功能：** 依据 KDS 41 20:2022 混凝土结构设计基准，指定反应谱缩放系数、风荷载组合、正交效应、特殊地震作用·竖向地震力·地下结构物荷载选项，自动生成混凝土构件设计用荷载组合。为 POST 专用 Endpoint，可向既有组合追加(ADD)或整体替换(REPLACE)。

### Input URI

```
{base url}/ope/LCOM-CONC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["KDS 41 20 : 2022"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        },
        "WIND_LOAD_COMB": {
          "type": "object",
          "required": ["PARAMETERS"],
          "properties": {
            "PARAMETERS": {
              "type": "array",
              "description": "List of wind load combination sets",
              "items": {
                "type": "object",
                "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                "properties": {
                  "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                  "WIND_LOAD_CASE": {
                    "type": "object",
                    "properties": {
                      "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                      "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                      "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                    }
                  },
                  "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                  "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                }
              }
            },
            "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
          }
        },
        "ORTHO_EFFECT": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
            "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
            "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
          }
        },
        "ADDITIONAL_LOAD": {
          "type": "object",
          "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
          "properties": {
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Special Seismic Load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                }
              }
            },
            "VERTICAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Vertical Seismic Forces" },
                "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
              }
            }
          }
        },
        "UNDERGROUND_LOAD": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "for Underground Load" },
            "SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "LOAD_CASE_LIST": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                  "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                  "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                  "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                }
              }
            },
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use special load for underground load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  },
                  "description": "Over-strength factors for underground special load"
                }
              }
            }
          }
        },
        "CS_ANALYSIS": { "type": "boolean", "default": false },
        "PRESTRESS_LOSS": { "type": "boolean", "default": false }
      }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|---|---|---|---|---|---|
| 1 | OPTION – 是向既有组合追加还是整体替换 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 必填 |
| 2 | 混凝土设计基准代码值 | `DGNCODE` | string (enum) | `KDS 41 20 : 2022` | 必填 |
| 3 | 反应谱荷载组合列表 | `RS_SCALE_FACTOR` | array [object] | - | 可选 |
| 3-1 | 荷载工况名 (静力: `NAME(ST)`, 反应谱: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 3-2 | 缩放系数 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 4 | 风荷载组合集 | `WIND_LOAD_COMB` | object | - | 可选 |
| 4-1 | 风荷载组合集列表 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 必填 (WIND_LOAD_COMB 使用时) |
| 4-1-a | 风荷载组 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 必填 |
| 4-1-b | 按风荷载方向(Wind Direction)的工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 必填 |
| 4-1-b-1 | 顺风(Along)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 可选 |
| 4-1-b-2 | 横风(Across)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 可选 |
| 4-1-b-3 | 扭转(Torsion)荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 可选 |
| 4-1-c | 阵风系数 | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 最小值 0 | 可选 |
| 4-1-d | Kappa 系数 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 最小值 0 | 可选 |
| 4-2 | 扭转风荷载方向 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (默认值 `BOTH`) | 可选 |
| 5 | 正交效应考虑选项 | `ORTHO_EFFECT` | object | - | 可选 |
| 5-1 | 是否考虑正交效应 | `ORTHO_EFFECT.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 5-2 | 正交效应方式 – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 条件性必填 |
| 5-3 | 正交荷载工况对 (长度固定为 2) – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] | - | 条件性必填 |
| 6 | 附加荷载选项容器 | `ADDITIONAL_LOAD` | object | - | 可选 |
| 6-1 | 特殊地震作用选项 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 必填 (ADDITIONAL_LOAD 使用时) |
| 6-1-a | 是否使用特殊地震作用 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 6-1-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 6-1-c | Sds – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 6-1-d | 超强系数列表 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 6-1-d-1 | 荷载工况名 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 6-1-d-2 | 缩放系数 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |
| 6-2 | 竖向地震力选项 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 必填 (ADDITIONAL_LOAD 使用时) |
| 6-2-a | 是否考虑竖向地震力 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 6-2-b | 竖向力系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 最小值 0 | 条件性必填 |
| 7 | 地下结构物荷载选项 | `UNDERGROUND_LOAD` | object | - | 可选 |
| 7-1 | 是否使用地下结构物荷载 | `UNDERGROUND_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 (UNDERGROUND_LOAD 使用时) |
| 7-2 | 地下结构物荷载缩放系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 条件性必填 |
| 7-2-a | 荷载工况名 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 7-2-b | 缩放系数 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 7-3 | 地震荷载工况列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 条件性必填 |
| 7-3-a | 荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 必填 |
| 7-3-b | 地震荷载工况方向 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 必填 |
| 7-3-c | 地震分量土压力荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 必填 |
| 7-3-d | 静力分量土压力荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 必填 |
| 7-4 | 地下结构物特殊荷载使用选项 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 可选 |
| 7-4-a | 是否使用地下结构物特殊荷载 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 7-4-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 7-4-c | Sds – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 7-4-d | 地下结构物特殊荷载超强系数列表(说明: Over-strength factors) – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 7-4-d-1 | 荷载工况名 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 7-4-d-2 | 缩放系数 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |
| 8 | 是否反映施工阶段分析结果 | `CS_ANALYSIS` | boolean | 默认值 `false` | 可选 |
| 9 | 是否反映预应力损失 | `PRESTRESS_LOSS` | boolean | 默认值 `false` | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 20 : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false },
    "CS_ANALYSIS": false,
    "PRESTRESS_LOSS": false
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-CONC generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 20 : 2022",
    "GENERATED_COMB_COUNT": 18
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

# ── POST: KDS 41 20:2022 混凝土设计荷载组合自动生成 ──────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS 41 20 : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False},
        "CS_ANALYSIS": False,
        "PRESTRESS_LOSS": False
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-CONC", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## 17. `/ope/LCOM-STEEL` — Load Combination (Steel) – KDS 41 30:2022

> **功能：** 依据 KDS 41 30:2022 钢结构设计基准，指定反应谱缩放系数、风荷载组合、正交效应、特殊地震作用·竖向地震力·地下结构物荷载选项，自动生成钢结构构件设计用荷载组合。为 POST 专用 Endpoint，可向既有组合追加(ADD)或整体替换(REPLACE)。与 LCOM-CONC 的模式结构相同，但不存在 `CS_ANALYSIS`、`PRESTRESS_LOSS` 字段。

### Input URI

```
{base url}/ope/LCOM-STEEL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["KDS 41 30 : 2022"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        },
        "WIND_LOAD_COMB": {
          "type": "object",
          "required": ["PARAMETERS"],
          "properties": {
            "PARAMETERS": {
              "type": "array",
              "description": "List of wind load combination sets",
              "items": {
                "type": "object",
                "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                "properties": {
                  "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                  "WIND_LOAD_CASE": {
                    "type": "object",
                    "properties": {
                      "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                      "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                      "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                    }
                  },
                  "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                  "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                }
              }
            },
            "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
          }
        },
        "ORTHO_EFFECT": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
            "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
            "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
          }
        },
        "ADDITIONAL_LOAD": {
          "type": "object",
          "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
          "properties": {
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Special Seismic Load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                }
              }
            },
            "VERTICAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Vertical Seismic Forces" },
                "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
              }
            }
          }
        },
        "UNDERGROUND_LOAD": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "for Underground Load" },
            "SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "LOAD_CASE_LIST": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                  "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                  "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                  "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                }
              }
            },
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use special load for underground load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  },
                  "description": "Over-strength factors for underground special load"
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

### Parameters

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|---|---|---|---|---|---|
| 1 | OPTION – 是向既有组合追加还是整体替换 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 必填 |
| 2 | 钢结构设计基准代码值 | `DGNCODE` | string (enum) | `KDS 41 30 : 2022` | 必填 |
| 3 | 反应谱荷载组合列表 | `RS_SCALE_FACTOR` | array [object] | - | 可选 |
| 3-1 | 荷载工况名 (静力: `NAME(ST)`, 反应谱: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 3-2 | 缩放系数 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 4 | 风荷载组合集 | `WIND_LOAD_COMB` | object | - | 可选 |
| 4-1 | 风荷载组合集列表 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 必填 (WIND_LOAD_COMB 使用时) |
| 4-1-a | 风荷载组 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 必填 |
| 4-1-b | WIND_LOAD_CASE 容器 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 必填 |
| 4-1-b-1 | 顺风(Along)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 可选 |
| 4-1-b-2 | 横风(Across)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 可选 |
| 4-1-b-3 | 扭转(Torsion)荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 可选 |
| 4-1-c | 阵风系数 | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 最小值 0 | 可选 |
| 4-1-d | Kappa 系数 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 最小值 0 | 可选 |
| 4-2 | 扭转风荷载方向 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (默认值 `BOTH`) | 可选 |
| 5 | 正交效应考虑选项 | `ORTHO_EFFECT` | object | - | 可选 |
| 5-1 | 是否考虑正交效应 | `ORTHO_EFFECT.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 5-2 | 正交效应方式 – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 条件性必填 |
| 5-3 | 正交荷载工况对 (长度固定为 2) – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] | - | 条件性必填 |
| 6 | 附加荷载选项容器 | `ADDITIONAL_LOAD` | object | - | 可选 |
| 6-1 | 特殊地震作用选项 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 必填 (ADDITIONAL_LOAD 使用时) |
| 6-1-a | 是否使用特殊地震作用 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 6-1-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 6-1-c | Sds – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 6-1-d | Over Strength Factor 列表 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 6-1-d-1 | 荷载工况名 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 6-1-d-2 | 缩放系数 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |
| 6-2 | 竖向地震力选项 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 必填 (ADDITIONAL_LOAD 使用时) |
| 6-2-a | 是否考虑竖向地震力 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 6-2-b | 竖向力系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 最小值 0 | 条件性必填 |
| 7 | 地下结构物荷载选项 | `UNDERGROUND_LOAD` | object | - | 可选 |
| 7-1 | 是否使用地下结构物荷载 | `UNDERGROUND_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 (UNDERGROUND_LOAD 使用时) |
| 7-2 | 地下结构物荷载缩放系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 条件性必填 |
| 7-2-a | 荷载工况名 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 7-2-b | 缩放系数 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 7-3 | 地震荷载工况列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 条件性必填 |
| 7-3-a | 荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 必填 |
| 7-3-b | 地震荷载工况方向 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 必填 |
| 7-3-c | 地震分量土压力荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 必填 |
| 7-3-d | 静力分量土压力荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 必填 |
| 7-4 | 地下结构物特殊荷载使用选项 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 可选 |
| 7-4-a | 是否使用地下结构物特殊荷载 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 7-4-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 7-4-c | Sds – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 7-4-d | 地下结构物特殊荷载超强系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 7-4-d-1 | 荷载工况名 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 7-4-d-2 | 缩放系数 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 30 : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false }
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-STEEL generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 30 : 2022",
    "GENERATED_COMB_COUNT": 16
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

# ── POST: KDS 41 30:2022 钢结构设计荷载组合自动生成 ────────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS 41 30 : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False}
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-STEEL", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## 18. `/ope/LCOM-SRC` — Load Combination (SRC) – KDS 41 SRC:2022 / AIK-SRC2K

> **功能：** 依据 KDS 41 SRC:2022 组合结构(钢管混凝土/埋入型钢等)设计基准，指定反应谱缩放系数、风荷载组合、正交效应、特殊地震作用·竖向地震力·地下结构物荷载选项，自动生成 SRC 构件设计用荷载组合。为 POST 专用 Endpoint，可向既有组合追加(ADD)或整体替换(REPLACE)。同一 Endpoint 也支持指定 `DGNCODE: "AIK-SRC2K"` 的更简化模式(`OPTION` + `DGNCODE` + `RS_SCALE_FACTOR`)，其在本文下方 "LCOM-GEN/SRC AIK-SRC2K 变体模式" 一节中说明。本节仅处理 KDS 41 SRC:2022 变体。

### Input URI

```
{base url}/ope/LCOM-SRC
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["KDS 41 SRC : 2022"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        },
        "WIND_LOAD_COMB": {
          "type": "object",
          "required": ["PARAMETERS"],
          "properties": {
            "PARAMETERS": {
              "type": "array",
              "description": "List of wind load combination sets",
              "items": {
                "type": "object",
                "required": ["BUILDING_TYPE", "WIND_LOAD_CASE"],
                "properties": {
                  "BUILDING_TYPE": { "type": "string", "enum": ["MIDDLE", "HIGH"], "description": "Wind Loads Group" },
                  "WIND_LOAD_CASE": {
                    "type": "object",
                    "properties": {
                      "ALONG": { "type": "string", "description": "Along Wind Load Case" },
                      "ACROSS": { "type": "string", "description": "Across Wind Load Case" },
                      "TORSION": { "type": "string", "description": "Torsional Wind Load Case" }
                    }
                  },
                  "GUST_FACTOR": { "type": "number", "minimum": 0, "description": "GD" },
                  "KAPPA_FACTOR": { "type": "number", "minimum": 0, "description": "Kappa" }
                }
              }
            },
            "TORSION_DIR": { "type": "string", "enum": ["BOTH", "POSITIVE", "NEGATIVE"], "default": "BOTH", "description": "Torsion Wind Direction" }
          }
        },
        "ORTHO_EFFECT": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "Consider Orthogonal Effect" },
            "TYPE": { "type": "string", "enum": ["100_30", "SRSS"], "description": "Orthogonal Effect Type" },
            "LOAD_GROUP": { "type": "array", "minItems": 2, "maxItems": 2, "items": { "type": "string" }, "description": "Load Case1, Load Case2" }
          }
        },
        "ADDITIONAL_LOAD": {
          "type": "object",
          "required": ["SPECIAL_LOAD", "VERTICAL_LOAD"],
          "properties": {
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Special Seismic Load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  }
                }
              }
            },
            "VERTICAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "for Vertical Seismic Forces" },
                "FORCE_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Force Factor" }
              }
            }
          }
        },
        "UNDERGROUND_LOAD": {
          "type": "object",
          "required": ["OPT_USE"],
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false, "description": "for Underground Load" },
            "SCALE_FACTOR": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "FACTOR"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Load Case" },
                  "FACTOR": { "type": "number", "description": "Scale Factor" }
                }
              }
            },
            "LOAD_CASE_LIST": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["LOAD_CASE", "DIRECTION", "LOAD_CASE_SEISMIC", "LOAD_CASE_STATIC"],
                "properties": {
                  "LOAD_CASE": { "type": "string", "description": "Seismic Load Case List - LoadCase" },
                  "DIRECTION": { "type": "string", "enum": ["POSITIVE", "NEGATIVE"], "description": "Seismic Load Case List - Direction" },
                  "LOAD_CASE_SEISMIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Seismic" },
                  "LOAD_CASE_STATIC": { "type": "array", "items": { "type": "string" }, "description": "Earth Pressure Load Case - Static" }
                }
              }
            },
            "SPECIAL_LOAD": {
              "type": "object",
              "required": ["OPT_USE"],
              "properties": {
                "OPT_USE": { "type": "boolean", "default": false, "description": "Whether to use special load for underground load" },
                "VERTICAL_LOAD_FACTOR": { "type": "number", "minimum": 0, "description": "Vertical Load Factor" },
                "SDS": { "type": "number", "minimum": 0, "description": "Sds" },
                "OVER_STRENGTH_FACTOR": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": ["LOAD_CASE", "FACTOR"],
                    "properties": {
                      "LOAD_CASE": { "type": "string", "description": "Load Case" },
                      "FACTOR": { "type": "number", "description": "Scale Factor" }
                    }
                  },
                  "description": "Over-strength factors for underground special load"
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

### Parameters

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|---|---|---|---|---|---|
| 1 | OPTION – 是向既有组合追加还是整体替换 | `OPTION` | string (enum) | `ADD`, `REPLACE` | 必填 |
| 2 | SRC 设计基准代码值 | `DGNCODE` | string (enum) | `KDS 41 SRC : 2022` | 必填 |
| 3 | 反应谱荷载组合列表 | `RS_SCALE_FACTOR` | array [object] | - | 可选 |
| 3-1 | 荷载工况名 (静力: `NAME(ST)`, 反应谱: `NAME(RS)`) | `RS_SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 3-2 | 缩放系数 | `RS_SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 4 | 风荷载组合集 | `WIND_LOAD_COMB` | object | - | 可选 |
| 4-1 | 风荷载组合集列表 | `WIND_LOAD_COMB.PARAMETERS` | array [object] | - | 必填 (WIND_LOAD_COMB 使用时) |
| 4-1-a | 风荷载组 | `WIND_LOAD_COMB.PARAMETERS[].BUILDING_TYPE` | string (enum) | `MIDDLE`, `HIGH` | 必填 |
| 4-1-b | 按风荷载方向(Wind Direction)的工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE` | object | - | 必填 |
| 4-1-b-1 | 顺风(Along)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ALONG` | string | - | 可选 |
| 4-1-b-2 | 横风(Across)方向荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.ACROSS` | string | - | 可选 |
| 4-1-b-3 | 扭转(Torsion)荷载工况 | `WIND_LOAD_COMB.PARAMETERS[].WIND_LOAD_CASE.TORSION` | string | - | 可选 |
| 4-1-c | 阵风系数 | `WIND_LOAD_COMB.PARAMETERS[].GUST_FACTOR` | number | 最小值 0 | 可选 |
| 4-1-d | Kappa 系数 | `WIND_LOAD_COMB.PARAMETERS[].KAPPA_FACTOR` | number | 最小值 0 | 可选 |
| 4-2 | 扭转风荷载方向 | `WIND_LOAD_COMB.TORSION_DIR` | string (enum) | `BOTH`, `POSITIVE`, `NEGATIVE` (默认值 `BOTH`) | 可选 |
| 5 | 正交效应考虑选项 | `ORTHO_EFFECT` | object | - | 可选 |
| 5-1 | 是否考虑正交效应 | `ORTHO_EFFECT.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 5-2 | 正交效应方式 – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.TYPE` | string (enum) | `100_30`, `SRSS` | 条件性必填 |
| 5-3 | 正交荷载工况对 (长度固定为 2) – `ORTHO_EFFECT.OPT_USE`为 `true` 时必填 | `ORTHO_EFFECT.LOAD_GROUP` | array [string] | - | 条件性必填 |
| 6 | 附加荷载选项容器 | `ADDITIONAL_LOAD` | object | - | 可选 |
| 6-1 | 特殊地震作用选项 | `ADDITIONAL_LOAD.SPECIAL_LOAD` | object | - | 必填 (ADDITIONAL_LOAD 使用时) |
| 6-1-a | 是否使用特殊地震作用 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 6-1-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 6-1-c | Sds – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 6-1-d | Over strength factor 列表 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 6-1-d-1 | 荷载工况名 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 6-1-d-2 | 缩放系数 | `ADDITIONAL_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |
| 6-2 | 竖向地震力选项 | `ADDITIONAL_LOAD.VERTICAL_LOAD` | object | - | 必填 (ADDITIONAL_LOAD 使用时) |
| 6-2-a | 是否考虑竖向地震力 | `ADDITIONAL_LOAD.VERTICAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 6-2-b | 竖向力系数 – `OPT_USE`为 `true` 时必填 | `ADDITIONAL_LOAD.VERTICAL_LOAD.FORCE_FACTOR` | number | 最小值 0 | 条件性必填 |
| 7 | 地下结构物荷载选项 | `UNDERGROUND_LOAD` | object | - | 可选 |
| 7-1 | 是否使用地下结构物荷载 | `UNDERGROUND_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 (UNDERGROUND_LOAD 使用时) |
| 7-2 | 地下结构物荷载缩放系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SCALE_FACTOR` | array [object] | - | 条件性必填 |
| 7-2-a | 荷载工况名 | `UNDERGROUND_LOAD.SCALE_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 7-2-b | 缩放系数 | `UNDERGROUND_LOAD.SCALE_FACTOR[].FACTOR` | number | - | 必填 |
| 7-3 | 地震荷载工况列表(Seismic Load Case List) – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.LOAD_CASE_LIST` | array [object] | - | 条件性必填 |
| 7-3-a | 荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE` | string | - | 必填 |
| 7-3-b | 地震荷载工况方向 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].DIRECTION` | string (enum) | `POSITIVE`, `NEGATIVE` | 必填 |
| 7-3-c | 地震分量土压力荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_SEISMIC` | array [string] | - | 必填 |
| 7-3-d | 静力分量土压力荷载工况名 | `UNDERGROUND_LOAD.LOAD_CASE_LIST[].LOAD_CASE_STATIC` | array [string] | - | 必填 |
| 7-4 | 地下结构物特殊荷载使用选项 | `UNDERGROUND_LOAD.SPECIAL_LOAD` | object | - | 可选 |
| 7-4-a | 是否使用地下结构物特殊荷载 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OPT_USE` | boolean | 默认值 `false` | 必填 |
| 7-4-b | 竖向荷载系数 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.VERTICAL_LOAD_FACTOR` | number | 最小值 0 | 条件性必填 |
| 7-4-c | Sds – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.SDS` | number | 最小值 0 | 条件性必填 |
| 7-4-d | 地下结构物特殊荷载超强系数列表 – `OPT_USE`为 `true` 时必填 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR` | array [object] | - | 条件性必填 |
| 7-4-d-1 | 荷载工况名 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].LOAD_CASE` | string | - | 必填 |
| 7-4-d-2 | 缩放系数 | `UNDERGROUND_LOAD.SPECIAL_LOAD.OVER_STRENGTH_FACTOR[].FACTOR` | number | - | 必填 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 SRC : 2022",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ],
    "WIND_LOAD_COMB": {
      "PARAMETERS": [
        {
          "BUILDING_TYPE": "HIGH",
          "WIND_LOAD_CASE": { "ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)" },
          "GUST_FACTOR": 2.2,
          "KAPPA_FACTOR": 0.55
        }
      ],
      "TORSION_DIR": "BOTH"
    },
    "ORTHO_EFFECT": {
      "OPT_USE": true,
      "TYPE": "100_30",
      "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
    },
    "ADDITIONAL_LOAD": {
      "SPECIAL_LOAD": {
        "OPT_USE": true,
        "VERTICAL_LOAD_FACTOR": 0.2,
        "SDS": 0.5,
        "OVER_STRENGTH_FACTOR": [
          { "LOAD_CASE": "RX(RS)", "FACTOR": 2.5 },
          { "LOAD_CASE": "RY(RS)", "FACTOR": 2.5 }
        ]
      },
      "VERTICAL_LOAD": { "OPT_USE": true, "FORCE_FACTOR": 0.2 }
    },
    "UNDERGROUND_LOAD": { "OPT_USE": false }
  }
}
```

**POST Response Body**

```json
{
  "message": "LCOM-SRC generated successfully.",
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "KDS 41 SRC : 2022",
    "GENERATED_COMB_COUNT": 20
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

# ── POST: KDS 41 SRC:2022 组合结构设计荷载组合自动生成 ─────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS 41 SRC : 2022",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ],
        "WIND_LOAD_COMB": {
            "PARAMETERS": [
                {
                    "BUILDING_TYPE": "HIGH",
                    "WIND_LOAD_CASE": {"ALONG": "WX", "ACROSS": "WX(A)", "TORSION": "WX(T)"},
                    "GUST_FACTOR": 2.2,
                    "KAPPA_FACTOR": 0.55
                }
            ],
            "TORSION_DIR": "BOTH"
        },
        "ORTHO_EFFECT": {
            "OPT_USE": True,
            "TYPE": "100_30",
            "LOAD_GROUP": ["RX(RS)", "RY(RS)"]
        },
        "ADDITIONAL_LOAD": {
            "SPECIAL_LOAD": {
                "OPT_USE": True,
                "VERTICAL_LOAD_FACTOR": 0.2,
                "SDS": 0.5,
                "OVER_STRENGTH_FACTOR": [
                    {"LOAD_CASE": "RX(RS)", "FACTOR": 2.5},
                    {"LOAD_CASE": "RY(RS)", "FACTOR": 2.5}
                ]
            },
            "VERTICAL_LOAD": {"OPT_USE": True, "FORCE_FACTOR": 0.2}
        },
        "UNDERGROUND_LOAD": {"OPT_USE": False}
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-SRC", json=payload, headers=HEADERS)
resp.raise_for_status()
print(resp.json())
```

---

## LCOM-GEN/SRC AIK-SRC2K 变体模式

`DGNCODE` 为 `"AIK-SRC2K"` 时，`/ope/LCOM-GEN`、`/ope/LCOM-SRC` 使用下方简化后的模式(与上方第 15·18 节的 KDS:2022 模式相互独立)。

### JSON Schema (通用)

```json
{
  "type": "object",
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["OPTION", "DGNCODE"],
      "properties": {
        "OPTION": { "type": "string", "enum": ["ADD", "REPLACE"] },
        "DGNCODE": { "type": "string", "enum": ["AIK-SRC2K"] },
        "RS_SCALE_FACTOR": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["LOAD_CASE", "FACTOR"],
            "properties": {
              "LOAD_CASE": { "type": "string", "description": "Response Spectrum Load Case" },
              "FACTOR": { "type": "number", "description": "Scale Factor" }
            }
          }
        }
      }
    }
  }
}
```

> ⚠️ 2026-08-26 确认: 上述模式的 `required: ["OPTION", "DGNCODE"]` 以 `/ope/LCOM-SRC`
> (AIK-SRC2K) 为准。`/ope/LCOM-GEN`(AIK-SRC2K) 的官方模式为
> `required: ["OPTION", "DGNCODE", "RS_SCALE_FACTOR"]`，`RS_SCALE_FACTOR` 也是必填 —
> 两个 Endpoint 仅此一字的必填与否不同、其余结构相同，故合并标注为 "通用" 模式，
> 但注意不要将其原样用作 `/ope/LCOM-GEN` 的校验模式。下方 Parameters
> 表第 3 行已反映该差异。

### Parameters

| No. | 说明 | Key | 值类型 | 必填 |
|-----|------|-----|-----------|------|
| 1 | 处理方式 · 追加: `"ADD"` / 替换: `"REPLACE"` | `"OPTION"` | String (enum) | **Required** |
| 2 | 设计代码 · `"AIK-SRC2K"` | `"DGNCODE"` | String (enum) | **Required** |
| 3 | 各反应谱荷载工况的倍率列表 (`/ope/LCOM-GEN`端为 **Required**, `/ope/LCOM-SRC`端为 Optional) | `"RS_SCALE_FACTOR"` | Array [Object] | 按 Endpoint 而异 |
| 3-1 | └ 荷载工况名 · 静力: `NAME(ST)` / 反应谱: `NAME(RS)` | `RS_SCALE_FACTOR[].LOAD_CASE` | String | **Required** |
| 3-2 | └ 倍率 | `RS_SCALE_FACTOR[].FACTOR` | Number | **Required** |

### Request Body 示例

**`/ope/LCOM-GEN` (AIK-SRC2K)**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "AIK-SRC2K",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1 }
    ]
  }
}
```

**`/ope/LCOM-SRC` (AIK-SRC2K)**

```json
{
  "Argument": {
    "OPTION": "ADD",
    "DGNCODE": "AIK-SRC2K",
    "RS_SCALE_FACTOR": [
      { "LOAD_CASE": "RX(RS)", "FACTOR": 1.2 },
      { "LOAD_CASE": "RY(RS)", "FACTOR": 1.3 }
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

# ── POST: 按 AIK-SRC2K 基准自动生成一般荷载组合 ───────────────────
payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "AIK-SRC2K",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1}
        ]
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-GEN", json=payload, headers=HEADERS)
print("POST (LCOM-GEN, AIK-SRC2K):", resp.status_code, resp.json())

# ── POST: 按 AIK-SRC2K 基准自动生成 SRC 荷载组合 ────────────────────
payload2 = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "AIK-SRC2K",
        "RS_SCALE_FACTOR": [
            {"LOAD_CASE": "RX(RS)", "FACTOR": 1.2},
            {"LOAD_CASE": "RY(RS)", "FACTOR": 1.3}
        ]
    }
}
resp = requests.post(f"{BASE_URL}/ope/LCOM-SRC", json=payload2, headers=HEADERS)
print("POST (LCOM-SRC, AIK-SRC2K):", resp.status_code, resp.json())
```

---

## 19. `/ope/GSBG` — Bridge Girder Diagram Image Generation

> ℹ️ **2026-07-14 确认:** 已作为 [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual) 官方概述目录 OPE 部分第 19 项正式建立链接，2026-07-12 登记时的 "待确认" 状态已解除。但在此期间(2026-07-12 → 2026-07-14)官方文章自身的模式发生变更，故下文已更新为最新版 —— 主要变更点是 **删除 `LC_TYPE` 字段**(仅用 `LC_NAME`)与 **`BATCH_LIST` 由对象数组(`{BRDG_GROUP, SF, GROUP}`)改为字符串数组**。若此前按该模式编写了联调代码，则必须更新。
>
> **功能：** 生成桥梁主梁(Bridge Girder)的应力(Stress)/构件内力(Force)图图像并保存为文件。 与 `/db/GSBG`(DB 部分，图的查询/设置)是不同的 Endpoint，本端是**仅用于生成图像文件的 OPE 命令**。

### Input URI

```
{base url}/ope/GSBG
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["Argument"],
  "properties": {
    "Argument": {
      "type": "object",
      "additionalProperties": false,
      "required": ["LC_NAME", "DGRM_TYPE", "STAGE_LIST", "EXPORT_PATH", "EXTENSION"],
      "properties": {
        "LC_NAME": { "type": "string", "description": "Load Case/Combination name" },
        "DGRM_TYPE": { "type": "integer", "enum": [0, 1], "description": "0: Stress, 1: Force" },
        "BATCH": { "type": "boolean", "default": true, "description": "생략 시 true로 처리" },
        "X_AXIS_TYPE": { "type": "integer", "enum": [0, 1], "default": 0, "description": "0: Distance, 1: Node" },
        "BRDG_GROUP": { "type": "string", "description": "Bridge Girder Element Group (BATCH=false일 때만 사용)" },
        "COMPONENTS": { "type": "integer", "default": 0, "description": "Component. DGRM_TYPE에 따라 허용 enum 값이 다름 (아래 allOf 참고)" },
        "7TH_DOF_TYPE": { "type": "integer", "enum": [0, 1, 2, 3, 4, 5, 6], "default": 0, "description": "DGRM_TYPE=Stress·COMPONENTS=7th DOF일 때만 사용" },
        "COMBINED_COMP": { "type": "integer", "enum": [0, 1, 2, 3, 4], "default": 0, "description": "DGRM_TYPE=Stress·COMPONENTS=Combined일 때만 사용" },
        "STRESS_LINE": {
          "type": "object",
          "additionalProperties": false,
          "description": "허용응력선 (COMP/TENS 단위는 현재 시스템 단위 설정을 따름)",
          "properties": {
            "OPT_USE": { "type": "boolean", "default": false },
            "COMP": { "type": "integer", "description": "허용 압축응력" },
            "TENS": { "type": "integer", "description": "허용 인장응력" }
          }
        },
        "BATCH_LIST": {
          "type": "array",
          "minItems": 1,
          "description": "Batch 출력 그룹명 목록. BATCH=true(또는 생략) 시 각 항목은 문자열 그룹명 그대로 입력",
          "items": { "type": "string", "minLength": 1 }
        },
        "STAGE_LIST": { "type": "array", "minItems": 1, "items": { "type": "string" }, "description": "다이어그램을 생성할 시공단계 목록" },
        "EXPORT_PATH": { "type": "string", "description": "생성된 이미지의 저장 경로" },
        "EXTENSION": { "type": "string", "enum": ["bmp", "jpg", "emf"], "description": "저장할 이미지 파일 확장자" }
      },
      "allOf": [
        { "x-branch-label": "DGRM_TYPE = Stress일 때 COMPONENTS enum = 0(Sax)/1(+Sby)/2(-Sby)/3(+Sbz)/4(-Sbz)/5(Combined)/6(7th DOF)" },
        { "x-branch-label": "DGRM_TYPE = Force일 때 COMPONENTS enum = 0(Fx)/1(Fy)/2(Fz)/3(Mx)/4(My)/5(Mz)/6(Mb)/7(Mt)/8(Mw)" },
        { "x-branch-label": "BATCH=true(또는 생략) 시 BATCH_LIST 필수, BRDG_GROUP·COMPONENTS·7TH_DOF_TYPE·COMBINED_COMP는 최상위에 허용되지 않음" },
        { "x-branch-label": "BATCH=false 시 BRDG_GROUP 필수, BATCH_LIST 허용 안 됨" },
        { "x-branch-label": "DGRM_TYPE=Force일 때 STRESS_LINE 허용 안 됨" },
        { "x-branch-label": "7TH_DOF_TYPE은 DGRM_TYPE=Stress & COMPONENTS=6(7th DOF)일 때만 허용" },
        { "x-branch-label": "COMBINED_COMP는 DGRM_TYPE=Stress & COMPONENTS=5(Combined)일 때만 허용" }
      ]
    }
  }
}
```

### Parameters

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|-----------|---------|----------|
| 1 | Load Case/Combination Name | `"LC_NAME"` | String | – | Required |
| 2 | Diagram Type (Stress: `0` / Force: `1`) | `"DGRM_TYPE"` | Integer | – | Required |
| 3 | Batch Option (省略时 true) | `"BATCH"` | Boolean | true | Optional |
| 4 | X-Axis Type (Distance: `0` / Node: `1`) | `"X_AXIS_TYPE"` | Integer | 0 | Optional |
| 5 | Batch Output Group-Name List (`BATCH=true` 时，各项按原样填字符串) | `"BATCH_LIST"` | Array[String] | – | Required (`BATCH=true`) |
| 6 | Bridge Girder Element Group (`BATCH=false` 时) | `"BRDG_GROUP"` | String | – | Required (`BATCH=false`) |
| 7 | Component — Stress(`DGRM_TYPE=0`): Sax:0/+Sby:1/-Sby:2/+Sbz:3/-Sbz:4/Combined:5/7th DOF:6, Force(`DGRM_TYPE=1`): Fx:0/Fy:1/Fz:2/Mx:3/My:4/Mz:5/Mb:6/Mt:7/Mw:8 | `"COMPONENTS"` | Integer | 0 | Optional |
| 8 | Location for Display of Stress (`BATCH=false`, `DGRM_TYPE=0`, `COMPONENTS=5`) — Max:0 / 1(-y,+z):1 / 2(+y,+z):2 / 3(+y,-z):3 / 4(-y,-z):4 | `"COMBINED_COMP"` | Integer | 0 | Optional |
| 9 | 7th DOF Type (`BATCH=false`, `DGRM_TYPE=0`, `COMPONENTS=6`) — Sax(Warping):0 / Ssy(Mt):1 / Ssy(Mw):2 / Ssz(Mt):3 / Ssz(Mw):4 / Combined(Ssy):5 / Combined(Ssz):6 | `"7TH_DOF_TYPE"` | Integer | 0 | Optional |
| 10 | Allowable Stress Line (仅 `DGRM_TYPE=0` 时) | `"STRESS_LINE"` | Object | – | Optional |
| 10-(1) | Draw Allowable Stress Line | `"STRESS_LINE.OPT_USE"` | Boolean | false | Optional |
| 10-(2) | Allowable Compression Stress (`OPT_USE=true`) | `"STRESS_LINE.COMP"` | Integer | – | Required |
| 10-(3) | Allowable Tension Stress (`OPT_USE=true`) | `"STRESS_LINE.TENS"` | Integer | – | Required |
| 11 | Stage List for Diagram Generation | `"STAGE_LIST"` | Array[String] | – | Required |
| 12 | Export Path | `"EXPORT_PATH"` | String | – | Required |
| 13 | Export Image File Extension (`"bmp"` / `"jpg"` / `"emf"`) | `"EXTENSION"` | String | – | Required |

### Request Examples

**Stress, BATCH = true**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 0,
    "BATCH": true,
    "X_AXIS_TYPE": 1,
    "STRESS_LINE": { "OPT_USE": true, "COMP": 210000, "TENS": 180000 },
    "BATCH_LIST": ["Stress_Combined_Left", "Stress_7thDOF_Right", "Stress_Girder_Center"],
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\StressBatch",
    "EXTENSION": "jpg"
  }
}
```

**Stress, BATCH = false**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 0,
    "BATCH": false,
    "X_AXIS_TYPE": 1,
    "BRDG_GROUP": "BG_LEFT",
    "COMPONENTS": 6,
    "7TH_DOF_TYPE": 6,
    "STRESS_LINE": { "OPT_USE": true, "COMP": 210000, "TENS": 180000 },
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\StressSingle",
    "EXTENSION": "emf"
  }
}
```

**Force, BATCH = true**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 1,
    "BATCH": true,
    "X_AXIS_TYPE": 0,
    "BATCH_LIST": ["Force_Left_Girder", "Force_Right_Girder", "Force_Center_Girder"],
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\ForceBatch",
    "EXTENSION": "bmp"
  }
}
```

**Force, BATCH = false**

```json
{
  "Argument": {
    "LC_NAME": "Dead Load",
    "DGRM_TYPE": 1,
    "BATCH": false,
    "X_AXIS_TYPE": 0,
    "BRDG_GROUP": "BG_RIGHT",
    "COMPONENTS": 8,
    "STAGE_LIST": ["CS1", "CS2"],
    "EXPORT_PATH": "C:\\Temp\\GSBG\\ForceSingle",
    "EXTENSION": "jpg"
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

# ── POST: 批量生成主梁应力图图像 ─────────────────────
payload = {
    "Argument": {
        "LC_NAME": "Dead Load",
        "DGRM_TYPE": 0,
        "BATCH": True,
        "X_AXIS_TYPE": 1,
        "STRESS_LINE": {"OPT_USE": True, "COMP": 210000, "TENS": 180000},
        "BATCH_LIST": ["Stress_Combined_Left", "Stress_7thDOF_Right", "Stress_Girder_Center"],
        "STAGE_LIST": ["CS1", "CS2"],
        "EXPORT_PATH": "C:\\Temp\\GSBG\\StressBatch",
        "EXTENSION": "jpg",
    }
}
resp = requests.post(f"{BASE_URL}/ope/GSBG", json=payload, headers=HEADERS)
print("POST (GSBG):", resp.status_code, resp.json())
```

---

## End-to-End Workflow

以下为模型前处理(网格划分·构件指派)及设计荷载组合自动生成的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 确认项目现状 ─────────────────────────────────────
r1 = requests.get(f"{BASE_URL}/ope/PROJECTSTATUS", headers=HEADERS)
print(f"STEP1 PROJECTSTATUS: {r1.status_code}")

# ── STEP 2: 平面区域自动划分网格 ────────────────────────────────────
mesh_payload = {
    "Argument": {
        "MESHER": {"METHOD": "PlanarElements", "TARGETS": [1401]},
        "MESH_SIZE": {"LENGTH": 1},
        "PROPERTY": {"ELEMENT_TYPE": "Plate", "MATERIAL": 1, "THICKNESS": 1},
        "DOMAIN_NAME": {"NAME": "Slab_1F"}
    }
}
r2 = requests.post(f"{BASE_URL}/ope/AUTOMESH", json=mesh_payload, headers=HEADERS)
print(f"STEP2 AUTOMESH: {r2.status_code}")

# ── STEP 3: 构件(Member)自动指派 ─────────────────────────────────
memb_payload = {"Argument": {"ASSIGN_TYPE": "AUTO", "SELECTION_TYPE": "ALL", "ALLOW_SINGLE": True}}
r3 = requests.post(f"{BASE_URL}/ope/MEMB", json=memb_payload, headers=HEADERS)
print(f"STEP3 MEMB: {r3.status_code}")

# ── STEP 4: 设置楼层审查参数 ──────────────────────────────────
story_payload = {"Argument": {"COUNTRY_CODE": "KBC2009"}}
r4 = requests.post(f"{BASE_URL}/ope/STORY_PARAM", json=story_payload, headers=HEADERS)
print(f"STEP4 STORY_PARAM: {r4.status_code}")

# ── STEP 5: 钢结构设计荷载组合自动生成 ───────────────────────────
lcom_steel_payload = {
    "Argument": {
        "OPTION": "ADD",
        "DGNCODE": "KDS(41-30:2022)",
        "STATIC_LOADS": [
            {"LOAD_CASE": "DeadLoad(ST)", "TYPE": "DEAD"},
            {"LOAD_CASE": "LiveLoad(ST)", "TYPE": "LIVE"}
        ]
    }
}
r5 = requests.post(f"{BASE_URL}/ope/LCOM-STEEL", json=lcom_steel_payload, headers=HEADERS)
print(f"STEP5 LCOM-STEEL: {r5.status_code}")

# ── STEP 6: 将生成的荷载组合指定用于钢结构设计审查 ────────────
uslc_payload = {
    "Argument": {
        "LCOM_LIST": [{"TYPE": "STEEL", "NAME": "sLCB1"}],
        "PREFIX": "N",
        "POSITION": "STEEL",
        "LOADS": {"SELF_WEIGHT": True, "NODAL_LOAD": True, "BEAM_LOAD": True}
    }
}
r6 = requests.post(f"{BASE_URL}/ope/USLC", json=uslc_payload, headers=HEADERS)
print(f"STEP6 USLC: {r6.status_code}")
```
