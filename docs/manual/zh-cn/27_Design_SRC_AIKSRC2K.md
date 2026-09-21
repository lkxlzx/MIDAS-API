# 27. Design Code – SRC AIK-SRC2K (SRC 型钢混凝土组合构件设计)

> **适用产品：** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **认证头：** `MAPI-Key: <已签发的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../27_Design_SRC_AIKSRC2K.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分涵盖 **SRC（型钢混凝土组合构件）设计代码 AIK-SRC2K** 的 **27 个端点**。所有端点均使用公共 URI 前缀 **`{base url}/DESIGN/SRC/AIK-SRC2K/<CODE>`**。

- **`"Assign"` 方式：** 设计代码、构件参数、材料、截面设置端点在请求体中使用 `"Assign"` 对象（键为 ID 字符串或构件编号）。
- **`"Argument"` 方式：** 验算执行（`*-ANAL`）、结果表格（`*-TABLE`、`TABLE`）、报告（`*-REPORT`）、优化设计（`OCHECK`）端点仅支持 `POST`，通过 `"Argument"` 对象指定对象与选项。
- **方法模式：** 各端点不同（例：`DSRC`=PUT·DELETE、`DCO`=PUT·GET·DELETE、设置单例=GET·PUT·DELETE、构件参数=POST·GET·PUT·DELETE、动作=仅 POST）。请确认各节的 Active Methods。
- **`TABLE` 公共 URI：** SRC 梁/柱设计内力使用相同的 URI `DESIGN/SRC/AIK-SRC2K/TABLE`，以 `TABLE_TYPE`（`SRCBEAMDESIGNFORCES`/`SRCCOLUMNDESIGNFORCES`）区分。

> **参考：** 钢结构设计见 **[25_Design_Steel_KDS41302022.md](./25_Design_Steel_KDS41302022.md)**，RC 设计见 **[26_Design_RC_KDS41202022.md](./26_Design_RC_KDS41202022.md)**。SRC 设计荷载组合在第 13 章（Load Combinations）中说明。

---

## 端点列表（27 个）

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`DSRC`](#1-designsrcaik-src2kdsrc--src-design-code-src-设计代码) | SRC 设计代码 | `PUT` · `DELETE` |
| 2 | [`DCO`](#2-designsrcaik-src2kdco--design-code-option-设计代码选项) | 设计代码选项 | `PUT` · `GET` · `DELETE` |
| 3 | [`DCTL`](#3-designsrcaik-src2kdctl--definition-of-frame-框架定义) | 框架定义 | `GET` · `PUT` · `DELETE` |
| 4 | [`LLRF`](#4-designsrcaik-src2kllrf--live-load-reduction-factor-活荷载折减系数) | 活荷载折减系数 | `GET` · `PUT` · `DELETE` |
| 5 | [`LCTB`](#5-designsrcaik-src2klctb--load-contribution-for-nonlinear-load-case-非线性荷载工况荷载贡献) | 非线性荷载工况荷载贡献 | `GET` · `DELETE` |
| 6 | [`LENG`](#6-designsrcaik-src2kleng--unbraced-length-l-lb-未支撑长度) | 未支撑长度(L, Lb) | `POST` · `GET` · `PUT` · `DELETE` |
| 7 | [`KFAC`](#7-designsrcaik-src2kkfac--effective-length-factor-k-有效屈曲长度系数) | 有效屈曲长度系数(K) | `POST` · `GET` · `PUT` · `DELETE` |
| 8 | [`LTSR`](#8-designsrcaik-src2kltsr--limiting-slenderness-ratio-长细比限制) | 长细比限制 | `POST` · `GET` · `PUT` · `DELETE` |
| 9 | [`CMFT`](#9-designsrcaik-src2kcmft--equivalent-moment-correction-factorcm-等效弯矩校正系数) | 等效弯矩校正系数(Cm) | `POST` · `GET` · `PUT` · `DELETE` |
| 10 | [`FMAG`](#10-designsrcaik-src2kfmag--moment-magnifierb1delta_b-b2delta_s-弯矩放大系数) | 弯矩放大系数(B1/δb, B2/δs) | `POST` · `GET` · `PUT` · `DELETE` |
| 11 | [`MLLR`](#11-designsrcaik-src2kmllr--modify-live-load-reduction-factor-活荷载折减系数修改) | 活荷载折减系数修改 | `POST` · `GET` · `PUT` · `DELETE` |
| 12 | [`SUEQ`](#12-designsrcaik-src2ksueq--scale-up-factor-for-earthquake-地震放大系数) | 地震放大系数 | `POST` · `GET` · `PUT` · `DELETE` |
| 13 | [`MBTP`](#13-designsrcaik-src2kmbtp--modify-member-type-构件类型修改) | 构件类型修改 | `POST` · `GET` · `PUT` · `DELETE` |
| 14 | [`EQCT`](#14-designsrcaik-src2keqct--seismic-load-combination-type-地震荷载组合类型) | 地震荷载组合类型 | `POST` · `GET` · `PUT` · `DELETE` |
| 15 | [`BC-ANAL`](#15-designsrcaik-src2kbc-anal--src-beam-checking-perform-src-梁验算执行) | SRC 梁验算执行 | `POST` |
| 16 | [`BC-TABLE`](#16-designsrcaik-src2kbc-table--src-beam-checking-table-src-梁验算表格) | SRC 梁验算表格 | `POST` |
| 17 | [`BC-REPORT`](#17-designsrcaik-src2kbc-report--src-beam-checking-report-src-梁验算报告) | SRC 梁验算报告 | `POST` |
| 18 | [`CC-ANAL`](#18-designsrcaik-src2kcc-anal--src-column-checking-perform-src-柱验算执行) | SRC 柱验算执行 | `POST` |
| 19 | [`CC-TABLE`](#19-designsrcaik-src2kcc-table--src-column-checking-table-src-柱验算表格) | SRC 柱验算表格 | `POST` |
| 20 | [`CC-REPORT`](#20-designsrcaik-src2kcc-report--src-column-checking-report-src-柱验算报告) | SRC 柱验算报告 | `POST` |
| 21 | [`OCHECK`](#21-designsrcaik-src2kocheck--src-optimal-design-src-优化设计) | SRC 优化设计 | `POST` |
| 22 | [`TABLE`（梁）](#22-designsrcaik-src2ktable--src-beam-design-forces-src-梁设计内力) | SRC 梁设计内力 | `POST` |
| 23 | [`TABLE`（柱）](#23-designsrcaik-src2ktable--src-column-design-forces-src-柱设计内力) | SRC 柱设计内力 | `POST` |
| 24 | [`MATD`](#24-designsrcaik-src2kmatd--modify-src-material-src-材料修改) | SRC 材料修改 | `GET` · `PUT` · `DELETE` |
| 25 | [`MCRD`](#25-designsrcaik-src2kmcrd--modify-src-column-section-data-src-柱截面数据修改) | SRC 柱截面数据修改 | `POST` · `GET` · `PUT` · `DELETE` |
| 26 | [`MEMB`](#26-designsrcaik-src2kmemb--member-assignment-构件指定) | 构件指定 | `GET` · `PUT` · `DELETE` |
| 27 | [`MRBD`](#27-designsrcaik-src2kmrbd--modify-src-beam-section-data-src-梁截面数据修改) | SRC 梁截面数据修改 | `POST` · `GET` · `PUT` · `DELETE` |

---

## 1. `DESIGN/SRC/AIK-SRC2K/DSRC` — SRC Design Code (SRC 设计代码)

> **功能：** 设置 SRC 设计代码（AIK-SRC2K）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/DSRC
```

### Active Methods

`PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "DGNCODE"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "Design Code",
              "enum": [
                "AIK-SRC2K"
              ]
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `DGNCODE` | string | 设计代码 — 可能取值：`AIK-SRC2K` |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AIK-SRC2K"
    }
  }
}
```

**Response Body**

```json
{
  "DSRC": {
    "1": {
      "DGNCODE": "AIK-SRC2K"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "1": {
            "DGNCODE": "AIK-SRC2K"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DSRC", json=payload, headers=HEADERS)
res.raise_for_status()

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DSRC", headers=HEADERS)
```

---

## 2. `DESIGN/SRC/AIK-SRC2K/DCO` — Design Code Option (设计代码选项)

> **功能：** 设置 SRC 设计代码选项（是否应用抗震等全局设计选项）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/DCO
```

### Active Methods

`PUT` · `GET` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "minProperties": 1,
      "maxProeprties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "DGNCODE",
            "SEISMIC"
          ],
          "additionalProperties": false,
          "properties": {
            "DGNCODE": {
              "type": "string",
              "description": "Design code.",
              "default": "AIK-SRC2K",
              "oneOf": [
                {
                  "const": "AIK-SRC2K",
                  "title": "AIK-SRC2K"
                }
              ]
            },
            "SEISMIC": {
              "type": "boolean",
              "description": "Whether seismic design is applied.",
              "default": true
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `DGNCODE` | string | 设计代码。— `AIK-SRC2K`=AIK-SRC2K | AIK-SRC2K | O |
| `SEISMIC` | boolean | 是否应用抗震设计。 | true | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "AIK-SRC2K",
      "SEISMIC": true
    }
  }
}
```

**Response Body**

```json
{
  "SRCDCO": {
    "1": {
      "DGNCODE": "AIK-SRC2K",
      "SEISMIC": true
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "1": {
            "DGNCODE": "AIK-SRC2K",
            "SEISMIC": true
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCO", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCO", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCO", headers=HEADERS)
```

---

## 3. `DESIGN/SRC/AIK-SRC2K/DCTL` — Definition of Frame (框架定义)

