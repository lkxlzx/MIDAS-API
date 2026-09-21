# 25. Design Code – STEEL KDS 41 30:2022 (钢结构设计)

> **适用产品：** MIDAS Gen NX · MIDAS Civil NX
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **认证头部：** `MAPI-Key: <已签发的密钥>`
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../25_Design_Steel_KDS41302022.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本章涉及**钢结构（Steel）设计标准 KDS 41 30:2022** 的设计输入·执行·结果相关 **28个端点**（公共前缀 `KDS-41-30-2022/<CODE>` 端点27个 + 钢结构设计代码选择端点 `DSTL` 1个）。除 `DSTL` 外的27个共享以下公共 URI 前缀。

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/<CODE>
```

这里的 `<CODE>` 为各端点代码（`DCO`、`LENG`、`MEMB`、`CODE-ANAL` 等）。

> ⚠️ **2026-09-06 新增反映：** `DESIGN/STEEL/DSTL`（选择当前有效的钢结构设计代码）的原文生成日
> 虽为 2026-05-04、此前早已存在，但在定期检查（2026-09-06）中确认到该文章与手册落地页
> 一同更新（2026-09-04）才发现。它是不使用 `KDS-41-30-2022` 前缀的独立
> URI，故对编号体系无影响，以 `## 0.` 追加。RC 侧的对应端点为
> [26章 `DESIGN/RC/DRC`](./26_Design_RC_KDS41202022.md#0-designrcdrc--rc-design-code-rc-设计代码选择)。

> **公共约定 — 请求包装（wrapper）：**
> - **设置（config）·构件（member）端点**在最上层放置 `"Assign"` 对象，其内以对象 ID（要素·构件·材质 ID 等）作为**字符串键**，将各条记录收纳其中。GET 响应的最上层键会变为该端点代码（例：`DCO`、`LENG`），并以相同结构返回。
> - **执行/结果（action）端点**为 POST 专用作业，不放 `"Assign"`，而在最上层放置 `"Argument"` 对象。

> **三种方法模式：**
> 1. **Config-singleton**（例：`DCO`、`DCTL`、`LLRF`、`SRDF`、`SMODI`、`MEMB`）— 每模型一组的整体/集合设置，**没有 POST**。记录在首次查询时隐式生成，或以 **PUT** 设置/修改。（`LCTB` 为仅支持 `GET`·`DELETE` 的派生信息。）
> 2. **Member-CRUD**（例：`HCBM`、`LENG`、`KFAC`、`LTSR`、`SLRS`、`SERV`、`EQCT`、`ULCT`、`SUEQ`、`CRCM`、`CMFT`、`FMAG`、`CBFT`、`MBTP`、`MLLR`）— 支持基于构件/ID 键的**完整 CRUD**（POST·GET·PUT·DELETE）。
> 3. **POST-action**（`CODE-ANAL`、`CODE-TABLE`、`CODE-REPORT`、`DREULT`、`TABLE`）— 作为校核执行·结果表·报告书·图像输出等**作业，仅支持 POST**。

> ⚠️ **各端点的 Active Methods 各不相同。** 请严格遵循下方各节的 **Active Methods**。（例：`DCO`/`DCTL`/`LLRF`/`SMODI`/`MEMB` = GET·PUT·DELETE，`LCTB` = GET·DELETE，`SRDF` = GET·DELETE·PUT，5个 action 端点 = POST。）

---

## Endpoint 列表

### 组 1. 设计代码·一般设置

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 0 | [`DESIGN/STEEL/DSTL`](#0-designsteeldstl--design-code-钢结构设计代码选择) | Design Code（钢结构设计代码选择，不使用 `KDS-41-30-2022` 前缀） | GET · PUT · DELETE |
| 1 | [`.../DCO`](#1-designsteelkds-41-30-2022dco--design-code-option-设计代码选项) | Design Code Option（设计代码选项） | GET · PUT · DELETE |
| 2 | [`.../DCTL`](#2-designsteelkds-41-30-2022dctl--definition-of-frame-框架定义) | Definition of Frame（框架定义） | GET · PUT · DELETE |
| 3 | [`.../LLRF`](#3-designsteelkds-41-30-2022llrf--live-load-reduction-factor-活荷载折减系数) | Live Load Reduction Factor（活荷载折减系数） | GET · PUT · DELETE |
| 4 | [`.../LCTB`](#4-designsteelkds-41-30-2022lctb--load-contribution-for-nonlinear-load-case-非线性荷载工况的荷载贡献) | Load Contribution for Nonlinear Load Case（非线性荷载工况的荷载贡献） | GET · DELETE |
| 5 | [`.../SRDF`](#5-designsteelkds-41-30-2022srdf--strength-reduction-factors-强度折减系数-φ) | Strength Reduction Factors（强度折减系数 φ） | GET · DELETE · PUT |
| 6 | [`.../SERV`](#6-designsteelkds-41-30-2022serv--serviceability-parameters-使用性参数) | Serviceability Parameters（使用性参数） | POST · GET · PUT · DELETE |
| 7 | [`.../EQCT`](#7-designsteelkds-41-30-2022eqct--seismic-load-combination-type-地震作用组合类型) | Seismic Load Combination Type（地震作用组合类型） | POST · GET · PUT · DELETE |
| 8 | [`.../ULCT`](#8-designsteelkds-41-30-2022ulct--underground-load-combination-type-地下荷载组合类型) | Underground Load Combination Type（地下荷载组合类型） | POST · GET · PUT · DELETE |
| 9 | [`.../SUEQ`](#9-designsteelkds-41-30-2022sueq--scale-up-factor-for-earthquake-地震放大系数) | Scale up Factor for Earthquake（地震放大系数） | POST · GET · PUT · DELETE |
| 10 | [`.../CRCM`](#10-designsteelkds-41-30-2022crcm--combined-ratio-calculation-method-for-circular-section-圆形截面组合比计算法) | Combined Ratio Calculation Method for Circular Section（圆形截面组合比计算法） | POST · GET · PUT · DELETE |

### 组 2. 按构件设计参数

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 11 | [`.../HCBM`](#11-designsteelkds-41-30-2022hcbm--haunched-beam-assignment-加腋梁指定) | Haunched Beam Assignment（加腋梁指定） | POST · GET · PUT · DELETE |
| 12 | [`.../LENG`](#12-designsteelkds-41-30-2022leng--unbraced-length-未支撑长度-l-lb) | Unbraced Length（未支撑长度 L, Lb） | POST · GET · PUT · DELETE |
| 13 | [`.../KFAC`](#13-designsteelkds-41-30-2022kfac--effective-length-factor-有效屈曲长度系数-k) | Effective Length Factor（有效屈曲长度系数 K） | POST · GET · PUT · DELETE |
| 14 | [`.../LTSR`](#14-designsteelkds-41-30-2022ltsr--limiting-slenderness-ratio-长细比限制) | Limiting Slenderness Ratio（长细比限制） | POST · GET · PUT · DELETE |
| 15 | [`.../CMFT`](#15-designsteelkds-41-30-2022cmft--equivalent-moment-correction-factor-等效弯矩修正系数-cm) | Equivalent Moment Correction Factor（等效弯矩修正系数 Cm） | POST · GET · PUT · DELETE |
| 16 | [`.../FMAG`](#16-designsteelkds-41-30-2022fmag--moment-magnifier-弯矩放大系数-b1δb-b2δs) | Moment Magnifier（弯矩放大系数 B1/Δb, B2/Δs） | POST · GET · PUT · DELETE |
| 17 | [`.../CBFT`](#17-designsteelkds-41-30-2022cbft--bending-coefficient-弯曲系数-cb) | Bending Coefficient（弯曲系数 Cb） | POST · GET · PUT · DELETE |
| 18 | [`.../MBTP`](#18-designsteelkds-41-30-2022mbtp--modify-member-type-构件类型修改) | Modify Member Type（构件类型修改） | POST · GET · PUT · DELETE |
| 19 | [`.../SLRS`](#19-designsteelkds-41-30-2022slrs--seismic-load-resisting-system-by-member-按构件抗震抗侧力体系) | Seismic Load Resisting System by Member（按构件抗震抗侧力体系） | POST · GET · PUT · DELETE |
| 20 | [`.../MLLR`](#20-designsteelkds-41-30-2022mllr--modify-live-load-reduction-factor-活荷载折减系数修改) | Modify Live Load Reduction Factor（活荷载折减系数修改） | POST · GET · PUT · DELETE |
| 21 | [`.../MEMB`](#21-designsteelkds-41-30-2022memb--member-assignment-设计构件指定) | Member Assignment（设计构件指定） | GET · PUT · DELETE |

### 组 3. 材料

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 22 | [`.../SMODI`](#22-designsteelkds-41-30-2022smodi--modify-steel-material-钢材材质修改) | Modify Steel Material（钢材材质修改） | GET · PUT · DELETE |

### 组 4. 设计执行·结果（POST 专用）

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 23 | [`.../CODE-ANAL`](#23-designsteelkds-41-30-2022code-anal--steel-code-check-perform-钢结构规范校核执行) | Steel Code Check Perform（钢结构规范校核执行） | POST |
| 24 | [`.../CODE-TABLE`](#24-designsteelkds-41-30-2022code-table--steel-code-check-table-钢结构规范校核表) | Steel Code Check Table（钢结构规范校核表） | POST |
| 25 | [`.../CODE-REPORT`](#25-designsteelkds-41-30-2022code-report--steel-code-check-report-钢结构规范校核报告) | Steel Code Check Report（钢结构规范校核报告） | POST |
| 26 | [`.../DREULT`](#26-designsteelkds-41-30-2022dreult--steel-design-result-钢结构设计结果图像) | Steel Design Result（钢结构设计结果图像） | POST |
| 27 | [`.../TABLE`](#27-designsteelkds-41-30-2022table--steel-member-design-forces-钢构件设计内力) | Steel Member Design Forces（钢构件设计内力） | POST |

---

## 0. `DESIGN/STEEL/DSTL` — Design Code (钢结构设计代码选择)

> **功能：** 选择当前项目要采用的**钢结构设计代码**。与本章节其余27个
> 端点（`KDS-41-30-2022/<CODE>`）不同，其 URI 不使用 `KDS-41-30-2022` 前缀，
> 是独立的上层选择端点。

### Input URI

```
{base url}/DESIGN/STEEL/DSTL
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
                "KDS 41 30 : 2022"
              ]
            }
          }
        }
      }
    }
  }
}
```

> ⚠️ **原文 schema 笔误：** 原文中 `"maxProperties"` 被误写为 **`"maxroperties"`**
> （2026-09-06 确认，原文 `maxProperties` 0次 / `maxroperties` 1次）。结构相同的26章
> `DESIGN/RC/DRC` 则正确标为 `"maxProperties"`，故上方 schema 采用了正确写法。
> 属于可报错反馈对象。

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | Assign 包装（ID 字符串键，1个） | `"Assign"` | Object | — | **必填** |
| 2 | 钢结构设计代码 · 当前仅支持 `"KDS 41 30 : 2022"` 一个取值 | `"DGNCODE"` | String (enum) | — | **必填** |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022"
    }
  }
}
```

**GET Response Body**

```json
{
  "DSTL": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022"
    }
  }
}
```

> **参考：** GET 响应的最上层键与端点名相同，为 `"DSTL"`。承担同一职责的26章
> `DESIGN/RC/DRC` 其响应键却与端点名不同，为 `"DCON"`，二者规则不一，须注意。
> 此外24章 [`/db/DSTL`](./24_DB_Design.md#2-dbdstl--design-steel-code-钢结构设计代码) 名字
> 虽相同，但 URI·schema 均异，是另一个独立的旧（舊）命名空间端点。

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/DSTL"

# 选择钢结构设计代码（PUT）：KDS 41 30:2022
payload = {"Assign": {"1": {"DGNCODE": "KDS 41 30 : 2022"}}}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 1. `DESIGN/STEEL/KDS-41-30-2022/DCO` — Design Code Option (设计代码选项)

> **功能：** 设置钢结构设计标准（KDS 41 30:2022）以及侧向支撑·挠度校核·抗震特别规定·圆形截面组合比方法等全局设计选项。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/DCO
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
          "title": "Steel Design Code",
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
                "KDS 41 30 : 2022"
              ]
            },
            "LAT_BRACE": {
              "type": "boolean",
              "description": "All Beams/Girders are Laterally Braced",
              "default": false
            },
            "DEFL_CHK": {
              "type": "boolean",
              "description": "Check Beam/Column Deflection",
              "default": true
            },
            "SEISMIC": {
              "type": "boolean",
              "description": "Apply Special Provisions for Seismic Design",
              "default": false
            },
            "COMB_RATIO": {
              "type": "integer",
              "description": "Combined Ratio Method for Circular Section",
              "default": 0,
              "oneOf": [
                {
                  "title": "SRSS (Square root of sum of square)",
                  "const": 0
                },
                {
                  "title": "Linear Sum",
                  "const": 1
                }
              ]
            },
            "SEIS_SYS": {
              "type": "string",
              "description": "Seismic Load Resisting System",
              "enum": [
                "Special Moment Frames",
                "Intermediate Moment Frames",
                "Ordinary Moment Frames",
                "Special Concentrically Braced Frames",
                "Ordinary Concentrically Braced Frames",
                "Eccentrically Braced Frames",
                "Buckling-Restrained Braced Frames",
                "Special Plate Shear Walls"
              ],
              "default": "Special Moment Frames"
            },
            "COL_WEAK": {
              "type": "boolean",
              "description": "Consider strong column-weak beam on last floor",
              "default": true
            },
            "UNDGR_LD": {
              "type": "boolean",
              "description": "Use Under Ground Load Combination Type for Under Ground Members",
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装（ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 设计代码（固定为 KDS 41 30 : 2022） | `"DGNCODE"` | String (enum) | — | **必填** |
| 3 | 所有梁/主梁假设有侧向支撑 | `"LAT_BRACE"` | Boolean | `false` | 可选 |
| 4 | 梁/柱挠度校核 | `"DEFL_CHK"` | Boolean | `true` | 可选 |
| 5 | 应用抗震设计特别规定 | `"SEISMIC"` | Boolean | `false` | 可选 |
| 6 | 圆形截面组合比方法（0=SRSS，1=Linear Sum） | `"COMB_RATIO"` | Integer | `0` | 可选 |
| 7 | 抗震抗侧力体系（SEISMIC=true 时）— Special/Intermediate/Ordinary Moment Frames, Special/Ordinary Concentrically Braced Frames, Eccentrically Braced Frames, Buckling-Restrained Braced Frames, Special Plate Shear Walls | `"SEIS_SYS"` | String (enum) | `"Special Moment Frames"` | 条件必填 |
| 8 | 考虑最上层强柱弱梁 | `"COL_WEAK"` | Boolean | `true` | 可选 |
| 9 | 对地下构件使用地下荷载组合类型 | `"UNDGR_LD"` | Boolean | `true` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022",
      "LAT_BRACE": false,
      "DEFL_CHK": true,
      "SEISMIC": true,
      "COMB_RATIO": 1,
      "SEIS_SYS": "Special Moment Frames",
      "COL_WEAK": true,
      "UNDGR_LD": true
    }
  }
}
```

**GET Response Body**

```json
{
  "DCO": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022",
      "LAT_BRACE": false,
      "DEFL_CHK": true,
      "SEISMIC": true,
      "COMB_RATIO": 1,
      "UNDGR_LD": true,
      "SEIS_SYS": "Special Moment Frames",
      "COL_WEAK": true
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/DCO"

# 1) 设置（PUT）
payload = {
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 30 : 2022",
      "LAT_BRACE": false,
      "DEFL_CHK": true,
      "SEISMIC": true,
      "COMB_RATIO": 1,
      "SEIS_SYS": "Special Moment Frames",
      "COL_WEAK": true,
      "UNDGR_LD": true
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 删除（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 2. `DESIGN/STEEL/KDS-41-30-2022/DCTL` — Definition of Frame (框架定义)

> **功能：** 定义设计框架 X/Y 方向是否为有侧移（Sway/Non-sway）、有效屈曲长度系数是否自动计算、设计类型（3D/平面）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/DCTL
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装（仅允许1个 ID，maxProperties=1） | `"Assign"` | Object | — | **必填** |
| 2 | X方向框架（`"Unbraced Sway"`=无侧向支撑·Sway，`"Braced Non-sway"`=有侧向支撑·Non-sway） | `"FRAMEX"` | String (oneOf) | `"Braced Non-sway"` | 可选 |
| 3 | Y方向框架（取值与 FRAMEX 相同） | `"FRAMEY"` | String (oneOf) | `"Braced Non-sway"` | 可选 |
| 4 | 有效屈曲长度系数自动计算 | `"bAUTOKF"` | Boolean | `false` | 可选 |
| 5 | 设计类型（`"3D"`=3-D，`"XZ"`=X-Z平面，`"YZ"`=Y-Z平面，`"XY"`=X-Y平面） | `"DT"` | String (oneOf) | `"3D"` | 可选 |

### Request / Response JSON

**PUT Request Body**

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

**GET Response Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/DCTL"

# 1) 设置（PUT）
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
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 删除（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 3. `DESIGN/STEEL/KDS-41-30-2022/LLRF` — Live Load Reduction Factor (活荷载折减系数)

> **功能：** 设置按楼层、平面范围的活荷载折减系数表以及适用成分（轴力/弯矩/剪力）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LLRF
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
                      0.75,
                      0.7,
                      0.65,
                      0.6,
                      0.55,
                      0.5
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
                      0.75,
                      0.7,
                      0.65,
                      0.6,
                      0.55,
                      0.5
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 计算规则（0=by General Design Code，1=by Chinese Standard） | `"CALC_RULE"` | Integer | `0` | 可选 |
| 3 | 适用成分（`"ALL"`,`"AXIAL"`,`"MOMENTS"`,`"SHEAR"`） | `"APPLIED_COMP"` | Array[String] | `["AXIAL"]` | 可选 |
| 4 | 活荷载工况名称列表 | `"LIVE_LOAD_CASES"` | Array[String] | — | 可选 |
| 5 | 折减系数表数据 | `"REDUCTION_DATA"` | Array[Object] | — | **必填** |
| 5.1 | 楼层名称 | `"STORY"` | String | — | **必填** |
| 5.2 | X 最小坐标 | `"XMIN"` | Number | `0` | 可选 |
| 5.3 | X 最大坐标 | `"XMAX"` | Number | `0` | 可选 |
| 5.4 | Y 最小坐标 | `"YMIN"` | Number | `0` | 可选 |
| 5.5 | Y 最大坐标 | `"YMAX"` | Number | `0` | 可选 |
| 5.6 | Rmax（仅 General Design Code，enum 1~0.5） | `"RANGE_MAX"` | Number | `1` | 可选 |
| 5.7 | Rmin（仅 General Design Code，enum 1~0.5） | `"RANGE_MIN"` | Number | `0.5` | 可选 |

### Request / Response JSON

**PUT Request Body**

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

**GET Response Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LLRF"

# 1) 设置（PUT）
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
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 删除（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 4. `DESIGN/STEEL/KDS-41-30-2022/LCTB` — Load Contribution for Nonlinear Load Case (非线性荷载工况的荷载贡献)

> **功能：** 查询/删除针对非线性解析荷载工况的荷载贡献（Load Contribution）定义。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LCTB
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 荷载贡献名称 | `"NAME"` | String | — | **必填** |
| 3 | 说明 | `"DESC"` | String | `""` | 可选 |
| 4 | 荷载贡献项 | `"BASE_ITEM"` | Array[Object] | — | **必填** |
| 4.1 | 系数 | `"FACTOR"` | Number | — | **必填** |
| 4.2 | 荷载工况名称 | `"LOAD_CASE_NAME"` | String | — | **必填** |

### Request / Response JSON

**GET Response Body**（LCTB 仅支持查询·删除）

```json
{
  "LCTB": {
    "2": {
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
    "3": {
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
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LCTB"

# LCTB 仅支持 GET / DELETE（查询与删除）
res = requests.get(URI, headers=HEADERS)
print("GET:", res.status_code, res.json())

# 全部删除
# requests.delete(URI, headers=HEADERS)
```

---

## 5. `DESIGN/STEEL/KDS-41-30-2022/SRDF` — Strength Reduction Factors (强度折减系数 φ)

> **功能：** 设置受拉/受压/受弯/受剪的强度折减系数（φ）取值。φ_t2（净截面剪断）固定为 0.75（read-only）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SRDF
```

### Active Methods

`GET` · `DELETE` · `PUT`

### JSON Schema

```json
{
  "type": "object",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "description": "Strength Reduction Factors settings (shared structure: T_DSTL_D). Supported methods: GET, PUT. Checklist Text (view-only).",
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\"), where each entry represents an element.",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "PHI_T1": {
              "type": "number",
              "description": "For Yielding in Gross Section (phi_t1)",
              "default": 0.9
            },
            "PHI_T2": {
              "type": "number",
              "description": "For Fracture in Net Section (phi_t2) - read-only fixed value",
              "const": 0.75,
              "default": 0.75,
              "readOnly": true
            },
            "PHI_C": {
              "type": "number",
              "description": "For Compression Members (phi_c)",
              "default": 0.9
            },
            "PHI_B": {
              "type": "number",
              "description": "For Flexural Members (phi_b)",
              "default": 0.9
            },
            "PHI_V": {
              "type": "number",
              "description": "For Shear (phi_v)",
              "default": 0.9
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
|-----|------|-----|------|--------|------|
| 1 | Assign 包装（仅允许1个 ID，maxProperties=1） | `"Assign"` | Object | — | **必填** |
| 2 | 毛截面屈服（φ_t1） | `"PHI_T1"` | Number | `0.9` | 可选 |
| 3 | 净截面断裂（φ_t2）— 固定为 0.75 read-only | `"PHI_T2"` | Number (const 0.75) | `0.75` | 可选 |
| 4 | 受压构件（φ_c） | `"PHI_C"` | Number | `0.9` | 可选 |
| 5 | 受弯构件（φ_b） | `"PHI_B"` | Number | `0.9` | 可选 |
| 6 | 受剪（φ_v） | `"PHI_V"` | Number | `0.9` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "PHI_T1": 0.75,
      "PHI_T2": 0.75,
      "PHI_C": 0.25,
      "PHI_B": 0.45,
      "PHI_V": 0.85
    }
  }
}
```

**GET Response Body**

```json
{
  "SRDF": {
    "1": {
      "PHI_T1": 0.75,
      "PHI_T2": 0.75,
      "PHI_C": 0.25,
      "PHI_B": 0.45,
      "PHI_V": 0.85
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SRDF"

# 1) 设置（PUT）
payload = {
  "Assign": {
    "1": {
      "PHI_T1": 0.75,
      "PHI_T2": 0.75,
      "PHI_C": 0.25,
      "PHI_B": 0.45,
      "PHI_V": 0.85
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 删除（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 6. `DESIGN/STEEL/KDS-41-30-2022/SERV` — Serviceability Parameters (使用性参数)

> **功能：** 设置各构件的挠度控制值（Deflection Control）与挠度放大系数（DAF）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SERV
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
            "DEFLECT_CONTROL": {
              "type": "number",
              "description": "Deflection Control",
              "default": 300
            },
            "DAF": {
              "type": "number",
              "description": "Deflection Amplification Factor",
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 挠度控制值（span/n） | `"DEFLECT_CONTROL"` | Number | `300` | 可选 |
| 3 | 挠度放大系数 | `"DAF"` | Number | `1` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "DEFLECT_CONTROL": 400,
      "DAF": 2
    },
    "934": {
      "DAF": 2
    },
    "1057": {
      "DEFLECT_CONTROL": 500
    }
  }
}
```

**GET Response Body**

```json
{
  "SERV": {
    "915": {
      "DEFLECT_CONTROL": 400,
      "DAF": 2
    },
    "934": {
      "DAF": 2
    },
    "1057": {
      "DEFLECT_CONTROL": 500
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SERV"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "915": {
      "DEFLECT_CONTROL": 400,
      "DAF": 2
    },
    "934": {
      "DAF": 2
    },
    "1057": {
      "DEFLECT_CONTROL": 500
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 7. `DESIGN/STEEL/KDS-41-30-2022/EQCT` — Seismic Load Combination Type (地震作用组合类型)

> **功能：** 按构件指定采用特别地震作用（Special Seismic Loads）还是竖向地震力（Vertical Seismic Forces）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/EQCT
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 构件类型（`"Special Seismic Loads"`, `"Vertical Seismic Forces"`） | `"TYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

**GET Response Body**

```json
{
  "EQCT": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/EQCT"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 8. `DESIGN/STEEL/KDS-41-30-2022/ULCT` — Underground Load Combination Type (地下荷载组合类型)

> **功能：** 按构件指定是否应用地下荷载组合（Underground Loads）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/ULCT
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
  "description": "Underground Load Combination settings. Checklist Text (view-only).",
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
            "bUNDERLOADTYPE": {
              "type": "boolean",
              "description": "Assign Member: true for Underground Loads, false for None-underground Loads",
              "oneOf": [
                {
                  "title": "For Underground Loads",
                  "const": true
                },
                {
                  "title": "For None-underground Loads",
                  "const": false
                }
              ],
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 地下荷载类型（`true`=用于地下荷载，`false`=用于非地下荷载） | `"bUNDERLOADTYPE"` | Boolean (oneOf) | `false` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "885": {
      "bUNDERLOADTYPE": true
    },
    "888": {
      "bUNDERLOADTYPE": false
    }
  }
}
```

**GET Response Body**

```json
{
  "ULCT": {
    "885": {
      "bUNDERLOADTYPE": true
    },
    "888": {
      "bUNDERLOADTYPE": false
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/ULCT"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "885": {
      "bUNDERLOADTYPE": true
    },
    "888": {
      "bUNDERLOADTYPE": false
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 9. `DESIGN/STEEL/KDS-41-30-2022/SUEQ` — Scale up Factor for Earthquake (地震放大系数)

> **功能：** 按构件设置荷载工况/荷载组合的轴力·弯矩·剪力地震放大系数。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SUEQ
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 荷载工况 - 轴力放大系数 | `"LC_AXIAL"` | Number | `1` | 可选 |
| 3 | 荷载工况 - 弯矩放大系数 | `"LC_MOMENT"` | Number | `1` | 可选 |
| 4 | 荷载工况 - 剪力放大系数 | `"LC_SHEAR"` | Number | `1` | 可选 |
| 5 | 荷载组合 - 轴力放大系数 | `"LCOM_AXIAL"` | Number | `1` | 可选 |
| 6 | 荷载组合 - 弯矩放大系数 | `"LCOM_MOMENT"` | Number | `1` | 可选 |
| 7 | 荷载组合 - 剪力放大系数 | `"LCOM_SHEAR"` | Number | `1` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "934": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
```

**GET Response Body**

```json
{
  "SUEQ": {
    "915": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "934": {
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SUEQ"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "915": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "934": {
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 10. `DESIGN/STEEL/KDS-41-30-2022/CRCM` — Combined Ratio Calculation Method for Circular Section (圆形截面组合比计算法)

> **功能：** 按构件设置圆形（管形）截面的组合强度计算方法（SRSS / Linear Sum）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CRCM
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
          "title": "Combined Strength Method",
          "type": "object",
          "required": [
            "METHOD"
          ],
          "additionalProperties": false,
          "properties": {
            "METHOD": {
              "type": "string",
              "description": "Combined Strength Method",
              "oneOf": [
                {
                  "title": "SRSS",
                  "const": "SRSS"
                },
                {
                  "title": "Linear Sum",
                  "const": "Linear Sum"
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 组合强度方法（`"SRSS"`, `"Linear Sum"`） | `"METHOD"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1058": {
      "METHOD": "Linear Sum"
    },
    "1059": {
      "METHOD": "SRSS"
    }
  }
}
```

**GET Response Body**

```json
{
  "CRCM": {
    "1058": {
      "METHOD": "Linear Sum"
    },
    "1059": {
      "METHOD": "SRSS"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CRCM"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "1058": {
      "METHOD": "Linear Sum"
    },
    "1059": {
      "METHOD": "SRSS"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 11. `DESIGN/STEEL/KDS-41-30-2022/HCBM` — Haunched Beam Assignment (加腋梁指定)

> **功能：** 将要素分组为 Part A/B/C，定义加腋梁（Haunched Beam）设计构件。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/HCBM
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
          "required": [
            "NAME",
            "PART_A",
            "PART_B",
            "PART_C",
            "POS_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "NAME": {
              "type": "string",
              "description": "Haunch Name"
            },
            "PART_A": {
              "type": "object",
              "description": "Element No. Input for Part A (Use only one method)",
              "additionalProperties": false,
              "required": [
                "INPUT_METHOD"
              ],
              "properties": {
                "INPUT_METHOD": {
                  "type": "string",
                  "description": "Select input method for Part A",
                  "oneOf": [
                    {
                      "title": "Specify each Element ID",
                      "const": "KEYS"
                    },
                    {
                      "title": "Specify ID range",
                      "const": "TO"
                    }
                  ]
                },
                "KEYS": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  },
                  "minItems": 1,
                  "description": "Specify each Element ID"
                },
                "TO": {
                  "type": "string",
                  "description": "Specify ID range (e.g. \"101 to 105\")"
                }
              }
            },
            "PART_B": {
              "type": "object",
              "description": "Element No. Input for Part B (Use only one method)",
              "additionalProperties": false,
              "required": [
                "INPUT_METHOD"
              ],
              "properties": {
                "INPUT_METHOD": {
                  "type": "string",
                  "description": "Select input method for Part B",
                  "oneOf": [
                    {
                      "title": "Specify each Element ID",
                      "const": "KEYS"
                    },
                    {
                      "title": "Specify ID range",
                      "const": "TO"
                    }
                  ]
                },
                "KEYS": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  },
                  "minItems": 1,
                  "description": "Specify each Element ID"
                },
                "TO": {
                  "type": "string",
                  "description": "Specify ID range (e.g. \"101 to 105\")"
                }
              }
            },
            "PART_C": {
              "type": "object",
              "description": "Element No. Input for Part C (Use only one method)",
              "additionalProperties": false,
              "required": [
                "INPUT_METHOD"
              ],
              "properties": {
                "INPUT_METHOD": {
                  "type": "string",
                  "description": "Select input method for Part C",
                  "oneOf": [
                    {
                      "title": "Specify each Element ID",
                      "const": "KEYS"
                    },
                    {
                      "title": "Specify ID range",
                      "const": "TO"
                    }
                  ]
                },
                "KEYS": {
                  "type": "array",
                  "items": {
                    "type": "integer"
                  },
                  "minItems": 1,
                  "description": "Specify each Element ID"
                },
                "TO": {
                  "type": "string",
                  "description": "Specify ID range (e.g. \"101 to 105\")"
                }
              }
            },
            "POS_TYPE": {
              "type": "integer",
              "description": "Design Position Type",
              "oneOf": [
                {
                  "title": "Part 1/2",
                  "const": 0
                },
                {
                  "title": "User",
                  "const": 1
                }
              ]
            },
            "L1": {
              "type": "number",
              "description": "User defined L1 distance",
              "default": 1
            },
            "L2": {
              "type": "number",
              "description": "User defined L2 distance",
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 加腋名称 | `"NAME"` | String | — | **必填** |
| 3 | Part A 要素输入（仅使用1种方法） | `"PART_A"` | Object | — | **必填** |
| 3.1 | 输入方式（`"KEYS"`=个别 ID，`"TO"`=范围） | `"INPUT_METHOD"` | String (oneOf) | — | **必填** |
| 3.2 | 个别要素 ID（INPUT_METHOD=KEYS，minItems 1） | `"KEYS"` | Array[Integer] | — | 条件必填 |
| 3.3 | ID 范围字符串（INPUT_METHOD=TO，例 `"101 to 105"`） | `"TO"` | String | — | 条件必填 |
| 4 | Part B 要素输入（结构与 PART_A 相同） | `"PART_B"` | Object | — | **必填** |
| 5 | Part C 要素输入（结构与 PART_A 相同） | `"PART_C"` | Object | — | **必填** |
| 6 | 设计位置类型（0=Part 1/2，1=User） | `"POS_TYPE"` | Integer (oneOf) | — | **必填** |
| 7 | 用户自定义 L1 距离（POS_TYPE=1） | `"L1"` | Number | `1` | 可选 |
| 8 | 用户自定义 L2 距离（POS_TYPE=1） | `"L2"` | Number | `1` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "NAME": "h1",
      "POS_TYPE": 0,
      "L1": 0.5,
      "L2": 0.5,
      "PART_A": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1065
        ]
      },
      "PART_B": {
        "INPUT_METHOD": "TO",
        "TO": "1066to1071"
      },
      "PART_C": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1072
        ]
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "HCBM": {
    "1": {
      "NAME": "h1",
      "PART_A": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1065
        ]
      },
      "PART_B": {
        "INPUT_METHOD": "TO",
        "TO": "1066to1071"
      },
      "PART_C": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1072
        ]
      },
      "POS_TYPE": 0,
      "L1": 0.5,
      "L2": 0.5
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/HCBM"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "1": {
      "NAME": "h1",
      "POS_TYPE": 0,
      "L1": 0.5,
      "L2": 0.5,
      "PART_A": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1065
        ]
      },
      "PART_B": {
        "INPUT_METHOD": "TO",
        "TO": "1066to1071"
      },
      "PART_C": {
        "INPUT_METHOD": "KEYS",
        "KEYS": [
          1072
        ]
      }
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 12. `DESIGN/STEEL/KDS-41-30-2022/LENG` — Unbraced Length (未支撑长度 L, Lb)

> **功能：** 设置各构件的未支撑长度（Ly, Lz）、侧向未支撑长度（Lb）、扭转未支撑长度（Lt）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LENG
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 未支撑长度 Ly | `"LY"` | Number | `0` | 可选 |
| 3 | 未支撑长度 Lz | `"LZ"` | Number | `0` | 可选 |
| 4 | 侧向未支撑长度 Lb | `"LB"` | Number | `0` | 可选 |
| 5 | 不考虑侧向未支撑长度 | `"bNOTUSE"` | Boolean | `false` | 可选 |
| 6 | 扭转未支撑长度 Lt | `"LT"` | Number | `0` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 1,
      "bNOTUSE": true,
      "LT": 1
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
```

**GET Response Body**

```json
{
  "LENG": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 1,
      "bNOTUSE": true,
      "LT": 1
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LENG"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "888": {
      "LY": 1,
      "LZ": 1,
      "LB": 1,
      "bNOTUSE": true,
      "LT": 1
    },
    "891": {
      "LY": 1,
      "LZ": 1,
      "LB": 2
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 13. `DESIGN/STEEL/KDS-41-30-2022/KFAC` — Effective Length Factor (有效屈曲长度系数 K)

> **功能：** 设置各构件的有效屈曲长度系数 Ky, Kz, Kt。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/KFAC
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 有效屈曲长度系数 Ky | `"Ky"` | Number | `1` | 可选 |
| 3 | 有效屈曲长度系数 Kz | `"Kz"` | Number | `1` | 可选 |
| 4 | 有效屈曲长度系数 Kt | `"Kt"` | Number | `1` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "859": {
      "Ky": 1
    },
    "860": {
      "Ky": 2,
      "Kz": 2
    },
    "902": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

**GET Response Body**

```json
{
  "KFAC": {
    "859": {
      "Ky": 1
    },
    "860": {
      "Ky": 2,
      "Kz": 2
    },
    "902": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/KFAC"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "859": {
      "Ky": 1
    },
    "860": {
      "Ky": 2,
      "Kz": 2
    },
    "902": {
      "Kz": 3,
      "Kt": 3
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 14. `DESIGN/STEEL/KDS-41-30-2022/LTSR` — Limiting Slenderness Ratio (长细比限制)

> **功能：** 设置各构件的受压/受拉长细比限制值。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/LTSR
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 不校核长细比 | `"bNOTCHECK"` | Boolean | `false` | 可选 |
| 3 | 受压长细比限制 | `"COMP"` | Number | — | **必填** |
| 4 | 受拉长细比限制 | `"TENS"` | Number | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1067": {
      "COMP": 300,
      "TENS": 200
    },
    "1068": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

**GET Response Body**

```json
{
  "LTSR": {
    "1067": {
      "COMP": 300,
      "TENS": 200
    },
    "1068": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/LTSR"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "1067": {
      "COMP": 300,
      "TENS": 200
    },
    "1068": {
      "COMP": 300,
      "TENS": 200
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 15. `DESIGN/STEEL/KDS-41-30-2022/CMFT` — Equivalent Moment Correction Factor (等效弯矩修正系数 Cm)

> **功能：** 以自动计算或用户取值方式设置各构件的等效弯矩修正系数 CMy、CMz。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CMFT
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 自动计算 | `"OPT_AUTO"` | Boolean | `false` | 可选 |
| 3 | CMy | `"CMY"` | Number | `0` | 可选 |
| 4 | CMz | `"CMZ"` | Number | `0` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1067": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    }
  }
}
```

**GET Response Body**

```json
{
  "CMFT": {
    "1067": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CMFT"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "1067": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 16. `DESIGN/STEEL/KDS-41-30-2022/FMAG` — Moment Magnifier (弯矩放大系数 B1/Δb, B2/Δs)

> **功能：** 设置各构件的一次/二次弯矩放大系数（B1y·B1z, B2y·B2z）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/FMAG
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | B1y - Δby（一次弯矩 Y） | `"B1Y_DELTA_BY"` | Number | `1` | 可选 |
| 3 | B1z - Δbz（一次弯矩 Z） | `"B1Z_DELTA_BZ"` | Number | `1` | 可选 |
| 4 | B2y - Δsy（二次弯矩 Y） | `"B2Y_DELTA_SY"` | Number | `1` | 可选 |
| 5 | B2z - Δsz（二次弯矩 Z） | `"B2Z_DELTA_SZ"` | Number | `1` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "1058": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    }
  }
}
```

**GET Response Body**

```json
{
  "FMAG": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1,
      "B2Z_DELTA_SZ": 1
    },
    "1058": {
      "B1Y_DELTA_BY": 1,
      "B1Z_DELTA_BZ": 1,
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/FMAG"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "915": {
      "B1Y_DELTA_BY": 1.1,
      "B1Z_DELTA_BZ": 1.2
    },
    "1058": {
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1.4
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 17. `DESIGN/STEEL/KDS-41-30-2022/CBFT` — Bending Coefficient (弯曲系数 Cb)

> **功能：** 以自动计算或用户取值方式设置各构件的侧向屈曲弯曲系数 Cb。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CBFT
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
            "AUTO_CAL": {
              "type": "boolean",
              "description": "Auto Calculate by Program",
              "default": false
            },
            "VALUE": {
              "type": "number",
              "description": "Bending Coefficient (Cb) Value",
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 程序自动计算 | `"AUTO_CAL"` | Boolean | `false` | 可选 |
| 3 | 弯曲系数 Cb 取值（AUTO_CAL=false 时） | `"VALUE"` | Number | `1` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "AUTO_CAL": true
    },
    "1058": {
      "AUTO_CAL": false,
      "VALUE": 1.2
    },
    "1059": {
      "AUTO_CAL": false,
      "VALUE": 1.25
    }
  }
}
```

**GET Response Body**

```json
{
  "CBFT": {
    "915": {
      "AUTO_CAL": true
    },
    "1058": {
      "AUTO_CAL": false,
      "VALUE": 1.2
    },
    "1059": {
      "AUTO_CAL": false,
      "VALUE": 1.25
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CBFT"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "915": {
      "AUTO_CAL": true
    },
    "1058": {
      "AUTO_CAL": false,
      "VALUE": 1.2
    },
    "1059": {
      "AUTO_CAL": false,
      "VALUE": 1.25
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 18. `DESIGN/STEEL/KDS-41-30-2022/MBTP` — Modify Member Type (构件类型修改)

> **功能：** 更改要素的设计构件类型（Column/Beam/Brace）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/MBTP
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 构件类型（`"COLUMN"`, `"BEAM"`, `"BRACE"`） | `"TYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
```

**GET Response Body**

```json
{
  "MBTP": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/MBTP"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1066": {
      "TYPE": "BEAM"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 19. `DESIGN/STEEL/KDS-41-30-2022/SLRS` — Seismic Load Resisting System by Member (按构件抗震抗侧力体系)

> **功能：** 设置各构件的抗震抗侧力框架类型（中心支撑框架/偏心支撑框架/屈曲约束支撑/特种钢板剪力墙）与校核选项。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SLRS
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
            "FRAME_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "FRAME_TYPE": {
              "type": "string",
              "description": "Seismic Load Resisting System Frame Type",
              "oneOf": [
                {
                  "title": "Special Concentrically Braced Frames",
                  "const": "Special Concentrically Braced Frames"
                },
                {
                  "title": "Ordinary Concentrically Braced Frames",
                  "const": "Ordinary Concentrically Braced Frames"
                },
                {
                  "title": "Eccentrically Braced Frames",
                  "const": "Eccentrically Braced Frames"
                },
                {
                  "title": "Buckling Restrained Braced Frames",
                  "const": "Buckling Restrained Braced Frames"
                },
                {
                  "title": "Special Plate Shear Walls",
                  "const": "Special Plate Shear Walls"
                }
              ]
            },
            "CHECK_OPTION": {
              "type": "boolean",
              "description": "Check for Brace Slenderness Ratio / Check for Links (not supported for Buckling-Restrained Braced Frames and Special Plate Shear Walls)",
              "default": true
            }
          },
          "allOf": [
            {
              "if": {
                "properties": {
                  "FRAME_TYPE": {
                    "enum": [
                      "Buckling Restrained Braced Frames",
                      "Special Plate Shear Walls"
                    ]
                  }
                },
                "required": [
                  "FRAME_TYPE"
                ]
              },
              "then": {
                "properties": {
                  "CHECK_OPTION": {
                    "const": false
                  }
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 抗震抗侧力体系框架类型（`"Special Concentrically Braced Frames"`, `"Ordinary Concentrically Braced Frames"`, `"Eccentrically Braced Frames"`, `"Buckling Restrained Braced Frames"`, `"Special Plate Shear Walls"`） | `"FRAME_TYPE"` | String (oneOf) | — | **必填** |
| 3 | 支撑长细比校核 / 链接件（Link）校核（Buckling Restrained·Special Plate Shear Walls 不支持 → 强制为 false） | `"CHECK_OPTION"` | Boolean | `true` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "FRAME_TYPE": "Special Concentrically Braced Frames",
      "CHECK_OPTION": true
    },
    "934": {
      "FRAME_TYPE": "Ordinary Concentrically Braced Frames",
      "CHECK_OPTION": false
    },
    "1058": {
      "FRAME_TYPE": "Buckling Restrained Braced Frames"
    }
  }
}
```

**GET Response Body**

```json
{
  "SLRS": {
    "915": {
      "FRAME_TYPE": "Special Concentrically Braced Frames",
      "CHECK_OPTION": true
    },
    "934": {
      "FRAME_TYPE": "Ordinary Concentrically Braced Frames",
      "CHECK_OPTION": false
    },
    "1058": {
      "FRAME_TYPE": "Buckling Restrained Braced Frames"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SLRS"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "915": {
      "FRAME_TYPE": "Special Concentrically Braced Frames",
      "CHECK_OPTION": true
    },
    "934": {
      "FRAME_TYPE": "Ordinary Concentrically Braced Frames",
      "CHECK_OPTION": false
    },
    "1058": {
      "FRAME_TYPE": "Buckling Restrained Braced Frames"
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 20. `DESIGN/STEEL/KDS-41-30-2022/MLLR` — Modify Live Load Reduction Factor (活荷载折减系数修改)

> **功能：** 逐构件单独修改活荷载折减系数（0.3~1.0）与适用成分（轴力/弯矩/剪力）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/MLLR
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 折减系数（范围 0.3 ~ 1.0） | `"FACTOR"` | Number | `1` | 可选 |
| 3 | 适用成分 | `"COMPONENTS"` | Object | — | 可选 |
| 3.1 | 轴力 | `"AXIAL"` | Boolean | `false` | 可选 |
| 3.2 | 弯矩 | `"MOMENT"` | Boolean | `false` | 可选 |
| 3.3 | 剪力 | `"SHEAR"` | Boolean | `false` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "922": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "934": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "MLLR": {
    "922": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "934": {
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/MLLR"

# 1) 生成/设置（POST）
payload = {
  "Assign": {
    "922": {
      "COMPONENTS": {
        "AXIAL": false,
        "MOMENT": true,
        "SHEAR": false
      }
    },
    "934": {
      "FACTOR": 0.9,
      "COMPONENTS": {
        "AXIAL": true,
        "SHEAR": false
      }
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code, res.json())

# 2) 查询（GET）/ 修改（PUT）/ 删除（DELETE）
print("GET:", requests.get(URI, headers=HEADERS).json())
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 21. `DESIGN/STEEL/KDS-41-30-2022/MEMB` — Member Assignment (设计构件指定)

> **功能：** 为设计构件 ID 指定要素列表，并指定局部方向是否反转。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/MEMB
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装 | `"Assign"` | Object | — | **必填** |
| 2 | 要素列表 | `"AELEM"` | Array[Integer] | — | **必填** |
| 3 | 局部方向反转 | `"bREVERSE"` | Boolean | `false` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        933,
        934
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        906,
        891
      ],
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
      "AELEM": [
        933,
        934
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        906,
        891
      ],
      "bREVERSE": true
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/MEMB"

# 1) 设置（PUT）
payload = {
  "Assign": {
    "1": {
      "AELEM": [
        933,
        934
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        906,
        891
      ],
      "bREVERSE": true
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 删除（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 22. `DESIGN/STEEL/KDS-41-30-2022/SMODI` — Modify Steel Material (钢材材质修改)

> **功能：** 按材质 ID 将钢材材质修改为基于标准代码（KS22(S)）或用户自定义（None）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/SMODI
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
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
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
                {
                  "const": "SS550",
                  "title": "SS550"
                },
                {
                  "const": "SM275",
                  "title": "SM275"
                },
                {
                  "const": "SM355",
                  "title": "SM355"
                },
                {
                  "const": "SM420",
                  "title": "SM420"
                },
                {
                  "const": "SM460",
                  "title": "SM460"
                },
                {
                  "const": "SM275TMC",
                  "title": "SM275TMC"
                },
                {
                  "const": "SM355TMC",
                  "title": "SM355TMC"
                },
                {
                  "const": "SM420TMC",
                  "title": "SM420TMC"
                },
                {
                  "const": "SM460TMC",
                  "title": "SM460TMC"
                },
                {
                  "const": "SMA275A",
                  "title": "SMA275A"
                },
                {
                  "const": "SMA275B",
                  "title": "SMA275B"
                },
                {
                  "const": "SMA275C",
                  "title": "SMA275C"
                },
                {
                  "const": "SMA355A",
                  "title": "SMA355A"
                },
                {
                  "const": "SMA355B",
                  "title": "SMA355B"
                },
                {
                  "const": "SMA355C",
                  "title": "SMA355C"
                },
                {
                  "const": "SMA460",
                  "title": "SMA460"
                },
                {
                  "const": "HSM500",
                  "title": "HSM500"
                },
                {
                  "const": "SN275A",
                  "title": "SN275A"
                },
                {
                  "const": "SN275B",
                  "title": "SN275B"
                },
                {
                  "const": "SN275C",
                  "title": "SN275C"
                },
                {
                  "const": "SN355",
                  "title": "SN355"
                },
                {
                  "const": "SN460",
                  "title": "SN460"
                },
                {
                  "const": "SHN275",
                  "title": "SHN275"
                },
                {
                  "const": "SHN355",
                  "title": "SHN355"
                },
                {
                  "const": "SHN420",
                  "title": "SHN420"
                },
                {
                  "const": "SHN460",
                  "title": "SHN460"
                },
                {
                  "const": "HSB380",
                  "title": "HSB380"
                },
                {
                  "const": "HSB460",
                  "title": "HSB460"
                },
                {
                  "const": "HSB690",
                  "title": "HSB690"
                },
                {
                  "const": "HSA650",
                  "title": "HSA650"
                },
                {
                  "const": "SGT275",
                  "title": "SGT275"
                },
                {
                  "const": "SGT355",
                  "title": "SGT355"
                },
                {
                  "const": "SGT410",
                  "title": "SGT410"
                },
                {
                  "const": "SGT450",
                  "title": "SGT450"
                },
                {
                  "const": "SGT550",
                  "title": "SGT550"
                },
                {
                  "const": "SRT275",
                  "title": "SRT275"
                },
                {
                  "const": "SRT355",
                  "title": "SRT355"
                },
                {
                  "const": "SRT410",
                  "title": "SRT410"
                },
                {
                  "const": "SRT450",
                  "title": "SRT450"
                },
                {
                  "const": "SRT550",
                  "title": "SRT550"
                },
                {
                  "const": "SNT275",
                  "title": "SNT275"
                },
                {
                  "const": "SNT355",
                  "title": "SNT355"
                },
                {
                  "const": "SNT460",
                  "title": "SNT460"
                },
                {
                  "const": "SHT410",
                  "title": "SHT410"
                },
                {
                  "const": "SHT460",
                  "title": "SHT460"
                },
                {
                  "const": "SNRT295E",
                  "title": "SNRT295E"
                },
                {
                  "const": "SNRT390E",
                  "title": "SNRT390E"
                },
                {
                  "const": "SNRT275A",
                  "title": "SNRT275A"
                },
                {
                  "const": "SNRT355A",
                  "title": "SNRT355A"
                },
                {
                  "const": "SSC275",
                  "title": "SSC275"
                },
                {
                  "const": "SWH275",
                  "title": "SWH275"
                },
                {
                  "const": "SWH355",
                  "title": "SWH355"
                },
                {
                  "const": "SWH420",
                  "title": "SWH420"
                },
                {
                  "const": "SWH460",
                  "title": "SWH460"
                },
                {
                  "const": "SF490",
                  "title": "SF490"
                },
                {
                  "const": "SF540",
                  "title": "SF540"
                },
                {
                  "const": "SDP1",
                  "title": "SDP1"
                },
                {
                  "const": "SDP2",
                  "title": "SDP2"
                },
                {
                  "const": "SDP3",
                  "title": "SDP3"
                },
                {
                  "const": "SWPC1",
                  "title": "SWPC1"
                },
                {
                  "const": "SWPD1",
                  "title": "SWPD1"
                },
                {
                  "const": "SWPC",
                  "title": "SWPC"
                },
                {
                  "const": "SWPD",
                  "title": "SWPD"
                }
              ]
            },
            "NAME": {
              "type": "string",
              "description": "User-defined steel material name when CODE is None."
            },
            "ES": {
              "type": "number",
              "description": "Modulus of Elasticity (Es). When CODE is None, user input is required. When CODE is Standard, this value is auto-filled from the selected standard code and grade and should be treated as read-only in UI."
            },
            "PS": {
              "type": "number",
              "description": "Poisson's Ratio (Ps). When CODE is None, user input is required. When CODE is Standard, this value is auto-filled from the selected standard code and grade and should be treated as read-only in UI."
            },
            "FU": {
              "type": "number",
              "description": "Tensile Strength (Fu). When CODE is None, user input is required. When CODE is Standard, this value is auto-filled from the selected standard code and grade and should be treated as read-only in UI."
            },
            "FY": {
              "type": "number",
              "description": "Yield Strength (Fy) for CODE=None. Required when CODE is None."
            },
            "FY1": {
              "type": "number",
              "description": "Yield Strength (Fy1). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY2": {
              "type": "number",
              "description": "Yield Strength (Fy2). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY3": {
              "type": "number",
              "description": "Yield Strength (Fy3). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY4": {
              "type": "number",
              "description": "Yield Strength (Fy4). Auto-filled from the selected standard code and grade when CODE is Standard."
            },
            "FY5": {
              "type": "number",
              "description": "Yield Strength (Fy5). Auto-filled from the selected standard code and grade when CODE is Standard."
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
                  "PS",
                  "FU"
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
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装（材质 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 材质代码类型（`"None"`=用户自定义，`"Standard"`=标准代码） | `"CODE"` | String (oneOf) | — | **必填** |
| 3 | 标准代码（CODE=Standard，目前仅支持 `"KS22(S)"`） | `"STANDARD_CODE"` | String (oneOf) | — | 条件必填 |
| 4 | 钢级 Grade（CODE=Standard）— SS235/SS275/…/SM355/…/SN460/SHN460/HSB690/HSA650/… 等 KS22(S) 共68种 | `"GRADE"` | String (oneOf) | — | 条件必填 |
| 5 | 用户自定义材质名（CODE=None） | `"NAME"` | String | — | 条件必填 |
| 6 | 屈服强度 Fy（CODE=None） | `"FY"` | Number | — | 条件必填 |
| 7 | 弹性模量 Es（CODE=None 时输入 / Standard 自动填入） | `"ES"` | Number | — | 条件必填 |
| 8 | 泊松比 Ps（CODE=None 时输入 / Standard 自动填入） | `"PS"` | Number | — | 条件必填 |
| 9 | 抗拉强度 Fu（CODE=None 时输入 / Standard 自动填入） | `"FU"` | Number | — | 条件必填 |
| 10 | 屈服强度 Fy1（CODE=Standard 自动填入） | `"FY1"` | Number | — | 可选 |
| 11 | 屈服强度 Fy2（CODE=Standard 自动填入） | `"FY2"` | Number | — | 可选 |
| 12 | 屈服强度 Fy3（CODE=Standard 自动填入） | `"FY3"` | Number | — | 可选 |
| 13 | 屈服强度 Fy4（CODE=Standard 自动填入） | `"FY4"` | Number | — | 可选 |
| 14 | 屈服强度 Fy5（CODE=Standard 自动填入） | `"FY5"` | Number | — | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "100": {
      "CODE": "Standard",
      "STANDARD_CODE": "KS22(S)",
      "GRADE": "SM355"
    },
    "101": {
      "CODE": "None",
      "ES": 40000000,
      "PS": 0,
      "FU": 0,
      "NAME": "test",
      "FY": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "SMODI": {
    "100": {
      "CODE": "Standard",
      "STANDARD_CODE": "KS22(S)",
      "GRADE": "SM355"
    },
    "101": {
      "CODE": "None",
      "ES": 40000000,
      "PS": 0,
      "FU": 0,
      "NAME": "test",
      "FY": 0
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/SMODI"

# 1) 设置（PUT）
payload = {
  "Assign": {
    "100": {
      "CODE": "Standard",
      "STANDARD_CODE": "KS22(S)",
      "GRADE": "SM355"
    },
    "101": {
      "CODE": "None",
      "ES": 40000000,
      "PS": 0,
      "FU": 0,
      "NAME": "test",
      "FY": 0
    }
  }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 删除（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 23. `DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL` — Steel Code Check Perform (钢结构规范校核执行)

> **功能：** 针对整体/按要素/按截面对象执行钢结构规范校核（设计计算）。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL
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
          "description": "Select target type for design calculation.",
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 执行对象类型（`"ALL"`=全部要素, `"ELEMS"`=按要素, `"SECTIONS"`=按截面） | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 可选 |
| 3 | 要素输入（ELEMS/SECTIONS 二者择一） | `"ELEMS"` | Object | — | 条件必填 |
| 3.1 | 个别 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 3.2 | ID 范围（例 `"1to160"`） | `"TO"` | String | — | 可选 |
| 3.3 | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |
| 4 | 截面编号（ELEMS/SECTIONS 二者择一） | `"SECTIONS"` | Array[Integer] | — | 条件必填 |

> `Argument` 必须**恰好只含** `"ELEMS"` 与 `"SECTIONS"` 之一（oneOf），且 `ELEMS` 内部只能从 `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 中选用一种。若 `PERFORM_TYPE="ALL"`，则无需指定对象，对全部对象执行。
>
> ⚠️ 2026-08-26 确认（article id `57389469766681`）：官方 JSON Schema 在最上层 `Argument` 中
> 明确要求必须含有 `"ELEMS"` 或 `"SECTIONS"` 之一（`oneOf`），但官方
> Request 示例却是 `{"Argument": {"PERFORM_TYPE": "ALL"}}` 这种两者皆省略的形态（原文
> 自身的 schema 与示例不一致）。鉴于判断示例反映的是实际行为，故 `PERFORM_TYPE="ALL"` 时
> 两者均可省略，维持此记述。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL"
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CODE-ANAL"

# 执行钢结构规范校核（设计计算）
payload = {
  "Argument": {
    "PERFORM_TYPE": "ALL"
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 24. `DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE` — Steel Code Check Table (钢结构规范校核表)

> **功能：** 以表格形式（按构件 MEMB / 按截面 PROP）返回钢结构规范校核的结果。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE
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
          "description": "Filter results by check status",
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
        "VIEW_RATPC": {
          "type": "boolean",
          "description": "Filter to show only members with RatPc greater than 0.4",
          "default": false
        },
        "TABLE_NAME": {
          "type": "string",
          "description": "Response Table Title",
          "default": ""
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
          }
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
          }
        },
        "COMPONENTS": {
          "type": "array",
          "description": "Components of Result Table",
          "items": {
            "type": "string",
            "enum": [
              "CHK",
              "MEMB",
              "COM",
              "SECT",
              "SHR",
              "Section",
              "Material",
              "Fy",
              "LCB",
              "Len",
              "Lb",
              "Ly",
              "Lz",
              "Cb",
              "Ky",
              "Kz",
              "B1y",
              "B1z",
              "B2y",
              "B2z",
              "RatPc",
              "Pu",
              "pPn",
              "Muy",
              "pMny",
              "Muz",
              "pMnz",
              "Vuy",
              "pVny",
              "Vuz",
              "pVnz",
              "Tu",
              "pTn",
              "Def",
              "Defa"
            ]
          }
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 表类型（`"MEMB"`=按构件, `"PROP"`=按截面） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 3 | 要素输入（ELEMS/SECTIONS 二者择一）— `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` | `"ELEMS"` | Object | — | 条件必填 |
| 4 | 截面编号（ELEMS/SECTIONS 二者择一） | `"SECTIONS"` | Array[Integer] | — | 条件必填 |
| 5 | 一次排序（0=SECT, 1=MEMB） | `"PRI_SORT"` | Integer (oneOf) | `1` | 可选 |
| 6 | 结果过滤器（0=All, 1=OK, 2=NG） | `"RESULT"` | Integer (oneOf) | `0` | 可选 |
| 7 | 仅显示 RatPc > 0.4 的构件 | `"VIEW_RATPC"` | Boolean | `false` | 可选 |
| 8 | 响应表标题 | `"TABLE_NAME"` | String | `""` | 可选 |
| 9 | 结果文件保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 10 | 单位设置 | `"UNIT"` | Object | — | 可选 |
| 10.1 | 力单位 | `"FORCE"` | String | — | 可选 |
| 10.2 | 长度单位 | `"DIST"` | String | — | 可选 |
| 10.3 | 热单位 | `"HEAT"` | String | — | 可选 |
| 10.4 | 温度单位 | `"TEMP"` | String | — | 可选 |
| 11 | 数字格式 | `"STYLES"` | Object | — | 可选 |
| 11.1 | 格式（Default/Fixed/Scientific/General） | `"FORMAT"` | String (enum) | — | 可选 |
| 11.2 | 小数位数（0~15） | `"PLACE"` | Integer | — | 可选 |
| 12 | 结果表成分列表 | `"COMPONENTS"` | Array[String] | — | 可选 |

> **`COMPONENTS` 主要成分：** `CHK`(校核结果), `MEMB`(构件号), `COM`(最大组合交互作用比), `SECT`(截面号), `SHR`(剪应力比), `Section`(截面名), `Material`(材质名), `Fy`(屈服强度), `LCB`(控制荷载组合), `Len`(构件长度), `Lb`(侧向支撑长度), `Ly`/`Lz`(未支撑长度), `Cb`(弯曲系数), `Ky`/`Kz`(有效长度系数), `B1y`/`B1z`/`B2y`/`B2z`(弯矩放大系数), `RatPc`(轴压强度比), `Pu`/`pPn`(所需/设计轴强度), `Muy`/`pMny`·`Muz`/`pMnz`(所需/设计受弯强度), `Vuy`/`pVny`·`Vuz`/`pVnz`(所需/设计受剪强度), `Tu`/`pTn`(所需/设计扭转强度), `Def`/`Defa`(挠度/允许挠度)。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "PROP",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "CHK",
      "MEMB",
      "COM",
      "SECT",
      "SHR",
      "Section",
      "Material",
      "Fy",
      "LCB",
      "Len",
      "Lb",
      "Ly",
      "Lz",
      "Cb",
      "Ky",
      "Kz",
      "B1y",
      "B1z",
      "B2y",
      "B2z",
      "RatPc",
      "Pu",
      "pPn",
      "Muy",
      "pMny",
      "Muz",
      "pMnz",
      "Vuy",
      "pVny",
      "Vuz",
      "pVnz",
      "Tu",
      "pTn",
      "Def",
      "Defa"
    ],
    "ELEMS": {
      "KEYS": [
        888
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
    "DIST": "M",
    "HEAD": [
      "CHK",
      "MEMB",
      "COM",
      "SECT",
      "SHR",
      "Section",
      "Material",
      "Fy",
      "LCB",
      "Len",
      "Lb",
      "Ly",
      "Lz",
      "Cb",
      "Ky",
      "Kz",
      "B1y",
      "B1z",
      "B2y",
      "B2z",
      "RatPc",
      "Pu",
      "pPn",
      "Muy",
      "pMny",
      "Muz",
      "pMnz",
      "Vuy",
      "pVny",
      "Vuz",
      "pVnz",
      "Tu",
      "pTn",
      "Def",
      "Defa"
    ],
    "DATA": [
      [
        "OK",
        "888",
        "0.000",
        "1",
        "0.000",
        "400x600, BT 600x400x6/6",
        "SM355",
        "355000",
        "10",
        "3.25000",
        "3.25000",
        "3.25000",
        "3.25000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "1.000",
        "0.000",
        "0.00000",
        "1905.50",
        "0.00000",
        "150.596",
        "0.00000",
        "51.1371",
        "0.00000",
        "460.080",
        "0.00000",
        "73.9731",
        "-",
        "-",
        "-",
        "-"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CODE-TABLE"

# 查询钢结构规范校核结果表
payload = {
  "Argument": {
    "TABLE_TYPE": "PROP",
    "PRI_SORT": 1,
    "RESULT": 0,
    "COMPONENTS": [
      "CHK",
      "MEMB",
      "COM",
      "SECT",
      "SHR",
      "Section",
      "Material",
      "Fy",
      "LCB",
      "Len",
      "Lb",
      "Ly",
      "Lz",
      "Cb",
      "Ky",
      "Kz",
      "B1y",
      "B1z",
      "B2y",
      "B2z",
      "RatPc",
      "Pu",
      "pPn",
      "Muy",
      "pMny",
      "Muz",
      "pMnz",
      "Vuy",
      "pVny",
      "Vuz",
      "pVnz",
      "Tu",
      "pTn",
      "Def",
      "Defa"
    ],
    "ELEMS": {
      "KEYS": [
        888
      ]
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 25. `DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT` — Steel Code Check Report (钢结构规范校核报告)

> **功能：** 将钢结构规范校核报告以 Graphic(JPG)/Detail(DOC)/Summary(TXT) 格式输出到文件。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT
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
        "CURRENT_MODE",
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
        "CURRENT_MODE": {
          "type": "string",
          "description": "Report output mode",
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
          "description": "List of section numbers to include in the report",
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
          "description": "Output file base name. For multiple elements, files are prefixed with index and element number (e.g. 001_E859_filename.jpg, 002_E1_filename.jpg)"
        }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 报告表类型（`"MEMB"`, `"PROP"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 输出模式（`"Graphic"`=JPG, `"Detail"`=DOC, `"Summary"`=TXT） | `"CURRENT_MODE"` | String (oneOf) | — | **必填** |
| 4 | 要素输入（ELEMS/SECTIONS 二者择一）— `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` | `"ELEMS"` | Object | — | 条件必填 |
| 5 | 截面编号（ELEMS/SECTIONS 二者择一） | `"SECTIONS"` | Array[Integer] | — | 条件必填 |
| 6 | 保存目录路径（例 `C:\\MIDAS\\Report\\`） | `"EXPORT_PATH"` | String | — | **必填** |
| 7 | 输出文件基本名称（多要素时附加索引·要素编号前缀） | `"OUTPUT_NAME"` | String | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {
      "KEYS": [
        888,
        1058
      ]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\out.jpg",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/CODE-REPORT"

# 将钢结构规范校核报告输出为文件
payload = {
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {
      "KEYS": [
        888,
        1058
      ]
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 26. `DESIGN/STEEL/KDS-41-30-2022/DREULT` — Steel Design Result (钢结构设计结果图像)

> **功能：** 在屏幕上显示钢结构设计结果，并以图像(JPG)形式截图·保存。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/DREULT
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
        "EXPORT_PATH",
        "RESULT_GRAPHIC"
      ],
      "additionalProperties": false,
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Image file save path and file name."
        },
        "FIGURE_NAME": {
          "type": "string",
          "description": "Smart report image name."
        },
        "SET_HIDDEN": {
          "type": "boolean",
          "description": "Hidden option.",
          "default": false
        },
        "ACTIVE": {
          "type": "object",
          "description": "View/Active settings. For detailed field specifications, refer to the Active documentation."
        },
        "WIDTH": {
          "type": "integer",
          "description": "Image width in pixels.",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "HEIGHT": {
          "type": "integer",
          "description": "Image height in pixels.",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "STAGE_NAME": {
          "type": "string",
          "description": "Construction stage name."
        },
        "ANGLE": {
          "type": "object",
          "description": "View angle settings.",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "HORIZONTAL": {
              "type": "number",
              "description": "Horizontal rotation angle.",
              "default": 0
            },
            "VERTICAL": {
              "type": "number",
              "description": "Vertical rotation angle.",
              "default": 0
            }
          }
        },
        "DISPLAY": {
          "type": "object",
          "description": "View/Display settings. For detailed field specifications, refer to the Display documentation."
        },
        "PERSPECTIVE": {
          "type": "boolean",
          "description": "Enable perspective view.",
          "default": false
        },
        "ZOOM_LEVEL": {
          "type": "number",
          "description": "Zoom level.",
          "default": 100,
          "minimum": 25,
          "maximum": 200
        },
        "BGCOLOR_TOP": {
          "type": "object",
          "description": "Top background color.",
          "additionalProperties": false,
          "properties": {
            "R": {
              "type": "integer",
              "description": "Red component.",
              "minimum": 0,
              "maximum": 255
            },
            "G": {
              "type": "integer",
              "description": "Green component.",
              "minimum": 0,
              "maximum": 255
            },
            "B": {
              "type": "integer",
              "description": "Blue component.",
              "minimum": 0,
              "maximum": 255
            }
          }
        },
        "RESULT_GRAPHIC": {
          "type": "object",
          "description": "Result graphic display settings.",
          "required": [
            "CURRENT_MODE",
            "LOAD_CASE_COMB"
          ],
          "additionalProperties": false,
          "properties": {
            "CURRENT_MODE": {
              "type": "string",
              "description": "Current mode.",
              "oneOf": [
                {
                  "title": "Steel Design",
                  "const": "INFLL_DESIGN_STEEL"
                }
              ]
            },
            "LOAD_CASE_COMB": {
              "type": "object",
              "description": "Load cases and combinations.",
              "required": [
                "TYPE",
                "NAME"
              ],
              "additionalProperties": false,
              "properties": {
                "TYPE": {
                  "type": "string",
                  "description": "Load case type.",
                  "oneOf": [
                    {
                      "title": "Steel Design Load Combination",
                      "const": "CBS"
                    }
                  ]
                },
                "NAME": {
                  "type": "string",
                  "description": "Load case or combination name."
                }
              }
            },
            "COMPONENTS": {
              "type": "object",
              "description": "Component selection for design result display.",
              "required": [],
              "additionalProperties": false,
              "properties": {
                "COMP": {
                  "type": "string",
                  "description": "Design component to display.",
                  "default": "Combined",
                  "oneOf": [
                    {
                      "title": "Axial",
                      "const": "Axial"
                    },
                    {
                      "title": "Shear-y",
                      "const": "Shear-y"
                    },
                    {
                      "title": "Shear-z",
                      "const": "Shear-z"
                    },
                    {
                      "title": "Bend-y",
                      "const": "Bend-y"
                    },
                    {
                      "title": "Bend-z",
                      "const": "Bend-z"
                    },
                    {
                      "title": "Combined",
                      "const": "Combined"
                    }
                  ]
                }
              }
            },
            "TYPE_OF_DISPLAY": {
              "type": "object",
              "description": "Display options for design result visualization.",
              "required": [],
              "additionalProperties": false,
              "properties": {
                "CONTOUR": {
                  "type": "object",
                  "description": "Contour display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "description": "Enable contour display.",
                      "default": false
                    },
                    "NUM_OF_COLOR": {
                      "type": "integer",
                      "description": "Number of contour colors.",
                      "default": 12,
                      "minimum": 2,
                      "maximum": 20
                    },
                    "COLOR_TYPE": {
                      "type": "string",
                      "description": "Contour color type.",
                      "default": "vrgb",
                      "oneOf": [
                        {
                          "title": "V->R->G->B",
                          "const": "vrgb"
                        },
                        {
                          "title": ">R->G->B",
                          "const": "rgb"
                        },
                        {
                          "title": "R->B->G",
                          "const": "rbg"
                        },
                        {
                          "title": "Gray Scaled",
                          "const": "gray scaled"
                        }
                      ]
                    },
                    "OPTIONS": {
                      "type": "object",
                      "description": "Contour options.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "GRADIENT_FILL": {
                          "type": "boolean",
                          "description": "Use gradient fill.",
                          "default": false
                        },
                        "CONTOUR_FILL": {
                          "type": "boolean",
                          "description": "Use contour fill.",
                          "default": true
                        }
                      }
                    }
                  }
                },
                "VALUES": {
                  "type": "object",
                  "description": "Value display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "description": "Enable value display.",
                      "default": false
                    },
                    "DECIMAL_PT": {
                      "type": "integer",
                      "description": "Decimal places.",
                      "default": 0,
                      "minimum": 0,
                      "maximum": 15
                    },
                    "VALUE_EXP": {
                      "type": "boolean",
                      "description": "Use exponential notation.",
                      "default": false
                    },
                    "MINMAX_ONLY": {
                      "type": "object",
                      "description": "Min/max display settings.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "MAXMIN": {
                          "type": "string",
                          "description": "Min/max display mode.",
                          "default": "Min & Max",
                          "oneOf": [
                            {
                              "title": "Min. & Max",
                              "const": "Min & Max"
                            },
                            {
                              "title": "Absolut Max",
                              "const": "Abs Max"
                            },
                            {
                              "title": "Maximum",
                              "const": "max"
                            },
                            {
                              "title": "MMinimumin",
                              "const": "min"
                            }
                          ]
                        },
                        "LIMIT_SCALE": {
                          "type": "integer",
                          "description": "Scale limit.",
                          "default": 0
                        }
                      }
                    },
                    "SET_ORIENT": {
                      "type": "integer",
                      "description": "Value text orientation.",
                      "default": 0
                    }
                  }
                },
                "LEGEND": {
                  "type": "object",
                  "description": "Legend display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "OPT_CHECK": {
                      "type": "boolean",
                      "description": "Enable legend display.",
                      "default": false
                    },
                    "POSITION": {
                      "type": "string",
                      "description": "Legend position.",
                      "default": "left",
                      "oneOf": [
                        {
                          "title": "Right",
                          "const": "right"
                        },
                        {
                          "title": "Left",
                          "const": "left"
                        },
                        {
                          "title": "Top",
                          "const": "top"
                        },
                        {
                          "title": "Bottom",
                          "const": "bottom"
                        }
                      ]
                    },
                    "VALUE_EXP": {
                      "type": "boolean",
                      "description": "Use exponential notation for legend values.",
                      "default": true
                    },
                    "DECIMAL_PT": {
                      "type": "integer",
                      "description": "Decimal places for legend values.",
                      "default": 0,
                      "minimum": 0,
                      "maximum": 15
                    }
                  }
                },
                "CODE_CHECKING_RATIO": {
                  "type": "object",
                  "description": "Steel code checking ratio display settings.",
                  "required": [],
                  "additionalProperties": false,
                  "properties": {
                    "CHECK": {
                      "type": "boolean",
                      "description": "Enable code checking ratio display.",
                      "default": true
                    },
                    "DISPLAY_MEMBERS": {
                      "type": "object",
                      "description": "Steel member types to display.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "BEAM": {
                          "type": "boolean",
                          "description": "Display beam members.",
                          "default": true
                        },
                        "COLUMN": {
                          "type": "boolean",
                          "description": "Display column members.",
                          "default": true
                        },
                        "BRACE": {
                          "type": "boolean",
                          "description": "Display brace members.",
                          "default": true
                        }
                      }
                    },
                    "COLUMN_SECTION_SIZE": {
                      "type": "object",
                      "description": "Column section size display settings.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "SCALE_FACTOR": {
                          "type": "number",
                          "description": "Scale factor for column section visualization.",
                          "default": 1,
                          "minimum": 0.1,
                          "maximum": 100
                        }
                      }
                    },
                    "VALUE_OPTION": {
                      "type": "object",
                      "description": "Value display format settings.",
                      "required": [],
                      "additionalProperties": false,
                      "properties": {
                        "DECIMAL_PLACES": {
                          "type": "integer",
                          "description": "Number of decimal places.",
                          "default": 2,
                          "minimum": 0,
                          "maximum": 15
                        },
                        "EXPONENTIAL": {
                          "type": "boolean",
                          "description": "Use exponential notation.",
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
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 图像保存路径及文件名 | `"EXPORT_PATH"` | String | — | **必填** |
| 3 | 智能报告图像名称 | `"FIGURE_NAME"` | String | — | 可选 |
| 4 | Hidden 选项 | `"SET_HIDDEN"` | Boolean | `false` | 可选 |
| 5 | View/Active 设置（引用 Active 文档） | `"ACTIVE"` | Object | — | 可选 |
| 6 | 图像宽度 px（100~10000） | `"WIDTH"` | Integer | `1000` | 可选 |
| 7 | 图像高度 px（100~10000） | `"HEIGHT"` | Integer | `1000` | 可选 |
| 8 | 施工阶段名称 | `"STAGE_NAME"` | String | — | 可选 |
| 9 | 视图角度 | `"ANGLE"` | Object | — | 可选 |
| 9.1 | 水平旋转角 | `"HORIZONTAL"` | Number | `0` | 可选 |
| 9.2 | 垂直旋转角 | `"VERTICAL"` | Number | `0` | 可选 |
| 10 | View/Display 设置（引用 Display 文档） | `"DISPLAY"` | Object | — | 可选 |
| 11 | 透视投影 | `"PERSPECTIVE"` | Boolean | `false` | 可选 |
| 12 | 缩放级别（25~200） | `"ZOOM_LEVEL"` | Number | `100` | 可选 |
| 13 | 上部背景色（R/G/B, 0~255） | `"BGCOLOR_TOP"` | Object | — | 可选 |
| 14 | 结果图形设置 | `"RESULT_GRAPHIC"` | Object | — | **必填** |
| 14.1 | 当前模式（`"INFLL_DESIGN_STEEL"`=Steel Design） | `"CURRENT_MODE"` | String (oneOf) | — | **必填** |
| 14.2 | 荷载工况/组合 | `"LOAD_CASE_COMB"` | Object | — | **必填** |
| 14.2.1 | 荷载类型（`"CBS"`=Steel Design Load Combination） | `"TYPE"` | String (oneOf) | — | **必填** |
| 14.2.2 | 荷载名称 | `"NAME"` | String | — | **必填** |
| 14.3 | 显示成分（`COMP`: Axial/Shear-y/Shear-z/Bend-y/Bend-z/Combined） | `"COMPONENTS"` | Object | — | 可选 |
| 14.4 | 显示类型（CONTOUR / VALUES / LEGEND / CODE_CHECKING_RATIO） | `"TYPE_OF_DISPLAY"` | Object | — | 可选 |
| 14.4.1 | Contour（OPT_CHECK, NUM_OF_COLOR 2~20, COLOR_TYPE vrgb/rgb/rbg/gray scaled, OPTIONS.GRADIENT_FILL·CONTOUR_FILL） | `"CONTOUR"` | Object | — | 可选 |
| 14.4.2 | Values（OPT_CHECK, DECIMAL_PT, VALUE_EXP, MINMAX_ONLY.MAXMIN, SET_ORIENT） | `"VALUES"` | Object | — | 可选 |
| 14.4.3 | Legend（OPT_CHECK, POSITION right/left/top/bottom, VALUE_EXP, DECIMAL_PT） | `"LEGEND"` | Object | — | 可选 |
| 14.4.4 | Code Checking Ratio（COMP=Combined 时; CHECK, DISPLAY_MEMBERS.BEAM·COLUMN·BRACE, COLUMN_SECTION_SIZE.SCALE_FACTOR, VALUE_OPTION） | `"CODE_CHECKING_RATIO"` | Object | — | 可选 |

> `RESULT_GRAPHIC` 的下级除上表之外，schema 中还定义了详细的嵌套字段（各颜色/取值/图例选项的默认值·范围请参考上方的 **JSON Schema** 块）。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\result\\steel design result.jpg",
    "SET_HIDDEN": true,
    "WIDTH": 1000,
    "HEIGHT": 1000,
    "PERSPECTIVE": false,
    "ZOOM_LEVEL": 100,
    "RESULT_GRAPHIC": {
      "CURRENT_MODE": "INFLL_DESIGN_STEEL",
      "LOAD_CASE_COMB": {
        "TYPE": "CBS",
        "NAME": "STEEL_gLCB5"
      },
      "COMPONENTS": {
        "COMP": "Combined"
      },
      "TYPE_OF_DISPLAY": {
        "LEGEND": {
          "OPT_CHECK": true,
          "VALUE_EXP": false,
          "DECIMAL_PT": 3
        },
        "CONTOUR": {
          "OPT_CHECK": true,
          "OPTIONS": {
            "GRADIENT_FILL": true
          }
        },
        "VALUES": {
          "OPT_CHECK": true,
          "DECIMAL_PT": 5,
          "VALUE_EXP": true,
          "SET_ORIENT": 15,
          "MINMAX_ONLY": {
            "MAXMIN": "min",
            "LIMIT_SCALE": 5
          }
        },
        "CODE_CHECKING_RATIO": {
          "CHECK": true,
          "DISPLAY_MEMBERS": {
            "COLUMN": true,
            "BEAM": false,
            "BRACE": true
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
  "message": "MIDAS GEN NX command complete"
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/DREULT"

# 截图/保存钢结构设计结果图像
payload = {
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\result\\steel design result.jpg",
    "SET_HIDDEN": true,
    "WIDTH": 1000,
    "HEIGHT": 1000,
    "PERSPECTIVE": false,
    "ZOOM_LEVEL": 100,
    "RESULT_GRAPHIC": {
      "CURRENT_MODE": "INFLL_DESIGN_STEEL",
      "LOAD_CASE_COMB": {
        "TYPE": "CBS",
        "NAME": "STEEL_gLCB5"
      },
      "COMPONENTS": {
        "COMP": "Combined"
      },
      "TYPE_OF_DISPLAY": {
        "LEGEND": {
          "OPT_CHECK": true,
          "VALUE_EXP": false,
          "DECIMAL_PT": 3
        },
        "CONTOUR": {
          "OPT_CHECK": true,
          "OPTIONS": {
            "GRADIENT_FILL": true
          }
        },
        "VALUES": {
          "OPT_CHECK": true,
          "DECIMAL_PT": 5,
          "VALUE_EXP": true,
          "SET_ORIENT": 15,
          "MINMAX_ONLY": {
            "MAXMIN": "min",
            "LIMIT_SCALE": 5
          }
        },
        "CODE_CHECKING_RATIO": {
          "CHECK": true,
          "DISPLAY_MEMBERS": {
            "COLUMN": true,
            "BEAM": false,
            "BRACE": true
          }
        }
      }
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## 27. `DESIGN/STEEL/KDS-41-30-2022/TABLE` — Steel Member Design Forces (钢构件设计内力)

> **功能：** 返回钢构件设计内力表（STEELMEMBERDESIGNFORCES），或将其保存为文件。

### Input URI

```
{base url}/DESIGN/STEEL/KDS-41-30-2022/TABLE
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
            "STEELMEMBERDESIGNFORCES"
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 响应表标题 | `"TABLE_NAME"` | String | `""` | 可选 |
| 3 | 表类型（固定为 `"STEELMEMBERDESIGNFORCES"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 4 | 结果文件保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 5 | 单位设置（FORCE/DIST/HEAT/TEMP） | `"UNIT"` | Object | `"System"` | 可选 |
| 6 | 数字格式（FORMAT: Default/Fixed/Scientific/General, PLACE 0~15） | `"STYLES"` | Object | `"System"` | 可选 |
| 7 | 结果表成分（`Index`,`Memb`,`Part`,`LComName`,`Type`,`Fx`,`Fy`,`Fz`,`Mx`,`My`,`Mz`） | `"COMPONENTS"` | Array[String] | — | 可选 |
| 8 | 节点/要素选择（`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 中之一） | `"NODE_ELEMS"` | Object | — | 可选 |
| 9 | 要素 PART（`PartI`,`Part1/4`,`Part2/4`,`Part3/4`,`PartJ`） | `"PARTS"` | Array[String] | `["All"]` | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\SteelMemberForces.json",
    "COMPONENTS": [
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
    "PARTS": [
      "All",
      "PartI",
      "Part1/4",
      "Part2/4",
      "Part3/4",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1072
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
    "DIST": "M",
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
        "1072",
        "I",
        "gLCB183",
        "Max",
        "0.0000",
        "0.0000",
        "-137.7264",
        "0.0000",
        "-144.9112",
        "0.0000"
      ],
      [
        "2",
        "1072",
        "I",
        "gLCB184",
        "Max",
        "0.0000",
        "0.0000",
        "-118.0512",
        "0.0000",
        "-124.2096",
        "0.0000"
      ],
      [
        "3",
        "1072",
        "1/4",
        "gLCB183",
        "Max",
        "0.0000",
        "0.0000",
        "-107.3363",
        "0.0000",
        "-83.5333",
        "0.0000"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022/TABLE"

# 查询钢构件设计内力表
payload = {
  "Argument": {
    "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\SteelMemberForces.json",
    "COMPONENTS": [
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
    "PARTS": [
      "All",
      "PartI",
      "Part1/4",
      "Part2/4",
      "Part3/4",
      "PartJ"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        1072
      ]
    }
  }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())
```

---

## End-to-End Workflow

以下示例将钢结构设计的典型流程串联为一个：**设计代码选项（DCO, PUT）→ 未支撑长度（LENG, POST）→ 设计构件指定（MEMB, PUT）→ 执行规范校核（CODE-ANAL）→ 查询结果表（CODE-TABLE / TABLE）**。其中包含处理公共 base 前缀的可复用辅助函数。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
STEEL_BASE = f"{BASE_URL}/DESIGN/STEEL/KDS-41-30-2022"


def steel(method, code, payload=None):
    """DESIGN/STEEL/KDS-41-30-2022/<code> 公共调用辅助函数"""
    url = f"{STEEL_BASE}/{code}"
    res = requests.request(method, url, headers=HEADERS, json=payload)
    res.raise_for_status()
    try:
        return res.json()
    except ValueError:
        return res.text


# 1) 设置设计代码选项（DCO, PUT）— config-singleton
steel("PUT", "DCO", {
    "Assign": {"1": {
        "DGNCODE": "KDS 41 30 : 2022",
        "DEFL_CHK": True,
        "SEISMIC": False,
        "COMB_RATIO": 0,
    }}
})

# 2) 设置未支撑长度（LENG, POST）— member-CRUD
steel("POST", "LENG", {
    "Assign": {
        "888": {"LY": 3.5, "LZ": 3.5, "LB": 3.5},
        "891": {"LY": 4.0, "LZ": 4.0, "LB": 2.0},
    }
})

# 3) 设计构件指定（MEMB, PUT）— 将要素编组为设计构件
steel("PUT", "MEMB", {
    "Assign": {
        "1": {"AELEM": [933, 934], "bREVERSE": False},
        "2": {"AELEM": [906, 891], "bREVERSE": True},
    }
})

# 4) 执行钢结构规范校核（CODE-ANAL, POST）— 对象为全部要素
print("规范校核:", steel("POST", "CODE-ANAL", {"Argument": {"PERFORM_TYPE": "ALL"}}))

# 5-a) 查询规范校核结果表（CODE-TABLE, POST）
table = steel("POST", "CODE-TABLE", {
    "Argument": {
        "TABLE_TYPE": "MEMB",
        "PRI_SORT": 1,
        "RESULT": 0,
        "COMPONENTS": ["CHK", "MEMB", "SECT", "Section", "Material", "COM", "RatPc"],
        "ELEMS": {"KEYS": [888]},
    }
})
print("校核表:", table)

# 5-b) 查询钢构件设计内力表（TABLE, POST）
forces = steel("POST", "TABLE", {
    "Argument": {
        "TABLE_TYPE": "STEELMEMBERDESIGNFORCES",
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
        "NODE_ELEMS": {"KEYS": [1072]},
    }
})
print("构件内力表:", forces)
```