> **功能：** 定义设计用框架（无侧移/有侧移、自动计算 K 等）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/DCTL
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "description": "Definition of Frame (shared structure: T_DCTL_D). Supported methods: GET, PUT.",
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FRAMEX": {
              "type": "string",
              "description": "X-Direction of Frame",
              "default": "Braced Non-sway",
              "oneOf": [
                {
                  "title": "Unbraced | Sway",
                  "const": "Unbraced Sway"
                },
                {
                  "title": "Braced | Non-sway",
                  "const": "Braced Non-sway"
                }
              ]
            },
            "FRAMEY": {
              "type": "string",
              "description": "Y-Direction of Frame",
              "default": "Braced Non-sway",
              "oneOf": [
                {
                  "title": "Unbraced | Sway",
                  "const": "Unbraced Sway"
                },
                {
                  "title": "Braced | Non-sway",
                  "const": "Braced Non-sway"
                }
              ]
            },
            "bAUTOKF": {
              "type": "boolean",
              "description": "Auto Calculate Effective Length Factor",
              "default": false
            },
            "DT": {
              "type": "string",
              "description": "Design Type",
              "default": "3D",
              "oneOf": [
                {
                  "title": "3-D",
                  "const": "3D"
                },
                {
                  "title": "X-Z Plane",
                  "const": "XZ"
                },
                {
                  "title": "Y-Z Plane",
                  "const": "YZ"
                },
                {
                  "title": "X-Y Plane",
                  "const": "XY"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `FRAMEX` | string | X 方向框架 — `Unbraced Sway`=无支撑 \| 有侧移; `Braced Non-sway`=支撑 \| 无侧移 | Braced Non-sway |  |
| `FRAMEY` | string | Y 方向框架 — `Unbraced Sway`=无支撑 \| 有侧移; `Braced Non-sway`=支撑 \| 无侧移 | Braced Non-sway |  |
| `bAUTOKF` | boolean | 有效屈曲长度系数自动计算 | false |  |
| `DT` | string | 设计类型 — `3D`=3-D; `XZ`=X-Z 平面; `YZ`=Y-Z 平面; `XY`=X-Y 平面 | 3D |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "XZ"
    }
  }
}
```

**Response Body**

```json
{
  "DCTL": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": true,
      "DT": "XZ"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "1": {
            "FRAMEX": "Braced Non-sway",
            "FRAMEY": "Braced Non-sway",
            "bAUTOKF": true,
            "DT": "XZ"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCTL", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCTL", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/DCTL", headers=HEADERS)
```

---

## 4. `DESIGN/SRC/AIK-SRC2K/LLRF` — Live Load Reduction Factor (活荷载折减系数)

> **功能：** 设置活荷载折减系数（基于构件支撑层数/影响面积）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LLRF
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "REDUCTION_DATA"
          ],
          "additionalProperties": false,
          "properties": {
            "CALC_RULE": {
              "type": "integer",
              "default": 0,
              "oneOf": [
                {
                  "title": "by General Design Code",
                  "const": 0
                },
                {
                  "title": "by Chinese Standard",
                  "const": 1
                }
              ]
            },
            "APPLIED_COMP": {
              "type": "array",
              "description": "Applied Components Selection",
              "items": {
                "type": "string",
                "enum": [
                  "ALL",
                  "AXIAL",
                  "MOMENTS",
                  "SHEAR"
                ]
              },
              "default": [
                "AXIAL"
              ]
            },
            "LIVE_LOAD_CASES": {
              "type": "array",
              "description": "Live Load Case Names (user defined list)",
              "items": {
                "type": "string"
              }
            },
            "REDUCTION_DATA": {
              "type": "array",
              "description": "Live Load Reduction Factor Table Data",
              "items": {
                "type": "object",
                "required": [
                  "STORY"
                ],
                "properties": {
                  "STORY": {
                    "type": "string",
                    "description": "Story Name"
                  },
                  "XMIN": {
                    "type": "number",
                    "default": 0,
                    "description": "X Min coordinate"
                  },
                  "XMAX": {
                    "type": "number",
                    "default": 0,
                    "description": "X Max coordinate"
                  },
                  "YMIN": {
                    "type": "number",
                    "default": 0,
                    "description": "Y Min coordinate"
                  },
                  "YMAX": {
                    "type": "number",
                    "default": 0,
                    "description": "Y Max coordinate"
                  },
                  "RANGE_MAX": {
                    "type": "number",
                    "description": "Range Max value (only for General Design Code)",
                    "enum": [
                      1,
                      0.95,
                      0.9,
                      0.85,
                      0.8,
                      "...(전체 11개)"
                    ],
                    "default": 1
                  },
                  "RANGE_MIN": {
                    "type": "number",
                    "description": "Range Min value (only for General Design Code)",
                    "enum": [
                      1,
                      0.95,
                      0.9,
                      0.85,
                      0.8,
                      "...(전체 11개)"
                    ],
                    "default": 0.5
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

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `CALC_RULE` | integer | — `0`=一般设计标准; `1`=中国标准规范 | 0 |  |
| `APPLIED_COMP` | array | 选择应用分量 | ["AXIAL"] |  |
| `LIVE_LOAD_CASES` | array | 活荷载工况名称（用户自定义列表） |  |  |
| `REDUCTION_DATA` | array | 活荷载折减系数表格数据 |  | O |
| └ `STORY` | string | 楼层名称 |  | O |
| └ `XMIN` | number | X 最小坐标 | 0 |  |
| └ `XMAX` | number | X 最大坐标 | 0 |  |
| └ `YMIN` | number | Y 最小坐标 | 0 |  |
| └ `YMAX` | number | Y 最大坐标 | 0 |  |
| └ `RANGE_MAX` | number | 区间最大值（仅 General Design Code）— 可能取值 11 个：`1` ~ `0.5` | 1 |  |
| └ `RANGE_MIN` | number | 区间最小值（仅 General Design Code）— 可能取值 11 个：`1` ~ `0.5` | 0.5 |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL",
        "SHEAR",
        "MOMENTS",
        "ALL"
      ],
      "LIVE_LOAD_CASES": [
        "LL2"
      ],
      "REDUCTION_DATA": [
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45,
          "RANGE_MAX": 0.9,
          "RANGE_MIN": 0.6
        },
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45
        }
      ]
    }
  }
}
```

**Response Body**

```json
{
  "LLRF": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL",
        "SHEAR",
        "MOMENTS",
        "ALL"
      ],
      "LIVE_LOAD_CASES": [
        "LL2"
      ],
      "REDUCTION_DATA": [
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45,
          "RANGE_MAX": 0.9,
          "RANGE_MIN": 0.6
        },
        {
          "STORY": "B2",
          "XMIN": -7.5,
          "XMAX": 1.15,
          "YMIN": -7.45,
          "YMAX": -7.45
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
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "1": {
            "CALC_RULE": 0,
            "APPLIED_COMP": [
                "AXIAL",
                "SHEAR",
                "MOMENTS",
                "ALL"
            ],
            "LIVE_LOAD_CASES": [
                "LL2"
            ],
            "REDUCTION_DATA": [
                {
                    "STORY": "B2",
                    "XMIN": -7.5,
                    "XMAX": 1.15,
                    "YMIN": -7.45,
                    "YMAX": -7.45,
                    "RANGE_MAX": 0.9,
                    "RANGE_MIN": 0.6
                },
                {
                    "STORY": "B2",
                    "XMIN": -7.5,
                    "XMAX": 1.15,
                    "YMIN": -7.45,
                    "YMAX": -7.45
                }
            ]
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LLRF", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LLRF", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LLRF", headers=HEADERS)
```

---

## 5. `DESIGN/SRC/AIK-SRC2K/LCTB` — Load Contribution for Nonlinear Load Case (非线性荷载工况荷载贡献)

> **功能：** 设置针对非线性荷载工况的荷载贡献（Load Contribution）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LCTB
```

### Active Methods

`GET` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "NAME",
            "BASE_ITEM"
          ],
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "description": "Load Contribution Name"
            },
            "DESC": {
              "type": "string",
              "description": "Description",
              "default": ""
            },
            "BASE_ITEM": {
              "type": "array",
              "description": "Load Contribution Items",
              "items": {
                "type": "object",
                "required": [
                  "FACTOR",
                  "LOAD_CASE_NAME"
                ],
                "additionalProperties": false,
                "properties": {
                  "FACTOR": {
                    "type": "number",
                    "description": "Factor"
                  },
                  "LOAD_CASE_NAME": {
                    "type": "string",
                    "description": "Load Case Name"
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

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `NAME` | string | 荷载贡献名称 |  | O |
| `DESC` | string | 说明 |  |  |
| `BASE_ITEM` | array | 荷载贡献项 |  | O |
| └ `FACTOR` | number | 系数 |  | O |
| └ `LOAD_CASE_NAME` | string | 荷载工况名称 |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Response Body**

```json
{
  "LCTB": {
    "1": {
      "NAME": "NgLCB6",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "LL"
        },
        {
          "FACTOR": 0.5,
          "LOAD_CASE_NAME": "SL"
        }
      ]
    },
    "2": {
      "NAME": "NgLCB7",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "SL"
        },
        {
          "FACTOR": 1,
          "LOAD_CASE_NAME": "LL"
        }
      ]
    },
    "3": {
      "NAME": "NgLCB8",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "SL"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WX"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WX(A)"
        }
      ]
    },
    "4": {
      "NAME": "NgLCB9",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "SL"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WX"
        },
        {
          "FACTOR": -0.65,
          "LOAD_CASE_NAME": "WX(A)"
        }
      ]
    },
    "5": {
      "NAME": "NgLCB10",
      "DESC": "",
      "BASE_ITEM": [
        {
          "FACTOR": 1.2,
          "LOAD_CASE_NAME": "DL"
        },
        {
          "FACTOR": 1.6,
          "LOAD_CASE_NAME": "SL"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WY"
        },
        {
          "FACTOR": 0.65,
          "LOAD_CASE_NAME": "WY(A)"
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
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（GET）
payload = {}
res = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LCTB", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LCTB", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LCTB", headers=HEADERS)
```

---

## 6. `DESIGN/SRC/AIK-SRC2K/LENG` — Unbraced Length (L, Lb) (未支撑长度)

> **功能：** 设置各构件的未支撑长度（Ly, Lz, Lb）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LENG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "LY": {
              "type": "number",
              "description": "Unbraced Length Ly",
              "default": 0
            },
            "LZ": {
              "type": "number",
              "description": "Unbraced Length Lz",
              "default": 0
            },
            "LB": {
              "type": "number",
              "description": "Laterally Unbraced Length",
              "default": 0
            },
            "bNOTUSE": {
              "type": "boolean",
              "description": "Do not consider of laterally unbraced length",
              "default": false
            },
            "LT": {
              "type": "number",
              "description": "Torsional Unbraced Length",
              "default": 0
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `LY` | number | 未支撑长度 Ly | 0 |  |
| `LZ` | number | 未支撑长度 Lz | 0 |  |
| `LB` | number | 横向未支撑长度 | 0 |  |
| `bNOTUSE` | boolean | 不考虑横向未支撑长度 | false |  |
| `LT` | number | 扭转未支撑长度 | 0 |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "LZ": 2,
      "LY": 1
    },
    "874": {
      "LY": 1,
      "LZ": 1
    }
  }
}
```

**Response Body**

```json
{
  "LENG": {
    "868": {
      "LY": 1,
      "LZ": 2
    },
    "874": {
      "LY": 1,
      "LZ": 1
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "LZ": 2,
            "LY": 1
        },
        "874": {
            "LY": 1,
            "LZ": 1
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LENG", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LENG", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LENG", headers=HEADERS)
```

---

## 7. `DESIGN/SRC/AIK-SRC2K/KFAC` — Effective Length Factor (K) (有效屈曲长度系数)

> **功能：** 设置各构件的有效屈曲长度系数（Ky, Kz）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/KFAC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "Ky": {
              "type": "number",
              "description": "Ky",
              "default": 1
            },
            "Kz": {
              "type": "number",
              "description": "Kz",
              "default": 1
            },
            "Kt": {
              "type": "number",
              "description": "Kt",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `Ky` | number | Ky | 1 |  |
| `Kz` | number | Kz | 1 |  |
| `Kt` | number | Kt | 1 |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "Ky": 1
    },
    "874": {
      "Ky": 2,
      "Kz": 2
    },
    "885": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

**Response Body**

```json
{
  "KFAC": {
    "868": {
      "Ky": 1
    },
    "874": {
      "Ky": 2,
      "Kz": 2
    },
    "885": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "Ky": 1
        },
        "874": {
            "Ky": 2,
            "Kz": 2
        },
        "885": {
            "Kz": 3,
            "Kt": 3
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/KFAC", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/KFAC", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/KFAC", headers=HEADERS)
```

---

## 8. `DESIGN/SRC/AIK-SRC2K/LTSR` — Limiting Slenderness Ratio (长细比限制)

> **功能：** 设置各构件的受压/受拉长细比限值。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/LTSR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "COMP",
            "TENS"
          ],
          "additionalProperties": false,
          "properties": {
            "bNOTCHECK": {
              "type": "boolean",
              "description": "Do not check for Slenderness Ratio",
              "default": false
            },
            "COMP": {
              "type": "number",
              "description": "Limiting Slenderness Ratio for Compression"
            },
            "TENS": {
              "type": "number",
              "description": "Limiting Slenderness Ratio for Tension"
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `bNOTCHECK` | boolean | 不进行长细比验算 | false |  |
| `COMP` | number | 受压构件长细比限值 |  | O |
| `TENS` | number | 受拉构件长细比限值 |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "COMP": 300,
      "TENS": 200
    },
    "874": {
      "COMP": 300,
      "TENS": 200
    },
    "885": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

**Response Body**

```json
{
  "LTSR": {
    "868": {
      "COMP": 300,
      "TENS": 200
    },
    "874": {
      "COMP": 300,
      "TENS": 200
    },
    "885": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "COMP": 300,
            "TENS": 200
        },
        "874": {
            "COMP": 300,
            "TENS": 200
        },
        "885": {
            "COMP": 300,
            "TENS": 200
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LTSR", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LTSR", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/LTSR", headers=HEADERS)
```

---

## 9. `DESIGN/SRC/AIK-SRC2K/CMFT` — Equivalent Moment Correction Factor(Cm) (等效弯矩校正系数)

> **功能：** 设置各构件的等效弯矩校正系数（Cm）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CMFT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "OPT_AUTO": {
              "type": "boolean",
              "description": "Auto Calculate",
              "default": false
            },
            "CMY": {
              "type": "number",
              "description": "CMy",
              "default": 0
            },
            "CMZ": {
              "type": "number",
              "description": "CMz",
              "default": 0
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `OPT_AUTO` | boolean | 自动计算 | false |  |
| `CMY` | number | CMy | 0 |  |
| `CMZ` | number | CMz | 0 |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "OPT_AUTO": true
    },
    "874": {
      "OPT_AUTO": true
    },
    "885": {
      "CMY": 0.7,
      "CMZ": 0.6
    }
  }
}
```

**Response Body**

```json
{
  "CMFT": {
    "868": {
      "OPT_AUTO": true
    },
    "874": {
      "OPT_AUTO": true
    },
    "885": {
      "CMY": 0.7,
      "CMZ": 0.6
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "OPT_AUTO": true
        },
        "874": {
            "OPT_AUTO": true
        },
        "885": {
            "CMY": 0.7,
            "CMZ": 0.6
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CMFT", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CMFT", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CMFT", headers=HEADERS)
```

---

## 10. `DESIGN/SRC/AIK-SRC2K/FMAG` — Moment Magnifier(B1/Delta_b, B2/Delta_s) (弯矩放大系数)

> **功能：** 设置各构件的弯矩放大系数（B1/δb, B2/δs）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/FMAG
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "B1Y_DELTA_BY": {
              "type": "number",
              "description": "B1y - Delta by (First Order Moment Y)",
              "default": 1
            },
            "B1Z_DELTA_BZ": {
              "type": "number",
              "description": "B1z - Delta bz (First Order Moment Z)",
              "default": 1
            },
            "B2Y_DELTA_SY": {
              "type": "number",
              "description": "B2y - Delta sy (Second Order Moment Y)",
              "default": 1
            },
            "B2Z_DELTA_SZ": {
              "type": "number",
              "description": "B2z - Delta sz (Second Order Moment Z)",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `B1Y_DELTA_BY` | number | B1y - Δby（一次弯矩 Y） | 1 |  |
| `B1Z_DELTA_BZ` | number | B1z - Δbz（一次弯矩 Z） | 1 |  |
| `B2Y_DELTA_SY` | number | B2y - Δsy（二次弯矩 Y） | 1 |  |
| `B2Z_DELTA_SZ` | number | B2z - Δsz（二次弯矩 Z） | 1 |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "874": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    },
    "885": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
    }
  }
}
```

**Response Body**

```json
{
  "FMAG": {
    "868": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "874": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    },
    "885": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "B1Y_DELTA_BY": 1.1,
            "B1Z_DELTA_BZ": 1.2
        },
        "874": {
            "B2Y_DELTA_SY": 1.3,
            "B2Z_DELTA_SZ": 1.4
        },
        "885": {
            "B1Z_DELTA_BZ": 1.2,
            "B2Y_DELTA_SY": 1.3
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/FMAG", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/FMAG", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/FMAG", headers=HEADERS)
```

---

## 11. `DESIGN/SRC/AIK-SRC2K/MLLR` — Modify Live Load Reduction Factor (活荷载折减系数修改)

> **功能：** 修改各构件的活荷载折减系数。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MLLR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "FACTOR": {
              "type": "number",
              "description": "Reduction Factor",
              "default": 1,
              "minimum": 0.3,
              "maximum": 1
            },
            "COMPONENTS": {
              "type": "object",
              "description": "Applied Components",
              "additionalProperties": false,
              "properties": {
                "AXIAL": {
                  "type": "boolean",
                  "description": "Axial Force",
                  "default": false
                },
                "MOMENT": {
                  "type": "boolean",
                  "description": "Moments",
                  "default": false
                },
                "SHEAR": {
                  "type": "boolean",
                  "description": "Shear Forces",
                  "default": false
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

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `FACTOR` | number | 折减系数 | 1 |  |
| `COMPONENTS` | object | 应用分量 |  |  |
| └ `AXIAL` | boolean | 轴力 | false |  |
| └ `MOMENT` | boolean | 弯矩 | false |  |
| └ `SHEAR` | boolean | 剪力 | false |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "874": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
```

**Response Body**

```json
{
  "MLLR": {
    "868": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "874": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "COMPONENTS": {
                "AXIAL": false,
                "MOMENT": true,
                "SHEAR": false
            }
        },
        "874": {
            "FACTOR": 0.9,
            "COMPONENTS": {
                "AXIAL": true,
                "SHEAR": false
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MLLR", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MLLR", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MLLR", headers=HEADERS)
```

---

## 12. `DESIGN/SRC/AIK-SRC2K/SUEQ` — Scale up Factor for Earthquake (地震放大系数)

> **功能：** 设置地震作用的放大（Scale-up）系数。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/SUEQ
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "LC_AXIAL": {
              "type": "number",
              "description": "Load Case - Axial Scale Factor",
              "default": 1
            },
            "LC_MOMENT": {
              "type": "number",
              "description": "Load Case - Moment Scale Factor",
              "default": 1
            },
            "LC_SHEAR": {
              "type": "number",
              "description": "Load Case - Shear Scale Factor",
              "default": 1
            },
            "LCOM_AXIAL": {
              "type": "number",
              "description": "Load Combination - Axial Scale Factor",
              "default": 1
            },
            "LCOM_MOMENT": {
              "type": "number",
              "description": "Load Combination - Moment Scale Factor",
              "default": 1
            },
            "LCOM_SHEAR": {
              "type": "number",
              "description": "Load Combination - Shear Scale Factor",
              "default": 1
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `LC_AXIAL` | number | 荷载工况 - 轴力放大系数 | 1 |  |
| `LC_MOMENT` | number | 荷载工况 - 弯矩放大系数 | 1 |  |
| `LC_SHEAR` | number | 荷载工况 - 剪力放大系数 | 1 |  |
| `LCOM_AXIAL` | number | 荷载组合 - 轴力放大系数 | 1 |  |
| `LCOM_MOMENT` | number | 荷载组合 - 弯矩放大系数 | 1 |  |
| `LCOM_SHEAR` | number | 荷载组合 - 剪力放大系数 | 1 |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "874": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
```

**Response Body**

```json
{
  "SUEQ": {
    "868": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "874": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "LC_AXIAL": 1.2,
            "LC_MOMENT": 1.2,
            "LC_SHEAR": 1.2,
            "LCOM_AXIAL": 1.2,
            "LCOM_MOMENT": 1.2,
            "LCOM_SHEAR": 1.2
        },
        "874": {
            "LC_SHEAR": 1.2,
            "LCOM_AXIAL": 1.2,
            "LCOM_MOMENT": 1.2,
            "LCOM_SHEAR": 1.2
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/SUEQ", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/SUEQ", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/SUEQ", headers=HEADERS)
```

---

## 13. `DESIGN/SRC/AIK-SRC2K/MBTP` — Modify Member Type (构件类型修改)

> **功能：** 修改构件的设计类型（梁/柱等）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MBTP
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Member Type",
              "oneOf": [
                {
                  "title": "Column",
                  "const": "COLUMN"
                },
                {
                  "title": "Beam",
                  "const": "BEAM"
                },
                {
                  "title": "Brace",
                  "const": "BRACE"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `TYPE` | string | 构件类型 — `COLUMN`=柱; `BEAM`=梁; `BRACE`=支撑 |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "TYPE": "BRACE"
    },
    "874": {
      "TYPE": "COLUMN"
    }
  }
}
```

**Response Body**

```json
{
  "MBTP": {
    "868": {
      "TYPE": "BRACE"
    },
    "874": {
      "TYPE": "COLUMN"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "TYPE": "BRACE"
        },
        "874": {
            "TYPE": "COLUMN"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MBTP", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MBTP", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MBTP", headers=HEADERS)
```

---

## 14. `DESIGN/SRC/AIK-SRC2K/EQCT` — Seismic Load Combination Type (地震荷载组合类型)

> **功能：** 设置地震荷载组合类型。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/EQCT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Assign Member Type",
              "oneOf": [
                {
                  "title": "Special Seismic Loads",
                  "const": "Special Seismic Loads"
                },
                {
                  "title": "Vertical Seismic Forces",
                  "const": "Vertical Seismic Forces"
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `TYPE` | string | 构件类型指定 — `Special Seismic Loads`=特殊地震荷载; `Vertical Seismic Forces`=竖向地震力 |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "868": {
      "TYPE": "Special Seismic Loads"
    },
    "874": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

**Response Body**

```json
{
  "EQCT": {
    "868": {
      "TYPE": "Special Seismic Loads"
    },
    "874": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "868": {
            "TYPE": "Special Seismic Loads"
        },
        "874": {
            "TYPE": "Vertical Seismic Forces"
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/EQCT", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/EQCT", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/EQCT", headers=HEADERS)
```

---

## 15. `DESIGN/SRC/AIK-SRC2K/BC-ANAL` — SRC Beam Checking Perform (SRC 梁验算执行)

> **功能：** 执行 SRC 梁验算（设计计算）。为 POST 专用动作。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/BC-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
          "oneOf": [
            {
              "title": "All Elements",
              "const": "ALL"
            },
            {
              "title": "By Element No.",
              "const": "ELEMS"
            },
            {
              "title": "By Section No.",
              "const": "SECTIONS"
            }
          ],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "description": "Section No. Input.",
          "items": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `PERFORM_TYPE` | string | 选择设计计算对象类型。ELEMS：按单元编号，SECTIONS：按截面编号，ALL：全部单元。— `ALL`=全部单元; `ELEMS`=按单元编号; `SECTIONS`=按截面编号 | ALL |  |
| `ELEMS` | object | 输入单元编号。 |  |  |
| └ `KEYS` | array | 指定单个 ID |  |  |
| └ `TO` | string | 指定 ID 范围（例：'1to160'） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `SECTIONS` | array | 输入截面编号。 |  |  |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        922
      ]
    }
  }
}
```

**Response Body**

```json
{
  "message": "success"
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "PERFORM_TYPE": "ALL",
        "ELEMS": {
            "KEYS": [
                922
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/BC-ANAL", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 16. `DESIGN/SRC/AIK-SRC2K/BC-TABLE` — SRC Beam Checking Table (SRC 梁验算表格)

> **功能：** 查询 SRC 梁验算结果表格（HEAD/DATA）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/BC-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "TABLE_TYPE"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Result Table Type",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element number input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify each element ID",
              "items": {
                "type": "integer"
              },
              "minItems": 1
            },
            "TO": {
              "type": "string",
              "description": "Specify element ID range (e.g., \"1to160\")"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify structure group name"
            }
          },
          "oneOf": [
            {
              "required": [
                "KEYS"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "TO"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "TO"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "STRUCTURE_GROUP_NAME"
                    ]
                  }
                ]
              }
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ],
              "not": {
                "anyOf": [
                  {
                    "required": [
                      "KEYS"
                    ]
                  },
                  {
                    "required": [
                      "TO"
                    ]
                  }
                ]
              }
            }
          ]
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the table.",
          "items": {
            "type": "integer"
          }
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Sorting criteria for member-based output (by Section No. or Member No.)",
          "default": 1,
          "oneOf": [
            {
              "title": "SECT",
              "const": 0
            },
            {
              "title": "MEMB",
              "const": 1
            }
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Filter results by checking status",
          "default": 0,
          "oneOf": [
            {
              "title": "All",
              "const": 0
            },
            {
              "title": "OK",
              "const": 1
            },
            {
              "title": "NG",
              "const": 2
            }
          ]
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": "SRC Checking Result"
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "additionalProperties": false,
          "properties": {
            "FORCE": {
              "type": "string",
              "description": "Force unit"
            },
            "DIST": {
              "type": "string",
              "description": "Length/Distance unit"
            },
            "HEAT": {
              "type": "string",
              "description": "Heat unit"
            },
            "TEMP": {
              "type": "string",
              "description": "Temperature unit"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "description": "Response Number Format",
          "additionalProperties": false,
          "properties": {
            "FORMAT": {
              "type": "string",
              "description": "Number format",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "description": "Digit place",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of SRC Checking Result Table",
          "items": {
            "type": "string",
            "enum": [
              "MEMB",
              "SECT",
              "Span",
              "Section",
              "Bc",
              "...(전체 27개)"
            ]
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `TABLE_TYPE` | string | 结果表类型 — 可能取值：`MEMB`, `PROP` |  | O |
| `ELEMS` | object | 输入单元编号。 |  |  |
| └ `KEYS` | array | 指定单个单元 ID |  |  |
| └ `TO` | string | 指定单元 ID 范围（例："1to160"） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `SECTIONS` | array | 表格中包含的截面编号列表。 |  |  |
| `PRI_SORT` | integer | 按构件输出的排序基准（截面编号或构件编号）— `0`=SECT; `1`=MEMB | 1 |  |
| `RESULT` | integer | 按验算状态过滤结果 — `0`=全部; `1`=OK; `2`=NG | 0 |  |
| `TABLE_NAME` | string | 结果表标题 | SRC Checking Result |  |
| `EXPORT_PATH` | string | 结果表保存路径 |  |  |
| `UNIT` | object | 结果单位设置 |  |  |
| └ `FORCE` | string | 力单位 |  |  |
| └ `DIST` | string | 长度/距离单位 |  |  |
| └ `HEAT` | string | 热量单位 |  |  |
| └ `TEMP` | string | 温度单位 |  |  |
| `STYLES` | object | 结果数字格式 |  |  |
| └ `FORMAT` | string | 数字格式 — 可能取值：`Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 小数位数 |  |  |
| `COMPONENTS` | array | SRC 验算结果表组成项 |  |  |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "Material",
      "Fy",
      "fc",
      "Fyr",
      "Fys",
      "POS",
      "CHK",
      "AsTop",
      "AsBot",
      "N_M",
      "LCB_N",
      "N_Mrs",
      "Rat_N",
      "P_M",
      "LCB_P",
      "P_Mrs",
      "Rat_P",
      "V",
      "LCB_V",
      "Vrs",
      "Rat_V"
    ],
    "ELEMS": {
      "KEYS": [
        922
      ]
    }
  }
}
```

**Response Body**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "MM",
    "HEAD": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "Material",
      "Fy",
      "fc",
      "Fyr",
      "Fys",
      "POS",
      "CHK",
      "AsTop",
      "AsBot",
      "N_M",
      "LCB_N",
      "N_Mrs",
      "Rat_N",
      "P_M",
      "LCB_P",
      "P_Mrs",
      "Rat_P",
      "V",
      "LCB_V",
      "Vrs",
      "Rat_V"
    ],
    "DATA": [
      [
        "922",
        "3",
        "4460.0",
        "H src200x100x5.5/8, H 200x100x5.5/8",
        "400.00",
        "400.00",
        "SS410",
        "0.4100",
        "0.03000",
        "0.40000",
        "0.40000",
        "I",
        "OK",
        "253.40",
        "774.20",
        "62068.5",
        "7",
        "68471.1",
        "0.91",
        "7082.47",
        "7",
        "105831",
        "0.07",
        "68.6914",
        "7",
        "251.879",
        "0.27"
      ],
      [
        "922",
        "3",
        "4460.0",
        "H src200x100x5.5/8, H 200x100x5.5/8",
        "400.00",
        "400.00",
        "SS410",
        "0.4100",
        "0.03000",
        "0.40000",
        "0.40000",
        "M",
        "OK",
        "397.20",
        "28.100",
        "0.00000",
        "7",
        "78786.7",
        "0.00",
        "43273.9",
        "7",
        "52309.1",
        "0.83",
        "51.2916",
        "7",
        "251.879",
        "0.20"
      ],
      [
        "922",
        "3",
        "4460.0",
        "H src200x100x5.5/8, H 200x100x5.5/8",
        "400.00",
        "400.00",
        "SS410",
        "0.4100",
        "0.03000",
        "0.40000",
        "0.40000",
        "J",
        "OK",
        "573.00",
        "573.00",
        "35970.5",
        "7",
        "91397.9",
        "0.39",
        "25750.1",
        "7",
        "91397.9",
        "0.28",
        "67.3729",
        "7",
        "251.879",
        "0.27"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "TABLE_TYPE": "MEMB",
        "PRI_SORT": 1,
        "RESULT": 0,
        "COMPONENTS": [
            "MEMB",
            "SECT",
            "Span",
            "Section",
            "Bc",
            "Hc",
            "Material",
            "Fy",
            "fc",
            "Fyr",
            "Fys",
            "POS",
            "CHK",
            "AsTop",
            "AsBot",
            "N_M",
            "LCB_N",
            "N_Mrs",
            "Rat_N",
            "P_M",
            "LCB_P",
            "P_Mrs",
            "Rat_P",
            "V",
            "LCB_V",
            "Vrs",
            "Rat_V"
        ],
        "ELEMS": {
            "KEYS": [
                922
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/BC-TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 17. `DESIGN/SRC/AIK-SRC2K/BC-REPORT` — SRC Beam Checking Report (SRC 梁验算报告)

> **功能：** 生成/查询 SRC 梁验算报告。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/BC-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "REPORT_TYPE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Report Table Type",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Report output mode for element-based report",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Detail (DOC document)",
              "const": "Detail"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            }
          ]
        },
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Report output mode for property-based report",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            }
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the report.",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "description": "Print positions for Detail report",
          "properties": {
            "END_I": {
              "type": "boolean",
              "description": "Include End I position",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "description": "Include Mid position",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "description": "Include End J position",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "Output file base name. For multiple elements, files are prefixed with index and element number (e.g. 001_E859_filename.jpg, 002_E1_filename.jpg)"
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `REPORT_TYPE` | string | 报告表类型 — 可能取值：`MEMB`, `PROP` |  | O |
| `CURRENT_MODE_MEMB` | string | 以单元为基准的报告输出模式 — `Graphic`=图形（JPG 图像）; `Detail`=详细（DOC 文档）; `Summary`=摘要（TXT 文本） |  |  |
| `CURRENT_MODE_PROP` | string | 以特性为基准的报告输出模式 — `Graphic`=图形（JPG 图像）; `Summary`=摘要（TXT 文本） |  |  |
| `ELEMS` | object | 输入单元编号。 |  |  |
| └ `KEYS` | array | 指定单个 ID |  |  |
| └ `TO` | string | 指定 ID 范围（例：'1to160'） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `SECTIONS` | array | 报告中包含的截面编号列表。 |  |  |
| `DETAIL_POSITIONS` | object | 详细报告输出位置 |  |  |
| └ `END_I` | boolean | 包含 I 端位置 | true |  |
| └ `MID` | boolean | 包含跨中位置 | false |  |
| └ `END_J` | boolean | 包含 J 端位置 | false |  |
| `EXPORT_PATH` | string | 保存报告文件的目录路径 |  | O |
| `OUTPUT_NAME` | string | 输出文件基本名称。存在多个单元时，文件名前会附加序号与单元编号（例：001_E859_filename.jpg, 002_E1_filename.jpg）。 |  | O |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "GRAPHIC.jpg",
    "CURRENT_MODE_MEMB": "Graphic"
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\GRAPHIC.jpg",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "GRAPHIC.jpg",
        "CURRENT_MODE_MEMB": "Graphic"
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/BC-REPORT", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 18. `DESIGN/SRC/AIK-SRC2K/CC-ANAL` — SRC Column Checking Perform (SRC 柱验算执行)

> **功能：** 执行 SRC 柱验算（设计计算）。为 POST 专用动作。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CC-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "Select target type for design calculation. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
          "oneOf": [
            {
              "title": "All Elements",
              "const": "ALL"
            },
            {
              "title": "By Element No.",
              "const": "ELEMS"
            },
            {
              "title": "By Section No.",
              "const": "SECTIONS"
            }
          ],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "description": "Section No. Input.",
          "items": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `PERFORM_TYPE` | string | 选择设计计算对象类型。ELEMS：按单元编号，SECTIONS：按截面编号，ALL：全部单元。— `ALL`=全部单元; `ELEMS`=按单元编号; `SECTIONS`=按截面编号 | ALL |  |
| `ELEMS` | object | 输入单元编号。 |  |  |
| └ `KEYS` | array | 指定单个 ID |  |  |
| └ `TO` | string | 指定 ID 范围（例：'1to160'） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `SECTIONS` | array | 输入截面编号。 |  |  |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        1062
      ]
    }
  }
}
```

**Response Body**

```json
{
  "message": "success"
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "PERFORM_TYPE": "ALL",
        "ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CC-ANAL", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 19. `DESIGN/SRC/AIK-SRC2K/CC-TABLE` — SRC Column Checking Table (SRC 柱验算表格)

> **功能：** 查询 SRC 柱验算结果表格（HEAD/DATA）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CC-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "TABLE_TYPE"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "TABLE_TYPE": {
          "type": "string",
          "description": "Result Table Type",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element number input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify each element ID",
              "items": {
                "type": "integer"
              },
              "minItems": 1
            },
            "TO": {
              "type": "string",
              "description": "Specify element ID range (e.g., \"1to160\")"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify structure group name"
            }
          },
          "anyOf": [
            {
              "required": [
                "KEYS"
              ]
            },
            {
              "required": [
                "TO"
              ]
            },
            {
              "required": [
                "STRUCTURE_GROUP_NAME"
              ]
            }
          ]
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section property numbers to include in the table.",
          "items": {
            "type": "integer"
          },
          "minItems": 1
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Sorting criteria for member-based output (by Section No. or Member No.)",
          "default": 1,
          "oneOf": [
            {
              "title": "SECT",
              "const": 0
            },
            {
              "title": "MEMB",
              "const": 1
            }
          ]
        },
        "RESULT": {
          "type": "integer",
          "description": "Filter results by checking status",
          "default": 0,
          "oneOf": [
            {
              "title": "All",
              "const": 0
            },
            {
              "title": "OK",
              "const": 1
            },
            {
              "title": "NG",
              "const": 2
            }
          ]
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": "SRC Column Checking Result"
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "additionalProperties": false,
          "properties": {
            "FORCE": {
              "type": "string",
              "description": "Force unit"
            },
            "DIST": {
              "type": "string",
              "description": "Length/Distance unit"
            },
            "HEAT": {
              "type": "string",
              "description": "Heat unit"
            },
            "TEMP": {
              "type": "string",
              "description": "Temperature unit"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "description": "Response Number Format",
          "additionalProperties": false,
          "properties": {
            "FORMAT": {
              "type": "string",
              "description": "Number format",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "description": "Digit place",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of SRC Column Checking Result Table (SSRC79 style). SEL is not included.",
          "items": {
            "type": "string",
            "enum": [
              "CHK",
              "MEMB",
              "SECT",
              "COM",
              "SHR",
              "...(전체 31개)"
            ]
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `TABLE_TYPE` | string | 结果表类型 — 可能取值：`MEMB`, `PROP` |  | O |
| `ELEMS` | object | 输入单元编号。 |  |  |
| └ `KEYS` | array | 指定单个单元 ID |  |  |
| └ `TO` | string | 指定单元 ID 范围（例："1to160"） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `SECTIONS` | array | 表格中包含的截面特性编号列表。 |  |  |
| `PRI_SORT` | integer | 按构件输出的排序基准（截面编号或构件编号）— `0`=SECT; `1`=MEMB | 1 |  |
| `RESULT` | integer | 按验算状态过滤结果 — `0`=全部; `1`=OK; `2`=NG | 0 |  |
| `TABLE_NAME` | string | 结果表标题 | SRC Column Checking Result |  |
| `EXPORT_PATH` | string | 结果表保存路径 |  |  |
| `UNIT` | object | 结果单位设置 |  |  |
| └ `FORCE` | string | 力单位 |  |  |
| └ `DIST` | string | 长度/距离单位 |  |  |
| └ `HEAT` | string | 热量单位 |  |  |
| └ `TEMP` | string | 温度单位 |  |  |
| `STYLES` | object | 结果数字格式 |  |  |
| └ `FORMAT` | string | 数字格式 — 可能取值：`Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 小数位数 |  |  |
| `COMPONENTS` | array | SRC 柱验算结果表组成项（SSRC79 方式）。不包含 SEL。 |  |  |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "CHK",
      "MEMB",
      "SECT",
      "COM",
      "SHR",
      "Type",
      "Rebar",
      "Section",
      "Material",
      "Fys",
      "Fyr",
      "fc",
      "Bc",
      "Hc",
      "LCB",
      "Len",
      "Ly",
      "Lz",
      "Ky",
      "Kz",
      "Cmy",
      "Cmz",
      "Pa",
      "My",
      "Mz",
      "fa",
      "fby",
      "fbz",
      "Fa",
      "FBy",
      "FBz"
    ],
    "ELEMS": {
      "KEYS": [
        1062
      ]
    }
  }
}
```

**Response Body**

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "MM",
    "HEAD": [
      "CHK",
      "MEMB",
      "SECT",
      "COM",
      "SHR",
      "Type",
      "Rebar",
      "Section",
      "Material",
      "Fys",
      "Fyr",
      "fc",
      "Bc",
      "Hc",
      "LCB",
      "Len",
      "Ly",
      "Lz",
      "Ky",
      "Kz",
      "Cmy",
      "Cmz",
      "Pa",
      "My",
      "Mz",
      "fa",
      "fby",
      "fbz",
      "Fa",
      "FBy",
      "FBz"
    ],
    "DATA": [
      [
        "OK",
        "1062",
        "4",
        "0.394",
        "0.039",
        "RHB",
        "4-2-D4",
        "C src200x100x5.5/8, H 200x100x5.5/8",
        "SS410",
        "0.41000",
        "0.40000",
        "0.03000",
        "400.00",
        "400.00",
        "7",
        "4512.08",
        "4512.08",
        "4512.08",
        "1.000",
        "1.000",
        "0.850",
        "0.850",
        "-651.51",
        "26932.7",
        "2822.88",
        "0.2399",
        "0.0700",
        "0.0124",
        "0.7894",
        "0.2733",
        "0.2733"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "TABLE_TYPE": "MEMB",
        "PRI_SORT": 1,
        "RESULT": 0,
        "COMPONENTS": [
            "CHK",
            "MEMB",
            "SECT",
            "COM",
            "SHR",
            "Type",
            "Rebar",
            "Section",
            "Material",
            "Fys",
            "Fyr",
            "fc",
            "Bc",
            "Hc",
            "LCB",
            "Len",
            "Ly",
            "Lz",
            "Ky",
            "Kz",
            "Cmy",
            "Cmz",
            "Pa",
            "My",
            "Mz",
            "fa",
            "fby",
            "fbz",
            "Fa",
            "FBy",
            "FBz"
        ],
        "ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CC-TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 20. `DESIGN/SRC/AIK-SRC2K/CC-REPORT` — SRC Column Checking Report (SRC 柱验算报告)

> **功能：** 生成/查询 SRC 柱验算报告。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/CC-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "REPORT_TYPE",
        "EXPORT_PATH",
        "OUTPUT_NAME"
      ],
      "additionalProperties": false,
      "oneOf": [
        {
          "required": [
            "ELEMS"
          ]
        },
        {
          "required": [
            "SECTIONS"
          ]
        }
      ],
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "description": "Report Table Type",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "description": "Report output mode for element-based report",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Detail (DOC document)",
              "const": "Detail"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            }
          ]
        },
        "CURRENT_MODE_PROP": {
          "type": "string",
          "description": "Report output mode for property-based report",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            }
          ]
        },
        "ELEMS": {
          "type": "object",
          "description": "Element No. Input.",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "description": "List of section numbers to include in the report.",
          "items": {
            "type": "integer"
          }
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Directory path to save the report files"
        },
        "OUTPUT_NAME": {
          "type": "string",
          "description": "Output file base name. For multiple elements, files are prefixed with index and element number (e.g. 001_E100_filename.jpg, 002_E865_filename.jpg)"
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `REPORT_TYPE` | string | 报告表类型 — 可能取值：`MEMB`, `PROP` |  | O |
| `CURRENT_MODE_MEMB` | string | 以单元为基准的报告输出模式 — `Graphic`=图形（JPG 图像）; `Detail`=详细（DOC 文档）; `Summary`=摘要（TXT 文本） |  |  |
| `CURRENT_MODE_PROP` | string | 以特性为基准的报告输出模式 — `Graphic`=图形（JPG 图像）; `Summary`=摘要（TXT 文本） |  |  |
| `ELEMS` | object | 输入单元编号。 |  |  |
| └ `KEYS` | array | 指定单个 ID |  |  |
| └ `TO` | string | 指定 ID 范围（例：'1to160'） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `SECTIONS` | array | 报告中包含的截面编号列表。 |  |  |
| `EXPORT_PATH` | string | 保存报告文件的目录路径 |  | O |
| `OUTPUT_NAME` | string | 输出文件基本名称。存在多个单元时，文件名前会附加序号与单元编号（例：001_E100_filename.jpg, 002_E865_filename.jpg）。 |  | O |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "Detail.txt",
    "ELEMS": {
      "KEYS": [
        1062
      ]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\Detail.txt",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "CURRENT_MODE_MEMB": "Detail",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "Detail.txt",
        "ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/CC-REPORT", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 21. `DESIGN/SRC/AIK-SRC2K/OCHECK` — SRC Optimal Design (SRC 优化设计)

> **功能：** 执行 SRC 优化设计（Optimal Design）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/OCHECK
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "SECT_LIST",
        "OUTPUT"
      ],
      "properties": {
        "SECT_LIST": {
          "type": "array",
          "description": "Section List & Design Criteria (SRC). Each item corresponds to one Section No entry and its design criteria (POST input only).",
          "items": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "SECT_NO",
              "SECT_DB"
            ],
            "properties": {
              "SECT_NO": {
                "type": "integer",
                "description": "Section Number (input)."
              },
              "SECT_DB": {
                "type": "string",
                "description": "Design Criteria - SectDB",
                "oneOf": [
                  {
                    "title": "BUILT (Welded sections)",
                    "const": "BUILT"
                  },
                  {
                    "title": "KS21 (Korean Standard rolled sections)",
                    "const": "KS21"
                  },
                  {
                    "title": "USER (User-defined sections)",
                    "const": "USER"
                  }
                ]
              },
              "ALLOW": {
                "type": "number",
                "description": "Design Criteria - Allow",
                "default": 1
              },
              "D1": {
                "type": "number",
                "description": "Design Criteria - D1",
                "default": 0
              },
              "D2": {
                "type": "number",
                "description": "Design Criteria - D2",
                "default": 0
              },
              "D3": {
                "type": "number",
                "description": "Design Criteria - D3",
                "default": 0
              },
              "D4": {
                "type": "number",
                "description": "Design Criteria - D4",
                "default": 0
              },
              "D5": {
                "type": "number",
                "description": "Design Criteria - D5",
                "default": 0
              },
              "D6": {
                "type": "number",
                "description": "Design Criteria - D6",
                "default": 0
              }
            }
          }
        },
        "ANALYSIS_OPT": {
          "type": "object",
          "description": "Analysis option - number of re-analysis iterations",
          "additionalProperties": false,
          "properties": {
            "ANAL_TIME": {
              "type": "integer",
              "description": "Number of re-analysis iterations (max 10). Set 0 for section selection only without re-analysis.",
              "default": 1,
              "minimum": 0,
              "maximum": 10
            }
          }
        },
        "PLATE_THICKNESS": {
          "type": "array",
          "description": "Plate thickness list for BUILT sections (max 50 entries)",
          "items": {
            "type": "number"
          }
        },
        "COLUMN_DESIGN": {
          "type": "object",
          "description": "Column design settings for optimal design of column members",
          "additionalProperties": false,
          "properties": {
            "APPLIED_FORCES": {
              "type": "integer",
              "description": "Applied forces and moments method for column design",
              "default": 0,
              "oneOf": [
                {
                  "title": "Axial Forces and Moments",
                  "const": 0
                },
                {
                  "title": "Axial Forces Only",
                  "const": 1
                }
              ]
            },
            "JOINT_METHOD": {
              "type": "integer",
              "description": "Joint method of built-up column splices",
              "default": 1,
              "oneOf": [
                {
                  "title": "Internal Const (Fixed inside, expand outward)",
                  "const": 0
                },
                {
                  "title": "External Const (Fixed outside, adjust inward)",
                  "const": 1
                }
              ]
            }
          }
        },
        "USER_DEFINED_SECT": {
          "type": "array",
          "description": "User-defined section database. Each row defines a section with No, Shape, and dimensions D1-D6.",
          "items": {
            "type": "object",
            "required": [
              "NO",
              "SHAPE"
            ],
            "additionalProperties": false,
            "properties": {
              "NO": {
                "type": "integer",
                "description": "Section No."
              },
              "SHAPE": {
                "type": "string",
                "description": "Section shape (L, C, H, T, B, P, SR, SB, 2L, 2C)"
              },
              "D1": {
                "type": "number",
                "default": 0
              },
              "D2": {
                "type": "number",
                "default": 0
              },
              "D3": {
                "type": "number",
                "default": 0
              },
              "D4": {
                "type": "number",
                "default": 0
              },
              "D5": {
                "type": "number",
                "default": 0
              },
              "D6": {
                "type": "number",
                "default": 0
              }
            }
          }
        },
        "OUTPUT": {
          "type": "object",
          "description": "Output options for optimal design results (can select multiple simultaneously)",
          "required": [
            "EXPORT_PATH"
          ],
          "additionalProperties": false,
          "properties": {
            "GRAPH_MAX_RATIO": {
              "type": "boolean",
              "description": "Output Max. Ratio graph",
              "default": true
            },
            "GRAPH_AVG_RATIO": {
              "type": "boolean",
              "description": "Output Average Ratio graph",
              "default": true
            },
            "GRAPH_WEIGHT": {
              "type": "boolean",
              "description": "Output Weight graph",
              "default": true
            },
            "GRAPH_WEIGHT_SUM": {
              "type": "boolean",
              "description": "Output Weight Sum graph",
              "default": true
            },
            "GRAPH_WEIGHT_RATIO": {
              "type": "boolean",
              "description": "Output Weight Ratio graph",
              "default": true
            },
            "TEXT_REPORT": {
              "type": "boolean",
              "description": "Output results as text report to screen and file",
              "default": true
            },
            "MODEL_UPDATE": {
              "type": "boolean",
              "description": "Apply selected optimal sections to the model",
              "default": true
            },
            "EXPORT_PATH": {
              "type": "string",
              "description": "File path to save report output"
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `SECT_LIST` | array | 截面列表及设计标准（SRC）。每一项对应一个截面编号及其设计标准（仅 POST 输入）。 |  | O |
| └ `SECT_NO` | integer | 截面编号（输入）。 |  | O |
| └ `SECT_DB` | string | 设计标准 - 截面 DB — `BUILT`=BUILT（焊接截面）; `KS21`=KS21（韩国产业标准轧制截面）; `USER`=USER（用户自定义截面） |  | O |
| └ `ALLOW` | number | 设计标准 - 容许值 | 1 |  |
| └ `D1` | number | 设计标准 - D1 | 0 |  |
| └ `D2` | number | 设计标准 - D2 | 0 |  |
| └ `D3` | number | 设计标准 - D3 | 0 |  |
| └ `D4` | number | 设计标准 - D4 | 0 |  |
| └ `D5` | number | 设计标准 - D5 | 0 |  |
| └ `D6` | number | 设计标准 - D6 | 0 |  |
| `ANALYSIS_OPT` | object | 分析选项 - 重分析迭代次数 |  |  |
| └ `ANAL_TIME` | integer | 重分析迭代次数（最多 10）。仅选择截面、不做重分析时设为 0。 | 1 |  |
| `PLATE_THICKNESS` | array | BUILT 截面的板件厚度列表（最多 50 个） |  |  |
| `COLUMN_DESIGN` | object | 用于柱构件优化设计的柱设计设置 |  |  |
| └ `APPLIED_FORCES` | integer | 柱设计用适用构件内力·弯矩方法 — `0`=轴力及弯矩; `1`=仅轴力 | 0 |  |
| └ `JOINT_METHOD` | integer | 装配柱接头连接方法 — `0`=Internal Const（内侧固定，向外扩展）; `1`=External Const（外侧固定，内侧调整） | 1 |  |
| `USER_DEFINED_SECT` | array | 用户自定义截面数据库。每行以 No、形状、尺寸 D1~D6 定义截面。 |  |  |
| └ `NO` | integer | 截面编号 |  | O |
| └ `SHAPE` | string | 截面形状（L, C, H, T, B, P, SR, SB, 2L, 2C） |  | O |
| └ `D1` | number |  | 0 |  |
| └ `D2` | number |  | 0 |  |
| └ `D3` | number |  | 0 |  |
| └ `D4` | number |  | 0 |  |
| └ `D5` | number |  | 0 |  |
| └ `D6` | number |  | 0 |  |
| `OUTPUT` | object | 优化设计结果输出选项（可同时多选） |  | O |
| └ `GRAPH_MAX_RATIO` | boolean | 输出最大比值图形 | true |  |
| └ `GRAPH_AVG_RATIO` | boolean | 输出平均比值图形 | true |  |
| └ `GRAPH_WEIGHT` | boolean | 输出重量图形 | true |  |
| └ `GRAPH_WEIGHT_SUM` | boolean | 输出重量合计图形 | true |  |
| └ `GRAPH_WEIGHT_RATIO` | boolean | 输出重量比值图形 | true |  |
| └ `TEXT_REPORT` | boolean | 将结果以文本报告输出至屏幕与文件 | true |  |
| └ `MODEL_UPDATE` | boolean | 将所选最优截面应用于模型 | true |  |
| └ `EXPORT_PATH` | string | 保存报告输出的文件路径 |  | O |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "SECT_LIST": [
      {
        "SECT_NO": 4,
        "SECT_DB": "KS21",
        "ALLOW": 1,
        "D1": 0,
        "D2": 0,
        "D3": 0,
        "D4": 0,
        "D5": 0,
        "D6": 0
      }
    ],
    "OUTPUT": {
      "GRAPH_MAX_RATIO": true,
      "GRAPH_AVG_RATIO": true,
      "GRAPH_WEIGHT": true,
      "GRAPH_WEIGHT_SUM": true,
      "GRAPH_WEIGHT_RATIO": true,
      "TEXT_REPORT": true,
      "MODEL_UPDATE": true,
      "EXPORT_PATH": "C:\\MIDAS\\Result\\"
    }
  }
}
```

**Response Body**

```json
{
  "ODSR_RUN_RESPONSE": {
    "FORCE": "KN",
    "DIST": "MM",
    "HEAD": [
      "No",
      "Name",
      "SteelSize",
      "Astl",
      "COM",
      "Axial",
      "Ben-y",
      "Ben-z",
      "Shear"
    ],
    "DATA": [
      [
        "4",
        "C src200x100x5.5/8",
        "LH 150x75x3.2/4.5",
        "1126.00",
        "0.511",
        "0.339",
        "0.330",
        "0.047",
        "0.086"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "SECT_LIST": [
            {
                "SECT_NO": 4,
                "SECT_DB": "KS21",
                "ALLOW": 1,
                "D1": 0,
                "D2": 0,
                "D3": 0,
                "D4": 0,
                "D5": 0,
                "D6": 0
            }
        ],
        "OUTPUT": {
            "GRAPH_MAX_RATIO": true,
            "GRAPH_AVG_RATIO": true,
            "GRAPH_WEIGHT": true,
            "GRAPH_WEIGHT_SUM": true,
            "GRAPH_WEIGHT_RATIO": true,
            "TEXT_REPORT": true,
            "MODEL_UPDATE": true,
            "EXPORT_PATH": "C:\\MIDAS\\Result\\"
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/OCHECK", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 22. `DESIGN/SRC/AIK-SRC2K/TABLE` — SRC Beam Design Forces (SRC 梁设计内力)

> **功能：** 查询 SRC 梁设计内力（Design Forces）表格。URI 为 `TABLE` 共用，以 `TABLE_TYPE`=`SRCBEAMDESIGNFORCES` 区分。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "TABLE_TYPE"
      ],
      "additionalProperties": false,
      "properties": {
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Result Table Type",
          "enum": [
            "SRCBEAMDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "properties": {
            "FORCE": {
              "type": "string",
              "description": "Force unit"
            },
            "DIST": {
              "type": "string",
              "description": "Length/Distance unit"
            },
            "HEAT": {
              "type": "string",
              "description": "Heat unit"
            },
            "TEMP": {
              "type": "string",
              "description": "Temperature unit"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "description": "Response Number Format",
          "properties": {
            "FORMAT": {
              "type": "string",
              "description": "Number format",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "description": "Digit place",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fz",
              "Mx",
              "My(+)",
              "My(-)"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          }
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part1/4",
              "Part2/4",
              "Part3/4",
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `TABLE_NAME` | string | 结果表标题 |  |  |
| `TABLE_TYPE` | string | 结果表类型 — 可能取值：`SRCBEAMDESIGNFORCES` |  | O |
| `EXPORT_PATH` | string | 结果表保存路径 |  |  |
| `UNIT` | object | 结果单位设置 | System |  |
| └ `FORCE` | string | 力单位 |  |  |
| └ `DIST` | string | 长度/距离单位 |  |  |
| └ `HEAT` | string | 热量单位 |  |  |
| └ `TEMP` | string | 温度单位 |  |  |
| `STYLES` | object | 结果数字格式 | System |  |
| └ `FORMAT` | string | 数字格式 — 可能取值：`Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 小数位数 |  |  |
| `COMPONENTS` | array | 结果表组成项 |  |  |
| `NODE_ELEMS` | object | 输入节点/单元编号 |  |  |
| └ `KEYS` | array | 指定单个 ID |  |  |
| └ `TO` | string | 指定 ID 范围（例：'1to160'） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `PARTS` | array | 单元部件编号 | ["All"] |  |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
    "COMPONENTS": [
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(+)",
      "My(-)"
    ],
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        926
      ]
    }
  }
}
```

**Response Body**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "MM",
    "HEAD": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(+)",
      "My(-)"
    ],
    "DATA": [
      [
        "1",
        "926",
        "I",
        "gLCB5",
        "Max",
        "1.2976",
        "0.0000",
        "349.6767",
        "0.0000"
      ],
      [
        "2",
        "926",
        "I",
        "gLCB6",
        "Max",
        "1.3023",
        "0.0000",
        "364.0208",
        "0.0000"
      ],
      [
        "3",
        "926",
        "I",
        "gLCB7",
        "Max",
        "1.8279",
        "0.0000",
        "548.4875",
        "0.0000"
      ],
      [
        "4",
        "926",
        "J",
        "gLCB5",
        "Max",
        "1.5838",
        "0.0000",
        "341.5056",
        "0.0000"
      ],
      [
        "5",
        "926",
        "J",
        "gLCB6",
        "Max",
        "1.9019",
        "0.0000",
        "338.3354",
        "0.0000"
      ],
      [
        "6",
        "926",
        "J",
        "gLCB7",
        "Max",
        "2.3987",
        "0.0000",
        "535.9536",
        "0.0000"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "TABLE_TYPE": "SRCBEAMDESIGNFORCES",
        "COMPONENTS": [
            "Memb",
            "Part",
            "LComName",
            "Type",
            "Fz",
            "Mx",
            "My(+)",
            "My(-)"
        ],
        "PARTS": [
            "PartI",
            "PartJ"
        ],
        "NODE_ELEMS": {
            "KEYS": [
                926
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 23. `DESIGN/SRC/AIK-SRC2K/TABLE` — SRC Column Design Forces (SRC 柱设计内力)

> **功能：** 查询 SRC 柱设计内力（Design Forces）表格。URI 为 `TABLE` 共用，以 `TABLE_TYPE`=`SRCCOLUMNDESIGNFORCES` 区分。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Argument"
  ],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": [
        "TABLE_TYPE"
      ],
      "additionalProperties": false,
      "properties": {
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "description": "Result Table Type",
          "enum": [
            "SRCCOLUMNDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string",
          "description": "Result Table Save Path"
        },
        "UNIT": {
          "type": "object",
          "description": "Response Unit Setting",
          "properties": {
            "FORCE": {
              "type": "string",
              "description": "Force unit"
            },
            "DIST": {
              "type": "string",
              "description": "Length/Distance unit"
            },
            "HEAT": {
              "type": "string",
              "description": "Heat unit"
            },
            "TEMP": {
              "type": "string",
              "description": "Temperature unit"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "description": "Response Number Format",
          "properties": {
            "FORMAT": {
              "type": "string",
              "description": "Number format",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "description": "Digit place",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fx",
              "...(전체 10개)"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "description": "Node/Element No. Input",
          "properties": {
            "KEYS": {
              "type": "array",
              "description": "Specify Each ID",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string",
              "description": "Specify ID Range (e.g., '1to160')"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string",
              "description": "Specify Structure Group Name"
            }
          }
        },
        "PARTS": {
          "type": "array",
          "description": "Element Part Number",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part1/4",
              "Part2/4",
              "Part3/4",
              "PartJ"
            ]
          },
          "default": [
            "All"
          ]
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `TABLE_NAME` | string | 结果表标题 |  |  |
| `TABLE_TYPE` | string | 结果表类型 — 可能取值：`SRCCOLUMNDESIGNFORCES` |  | O |
| `EXPORT_PATH` | string | 结果表保存路径 |  |  |
| `UNIT` | object | 结果单位设置 | System |  |
| └ `FORCE` | string | 力单位 |  |  |
| └ `DIST` | string | 长度/距离单位 |  |  |
| └ `HEAT` | string | 热量单位 |  |  |
| └ `TEMP` | string | 温度单位 |  |  |
| `STYLES` | object | 结果数字格式 | System |  |
| └ `FORMAT` | string | 数字格式 — 可能取值：`Default`, `Fixed`, `Scientific`, `General` |  |  |
| └ `PLACE` | integer | 小数位数 |  |  |
| `COMPONENTS` | array | 结果表组成项 |  |  |
| `NODE_ELEMS` | object | 输入节点/单元编号 |  |  |
| └ `KEYS` | array | 指定单个 ID |  |  |
| └ `TO` | string | 指定 ID 范围（例：'1to160'） |  |  |
| └ `STRUCTURE_GROUP_NAME` | string | 指定结构组名称 |  |  |
| `PARTS` | array | 单元部件编号 | ["All"] |  |

> 上述字段位于 `"Argument"` 对象之下。

### Request / Response JSON

**Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
    "COMPONENTS": [],
    "PARTS": [
      "PartI",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1062
      ]
    }
  }
}
```

**Response Body**

```json
{
  "empty": {
    "FORCE": "KN",
    "DIST": "MM",
    "HEAD": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fx",
      "Fy",
      "Fz",
      "Mx",
      "My",
      "Mz"
    ],
    "DATA": [
      [
        "1",
        "1062",
        "I",
        "gLCB5",
        "Max",
        "-471.0683",
        "-0.3080",
        "-3.9955",
        "0.0000",
        "-0.0044",
        "-570.8548"
      ],
      [
        "2",
        "1062",
        "I",
        "gLCB6",
        "Max",
        "-527.5717",
        "-0.2221",
        "-5.1406",
        "0.0000",
        "-0.0058",
        "-547.2386"
      ],
      [
        "3",
        "1062",
        "I",
        "gLCB7",
        "Max",
        "-672.6419",
        "-1.0422",
        "-6.7439",
        "0.0000",
        "-0.0077",
        "-1879.5452"
      ],
      [
        "4",
        "1062",
        "J",
        "gLCB5",
        "Max",
        "-446.4142",
        "-0.3080",
        "-2.1875",
        "0.0000",
        "13949.2064",
        "818.9043"
      ],
      [
        "5",
        "1062",
        "J",
        "gLCB6",
        "Max",
        "-506.4395",
        "-0.2221",
        "-3.5909",
        "0.0000",
        "19698.7242",
        "454.9329"
      ],
      [
        "6",
        "1062",
        "J",
        "gLCB7",
        "Max",
        "-651.5098",
        "-1.0422",
        "-5.1942",
        "0.0000",
        "26932.6614",
        "2822.8793"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 执行设计/查询结果（POST 动作）
payload = {
    "Argument": {
        "TABLE_TYPE": "SRCCOLUMNDESIGNFORCES",
        "COMPONENTS": [],
        "PARTS": [
            "PartI",
            "PartJ"
        ],
        "NODE_ELEMS": {
            "KEYS": [
                1062
            ]
        }
    }
}
res = requests.post(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/TABLE", json=payload, headers=HEADERS)
res.raise_for_status()
print(res.json())
```

---

## 24. `DESIGN/SRC/AIK-SRC2K/MATD` — Modify SRC Material (SRC 材料修改)

> **功能：** 修改 SRC 材料（混凝土/钢材等级）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MATD
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is a material ID string (e.g., \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "STEEL",
            "CONCRETE",
            "REINFORCEMENT"
          ],
          "additionalProperties": false,
          "properties": {
            "STEEL": {
              "type": "object",
              "description": "Steel material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Steel material code type.",
                  "oneOf": [
                    {
                      "const": "None",
                      "title": "None"
                    },
                    {
                      "const": "Standard",
                      "title": "Standard"
                    }
                  ]
                },
                "STANDARD_CODE": {
                  "type": "string",
                  "description": "Steel standard code when CODE is Standard. Currently only KS22(S) is supported.",
                  "oneOf": [
                    {
                      "const": "KS22(S)",
                      "title": "KS22(S)"
                    }
                  ]
                },
                "GRADE": {
                  "type": "string",
                  "description": "Steel grade when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "SS235",
                      "title": "SS235"
                    },
                    {
                      "const": "SS275",
                      "title": "SS275"
                    },
                    {
                      "const": "SS315",
                      "title": "SS315"
                    },
                    {
                      "const": "SS410",
                      "title": "SS410"
                    },
                    {
                      "const": "SS450",
                      "title": "SS450"
                    },
                    "...(전체 68개)"
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "User-defined steel material name when CODE is None."
                },
                "ES": {
                  "type": "number",
                  "description": "Modulus of Elasticity. User input when CODE is None. Auto-filled when CODE is Standard."
                },
                "FU": {
                  "type": "number",
                  "description": "Tensile Strength. User input when CODE is None. Auto-filled when CODE is Standard."
                },
                "FY": {
                  "type": "number",
                  "description": "Yield Strength for CODE=None."
                },
                "FY1": {
                  "type": "number",
                  "description": "Yield Strength Fy1. Auto-filled when CODE is Standard."
                },
                "FY2": {
                  "type": "number",
                  "description": "Yield Strength Fy2. Auto-filled when CODE is Standard."
                },
                "FY3": {
                  "type": "number",
                  "description": "Yield Strength Fy3. Auto-filled when CODE is Standard."
                },
                "FY4": {
                  "type": "number",
                  "description": "Yield Strength Fy4. Auto-filled when CODE is Standard."
                },
                "FY5": {
                  "type": "number",
                  "description": "Yield Strength Fy5. Auto-filled when CODE is Standard."
                }
              },
              "allOf": [
                {
                  "if": {
                    "properties": {
                      "CODE": {
                        "const": "None"
                      }
                    },
                    "required": [
                      "CODE"
                    ]
                  },
                  "then": {
                    "required": [
                      "NAME",
                      "ES",
                      "FU",
                      "FY"
                    ]
                  }
                },
                {
                  "if": {
                    "properties": {
                      "CODE": {
                        "const": "Standard"
                      }
                    },
                    "required": [
                      "CODE"
                    ]
                  },
                  "then": {
                    "required": [
                      "STANDARD_CODE",
                      "GRADE"
                    ]
                  }
                }
              ]
            },
            "CONCRETE": {
              "type": "object",
              "description": "Concrete material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Concrete material code type.",
                  "oneOf": [
                    {
                      "const": "None",
                      "title": "None"
                    },
                    {
                      "const": "Standard",
                      "title": "Standard"
                    }
                  ]
                },
                "STANDARD_CODE": {
                  "type": "string",
                  "description": "Concrete standard code when CODE is Standard. Currently only KS19(RC) is supported.",
                  "oneOf": [
                    {
                      "const": "KS19(RC)",
                      "title": "KS19(RC)"
                    }
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "User-defined concrete material name when CODE is None."
                },
                "GRADE": {
                  "type": "string",
                  "description": "Concrete grade when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "C15",
                      "title": "C15"
                    },
                    {
                      "const": "C18",
                      "title": "C18"
                    },
                    {
                      "const": "C21",
                      "title": "C21"
                    },
                    {
                      "const": "C24",
                      "title": "C24"
                    },
                    {
                      "const": "C27",
                      "title": "C27"
                    },
                    "...(전체 20개)"
                  ]
                },
                "FC": {
                  "type": "number",
                  "description": "Specified Compressive Strength. User input when CODE is None. Auto-filled when CODE is Standard."
                }
              },
              "allOf": [
                {
                  "if": {
                    "properties": {
                      "CODE": {
                        "const": "None"
                      }
                    },
                    "required": [
                      "CODE"
                    ]
                  },
                  "then": {
                    "required": [
                      "NAME",
                      "FC"
                    ]
                  }
                },
                {
                  "if": {
                    "properties": {
                      "CODE": {
                        "const": "Standard"
                      }
                    },
                    "required": [
                      "CODE"
                    ]
                  },
                  "then": {
                    "required": [
                      "STANDARD_CODE",
                      "GRADE"
                    ]
                  }
                }
              ]
            },
            "REINFORCEMENT": {
              "type": "object",
              "description": "Reinforcement material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Reinforcement code type.",
                  "oneOf": [
                    {
                      "const": "None",
                      "title": "None"
                    },
                    {
                      "const": "Standard",
                      "title": "Standard"
                    }
                  ]
                },
                "STANDARD_CODE": {
                  "type": "string",
                  "description": "Reinforcement standard code when CODE is Standard. Currently only KS19(RC) is supported.",
                  "oneOf": [
                    {
                      "const": "KS19(RC)",
                      "title": "KS19(RC)"
                    }
                  ]
                },
                "MAIN_REBAR_NAME": {
                  "type": "string",
                  "description": "User-defined main rebar name when CODE is None."
                },
                "MAIN_REBAR_GRADE": {
                  "type": "string",
                  "description": "Grade of main rebar when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "SD300",
                      "title": "SD300"
                    },
                    {
                      "const": "SD400",
                      "title": "SD400"
                    },
                    {
                      "const": "SD500",
                      "title": "SD500"
                    },
                    {
                      "const": "SD600",
                      "title": "SD600"
                    },
                    {
                      "const": "SD700",
                      "title": "SD700"
                    },
                    {
                      "const": "SD400S",
                      "title": "SD400S"
                    },
                    {
                      "const": "SD500S",
                      "title": "SD500S"
                    },
                    {
                      "const": "SD600S",
                      "title": "SD600S"
                    }
                  ]
                },
                "FYR": {
                  "type": "number",
                  "description": "Yield Strength of main rebar. User input when CODE is None. Auto-filled when CODE is Standard."
                },
                "SUB_REBAR_NAME": {
                  "type": "string",
                  "description": "User-defined sub-rebar name when CODE is None."
                },
                "SUB_REBAR_GRADE": {
                  "type": "string",
                  "description": "Grade of sub-rebar when CODE is Standard.",
                  "oneOf": [
                    {
                      "const": "SD300",
                      "title": "SD300"
                    },
                    {
                      "const": "SD400",
                      "title": "SD400"
                    },
                    {
                      "const": "SD500",
                      "title": "SD500"
                    },
                    {
                      "const": "SD600",
                      "title": "SD600"
                    },
                    {
                      "const": "SD700",
                      "title": "SD700"
                    },
                    {
                      "const": "SD400S",
                      "title": "SD400S"
                    },
                    {
                      "const": "SD500S",
                      "title": "SD500S"
                    },
                    {
                      "const": "SD600S",
                      "title": "SD600S"
                    }
                  ]
                },
                "FYS": {
                  "type": "number",
                  "description": "Yield Strength of sub-rebar. User input when CODE is None. Auto-filled when CODE is Standard."
                }
              },
              "allOf": [
                {
                  "if": {
                    "properties": {
                      "CODE": {
                        "const": "None"
                      }
                    },
                    "required": [
                      "CODE"
                    ]
                  },
                  "then": {
                    "required": [
                      "MAIN_REBAR_NAME",
                      "FYR",
                      "SUB_REBAR_NAME",
                      "FYS"
                    ]
                  }
                },
                {
                  "if": {
                    "properties": {
                      "CODE": {
                        "const": "Standard"
                      }
                    },
                    "required": [
                      "CODE"
                    ]
                  },
                  "then": {
                    "required": [
                      "STANDARD_CODE",
                      "MAIN_REBAR_GRADE",
                      "SUB_REBAR_GRADE"
                    ]
                  }
                }
              ]
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `STEEL` | object | 选择钢材材质。 |  | O |
| └ `CODE` | string | 钢材材质代码类型。— `None`=无; `Standard`=标准 |  | O |
| └ `STANDARD_CODE` | string | CODE 为 Standard 时的钢材标准代码。当前仅支持 KS22(S)。— `KS22(S)`=KS22(S) |  |  |
| └ `GRADE` | string | CODE 为 Standard 时的钢材等级。— `SS235`=SS235; `SS275`=SS275; `SS315`=SS315; `SS410`=SS410; `SS450`=SS450; `SS550`=SS550; `SM275`=SM275; `SM355`=SM355; `SM420`=SM420; `SM460`=SM460; `SM275TMC`=SM275TMC; `SM355TMC`=SM355TMC …(全部 68 个) |  |  |
| └ `NAME` | string | CODE 为 None 时的用户自定义钢材名称。 |  |  |
| └ `ES` | number | 弹性模量。CODE 为 None 时由用户输入。CODE 为 Standard 时自动输入。 |  |  |
| └ `FU` | number | 抗拉强度。CODE 为 None 时由用户输入。CODE 为 Standard 时自动输入。 |  |  |
| └ `FY` | number | CODE=None 时的屈服强度。 |  |  |
| └ `FY1` | number | 屈服强度 Fy1。CODE 为 Standard 时自动输入。 |  |  |
| └ `FY2` | number | 屈服强度 Fy2。CODE 为 Standard 时自动输入。 |  |  |
| └ `FY3` | number | 屈服强度 Fy3。CODE 为 Standard 时自动输入。 |  |  |
| └ `FY4` | number | 屈服强度 Fy4。CODE 为 Standard 时自动输入。 |  |  |
| └ `FY5` | number | 屈服强度 Fy5。CODE 为 Standard 时自动输入。 |  |  |
| `CONCRETE` | object | 选择混凝土材质。 |  | O |
| └ `CODE` | string | 混凝土材质代码类型。— `None`=无; `Standard`=标准 |  | O |
| └ `STANDARD_CODE` | string | CODE 为 Standard 时的混凝土标准代码。当前仅支持 KS19(RC)。— `KS19(RC)`=KS19(RC) |  |  |
| └ `NAME` | string | CODE 为 None 时的用户自定义混凝土材质名称。 |  |  |
| └ `GRADE` | string | CODE 为 Standard 时的混凝土等级。— `C15`=C15; `C18`=C18; `C21`=C21; `C24`=C24; `C27`=C27; `C30`=C30; `C35`=C35; `C40`=C40; `C45`=C45; `C49`=C49; `C50`=C50; `C55`=C55 …(全部 20 个) |  |  |
| └ `FC` | number | 设计标准抗压强度。CODE 为 None 时由用户输入。CODE 为 Standard 时自动输入。 |  |  |
| `REINFORCEMENT` | object | 选择钢筋材质。 |  | O |
| └ `CODE` | string | 钢筋代码类型。— `None`=无; `Standard`=标准 |  | O |
| └ `STANDARD_CODE` | string | CODE 为 Standard 时的钢筋标准代码。当前仅支持 KS19(RC)。— `KS19(RC)`=KS19(RC) |  |  |
| └ `MAIN_REBAR_NAME` | string | CODE 为 None 时的用户自定义主筋名称。 |  |  |
| └ `MAIN_REBAR_GRADE` | string | CODE 为 Standard 时的主筋等级。— `SD300`=SD300; `SD400`=SD400; `SD500`=SD500; `SD600`=SD600; `SD700`=SD700; `SD400S`=SD400S; `SD500S`=SD500S; `SD600S`=SD600S |  |  |
| └ `FYR` | number | 主筋屈服强度。CODE 为 None 时由用户输入。CODE 为 Standard 时自动输入。 |  |  |
| └ `SUB_REBAR_NAME` | string | CODE 为 None 时的用户自定义辅筋名称。 |  |  |
| └ `SUB_REBAR_GRADE` | string | CODE 为 Standard 时的辅筋等级。— `SD300`=SD300; `SD400`=SD400; `SD500`=SD500; `SD600`=SD600; `SD700`=SD700; `SD400S`=SD400S; `SD500S`=SD500S; `SD600S`=SD600S |  |  |
| └ `FYS` | number | 辅筋屈服强度。CODE 为 None 时由用户输入。CODE 为 Standard 时自动输入。 |  |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "5": {
      "STEEL": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS22(S)",
        "GRADE": "SM275TMC"
      },
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C65"
      },
      "REINFORCEMENT": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD700",
        "SUB_REBAR_GRADE": "SD700"
      }
    }
  }
}
```

**Response Body**

```json
{
  "MATD": {
    "5": {
      "STEEL": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS22(S)",
        "GRADE": "SM275TMC"
      },
      "CONCRETE": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C65"
      },
      "REINFORCEMENT": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD700",
        "SUB_REBAR_GRADE": "SD700"
      }
    }
  }
}
```

> ⚠️ **2026-08-27 确认（article id `59471948895129`）：** GET/PUT 响应示例中的 `"CODE"` 取值为 `"STANDARD"`（大写），与 PUT 请求示例、JSON Schema 中的 `oneOf`("Standard") 大小写不一致 — 属原文自身的矛盾，示例原文照录保持。（与第 26 章 MATD 为同一模式。）

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "5": {
            "STEEL": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS22(S)",
                "GRADE": "SM275TMC"
            },
            "CONCRETE": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "GRADE": "C65"
            },
            "REINFORCEMENT": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "MAIN_REBAR_GRADE": "SD700",
                "SUB_REBAR_GRADE": "SD700"
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MATD", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MATD", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MATD", headers=HEADERS)
```

---

## 25. `DESIGN/SRC/AIK-SRC2K/MCRD` — Modify SRC Column Section Data (SRC 柱截面数据修改)

> **功能：** 修改 SRC 柱截面数据（内置型钢布置等）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MCRD
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is a section ID string.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "MAIN_BAR",
            "SHEAR_BAR"
          ],
          "additionalProperties": false,
          "properties": {
            "MAIN_BAR": {
              "type": "object",
              "required": [
                "NUM",
                "NAME",
                "ROW",
                "DO"
              ],
              "description": "Main rebar data.",
              "additionalProperties": false,
              "properties": {
                "USE_REBAR_SPACE": {
                  "type": "boolean",
                  "description": "Auto-calculated rebar spacing.",
                  "default": true
                },
                "REBAR_SPACE": {
                  "type": "number",
                  "description": "Main rebar spacing. Used when USE_REBAR_SPACE is false.",
                  "default": 0,
                  "minimum": 0
                },
                "NUM": {
                  "type": "integer",
                  "description": "Total number of main rebars. Must be a multiple of 4.",
                  "minimum": 4,
                  "multipleOf": 4
                },
                "NAME": {
                  "type": "string",
                  "description": "Main rebar size designation.",
                  "oneOf": [
                    {
                      "title": "D4",
                      "const": "D4"
                    },
                    {
                      "title": "D5",
                      "const": "D5"
                    },
                    {
                      "title": "D6",
                      "const": "D6"
                    },
                    {
                      "title": "D7",
                      "const": "D7"
                    },
                    {
                      "title": "D8",
                      "const": "D8"
                    },
                    "...(전체 19개)"
                  ]
                },
                "ROW": {
                  "type": "integer",
                  "description": "Number of rebar rows for rectangular section. Must be a multiple of 2.",
                  "minimum": 2,
                  "multipleOf": 2
                },
                "DO": {
                  "type": "number",
                  "description": "Concrete cover / center distance d0.",
                  "minimum": 0
                }
              }
            },
            "SHEAR_BAR": {
              "type": "object",
              "required": [
                "NAME",
                "DIST"
              ],
              "description": "Hoop/tie rebar data.",
              "additionalProperties": false,
              "properties": {
                "NAME": {
                  "type": "string",
                  "description": "Hoop/tie rebar size designation.",
                  "oneOf": [
                    {
                      "title": "D4",
                      "const": "D4"
                    },
                    {
                      "title": "D5",
                      "const": "D5"
                    },
                    {
                      "title": "D6",
                      "const": "D6"
                    },
                    {
                      "title": "D7",
                      "const": "D7"
                    },
                    {
                      "title": "D8",
                      "const": "D8"
                    },
                    "...(전체 19개)"
                  ]
                },
                "DIST": {
                  "type": "number",
                  "description": "Hoop/tie rebar spacing. Used when USE_REBAR_SPACE is false.",
                  "exclusiveMinimum": 0
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

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `MAIN_BAR` | object | 主筋数据。 |  | O |
| └ `USE_REBAR_SPACE` | boolean | 自动计算的钢筋间距。 | true |  |
| └ `REBAR_SPACE` | number | 主筋间距。USE_REBAR_SPACE 为 false 时使用。 | 0 |  |
| └ `NUM` | integer | 主筋总根数。须为 4 的倍数。 |  | O |
| └ `NAME` | string | 主筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ `ROW` | integer | 矩形截面的钢筋排数。须为 2 的倍数。 |  | O |
| └ `DO` | number | 混凝土保护层 / 中心间距 d0。 |  | O |
| `SHEAR_BAR` | object | Hoop/Tie 箍筋数据。 |  | O |
| └ `NAME` | string | Hoop/Tie 箍筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ `DIST` | number | Hoop/Tie 箍筋间距。USE_REBAR_SPACE 为 false 时使用。 |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "4": {
      "MAIN_BAR": {
        "USE_REBAR_SPACE": true,
        "REBAR_SPACE": 0,
        "NUM": 4,
        "NAME": "D4",
        "ROW": 2,
        "DO": 0.05
      },
      "SHEAR_BAR": {
        "NAME": "D4",
        "DIST": 300
      }
    }
  }
}
```

**Response Body**

```json
{
  "MCRD": {
    "4": {
      "MAIN_BAR": {
        "USE_REBAR_SPACE": true,
        "NUM": 4,
        "NAME": "D4",
        "ROW": 2,
        "DO": 0.05,
        "REBAR_SPACE": 0
      },
      "SHEAR_BAR": {
        "NAME": "D4",
        "DIST": 300
      }
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "4": {
            "MAIN_BAR": {
                "USE_REBAR_SPACE": true,
                "REBAR_SPACE": 0,
                "NUM": 4,
                "NAME": "D4",
                "ROW": 2,
                "DO": 0.05
            },
            "SHEAR_BAR": {
                "NAME": "D4",
                "DIST": 300
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MCRD", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MCRD", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MCRD", headers=HEADERS)
```

---

## 26. `DESIGN/SRC/AIK-SRC2K/MEMB` — Member Assignment (构件指定)

> **功能：** 管理设计构件（单元→构件）的指定。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MEMB
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "AELEM"
          ],
          "additionalProperties": false,
          "properties": {
            "AELEM": {
              "type": "array",
              "description": "Element Lists",
              "items": {
                "type": "integer"
              }
            },
            "bREVERSE": {
              "type": "boolean",
              "description": "Reverse Local Direction",
              "default": false
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `AELEM` | array | 单元列表 |  | O |
| `bREVERSE` | boolean | 构件轴方向反转 | false |  |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        859,
        860,
        861
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        883,
        868
      ],
      "bREVERSE": true
    }
  }
}
```

**Response Body**

```json
{
  "MEMB": {
    "1": {
      "AELEM": [
        859,
        860,
        861
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        883,
        868
      ],
      "bREVERSE": true
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "1": {
            "AELEM": [
                859,
                860,
                861
            ],
            "bREVERSE": true
        },
        "2": {
            "AELEM": [
                883,
                868
            ],
            "bREVERSE": true
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MEMB", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MEMB", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MEMB", headers=HEADERS)
```

---

## 27. `DESIGN/SRC/AIK-SRC2K/MRBD` — Modify SRC Beam Section Data (SRC 梁截面数据修改)

> **功能：** 修改 SRC 梁截面数据（内置型钢/钢筋布置等）。

### Input URI

```
{base url}/DESIGN/SRC/AIK-SRC2K/MRBD
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is a Section ID.",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "DT",
            "DB",
            "SHEAR_BAR"
          ],
          "anyOf": [
            {
              "required": [
                "BAR_SECTOR_I"
              ]
            },
            {
              "required": [
                "BAR_SECTOR_M"
              ]
            },
            {
              "required": [
                "BAR_SECTOR_J"
              ]
            }
          ],
          "additionalProperties": false,
          "properties": {
            "BAR_SECTOR_I": {
              "type": "object",
              "description": "Rebar configuration at I-section.",
              "required": [
                "TOP",
                "BOT",
                "STIRRUP_SPACE"
              ],
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Top rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "BOT": {
                  "type": "object",
                  "description": "Bottom rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "STIRRUP_SPACE": {
                  "type": "number",
                  "description": "Stirrup spacing at I-section.",
                  "exclusiveMinimum": 0
                },
                "STIRRUP_NUM": {
                  "type": "integer",
                  "description": "Number of stirrup sets at I-section.",
                  "default": 2,
                  "minimum": 2,
                  "maximum": 20
                }
              }
            },
            "BAR_SECTOR_M": {
              "type": "object",
              "description": "Rebar configuration at M-section.",
              "required": [
                "TOP",
                "BOT",
                "STIRRUP_SPACE"
              ],
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Top rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "BOT": {
                  "type": "object",
                  "description": "Bottom rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "STIRRUP_SPACE": {
                  "type": "number",
                  "description": "Stirrup spacing at M-section.",
                  "exclusiveMinimum": 0
                },
                "STIRRUP_NUM": {
                  "type": "integer",
                  "description": "Number of stirrup sets at M-section.",
                  "default": 2,
                  "minimum": 2,
                  "maximum": 20
                }
              }
            },
            "BAR_SECTOR_J": {
              "type": "object",
              "description": "Rebar configuration at J-section.",
              "required": [
                "TOP",
                "BOT",
                "STIRRUP_SPACE"
              ],
              "additionalProperties": false,
              "properties": {
                "TOP": {
                  "type": "object",
                  "description": "Top rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of top rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of top rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of top rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "BOT": {
                  "type": "object",
                  "description": "Bottom rebar configuration.",
                  "required": [
                    "LAYER1"
                  ],
                  "additionalProperties": false,
                  "properties": {
                    "LAYER1": {
                      "type": "object",
                      "description": "First layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the first layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the first layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    },
                    "LAYER2": {
                      "type": "object",
                      "description": "Second layer of bottom rebars.",
                      "required": [
                        "NAME",
                        "NUM"
                      ],
                      "additionalProperties": false,
                      "properties": {
                        "NAME": {
                          "type": "string",
                          "description": "Rebar size designation for the second layer of bottom rebars.",
                          "oneOf": [
                            {
                              "title": "D4",
                              "const": "D4"
                            },
                            {
                              "title": "D5",
                              "const": "D5"
                            },
                            {
                              "title": "D6",
                              "const": "D6"
                            },
                            {
                              "title": "D7",
                              "const": "D7"
                            },
                            {
                              "title": "D8",
                              "const": "D8"
                            },
                            "...(전체 19개)"
                          ]
                        },
                        "NUM": {
                          "type": "integer",
                          "description": "Number of rebars in the second layer of bottom rebars.",
                          "minimum": 1
                        }
                      }
                    }
                  }
                },
                "STIRRUP_SPACE": {
                  "type": "number",
                  "description": "Stirrup spacing at J-section.",
                  "exclusiveMinimum": 0
                },
                "STIRRUP_NUM": {
                  "type": "integer",
                  "description": "Number of stirrup sets at J-section.",
                  "default": 2,
                  "minimum": 2,
                  "maximum": 20
                }
              }
            },
            "DT": {
              "type": "number",
              "description": "Top rebar cover thickness.",
              "exclusiveMinimum": 0
            },
            "DB": {
              "type": "number",
              "description": "Bottom rebar cover thickness.",
              "exclusiveMinimum": 0
            },
            "SHEAR_BAR": {
              "type": "string",
              "description": "Stirrup rebar size designation.",
              "oneOf": [
                {
                  "title": "D4",
                  "const": "D4"
                },
                {
                  "title": "D5",
                  "const": "D5"
                },
                {
                  "title": "D6",
                  "const": "D6"
                },
                {
                  "title": "D7",
                  "const": "D7"
                },
                {
                  "title": "D8",
                  "const": "D8"
                },
                "...(전체 19개)"
              ]
            }
          }
        }
      }
    }
  }
}
```

### 参数

| Key | 值类型 | 说明 | 默认值 | 必填 |
|-----|------|------|--------|------|
| `BAR_SECTOR_I` | object | I 端截面钢筋布置。 |  |  |
| └ `TOP` | object | 上部钢筋布置。 |  | O |
| └ └ `LAYER1` | object | 上部钢筋第 1 层。 |  | O |
| └ └ └ `NAME` | string | 上部钢筋第 1 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 上部钢筋第 1 层的钢筋根数。 |  | O |
| └ └ `LAYER2` | object | 上部钢筋第 2 层。 |  |  |
| └ └ └ `NAME` | string | 上部钢筋第 2 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 上部钢筋第 2 层的钢筋根数。 |  | O |
| └ `BOT` | object | 下部钢筋布置。 |  | O |
| └ └ `LAYER1` | object | 下部钢筋第 1 层。 |  | O |
| └ └ └ `NAME` | string | 下部钢筋第 1 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 下部钢筋第 1 层的钢筋根数。 |  | O |
| └ └ `LAYER2` | object | 下部钢筋第 2 层。 |  |  |
| └ └ └ `NAME` | string | 下部钢筋第 2 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 下部钢筋第 2 层的钢筋根数。 |  | O |
| └ `STIRRUP_SPACE` | number | I 端截面箍筋间距。 |  | O |
| └ `STIRRUP_NUM` | integer | I 端截面箍筋组数。 | 2 |  |
| `BAR_SECTOR_M` | object | M 端截面钢筋布置。 |  |  |
| └ `TOP` | object | 上部钢筋布置。 |  | O |
| └ └ `LAYER1` | object | 上部钢筋第 1 层。 |  | O |
| └ └ └ `NAME` | string | 上部钢筋第 1 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 上部钢筋第 1 层的钢筋根数。 |  | O |
| └ └ `LAYER2` | object | 上部钢筋第 2 层。 |  |  |
| └ └ └ `NAME` | string | 上部钢筋第 2 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 上部钢筋第 2 层的钢筋根数。 |  | O |
| └ `BOT` | object | 下部钢筋布置。 |  | O |
| └ └ `LAYER1` | object | 下部钢筋第 1 层。 |  | O |
| └ └ └ `NAME` | string | 下部钢筋第 1 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 下部钢筋第 1 层的钢筋根数。 |  | O |
| └ └ `LAYER2` | object | 下部钢筋第 2 层。 |  |  |
| └ └ └ `NAME` | string | 下部钢筋第 2 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 下部钢筋第 2 层的钢筋根数。 |  | O |
| └ `STIRRUP_SPACE` | number | M 端截面箍筋间距。 |  | O |
| └ `STIRRUP_NUM` | integer | M 端截面箍筋组数。 | 2 |  |
| `BAR_SECTOR_J` | object | J 端截面钢筋布置。 |  |  |
| └ `TOP` | object | 上部钢筋布置。 |  | O |
| └ └ `LAYER1` | object | 上部钢筋第 1 层。 |  | O |
| └ └ └ `NAME` | string | 上部钢筋第 1 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 上部钢筋第 1 层的钢筋根数。 |  | O |
| └ └ `LAYER2` | object | 上部钢筋第 2 层。 |  |  |
| └ └ └ `NAME` | string | 上部钢筋第 2 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 上部钢筋第 2 层的钢筋根数。 |  | O |
| └ `BOT` | object | 下部钢筋布置。 |  | O |
| └ └ `LAYER1` | object | 下部钢筋第 1 层。 |  | O |
| └ └ └ `NAME` | string | 下部钢筋第 1 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 下部钢筋第 1 层的钢筋根数。 |  | O |
| └ └ `LAYER2` | object | 下部钢筋第 2 层。 |  |  |
| └ └ └ `NAME` | string | 下部钢筋第 2 层的钢筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |
| └ └ └ `NUM` | integer | 下部钢筋第 2 层的钢筋根数。 |  | O |
| └ `STIRRUP_SPACE` | number | J 端截面箍筋间距。 |  | O |
| └ `STIRRUP_NUM` | integer | J 端截面箍筋组数。 | 2 |  |
| `DT` | number | 上部钢筋保护层厚度。 |  | O |
| `DB` | number | 下部钢筋保护层厚度。 |  | O |
| `SHEAR_BAR` | string | 箍筋规格。— `D4`=D4; `D5`=D5; `D6`=D6; `D7`=D7; `D8`=D8; `D10`=D10; `D13`=D13; `D16`=D16; `D19`=D19; `D22`=D22; `D25`=D25; `D29`=D29 …(全部 19 个) |  | O |

> 上述字段位于 `"Assign"` 对象的各 ID 键（例：`"1"`）之下。

### Request / Response JSON

**Request Body**

```json
{
  "Assign": {
    "3": {
      "DT": 0.1,
      "DB": 0.1,
      "SHEAR_BAR": "D4",
      "BAR_SECTOR_I": {
        "STIRRUP_SPACE": 150,
        "STIRRUP_NUM": 2,
        "TOP": {
          "LAYER1": {
            "NAME": "D32",
            "NUM": 2
          },
          "LAYER2": {
            "NAME": "D32",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D35",
            "NUM": 1
          },
          "LAYER2": {
            "NAME": "D35",
            "NUM": 3
          }
        }
      },
      "BAR_SECTOR_M": {
        "STIRRUP_SPACE": 150,
        "TOP": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 1
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        }
      },
      "BAR_SECTOR_J": {
        "STIRRUP_SPACE": 150,
        "TOP": {
          "LAYER1": {
            "NAME": "D51",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        }
      }
    }
  }
}
```

**Response Body**

```json
{
  "MRBD": {
    "3": {
      "BAR_SECTOR_I": {
        "TOP": {
          "LAYER1": {
            "NAME": "D32",
            "NUM": 2
          },
          "LAYER2": {
            "NAME": "D32",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D35",
            "NUM": 1
          },
          "LAYER2": {
            "NAME": "D35",
            "NUM": 3
          }
        },
        "STIRRUP_SPACE": 150,
        "STIRRUP_NUM": 2
      },
      "BAR_SECTOR_M": {
        "TOP": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 1
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        },
        "STIRRUP_SPACE": 150
      },
      "BAR_SECTOR_J": {
        "TOP": {
          "LAYER1": {
            "NAME": "D51",
            "NUM": 2
          }
        },
        "BOT": {
          "LAYER1": {
            "NAME": "D43",
            "NUM": 2
          }
        },
        "STIRRUP_SPACE": 150
      },
      "DT": 0.1,
      "DB": 0.1,
      "SHEAR_BAR": "D4"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "在此填入_已获取的密钥", "Content-Type": "application/json"}

# 设置数据（PUT）
payload = {
    "Assign": {
        "3": {
            "DT": 0.1,
            "DB": 0.1,
            "SHEAR_BAR": "D4",
            "BAR_SECTOR_I": {
                "STIRRUP_SPACE": 150,
                "STIRRUP_NUM": 2,
                "TOP": {
                    "LAYER1": {
                        "NAME": "D32",
                        "NUM": 2
                    },
                    "LAYER2": {
                        "NAME": "D32",
                        "NUM": 2
                    }
                },
                "BOT": {
                    "LAYER1": {
                        "NAME": "D35",
                        "NUM": 1
                    },
                    "LAYER2": {
                        "NAME": "D35",
                        "NUM": 3
                    }
                }
            },
            "BAR_SECTOR_M": {
                "STIRRUP_SPACE": 150,
                "TOP": {
                    "LAYER1": {
                        "NAME": "D43",
                        "NUM": 1
                    }
                },
                "BOT": {
                    "LAYER1": {
                        "NAME": "D43",
                        "NUM": 2
                    }
                }
            },
            "BAR_SECTOR_J": {
                "STIRRUP_SPACE": 150,
                "TOP": {
                    "LAYER1": {
                        "NAME": "D51",
                        "NUM": 2
                    }
                },
                "BOT": {
                    "LAYER1": {
                        "NAME": "D43",
                        "NUM": 2
                    }
                }
            }
        }
    }
}
res = requests.put(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MRBD", json=payload, headers=HEADERS)
res.raise_for_status()

# 查询设置值（GET）
got = requests.get(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MRBD", headers=HEADERS)
print(got.json())

# 删除：requests.delete(f"{BASE_URL}/DESIGN/SRC/AIK-SRC2K/MRBD", headers=HEADERS)
```
