# 26. Design Code – RC KDS 41 20:2022 (钢筋混凝土设计)

> **适用产品：** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> ```
> **认证头：** `MAPI-Key: <已签发的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../26_Design_RC_KDS41202022.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分涵盖 **钢筋混凝土（RC）设计代码 KDS 41 20:2022** 相关的 **70 个端点**（通用前缀
`KDS-41-20-2022/<CODE>` 端点 69 个 + RC 设计代码选择端点 `DRC` 1 个）。
除 `DRC` 外的 69 个端点均使用通用 URI 前缀 **`{base url}/DESIGN/RC/KDS-41-20-2022/<CODE>`**，
按各自的端点代码拼接使用。

> ⚠️ **2026-08-06 新端点发现：** `DESIGN/RC/DRC`（激活的 RC 设计代码选择）的原文
> 生成日期为 2026-06-18，此前早已存在；只是在章概览文章（“KDS 41 20 : 2022”）中于
> 2026-08-06 新增了收录该条目的 “Design Code” 分组时才被发现。它使用不写 `KDS-41-20-2022` 前缀的
> 独立 URI（`DESIGN/RC/DRC`），因此在不影响编号体系的前提下以 `## 0.` 追加。

- **`"Assign"` 方式：** 设计代码与构件参数设置端点在请求体中使用 `"Assign"` 对象，各键为字符串 ID（例：`"1"`）或构件编号。
- **`"Argument"` 方式：** 设计执行（ANAL）、结果表格（TABLE）、报告（REPORT）端点仅支持 POST，通过 `"Argument"` 对象指定对象与选项。
- **三种方法模式：**
  - **设置单例** （例：`DCO`、`LLRF`、`MATD`、`MEMB`、`SRDF`、`LMRR`）：`GET` · `PUT` · `DELETE`（无 POST，用 PUT 创建/更新）
  - **构件级参数** （例：`LENG`、`KFAC`、`FMAG`、钢筋数据 `REBB` 等）：`POST` · `GET` · `PUT` · `DELETE`（构件 ID `Assign`）
  - **设计执行与结果** （`*-ANAL` / `*-TABLE` / `*-REPORT`、`CDESIGN`、`TABLE`）：仅 `POST` 动作

> **参考：** 各端点准确的 Active Methods 已在下表与各节中注明。钢结构设计见 **[25_Design_Steel_KDS41302022.md](./25_Design_Steel_KDS41302022.md)**，SRC 型钢混凝土设计见 **[27_Design_SRC_AIKSRC2K.md](./27_Design_SRC_AIKSRC2K.md)**。RC 设计荷载组合在第 13 章（Load Combinations）中说明。

---

## 端点列表（70 个）

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 0 | [`DRC`](#0-designrcdrc--rc-design-code-rc-设计代码选择) | RC 设计代码选择（不使用 `KDS-41-20-2022` 前缀） | GET · PUT · DELETE |
| 1 | [`DCO`](#1-designrckds-41-20-2022dco--concrete-design-code-option-混凝土设计代码选项) | 混凝土设计代码选项 | GET · PUT · DELETE |
| 2 | [`DCTL`](#2-designrckds-41-20-2022dctl--definition-of-frame-框架定义) | 框架定义 | GET · PUT · DELETE |
| 3 | [`LLRF`](#3-designrckds-41-20-2022llrf--live-load-reduction-factor-活荷载折减系数) | 活荷载折减系数 | GET · PUT · DELETE |
| 4 | [`LCTB`](#4-designrckds-41-20-2022lctb--load-contribution-for-nonlinear-load-case-非线性荷载工况荷载贡献) | 非线性荷载工况荷载贡献 | GET · DELETE |
| 5 | [`SRDF`](#5-designrckds-41-20-2022srdf--strength-reduction-factors-强度折减系数) | 强度折减系数 | GET · PUT · DELETE |
| 6 | [`EQCT`](#6-designrckds-41-20-2022eqct--seismic-load-combination-type-地震荷载组合类型) | 地震荷载组合类型 | POST · GET · PUT · DELETE |
| 7 | [`ULCT`](#7-designrckds-41-20-2022ulct--underground-load-combination-type-地下荷载组合类型) | 地下荷载组合类型 | POST · GET · PUT · DELETE |
| 8 | [`SUEQ`](#8-designrckds-41-20-2022sueq--scale-up-factor-for-earthquake-地震放大系数) | 地震放大系数 | POST · GET · PUT · DELETE |
| 9 | [`SDGN`](#9-designrckds-41-20-2022sdgn--seismic-design-type-抗震设计类型) | 抗震设计类型 | POST · GET · PUT · DELETE |
| 10 | [`SCOL`](#10-designrckds-41-20-2022scol--seismic-column-type-抗震柱类型) | 抗震柱类型 | POST · GET · PUT · DELETE |
| 11 | [`MBTP`](#11-designrckds-41-20-2022mbtp--modify-member-type-构件类型修改) | 构件类型修改 | POST · GET · PUT · DELETE |
| 12 | [`MEMB`](#12-designrckds-41-20-2022memb--member-assignment-构件指定) | 构件指定 | GET · PUT · DELETE |
| 13 | [`MATD`](#13-designrckds-41-20-2022matd--modify-concrete-material-混凝土材料修改) | 混凝土材料修改 | GET · PUT · DELETE |
| 14 | [`LENG`](#14-designrckds-41-20-2022leng--unbraced-length-l-lb-未支撑长度) | 未支撑长度(L, Lb) | POST · GET · PUT · DELETE |
| 15 | [`KFAC`](#15-designrckds-41-20-2022kfac--effective-length-factor-k-有效屈曲长度系数) | 有效屈曲长度系数(K) | POST · GET · PUT · DELETE |
| 16 | [`CMFT`](#16-designrckds-41-20-2022cmft--equivalent-moment-correction-factorcm-等效弯矩校正系数) | 等效弯矩校正系数(Cm) | POST · GET · PUT · DELETE |
| 17 | [`FMAG`](#17-designrckds-41-20-2022fmag--moment-magnifierb1delta_b-b2delta_s-弯矩放大系数) | 弯矩放大系数(B1/δb, B2/δs) | POST · GET · PUT · DELETE |
| 18 | [`MLLR`](#18-designrckds-41-20-2022mllr--modify-live-load-reduction-factor-活荷载折减系数修改) | 活荷载折减系数修改 | POST · GET · PUT · DELETE |
| 19 | [`HCBM`](#19-designrckds-41-20-2022hcbm--haunched-beam-assignment-加腋梁指定) | 加腋梁指定 | POST · GET · PUT · DELETE |
| 20 | [`MRFT`](#20-designrckds-41-20-2022mrft--moment-redistribution-factor-弯矩重分布系数) | 弯矩重分布系数 | POST · GET · PUT · DELETE |
| 21 | [`TRFT`](#21-designrckds-41-20-2022trft--torsion-reduction-factor-扭转折减系数) | 扭转折减系数 | POST · GET · PUT · DELETE |
| 22 | [`MCMB`](#22-designrckds-41-20-2022mcmb--moment-calculation-method-for-beam-梁弯矩计算方法) | 梁弯矩计算方法 | POST · GET · PUT · DELETE |
| 23 | [`DFBA`](#23-designrckds-41-20-2022dfba--design-force-for-beam-assigned-as-member-构件指定梁的设计内力) | 构件指定梁的设计内力 | POST · GET · PUT · DELETE |
| 24 | [`PMDM`](#24-designrckds-41-20-2022pmdm--p-m-curve-calculation-method-p-m-曲线计算方法) | P-M 曲线计算方法 | POST · GET · DELETE · PUT |
| 25 | [`WMAK`](#25-designrckds-41-20-2022wmak--modify-wall-mark-data-墙体标识数据修改) | 墙体标识数据修改 | POST · GET · PUT · DELETE |
| 26 | [`BEMW`](#26-designrckds-41-20-2022bemw--boundary-element-method-by-wall-id-按墙体id的边缘构件法) | 按墙体ID的边缘构件法 | POST · GET · PUT · DELETE |
| 27 | [`REXC`](#27-designrckds-41-20-2022rexc--rebar-exposure-condition-钢筋暴露条件) | 钢筋暴露条件 | POST · GET · PUT · DELETE |
| 28 | [`LMRR`](#28-designrckds-41-20-2022lmrr--limiting-maximum-rebar-ratio-最大配筋率限制) | 最大配筋率限制 | GET · PUT · DELETE |
| 29 | [`DCRM-BEAM`](#29-designrckds-41-20-2022dcrm-beam--design-criteria-for-rebars-by-beam-member-按梁构件的钢筋设计准则) | 按梁构件的钢筋设计准则 | POST · GET · PUT · DELETE |
| 30 | [`DCRM-COLUMN`](#30-designrckds-41-20-2022dcrm-column--design-criteria-for-rebars-by-column-member-按柱构件的钢筋设计准则) | 按柱构件的钢筋设计准则 | POST · GET · PUT · DELETE |
| 31 | [`DCRM-BRACE`](#31-designrckds-41-20-2022dcrm-brace--design-criteria-for-rebars-by-brace-member-按支撑构件的钢筋设计准则) | 按支撑构件的钢筋设计准则 | POST · GET · PUT · DELETE |
| 32 | [`DCRM-WALL`](#32-designrckds-41-20-2022dcrm-wall--design-criteria-for-rebars-by-wall-member-按墙体构件的钢筋设计准则) | 按墙体构件的钢筋设计准则 | POST · GET · PUT · DELETE |
| 33 | [`DCRE`](#33-designrckds-41-20-2022dcre--design-criteria-for-rebar-钢筋设计准则) | 钢筋设计准则 | POST · GET · PUT · DELETE |
| 34 | [`DCREM`](#34-designrckds-41-20-2022dcrem--same-beam-rebar-at-joints-节点处梁钢筋同一化) | 节点处梁钢筋同一化 | POST · GET · PUT · DELETE |
| 35 | [`REBB`](#35-designrckds-41-20-2022rebb--modify-beam-rebar-data-梁钢筋数据修改) | 梁钢筋数据修改 | POST · GET · DELETE · PUT |
| 36 | [`REBC`](#36-designrckds-41-20-2022rebc--modify-column-rebar-data-柱钢筋数据修改) | 柱钢筋数据修改 | POST · GET · PUT · DELETE |
| 37 | [`REBW`](#37-designrckds-41-20-2022rebw--modify-wall-rebar-data-墙体钢筋数据修改) | 墙体钢筋数据修改 | POST · PUT · DELETE · GET |
| 38 | [`REBR`](#38-designrckds-41-20-2022rebr--modify-brace-rebar-data-支撑钢筋数据修改) | 支撑钢筋数据修改 | POST · GET · PUT · DELETE |
| 39 | [`BD-ANAL`](#39-designrckds-41-20-2022bd-anal--rc-beam-design-perform-rc-梁设计执行) | RC 梁设计执行 | POST |
| 40 | [`BD-TABLE`](#40-designrckds-41-20-2022bd-table--rc-beam-design-table-rc-梁设计表格) | RC 梁设计表格 | POST |
| 41 | [`BD-REPORT`](#41-designrckds-41-20-2022bd-report--rc-beam-design-report-rc-梁设计报告) | RC 梁设计报告 | POST |
| 42 | [`CD-ANAL`](#42-designrckds-41-20-2022cd-anal--rc-column-design-perform-rc-柱设计执行) | RC 柱设计执行 | POST |
| 43 | [`CD-TABLE`](#43-designrckds-41-20-2022cd-table--rc-column-design-table-rc-柱设计表格) | RC 柱设计表格 | POST |
| 44 | [`CD-REPORT`](#44-designrckds-41-20-2022cd-report--rc-column-design-report-rc-柱设计报告) | RC 柱设计报告 | POST |
| 45 | [`BRD-ANAL`](#45-designrckds-41-20-2022brd-anal--rc-brace-design-perform-rc-支撑设计执行) | RC 支撑设计执行 | POST |
| 46 | [`BRD-TABLE`](#46-designrckds-41-20-2022brd-table--rc-brace-design-table-rc-支撑设计表格) | RC 支撑设计表格 | POST |
| 47 | [`BRD-REPORT`](#47-designrckds-41-20-2022brd-report--rc-brace-design-report-rc-支撑设计报告) | RC 支撑设计报告 | POST |
| 48 | [`WD-ANAL`](#48-designrckds-41-20-2022wd-anal--rc-wall-design-perform-rc-墙体设计执行) | RC 墙体设计执行 | POST |
| 49 | [`WD-TABLE`](#49-designrckds-41-20-2022wd-table--rc-wall-design-table-rc-墙体设计表格) | RC 墙体设计表格 | POST |
| 50 | [`WD-REPORT`](#50-designrckds-41-20-2022wd-report--rc-wall-design-report-rc-墙体设计报告) | RC 墙体设计报告 | POST |
| 51 | [`HCD-ANAL`](#51-designrckds-41-20-2022hcd-anal--rc-haunched-beam-design-perform-rc-加腋梁设计执行) | RC 加腋梁设计执行 | POST |
| 52 | [`HCD-TABLE`](#52-designrckds-41-20-2022hcd-table--rc-haunched-beam-design-table-rc-加腋梁设计表格) | RC 加腋梁设计表格 | POST |
| 53 | [`HCD-REPORT`](#53-designrckds-41-20-2022hcd-report--rc-haunched-beam-design-report-rc-加腋梁设计报告) | RC 加腋梁设计报告 | POST |
| 54 | [`BC-ANAL`](#54-designrckds-41-20-2022bc-anal--rc-beam-check-perform-rc-梁验算执行) | RC 梁验算执行 | POST |
| 55 | [`BC-TABLE`](#55-designrckds-41-20-2022bc-table--rc-beam-check-table-rc-梁验算表格) | RC 梁验算表格 | POST |
| 56 | [`BC-REPORT`](#56-designrckds-41-20-2022bc-report--rc-beam-check-report-rc-梁验算报告) | RC 梁验算报告 | POST |
| 57 | [`CC-ANAL`](#57-designrckds-41-20-2022cc-anal--rc-column-check-perform-rc-柱验算执行) | RC 柱验算执行 | POST |
| 58 | [`CC-TABLE`](#58-designrckds-41-20-2022cc-table--rc-column-check-table-rc-柱验算表格) | RC 柱验算表格 | POST |
| 59 | [`CC-REPORT`](#59-designrckds-41-20-2022cc-report--rc-column-check-report-rc-柱验算报告) | RC 柱验算报告 | POST |
| 60 | [`BRC-ANAL`](#60-designrckds-41-20-2022brc-anal--rc-brace-check-perform-rc-支撑验算执行) | RC 支撑验算执行 | POST |
| 61 | [`BRC-TABLE`](#61-designrckds-41-20-2022brc-table--rc-brace-check-table-rc-支撑验算表格) | RC 支撑验算表格 | POST |
| 62 | [`BRC-REPORT`](#62-designrckds-41-20-2022brc-report--rc-brace-check-report-rc-支撑验算报告) | RC 支撑验算报告 | POST |
| 63 | [`WC-ANAL`](#63-designrckds-41-20-2022wc-anal--rc-wall-check-perform-rc-墙体验算执行) | RC 墙体验算执行 | POST |
| 64 | [`WC-TABLE`](#64-designrckds-41-20-2022wc-table--rc-wall-check-table-rc-墙体验算表格) | RC 墙体验算表格 | POST |
| 65 | [`WC-REPORT`](#65-designrckds-41-20-2022wc-report--rc-wall-check-report-rc-墙体验算报告) | RC 墙体验算报告 | POST |
| 66 | [`CDESIGN`](#66-designrckds-41-20-2022cdesign--rc-concrete-design-result-rc-混凝土综合设计结果) | RC 混凝土综合设计结果 | POST |
| 67 | [`TABLE`](#67-designrckds-41-20-2022table--column-design-forces-柱设计内力) | 柱设计内力(Column Design Forces) | POST |
| 68 | [`TABLE`](#68-designrckds-41-20-2022table--brace-design-forces-支撑设计内力) | 支撑设计内力(Brace Design Forces) | POST |
| 69 | [`TABLE`](#69-designrckds-41-20-2022table--beam-design-forces-梁设计内力) | 梁设计内力(Beam Design Forces) | POST |

---

## 0. `DESIGN/RC/DRC` — RC Design Code (RC 设计代码选择)

> **功能：** 选择当前项目要应用的 **RC 设计代码**。本章其余 69 个
> 端点（`KDS-41-20-2022/<CODE>`）的 URI 都带该前缀，而本端点是
> 一个不使用 `KDS-41-20-2022` 前缀的独立上层选择端点。

### Input URI

```
{base url}/DESIGN/RC/DRC
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
                "KDS 41 20 : 2022"
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
| --- | --- | --- | --- | --- | --- |
| 1 | Assign 包装（ID 字符串键，1 个） | `"Assign"` | Object | — | **必填** |
| 2 | RC 设计代码 · 当前仅支持 `"KDS 41 20 : 2022"` 一个取值 | `"DGNCODE"` | String (enum) | — | **必填** |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KDS 41 20 : 2022"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCON": {
    "1": {
      "DGNCODE": "KDS 41 20 : 2022"
    }
  }
}
```

> ⚠️ **响应顶层键注意：** GET 响应的顶层键为 `"DCON"`（既不是端点名 `DRC`，
> 也不是选项端点 `DCO`），与原文 Response 示例保持一致。

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/DRC"

# 选择 RC 设计代码（PUT）：KDS 41 20:2022
payload = {"Assign": {"1": {"DGNCODE": "KDS 41 20 : 2022"}}}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 1. `DESIGN/RC/KDS-41-20-2022/DCO` — Concrete Design Code Option (混凝土设计代码选项)

> **功能：** 设置混凝土设计标准（KDS 41 20:2022）以及抗震特别规定、扭转、弯矩重分布、暴露条件、P-M 曲线计算法等全局设计选项。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCO
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
            "DESIGN_CD"
          ],
          "additionalProperties": false,
          "properties": {
            "DESIGN_CD": {
              "type": "string",
              "description": "Concrete design code standard",
              "oneOf": [
                {
                  "title": "KDS 41 20 : 2022",
                  "const": "KDS 41 20 : 2022"
                }
              ]
            },
            "SEISMIC_PROV": {
              "type": "boolean",
              "description": "Apply Special Provisions for Seismic Design",
              "default": false
            },
            "SEISMIC": {
              "type": "object",
              "description": "Seismic design parameters",
              "additionalProperties": false,
              "properties": {
                "FRAME_TYPE": {
                  "type": "string",
                  "description": "Select Frame Type",
                  "default": "Special",
                  "oneOf": [
                    {
                      "title": "Special Moment Frames",
                      "const": "Special"
                    },
                    {
                      "title": "Intermediate Moment Frames",
                      "const": "Intermediate"
                    },
                    {
                      "title": "Ordinary Moment Frames",
                      "const": "Ordinary"
                    }
                  ]
                },
                "STRONG_COL_WEAK_LAST": {
                  "type": "boolean",
                  "description": "Consider strong column-weak beam on last floor",
                  "default": true
                },
                "SHEAR_WALL": {
                  "type": "object",
                  "description": "Shear Wall Type configuration",
                  "additionalProperties": false,
                  "properties": {
                    "SPEC_RC_WALL": {
                      "type": "boolean",
                      "description": "Special RC Structural Wall",
                      "default": true
                    },
                    "BDRY_ELEM_MTHD": {
                      "type": "string",
                      "description": "Boundary Element Method",
                      "default": "Displacement",
                      "oneOf": [
                        {
                          "title": "Displacement Based Method",
                          "const": "Displacement"
                        },
                        {
                          "title": "Stress Based Method",
                          "const": "Stress"
                        }
                      ]
                    },
                    "DEFL_AMP_FACT": {
                      "type": "number",
                      "description": "Deflection Amplification Factor (Cd)",
                      "default": 4.5,
                      "enum": [
                        1.25,
                        1.5,
                        2,
                        2.5,
                        3,
                        3.25,
                        4,
                        4.5,
                        5,
                        5.5,
                        6,
                        6.5
                      ]
                    },
                    "IMP_FACT": {
                      "type": "number",
                      "description": "Important Factor (Ie)",
                      "default": 1.2,
                      "enum": [
                        1,
                        1.2,
                        1.5
                      ]
                    }
                  }
                },
                "SHEAR_DES": {
                  "type": "object",
                  "description": "Shear for Design configuration",
                  "additionalProperties": false,
                  "properties": {
                    "R": {
                      "type": "number",
                      "description": "Special-only R factor input shown as 'R*Vc(a1*Σ(Mpr)/L) ≥ max(Ve1,Ve2)/2 , R='",
                      "default": 0,
                      "minimum": 0
                    },
                    "MTHD": {
                      "type": "string",
                      "description": "Calculation method",
                      "default": "MIN",
                      "oneOf": [
                        {
                          "title": "MAX(Ve1,Ve2)",
                          "const": "MAX"
                        },
                        {
                          "title": "MIN(Ve1,Ve2)",
                          "const": "MIN"
                        },
                        {
                          "title": "Ve1",
                          "const": "Ve1"
                        },
                        {
                          "title": "Ve2",
                          "const": "Ve2"
                        }
                      ]
                    },
                    "A1": {
                      "type": "number",
                      "description": "Ve1 = Vg + a1*Σ(Mn)/L coefficient",
                      "default": 1
                    },
                    "A2": {
                      "type": "number",
                      "description": "Ve2 = Vg + a2*Veq coefficient",
                      "default": 2
                    }
                  }
                },
                "BEAM_COL_JNT_DES": {
                  "type": "boolean",
                  "description": "Beam-Column Joint Design",
                  "default": false
                },
                "JOINT": {
                  "type": "object",
                  "description": "Beam-Column Joint configuration",
                  "additionalProperties": false,
                  "properties": {
                    "CHK_POS": {
                      "type": "string",
                      "description": "Select Check Position",
                      "default": "Bottom",
                      "oneOf": [
                        {
                          "title": "Top",
                          "const": "Top"
                        },
                        {
                          "title": "Bottom",
                          "const": "Bottom"
                        }
                      ]
                    },
                    "EXCL_MEM_TYPES": {
                      "type": "array",
                      "description": "Member Types to be excluded in Seismic Design",
                      "items": {
                        "type": "string",
                        "enum": [
                          "SUBBEAM",
                          "CANTIL",
                          "UGBEAMCOL"
                        ]
                      },
                      "uniqueItems": true,
                      "default": [
                        "SUBBEAM",
                        "CANTIL",
                        "UGBEAMCOL"
                      ]
                    }
                  }
                }
              }
            },
            "TORS_DES": {
              "type": "boolean",
              "description": "Torsion Design",
              "default": false
            },
            "TORS_RDCT_FACT": {
              "type": "number",
              "description": "Torsion Reduction Factor for Beam",
              "default": 1,
              "minimum": 0
            },
            "MOM_REDIST_FACT": {
              "type": "number",
              "description": "Moment Redistribution Factor for Beam",
              "default": 1,
              "exclusiveMinimum": 0,
              "maximum": 1
            },
            "MOM_CALC_MTHD": {
              "type": "string",
              "description": "Moment Calculation Method for Beam",
              "default": "Equivalent",
              "oneOf": [
                {
                  "title": "Equivalent Rebar",
                  "const": "Equivalent"
                },
                {
                  "title": "Each Rebar",
                  "const": "Each"
                }
              ]
            },
            "USE_SUBDIV_FORCE": {
              "type": "boolean",
              "description": "Use Subdivided Force for Beam Assigned as Member",
              "default": false
            },
            "EXP_COND": {
              "type": "string",
              "description": "Exposure Condition (kcr)",
              "default": "Dry",
              "oneOf": [
                {
                  "title": "Dry",
                  "const": "Dry"
                },
                {
                  "title": "etc",
                  "const": "etc"
                }
              ]
            },
            "PM_CRV_CALC": {
              "type": "string",
              "description": "P-M Curve Calculation Method",
              "default": "KeepMPConstant",
              "oneOf": [
                {
                  "title": "Keep P Constant",
                  "const": "KeepPConstant"
                },
                {
                  "title": "Keep M/P Constant",
                  "const": "KeepMPConstant"
                }
              ]
            },
            "UG_LC": {
              "type": "boolean",
              "description": "Use Under Ground Load Combination Type for Under Ground Members",
              "default": true
            },
            "CONC_STRS_STRN": {
              "type": "string",
              "description": "Concrete Stress-Strain Type for Bending",
              "default": "Equivalent",
              "oneOf": [
                {
                  "title": "Equivalent-Rectangle",
                  "const": "Equivalent"
                },
                {
                  "title": "Parabola-Rectangle (Average)",
                  "const": "Parabola"
                }
              ]
            },
            "FS_MAIN_BAR": {
              "type": "string",
              "description": "fs of Main bar in Beam Design",
              "default": "2/3fy",
              "oneOf": [
                {
                  "title": "2/3*fy",
                  "const": "2/3fy"
                },
                {
                  "title": "By Program",
                  "const": "ByProgram"
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
| 1 | Assign 包装（ID 字符串键，1 个） | `"Assign"` | Object | — | **必填** |
| 2 | 设计代码（固定为 KDS 41 20 : 2022） | `"DESIGN_CD"` | String (oneOf) | — | **必填** |
| 3 | 应用抗震设计特别规定 | `"SEISMIC_PROV"` | Boolean | `false` | 可选 |
| 4 | 扭转设计 | `"TORS_DES"` | Boolean | `false` | 可选 |
| 5 | 梁扭转折减系数（≥0，TORS_DES=true 时） | `"TORS_RDCT_FACT"` | Number | `1` | 可选 |
| 6 | 梁弯矩重分布系数（>0，≤1） | `"MOM_REDIST_FACT"` | Number | `1` | 可选 |
| 7 | 梁弯矩计算法（Equivalent=等效钢筋，Each=单根钢筋） | `"MOM_CALC_MTHD"` | String (oneOf) | `"Equivalent"` | 可选 |
| 8 | 对构件指定的梁使用细分构件内力 | `"USE_SUBDIV_FORCE"` | Boolean | `false` | 可选 |
| 9 | 暴露条件 kcr（Dry / etc） | `"EXP_COND"` | String (oneOf) | `"Dry"` | 可选 |
| 10 | P-M 曲线计算法（KeepPConstant=固定 P，KeepMPConstant=固定 M/P） | `"PM_CRV_CALC"` | String (oneOf) | `"KeepMPConstant"` | 可选 |
| 11 | 对地下构件使用地下荷载组合类型 | `"UG_LC"` | Boolean | `true` | 可选 |
| 12 | 受弯混凝土应力-应变类型（Equivalent=等效矩形，Parabola=抛物线-矩形平均） | `"CONC_STRS_STRN"` | String (oneOf) | `"Equivalent"` | 可选 |
| 13 | 梁设计主筋 fs（2/3fy / ByProgram） | `"FS_MAIN_BAR"` | String (oneOf) | `"2/3fy"` | 可选 |
| 14 | 抗震设计参数（SEISMIC_PROV=true 时） | `"SEISMIC"` | Object | — | 可选 |
| 14.1 | 框架类型（Special=特殊，Intermediate=中间，Ordinary=普通抗弯框架） | `"FRAME_TYPE"` | String (oneOf) | `"Special"` | 可选 |
| 14.2 | 考虑顶层强柱弱梁 | `"STRONG_COL_WEAK_LAST"` | Boolean | `true` | 可选 |
| 14.3 | 剪力墙设置（FRAME_TYPE=Special/Intermediate 时） | `"SHEAR_WALL"` | Object | — | 可选 |
| 14.3.1 | 特殊钢筋混凝土结构墙 | `"SPEC_RC_WALL"` | Boolean | `true` | 可选 |
| 14.3.2 | 边缘构件法（Displacement=位移基准，Stress=应力基准） | `"BDRY_ELEM_MTHD"` | String (oneOf) | `"Displacement"` | 可选 |
| 14.3.3 | 位移放大系数 Cd（1.25/1.5/2/2.5/3/3.25/4/4.5/5/5.5/6/6.5） | `"DEFL_AMP_FACT"` | Number (enum) | `4.5` | 可选 |
| 14.3.4 | 重要性系数 Ie（1 / 1.2 / 1.5） | `"IMP_FACT"` | Number (enum) | `1.2` | 可选 |
| 14.4 | 设计剪力设置 | `"SHEAR_DES"` | Object | — | 可选 |
| 14.4.1 | 计算法（MAX(Ve1,Ve2) / MIN(Ve1,Ve2) / Ve1 / Ve2） | `"MTHD"` | String (oneOf) | `"MIN"` | 可选 |
| 14.4.2 | R·Vc ≥ max(Ve1,Ve2)/2 中的 R（≥0，FRAME_TYPE=Special） | `"R"` | Number | `0` | 可选 |
| 14.4.3 | a1：Ve1 = Vg + a1·Σ(Mn)/L | `"A1"` | Number | `1` | 可选 |
| 14.4.4 | a2：Ve2 = Vg + a2·Veq | `"A2"` | Number | `2` | 可选 |
| 14.5 | 梁-柱节点设计 | `"BEAM_COL_JNT_DES"` | Boolean | `false` | 可选 |
| 14.6 | 梁-柱节点设置 | `"JOINT"` | Object | — | 可选 |
| 14.6.1 | 排除抗震设计的构件类型（SUBBEAM=次梁，CANTIL=悬臂，UGBEAMCOL=地下梁/柱） | `"EXCL_MEM_TYPES"` | Array[string] | `["SUBBEAM","CANTIL","UGBEAMCOL"]` | 可选 |
| 14.6.2 | 验算位置（Top / Bottom） | `"CHK_POS"` | String (oneOf) | `"Bottom"` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "DESIGN_CD": "KDS 41 20 : 2022",
      "MOM_CALC_MTHD": "Equivalent",
      "EXP_COND": "etc",
      "PM_CRV_CALC": "KeepMPConstant",
      "CONC_STRS_STRN": "Equivalent",
      "FS_MAIN_BAR": "2/3fy",
      "SEISMIC_PROV": true,
      "TORS_DES": true,
      "TORS_RDCT_FACT": 1,
      "MOM_REDIST_FACT": 1,
      "USE_SUBDIV_FORCE": true,
      "UG_LC": true,
      "SEISMIC": {
        "FRAME_TYPE": "Special",
        "STRONG_COL_WEAK_LAST": true,
        "BEAM_COL_JNT_DES": true,
        "JOINT": {
          "CHK_POS": "Top",
          "EXCL_MEM_TYPES": [
            "SUBBEAM",
            "CANTIL",
            "UGBEAMCOL"
          ]
        },
        "SHEAR_WALL": {
          "SPEC_RC_WALL": true,
          "BDRY_ELEM_MTHD": "Displacement",
          "DEFL_AMP_FACT": 4,
          "IMP_FACT": 1.2
        },
        "SHEAR_DES": {
          "R": 0.5,
          "MTHD": "Ve1",
          "A1": 1.1,
          "A2": 1.2
        }
      }
    }
  }
}
```

**GET Response Body (顶层键 `DCORC`)**

```json
{
  "DCORC": {
    "1": {
      "DESIGN_CD": "KDS 41 20 : 2022",
      "SEISMIC_PROV": true,
      "TORS_DES": true,
      "MOM_REDIST_FACT": 1,
      "MOM_CALC_MTHD": "Equivalent",
      "USE_SUBDIV_FORCE": true,
      "EXP_COND": "etc",
      "PM_CRV_CALC": "KeepMPConstant",
      "UG_LC": true,
      "CONC_STRS_STRN": "Equivalent",
      "FS_MAIN_BAR": "2/3fy",
      "SEISMIC": {
        "FRAME_TYPE": "Special",
        "STRONG_COL_WEAK_LAST": true,
        "SHEAR_WALL": {
          "SPEC_RC_WALL": true,
          "BDRY_ELEM_MTHD": "Displacement",
          "DEFL_AMP_FACT": 4,
          "IMP_FACT": 1.2
        },
        "SHEAR_DES": {
          "MTHD": "Ve1",
          "R": 0.5,
          "A1": 1.1,
          "A2": 1.2
        },
        "BEAM_COL_JNT_DES": true,
        "JOINT": {
          "EXCL_MEM_TYPES": [
            "SUBBEAM",
            "CANTIL",
            "UGBEAMCOL"
          ],
          "CHK_POS": "Top"
        }
      },
      "TORS_RDCT_FACT": 1
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCO"

# 1) 设置全局混凝土设计选项（PUT）— 含抗震特别规定
payload = {
    "Assign": {
        "1": {
            "DESIGN_CD": "KDS 41 20 : 2022",
            "SEISMIC_PROV": True,          # 应用抗震特别规定
            "TORS_DES": True,              # 执行扭转设计
            "MOM_REDIST_FACT": 0.9,        # 弯矩重分布系数(0~1)
            "PM_CRV_CALC": "KeepMPConstant",
            "SEISMIC": {
                "FRAME_TYPE": "Special",
                "SHEAR_WALL": {"BDRY_ELEM_MTHD": "Displacement", "IMP_FACT": 1.2},
            },
        }
    }
}
res = requests.put(URI, headers=HEADERS, json=payload)
print("PUT:", res.status_code, res.json())

# 2) 查询当前设置（GET）
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 重置设置（DELETE）— 需要时
# requests.delete(URI, headers=HEADERS)
```

---

## 2. `DESIGN/RC/KDS-41-20-2022/DCTL` — Definition of Frame (框架定义)

> **功能：** 定义设计框架 X/Y 方向是否为侧向支撑（Sway/Non-sway）、有效屈曲长度系数是否自动计算、设计类型（3D/平面）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCTL
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
| 1 | Assign 包装（ID 字符串键，1 个） | `"Assign"` | Object | — | **必填** |
| 2 | X 方向框架（Unbraced Sway=非侧向支撑/侧移，Braced Non-sway=侧向支撑/无侧移） | `"FRAMEX"` | String (oneOf) | `"Braced Non-sway"` | 可选 |
| 3 | Y 方向框架（Unbraced Sway=非侧向支撑/侧移，Braced Non-sway=侧向支撑/无侧移） | `"FRAMEY"` | String (oneOf) | `"Braced Non-sway"` | 可选 |
| 4 | 有效屈曲长度系数自动计算 | `"bAUTOKF"` | Boolean | `false` | 可选 |
| 5 | 设计类型（3D / XZ / YZ / XY 平面） | `"DT"` | String (oneOf) | `"3D"` | 可选 |

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCTL"

# 设置框架定义（PUT）：X/Y 均为侧向支撑，K 自动计算，X-Z 平面设计
payload = {
    "Assign": {
        "1": {
            "FRAMEX": "Braced Non-sway",
            "FRAMEY": "Braced Non-sway",
            "bAUTOKF": True,
            "DT": "XZ",
        }
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 3. `DESIGN/RC/KDS-41-20-2022/LLRF` — Live Load Reduction Factor (活荷载折减系数)

> **功能：** 定义按楼层、按范围的活荷载折减系数表。指定适用成分（轴力/弯矩/剪力）、计算规则与目标活荷载工况。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LLRF
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
| 1 | Assign 包装（ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 计算规则（0=一般设计代码，1=中国标准） | `"CALC_RULE"` | Integer (oneOf) | `0` | 可选 |
| 3 | 适用成分（ALL=全部，AXIAL=轴力，MOMENTS=弯矩，SHEAR=剪力） | `"APPLIED_COMP"` | Array[string] | `["AXIAL"]` | 可选 |
| 4 | 目标活荷载工况名列表 | `"LIVE_LOAD_CASES"` | Array[string] | — | 可选 |
| 5 | 活荷载折减系数表格数据 | `"REDUCTION_DATA"` | Array[object] | — | **必填** |
| 5.1 | 楼层名称 | `"STORY"` | String | — | **必填** |
| 5.2 | X 最小坐标 | `"XMIN"` | Number | `0` | 可选 |
| 5.3 | X 最大坐标 | `"XMAX"` | Number | `0` | 可选 |
| 5.4 | Y 最小坐标 | `"YMIN"` | Number | `0` | 可选 |
| 5.5 | Y 最大坐标 | `"YMAX"` | Number | `0` | 可选 |
| 5.6 | 最大值 Rmax（1~0.5，CALC_RULE=0 时） | `"RANGE_MAX"` | Number (enum) | `1` | 可选 |
| 5.7 | 最小值 Rmin（1~0.5，CALC_RULE=0 时） | `"RANGE_MIN"` | Number (enum) | `0.5` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "CALC_RULE": 0,
      "APPLIED_COMP": [
        "AXIAL"
      ],
      "LIVE_LOAD_CASES": [],
      "REDUCTION_DATA": []
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
        "AXIAL"
      ],
      "LIVE_LOAD_CASES": [],
      "REDUCTION_DATA": []
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LLRF"

# 设置活荷载折减系数（PUT）：为指定楼层范围指定折减系数范围
payload = {
    "Assign": {
        "1": {
            "CALC_RULE": 0,
            "APPLIED_COMP": ["AXIAL", "MOMENTS"],   # 施加于轴力·弯矩
            "LIVE_LOAD_CASES": ["LL"],
            "REDUCTION_DATA": [
                {"STORY": "2F", "XMIN": 0, "XMAX": 30, "YMIN": 0, "YMAX": 20,
                 "RANGE_MAX": 1, "RANGE_MIN": 0.5},
            ],
        }
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 4. `DESIGN/RC/KDS-41-20-2022/LCTB` — Load Contribution for Nonlinear Load Case (非线性荷载工况荷载贡献)

> **功能：** 查询与删除非线性分析荷载工况的荷载贡献（Load Contribution）条目。每个条目由系数与荷载工况名组成。（只读派生信息 — 仅支持 GET/DELETE）

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LCTB
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
| 1 | Assign 包装（ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 荷载贡献名称 | `"NAME"` | String | — | **必填** |
| 3 | 说明 | `"DESC"` | String | `""` | 可选 |
| 4 | 荷载贡献条目列表 | `"BASE_ITEM"` | Array[object] | — | **必填** |
| 4.1 | 系数 | `"FACTOR"` | Number | — | **必填** |
| 4.2 | 荷载工况名称 | `"LOAD_CASE_NAME"` | String | — | **必填** |

### Request / Response JSON

**GET Response Body (只读)**

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
    },
    "4": {
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
    "5": {
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
    "6": {
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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LCTB"

# LCTB 是仅支持 GET/DELETE 的只读派生信息。
# 1) 查询非线性荷载工况荷载贡献（GET）
res = requests.get(URI, headers=HEADERS)
print("GET:", res.status_code, res.json())

# 2) 全部删除（DELETE）
# print("DELETE:", requests.delete(URI, headers=HEADERS).json())
```

---

## 5. `DESIGN/RC/KDS-41-20-2022/SRDF` — Strength Reduction Factors (强度折减系数)

> **功能：** 设置受拉控制、螺旋筋构件、其他钢筋构件、剪力/扭转对应的强度折减系数 φ 值。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SRDF
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "description": "RC Strength Reduction Factors settings (KDS 41 20:2022). Supported methods: GET, PUT.",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by ID strings (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "maxProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [],
          "additionalProperties": false,
          "properties": {
            "PHI_T": {
              "type": "number",
              "description": "For Tensile Control (phi_t)",
              "default": 0.85
            },
            "PHI_C1": {
              "type": "number",
              "description": "Member with Spiral Reinforcement (phi_c1)",
              "default": 0.7
            },
            "PHI_C2": {
              "type": "number",
              "description": "Other Reinforced Member (phi_c2)",
              "default": 0.65
            },
            "PHI_V": {
              "type": "number",
              "description": "For Shear and Torsion (phi_v)",
              "default": 0.75
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
| 1 | Assign 包装（ID 字符串键，1 个） | `"Assign"` | Object | — | **必填** |
| 2 | 受拉控制 φt | `"PHI_T"` | Number | `0.85` | 可选 |
| 3 | 螺旋筋构件 φc1 | `"PHI_C1"` | Number | `0.7` | 可选 |
| 4 | 其他钢筋构件 φc2 | `"PHI_C2"` | Number | `0.65` | 可选 |
| 5 | 剪力·扭转 φv | `"PHI_V"` | Number | `0.75` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "PHI_T": 0.8,
      "PHI_C1": 0.65,
      "PHI_C2": 0.6,
      "PHI_V": 0.6
    }
  }
}
```

**GET Response Body (顶层键 `SRDFRC`)**

```json
{
  "SRDFRC": {
    "1": {
      "PHI_T": 0.8,
      "PHI_C1": 0.65,
      "PHI_C2": 0.6,
      "PHI_V": 0.6
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SRDF"

# 自定义强度折减系数 φ（PUT）
payload = {
    "Assign": {
        "1": {"PHI_T": 0.85, "PHI_C1": 0.70, "PHI_C2": 0.65, "PHI_V": 0.75}
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 6. `DESIGN/RC/KDS-41-20-2022/EQCT` — Seismic Load Combination Type (地震荷载组合类型)

> **功能：** 按构件指定采用特殊地震作用（Special Seismic Loads）或竖向地震力（Vertical Seismic Forces）的类型。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/EQCT
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 构件类型（Special Seismic Loads / Vertical Seismic Forces） | `"TYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1066": {
      "TYPE": "Special Seismic Loads"
    },
    "1067": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    },
    "1069": {
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
    "1067": {
      "TYPE": "Special Seismic Loads"
    },
    "1068": {
      "TYPE": "Vertical Seismic Forces"
    },
    "1069": {
      "TYPE": "Vertical Seismic Forces"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/EQCT"

# 按单元新增指定地震荷载组合类型（POST）
payload = {
    "Assign": {
        "1066": {"TYPE": "Special Seismic Loads"},
        "1068": {"TYPE": "Vertical Seismic Forces"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
# 修改用 PUT，删除用 DELETE
```

---

## 7. `DESIGN/RC/KDS-41-20-2022/ULCT` — Underground Load Combination Type (地下荷载组合类型)

> **功能：** 按构件指定是否应用地下（Underground）荷载组合。true=用于地下荷载，false=用于非地下荷载。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/ULCT
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 是否地下荷载（true=用于地下荷载，false=用于非地下荷载） | `"bUNDERLOADTYPE"` | Boolean (oneOf) | `false` | 可选 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/ULCT"

# 按单元指定地下荷载组合类型（POST）
payload = {
    "Assign": {
        "885": {"bUNDERLOADTYPE": True},    # 施加地下荷载
        "888": {"bUNDERLOADTYPE": False},   # 非地下荷载
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 8. `DESIGN/RC/KDS-41-20-2022/SUEQ` — Scale up Factor for Earthquake (地震放大系数)

> **功能：** 按构件指定荷载工况（LC）与荷载组合（LCOM）的轴力、弯矩、剪力各自的地震放大（Scale up）系数。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SUEQ
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 荷载工况轴力放大系数 | `"LC_AXIAL"` | Number | `1` | 可选 |
| 3 | 荷载工况弯矩放大系数 | `"LC_MOMENT"` | Number | `1` | 可选 |
| 4 | 荷载工况剪力放大系数 | `"LC_SHEAR"` | Number | `1` | 可选 |
| 5 | 荷载组合轴力放大系数 | `"LCOM_AXIAL"` | Number | `1` | 可选 |
| 6 | 荷载组合弯矩放大系数 | `"LCOM_MOMENT"` | Number | `1` | 可选 |
| 7 | 荷载组合剪力放大系数 | `"LCOM_SHEAR"` | Number | `1` | 可选 |

### Request / Response JSON

**POST Request Body**

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
    },
    "1057": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "1058": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2
    },
    "1059": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
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
    },
    "1057": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LCOM_MOMENT": 1.2,
      "LCOM_SHEAR": 1.2
    },
    "1058": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
      "LC_SHEAR": 1.2,
      "LCOM_AXIAL": 1.2
    },
    "1059": {
      "LC_AXIAL": 1.2,
      "LC_MOMENT": 1.2,
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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SUEQ"

# 按构件指定地震放大系数（POST）
payload = {
    "Assign": {
        "915": {
            "LC_AXIAL": 1.2, "LC_MOMENT": 1.2, "LC_SHEAR": 1.2,
            "LCOM_AXIAL": 1.2, "LCOM_MOMENT": 1.2, "LCOM_SHEAR": 1.2,
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 9. `DESIGN/RC/KDS-41-20-2022/SDGN` — Seismic Design Type (抗震设计类型)

> **功能：** 按构件指定抗震设计类型。在抗震（Seismic）/非抗震（Non-Seismic）/非抗震抗力体系（Non-Seismic-Force-Resisting）中选择。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SDGN
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
      "description": "Keyed object (dictionary). Each property name is a member ID string (e.g., \"1\").",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "NTYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "NTYPE": {
              "type": "string",
              "description": "Seismic design type assigned to the member.",
              "oneOf": [
                {
                  "title": "for Seismic Design",
                  "const": "Seismic"
                },
                {
                  "title": "for Non-Seismic Design",
                  "const": "Non-Seismic"
                },
                {
                  "title": "for Non-Seismic-Force Resisting System",
                  "const": "Non-Seismic-Force-Resisting"
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
| 1 | Assign 包装（构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 抗震设计类型（Seismic / Non-Seismic / Non-Seismic-Force-Resisting） | `"NTYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "NTYPE": "Seismic"
    },
    "2": {
      "NTYPE": "Non-Seismic"
    },
    "3": {
      "NTYPE": "Non-Seismic-Force-Resisting"
    }
  }
}
```

**GET Response Body**

```json
{
  "SDGN": {
    "1": {
      "NTYPE": "Seismic"
    },
    "2": {
      "NTYPE": "Non-Seismic"
    },
    "3": {
      "NTYPE": "Non-Seismic-Force-Resisting"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SDGN"

# 按构件指定抗震设计类型（POST）
payload = {
    "Assign": {
        "1": {"NTYPE": "Seismic"},
        "2": {"NTYPE": "Non-Seismic"},
        "3": {"NTYPE": "Non-Seismic-Force-Resisting"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 10. `DESIGN/RC/KDS-41-20-2022/SCOL` — Seismic Column Type (抗震柱类型)

> **功能：** 按构件（柱）指定楼层类型。归类为底层架空柱（PILOTI）或软弱层（SOFT_STORY）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/SCOL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by member ID strings (e.g., \"1059\"), where each value is a story type setting object.",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "TYPE"
          ],
          "properties": {
            "TYPE": {
              "type": "string",
              "description": "Story type classification.",
              "oneOf": [
                {
                  "title": "PILOTI",
                  "const": "PILOTI"
                },
                {
                  "title": "SOFT_STORY",
                  "const": "SOFT_STORY"
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
| 1 | Assign 包装（构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 楼层类型（PILOTI / SOFT_STORY） | `"TYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "915": {
      "TYPE": "PILOTI"
    },
    "916": {
      "TYPE": "SOFT_STORY"
    }
  }
}
```

**GET Response Body**

```json
{
  "SCOL": {
    "915": {
      "TYPE": "PILOTI"
    },
    "916": {
      "TYPE": "SOFT_STORY"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/SCOL"

# 指定柱构件的抗震楼层类型（POST）
payload = {
    "Assign": {
        "915": {"TYPE": "PILOTI"},
        "916": {"TYPE": "SOFT_STORY"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 11. `DESIGN/RC/KDS-41-20-2022/MBTP` — Modify Member Type (构件类型修改)

> **功能：** 按单元将设计构件类型修改指定为柱（COLUMN）/梁（BEAM）/支撑（BRACE）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MBTP
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 构件类型（COLUMN=柱，BEAM=梁，BRACE=支撑） | `"TYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "934": {
      "TYPE": "BRACE"
    },
    "1058": {
      "TYPE": "COLUMN"
    },
    "1059": {
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
    "1059": {
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MBTP"

# 按单元修改设计构件类型（POST）
payload = {
    "Assign": {
        "934": {"TYPE": "BRACE"},
        "1058": {"TYPE": "COLUMN"},
        "1066": {"TYPE": "BEAM"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 12. `DESIGN/RC/KDS-41-20-2022/MEMB` — Member Assignment (构件指定)

> **功能：** 将多个单元合并为一个设计构件并指定。指定单元列表以及局部坐标方向是否反向。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MEMB
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
| 1 | Assign 包装（构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 单元列表 | `"AELEM"` | Array[integer] | — | **必填** |
| 3 | 局部坐标方向反向 | `"bREVERSE"` | Boolean | `false` | 可选 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "AELEM": [
        885,
        888,
        891
      ],
      "bREVERSE": true
    },
    "2": {
      "AELEM": [
        919
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
        860,
        861,
        862,
        863,
        864
      ],
      "bREVERSE": false
    },
    "2": {
      "AELEM": [
        865,
        866
      ],
      "bREVERSE": false
    },
    "3": {
      "AELEM": [
        1020,
        1021,
        1022
      ],
      "bREVERSE": false
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MEMB"

# 将多个单元指定为一个设计构件（PUT）
payload = {
    "Assign": {
        "1": {"AELEM": [885, 888, 891], "bREVERSE": True},
        "2": {"AELEM": [919]},
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 13. `DESIGN/RC/KDS-41-20-2022/MATD` — Modify Concrete Material (混凝土材料修改)

> **功能：** 按材料 ID 修改混凝土与钢筋材料。以标准代码（Standard）或自定义（None）指定等级/强度/轻骨料系数。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MATD
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
            "CONCRETE",
            "REBAR"
          ],
          "additionalProperties": false,
          "properties": {
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
                  "description": "Concrete code type.",
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
                    {
                      "const": "C30",
                      "title": "C30"
                    },
                    {
                      "const": "C35",
                      "title": "C35"
                    },
                    {
                      "const": "C40",
                      "title": "C40"
                    },
                    {
                      "const": "C45",
                      "title": "C45"
                    },
                    {
                      "const": "C49",
                      "title": "C49"
                    },
                    {
                      "const": "C50",
                      "title": "C50"
                    },
                    {
                      "const": "C55",
                      "title": "C55"
                    },
                    {
                      "const": "C60",
                      "title": "C60"
                    },
                    {
                      "const": "C65",
                      "title": "C65"
                    },
                    {
                      "const": "C70",
                      "title": "C70"
                    },
                    {
                      "const": "C75",
                      "title": "C75"
                    },
                    {
                      "const": "C80",
                      "title": "C80"
                    },
                    {
                      "const": "C85",
                      "title": "C85"
                    },
                    {
                      "const": "C90",
                      "title": "C90"
                    },
                    {
                      "const": "C95",
                      "title": "C95"
                    }
                  ]
                },
                "FC": {
                  "type": "number",
                  "description": "Specified compressive strength (fc|fck) in kN/mm². User input when CODE is None. Auto-filled from the selected standard code and grade when CODE is Standard."
                },
                "LIGHTWEIGHT": {
                  "type": "boolean",
                  "description": "Whether the lightweight concrete factor (Lambda) is applied. Editable for both CODE=None and CODE=Standard.",
                  "default": false
                },
                "LAMBDA": {
                  "type": "number",
                  "description": "Lambda value. Editable for both CODE=None and CODE=Standard.",
                  "default": 1
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
            "REBAR": {
              "type": "object",
              "description": "Rebar material selection.",
              "required": [
                "CODE"
              ],
              "additionalProperties": false,
              "properties": {
                "CODE": {
                  "type": "string",
                  "description": "Rebar code type.",
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
                  "description": "Rebar standard code when CODE is Standard. Currently only KS19(RC) is supported.",
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
                "FY": {
                  "type": "number",
                  "description": "Yield strength Fy of main rebar in kN/mm². User input when CODE is None. Auto-filled from the selected standard code and rebar grade when CODE is Standard."
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
                  "description": "Yield strength Fys of sub-rebar in kN/mm². User input when CODE is None. Auto-filled from the selected standard code and rebar grade when CODE is Standard."
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
                      "SUB_REBAR_NAME",
                      "FY",
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

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Assign 包装（材料 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 混凝土材料 | `"CONCRETE"` | Object | — | **必填** |
| 2.1 | 代码（None=自定义，Standard=标准） | `"CODE"` | String (oneOf) | — | **必填** |
| 2.2 | 应用轻骨料混凝土系数（Lambda） | `"LIGHTWEIGHT"` | Boolean | `false` | 可选 |
| 2.3 | Lambda 值 | `"LAMBDA"` | Number | `1` | 可选 |
| 2.4 | 标准代码（KS19(RC)）— CODE=Standard | `"STANDARD_CODE"` | String (oneOf) | — | 条件必填 |
| 2.5 | 混凝土等级（C15~C95 中择一）— CODE=Standard | `"GRADE"` | String (oneOf) | — | 条件必填 |
| 2.6 | 自定义材料名 — CODE=None | `"NAME"` | String | — | 条件必填 |
| 2.7 | 设计抗压强度 fck（kN/mm²）— CODE=None 时输入/Standard 自动 | `"FC"` | Number | — | 条件必填 |
| 3 | 钢筋材料 | `"REBAR"` | Object | — | **必填** |
| 3.1 | 代码（None=自定义，Standard=标准） | `"CODE"` | String (oneOf) | — | **必填** |
| 3.2 | 标准代码（KS19(RC)）— CODE=Standard | `"STANDARD_CODE"` | String (oneOf) | — | 条件必填 |
| 3.3 | 主筋等级（SD300/SD400/SD500/SD600/SD700/SD400S/SD500S/SD600S）— Standard | `"MAIN_REBAR_GRADE"` | String (oneOf) | — | 条件必填 |
| 3.4 | 辅助钢筋等级（SD300~SD600S）— Standard | `"SUB_REBAR_GRADE"` | String (oneOf) | — | 条件必填 |
| 3.5 | 主筋材料名 — CODE=None | `"MAIN_REBAR_NAME"` | String | — | 条件必填 |
| 3.6 | 辅助钢筋材料名 — CODE=None | `"SUB_REBAR_NAME"` | String | — | 条件必填 |
| 3.7 | 主筋屈服强度 Fy（kN/mm²）— None 时输入/Standard 自动 | `"FY"` | Number | — | 条件必填 |
| 3.8 | 辅助钢筋屈服强度 Fys（kN/mm²）— None 时输入/Standard 自动 | `"FYS"` | Number | — | 条件必填 |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "CONCRETE": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C15",
        "LIGHTWEIGHT": true,
        "LAMBDA": 1
      },
      "REBAR": {
        "CODE": "Standard",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400S",
        "SUB_REBAR_GRADE": "SD600"
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "MATD": {
    "1": {
      "CONCRETE": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "GRADE": "C15",
        "LIGHTWEIGHT": true,
        "LAMBDA": 1
      },
      "REBAR": {
        "CODE": "STANDARD",
        "STANDARD_CODE": "KS19(RC)",
        "MAIN_REBAR_GRADE": "SD400S",
        "SUB_REBAR_GRADE": "SD600"
      }
    }
  }
}
```

> ⚠️ **2026-08-26 确认（article id `59398794726041`）：** GET 响应示例中的 `"CODE"` 值为
> `"STANDARD"`（大写），与 PUT 请求示例·JSON Schema 的 `oneOf`（"Standard"）大小写
> 不同 — 这是原文自身的矛盾，示例原文照原样保留。

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MATD"

# 修改材料 ID 1 的混凝土/钢筋标准材料（PUT）
payload = {
    "Assign": {
        "1": {
            "CONCRETE": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "GRADE": "C24",
                "LIGHTWEIGHT": False,
                "LAMBDA": 1,
            },
            "REBAR": {
                "CODE": "Standard",
                "STANDARD_CODE": "KS19(RC)",
                "MAIN_REBAR_GRADE": "SD400",
                "SUB_REBAR_GRADE": "SD400",
            },
        }
    }
}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```

---

## 14. `DESIGN/RC/KDS-41-20-2022/LENG` — Unbraced Length (L, Lb) (未支撑长度)

> **功能：** 按构件指定未支撑长度 Ly·Lz、侧向屈曲未支撑长度 Lb、扭转未支撑长度 Lt。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LENG
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
| 1 | Assign 包装（ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 未支撑长度 Ly | `"LY"` | Number | `0` | 可选 |
| 3 | 未支撑长度 Lz | `"LZ"` | Number | `0` | 可选 |
| 4 | 侧向屈曲未支撑长度 Lb | `"LB"` | Number | `0` | 可选 |
| 5 | 不考虑侧向屈曲未支撑长度 | `"bNOTUSE"` | Boolean | `false` | 可选 |
| 6 | 扭转未支撑长度 Lt | `"LT"` | Number | `0` | 可选 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LENG"

# 按构件指定未支撑长度（POST）
payload = {
    "Assign": {
        "888": {"LY": 3.0, "LZ": 3.0, "LB": 3.0, "bNOTUSE": False, "LT": 3.0},
        "891": {"LY": 4.0, "LZ": 4.0, "LB": 2.0},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 15. `DESIGN/RC/KDS-41-20-2022/KFAC` — Effective Length Factor (K) (有效屈曲长度系数)

> **功能：** 按构件指定有效屈曲长度系数 Ky·Kz·Kt。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/KFAC
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | Ky | `"Ky"` | Number | `1` | 可选 |
| 3 | Kz | `"Kz"` | Number | `1` | 可选 |
| 4 | Kt | `"Kt"` | Number | `1` | 可选 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/KFAC"

# 按构件指定有效屈曲长度系数 K（POST）
payload = {
    "Assign": {
        "859": {"Ky": 1.0},
        "860": {"Ky": 2.0, "Kz": 2.0},
        "902": {"Kz": 3.0, "Kt": 3.0},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 16. `DESIGN/RC/KDS-41-20-2022/CMFT` — Equivalent Moment Correction Factor(Cm) (等效弯矩校正系数)

> **功能：** 按构件指定等效弯矩校正系数 CMy·CMz，或选择自动计算（OPT_AUTO）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/CMFT
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 自动计算 | `"OPT_AUTO"` | Boolean | `false` | 可选 |
| 3 | CMy | `"CMY"` | Number | `0` | 可选 |
| 4 | CMz | `"CMZ"` | Number | `0` | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1067": {
      "OPT_AUTO": true
    },
    "1068": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    },
    "1071": {
      "CMY": 0.8,
      "CMZ": 0.8
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
    "1068": {
      "OPT_AUTO": true
    },
    "1069": {
      "CMY": 0.7,
      "CMZ": 0.6
    },
    "1070": {
      "CMY": 0.72,
      "CMZ": 0.85
    },
    "1071": {
      "CMY": 0.8,
      "CMZ": 0.8
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CMFT"

# 指定等效弯矩校正系数 Cm（POST）：部分自动、部分使用手动值
payload = {
    "Assign": {
        "1067": {"OPT_AUTO": True},              # 自动计算
        "1069": {"CMY": 0.7, "CMZ": 0.6},        # 手动输入
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 17. `DESIGN/RC/KDS-41-20-2022/FMAG` — Moment Magnifier(B1/Delta_b, B2/Delta_s) (弯矩放大系数)

> **功能：** 按构件指定弯矩放大系数。B1(δb) 针对一次（无侧移）弯矩，B2(δs) 针对二次（有侧移）弯矩。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/FMAG
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | B1y - δby（Y 轴一次弯矩放大） | `"B1Y_DELTA_BY"` | Number | `1` | 可选 |
| 3 | B1z - δbz（Z 轴一次弯矩放大） | `"B1Z_DELTA_BZ"` | Number | `1` | 可选 |
| 4 | B2y - δsy（Y 轴二次弯矩放大） | `"B2Y_DELTA_SY"` | Number | `1` | 可选 |
| 5 | B2z - δsz（Z 轴二次弯矩放大） | `"B2Z_DELTA_SZ"` | Number | `1` | 可选 |

### Request / Response JSON

**POST Request Body**

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
    },
    "1059": {
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3
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
    },
    "1059": {
      "B1Y_DELTA_BY": 1,
      "B1Z_DELTA_BZ": 1.2,
      "B2Y_DELTA_SY": 1.3,
      "B2Z_DELTA_SZ": 1
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/FMAG"

# 按构件指定弯矩放大系数（POST）
payload = {
    "Assign": {
        "915": {"B1Y_DELTA_BY": 1.1, "B1Z_DELTA_BZ": 1.2},
        "1058": {"B2Y_DELTA_SY": 1.3, "B2Z_DELTA_SZ": 1.4},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 18. `DESIGN/RC/KDS-41-20-2022/MLLR` — Modify Live Load Reduction Factor (活荷载折减系数修改)

> **功能：** 按构件单独修改活荷载折减系数及适用成分（轴力/弯矩/剪力）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MLLR
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
| 1 | Assign 包装（单元 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 折减系数（≥0.3，≤1） | `"FACTOR"` | Number | `1` | 可选 |
| 3 | 适用成分 | `"COMPONENTS"` | Object | — | 可选 |
| 3.1 | 轴力 | `"AXIAL"` | Boolean | `false` | 可选 |
| 3.2 | 弯矩 | `"MOMENT"` | Boolean | `false` | 可选 |
| 3.3 | 剪力 | `"SHEAR"` | Boolean | `false` | 可选 |

### Request / Response JSON

**POST Request Body**

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
    },
    "1057": {
      "FACTOR": null,
      "COMPONENTS": {
        "MOMENT": true
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
    },
    "1057": {
      "COMPONENTS": {
        "MOMENT": true
      }
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MLLR"

# 按构件修改活荷载折减系数（POST）
payload = {
    "Assign": {
        "922": {"COMPONENTS": {"AXIAL": False, "MOMENT": True, "SHEAR": False}},
        "934": {"FACTOR": 0.9, "COMPONENTS": {"AXIAL": True}},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 19. `DESIGN/RC/KDS-41-20-2022/HCBM` — Haunched Beam Assignment (加腋梁指定)

> **功能：** 以 Part A/B/C 的单元组成指定加腋梁（Haunched Beam）。各部分可用单元 ID 列表（KEYS）或 ID 范围（TO）指定，并选择设计位置类型（Part 1/2 或 User）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/HCBM
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
| 1 | Assign 包装（ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 加腋名称 | `"NAME"` | String | — | **必填** |
| 3 | Part A 单元输入（仅使用 1 种方式） | `"PART_A"` | Object | — | **必填** |
| 3.1 | 输入方式（KEYS=逐个 ID，TO=ID 范围） | `"INPUT_METHOD"` | String (oneOf) | — | **必填** |
| 3.2 | 逐个单元 ID（INPUT_METHOD=KEYS，最少 1 个） | `"KEYS"` | Array[integer] | — | 条件 |
| 3.3 | ID 范围（例 "101 to 105"）（INPUT_METHOD=TO） | `"TO"` | String | — | 条件 |
| 4 | Part B 单元输入（结构与 Part A 相同） | `"PART_B"` | Object | — | **必填** |
| 5 | Part C 单元输入（结构与 Part A 相同） | `"PART_C"` | Object | — | **必填** |
| 6 | 设计位置类型（0=Part 1/2，1=User） | `"POS_TYPE"` | Integer (oneOf) | — | **必填** |
| 7 | 用户自定义 L1 距离（POS_TYPE=1 时） | `"L1"` | Number | `1` | 可选 |
| 8 | 用户自定义 L2 距离（POS_TYPE=1 时） | `"L2"` | Number | `1` | 可选 |

### Request / Response JSON

**POST Request Body**

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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/HCBM"

# 指定加腋梁（POST）：Part A=逐个 ID，Part B=范围，Part C=逐个 ID
payload = {
    "Assign": {
        "1": {
            "NAME": "h1",
            "POS_TYPE": 0,                       # Part 1/2 自动位置
            "PART_A": {"INPUT_METHOD": "KEYS", "KEYS": [1065]},
            "PART_B": {"INPUT_METHOD": "TO", "TO": "1066to1071"},
            "PART_C": {"INPUT_METHOD": "KEYS", "KEYS": [1072]},
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 20. `DESIGN/RC/KDS-41-20-2022/MRFT` — Moment Redistribution Factor (弯矩重分布系数)

> **功能：** 按梁构件指定弯矩重分布系数。仅适用于梁（Beam）构件类型。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MRFT
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "description": "Design Parameters - Moment Redistribution Factor (MRFT). Only Beam Member Type is applicable. Supported methods: POST, GET, PUT, DELETE.",
  "required": [
    "Assign"
  ],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by beam member ID strings (e.g., \"859\"), where each entry represents a moment redistribution factor assigned to the member. Only Beam Member Type is applicable.",
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
              "description": "Moment redistribution factor assigned to the member.",
              "default": 1,
              "exclusiveMinimum": 0,
              "maximum": 1
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
| 1 | Assign 包装（梁构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 弯矩重分布系数（>0，≤1） | `"FACTOR"` | Number | `1` | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "885": {
      "FACTOR": 1
    },
    "888": {
      "FACTOR": 0.01
    }
  }
}
```

**GET Response Body**

```json
{
  "MRFT": {
    "885": {
      "FACTOR": 1
    },
    "888": {
      "FACTOR": 0.01
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MRFT"

# 按梁构件指定弯矩重分布系数（POST）— 仅 Beam 类型有效
payload = {
    "Assign": {
        "885": {"FACTOR": 1.0},
        "888": {"FACTOR": 0.9},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 21. `DESIGN/RC/KDS-41-20-2022/TRFT` — Torsion Reduction Factor (扭转折减系数)

> **功能：** 按梁构件指定扭转折减系数。仅适用于梁（Beam）构件类型。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/TRFT
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
      "description": "Object keyed by beam member ID strings (e.g., \"859\"), where each entry assigns a torsion reduction factor. Only Beam Member Type is applicable.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "FACTOR"
          ],
          "additionalProperties": false,
          "properties": {
            "FACTOR": {
              "type": "number",
              "description": "Torsion reduction factor applied to the member.",
              "default": 1,
              "exclusiveMinimum": 0,
              "maximum": 1
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
| 1 | Assign 包装（梁构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 扭转折减系数（>0，≤1） | `"FACTOR"` | Number | `1` | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "888": {
      "FACTOR": 1
    }
  }
}
```

**GET Response Body**

```json
{
  "TRFT": {
    "888": {
      "FACTOR": 1
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TRFT"

# 按梁构件指定扭转折减系数（POST）
payload = {"Assign": {"888": {"FACTOR": 1.0}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
# 修改：requests.put(...) / 删除：requests.delete(...)
```

---

## 22. `DESIGN/RC/KDS-41-20-2022/MCMB` — Moment Calculation Method for Beam (梁弯矩计算方法)

> **功能：** 按梁构件指定弯矩计算方法。在 Each（各跨）与 Equivalent Frame（等效框架）中选择。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/MCMB
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
      "description": "Object keyed by member ID strings (e.g., \"1\"), where each entry represents the moment calculation method assigned to the beam member.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "CALC_METHOD"
          ],
          "additionalProperties": false,
          "properties": {
            "CALC_METHOD": {
              "type": "string",
              "description": "Moment calculation method for the beam member.",
              "oneOf": [
                {
                  "title": "Each Span",
                  "const": "EACH"
                },
                {
                  "title": "Equivalent Frame",
                  "const": "EQUI"
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
| 1 | Assign 包装（构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 弯矩计算方法（EACH=各跨，EQUI=等效框架） | `"CALC_METHOD"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "888": {
      "CALC_METHOD": "EACH"
    }
  }
}
```

**GET Response Body**

```json
{
  "MCMB": {
    "888": {
      "CALC_METHOD": "EACH"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/MCMB"

# 按梁构件指定弯矩计算方法（POST）
payload = {"Assign": {"888": {"CALC_METHOD": "EACH"}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 23. `DESIGN/RC/KDS-41-20-2022/DFBA` — Design Force for Beam Assigned as Member (构件指定梁的设计内力)

> **功能：** 指定已作为构件指定的梁的设计内力类型。在 Subdivided Forces（细分构件内力）与 Member Forces（构件内力）中选择。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DFBA
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
      "description": "Object keyed by member ID strings (e.g., \"1\"), where each entry represents the design force type assigned to the beam member.",
      "additionalProperties": false,
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "FORCE_TYPE"
          ],
          "additionalProperties": false,
          "properties": {
            "FORCE_TYPE": {
              "type": "string",
              "description": "Design force type for the beam member.",
              "oneOf": [
                {
                  "title": "Subdivided Forces",
                  "const": "Subdivided Forces"
                },
                {
                  "title": "Member Forces",
                  "const": "Member Forces"
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
| 1 | Assign 包装（构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 设计内力类型（Subdivided Forces / Member Forces） | `"FORCE_TYPE"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "859": {
      "FORCE_TYPE": "Subdivided Forces"
    },
    "860": {
      "FORCE_TYPE": "Member Forces"
    }
  }
}
```

**GET Response Body**

```json
{
  "DFBA": {
    "859": {
      "FORCE_TYPE": "Subdivided Forces"
    },
    "860": {
      "FORCE_TYPE": "Member Forces"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DFBA"

# 指定已作为构件指定的梁的设计内力类型（POST）
payload = {
    "Assign": {
        "859": {"FORCE_TYPE": "Subdivided Forces"},
        "860": {"FORCE_TYPE": "Member Forces"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 24. `DESIGN/RC/KDS-41-20-2022/PMDM` — P-M Curve Calculation Method (P-M 曲线计算方法)

> **功能：** 按构件指定 P-M 相关（interaction）设计的计算方法。在 P（固定轴力）与 M/P（固定弯矩/轴力比）中选择。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/PMDM
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by member ID strings (e.g., \"1059\"), where each value is a PMDM setting object.",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "CALC_METHOD"
          ],
          "properties": {
            "CALC_METHOD": {
              "type": "string",
              "description": "Calculation method for PM interaction design.",
              "oneOf": [
                {
                  "title": "P",
                  "const": "P"
                },
                {
                  "title": "M/P",
                  "const": "M/P"
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
| 1 | Assign 包装（构件 ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 计算方法（P=固定轴力，M/P=固定 M·P 比） | `"CALC_METHOD"` | String (oneOf) | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "915": {
      "CALC_METHOD": "P"
    }
  }
}
```

**GET Response Body**

```json
{
  "PMDM": {
    "915": {
      "CALC_METHOD": "P"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/PMDM"

# 按构件指定 P-M 曲线计算方法（POST）
payload = {"Assign": {"915": {"CALC_METHOD": "P"}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 25. `DESIGN/RC/KDS-41-20-2022/WMAK` — Modify Wall Mark Data (墙体标识数据修改)

> **功能：** 定义墙体标识（Wall Mark）。指定标识名称与目标墙体 ID 列表。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/WMAK
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "title": "Modify Wall Mark Data (WMAK)",
  "description": "POST /DESIGN/RC/KDS-41-20-2022/WMAK — Design Parameters - Modify Wall Mark Data",
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
          "title": "Modify Wall Mark Data",
          "type": "object",
          "required": [
            "MARKNAME",
            "WID_LIST"
          ],
          "additionalProperties": false,
          "properties": {
            "MARKNAME": {
              "type": "string",
              "description": "Wall mark name",
              "minLength": 1
            },
            "WID_LIST": {
              "type": "array",
              "description": "Target wall IDs",
              "items": {
                "type": "integer"
              },
              "minItems": 1
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
| 2 | 墙体标识名称（最少 1 个字符） | `"MARKNAME"` | String | — | **必填** |
| 3 | 目标墙体 ID 列表（最少 1 个） | `"WID_LIST"` | Array[integer] | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "MARKNAME": "W200",
      "WID_LIST": [
        1,
        2
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "WMAK": {
    "1": {
      "MARKNAME": "W200",
      "WID_LIST": [
        1,
        2
      ]
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WMAK"

# 定义墙体标识（POST）：将墙体 1、2 归入标识 "W200"
payload = {"Assign": {"1": {"MARKNAME": "W200", "WID_LIST": [1, 2]}}}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 26. `DESIGN/RC/KDS-41-20-2022/BEMW` — Boundary Element Method by Wall ID (按墙体ID的边缘构件法)

> **功能：** 设置按墙体是否使用边缘构件法（Boundary Element Method）及其方式（位移/应力基准）、是否设置最底层以及楼层名称。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/BEMW
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Object keyed by index strings (e.g., \"1\"), where each value is a boundary element wall setting object.",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BBNDR_ELEM_METHOD": {
              "type": "boolean",
              "description": "Whether to use boundary element method."
            },
            "NMETHOD_TYPE": {
              "type": "string",
              "description": "Boundary element method type.",
              "oneOf": [
                {
                  "title": "Displacement Based Method",
                  "const": "Displacement Based Method"
                },
                {
                  "title": "Stress Based Method",
                  "const": "Stress Based Method"
                }
              ]
            },
            "BBOT_STOR": {
              "type": "boolean",
              "description": "Whether to use bottom story setting."
            },
            "STOR_NAME": {
              "type": "string",
              "description": "Story name."
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
| 1 | Assign 包装（索引字符串键，1 个） | `"Assign"` | Object | — | **必填** |
| 2 | 是否使用边缘构件法 | `"BBNDR_ELEM_METHOD"` | Boolean | — | 可选 |
| 3 | 是否使用最底层设置 | `"BBOT_STOR"` | Boolean | — | 可选 |
| 4 | 方式类型（Displacement Based Method / Stress Based Method）— BBNDR_ELEM_METHOD=true | `"NMETHOD_TYPE"` | String (oneOf) | — | 可选 |
| 5 | 楼层名称（BBOT_STOR=true 时） | `"STOR_NAME"` | String | — | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "1": {
      "NMETHOD_TYPE": "Displacement Based Method",
      "BBNDR_ELEM_METHOD": true,
      "BBOT_STOR": true,
      "STOR_NAME": "B2"
    }
  }
}
```

**GET Response Body**

```json
{
  "BEMW": {
    "1": {
      "BBNDR_ELEM_METHOD": true,
      "NMETHOD_TYPE": "Displacement Based Method",
      "BBOT_STOR": true,
      "STOR_NAME": "B2"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BEMW"

# 设置按墙体的边缘构件法（POST）：位移基准，最底层 B2
payload = {
    "Assign": {
        "1": {
            "BBNDR_ELEM_METHOD": True,
            "NMETHOD_TYPE": "Displacement Based Method",
            "BBOT_STOR": True,
            "STOR_NAME": "B2",
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 27. `DESIGN/RC/KDS-41-20-2022/REXC` — Rebar Exposure Condition (钢筋暴露条件)

> **功能：** 按构件指定钢筋暴露条件（Rebar Exposure Condition）。在 Dry（干燥）与 Etc（其他）中选择。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REXC
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
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": [
            "EXPOSURE"
          ],
          "additionalProperties": false,
          "properties": {
            "EXPOSURE": {
              "type": "string",
              "description": "Rebar exposure condition.",
              "default": "Dry",
              "oneOf": [
                {
                  "const": "Etc",
                  "title": "Etc"
                },
                {
                  "const": "Dry",
                  "title": "Dry"
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
| 1 | Assign 包装（ID 字符串键） | `"Assign"` | Object | — | **必填** |
| 2 | 暴露条件（Dry=干燥，Etc=其他） | `"EXPOSURE"` | String (oneOf) | `"Dry"` | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Assign": {
    "17": {
      "EXPOSURE": "Dry"
    },
    "49": {
      "EXPOSURE": "Etc"
    }
  }
}
```

**GET Response Body**

```json
{
  "REXC": {
    "17": {
      "EXPOSURE": "Dry"
    },
    "49": {
      "EXPOSURE": "Etc"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REXC"

# 按构件指定钢筋暴露条件（POST）
payload = {
    "Assign": {
        "17": {"EXPOSURE": "Dry"},
        "49": {"EXPOSURE": "Etc"},
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).json())
print("GET :", requests.get(URI, headers=HEADERS).json())
```

---

## 28. `DESIGN/RC/KDS-41-20-2022/LMRR` — Limiting Maximum Rebar Ratio (最大配筋率限制)

> **功能：** 设置各设计的最大配筋率上限。分别指定剪力墙（Rhow）、柱（Rhoc）、支撑（Rhor）的最大配筋率。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/LMRR
```

### Active Methods

`GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "Assign"
  ],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "Keyed object (dictionary). Each property name is an ID string (e.g., \"1\").",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "RHOR",
            "RHOC",
            "RHOW"
          ],
          "properties": {
            "RHOW": {
              "type": "number",
              "description": "Maximum rebar ratio for Shear Wall Design (Rhow)."
            },
            "RHOC": {
              "type": "number",
              "description": "Maximum rebar ratio for Column Design (Rhoc)."
            },
            "RHOR": {
              "type": "number",
              "description": "Maximum rebar ratio for Brace Design (Rhor)."
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
| 1 | Assign 包装（ID 字符串键，1 个） | `"Assign"` | Object | — | **必填** |
| 2 | 剪力墙设计最大配筋率 Rhow | `"RHOW"` | Number | — | **必填** |
| 3 | 柱设计最大配筋率 Rhoc | `"RHOC"` | Number | — | **必填** |
| 4 | 支撑设计最大配筋率 Rhor | `"RHOR"` | Number | — | **必填** |

### Request / Response JSON

**PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "RHOW": 0.04,
      "RHOC": 0.03,
      "RHOR": 0.03
    }
  }
}
```

**GET Response Body**

```json
{
  "LMRR": {
    "1": {
      "RHOR": 0.03,
      "RHOC": 0.03,
      "RHOW": 0.04
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/LMRR"

# 设置最大配筋率限制（PUT）
payload = {"Assign": {"1": {"RHOW": 0.04, "RHOC": 0.03, "RHOR": 0.03}}}
print("PUT:", requests.put(URI, headers=HEADERS, json=payload).json())
print("GET:", requests.get(URI, headers=HEADERS).json())
```



---

## 29. `DESIGN/RC/KDS-41-20-2022/DCRM-BEAM` — Design Criteria for Rebars by Beam Member (按梁构件的钢筋设计准则)

> **功能：** 按梁（Beam）**构件 ID** 单独指定钢筋设计准则（主筋·箍筋·肢数·侧面钢筋·保护层·双排钢筋·间距限制·搭接）。用于将全局准则（`DCRE`）覆盖到特定构件。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-BEAM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 规格/数组 enum 的重复取值很多，已作缩略。实际 schema 中钢筋规格为 `oneOf`（title=const）形式的 **19 种（D4 ~ D57）**，箍筋肢数则为 **19 种（2 ~ 20）** 全部列出。下面的 `enum` 仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "부재 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "보 부재별 철근 규격·배근",
          "required": ["MAIN_REBAR", "STIRRUPS", "STIRRUP_ARRANGEMENT", "SIDE_BAR"],
          "additionalProperties": false,
          "properties": {
            "MAIN_REBAR": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "STIRRUPS": { "type": "string", "description": "스터럽(전단철근) 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "STIRRUP_ARRANGEMENT": { "type": "integer", "description": "스터럽 다리(leg) 수 (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "SIDE_BAR": { "type": "string", "description": "측면철근(side bar) 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "DT": { "type": "number", "description": "상단 피복 거리 dT", "default": 0 },
            "DB": { "type": "number", "description": "하단 피복 거리 dB", "default": 0 },
            "DOUBLY_REBAR": { "type": "boolean", "description": "복철근 설계 사용", "default": true },
            "DOUBLY_K": { "type": "number", "description": "복철근 k 계수", "default": 1 },
            "SPACING_LIMIT": { "type": "boolean", "description": "철근 간격 제한 고려", "default": true },
            "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
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
| 1 | 以构件 ID 字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 主筋规格 · 19 种（D4 ~ D57） | `"MAIN_REBAR"` | String (enum) | — | **必填** |
| 3 | 箍筋（抗剪钢筋）规格 · 19 种（D4 ~ D57） | `"STIRRUPS"` | String (enum) | — | **必填** |
| 4 | 箍筋肢数 · 2 ~ 20 | `"STIRRUP_ARRANGEMENT"` | Integer (enum) | — | **必填** |
| 5 | 侧面钢筋规格 · 19 种（D4 ~ D57） | `"SIDE_BAR"` | String (enum) | — | **必填** |
| 6 | 顶部保护层距离 dT | `"DT"` | Number | `0` | 可选 |
| 7 | 底部保护层距离 dB | `"DB"` | Number | `0` | 可选 |
| 8 | 使用双排钢筋设计 | `"DOUBLY_REBAR"` | Boolean | `true` | 可选 |
| 9 | 双排钢筋 k 系数 | `"DOUBLY_K"` | Number | `1` | 可选 |
| 10 | 考虑钢筋间距限制 | `"SPACING_LIMIT"` | Boolean | `true` | 可选 |
| 11 | 搭接选项（`None` \| `50%` \| `100%`） | `"SPLICED_BARS"` | String (enum) | `"50%"` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "885": {
      "MAIN_REBAR": "D4",
      "STIRRUPS": "D4",
      "STIRRUP_ARRANGEMENT": 4,
      "SIDE_BAR": "D4",
      "DT": 0.05,
      "DB": 0.05,
      "DOUBLY_REBAR": true,
      "DOUBLY_K": 1,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMB": {
    "885": {
      "MAIN_REBAR": "D4",
      "STIRRUPS": "D4",
      "STIRRUP_ARRANGEMENT": 4,
      "SIDE_BAR": "D4",
      "DT": 0.05,
      "DB": 0.05,
      "DOUBLY_REBAR": true,
      "DOUBLY_K": 1,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-BEAM"

# 1) 指定梁构件 885 的钢筋准则（POST）
payload = {
    "Assign": {
        "885": {
            "MAIN_REBAR": "D22",          # 主筋规格
            "STIRRUPS": "D10",            # 箍筋规格
            "STIRRUP_ARRANGEMENT": 4,     # 箍筋肢数
            "SIDE_BAR": "D13",            # 侧面钢筋规格
            "DT": 0.05, "DB": 0.05,       # 上、下保护层
            "DOUBLY_REBAR": True, "DOUBLY_K": 1,
            "SPACING_LIMIT": True,
            "SPLICED_BARS": "50%",        # 搭接选项
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)

# 2) 查询（GET）→ 顶层键为 "DCRMB"
print("GET:", requests.get(URI, headers=HEADERS).json())

# 3) 修改（PUT）/ 删除（DELETE）
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 30. `DESIGN/RC/KDS-41-20-2022/DCRM-COLUMN` — Design Criteria for Rebars by Column Member (按柱构件的钢筋设计准则)

> **功能：** 按柱（Column）**构件 ID** 单独指定钢筋设计准则（主筋·箍筋/螺旋箍筋·Y/Z 方向肢数·保护层·间距限制·搭接）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-COLUMN
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 钢筋规格 enum 为 **19 种（D4 ~ D57）**，肢数 enum 为 **19 种（2 ~ 20）** 全部列出，下面仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "부재 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "기둥 부재별 철근 규격·배근",
          "required": ["MAIN_REBAR", "TIES_SPIRALS", "ARRANGEMENT_Y", "ARRANGEMENT_Z"],
          "additionalProperties": false,
          "properties": {
            "MAIN_REBAR": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "ARRANGEMENT_Y": { "type": "integer", "description": "띠철근 다리 수 (local Y) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "ARRANGEMENT_Z": { "type": "integer", "description": "띠철근 다리 수 (local Z) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "DO": { "type": "number", "description": "주철근 중심까지 피복 거리 do", "default": 0 },
            "SPACING_LIMIT": { "type": "boolean", "description": "철근 간격 제한 고려", "default": true },
            "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
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
| 1 | 以构件 ID 字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 主筋规格 · 19 种（D4 ~ D57） | `"MAIN_REBAR"` | String (enum) | — | **必填** |
| 3 | 箍筋/螺旋箍筋规格 · 19 种（D4 ~ D57） | `"TIES_SPIRALS"` | String (enum) | — | **必填** |
| 4 | 箍筋肢数（local Y）· 2 ~ 20 | `"ARRANGEMENT_Y"` | Integer (enum) | — | **必填** |
| 5 | 箍筋肢数（local Z）· 2 ~ 20 | `"ARRANGEMENT_Z"` | Integer (enum) | — | **必填** |
| 6 | 至主筋中心的保护层距离 do | `"DO"` | Number | `0` | 可选 |
| 7 | 考虑钢筋间距限制 | `"SPACING_LIMIT"` | Boolean | `true` | 可选 |
| 8 | 搭接选项（`None` \| `50%` \| `100%`） | `"SPLICED_BARS"` | String (enum) | `"50%"` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "915": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "DO": 0.05,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMC": {
    "915": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "DO": 0.05,
      "SPACING_LIMIT": true,
      "SPLICED_BARS": "50%"
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-COLUMN"

# 指定柱构件 915 的钢筋准则（POST）
payload = {
    "Assign": {
        "915": {
            "MAIN_REBAR": "D22",
            "TIES_SPIRALS": "D10",
            "ARRANGEMENT_Y": 3,   # Y 方向箍筋肢数
            "ARRANGEMENT_Z": 3,   # Z 方向箍筋肢数
            "DO": 0.05,
            "SPACING_LIMIT": True,
            "SPLICED_BARS": "50%",
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "DCRMC"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 31. `DESIGN/RC/KDS-41-20-2022/DCRM-BRACE` — Design Criteria for Rebars by Brace Member (按支撑构件的钢筋设计准则)

> **功能：** 按支撑（Brace）**构件 ID** 指定钢筋设计准则。字段构成与柱（`DCRM-COLUMN`）相同（主筋·箍筋·Y/Z 肢数·保护层·间距限制·搭接）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-BRACE
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 钢筋规格 enum 为 **19 种（D4 ~ D57）**，肢数 enum 为 **19 种（2 ~ 20）**，下面仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "부재 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "가새 부재별 철근 규격·배근",
          "required": ["MAIN_REBAR", "TIES_SPIRALS", "ARRANGEMENT_Y", "ARRANGEMENT_Z"],
          "additionalProperties": false,
          "properties": {
            "MAIN_REBAR": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
            "ARRANGEMENT_Y": { "type": "integer", "description": "띠철근 다리 수 (local Y) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "ARRANGEMENT_Z": { "type": "integer", "description": "띠철근 다리 수 (local Z) (전체 19종: 2 ~ 20)", "enum": [2, 3, 4, 5, 6] },
            "DO": { "type": "number", "description": "주철근 중심까지 피복 거리 do", "default": 0 },
            "SPACING_LIMIT": { "type": "boolean", "description": "철근 간격 제한 고려", "default": true },
            "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
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
| 1 | 以构件 ID 字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 主筋规格 · 19 种（D4 ~ D57） | `"MAIN_REBAR"` | String (enum) | — | **必填** |
| 3 | 箍筋/螺旋箍筋规格 · 19 种（D4 ~ D57） | `"TIES_SPIRALS"` | String (enum) | — | **必填** |
| 4 | 箍筋肢数（local Y）· 2 ~ 20 | `"ARRANGEMENT_Y"` | Integer (enum) | — | **必填** |
| 5 | 箍筋肢数（local Z）· 2 ~ 20 | `"ARRANGEMENT_Z"` | Integer (enum) | — | **必填** |
| 6 | 至主筋中心的保护层距离 do | `"DO"` | Number | `0` | 可选 |
| 7 | 考虑钢筋间距限制 | `"SPACING_LIMIT"` | Boolean | `true` | 可选 |
| 8 | 搭接选项（`None` \| `50%` \| `100%`） | `"SPLICED_BARS"` | String (enum) | `"50%"` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "934": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "SPLICED_BARS": "50%",
      "DO": 0.05,
      "SPACING_LIMIT": true
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMR": {
    "934": {
      "MAIN_REBAR": "D4",
      "TIES_SPIRALS": "D4",
      "ARRANGEMENT_Y": 2,
      "ARRANGEMENT_Z": 2,
      "SPLICED_BARS": "50%",
      "DO": 0.05,
      "SPACING_LIMIT": true
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-BRACE"

# 指定支撑构件 934 的钢筋准则（POST）
payload = {
    "Assign": {
        "934": {
            "MAIN_REBAR": "D22",
            "TIES_SPIRALS": "D10",
            "ARRANGEMENT_Y": 2,
            "ARRANGEMENT_Z": 2,
            "DO": 0.05,
            "SPACING_LIMIT": True,
            "SPLICED_BARS": "50%",
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "DCRMR"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 32. `DESIGN/RC/KDS-41-20-2022/DCRM-WALL` — Design Criteria for Rebars by Wall Member (按墙体构件的钢筋设计准则)

> **功能：** 按墙体（Wall）**ID** 以及各 ID 内的**楼层（Story）** 单独指定钢筋设计准则（垂直·水平·端部钢筋，边缘构件水平钢筋，边缘构件水平/垂直间距，保护层 de/dw）。每个墙体 ID 拥有一个楼层条目数组 `"ITEMS"`，数组中的每一项同时包含楼层名称（`"STORY"`）与该层的钢筋规格字段。
>
> ℹ️ **2026-07-21 反映（结构变更）：** 官方手册 schema 由每个墙体 ID 对应单一钢筋规格对象（扁平结构：`Assign.{墙体ID}.{VERTICAL_REBAR, HORIZONTAL_REBAR, END_REBAR, BE_HORZ_REBAR, BE_HORZ_SPACE, BE_VERT_SPACE, DE, DW}`）变更为**楼层条目数组** `Assign.{墙体ID}.ITEMS[]` 结构。`ITEMS` 是墙体 ID 下新增的必填键，数组中的每一项连同新增必填字段 `"STORY"`（字符串）一起，把原有钢筋/间距字段包含在条目内部。原扁平结构已不再有效，若以此前的结构编写过对接代码则必须更新。GET 响应的顶层键（`"DCRMW"`）与 Active Methods（POST/GET/PUT/DELETE）未变更。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRM-WALL
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 钢筋规格 enum 为 **19 种（D4 ~ D57）**，下面仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "벽체 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "description": "벽체별 층(Story)별 배근 지정",
          "required": ["ITEMS"],
          "additionalProperties": false,
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "해당 벽체 ID의 층별 지정 목록",
              "minItems": 1,
              "items": {
                "type": "object",
                "description": "층별 벽체 철근 규격·배근",
                "required": ["STORY", "VERTICAL_REBAR", "HORIZONTAL_REBAR", "END_REBAR", "BE_HORZ_REBAR", "BE_HORZ_SPACE", "BE_VERT_SPACE"],
                "additionalProperties": false,
                "properties": {
                  "STORY": { "type": "string", "description": "층 이름", "minLength": 1 },
                  "VERTICAL_REBAR": { "type": "string", "description": "수직 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "HORIZONTAL_REBAR": { "type": "string", "description": "수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "END_REBAR": { "type": "string", "description": "단부 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "BE_HORZ_REBAR": { "type": "string", "description": "경계요소 수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                  "BE_HORZ_SPACE": { "type": "number", "description": "경계요소 수평 철근 간격" },
                  "BE_VERT_SPACE": { "type": "number", "description": "경계요소 수직 철근 간격" },
                  "DE": { "type": "number", "description": "단부 피복 거리 de (m)", "default": 0 },
                  "DW": { "type": "number", "description": "벽면 피복 거리 dw (m)", "default": 0 }
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
| --- | --- | --- | --- | --- | --- |
| 1 | 以墙体 ID 字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 该墙体 ID 的楼层指定列表（min 1） | `"ITEMS"` | Array[Object] | — | **必填** |

**`ITEMS` 数组条目（按楼层配筋指定）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| a | 楼层名称（最少 1 个字符） | `"STORY"` | String | — | **必填** |
| b | 垂直钢筋规格 · 19 种（D4 ~ D57） | `"VERTICAL_REBAR"` | String (enum) | — | **必填** |
| c | 水平钢筋规格 · 19 种（D4 ~ D57） | `"HORIZONTAL_REBAR"` | String (enum) | — | **必填** |
| d | 端部钢筋规格 · 19 种（D4 ~ D57） | `"END_REBAR"` | String (enum) | — | **必填** |
| e | 边缘构件水平钢筋规格 · 19 种（D4 ~ D57） | `"BE_HORZ_REBAR"` | String (enum) | — | **必填** |
| f | 边缘构件水平钢筋间距 | `"BE_HORZ_SPACE"` | Number | — | **必填** |
| g | 边缘构件垂直钢筋间距 | `"BE_VERT_SPACE"` | Number | — | **必填** |
| h | 端部保护层距离 de（m） | `"DE"` | Number | `0` | 可选 |
| i | 墙面保护层距离 dw（m） | `"DW"` | Number | `0` | 可选 |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "3": {
      "ITEMS": [
        {
          "STORY": "1F",
          "VERTICAL_REBAR": "D22",
          "HORIZONTAL_REBAR": "D32",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        },
        {
          "STORY": "B1",
          "VERTICAL_REBAR": "D4",
          "HORIZONTAL_REBAR": "D10",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        }
      ]
    },
    "14": {
      "ITEMS": [
        {
          "STORY": "1F",
          "VERTICAL_REBAR": "D25",
          "HORIZONTAL_REBAR": "D32",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        },
        {
          "STORY": "B1",
          "VERTICAL_REBAR": "D4",
          "HORIZONTAL_REBAR": "D32",
          "END_REBAR": "D41",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRMW": {
    "3": {
      "ITEMS": [
        {
          "STORY": "1F",
          "VERTICAL_REBAR": "D22",
          "HORIZONTAL_REBAR": "D32",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        },
        {
          "STORY": "B1",
          "VERTICAL_REBAR": "D4",
          "HORIZONTAL_REBAR": "D10",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        }
      ]
    },
    "14": {
      "ITEMS": [
        {
          "STORY": "1F",
          "VERTICAL_REBAR": "D25",
          "HORIZONTAL_REBAR": "D32",
          "END_REBAR": "D5",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
        },
        {
          "STORY": "B1",
          "VERTICAL_REBAR": "D4",
          "HORIZONTAL_REBAR": "D32",
          "END_REBAR": "D41",
          "BE_HORZ_REBAR": "D13",
          "BE_HORZ_SPACE": 1.6404199475065615,
          "BE_VERT_SPACE": 1.6404199475065615,
          "DE": 1.6404199475065615,
          "DW": 1.6404199475065615
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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRM-WALL"

# 指定墙体 976 按楼层（1F/B1）的钢筋准则（POST）— ITEMS[] 数组，每项含 STORY
payload = {
    "Assign": {
        "976": {
            "ITEMS": [
                {
                    "STORY": "1F",
                    "VERTICAL_REBAR": "D13",     # 垂直钢筋
                    "HORIZONTAL_REBAR": "D10",   # 水平钢筋
                    "END_REBAR": "D13",          # 端部钢筋
                    "BE_HORZ_REBAR": "D10",      # 边缘构件水平钢筋
                    "BE_HORZ_SPACE": 0.2,        # 边缘构件水平间距
                    "BE_VERT_SPACE": 0.1,        # 边缘构件垂直间距
                    "DE": 0.05, "DW": 0.05,
                },
                {
                    "STORY": "B1",
                    "VERTICAL_REBAR": "D4",
                    "HORIZONTAL_REBAR": "D10",
                    "END_REBAR": "D5",
                    "BE_HORZ_REBAR": "D13",
                    "BE_HORZ_SPACE": 0.2,
                    "BE_VERT_SPACE": 0.2,
                    "DE": 0.05, "DW": 0.05,
                },
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "DCRMW"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 33. `DESIGN/RC/KDS-41-20-2022/DCRE` — Design Criteria for Rebar (钢筋设计准则)

> **功能：** 按构件种类（`BEAM`·`COLUMN`·`BRACE`·`WALL`）一次性设置模型**全局**的 RC 钢筋设计准则。梁/柱/支撑拥有与 `DCRM-*` 类似的字段，但主筋以**数组（多规格，最多 5 种）** 输入；墙体另含按直径的材料映射、面外受弯、间距列表等**附加设置**。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCRE
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 钢筋规格 enum（**19 种 D4 ~ D57**）与材料 grade enum（**9 种**）重复项很多，规格仅写出前 5 个、材料写出全部。`Assign` 的 `minProperties` 与 `maxProperties` 均为 1，是**单条全局记录**。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "인덱스 문자열(예: \"1\") 하나만 갖는 전역 설정 맵.",
      "minProperties": 1,
      "maxProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "BEAM": {
              "type": "object",
              "description": "보 철근 규격·배근",
              "properties": {
                "MAIN_REBAR": { "type": "array", "description": "주철근 규격 (최대 5종)", "default": ["D22"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "STIRRUPS": { "type": "string", "description": "스터럽 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "STIRRUP_ARRANGEMENT": { "type": "integer", "description": "스터럽 다리 수 (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "SIDE_BAR": { "type": "string", "description": "측면철근 규격 (전체 19종: D4 ~ D57)", "default": "D13", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "DT": { "type": "number", "description": "상단 피복", "default": 0 },
                "DB": { "type": "number", "description": "하단 피복", "default": 0 },
                "DOUBLY_REBAR": { "type": "boolean", "description": "복철근 설계", "default": true },
                "DOUBLY_K": { "type": "number", "description": "복철근 k 계수", "default": 1 },
                "SPACING_LIMIT": { "type": "boolean", "description": "간격 제한 고려", "default": true },
                "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
              }
            },
            "COLUMN": {
              "type": "object",
              "description": "기둥 철근 규격·배근",
              "properties": {
                "MAIN_REBAR": { "type": "array", "description": "주철근 규격 (최대 5종)", "default": ["D22"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "ARRANGEMENT_Y": { "type": "integer", "description": "다리 수 (Y) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "ARRANGEMENT_Z": { "type": "integer", "description": "다리 수 (Z) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "DO": { "type": "number", "description": "주철근 중심 피복 do", "default": 0 },
                "SPACING_LIMIT": { "type": "boolean", "description": "간격 제한 고려", "default": true },
                "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
              }
            },
            "BRACE": {
              "type": "object",
              "description": "가새 철근 규격·배근 (COLUMN과 동일 필드)",
              "properties": {
                "MAIN_REBAR": { "type": "array", "description": "주철근 규격 (최대 5종)", "default": ["D22"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "TIES_SPIRALS": { "type": "string", "description": "띠철근/나선철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "ARRANGEMENT_Y": { "type": "integer", "description": "다리 수 (Y) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "ARRANGEMENT_Z": { "type": "integer", "description": "다리 수 (Z) (전체 19종: 2 ~ 20)", "default": 2, "enum": [2, 3, 4, 5, 6] },
                "DO": { "type": "number", "description": "주철근 중심 피복 do", "default": 0 },
                "SPACING_LIMIT": { "type": "boolean", "description": "간격 제한 고려", "default": true },
                "SPLICED_BARS": { "type": "string", "description": "이음 옵션", "default": "50%", "enum": ["None", "50%", "100%"] }
              }
            },
            "WALL": {
              "type": "object",
              "description": "전단벽 철근 규격·배근",
              "properties": {
                "VERTICAL_REBAR": { "type": "array", "description": "수직 철근 규격 (다중 선택)", "default": ["D13"], "items": { "type": "string", "description": "전체 19종: D4 ~ D57", "enum": ["D4", "D5", "D6", "D7", "D8"] } },
                "HORIZONTAL_REBAR": { "type": "string", "description": "수평 철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "END_REBAR": { "type": "string", "description": "단부 철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "BE_HORZ_REBAR": { "type": "string", "description": "경계요소 수평 철근 규격 (전체 19종: D4 ~ D57)", "default": "D10", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                "BE_HORZ_SPACE": { "type": "number", "description": "경계요소 수평 간격", "default": 0.2 },
                "BE_VERT_SPACE": { "type": "number", "description": "경계요소 수직 간격", "default": 0.1 },
                "DE": { "type": "number", "description": "단부 첫 수직철근까지 거리", "default": 0 },
                "DW": { "type": "number", "description": "벽면까지 피복 거리", "default": 0 },
                "MATERIAL_BY_DIAMETER": { "type": "boolean", "description": "직경별 재질 사용", "default": false },
                "MATERIAL_BY_DIAMETER_INPUT": {
                  "type": "object",
                  "description": "직경별 재질 입력 (MATERIAL_BY_DIAMETER=true 일 때)",
                  "properties": {
                    "VERTICAL_END_REBAR": {
                      "type": "array",
                      "description": "수직/단부 철근 재질 매핑",
                      "items": {
                        "type": "object",
                        "properties": {
                          "REBAR_DIAMETER": { "type": "string", "description": "철근 직경 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "MATERIAL": { "type": "string", "description": "재질 등급", "enum": ["None", "SD300", "SD400", "SD500", "SD600", "SD700", "SD400S", "SD500S", "SD600S"] }
                        }
                      }
                    },
                    "HORIZONTAL_REBAR": {
                      "type": "array",
                      "description": "수평 철근 재질 매핑 (VERTICAL_END_REBAR와 동일 항목 구조)",
                      "items": {
                        "type": "object",
                        "properties": {
                          "REBAR_DIAMETER": { "type": "string", "description": "철근 직경 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "MATERIAL": { "type": "string", "description": "재질 등급", "enum": ["None", "SD300", "SD400", "SD500", "SD600", "SD700", "SD400S", "SD500S", "SD600S"] }
                        }
                      }
                    }
                  }
                },
                "ADDITIONAL_WALL_DATA": {
                  "type": "object",
                  "description": "벽체 추가 데이터",
                  "properties": {
                    "OUT_OF_PLANE_BENDING": { "type": "boolean", "description": "면외 휨 설계", "default": false },
                    "VERTICAL_REBAR_SPACING": {
                      "type": "object",
                      "description": "수직 철근 간격 설정 (생략 시 기본 상태 적용)",
                      "properties": {
                        "UNIT": { "type": "string", "description": "간격 단위", "default": "mm", "enum": ["mm", "in"] },
                        "LIST_FOR_DESIGN": { "type": "array", "description": "설계에 사용할 간격 값 목록", "default": [100, 150], "items": { "type": "number" } }
                      }
                    },
                    "HORIZONTAL_REBAR_SPACING_FROM": { "type": "number", "description": "수평 철근 간격(from). 단위 m 기준 기본 0.05", "default": 0.05 },
                    "END_REBAR_METHOD": { "type": "integer", "description": "단부 철근 설계 방법", "default": 1, "enum": [1, 2, 3, 4] },
                    "DIST1": { "type": "number", "description": "단부 철근 4개 배근 간격", "default": 0.3 },
                    "DIST2": { "type": "number", "description": "단부 철근 6개 배근 간격", "default": 0.15 },
                    "DIST3": { "type": "number", "description": "단부 철근 8개 이상 배근 간격", "default": 0.1 }
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

**Root / 构件分组**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | 仅含 1 个索引字符串的全局设置映射 | `"Assign"` | Object | — | **必填** |
| 2 | 梁钢筋准则 | `"BEAM"` | Object | — | 可选 |
| 3 | 柱钢筋准则 | `"COLUMN"` | Object | — | 可选 |
| 4 | 支撑钢筋准则 | `"BRACE"` | Object | — | 可选 |
| 5 | 墙体钢筋准则 | `"WALL"` | Object | — | 可选 |

**`BEAM` 对象（柱/支撑类似，参见 `DCRM-*`）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 主筋规格数组（最多 5 种）· 各项为 19 种（D4 ~ D57） | `"MAIN_REBAR"` | Array[String] | `["D22"]` | 可选 |
| b | 箍筋规格 · 19 种 | `"STIRRUPS"` | String (enum) | `"D10"` | 可选 |
| c | 箍筋肢数 · 2 ~ 20 | `"STIRRUP_ARRANGEMENT"` | Integer (enum) | `2` | 可选 |
| d | 侧面钢筋规格 · 19 种 | `"SIDE_BAR"` | String (enum) | `"D13"` | 可选 |
| e | 上/下保护层 | `"DT"` / `"DB"` | Number | `0` | 可选 |
| f | 双排钢筋设计 / k 系数 | `"DOUBLY_REBAR"` / `"DOUBLY_K"` | Boolean / Number | `true` / `1` | 可选 |
| g | 考虑间距限制 | `"SPACING_LIMIT"` | Boolean | `true` | 可选 |
| h | 搭接选项（`None` \| `50%` \| `100%`） | `"SPLICED_BARS"` | String (enum) | `"50%"` | 可选 |

**`COLUMN` / `BRACE` 对象（共用）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 主筋规格数组（最多 5 种） | `"MAIN_REBAR"` | Array[String] | `["D22"]` | 可选 |
| b | 箍筋/螺旋箍筋规格 · 19 种 | `"TIES_SPIRALS"` | String (enum) | `"D10"` | 可选 |
| c | 肢数 Y / Z · 2 ~ 20 | `"ARRANGEMENT_Y"` / `"ARRANGEMENT_Z"` | Integer (enum) | `2` | 可选 |
| d | 主筋中心保护层 do | `"DO"` | Number | `0` | 可选 |
| e | 间距限制 / 搭接 | `"SPACING_LIMIT"` / `"SPLICED_BARS"` | Boolean / String | `true` / `"50%"` | 可选 |

**`WALL` 对象**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 垂直钢筋规格数组（多选）· 19 种 | `"VERTICAL_REBAR"` | Array[String] | `["D13"]` | 可选 |
| b | 水平 / 端部 / 边缘构件水平钢筋规格 · 19 种 | `"HORIZONTAL_REBAR"` / `"END_REBAR"` / `"BE_HORZ_REBAR"` | String (enum) | `"D10"` | 可选 |
| c | 边缘构件水平 / 垂直间距 | `"BE_HORZ_SPACE"` / `"BE_VERT_SPACE"` | Number | `0.2` / `0.1` | 可选 |
| d | 至端部第一根垂直钢筋的距离 / 墙面保护层 | `"DE"` / `"DW"` | Number | `0` | 可选 |
| e | 按直径使用材料 | `"MATERIAL_BY_DIAMETER"` | Boolean | `false` | 可选 |
| f | 按直径的材料输入（使用时） | `"MATERIAL_BY_DIAMETER_INPUT"` | Object | — | 条件 |
| g | 墙体附加数据 | `"ADDITIONAL_WALL_DATA"` | Object | — | 可选 |

**`MATERIAL_BY_DIAMETER_INPUT` 对象** — `VERTICAL_END_REBAR`、`HORIZONTAL_REBAR` 两个数组拥有相同的条目结构。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 垂直/端部钢筋材料映射数组 | `"VERTICAL_END_REBAR"` | Array[Object] | — | 可选 |
| b | 水平钢筋材料映射数组 | `"HORIZONTAL_REBAR"` | Array[Object] | — | 可选 |
| a→ | 钢筋直径 · 19 种（D4 ~ D57） | `"REBAR_DIAMETER"` | String (enum) | — | 可选 |
| a→ | 材料等级 · `None`,`SD300`,`SD400`,`SD500`,`SD600`,`SD700`,`SD400S`,`SD500S`,`SD600S` | `"MATERIAL"` | String (enum) | — | 可选 |

**`ADDITIONAL_WALL_DATA` 对象**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 面外受弯设计 | `"OUT_OF_PLANE_BENDING"` | Boolean | `false` | 可选 |
| b | 垂直钢筋间距设置（`UNIT`：`mm`/`in`，`LIST_FOR_DESIGN`：间距值数组） | `"VERTICAL_REBAR_SPACING"` | Object | `{"UNIT":"mm","LIST_FOR_DESIGN":[100,150]}` | 可选 |
| c | 水平钢筋间距（from） | `"HORIZONTAL_REBAR_SPACING_FROM"` | Number | `0.05` | 可选 |
| d | 端部钢筋设计方法（`1`=Method-1 … `4`=Method-4） | `"END_REBAR_METHOD"` | Integer (enum) | `1` | 可选 |
| e | 端部钢筋配筋间距（4 根 / 6 根 / 8 根及以上） | `"DIST1"` / `"DIST2"` / `"DIST3"` | Number | `0.3` / `0.15` / `0.1` | 可选 |

> ⚠️ **示例表记差异：** 下面的 Request 示例把 `SPLICED_BARS` 作为整数（`1`）、把 `VERTICAL_REBAR_SPACING` 作为 `["@100", "@150", …]` 字符串数组发送。与 schema 定义（`SPLICED_BARS` = `"50%"` 等字符串 enum，`VERTICAL_REBAR_SPACING` = 对象）的表记方式不同，因此实际发送时按下面示例的格式照办更安全。

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "BEAM": {
        "MAIN_REBAR": ["D22"],
        "STIRRUPS": "D10",
        "STIRRUP_ARRANGEMENT": 2,
        "SIDE_BAR": "D13",
        "DT": 0,
        "DB": 0,
        "DOUBLY_REBAR": true,
        "SPACING_LIMIT": true,
        "DOUBLY_K": 1,
        "SPLICED_BARS": 1
      },
      "COLUMN": {
        "MAIN_REBAR": ["D22"],
        "TIES_SPIRALS": "D10",
        "ARRANGEMENT_Y": 2,
        "ARRANGEMENT_Z": 2,
        "DO": 0,
        "SPACING_LIMIT": true,
        "SPLICED_BARS": 1
      },
      "BRACE": {
        "MAIN_REBAR": ["D22"],
        "TIES_SPIRALS": "D10",
        "ARRANGEMENT_Y": 2,
        "ARRANGEMENT_Z": 2,
        "DO": 0,
        "SPACING_LIMIT": true,
        "SPLICED_BARS": 1
      },
      "WALL": {
        "VERTICAL_REBAR": ["D10", "D13"],
        "HORIZONTAL_REBAR": "D10",
        "END_REBAR": "D13",
        "BE_HORZ_REBAR": "D10",
        "BE_HORZ_SPACE": 0.2,
        "BE_VERT_SPACE": 0.1,
        "DE": 0.05,
        "DW": 0.05,
        "MATERIAL_BY_DIAMETER": false,
        "ADDITIONAL_WALL_DATA": {
          "OUT_OF_PLANE_BENDING": false,
          "VERTICAL_REBAR_SPACING": ["@100", "@150", "@200", "@300", "@400"],
          "HORIZONTAL_REBAR_SPACING_FROM": 0.05,
          "END_REBAR_METHOD": 3,
          "DIST1": 0.3,
          "DIST2": 0.15,
          "DIST3": 0.1
        }
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "DCRE": {
    "1": {
      "BEAM": {
        "MAIN_REBAR": ["D22"],
        "STIRRUPS": "D10",
        "STIRRUP_ARRANGEMENT": 2,
        "SIDE_BAR": "D13",
        "DT": 0,
        "DB": 0,
        "DOUBLY_REBAR": true,
        "SPACING_LIMIT": true,
        "DOUBLY_K": 1,
        "SPLICED_BARS": 1
      },
      "WALL": {
        "VERTICAL_REBAR": ["D10", "D13"],
        "HORIZONTAL_REBAR": "D10",
        "END_REBAR": "D13",
        "BE_HORZ_REBAR": "D10",
        "BE_HORZ_SPACE": 0.2,
        "BE_VERT_SPACE": 0.1,
        "DE": 0.05,
        "DW": 0.05,
        "MATERIAL_BY_DIAMETER": false,
        "ADDITIONAL_WALL_DATA": {
          "OUT_OF_PLANE_BENDING": false,
          "VERTICAL_REBAR_SPACING": ["@100", "@150", "@200", "@300", "@400"],
          "HORIZONTAL_REBAR_SPACING_FROM": 0.05,
          "END_REBAR_METHOD": 3,
          "DIST1": 0.3,
          "DIST2": 0.15,
          "DIST3": 0.1
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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCRE"

# 设置全局 RC 钢筋准则（POST）— 按构件种类批量指定
payload = {
    "Assign": {
        "1": {
            "BEAM": {
                "MAIN_REBAR": ["D22"],          # 主筋为数组（最多 5 种）
                "STIRRUPS": "D10",
                "STIRRUP_ARRANGEMENT": 2,
                "SIDE_BAR": "D13",
                "DT": 0, "DB": 0,
                "DOUBLY_REBAR": True, "DOUBLY_K": 1,
                "SPACING_LIMIT": True,
                "SPLICED_BARS": 1,              # 示例表记：整数
            },
            "COLUMN": {
                "MAIN_REBAR": ["D22"], "TIES_SPIRALS": "D10",
                "ARRANGEMENT_Y": 2, "ARRANGEMENT_Z": 2,
                "DO": 0, "SPACING_LIMIT": True, "SPLICED_BARS": 1,
            },
            "WALL": {
                "VERTICAL_REBAR": ["D10", "D13"],
                "HORIZONTAL_REBAR": "D10", "END_REBAR": "D13",
                "BE_HORZ_REBAR": "D10",
                "BE_HORZ_SPACE": 0.2, "BE_VERT_SPACE": 0.1,
                "DE": 0.05, "DW": 0.05,
                "MATERIAL_BY_DIAMETER": False,
                "ADDITIONAL_WALL_DATA": {
                    "OUT_OF_PLANE_BENDING": False,
                    "VERTICAL_REBAR_SPACING": ["@100", "@150", "@200"],
                    "HORIZONTAL_REBAR_SPACING_FROM": 0.05,
                    "END_REBAR_METHOD": 3,
                    "DIST1": 0.3, "DIST2": 0.15, "DIST3": 0.1,
                },
            },
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "DCRE"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 34. `DESIGN/RC/KDS-41-20-2022/DCREM` — Same Beam Rebar at Joints (节点处梁钢筋同一化)

> **功能：** 用于将在节点（节）处相交的梁的钢筋**处理为同一值**的设置。可作用于全部构件（`SELECT_ALL`），或按节点（node）分别指定夹住该节点的**恰好 2 个单元编号**。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/DCREM
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "type": "object",
  "additionalProperties": false,
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "인덱스 문자열(예: \"1\")을 키로 갖는 설정 맵.",
      "minProperties": 1,
      "additionalProperties": {
        "type": "object",
        "additionalProperties": false,
        "required": ["SELECT_ALL"],
        "properties": {
          "SELECT_ALL": { "type": "boolean", "description": "사용 가능한 모든 부재에 적용" },
          "SELECTED_MEMBERS": {
            "type": "object",
            "description": "선택 부재 맵. 각 키는 절점(node) ID 문자열, 값은 해당 절점의 요소 목록.",
            "minProperties": 1,
            "additionalProperties": {
              "type": "object",
              "additionalProperties": false,
              "required": ["ELEM_LIST"],
              "properties": {
                "ELEM_LIST": {
                  "type": "array",
                  "description": "절점이 사이에 위치하는 정확히 2개의 요소 번호",
                  "items": { "type": "integer" },
                  "minItems": 2,
                  "maxItems": 2
                }
              }
            }
          }
        },
        "allOf": [
          {
            "if": { "properties": { "SELECT_ALL": { "const": false } }, "required": ["SELECT_ALL"] },
            "then": { "required": ["SELECTED_MEMBERS"] }
          }
        ]
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | 以索引字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 应用于所有构件 | `"SELECT_ALL"` | Boolean | — | **必填** |
| 3 | 选定构件映射（`SELECT_ALL`=false 时必填）。键为节点 ID 字符串 | `"SELECTED_MEMBERS"` | Object | — | 条件必填 |
| 3.1 | 夹住该节点的恰好 2 个单元编号 | `"ELEM_LIST"` | Array[Integer] (长度 2) | — | **必填** |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "SELECT_ALL": false,
      "SELECTED_MEMBERS": {
        "347": { "ELEM_LIST": [925, 926] },
        "364": { "ELEM_LIST": [922, 924] },
        "365": { "ELEM_LIST": [924, 925] },
        "396": { "ELEM_LIST": [926, 927] }
      }
    }
  }
}
```

**GET Response Body**

```json
{
  "DCREM": {
    "1": {
      "SELECT_ALL": false,
      "SELECTED_MEMBERS": {
        "347": { "ELEM_LIST": [925, 926] },
        "364": { "ELEM_LIST": [922, 924] },
        "365": { "ELEM_LIST": [924, 925] },
        "396": { "ELEM_LIST": [926, 927] }
      }
    }
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/DCREM"

# 方法 1) 所有构件同一化（POST）
requests.post(URI, headers=HEADERS, json={"Assign": {"1": {"SELECT_ALL": True}}})

# 方法 2) 按节点指定位于其两侧的 2 个单元
payload = {
    "Assign": {
        "1": {
            "SELECT_ALL": False,
            "SELECTED_MEMBERS": {
                "347": {"ELEM_LIST": [925, 926]},   # 节点 347 左右单元
                "364": {"ELEM_LIST": [922, 924]},
            },
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "DCREM"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 35. `DESIGN/RC/KDS-41-20-2022/REBB` — Modify Beam Rebar Data (梁钢筋数据修改)

> **功能：** 按截面（section）编号修改混凝土梁的钢筋数据。每个 `ITEMS` 条目包含 I·M·J 三个区段（`BAR_SECTOR_I/M/J`）的上、下主筋（按层）、箍筋（抗剪钢筋）、表面钢筋（skin bar）与上、下保护层（`DT`/`DB`），并可用 `CREATE_SUB_SECTION` 生成子截面。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBB
```

### Active Methods

`POST` · `GET` · `DELETE` · `PUT`

### JSON Schema

> schema 非常大（≈99KB）。三个区段（`BAR_SECTOR_I/M/J`）为**相同的对象结构**重复，因此下面仅完整展开 `BAR_SECTOR_I`，`BAR_SECTOR_M`·`BAR_SECTOR_J` 标注为同结构。钢筋规格 enum（**19 种 D4 ~ D57**）仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "단면 번호 문자열을 키로 갖는 맵 (예: \"211\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "콘크리트 보 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["BAR_SECTOR_I", "BAR_SECTOR_M", "BAR_SECTOR_J", "DT", "DB"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "description": "서브 단면 생성", "default": false },
                  "ID": { "type": "integer", "description": "서브 단면 ID (읽기 전용)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "요소 번호 입력 (CREATE_SUB_SECTION=true 일 때 필수). KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "description": "각 요소 ID 지정", "items": { "type": "integer" } },
                      "TO": { "type": "string", "description": "ID 범위 (예: '1to160')" },
                      "STRUCTURE_GROUP_NAME": { "type": "string", "description": "구조 그룹 이름 지정" }
                    }
                  },
                  "BAR_SECTOR_I": {
                    "type": "object",
                    "description": "I단 구간 철근",
                    "required": ["MAIN_BAR_TOP", "MAIN_BAR_BOT", "SHEAR_BAR"],
                    "properties": {
                      "MAIN_BAR_TOP": {
                        "type": "object",
                        "description": "상단 주철근 (레이어별)",
                        "required": ["LAYER1"],
                        "properties": {
                          "LAYER1": {
                            "type": "object",
                            "required": ["NAME", "NUM"],
                            "properties": {
                              "NAME": { "type": "string", "description": "규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                              "NUM": { "type": "integer", "description": "철근 개수" }
                            }
                          },
                          "LAYER2": {
                            "type": "object",
                            "required": ["NAME", "NUM"],
                            "properties": {
                              "NAME": { "type": "string", "description": "규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                              "NUM": { "type": "integer", "description": "철근 개수" }
                            }
                          }
                        }
                      },
                      "MAIN_BAR_BOT": {
                        "type": "object",
                        "description": "하단 주철근 (레이어별, MAIN_BAR_TOP과 동일 구조: LAYER1 필수 / LAYER2 선택)",
                        "required": ["LAYER1"],
                        "properties": {
                          "LAYER1": { "type": "object", "required": ["NAME", "NUM"], "properties": { "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] }, "NUM": { "type": "integer" } } },
                          "LAYER2": { "type": "object", "required": ["NAME", "NUM"], "properties": { "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] }, "NUM": { "type": "integer" } } }
                        }
                      },
                      "SHEAR_BAR": {
                        "type": "object",
                        "description": "스터럽 데이터",
                        "required": ["NAME", "LEG", "DIST"],
                        "properties": {
                          "NAME": { "type": "string", "description": "스터럽 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "LEG": { "type": "integer", "description": "다리 수" },
                          "DIST": { "type": "number", "description": "스터럽 간격 @" }
                        }
                      },
                      "SKIN_BAR": {
                        "type": "object",
                        "description": "표피철근 (이 객체가 있으면 사용)",
                        "required": ["NAME", "NUM"],
                        "properties": {
                          "NAME": { "type": "string", "description": "표피철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                          "NUM": { "type": "integer", "description": "철근 개수" }
                        }
                      }
                    }
                  },
                  "BAR_SECTOR_M": { "type": "object", "description": "중앙(M) 구간 철근 — BAR_SECTOR_I와 동일 구조 (반복 구조, 지면상 생략)" },
                  "BAR_SECTOR_J": { "type": "object", "description": "J단 구간 철근 — BAR_SECTOR_I와 동일 구조 (반복 구조, 지면상 생략)" },
                  "DT": { "type": "number", "description": "상단 콘크리트면~상단 철근중심 거리" },
                  "DB": { "type": "number", "description": "하단 콘크리트면~하단 철근중심 거리" }
                },
                "allOf": [
                  {
                    "if": { "properties": { "CREATE_SUB_SECTION": { "const": true } }, "required": ["CREATE_SUB_SECTION"] },
                    "then": { "required": ["ELEMS"] }
                  }
                ]
              }
            }
          }
        }
      }
    }
  }
}
```

> **重复结构说明：** `BAR_SECTOR_M`·`BAR_SECTOR_J` 与上面的 `BAR_SECTOR_I` 字段完全相同（`MAIN_BAR_TOP`/`MAIN_BAR_BOT`（各自 `LAYER1` 必填、`LAYER2` 可选）、`SHEAR_BAR`、`SKIN_BAR`）。为保证 JSON 块的合法性，这两个区段仅保留说明、省略内部展开。

### 参数

**Root / Item**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | 以截面编号字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 混凝土梁钢筋条目（min 1） | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否生成子截面 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 可选 |
| (2) | 子截面 ID（只读） | `"ID"` | Integer | — | 可选 |
| (3) | 单元编号输入（`CREATE_SUB_SECTION`=true 时必填） | `"ELEMS"` | Object | — | 条件 |
| (4) | I 端区段钢筋 | `"BAR_SECTOR_I"` | Object | — | **必填** |
| (5) | 中部（M）区段钢筋 | `"BAR_SECTOR_M"` | Object | — | **必填** |
| (6) | J 端区段钢筋 | `"BAR_SECTOR_J"` | Object | — | **必填** |
| (7) | 顶部保护层距离 dT | `"DT"` | Number | — | **必填** |
| (8) | 底部保护层距离 dB | `"DB"` | Number | — | **必填** |

**`BAR_SECTOR_I/M/J` 区段对象（三区段相同）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 顶部主筋（按层） | `"MAIN_BAR_TOP"` | Object | — | **必填** |
| b | 底部主筋（按层） | `"MAIN_BAR_BOT"` | Object | — | **必填** |
| a/b→ | 第 1 层（必填）/ 第 2 层（可选） | `"LAYER1"` / `"LAYER2"` | Object | — | LAYER1 **必填** |
| — | 层内钢筋规格 · 19 种（D4 ~ D57） | `"NAME"` | String (enum) | — | **必填** |
| — | 层内钢筋根数 | `"NUM"` | Integer | — | **必填** |
| c | 箍筋（抗剪钢筋） | `"SHEAR_BAR"` | Object | — | **必填** |
| c→ | 箍筋规格 / 肢数 / 间距 | `"NAME"` / `"LEG"` / `"DIST"` | String / Integer / Number | — | **必填** |
| d | 表面钢筋（skin bar，有则使用） | `"SKIN_BAR"` | Object | — | 可选 |
| d→ | 表面钢筋规格 / 根数 | `"NAME"` / `"NUM"` | String / Integer | — | **必填** |

**`CREATE_SUB_SECTION == true` 时 — `ELEMS`（KEYS / TO / STRUCTURE_GROUP_NAME 中择一）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 单元 ID 数组 | `"KEYS"` | Array[Integer] | — | 可选 |
| b | ID 范围（例：`"1to160"`） | `"TO"` | String | — | 可选 |
| c | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |

> **示例表记差异：** 下面的 Request/Response 示例把上、下主筋表记为 `"vMAIN_BAR_TOP"`/`"vMAIN_BAR_BOT"` **数组**，表面钢筋表记为 `"SKIN_BAR_NAME"`/`"SKIN_BAR_NUM"`，保护层表记为 `"MAIN_BAR_DC_TOP"`/`"MAIN_BAR_DC_BOT"`（与 schema 的 `LAYER*`/`SKIN_BAR`/`DT`·`DB` 表记方式不同）。实际发送时按下面示例的格式照办更安全。

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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBB"

# 修改截面 211 的梁钢筋数据（I·M·J 三区段相同适用）
sector = {
    "vMAIN_BAR_TOP": [],
    "vMAIN_BAR_BOT": [],
    "SHEAR_BAR": {"NAME": "D10", "LEG": 2, "DIST": 0.1},   # 箍筋
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
                    "MAIN_BAR_DC_TOP": 0.07,   # 顶部保护层
                    "MAIN_BAR_DC_BOT": 0.07,   # 底部保护层
                    "bSAME_SIZE_TOP_BOT": True,
                    "bSAME_SIZE_IMJ": True,
                    "bSAME_SIZE_LAYER": True,
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "REBB"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 36. `DESIGN/RC/KDS-41-20-2022/REBC` — Modify Column Rebar Data (柱钢筋数据修改)

> **功能：** 按截面编号修改混凝土柱的钢筋数据。包含主筋（`MAIN_BAR`）、端部/中部抗剪钢筋（`SHEAR_BAR_END`/`SHEAR_BAR_CEN`）、保护层距离（`DO`）、箍筋类型（`HOOP_TYPE`）、弯钩类型（`HOOK_TYPE`）。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 钢筋规格 enum（**19 种 D4 ~ D57**）仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "properties": {
    "Assign": {
      "type": "object",
      "description": "단면 번호 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "콘크리트 기둥 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["MAIN_BAR", "SHEAR_BAR_END", "SHEAR_BAR_CEN", "DO"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "description": "서브 단면 생성", "default": false },
                  "ID": { "type": "integer", "description": "서브 단면 ID (읽기 전용)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "요소 번호 입력 (CREATE_SUB_SECTION=true 일 때 필수). KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string", "description": "ID 범위 (예: '1to160')" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "description": "주철근 데이터",
                    "required": ["NAME", "NUM", "ROW", "USE_CORNER"],
                    "properties": {
                      "NAME": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "NUM": { "type": "integer", "description": "철근 총 개수" },
                      "ROW": { "type": "integer", "description": "철근 열(row) 수" },
                      "USE_CORNER": { "type": "boolean", "description": "코너 철근 사용" },
                      "NAME_CORNER": { "type": "string", "description": "코너 철근 규격 (USE_CORNER=true 일 때, 전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "description": "단부 전단철근 데이터",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "후프 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer", "description": "다리 수 (local Y)" },
                      "LEG_Z": { "type": "integer", "description": "다리 수 (local Z)" },
                      "DIST": { "type": "number", "description": "철근 간격 @" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "description": "중앙부 전단철근 데이터 (SHEAR_BAR_END와 동일 구조)",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "콘크리트면~철근중심 거리" },
                  "HOOP_TYPE": { "type": "string", "description": "후프 철근 타입", "default": "Ties", "enum": ["Ties", "Spirals"] },
                  "HOOK_TYPE": { "type": "integer", "description": "후크 타입 (0: 90+(135 or 180), 1: Both(135 or 180))", "default": 0, "enum": [0, 1] }
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
|-----|------|-----|------|--------|------|
| 1 | 以截面编号字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 混凝土柱钢筋条目（min 1） | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否生成子截面 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 可选 |
| (2) | 子截面 ID（只读） | `"ID"` | Integer | — | 可选 |
| (3) | 单元编号输入（`CREATE_SUB_SECTION`=true 时必填） | `"ELEMS"` | Object | — | 条件 |
| (4) | 主筋 | `"MAIN_BAR"` | Object | — | **必填** |
| (5) | 端部抗剪钢筋 | `"SHEAR_BAR_END"` | Object | — | **必填** |
| (6) | 中部抗剪钢筋 | `"SHEAR_BAR_CEN"` | Object | — | **必填** |
| (7) | 混凝土面~钢筋中心距离（do） | `"DO"` | Number | — | **必填** |
| (8) | 箍筋类型（`Ties` \| `Spirals`） | `"HOOP_TYPE"` | String (enum) | `"Ties"` | 可选 |
| (9) | 弯钩类型（`0`：90+(135 or 180) \| `1`：Both(135 or 180)） | `"HOOK_TYPE"` | Integer (enum) | `0` | 可选 |

**`MAIN_BAR` 对象**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 主筋规格 · 19 种（D4 ~ D57） | `"NAME"` | String (enum) | — | **必填** |
| b | 钢筋总根数 | `"NUM"` | Integer | — | **必填** |
| c | 排（row）数 | `"ROW"` | Integer | — | **必填** |
| d | 使用角部钢筋 | `"USE_CORNER"` | Boolean | — | **必填** |
| a' | 角部钢筋规格（USE_CORNER=true 时）· 19 种 | `"NAME_CORNER"` | String (enum) | — | 条件 |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 对象（同结构）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 箍筋规格 · 19 种（D4 ~ D57） | `"NAME"` | String (enum) | — | **必填** |
| b | 肢数（local Y） | `"LEG_Y"` | Integer | — | **必填** |
| c | 肢数（local Z） | `"LEG_Z"` | Integer | — | **必填** |
| d | 钢筋间距 @ | `"DIST"` | Number | — | **必填** |

**`CREATE_SUB_SECTION == true` 时 — `ELEMS`（KEYS / TO / STRUCTURE_GROUP_NAME 中择一）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 单元 ID 数组 | `"KEYS"` | Array[Integer] | — | 可选 |
| b | ID 范围（例：`"1to160"`） | `"TO"` | String | — | 可选 |
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

**GET Response Body**

```json
{
  "REBC": {
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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBC"

# 修改截面 1 的柱钢筋数据（POST）
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
                    "HOOP_TYPE": "Ties",   # Ties 或 Spirals
                    "HOOK_TYPE": 0,        # 0: 90+(135/180), 1: Both(135/180)
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "REBC"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 37. `DESIGN/RC/KDS-41-20-2022/REBW` — Modify Wall Rebar Data (墙体钢筋数据修改)

> **功能：** 按墙体 ID 修改钢筋数据。包含垂直/水平钢筋、端部钢筋（End Rebar）、边缘构件（Boundary Element）水平钢筋、保护层距离（dw、de）、厚度以及子墙体 ID/楼层（Story）信息。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBW
```

### Active Methods

`POST` · `PUT` · `DELETE` · `GET`

### JSON Schema

> 钢筋规格 enum（**19 种 D4 ~ D57**）仅写出前 5 个。条件必填（`allOf`）规则包含在 schema 末尾。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "벽체 ID 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "벽체 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["VERTICAL_REBAR", "HORIZONTAL_REBAR", "CONCRETE_FACE_TO_CENTER_OF_REBAR"],
                "properties": {
                  "CREATE_SUB_WALL_ID": { "type": "boolean", "description": "서브 벽체 ID 생성", "default": false },
                  "SUB_WALL_ID": { "type": "integer", "description": "서브 벽체 ID (CREATE_SUB_WALL_ID=true 일 때 읽기 전용)" },
                  "STORY": {
                    "type": "object",
                    "description": "층 범위 (CREATE_SUB_WALL_ID=true 일 때 필수)",
                    "required": ["FROM", "TO"],
                    "properties": {
                      "FROM": { "type": "string", "description": "시작 층" },
                      "TO": { "type": "string", "description": "종료 층" }
                    }
                  },
                  "VERTICAL_REBAR": {
                    "type": "object",
                    "description": "수직 철근 데이터",
                    "required": ["NAME", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "수직 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "DIST": { "type": "number", "description": "수직 철근 간격" }
                    }
                  },
                  "HORIZONTAL_REBAR": {
                    "type": "object",
                    "description": "수평 철근 데이터",
                    "required": ["NAME", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "DIST": { "type": "number", "description": "수평 철근 간격" }
                    }
                  },
                  "USE_END_REBAR": { "type": "boolean", "description": "단부 철근 입력 사용", "default": false },
                  "END_REBAR": {
                    "type": "object",
                    "description": "단부 철근 데이터 (USE_END_REBAR=true 일 때 필수)",
                    "required": ["NAME", "NUM", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "단부(수직) 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "NUM": { "type": "integer", "description": "단부 철근 개수" },
                      "DIST": { "type": "number", "description": "단부 철근 간격" }
                    }
                  },
                  "BE_HORIZONTAL_REBAR": {
                    "type": "object",
                    "description": "경계요소 수평 철근 데이터",
                    "required": ["NAME", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "경계요소 수평 철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "DIST": { "type": "number", "description": "경계요소 수평 철근 간격" }
                    }
                  },
                  "BOUNDARY_ELEMENT_LENGTH": { "type": "number", "description": "경계요소 길이", "default": 0 },
                  "CONCRETE_FACE_TO_CENTER_OF_REBAR": {
                    "type": "object",
                    "description": "콘크리트면~철근중심 거리",
                    "required": ["DW", "DE"],
                    "properties": {
                      "DW": { "type": "number", "description": "콘크리트면~수직 철근중심 (dw)" },
                      "DE": { "type": "number", "description": "콘크리트면~경계요소 철근중심 (de)" }
                    }
                  },
                  "USE_MODEL_THICKNESS": { "type": "boolean", "description": "모델 두께 사용", "default": true },
                  "THICKNESS": { "type": "number", "description": "벽체 두께 (USE_MODEL_THICKNESS=false 일 때 필수)" }
                },
                "allOf": [
                  { "if": { "properties": { "CREATE_SUB_WALL_ID": { "const": true } }, "required": ["CREATE_SUB_WALL_ID"] }, "then": { "required": ["SUB_WALL_ID", "STORY"] } },
                  { "if": { "properties": { "USE_END_REBAR": { "const": true } }, "required": ["USE_END_REBAR"] }, "then": { "required": ["END_REBAR"] } },
                  { "if": { "properties": { "USE_MODEL_THICKNESS": { "const": false } }, "required": ["USE_MODEL_THICKNESS"] }, "then": { "required": ["THICKNESS"] } }
                ]
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
|-----|------|-----|------|--------|------|
| 1 | 以墙体 ID 字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 墙体钢筋条目（min 1） | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 生成子墙体 ID | `"CREATE_SUB_WALL_ID"` | Boolean | `false` | 可选 |
| (2) | 子墙体 ID（只读，生成时必填） | `"SUB_WALL_ID"` | Integer | — | 条件 |
| (3) | 楼层范围（`FROM`/`TO`，生成时必填） | `"STORY"` | Object | — | 条件 |
| (4) | 垂直钢筋（`NAME`·`DIST`） | `"VERTICAL_REBAR"` | Object | — | **必填** |
| (5) | 水平钢筋（`NAME`·`DIST`） | `"HORIZONTAL_REBAR"` | Object | — | **必填** |
| (6) | 使用端部钢筋输入 | `"USE_END_REBAR"` | Boolean | `false` | 可选 |
| (7) | 端部钢筋（`NAME`·`NUM`·`DIST`，使用时必填） | `"END_REBAR"` | Object | — | 条件 |
| (8) | 边缘构件水平钢筋（`NAME`·`DIST`） | `"BE_HORIZONTAL_REBAR"` | Object | — | 可选 |
| (9) | 边缘构件长度 | `"BOUNDARY_ELEMENT_LENGTH"` | Number | `0` | 可选 |
| (10) | 混凝土面~钢筋中心距离（`DW`·`DE`） | `"CONCRETE_FACE_TO_CENTER_OF_REBAR"` | Object | — | **必填** |
| (11) | 使用模型厚度 | `"USE_MODEL_THICKNESS"` | Boolean | `true` | 可选 |
| (12) | 墙体厚度（`USE_MODEL_THICKNESS`=false 时必填） | `"THICKNESS"` | Number | — | 条件 |

**钢筋子对象字段汇总**

| 对象 | 字段 | 说明 |
|------|------|------|
| `VERTICAL_REBAR` / `HORIZONTAL_REBAR` / `BE_HORIZONTAL_REBAR` | `NAME`（19 种 D4 ~ D57）· `DIST` | 规格 · 间距 |
| `END_REBAR` | `NAME`（19 种）· `NUM` · `DIST` | 规格 · 根数 · 间距 |
| `CONCRETE_FACE_TO_CENTER_OF_REBAR` | `DW` · `DE` | 垂直/边缘构件钢筋保护层 |
| `STORY` | `FROM` · `TO` | 起始/结束楼层字符串 |

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

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBW"

# 修改墙体 1 的钢筋数据（子墙体 + 端部钢筋 + 用户自定义厚度）
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_WALL_ID": True,
                    "SUB_WALL_ID": 1,
                    "STORY": {"FROM": "2F", "TO": "Roof"},   # 生成时必填
                    "VERTICAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "HORIZONTAL_REBAR": {"NAME": "D16", "DIST": 200},
                    "USE_END_REBAR": True,
                    "END_REBAR": {"NAME": "D25", "NUM": 2, "DIST": 150},   # 使用时必填
                    "BE_HORIZONTAL_REBAR": {"NAME": "D19", "DIST": 222},
                    "BOUNDARY_ELEMENT_LENGTH": 222,
                    "CONCRETE_FACE_TO_CENTER_OF_REBAR": {"DW": 50, "DE": 50},
                    "USE_MODEL_THICKNESS": False,
                    "THICKNESS": 1000,   # 不使用模型厚度时必填
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "REBW"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```

---

## 38. `DESIGN/RC/KDS-41-20-2022/REBR` — Modify Brace Rebar Data (支撑钢筋数据修改)

> **功能：** 按截面编号修改混凝土支撑（Brace）的钢筋数据。结构与柱（`REBC`）类似，但 `MAIN_BAR` 中没有 `USE_CORNER`，也没有弯钩类型（`HOOK_TYPE`），由主筋（`MAIN_BAR`）、端部/中部抗剪钢筋（`SHEAR_BAR_END`/`SHEAR_BAR_CEN`）、保护层（`DO`）、箍筋类型（`HOOP_TYPE`）构成。

### Input URI

```
{base url}/DESIGN/RC/KDS-41-20-2022/REBR
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

> 钢筋规格 enum（**19 种 D4 ~ D57**）仅写出前 5 个。

```json
{
  "type": "object",
  "required": ["Assign"],
  "additionalProperties": false,
  "properties": {
    "Assign": {
      "type": "object",
      "description": "단면 번호 문자열을 키로 갖는 맵 (예: \"1\").",
      "minProperties": 1,
      "additionalProperties": false,
      "patternProperties": {
        "^[0-9]+$": {
          "type": "object",
          "required": ["ITEMS"],
          "properties": {
            "ITEMS": {
              "type": "array",
              "description": "콘크리트 가새 철근 항목",
              "minItems": 1,
              "items": {
                "type": "object",
                "required": ["MAIN_BAR", "SHEAR_BAR_END", "SHEAR_BAR_CEN", "DO"],
                "properties": {
                  "CREATE_SUB_SECTION": { "type": "boolean", "description": "서브 단면 생성", "default": false },
                  "ID": { "type": "integer", "description": "서브 단면 ID (읽기 전용)" },
                  "ELEMS": {
                    "type": "object",
                    "description": "요소 번호 입력 (CREATE_SUB_SECTION=true 일 때 필수). KEYS / TO / STRUCTURE_GROUP_NAME 중 택1",
                    "properties": {
                      "KEYS": { "type": "array", "items": { "type": "integer" } },
                      "TO": { "type": "string", "description": "ID 범위 (예: '1to160')" },
                      "STRUCTURE_GROUP_NAME": { "type": "string" }
                    }
                  },
                  "MAIN_BAR": {
                    "type": "object",
                    "description": "주철근 데이터",
                    "required": ["NAME", "NUM", "ROW"],
                    "properties": {
                      "NAME": { "type": "string", "description": "주철근 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "NUM": { "type": "integer", "description": "철근 총 개수", "minItems": 4 },
                      "ROW": { "type": "integer", "description": "철근 열(row) 수" }
                    }
                  },
                  "SHEAR_BAR_END": {
                    "type": "object",
                    "description": "단부 전단철근 데이터",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "description": "후프 규격 (전체 19종: D4 ~ D57)", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer", "description": "다리 수 (local Y)" },
                      "LEG_Z": { "type": "integer", "description": "다리 수 (local Z)" },
                      "DIST": { "type": "number", "description": "철근 간격 @" }
                    }
                  },
                  "SHEAR_BAR_CEN": {
                    "type": "object",
                    "description": "중앙부 전단철근 데이터 (SHEAR_BAR_END와 동일 구조)",
                    "required": ["NAME", "LEG_Y", "LEG_Z", "DIST"],
                    "properties": {
                      "NAME": { "type": "string", "enum": ["D4", "D5", "D6", "D7", "D8"] },
                      "LEG_Y": { "type": "integer" },
                      "LEG_Z": { "type": "integer" },
                      "DIST": { "type": "number" }
                    }
                  },
                  "DO": { "type": "number", "description": "콘크리트면~철근중심 거리" },
                  "HOOP_TYPE": { "type": "string", "description": "후프 철근 타입", "default": "Ties", "enum": ["Ties", "Spirals"] }
                },
                "allOf": [
                  { "if": { "properties": { "CREATE_SUB_SECTION": { "const": true } }, "required": ["CREATE_SUB_SECTION"] }, "then": { "required": ["ELEMS"] } }
                ]
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
|-----|------|-----|------|--------|------|
| 1 | 以截面编号字符串为键的映射 | `"Assign"` | Object | — | **必填** |
| 2 | 混凝土支撑钢筋条目（min 1） | `"ITEMS"` | Array[Object] | — | **必填** |
| (1) | 是否生成子截面 | `"CREATE_SUB_SECTION"` | Boolean | `false` | 可选 |
| (2) | 子截面 ID（只读） | `"ID"` | Integer | — | 可选 |
| (3) | 单元编号输入（`CREATE_SUB_SECTION`=true 时必填） | `"ELEMS"` | Object | — | 条件 |
| (4) | 主筋 | `"MAIN_BAR"` | Object | — | **必填** |
| (5) | 端部抗剪钢筋 | `"SHEAR_BAR_END"` | Object | — | **必填** |
| (6) | 中部抗剪钢筋 | `"SHEAR_BAR_CEN"` | Object | — | **必填** |
| (7) | 混凝土面~钢筋中心距离（do） | `"DO"` | Number | — | **必填** |
| (8) | 箍筋类型（`Ties` \| `Spirals`） | `"HOOP_TYPE"` | String (enum) | `"Ties"` | 可选 |

**`MAIN_BAR` 对象**（与柱不同，无 `USE_CORNER`/`NAME_CORNER`）

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 主筋规格 · 19 种（D4 ~ D57） | `"NAME"` | String (enum) | — | **必填** |
| b | 钢筋总根数（min 4） | `"NUM"` | Integer | — | **必填** |
| c | 排（row）数 | `"ROW"` | Integer | — | **必填** |

**`SHEAR_BAR_END` / `SHEAR_BAR_CEN` 对象（同结构）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 箍筋规格 · 19 种（D4 ~ D57） | `"NAME"` | String (enum) | — | **必填** |
| b | 肢数（local Y） | `"LEG_Y"` | Integer | — | **必填** |
| c | 肢数（local Z） | `"LEG_Z"` | Integer | — | **必填** |
| d | 钢筋间距 @ | `"DIST"` | Number | — | **必填** |

**`CREATE_SUB_SECTION == true` 时 — `ELEMS`（KEYS / TO / STRUCTURE_GROUP_NAME 中择一）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| a | 单元 ID 数组 | `"KEYS"` | Array[Integer] | — | 可选 |
| b | ID 范围（例：`"1to160"`） | `"TO"` | String | — | 可选 |
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
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/REBR"

# 修改截面 1 的支撑钢筋数据（POST）
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "CREATE_SUB_SECTION": False,
                    "MAIN_BAR": {"NAME": "D22", "NUM": 4, "ROW": 2},   # 无 USE_CORNER
                    "SHEAR_BAR_END": {"NAME": "D7", "LEG_Y": 2, "LEG_Z": 2, "DIST": 300},
                    "SHEAR_BAR_CEN": {"NAME": "D22", "LEG_Y": 3, "LEG_Z": 3, "DIST": 300},
                    "DO": 0.05,
                    "HOOP_TYPE": "Spirals",   # Ties 或 Spirals（无 HOOK_TYPE）
                }
            ]
        }
    }
}
print("POST:", requests.post(URI, headers=HEADERS, json=payload).status_code)
print("GET:", requests.get(URI, headers=HEADERS).json())   # 顶层键 "REBR"
# requests.put(URI, headers=HEADERS, json=payload)
# requests.delete(URI, headers=HEADERS)
```


---

## 39. `DESIGN/RC/KDS-41-20-2022/BD-ANAL` — RC Beam Design Perform (RC 梁设计执行)

> **功能：** 对指定的单元 · 截面（或全部）执行 RC 梁设计计算。结果保存在模型中，随后通过 `BD-TABLE` / `BD-REPORT` 查询。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "description": "ALL: all elements, ELEMS: by element No., SECTIONS: by section No.",
          "enum": ["ALL", "ELEMS", "SECTIONS"],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 执行对象（`"ALL"`=全部，`"ELEMS"`=单元编号，`"SECTIONS"`=截面编号） | `"PERFORM_TYPE"` | String (enum) | `"ALL"` | 可选 |
| 3 | 单元指定（`ELEMS`/`SECTIONS` 之一）— `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 条件 |
| 3.1 | 逐个指定单元 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 3.2 | 单元 ID 范围（例 `"1to160"`） | `"TO"` | String | — | 可选 |
| 3.3 | 结构组名 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |
| 4 | 截面编号列表（`ELEMS`/`SECTIONS` 之一） | `"SECTIONS"` | Array[Integer] | — | 条件 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ELEMS",
    "ELEMS": {
      "KEYS": [79, 80, 81]
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    # DESIGN/RC 端点通用 POST 辅助函数
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 对 79、80、81 号单元执行 RC 梁设计
res = rc_post("BD-ANAL", {"PERFORM_TYPE": "ELEMS", "ELEMS": {"KEYS": [79, 80, 81]}})
print("POST:", res.status_code)
print(res.json())   # {"message": "success"}
```

---

## 40. `DESIGN/RC/KDS-41-20-2022/BD-TABLE` — RC Beam Design Table (RC 梁设计表格)

> **功能：** 以表格（HEAD/DATA）形式返回已执行的 RC 梁设计结果。可按构件（MEMB）或按截面属性（PROP）查询。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"], "not": { "required": ["SECTIONS"] } },
        { "required": ["SECTIONS"], "not": { "required": ["ELEMS"] } }
      ],
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string", "default": "RC Beam Design Result" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 表格类型（`"MEMB"`=按构件，`"PROP"`=按截面） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 3 | 单元指定（`ELEMS`/`SECTIONS` 之一）— `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` | `"ELEMS"` | Object | — | 条件 |
| 4 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |
| 5 | 排序依据（`0`=SECT，`1`=MEMB）— `TABLE_TYPE`=MEMB 时 | `"PRI_SORT"` | Integer | `1` | 可选 |
| 6 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer | `0` | 可选 |
| 7 | 响应表格标题 | `"TABLE_NAME"` | String | `"RC Beam Design Result"` | 可选 |
| 8 | 结果文件保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 9 | 单位设置（`FORCE`/`DIST`/`HEAT`/`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 10 | 数字格式（`FORMAT`，`PLACE` 0~15） | `"STYLES"` | Object | System | 可选 |
| 11 | 显示列列表（参见下面 HEAD） | `"COMPONENTS"` | Array[String] | All | 可选 |

**响应 `HEAD` 列说明**（25 列）

| 列 | 含义 |
|----|------|
| `MEMB` / `SECT` | 构件编号 / 截面编号 |
| `Span` / `Section` | 跨长 / 截面名 |
| `Bc` / `Hc` | 截面宽度 / 高度 |
| `bf` / `hf` | 翼缘宽度 / 厚度 |
| `fck` / `fy` / `fys` | 混凝土 · 主筋 · 抗剪钢筋设计强度 |
| `POS` | 验算位置（`I`/`M`/`J`） |
| `N(-)/Mu` / `LCB_NegMu` / `AsTop` / `Rebar_Top` | 负弯矩需求强度 · 控制荷载组合 · 上部钢筋量 · 上部配筋 |
| `P(+)/Mu` / `LCB_PosMu` / `AsBot` / `Rebar_Bot` | 正弯矩需求强度 · 控制荷载组合 · 下部钢筋量 · 下部配筋 |
| `Vu` / `LCB_Vu` / `AsV` / `Stirrup` | 抗剪需求强度 · 控制荷载组合 · 抗剪钢筋量 · 箍筋配筋 |
| `CHK` | 判定（`OK`/`NG`） |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Beam Design Result",
    "COMPONENTS": [
      "MEMB", "SECT", "Span", "Section", "Bc", "Hc", "bf", "hf",
      "fck", "fy", "fys", "POS", "N(-)/Mu", "LCB_NegMu", "AsTop",
      "Rebar_Top", "P(+)/Mu", "LCB_PosMu", "AsBot", "Rebar_Bot",
      "Vu", "LCB_Vu", "AsV", "Stirrup", "CHK"
    ],
    "ELEMS": { "KEYS": [859, 860] }
  }
}
```

**Response Body**

```json
{
  "RC Beam Design Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB", "SECT", "Span", "Section", "Bc", "Hc", "bf", "hf",
      "fck", "fy", "fys", "POS", "N(-)/Mu", "LCB_NegMu", "AsTop",
      "Rebar_Top", "P(+)/Mu", "LCB_PosMu", "AsBot", "Rebar_Bot",
      "Vu", "LCB_Vu", "AsV", "Stirrup", "CHK"
    ],
    "DATA": [
      [
        "859", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "I", "358.563", "6", "0.0018",
        "4-D25", "117.551", "6", "0.0007", "3-D25",
        "211.962", "6", "0.0004", "3-D13 @310", "OK"
      ],
      [
        "859", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "M", "0.00000", "26", "0.0000",
        "2-D25", "310.677", "6", "0.0015", "4-D25",
        "162.023", "6", "0.0004", "3-D13 @310", "OK"
      ],
      [
        "859", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "J", "438.788", "6", "0.0022",
        "5-D25", "80.1426", "8", "0.0005", "3-D25",
        "227.693", "6", "0.0004", "3-D13 @310", "OK"
      ],
      [
        "860", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "I", "371.955", "6", "0.0019",
        "4-D25", "116.748", "6", "0.0007", "3-D25",
        "216.899", "6", "0.0004", "3-D13 @310", "OK"
      ],
      [
        "860", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "M", "0.00000", "26", "0.0000",
        "2-D25", "322.462", "6", "0.0016", "4-D25",
        "157.086", "6", "0.0004", "3-D13 @310", "OK"
      ],
      [
        "860", "511", "10.200", "RG1", "0.4500", "0.7000", "0.0000", "0.0000",
        "24000.0", "400000", "400000", "J", "401.826", "6", "0.0020",
        "4-D25", "104.378", "11", "0.0007", "3-D25",
        "222.756", "6", "0.0004", "3-D13 @310", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 查询 RC 梁设计结果表（按构件，859·860 号）
res = rc_post("BD-TABLE", {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0,
    "ELEMS": {"KEYS": [859, 860]},
})
table = res.json()["RC Beam Design Result"]
head = table["HEAD"]
for row in table["DATA"]:
    # 将 HEAD 列与 DATA 值配对输出
    print(dict(zip(head, row)))
```

---

## 41. `DESIGN/RC/KDS-41-20-2022/BD-REPORT` — RC Beam Design Report (RC 梁设计报告)

> **功能：** 将 RC 梁设计结果输出为 Graphic(JPG) · Detail(DOC) · Summary(TXT) 格式的文件。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "CURRENT_MODE_MEMB": { "type": "string", "enum": ["Graphic", "Detail", "Summary"] },
        "CURRENT_MODE_PROP": { "type": "string", "enum": ["Graphic", "Summary"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": { "type": "boolean", "default": true },
            "MID": { "type": "boolean", "default": false },
            "END_J": { "type": "boolean", "default": false }
          }
        },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 报告类型（`"MEMB"`=按构件，`"PROP"`=按截面） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 输出模式（按构件）— `"Graphic"`/`"Detail"`/`"Summary"` | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 条件（MEMB） |
| 4 | 输出模式（按截面）— `"Graphic"`/`"Summary"` | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 条件（PROP） |
| 5 | 单元指定（`ELEMS`/`SECTIONS` 之一） | `"ELEMS"` | Object | — | 条件 |
| 6 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |
| 7 | Detail 输出位置（`END_I`/`MID`/`END_J`）— Detail 模式时 | `"DETAIL_POSITIONS"` | Object | — | 可选 |
| 8 | 保存目录路径（例 `C:\\MIDAS\\Report\\`） | `"EXPORT_PATH"` | String | — | **必填** |
| 9 | 输出文件基础名（多单元时附加索引·单元编号作前缀） | `"OUTPUT_NAME"` | String | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {
      "KEYS": [79]
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 将 79 号梁的设计结果输出为 Graphic(JPG) 报告
res = rc_post("BD-REPORT", {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "out.jpg",
    "ELEMS": {"KEYS": [79]},
})
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```

---

## 42. `DESIGN/RC/KDS-41-20-2022/CD-ANAL` — RC Column Design Perform (RC 柱设计执行)

> **功能：** 对指定的单元 · 截面（或全部）执行 RC 柱设计计算。结果随后通过 `CD-TABLE` / `CD-REPORT` 查询。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "enum": ["ALL", "ELEMS", "SECTIONS"],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 执行对象（`"ALL"`/`"ELEMS"`/`"SECTIONS"`） | `"PERFORM_TYPE"` | String (enum) | `"ALL"` | 可选 |
| 3 | 单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 条件 |
| 4 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [105, 915]
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 对全部柱单元执行 RC 柱设计
res = rc_post("CD-ANAL", {"PERFORM_TYPE": "ALL"})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 43. `DESIGN/RC/KDS-41-20-2022/CD-TABLE` — RC Column Design Table (RC 柱设计表格)

> **功能：** 以表格（HEAD/DATA）形式返回已执行的 RC 柱设计结果。包含 P-M 相关与抗剪验算结果。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 表格类型（`"MEMB"`/`"PROP"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 3 | 单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 条件 |
| 4 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |
| 5 | 排序依据（`0`=SECT，`1`=MEMB） | `"PRI_SORT"` | Integer | `1` | 可选 |
| 6 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer | `0` | 可选 |
| 7 | 响应表格标题 · 保存路径 · 单位 · 格式 · 显示列 | `"TABLE_NAME"`/`"EXPORT_PATH"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 各类型 | — | 可选 |

**响应 `HEAD` 列说明**（32 列）

| 列 | 含义 |
|----|------|
| `MEMB` / `SECT` / `Section` | 构件编号 / 截面编号 / 截面名 |
| `Bc` / `Hc` / `Height` | 截面宽度 / 高度 / 构件长度 |
| `fck` / `fy` / `fys` | 混凝土 · 主筋 · 抗剪钢筋设计强度 |
| `LCB` | 控制荷载组合编号 |
| `phiPn.max` / `Pu` / `phiPn` / `Rat-P` | 最大设计轴压强度 · 需求轴力 · 设计轴压强度 · 轴力比 |
| `Mc` / `phiMn` / `Rat-M` | 需求弯矩 · 设计受弯强度 · 弯矩比 |
| `Mc/Pu` / `Mcz/Mcy` | 偏心 · 双向弯矩比 |
| `Ast` / `V-Rebar` | 主筋量 · 主筋配筋 |
| `LCB_Vu_end` / `LCB_Vu_mid` | 端部 · 中部抗剪控制荷载组合 |
| `Vu.end` / `Vu.mid` / `Rat-V.end` / `Rat-V.mid` | 端部 · 中部需求剪力及剪力比 |
| `As-H.end` / `As-H.mid` / `H-Rebar.end` / `H-Rebar.mid` | 端部 · 中部横向钢筋量及配筋 |
| `CHK` | 判定（`OK`/`NG`） |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "PRI_SORT": 1,
    "RESULT": 0
  }
}
```

**Response Body**

```json
{
  "Result Table": {
    "FORCE": "KGF",
    "DIST": "M",
    "HEAD": [
      "MEMB", "SECT", "Section", "Bc", "Hc", "fck", "Height", "fy", "fys",
      "LCB", "phiPn.max", "Pu", "phiPn", "Rat-P", "Mc", "phiMn", "Rat-M",
      "Mc/Pu", "Mcz/Mcy", "Ast", "V-Rebar", "LCB_Vu_end", "LCB_Vu_mid",
      "Vu.end", "Vu.mid", "Rat-V.end", "Rat-V.mid", "As-H.end", "As-H.mid",
      "H-Rebar.end", "H-Rebar.mid", "CHK"
    ],
    "DATA": [
      [
        "915", "100", "D300", "0.0000", "0.3000", "3059149", "4.0000",
        "6.1E+07", "4.1E+07", "7", "118735", "18065.4", "48178.0", "0.375",
        "1750.05", "4666.58", "0.375", "0.09687", "54.390346", "0.0008",
        "6-0-D13", "7", "7", "412.936", "412.936", "0.027", "0.027",
        "0.0000", "0.0000", "2-D13 @200", "2-D13 @200", "OK"
      ],
      [
        "1058", "100", "D300", "0.0000", "0.3000", "3059149", "4.0000",
        "6.1E+07", "4.1E+07", "5", "119777", "950.018", "110012", "0.009",
        "32.2447", "3733.91", "0.009", "0.03394", "45.000000", "0.0008",
        "4-0-D16", "47", "47", "0.00000", "0.00000", "0.000", "0.000",
        "0.0000", "0.0000", "2-D7  @200", "2-D7  @200", "OK"
      ],
      [
        "1059", "100", "D300", "0.0000", "0.3000", "3059149", "4.0000",
        "6.1E+07", "4.1E+07", "7", "119777", "9088.78", "14275.4", "0.637",
        "3543.83", "5584.15", "0.635", "0.38991", "86.471081", "0.0008",
        "4-0-D16", "7", "7", "884.284", "884.284", "0.106", "0.106",
        "0.0000", "0.0000", "2-D7  @200", "2-D7  @200", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 查询 RC 柱设计结果表（按构件排序，仅过滤 NG 时设 RESULT=2）
res = rc_post("CD-TABLE", {"TABLE_TYPE": "MEMB", "PRI_SORT": 1, "RESULT": 0})
table = res.json()["Result Table"]
head = table["HEAD"]
chk_idx = head.index("CHK")
for row in table["DATA"]:
    # 突出输出判定（CHK）为 NG 的柱
    mark = "  <-- 验算" if row[chk_idx] != "OK" else ""
    print(row[0], row[chk_idx], mark)
```

---

## 44. `DESIGN/RC/KDS-41-20-2022/CD-REPORT` — RC Column Design Report (RC 柱设计报告)

> **功能：** 将 RC 柱设计结果输出为 Graphic(JPG) · Detail(DOC) · Summary(TXT) · PM Curve(JPG) 格式的文件。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "CURRENT_MODE_PROP": { "type": "string", "enum": ["Graphic", "Summary"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 报告类型（`"MEMB"`/`"PROP"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 输出模式（按构件）— `"Graphic"`/`"Detail"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 条件（MEMB） |
| 4 | 输出模式（按截面）— `"Graphic"`/`"Summary"` | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 条件（PROP） |
| 5 | 单元指定（`ELEMS`/`SECTIONS` 之一） | `"ELEMS"` | Object | — | 条件 |
| 6 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |
| 7 | 保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 8 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result",
    "OUTPUT_NAME": "name",
    "ELEMS": {
      "KEYS": [291, 292]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Resultname",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 输出 291·292 号柱的 P-M 相关图（PMCurve）报告
res = rc_post("CD-REPORT", {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "pm.jpg",
    "ELEMS": {"KEYS": [291, 292]},
})
print(res.json())
```

---

## 45. `DESIGN/RC/KDS-41-20-2022/BRD-ANAL` — RC Brace Design Perform (RC 支撑设计执行)

> **功能：** 对指定的单元 · 截面（或全部）执行 RC 支撑（Brace）设计计算。结果随后通过 `BRD-TABLE` / `BRD-REPORT` 查询。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "PERFORM_TYPE": {
          "type": "string",
          "enum": ["ALL", "ELEMS", "SECTIONS"],
          "default": "ALL"
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 执行对象（`"ALL"`/`"ELEMS"`/`"SECTIONS"`） | `"PERFORM_TYPE"` | String (enum) | `"ALL"` | 可选 |
| 3 | 单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 条件 |
| 4 | 截面编号（或截面名）列表 | `"SECTIONS"` | Array | — | 条件 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "SECTIONS",
    "SECTIONS": ["G1"]
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 对 "G1" 截面支撑执行 RC 支撑设计
res = rc_post("BRD-ANAL", {"PERFORM_TYPE": "SECTIONS", "SECTIONS": ["G1"]})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 46. `DESIGN/RC/KDS-41-20-2022/BRD-TABLE` — RC Brace Design Table (RC 支撑设计表格)

> **功能：** 以表格（HEAD/DATA）形式返回已执行的 RC 支撑设计结果。包含轴力-受弯（P-M）及抗剪验算结果。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "PRI_SORT": { "type": "integer", "enum": [0, 1], "default": 1 },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 表格类型（`"MEMB"`/`"PROP"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 3 | 单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 条件 |
| 4 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |
| 5 | 排序依据（`0`=SECT，`1`=MEMB） | `"PRI_SORT"` | Integer | `1` | 可选 |
| 6 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer | `0` | 可选 |
| 7 | 表格标题 · 保存路径 · 单位 · 格式 · 显示列 | `"TABLE_NAME"`/`"EXPORT_PATH"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 各类型 | — | 可选 |

**响应 `HEAD` 列说明**（28 列）

| 列 | 含义 |
|----|------|
| `MEMB` / `SECT` / `Section` | 构件编号 / 截面编号 / 截面名 |
| `Bc` / `Hc` / `Height` | 截面宽度 / 高度 / 构件长度 |
| `fck` / `fy` / `fys` | 混凝土 · 主筋 · 抗剪钢筋设计强度 |
| `LCB` | 控制荷载组合编号 |
| `phiPn.max` / `Pu` / `phiPn` / `Rat-P` | 最大设计轴压强度 · 需求轴力 · 设计轴压强度 · 轴力比 |
| `Mc` / `phiMn` / `Rat-M` / `Rat-My` / `Rat-Mz` | 需求弯矩 · 设计受弯强度 · 弯矩比 · y·z 轴弯矩比 |
| `Mc/Pu` / `Mcz/Mcy` | 偏心 · 双向弯矩比 |
| `Ast` / `V-Rebar` | 主筋量 · 主筋配筋 |
| `Vu` / `Rat-V` | 需求剪力 · 剪力比 |
| `As-H` / `H-Rebar` | 横向钢筋量 · 横向钢筋配筋 |
| `CHK` | 判定（`OK`/`NG`） |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "MEMB",
    "SECTIONS": [3],
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Brace Design Result"
  }
}
```

**Response Body**

```json
{
  "RC Brace Design Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB", "SECT", "Section", "Bc", "Hc", "Height", "fck", "fy", "fys",
      "LCB", "phiPn.max", "Pu", "phiPn", "Rat-P", "Mc", "phiMn", "Rat-M",
      "Rat-My", "Rat-Mz", "Mc/Pu", "Mcz/Mcy", "Ast", "V-Rebar", "Vu",
      "Rat-V", "As-H", "H-Rebar", "CHK"
    ],
    "DATA": [
      [
        "789", "411", "G1", "0.4000", "0.7000", "10.200", "24000.0",
        "400000", "400000", "6", "4039.99", "0.00000", "-", "0.000",
        "476.307", "515.983", "0.923", "0.923", "0.000", "-", "0.000000",
        "0.0054", "14-5-D22", "228.405", "0.790", "0.0004", "2-D10 @200", "OK"
      ],
      [
        "867", "511", "RG1", "0.4500", "0.7000", "10.200", "24000.0",
        "400000", "400000", "6", "4258.45", "0.00000", "-", "0.000",
        "397.106", "458.078", "0.867", "0.867", "0.000", "-", "0.000000",
        "0.0046", "12-4-D22", "220.031", "0.743", "0.0004", "2-D10 @220", "OK"
      ],
      [
        "868", "511", "RG1", "0.4500", "0.7000", "10.200", "24000.0",
        "400000", "400000", "6", "4258.45", "0.00000", "-", "0.000",
        "406.835", "458.078", "0.888", "0.888", "0.000", "-", "0.000000",
        "0.0046", "12-4-D22", "221.859", "0.749", "0.0004", "2-D10 @220", "OK"
      ],
      [
        "871", "512", "RG2", "0.4000", "0.7000", "7.2000", "24000.0",
        "400000", "400000", "15", "3581.52", "0.00000", "-", "0.000",
        "220.147", "311.586", "0.707", "0.707", "0.000", "-", "0.000000",
        "0.0031", "8-3-D22", "120.289", "0.416", "0.0003", "2-D10 @200", "OK"
      ],
      [
        "873", "513", "RG3", "0.6000", "0.8000", "9.0000", "24000.0",
        "400000", "400000", "6", "6467.23", "0.00000", "-", "0.000",
        "787.844", "789.010", "0.999", "0.999", "0.000", "-", "0.000000",
        "0.0070", "18-5-D22", "392.386", "0.993", "0.0006", "2-D10 @240", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 查询 3 号截面支撑设计结果表
res = rc_post("BRD-TABLE", {
    "TABLE_TYPE": "MEMB",
    "SECTIONS": [3],
    "PRI_SORT": 1,
    "RESULT": 0,
})
table = res.json()["RC Brace Design Result"]
head = table["HEAD"]
for row in table["DATA"]:
    print(dict(zip(head, row)))
```

---

## 47. `DESIGN/RC/KDS-41-20-2022/BRD-REPORT` — RC Brace Design Report (RC 支撑设计报告)

> **功能：** 将 RC 支撑设计结果输出为 Graphic(JPG) · Detail(DOC) · Summary(TXT) · PM Curve(JPG) 格式的文件。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "oneOf": [
        { "required": ["ELEMS"] },
        { "required": ["SECTIONS"] }
      ],
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["MEMB", "PROP"] },
        "CURRENT_MODE_MEMB": {
          "type": "string",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "CURRENT_MODE_PROP": { "type": "string", "enum": ["Graphic", "Summary"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "SECTIONS": { "type": "array", "items": { "type": "integer" } },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 报告类型（`"MEMB"`/`"PROP"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 输出模式（按构件）— `"Graphic"`/`"Detail"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 条件（MEMB） |
| 4 | 输出模式（按截面）— `"Graphic"`/`"Summary"` | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 条件（PROP） |
| 5 | 单元指定（`ELEMS`/`SECTIONS` 之一） | `"ELEMS"` | Object | — | 条件 |
| 6 | 截面编号列表 | `"SECTIONS"` | Array[Integer] | — | 条件 |
| 7 | 保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 8 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "pm.jpg",
    "ELEMS": {
      "KEYS": [789]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\pm.jpg",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 输出 789 号支撑的 P-M 相关图（PMCurve）报告
res = rc_post("BRD-REPORT", {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "PMCurve",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "pm.jpg",
    "ELEMS": {"KEYS": [789]},
})
print(res.json())
```

---

## 48. `DESIGN/RC/KDS-41-20-2022/WD-ANAL` — RC Wall Design Perform (RC 墙体设计执行)

> **功能：** 对指定的墙体 ID · 楼层（Story）组合执行 RC 墙体（Wall）设计计算。墙体不以单元指定，而用 `WALL_IDS` + `STORY` 组合指定。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "SELECTIONS": {
          "type": "array",
          "description": "Wall ID and Story pairs to design",
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": { "type": "array", "items": { "type": "integer" } },
                  "TO": { "type": "string" }
                }
              },
              "STORY": { "type": "array", "items": { "type": "string" } }
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
| 2 | 墙体 ID · 楼层组合列表（省略时以全部墙体·全部楼层为对象） | `"SELECTIONS"` | Array[Object] | — | 可选 |
| 2.1 | 墙体 ID 指定（`KEYS`=逐个，`TO`=范围例 `"10to20"`，省略时全部墙体） | `"WALL_IDS"` | Object | — | 可选 |
| 2.2 | 目标楼层名称列表（例 `["B1F", "1F"]`，省略时全部楼层） | `"STORY"` | Array[String] | — | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SELECTIONS": [
      {
        "WALL_IDS": { "KEYS": [1, 2, 3] },
        "STORY": ["B1F", "1F"]
      },
      {
        "WALL_IDS": { "TO": "10to20" },
        "STORY": ["2F", "3F"]
      }
    ]
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 对墙体 1·2·3（B1F·1F）、10~20（2F·3F）组合执行 RC 墙体设计
res = rc_post("WD-ANAL", {
    "SELECTIONS": [
        {"WALL_IDS": {"KEYS": [1, 2, 3]}, "STORY": ["B1F", "1F"]},
        {"WALL_IDS": {"TO": "10to20"}, "STORY": ["2F", "3F"]},
    ]
})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 49. `DESIGN/RC/KDS-41-20-2022/WD-TABLE` — RC Wall Design Table (RC 墙体设计表格)

> **功能：** 以表格形式返回已执行的 RC 墙体设计结果。响应为在 `data` 对象内装入 `COMPONENTS`（列定义）与 `ROWS`（行对象数组）的结构。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "properties": {
        "TABLE_TYPE": { "type": "string", "enum": ["WID+STORY", "WID"] },
        "SELECTIONS": {
          "type": "array",
          "description": "List of wall and story selections to include. If omitted or empty, all walls and all stories are included.",
          "minItems": 0,
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": { "type": "array", "items": { "type": "integer" } },
                  "TO": { "type": "string" }
                }
              },
              "STORY": { "type": "array", "items": { "type": "string" } }
            }
          }
        },
        "PRI_SORT": {
          "type": "integer",
          "description": "Sorting criteria for WID+STORY output (by WID or Story)",
          "default": 1,
          "oneOf": [
            { "title": "Story", "const": 0 },
            { "title": "WID", "const": 1 }
          ]
        },
        "PRI_SORT_WID": {
          "type": "integer",
          "description": "Sorting criteria for WID output (by Wall Mark or WID)",
          "default": 1,
          "oneOf": [
            { "title": "WallMark", "const": 0 },
            { "title": "WID", "const": 1 }
          ]
        },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string", "default": "RC Wall Design Result" },
        "EXPORT_PATH": { "type": "string", "description": "Result Table Save Path" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 表格类型（`"WID+STORY"`=按墙体+楼层，`"WID"`=按墙体） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 3 | 墙体 ID · 楼层组合列表（`WALL_IDS`+`STORY`） | `"SELECTIONS"` | Array[Object] | — | 可选 |
| 4 | 排序依据（`0`=Story，`1`=WID）— 用于 `TABLE_TYPE`=WID+STORY 输出 | `"PRI_SORT"` | Integer (oneOf) | `1` | 可选 |
| 5 | 排序依据（`0`=WallMark，`1`=WID）— 用于 `TABLE_TYPE`=WID 输出 | `"PRI_SORT_WID"` | Integer (oneOf) | `1` | 可选 |
| 6 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer | `0` | 可选 |
| 7 | 结果文件保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 8 | 表格标题 · 单位 · 格式 · 显示列 | `"TABLE_NAME"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 各类型 | — | 可选 |

**响应 `COMPONENTS`（列）说明 — 下面示例用到的 13 列**

| 列 | 含义 |
|----|------|
| `WID` / `Story` / `Wall Mark` | 墙体 ID / 楼层 / 墙体标识 |
| `Pu` / `Rat-Py` / `Rat-Pz` | 需求轴力 · y·z 方向轴力比 |
| `Mcy` / `Mcz` / `Rat-My` / `Rat-Mz` | y·z 轴需求弯矩及弯矩比 |
| `Vu` / `Rat-V` | 需求剪力 · 剪力比 |
| `CHK` | 判定（`OK`/`NG`） |

> ⚠️ **2026-08-26 确认（article id `57442273865625`）：** `COMPONENTS` schema 的实际 `enum` 定义了远多于上面
> 13 列的 **35 个**可选列 — 除上述 13 列外还有 `Lw`、`HTw`、`hw`、
> `phiPn.max`, `phiPny`, `phiPnz`, `LCB_Mc`, `phiMny`, `phiMnz`, `BE`, `BEREBAR`, `BEL`,
> `LCB_Vu`, `phiVn`, `As-V`, `V-Rebar`, `As-H`, `H-Rebar`, `End-Rebar`, `BarLayer`, `fck`,
> `fy`、`fys`、`WallMark`（schema enum 的表记，下面 Request/Response 示例使用的是含空格的
> `"Wall Mark"` — 原文自身的表记不一致）也可指定。本表仅说明示例中实际
> 用到的 13 列，其余 22 列原文没有逐项说明，仅确认了列名。

> **参考：** 与其他构件不同，墙体表格的响应不是 `HEAD`/`DATA` 数组，而是 `data.COMPONENTS`（列名称数组）+ `data.ROWS`（以列名为键的对象数组）结构。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "WID+STORY",
    "SELECTIONS": [
      {
        "WALL_IDS": { "KEYS": [1, 3] },
        "STORY": ["3F"]
      },
      {
        "WALL_IDS": { "TO": "10to12" },
        "STORY": ["3F"]
      }
    ],
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Wall Design Result",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "COMPONENTS": [
      "WID", "Story", "Wall Mark", "Pu", "Rat-Py", "Rat-Pz",
      "Mcy", "Mcz", "Rat-My", "Rat-Mz", "Vu", "Rat-V", "CHK"
    ]
  }
}
```

**Response Body**

```json
{
  "status": "success",
  "message": "RC Wall Design Result table generated successfully.",
  "data": {
    "TABLE_NAME": "RC Wall Design Result",
    "TABLE_TYPE": "WID+STORY",
    "UNIT": { "FORCE": "kN", "DIST": "m", "MOMENT": "kN·m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 3 },
    "PRI_SORT": 1,
    "RESULT": 0,
    "TOTAL_COUNT": 5,
    "COMPONENTS": [
      "WID", "Story", "Wall Mark", "Pu", "Rat-Py", "Rat-Pz",
      "Mcy", "Mcz", "Rat-My", "Rat-Mz", "Vu", "Rat-V", "CHK"
    ],
    "ROWS": [
      {
        "WID": 1, "Story": "3F", "Wall Mark": "W1",
        "Pu": "1425.000", "Rat-Py": "0.242", "Rat-Pz": "0.226",
        "Mcy": "318.000", "Mcz": "276.000", "Rat-My": "0.323", "Rat-Mz": "0.281",
        "Vu": "184.000", "Rat-V": "0.254", "CHK": "OK"
      },
      {
        "WID": 3, "Story": "3F", "Wall Mark": "W3",
        "Pu": "1940.000", "Rat-Py": "0.327", "Rat-Pz": "0.306",
        "Mcy": "548.000", "Mcz": "421.000", "Rat-My": "0.442", "Rat-Mz": "0.381",
        "Vu": "294.000", "Rat-V": "0.392", "CHK": "OK"
      },
      {
        "WID": 10, "Story": "3F", "Wall Mark": "W10",
        "Pu": "4580.000", "Rat-Py": "0.684", "Rat-Pz": "0.652",
        "Mcy": "1450.000", "Mcz": "1125.000", "Rat-My": "0.768", "Rat-Mz": "0.704",
        "Vu": "642.000", "Rat-V": "0.726", "CHK": "OK"
      },
      {
        "WID": 11, "Story": "3F", "Wall Mark": "W11",
        "Pu": "4720.000", "Rat-Py": "0.701", "Rat-Pz": "0.668",
        "Mcy": "1525.000", "Mcz": "1194.000", "Rat-My": "0.782", "Rat-Mz": "0.719",
        "Vu": "668.000", "Rat-V": "0.748", "CHK": "OK"
      },
      {
        "WID": 12, "Story": "3F", "Wall Mark": "W12",
        "Pu": "4955.000", "Rat-Py": "0.724", "Rat-Pz": "0.691",
        "Mcy": "1604.000", "Mcz": "1268.000", "Rat-My": "0.812", "Rat-Mz": "0.742",
        "Vu": "704.000", "Rat-V": "0.781", "CHK": "OK"
      }
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 查询 3F 层墙体 1·3·10~12 的设计结果表
res = rc_post("WD-TABLE", {
    "TABLE_TYPE": "WID+STORY",
    "SELECTIONS": [
        {"WALL_IDS": {"KEYS": [1, 3]}, "STORY": ["3F"]},
        {"WALL_IDS": {"TO": "10to12"}, "STORY": ["3F"]},
    ],
    "PRI_SORT": 1,
    "RESULT": 0,
})
data = res.json()["data"]
# 响应为 COMPONENTS（列）+ ROWS（行对象）结构
for row in data["ROWS"]:
    print(row["WID"], row["Story"], row["Wall Mark"], row["CHK"])
```

---

## 50. `DESIGN/RC/KDS-41-20-2022/WD-REPORT` — RC Wall Design Report (RC 墙体设计报告)

> **功能：** 将 RC 墙体设计结果输出为 Graphic(JPG) · Detail(DOC) · Summary(TXT) · PM Curve(JPG) 格式的文件。墙体用 `SELECTIONS`（墙体 ID + 楼层）指定。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["REPORT_TYPE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "properties": {
        "REPORT_TYPE": { "type": "string", "enum": ["WID+STORY", "WID"], "default": "WID+STORY" },
        "CURRENT_MODE_WID_STORY": {
          "type": "string",
          "description": "Report output mode for WID+STORY (Detail supported)",
          "enum": ["Graphic", "Detail", "Summary", "PMCurve"]
        },
        "CURRENT_MODE_WID": {
          "type": "string",
          "description": "Report output mode for WID (Detail not supported)",
          "enum": ["Graphic", "Summary", "PMCurve"]
        },
        "SELECTIONS": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": { "type": "array", "items": { "type": "integer" } },
                  "TO": { "type": "string" }
                }
              },
              "STORY": { "type": "array", "items": { "type": "string" } }
            }
          }
        },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 报告类型（`"WID+STORY"`/`"WID"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 输出模式（墙体+楼层，支持 Detail）— `"Graphic"`/`"Detail"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_WID_STORY"` | String (oneOf) | — | 条件（WID+STORY） |
| 4 | 输出模式（墙体，不支持 Detail）— `"Graphic"`/`"Summary"`/`"PMCurve"` | `"CURRENT_MODE_WID"` | String (oneOf) | — | 条件（WID） |
| 5 | 墙体 ID · 楼层组合列表（`WALL_IDS`+`STORY`，省略时全部） | `"SELECTIONS"` | Array[Object] | — | 可选 |
| 6 | 保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 7 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "WID+STORY",
    "CURRENT_MODE_WID_STORY": "Detail",
    "SELECTIONS": [
      {
        "WALL_IDS": { "KEYS": [101, 102] },
        "STORY": ["1F", "2F"]
      },
      {
        "WALL_IDS": { "TO": "201to205" },
        "STORY": ["3F"]
      }
    ],
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "RC_Wall_Report"
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\result.jpg",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 将墙体 101·102（1F·2F）、201~205（3F）的设计结果输出为 Detail(DOC) 报告
res = rc_post("WD-REPORT", {
    "REPORT_TYPE": "WID+STORY",
    "CURRENT_MODE_WID_STORY": "Detail",
    "SELECTIONS": [
        {"WALL_IDS": {"KEYS": [101, 102]}, "STORY": ["1F", "2F"]},
        {"WALL_IDS": {"TO": "201to205"}, "STORY": ["3F"]},
    ],
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "RC_Wall_Report",
})
print(res.json())
```

---

## 51. `DESIGN/RC/KDS-41-20-2022/HCD-ANAL` — RC Haunched Beam Design Perform (RC 加腋梁设计执行)

> **功能：** 对指定的加腋梁（Haunched Beam）单元执行 RC 设计计算。结果随后通过 `HCD-TABLE` / `HCD-REPORT` 查询。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/HCD-ANAL
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "description": "Execute design calculation",
      "additionalProperties": false,
      "properties": {
        "ELEMS": {
          "type": "object",
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
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 加腋梁单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 可选 |
| 2.1 | 逐个指定单元 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 2.2 | 单元 ID 范围（例 `"1to160"`） | `"TO"` | String | — | 可选 |
| 2.3 | 结构组名 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "ELEMS": {
      "KEYS": [1065, 1073]
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

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 对 1065·1073 号加腋梁执行 RC 加腋梁设计
res = rc_post("HCD-ANAL", {"ELEMS": {"KEYS": [1065, 1073]}})
print("POST:", res.status_code, res.json())   # {"message": "success"}
```

---

## 52. `DESIGN/RC/KDS-41-20-2022/HCD-TABLE` — RC Haunched Beam Design Table (RC 加腋梁设计表格)

> **功能：** 以表格（HEAD/DATA）形式返回已执行的 RC 加腋梁设计结果。按加腋区段（T/N 区段）的位置（`POS`）提供受弯·抗剪验算结果。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/HCD-TABLE
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "RESULT": { "type": "integer", "enum": [0, 1, 2], "default": 0 },
        "TABLE_NAME": { "type": "string" },
        "EXPORT_PATH": { "type": "string" },
        "UNIT": { "type": "object" },
        "STYLES": { "type": "object" },
        "COMPONENTS": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 加腋梁单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 可选 |
| 3 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer | `0` | 可选 |
| 4 | 表格标题 · 保存路径 · 单位 · 格式 · 显示列 | `"TABLE_NAME"`/`"EXPORT_PATH"`/`"UNIT"`/`"STYLES"`/`"COMPONENTS"` | 各类型 | — | 可选 |

**响应 `HEAD` 列说明**（20 列）

| 列 | 含义 |
|----|------|
| `HCBM` / `Section` | 加腋梁构件编号 / 区段截面名（`T1`/`N`/`T2` 等） |
| `Bc-I` / `Hc-I` / `Bc-J` / `Hc-J` | I 端 · J 端截面宽度 / 高度 |
| `POS` | 验算位置（1~n 分割点） |
| `N(-)Mu` / `LCB_NegMu` / `AsTop` / `Rebar_Top` | 负弯矩需求强度 · 控制荷载组合 · 上部钢筋量 · 上部配筋 |
| `P(+)Mu` / `LCB_PosMu` / `AsBot` / `Rebar_Bot` | 正弯矩需求强度 · 控制荷载组合 · 下部钢筋量 · 下部配筋 |
| `Vu` / `LCB_Vu` / `AsV` / `Stirrup` | 抗剪需求强度 · 控制荷载组合 · 抗剪钢筋量 · 箍筋配筋 |
| `CHK` | 判定（`OK`/`NG`） |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "RESULT": 0,
    "COMPONENTS": [
      "HCBM", "Section", "Bc-I", "Hc-I", "Bc-J", "Hc-J", "POS",
      "N(-)Mu", "LCB_NegMu", "AsTop", "Rebar_Top", "P(+)Mu",
      "LCB_PosMu", "AsBot", "Rebar_Bot", "Vu", "LCB_Vu", "AsV",
      "Stirrup", "CHK"
    ],
    "ELEMS": { "KEYS": [1065, 1073] }
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
      "HCBM", "Section", "Bc-I", "Hc-I", "Bc-J", "Hc-J", "POS",
      "N(-)Mu", "LCB_NegMu", "AsTop", "Rebar_Top", "P(+)Mu",
      "LCB_PosMu", "AsBot", "Rebar_Bot", "Vu", "LCB_Vu", "AsV",
      "Stirrup", "CHK"
    ],
    "DATA": [
      [
        "1065", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "1",
        "1102.57", "6", "0.0037", "10-D22", "0.00000", "200", "0.0000",
        "2-D22", "220.513", "6", "0.0009", "2-D10 @160", "OK"
      ],
      [
        "1065", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "2",
        "1048.87", "6", "0.0038", "11-D22", "0.00000", "200", "0.0000",
        "2-D22", "214.847", "6", "0.0009", "2-D10 @160", "OK"
      ],
      [
        "1065", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "3",
        "845.696", "5", "0.0044", "12-D22", "0.00000", "200", "0.0000",
        "2-D22", "193.595", "6", "0.0009", "2-D10 @160", "OK"
      ],
      [
        "1065", "N", "1.0000", "0.5000", "1.0000", "0.5000", "4",
        "0.00000", "", "0.0000", "None", "0.00000", "", "0.0000",
        "None", "-", "-", "-", "-", "OK"
      ],
      [
        "1065", "N", "1.0000", "0.5000", "1.0000", "0.5000", "5",
        "0.00000", "", "0.0000", "None", "0.00000", "", "0.0000",
        "None", "-", "-", "-", "-", "OK"
      ],
      [
        "1065", "N", "1.0000", "0.5000", "1.0000", "0.5000", "6",
        "0.00000", "", "0.0000", "None", "0.00000", "", "0.0000",
        "None", "-", "-", "-", "-", "OK"
      ],
      [
        "1065", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "7",
        "50.1371", "5", "0.0002", "9-D22", "0.00000", "200", "0.0000",
        "2-D22", "47.9404", "5", "0.0000", "2-D10 @210", "OK"
      ],
      [
        "1065", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "8",
        "39.4785", "5", "0.0001", "9-D22", "0.00000", "200", "0.0000",
        "2-D22", "42.5657", "5", "0.0000", "2-D10 @290", "OK"
      ],
      [
        "1065", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "9",
        "8.21148", "5", "0.0000", "9-D22", "0.00000", "200", "0.0000",
        "2-D22", "19.4192", "5", "0.0000", "2-D10 @310", "OK"
      ],
      [
        "1073", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "1",
        "2555.66", "5", "0.0128", "13-13-D22", "0.00000", "200", "0.0000",
        "2-D22", "365.532", "5", "0.0010", "2-D10 @140", "N"
      ],
      [
        "1073", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "2",
        "2376.23", "5", "0.0107", "13-13-D22", "0.00000", "200", "0.0000",
        "2-D22", "352.311", "5", "0.0010", "2-D10 @140", "N"
      ],
      [
        "1073", "T1", "1.0000", "0.7000", "1.0000", "0.5000", "3",
        "2036.18", "5", "0.0086", "13-13-D22", "0.00000", "200", "0.0000",
        "2-D22", "328.341", "5", "0.0010", "2-D10 @140", "N"
      ],
      [
        "1073", "N", "1.0000", "0.5000", "1.0000", "0.5000", "4",
        "0.00000", "", "0.0000", "None", "0.00000", "", "0.0000",
        "None", "-", "-", "-", "-", "OK"
      ],
      [
        "1073", "N", "1.0000", "0.5000", "1.0000", "0.5000", "5",
        "0.00000", "", "0.0000", "None", "0.00000", "", "0.0000",
        "None", "-", "-", "-", "-", "OK"
      ],
      [
        "1073", "N", "1.0000", "0.5000", "1.0000", "0.5000", "6",
        "0.00000", "", "0.0000", "None", "0.00000", "", "0.0000",
        "None", "-", "-", "-", "-", "OK"
      ],
      [
        "1073", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "7",
        "341.337", "5", "0.0028", "8-D22", "0.00000", "200", "0.0000",
        "2-D22", "193.540", "5", "0.0010", "2-D10 @140", "OK"
      ],
      [
        "1073", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "8",
        "247.220", "5", "0.0016", "5-D22", "0.00000", "200", "0.0000",
        "2-D22", "182.791", "5", "0.0010", "2-D10 @140", "OK"
      ],
      [
        "1073", "T2", "1.0000", "0.5000", "1.0000", "0.7000", "9",
        "76.1395", "5", "0.0004", "4-D22", "0.00000", "200", "0.0000",
        "2-D22", "158.821", "5", "0.0000", "2-D10 @310", "OK"
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

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 查询 1065·1073 号加腋梁设计结果表
res = rc_post("HCD-TABLE", {"RESULT": 0, "ELEMS": {"KEYS": [1065, 1073]}})
table = res.json()["Result Table"]
head = table["HEAD"]
for row in table["DATA"]:
    # 加腋梁按区段（Section）·位置（POS）输出多行
    print(dict(zip(head, row)))
```

---

## 53. `DESIGN/RC/KDS-41-20-2022/HCD-REPORT` — RC Haunched Beam Design Report (RC 加腋梁设计报告)

> **功能：** 将 RC 加腋梁设计结果输出为 Graphic(JPG) 格式的文件。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/HCD-REPORT
```

### Active Methods

`POST`

### JSON Schema

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["CURRENT_MODE", "EXPORT_PATH", "OUTPUT_NAME"],
      "additionalProperties": false,
      "properties": {
        "CURRENT_MODE": { "type": "string", "enum": ["Graphic"] },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": { "type": "array", "items": { "type": "integer" } },
            "TO": { "type": "string" },
            "STRUCTURE_GROUP_NAME": { "type": "string" }
          }
        },
        "EXPORT_PATH": { "type": "string" },
        "OUTPUT_NAME": { "type": "string" }
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 输出模式（`"Graphic"`=JPG 图像） | `"CURRENT_MODE"` | String (enum) | — | **必填** |
| 3 | 加腋梁单元指定 — `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一 | `"ELEMS"` | Object | — | 可选 |
| 4 | 保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 5 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "graphic",
    "ELEMS": {
      "KEYS": [1073]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\graphic",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX（Civil NX 为 /civil）
HEADERS = {"MAPI-Key": "<已签发的密钥>", "Content-Type": "application/json"}

def rc_post(code, arg):
    uri = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/{code}"
    return requests.post(uri, headers=HEADERS, json={"Argument": arg})

# 将 1073 号加腋梁的设计结果输出为 Graphic(JPG) 报告
res = rc_post("HCD-REPORT", {
    "CURRENT_MODE": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "graphic",
    "ELEMS": {"KEYS": [1073]},
})
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```


---

## 54. `DESIGN/RC/KDS-41-20-2022/BC-ANAL` — RC Beam Check Perform (RC 梁验算执行)

> **功能：** 对已指定配筋（rebar）的 RC 梁构件执行**规范验算（Checking）** 计算。支持全部（`ALL`）·按单元（`ELEMS`）·按截面（`SECTIONS`）的对象选择，结果随后通过 `BC-TABLE`/`BC-REPORT` 查询。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BC-ANAL
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
          "description": "Select target type. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          "description": "Element No. Input",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Specify Each ID"
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
          "items": {
            "type": "integer"
          },
          "description": "Section No. Input"
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
| 2 | 执行对象类型（`"ALL"`=全部，`"ELEMS"`=按单元，`"SECTIONS"`=按截面） | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 可选 |
| 3 | 单元输入（ELEMS / SECTIONS 之一） | `"ELEMS"` | Object | — | 条件 |
| 3.1 | 逐个 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 3.2 | ID 范围（例 `"1to160"`） | `"TO"` | String | — | 可选 |
| 3.3 | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |
| 4 | 截面编号（ELEMS / SECTIONS 之一） | `"SECTIONS"` | Array[Integer] | — | 条件 |

> `Argument` 必须仅包含 `"ELEMS"` 或 `"SECTIONS"` 中的**恰好一个**（oneOf），`ELEMS` 内部也只能使用 `KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一。若 `PERFORM_TYPE="ALL"`，则无需指定对象即验算全部梁。

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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"   # Civil NX（Gen NX 为 /gen）
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BC-ANAL"

# 对全部 RC 梁执行规范验算
payload = {"Argument": {"PERFORM_TYPE": "ALL"}}
res = requests.post(URI, headers=HEADERS, json=payload)
print("POST:", res.status_code)
print(res.json())   # {"message": "success"}
```

---

## 55. `DESIGN/RC/KDS-41-20-2022/BC-TABLE` — RC Beam Check Table (RC 梁验算表格)

> **功能：** 以表格（HEAD/DATA）形式返回 RC 梁验算结果。同时输出强度验算（受弯正/负弯矩·抗剪）与配筋详图（主筋·箍筋最小/最大条件）。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`，对象用 `"ELEMS"` 或 `"SECTIONS"` 之一（oneOf）指定。主要属性如下。

```json
{
  "type": "object",
  "required": ["Argument"],
  "additionalProperties": false,
  "properties": {
    "Argument": {
      "type": "object",
      "required": ["TABLE_TYPE"],
      "additionalProperties": false,
      "oneOf": [{"required": ["ELEMS"]}, {"required": ["SECTIONS"]}],
      "properties": {
        "PRI_SORT":    {"type": "integer", "default": 1, "oneOf": [{"title": "Section", "const": 0}, {"title": "Member", "const": 1}]},
        "ELEMS":       {"type": "object", "properties": {"KEYS": {"type": "array", "items": {"type": "integer"}}, "TO": {"type": "string"}, "STRUCTURE_GROUP_NAME": {"type": "string"}}},
        "SECTIONS":    {"type": "array", "items": {"type": "integer"}},
        "RESULT":      {"type": "integer", "default": 0, "oneOf": [{"title": "All", "const": 0}, {"title": "OK", "const": 1}, {"title": "NG", "const": 2}]},
        "TABLE_NAME":  {"type": "string", "default": "RC Beam Checking Result"},
        "TABLE_TYPE":  {"type": "string", "enum": ["MEMB", "PROP"]},
        "EXPORT_PATH": {"type": "string"},
        "UNIT":        {"type": "object", "properties": {"FORCE": {"type": "string"}, "DIST": {"type": "string"}, "HEAT": {"type": "string"}, "TEMP": {"type": "string"}}},
        "STYLES":      {"type": "object", "properties": {"FORMAT": {"type": "string", "enum": ["Default", "Fixed", "Scientific", "General"]}, "PLACE": {"type": "integer", "minimum": 0, "maximum": 15}}},
        "COMPONENTS":  {"type": "array", "items": {"type": "string"}}
      }
    }
  }
}
```

### 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------|--------|------|
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 排序依据（`0`=Section，`1`=Member） | `"PRI_SORT"` | Integer (oneOf) | `1` | 可选 |
| 3 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer (oneOf) | `0` | 可选 |
| 4 | 响应表格标题 | `"TABLE_NAME"` | String | `"RC Beam Checking Result"` | 可选 |
| 5 | 结果表格类型（`"MEMB"` 或 `"PROP"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 6 | 目标单元（ELEMS / SECTIONS 之一） | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 条件 |
| 7.1 | 逐个 ID / ID 范围 / 结构组 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 可选 |
| 8 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 9 | 单位设置（`FORCE`,`DIST`,`HEAT`,`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 10 | 数字格式（`FORMAT`,`PLACE`） | `"STYLES"` | Object | System | 可选 |
| 11 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |


**Response HEAD 列说明**（按与请求 `COMPONENTS` 相同的顺序返回）：

| 列(HEAD) | 含义 |
|------|------|
| `MEMB` | Element number |
| `SECT` | Section property number |
| `Span` | Length of beam member |
| `Section` | Symbol for sectional shape (SB: Rectangular, TEE: T-shape) |
| `Bc` | Width of beam member |
| `Hc` | Height (depth) of beam member |
| `bf` | Width of the flange of T-shape section |
| `hf` | Thickness of the flange of T-shape section |
| `fck` | Design compressive strength of concrete (f'c) |
| `fy` | Design yield strength of main rebars |
| `fys` | Design yield strength of shear rebars |
| `POS` | Section design points (I, M, J). M reflects max values at 1/4, 1/2, and 3/4 points. |
| `CHK_STR` | Status of Checking Results (Strength) |
| `Neg_Rebar` | Negative moment strength - Rebar |
| `Neg_As_use` | Negative moment strength - As.use |
| `Neg_Mu` | Negative moment strength - N(-) Mu |
| `Neg_LCB` | Negative moment strength - LCB |
| `Neg_phiMn` | Negative moment strength - N(-) φMn |
| `Rat-N` | Negative moment strength - Ratio (Mu/φMn), red if > 1.0 |
| `Pos_Rebar` | Positive moment strength - Rebar |
| `Pos_As_use` | Positive moment strength - As.use |
| `Pos_Mu` | Positive moment strength - P(+) Mu |
| `Pos_LCB` | Positive moment strength - LCB |
| `Pos_phiMn` | Positive moment strength - P(+) φMn |
| `Rat-P` | Positive moment strength - Ratio (Mu/φMn), red if > 1.0 |
| `Sh_Stirrup` | Shear strength - Stirrup |
| `Sh_Vu` | Shear strength - Vu |
| `Sh_LCB` | Shear strength - LCB |
| `Sh_phiVc` | Shear strength - φVc |
| `Rat-V` | Shear strength - Ratio (Vu/φVc), red if > 1.0 |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |
| `Top_rho_max` | Main rebar (Top) - ρ.max (%) |
| `Top_rho_use` | Main rebar (Top) - ρ.use (%) |
| `Top_rho_min` | Main rebar (Top) - ρ.min (%) |
| `Top_s_max` | Main rebar (Top) - s.max |
| `Top_s_use` | Main rebar (Top) - s.use |
| `Bot_rho_max` | Main rebar (Bottom) - ρ.max (%) |
| `Bot_rho_use` | Main rebar (Bottom) - ρ.use (%) |
| `Bot_rho_min` | Main rebar (Bottom) - ρ.min (%) |
| `Bot_s_max` | Main rebar (Bottom) - s.max |
| `Bot_s_use` | Main rebar (Bottom) - s.use |
| `St_Av_use` | Stirrup - Av.use |
| `St_Av_min` | Stirrup - Av.min |
| `St_s_max` | Stirrup - s.max |
| `St_s_use` | Stirrup - s.use |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PRI_SORT": 1,
    "SECTIONS": [
      7
    ],
    "RESULT": 0,
    "TABLE_NAME": "RC Beam Checking Result",
    "TABLE_TYPE": "MEMB",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "bf",
      "hf",
      "fck",
      "fy",
      "fys",
      "POS",
      "CHK_STR",
      "Neg_Rebar",
      "Neg_As_use",
      "Neg_Mu",
      "Neg_LCB",
      "Neg_phiMn",
      "Rat-N",
      "Pos_Rebar",
      "Pos_As_use",
      "Pos_Mu",
      "Pos_LCB",
      "Pos_phiMn",
      "Rat-P",
      "Sh_Stirrup",
      "Sh_Vu",
      "Sh_LCB",
      "Sh_phiVc",
      "Rat-V",
      "CHK_RBR",
      "Top_rho_max",
      "Top_rho_use",
      "Top_rho_min",
      "Top_s_max",
      "Top_s_use",
      "Bot_rho_max",
      "Bot_rho_use",
      "Bot_rho_min",
      "Bot_s_max",
      "Bot_s_use",
      "St_Av_use",
      "St_Av_min",
      "St_s_max",
      "St_s_use"
    ]
  }
}
```

**Response Body**（代表 DATA 2 行，每行长度 = HEAD 45 列）

```json
{
  "RC Beam Checking Result": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Span",
      "Section",
      "Bc",
      "Hc",
      "bf",
      "hf",
      "fck",
      "fy",
      "fys",
      "POS",
      "CHK_STR",
      "Neg_Rebar",
      "Neg_As_use",
      "Neg_Mu",
      "Neg_LCB",
      "Neg_phiMn",
      "Rat-N",
      "Pos_Rebar",
      "Pos_As_use",
      "Pos_Mu",
      "Pos_LCB",
      "Pos_phiMn",
      "Rat-P",
      "Sh_Stirrup",
      "Sh_Vu",
      "Sh_LCB",
      "Sh_phiVc",
      "Rat-V",
      "CHK_RBR",
      "Top_rho_max",
      "Top_rho_use",
      "Top_rho_min",
      "Top_s_max",
      "Top_s_use",
      "Bot_rho_max",
      "Bot_rho_use",
      "Bot_rho_min",
      "Bot_s_max",
      "Bot_s_use",
      "St_Av_use",
      "St_Av_min",
      "St_s_max",
      "St_s_use"
    ],
    "DATA": [
      [
        "1086",
        "7",
        "1.0000",
        "N",
        "1.0000",
        "0.5000",
        "0.0000",
        "0.0000",
        "30000.0",
        "600000",
        "400000",
        "I",
        "OK",
        "10-D22",
        "0.0039",
        "769.768",
        "5",
        "775.573",
        "0.99",
        "2-D22",
        "0.0008",
        "0.00000",
        "200",
        "185.633",
        "0.00",
        "2-D10 @160",
        "234.891",
        "5",
        "298.851",
        "0.57",
        "OK",
        "1.384",
        "0.887",
        "0.219",
        "0.1350",
        "0.0970",
        "2.093",
        "0.177",
        "0.000",
        "-",
        "-",
        "0.0000",
        "0.0000",
        "0.2183",
        "0.1600"
      ],
      [
        "1086",
        "7",
        "1.0000",
        "N",
        "1.0000",
        "0.5000",
        "0.0000",
        "0.0000",
        "30000.0",
        "600000",
        "400000",
        "M",
        "OK",
        "10-D22",
        "0.0039",
        "711.692",
        "5",
        "775.573",
        "0.92",
        "2-D22",
        "0.0008",
        "0.00000",
        "200",
        "185.633",
        "0.00",
        "2-D10 @160",
        "229.722",
        "5",
        "298.851",
        "0.55",
        "OK",
        "1.384",
        "0.887",
        "0.219",
        "0.1350",
        "0.0970",
        "2.093",
        "0.177",
        "0.000",
        "-",
        "-",
        "0.0000",
        "0.0000",
        "0.2183",
        "0.1600"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BC-TABLE"

# 查询截面编号 7 梁的验算结果表（按构件排序）
payload = {
    "Argument": {
        "PRI_SORT": 1,
        "SECTIONS": [7],
        "RESULT": 0,                       # All（OK/NG 全部）
        "TABLE_NAME": "RC Beam Checking Result",
        "TABLE_TYPE": "MEMB",
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = res.json()["RC Beam Checking Result"]
print("HEAD 列数:", len(table["HEAD"]))
for row in table["DATA"]:
    # 输出 POS（端部 I/M/J）、强度判定（CHK_STR）、剪力比（Rat-V）
    print(row[11], row[12], "Rat-V=", row[29])
```

---

## 56. `DESIGN/RC/KDS-41-20-2022/BC-REPORT` — RC Beam Check Report (RC 梁验算报告)

> **功能：** 将 RC 梁验算结果导出为文件（图形 JPG / Detail DOC / Summary TXT）。指定多个单元时，以附加了索引·单元编号的文件名分别保存。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BC-REPORT
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
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": {
              "type": "boolean",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 报告对象类型（`"MEMB"` / `"PROP"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 单元（MEMB）输出模式（`"Graphic"`/`"Detail"`/`"Summary"`） | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 条件 |
| 4 | 截面（PROP）输出模式（`"Graphic"`/`"Summary"`） | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 条件 |
| 5 | 目标单元（ELEMS / SECTIONS 之一） | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 条件 |
| 5.1 | 逐个 ID / ID 范围 / 结构组 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 可选 |
| 6 | Detail 输出位置（`END_I`,`MID`,`END_J`） | `"DETAIL_POSITIONS"` | Object | — | 可选 |
| 7 | 报告保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 8 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

> 若 `REPORT_TYPE="MEMB"` 则使用 `CURRENT_MODE_MEMB`，若为 `"PROP"` 则使用 `CURRENT_MODE_PROP`（仅 Graphic/Summary）。`DETAIL_POSITIONS` 仅在 `CURRENT_MODE_MEMB="Detail"` 时有效。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Detail",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "detail.txt",
    "ELEMS": {
      "KEYS": [
        1086
      ]
    },
    "DETAIL_POSITIONS": {
      "END_I": false,
      "MID": false,
      "END_J": true
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\detail.txt",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BC-REPORT"

# 将单元 1086 梁的 Detail 报告（J 端）保存为 TXT
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "CURRENT_MODE_MEMB": "Detail",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "detail.txt",
        "ELEMS": {"KEYS": [1086]},
        "DETAIL_POSITIONS": {"END_I": False, "MID": False, "END_J": True},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...detail.txt", "MESSAGE": ""}
```

---
## 57. `DESIGN/RC/KDS-41-20-2022/CC-ANAL` — RC Column Check Perform (RC 柱验算执行)

> **功能：** 对已指定配筋的 RC 柱构件执行 **P-M 相关·抗剪规范验算**。支持全部/按单元/按截面的对象选择。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CC-ANAL
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
          "description": "Select target type. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          "description": "Element No. Input",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Specify Each ID"
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
          "items": {
            "type": "integer"
          },
          "description": "Section No. Input"
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
| 2 | 执行对象类型（`"ALL"`=全部，`"ELEMS"`=按单元，`"SECTIONS"`=按截面） | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 可选 |
| 3 | 单元输入（ELEMS / SECTIONS 之一） | `"ELEMS"` | Object | — | 条件 |
| 3.1 | 逐个 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 3.2 | ID 范围（例 `"1to160"`） | `"TO"` | String | — | 可选 |
| 3.3 | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |
| 4 | 截面编号（ELEMS / SECTIONS 之一） | `"SECTIONS"` | Array[Integer] | — | 条件 |

> `ELEMS`/`SECTIONS` 为 oneOf，只能使用其中一个。示例为在 `PERFORM_TYPE="ALL"` 的同时指定单元 1059 的形式。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        1059
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CC-ANAL"

# 执行特定柱单元（1059）的验算
payload = {"Argument": {"PERFORM_TYPE": "ALL", "ELEMS": {"KEYS": [1059]}}}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"message": "success"}
```

---

## 58. `DESIGN/RC/KDS-41-20-2022/CC-TABLE` — RC Column Check Table (RC 柱验算表格)

> **功能：** 以表格返回 RC 柱验算结果。包含 P-M 相关（轴力/弯矩强度比）、端部与中部抗剪、主筋·箍筋（Hoop）配筋详图。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`，对象用 `"ELEMS"`/`"SECTIONS"` 之一（oneOf）指定。主要属性如下。

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
        "PRI_SORT": {
          "type": "integer",
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
          "default": "RC Column Checking Result"
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string"
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
| 2 | 排序依据（`0`=SECT，`1`=MEMB） | `"PRI_SORT"` | Integer (oneOf) | `1` | 可选 |
| 3 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer (oneOf) | `0` | 可选 |
| 4 | 响应表格标题 | `"TABLE_NAME"` | String | `"RC Column Checking Result"` | 可选 |
| 5 | 结果表格类型（`"MEMB"` 或 `"PROP"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 6 | 目标单元（ELEMS / SECTIONS 之一） | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 条件 |
| 6.1 | 逐个 ID / ID 范围 / 结构组 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 可选 |
| 7 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 8 | 单位设置（`FORCE`,`DIST`,`HEAT`,`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 9 | 数字格式（`FORMAT`,`PLACE`） | `"STYLES"` | Object | System | 可选 |
| 10 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |


**Response HEAD 列说明**（按与请求 `COMPONENTS` 相同的顺序返回）：

| 列(HEAD) | 含义 |
|------|------|
| `MEMB` | Element Number |
| `SECT` | Section Property Number |
| `Section` | Sectional Shape |
| `Bc` | Width of Column Member |
| `Hc` | Depth of Column Member |
| `fck` | Design Compressive Strength of Concrete (f'c) |
| `Height` | Height of Column Member |
| `fy` | Design Yield Strength of Main Rebars |
| `fys` | Design Yield Strength of Shear Rebars |
| `CHK_STR` | Status of Checking Results (Strength) |
| `LCB_PM` | Load Combination for Axial-Moment Check |
| `V_Rebar` | Vertical Rebar |
| `phiPn_max` | Maximum Axial Design Strength |
| `Pu` | Factored Axial Force |
| `phiPn` | Design Axial Strength |
| `Rat_P` | Axial Strength Ratio (Pu/φPn) |
| `Mc` | Factored Moment |
| `phiMn` | Design Moment Strength |
| `Rat_M` | Moment Strength Ratio (Mc/φMn) |
| `Rat_My` | Y-axis Moment Strength Ratio |
| `Rat_Mz` | Z-axis Moment Strength Ratio |
| `Mc_Pu` | Eccentricity |
| `Mcz_Mcy` | Moment Rotation (Mcz/Mcy) |
| `MFy` | Moment Factor (Y) |
| `MFz` | Moment Factor (Z) |
| `Mcy` | Factored Moment (Y) |
| `Mcz` | Factored Moment (Z) |
| `LCB_Vu_end` | Load Combination for Shear at End |
| `LCB_Vu_mid` | Load Combination for Shear at Mid |
| `Vu_end` | Factored Shear Force at End |
| `Vu_mid` | Factored Shear Force at Mid |
| `Rat_V_end` | Shear Strength Ratio at End |
| `Rat_V_mid` | Shear Strength Ratio at Mid |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |
| `H_Rebar_end` | Shear Rebar at End |
| `H_Rebar_mid` | Shear Rebar at Mid |
| `rho_max` | Main Rebar (%) - ρ.max |
| `rho_use` | Main Rebar (%) - ρ.use |
| `rho_min` | Main Rebar (%) - ρ.min |
| `Avy_use_end` | Hoop (End) - Avy.use |
| `Avy_min_end` | Hoop (End) - Avy.min |
| `Avz_use_end` | Hoop (End) - Avz.use |
| `Avz_min_end` | Hoop (End) - Avz.min |
| `s_max_end` | Hoop (End) - s.max |
| `s_use_end` | Hoop (End) - s.use |
| `Avy_use_mid` | Hoop (Mid) - Avy.use |
| `Avy_min_mid` | Hoop (Mid) - Avy.min |
| `Avz_use_mid` | Hoop (Mid) - Avz.use |
| `Avz_min_mid` | Hoop (Mid) - Avz.min |
| `s_max_mid` | Hoop (Mid) - s.max |
| `s_use_mid` | Hoop (Mid) - s.use |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Column Checking Result",
    "TABLE_TYPE": "MEMB",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB_PM",
      "V_Rebar",
      "phiPn_max",
      "Pu",
      "phiPn",
      "Rat_P",
      "Mc",
      "phiMn",
      "Rat_M",
      "Rat_My",
      "Rat_Mz",
      "Mc_Pu",
      "Mcz_Mcy",
      "MFy",
      "MFz",
      "Mcy",
      "Mcz",
      "LCB_Vu_end",
      "LCB_Vu_mid",
      "Vu_end",
      "Vu_mid",
      "Rat_V_end",
      "Rat_V_mid",
      "CHK_RBR",
      "H_Rebar_end",
      "H_Rebar_mid",
      "rho_max",
      "rho_use",
      "rho_min",
      "Avy_use_end",
      "Avy_min_end",
      "Avz_use_end",
      "Avz_min_end",
      "s_max_end",
      "s_use_end",
      "Avy_use_mid",
      "Avy_min_mid",
      "Avz_use_mid",
      "Avz_min_mid",
      "s_max_mid",
      "s_use_mid"
    ],
    "ELEMS": {
      "KEYS": [
        1058
      ]
    }
  }
}
```

**Response Body**（代表 DATA 1 行，每行长度 = HEAD 51 列）

```json
{
  "RC Column Checking Result": {
    "FORCE": "KGF",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB_PM",
      "V_Rebar",
      "phiPn_max",
      "Pu",
      "phiPn",
      "Rat_P",
      "Mc",
      "phiMn",
      "Rat_M",
      "Rat_My",
      "Rat_Mz",
      "Mc_Pu",
      "Mcz_Mcy",
      "MFy",
      "MFz",
      "Mcy",
      "Mcz",
      "LCB_Vu_end",
      "LCB_Vu_mid",
      "Vu_end",
      "Vu_mid",
      "Rat_V_end",
      "Rat_V_mid",
      "CHK_RBR",
      "H_Rebar_end",
      "H_Rebar_mid",
      "rho_max",
      "rho_use",
      "rho_min",
      "Avy_use_end",
      "Avy_min_end",
      "Avz_use_end",
      "Avz_min_end",
      "s_max_end",
      "s_use_end",
      "Avy_use_mid",
      "Avy_min_mid",
      "Avz_use_mid",
      "Avz_min_mid",
      "s_max_mid",
      "s_use_mid"
    ],
    "DATA": [
      [
        "1058",
        "100",
        "D300",
        "0.0000",
        "0.3000",
        "3059149",
        "4.0000",
        "6.1E+07",
        "4.1E+07",
        "OK",
        "5",
        "4-2-D22",
        "142746",
        "950.018",
        "116623",
        "0.008",
        "32.2447",
        "3958.30",
        "0.008",
        "0.008",
        "0.008",
        "0.03394",
        "45.000000",
        "1.000",
        "1.000",
        "22.8004",
        "22.8004",
        "47",
        "47",
        "0.00000",
        "0.00000",
        "0.000",
        "0.000",
        "OK",
        "2-D10 @150",
        "2-D10 @150",
        "3.000",
        "2.191",
        "1.000",
        "0.0001",
        "-",
        "0.0001",
        "-",
        "0.2000",
        "0.1500",
        "0.0001",
        "-",
        "0.0001",
        "-",
        "0.2000",
        "0.1500"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CC-TABLE"

# 查询单元 1058 柱的验算结果
payload = {
    "Argument": {
        "PRI_SORT": 1,
        "RESULT": 0,
        "TABLE_NAME": "RC Column Checking Result",
        "TABLE_TYPE": "MEMB",
        "ELEMS": {"KEYS": [1058]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = res.json()["RC Column Checking Result"]
head = table["HEAD"]
for row in table["DATA"]:
    rec = dict(zip(head, row))
    print(rec["MEMB"], "P比=", rec["Rat_P"], "M比=", rec["Rat_M"], rec["CHK_STR"])
```

---

## 59. `DESIGN/RC/KDS-41-20-2022/CC-REPORT` — RC Column Check Report (RC 柱验算报告)

> **功能：** 将 RC 柱验算结果导出为文件（Graphic/Detail/Summary）。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CC-REPORT
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
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": {
              "type": "boolean",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 报告对象类型（`"MEMB"` / `"PROP"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 单元（MEMB）输出模式（`"Graphic"`/`"Detail"`/`"Summary"`） | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 条件 |
| 4 | 截面（PROP）输出模式（`"Graphic"`/`"Summary"`） | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 条件 |
| 5 | 目标单元（ELEMS / SECTIONS 之一） | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 条件 |
| 5.1 | 逐个 ID / ID 范围 / 结构组 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 可选 |
| 6 | Detail 输出位置（`END_I`,`MID`,`END_J`） | `"DETAIL_POSITIONS"` | Object | — | 可选 |
| 7 | 报告保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 8 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

> 若 `REPORT_TYPE="MEMB"` 则使用 `CURRENT_MODE_MEMB`，若为 `"PROP"` 则使用 `CURRENT_MODE_PROP`（仅 Graphic/Summary）。`DETAIL_POSITIONS` 仅在 `CURRENT_MODE_MEMB="Detail"` 时有效。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "columnresult",
    "CURRENT_MODE_MEMB": "Graphic",
    "ELEMS": {
      "TO": "1058to1059"
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\columnresult",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CC-REPORT"

# 保存单元 1058~1059 柱的 Graphic 报告
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "columnresult",
        "CURRENT_MODE_MEMB": "Graphic",
        "ELEMS": {"TO": "1058to1059"},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```

---

## 60. `DESIGN/RC/KDS-41-20-2022/BRC-ANAL` — RC Brace Check Perform (RC 支撑验算执行)

> **功能：** 对已指定配筋的 RC 支撑（Brace）构件执行 P-M 相关·抗剪规范验算。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRC-ANAL
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
          "description": "Select target type. ELEMS: by element numbers, SECTIONS: by section numbers, ALL: all elements.",
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
          "description": "Element No. Input",
          "additionalProperties": false,
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              },
              "description": "Specify Each ID"
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
          "items": {
            "type": "integer"
          },
          "description": "Section No. Input"
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
| 2 | 执行对象类型（`"ALL"`=全部，`"ELEMS"`=按单元，`"SECTIONS"`=按截面） | `"PERFORM_TYPE"` | String (oneOf) | `"ALL"` | 可选 |
| 3 | 单元输入（ELEMS / SECTIONS 之一） | `"ELEMS"` | Object | — | 条件 |
| 3.1 | 逐个 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 3.2 | ID 范围（例 `"1to160"`） | `"TO"` | String | — | 可选 |
| 3.3 | 结构组名称 | `"STRUCTURE_GROUP_NAME"` | String | — | 可选 |
| 4 | 截面编号（ELEMS / SECTIONS 之一） | `"SECTIONS"` | Array[Integer] | — | 条件 |

> 示例为以单元 883、902 两根支撑为对象的指定形式。`ELEMS`/`SECTIONS` 为 oneOf，只能使用其中一个。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PERFORM_TYPE": "ALL",
    "ELEMS": {
      "KEYS": [
        883,
        902
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BRC-ANAL"

# 执行支撑单元 883、902 的验算
payload = {"Argument": {"PERFORM_TYPE": "ALL", "ELEMS": {"KEYS": [883, 902]}}}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"message": "success"}
```

---

## 61. `DESIGN/RC/KDS-41-20-2022/BRC-TABLE` — RC Brace Check Table (RC 支撑验算表格)

> **功能：** 以表格返回 RC 支撑验算结果。构成与柱验算类似，但提供无端部区分的单一位置值（轴力/弯矩强度比、抗剪、箍筋配筋）。响应顶层键为 `TABLE_NAME`（未指定时示例中为 `"Result Table"`）。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`，对象用 `"ELEMS"`/`"SECTIONS"` 之一（oneOf）指定。主要属性如下。

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
        "PRI_SORT": {
          "type": "integer",
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
          "default": "RC Brace Checking Result"
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string"
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
| 2 | 排序依据（`0`=SECT，`1`=MEMB） | `"PRI_SORT"` | Integer (oneOf) | `1` | 可选 |
| 3 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer (oneOf) | `0` | 可选 |
| 4 | 响应表格标题 | `"TABLE_NAME"` | String | `"RC Brace Checking Result"` | 可选 |
| 5 | 结果表格类型（`"MEMB"` 或 `"PROP"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 6 | 目标单元（ELEMS / SECTIONS 之一） | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 条件 |
| 6.1 | 逐个 ID / ID 范围 / 结构组 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 可选 |
| 7 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 8 | 单位设置（`FORCE`,`DIST`,`HEAT`,`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 9 | 数字格式（`FORMAT`,`PLACE`） | `"STYLES"` | Object | System | 可选 |
| 10 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |


**Response HEAD 列说明**（按与请求 `COMPONENTS` 相同的顺序返回）：

| 列(HEAD) | 含义 |
|------|------|
| `MEMB` | Element Number |
| `SECT` | Section Property Number |
| `Section` | Sectional Shape |
| `Bc` | Width of Brace Member |
| `Hc` | Depth of Brace Member |
| `fck` | Design Compressive Strength of Concrete (f'c) |
| `Height` | Height of Brace Member |
| `fy` | Design Yield Strength of Main Rebars |
| `fys` | Design Yield Strength of Shear Rebars |
| `CHK_STR` | Status of Checking Results (Strength) |
| `LCB` | Load Combination for P-M Interaction / Check |
| `phiPn.max` | Maximum Design Axial Strength |
| `Pu` | Factored Axial Force |
| `phiPn` | Design Axial Strength |
| `Rat-P` | Axial Strength Ratio (Pu/phiPn) |
| `Mc` | Factored Moment |
| `phiMn` | Design Moment Strength |
| `Rat-M` | Moment Strength Ratio (Mc/phiMn) |
| `Rat-My` | Y-axis Moment Strength Ratio |
| `Rat-Mz` | Z-axis Moment Strength Ratio |
| `Mc/Pu` | Eccentricity |
| `Mcz/Mcy` | Moment Rotation (Mcz/Mcy) |
| `V-Rebar` | Vertical Rebar |
| `MF.y` | Moment Factor (Y) |
| `MF.z` | Moment Factor (Z) |
| `Mcy` | Factored Moment (Y) |
| `Mcz` | Factored Moment (Z) |
| `H-Rebar` | Hoop / Shear Rebar |
| `Vu` | Factored Shear Force |
| `Rat-V` | Shear Strength Ratio (Vu/phiVn) |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |
| `rho.max` | Main Rebar (%) - rho.max |
| `rho.use` | Main Rebar (%) - rho.use |
| `rho.min` | Main Rebar (%) - rho.min |
| `Avy.use` | Hoop - Avy.use |
| `Avy.min` | Hoop - Avy.min |
| `Avz.use` | Hoop - Avz.use |
| `Avz.min` | Hoop - Avz.min |
| `s.max` | Hoop - s.max |
| `s.use` | Hoop - s.use |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_TYPE": "MEMB",
    "COMPONENTS": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB",
      "phiPn.max",
      "Pu",
      "phiPn",
      "Rat-P",
      "Mc",
      "phiMn",
      "Rat-M",
      "Rat-My",
      "Rat-Mz",
      "Mc/Pu",
      "Mcz/Mcy",
      "V-Rebar",
      "MF.y",
      "MF.z",
      "Mcy",
      "Mcz",
      "H-Rebar",
      "Vu",
      "Rat-V",
      "CHK_RBR",
      "rho.max",
      "rho.use",
      "rho.min",
      "Avy.use",
      "Avy.min",
      "Avz.use",
      "Avz.min",
      "s.max",
      "s.use"
    ],
    "ELEMS": {
      "KEYS": [
        883
      ]
    }
  }
}
```

**Response Body**（代表 DATA 1 行，每行长度 = HEAD 40 列）

```json
{
  "Result Table": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "MEMB",
      "SECT",
      "Section",
      "Bc",
      "Hc",
      "fck",
      "Height",
      "fy",
      "fys",
      "CHK_STR",
      "LCB",
      "phiPn.max",
      "Pu",
      "phiPn",
      "Rat-P",
      "Mc",
      "phiMn",
      "Rat-M",
      "Rat-My",
      "Rat-Mz",
      "Mc/Pu",
      "Mcz/Mcy",
      "V-Rebar",
      "MF.y",
      "MF.z",
      "Mcy",
      "Mcz",
      "H-Rebar",
      "Vu",
      "Rat-V",
      "CHK_RBR",
      "rho.max",
      "rho.use",
      "rho.min",
      "Avy.use",
      "Avy.min",
      "Avz.use",
      "Avz.min",
      "s.max",
      "s.use"
    ],
    "DATA": [
      [
        "883",
        "2",
        "300x600",
        "0.3000",
        "0.6000",
        "30000.0",
        "3.1100",
        "600000",
        "400000",
        "M-",
        "5",
        "2849.37",
        "0.00000",
        "-",
        "0.000",
        "491.277",
        "199.531",
        "2.462",
        "2.462",
        "0.000",
        "-",
        "0.000000",
        "4-2-D22",
        "1.000",
        "1.000",
        "491.277",
        "0.00000",
        "2-D22 @200",
        "229.714",
        "0.313",
        "M",
        "3.000",
        "0.860",
        "1.000",
        "0.0008",
        "-",
        "0.0008",
        "0.0001",
        "0.2000",
        "0.2000"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BRC-TABLE"

# 查询单元 883 支撑的验算结果（未指定 TABLE_NAME → 响应键为 "Result Table"）
payload = {
    "Argument": {
        "PRI_SORT": 1,
        "RESULT": 0,
        "TABLE_TYPE": "MEMB",
        "ELEMS": {"KEYS": [883]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
body = res.json()
table = body.get("RC Brace Checking Result") or body["Result Table"]
head = table["HEAD"]
for row in table["DATA"]:
    rec = dict(zip(head, row))
    print(rec["MEMB"], rec["CHK_STR"], "Rat-V=", rec["Rat-V"])
```

---

## 62. `DESIGN/RC/KDS-41-20-2022/BRC-REPORT` — RC Brace Check Report (RC 支撑验算报告)

> **功能：** 将 RC 支撑验算结果导出为文件（Graphic/Detail/Summary）。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/BRC-REPORT
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
          "enum": [
            "MEMB",
            "PROP"
          ]
        },
        "CURRENT_MODE_MEMB": {
          "type": "string",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          }
        },
        "SECTIONS": {
          "type": "array",
          "items": {
            "type": "integer"
          }
        },
        "DETAIL_POSITIONS": {
          "type": "object",
          "properties": {
            "END_I": {
              "type": "boolean",
              "default": true
            },
            "MID": {
              "type": "boolean",
              "default": false
            },
            "END_J": {
              "type": "boolean",
              "default": false
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 报告对象类型（`"MEMB"` / `"PROP"`） | `"REPORT_TYPE"` | String (enum) | — | **必填** |
| 3 | 单元（MEMB）输出模式（`"Graphic"`/`"Detail"`/`"Summary"`） | `"CURRENT_MODE_MEMB"` | String (oneOf) | — | 条件 |
| 4 | 截面（PROP）输出模式（`"Graphic"`/`"Summary"`） | `"CURRENT_MODE_PROP"` | String (oneOf) | — | 条件 |
| 5 | 目标单元（ELEMS / SECTIONS 之一） | `"ELEMS"` / `"SECTIONS"` | Object / Array | — | 条件 |
| 5.1 | 逐个 ID / ID 范围 / 结构组 | `"KEYS"` / `"TO"` / `"STRUCTURE_GROUP_NAME"` | Array\[Int] / String / String | — | 可选 |
| 6 | Detail 输出位置（`END_I`,`MID`,`END_J`） | `"DETAIL_POSITIONS"` | Object | — | 可选 |
| 7 | 报告保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 8 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |

> 若 `REPORT_TYPE="MEMB"` 则使用 `CURRENT_MODE_MEMB`，若为 `"PROP"` 则使用 `CURRENT_MODE_PROP`（仅 Graphic/Summary）。`DETAIL_POSITIONS` 仅在 `CURRENT_MODE_MEMB="Detail"` 时有效。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "MEMB",
    "CURRENT_MODE_MEMB": "Graphic",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\",
    "OUTPUT_NAME": "Graphic.jpg",
    "ELEMS": {
      "KEYS": [
        883
      ]
    }
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\Graphic.jpg",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/BRC-REPORT"

# 保存单元 883 支撑的 Graphic(JPG) 报告
payload = {
    "Argument": {
        "REPORT_TYPE": "MEMB",
        "CURRENT_MODE_MEMB": "Graphic",
        "EXPORT_PATH": "C:\\MIDAS\\Result\\",
        "OUTPUT_NAME": "Graphic.jpg",
        "ELEMS": {"KEYS": [883]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...Graphic.jpg", "MESSAGE": ""}
```

---

## 63. `DESIGN/RC/KDS-41-20-2022/WC-ANAL` — RC Wall Check Perform (RC 墙体验算执行)

> **功能：** 对 RC 墙体（Shear Wall）构件执行规范验算。墙体不以单元编号指定对象，而用**墙 ID（WALL_IDS）与楼层（STORY）** 的组合（`SELECTIONS`）指定；省略时验算全部墙·全部楼层。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WC-ANAL
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
      "description": "Execute RC Wall design calculation. If SELECTIONS is omitted or empty, all wall IDs and all stories are included.",
      "additionalProperties": false,
      "properties": {
        "SELECTIONS": {
          "type": "array",
          "minItems": 0,
          "items": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "KEYS": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  },
                  "TO": {
                    "type": "string"
                  }
                },
                "oneOf": [
                  {
                    "required": [
                      "KEYS"
                    ],
                    "not": {
                      "required": [
                        "TO"
                      ]
                    }
                  },
                  {
                    "required": [
                      "TO"
                    ],
                    "not": {
                      "required": [
                        "KEYS"
                      ]
                    }
                  }
                ]
              },
              "STORY": {
                "type": "array",
                "items": {
                  "type": "string"
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
| 2 | 墙/层选择列表（省略时全部） | `"SELECTIONS"` | Array[Object] | — | 可选 |
| 2.1 | 墙 ID 指定 | `"WALL_IDS"` | Object | — | 可选 |
| 2.1.1 | 逐个墙 ID | `"KEYS"` | Array[Integer] | — | 可选 |
| 2.1.2 | 墙 ID 范围（例 `"1to20"`） | `"TO"` | String | — | 可选 |
| 2.2 | 楼层名称列表 | `"STORY"` | Array[String] | — | 可选 |

> `WALL_IDS` 只能使用 `KEYS` 或 `TO` 之一（oneOf）。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "SELECTIONS": [
      {
        "WALL_IDS": {
          "KEYS": [
            1,
            2,
            3
          ]
        },
        "STORY": [
          "B1F",
          "1F"
        ]
      },
      {
        "WALL_IDS": {
          "TO": "10to20"
        },
        "STORY": [
          "2F",
          "3F"
        ]
      }
    ]
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WC-ANAL"

# 验算墙 1~3（B1F,1F）与墙 10~20（2F,3F）
payload = {
    "Argument": {
        "SELECTIONS": [
            {"WALL_IDS": {"KEYS": [1, 2, 3]}, "STORY": ["B1F", "1F"]},
            {"WALL_IDS": {"TO": "10to20"}, "STORY": ["2F", "3F"]},
        ]
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"message": "success"}
```

---

## 64. `DESIGN/RC/KDS-41-20-2022/WC-TABLE` — RC Wall Check Table (RC 墙体验算表格)

> **功能：** 以表格返回 RC 墙体验算结果。墙体通过 `TABLE_TYPE` 选择输出单位（`"WID+STORY"`=墙ID+层，`"WID"`=墙ID），对象用 `SELECTIONS`（WALL_IDS + STORY）指定。响应不是 `HEAD`/`DATA`，而是 **`COMPONENTS` + `DATA`（每行为以列名为键的对象）** 形式。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WC-TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`，对象用 `SELECTIONS`（省略时全部墙·全部层）指定。主要属性如下。

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
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "WID+STORY",
            "WID"
          ]
        },
        "SELECTIONS": {
          "type": "array",
          "minItems": 0,
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  },
                  "TO": {
                    "type": "string"
                  }
                },
                "oneOf": [
                  {
                    "required": [
                      "KEYS"
                    ],
                    "not": {
                      "required": [
                        "TO"
                      ]
                    }
                  },
                  {
                    "required": [
                      "TO"
                    ],
                    "not": {
                      "required": [
                        "KEYS"
                      ]
                    }
                  }
                ]
              },
              "STORY": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        },
        "PRI_SORT": {
          "type": "integer",
          "default": 1,
          "oneOf": [
            {
              "title": "Story",
              "const": 0
            },
            {
              "title": "WID",
              "const": 1
            }
          ]
        },
        "PRI_SORT_WID": {
          "type": "integer",
          "default": 1,
          "oneOf": [
            {
              "title": "WallMark",
              "const": 0
            },
            {
              "title": "WID",
              "const": 1
            }
          ]
        },
        "RESULT": {
          "type": "integer",
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
          "default": "RC Wall Checking Result"
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          }
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          }
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string"
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
| 2 | 输出单位（`"WID+STORY"` / `"WID"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 3 | 墙/层选择列表（省略时全部） | `"SELECTIONS"` | Array[Object] | — | 可选 |
| 3.1 | 墙 ID（`KEYS` 或 `TO`） | `"WALL_IDS"` | Object | — | 可选 |
| 3.2 | 楼层名称列表 | `"STORY"` | Array[String] | — | 可选 |
| 4 | WID+STORY 排序（`0`=Story，`1`=WID） | `"PRI_SORT"` | Integer | `1` | 可选 |
| 5 | WID 排序（`0`=WallMark，`1`=WID） | `"PRI_SORT_WID"` | Integer | `1` | 可选 |
| 6 | 结果过滤（`0`=All，`1`=OK，`2`=NG） | `"RESULT"` | Integer | `0` | 可选 |
| 7 | 响应表格标题 | `"TABLE_NAME"` | String | `"RC Wall Checking Result"` | 可选 |
| 8 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 9 | 单位设置 | `"UNIT"` | Object | System | 可选 |
| 10 | 数字格式 | `"STYLES"` | Object | System | 可选 |
| 11 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |


**响应 `COMPONENTS` 列说明**（以示例请求为基准，即 `DATA` 各对象的键）：

| 列 | 含义 |
|------|------|
| `WID` | Wall Number |
| `Story` | Story Name |
| `Wall Mark` | Designation for Shear Wall Member |
| `Pu` | Factored Axial Force (Maximum for Wall Mark) |
| `Rat-Py` | Axial Strength Ratio in Y-direction (Maximum for Wall Mark) |
| `Rat-Pz` | Axial Strength Ratio in Z-direction (Maximum for Wall Mark) |
| `Mcy` | Factored Moment in Y-direction (Maximum for Wall Mark) |
| `Mcz` | Factored Moment in Z-direction (Maximum for Wall Mark) |
| `Rat-My` | Moment Strength Ratio in Y-direction (Maximum for Wall Mark) |
| `Rat-Mz` | Moment Strength Ratio in Z-direction (Maximum for Wall Mark) |
| `Vu` | Factored Shear Force (Maximum for Wall Mark) |
| `phiVn` | Design Shear Strength |
| `Rat-V` | Shear Strength Ratio (Maximum for Wall Mark) |
| `CHK_STR` | Status of Checking Results (Strength) |
| `CHK_RBR` | Status of Checking Results (Rebar Detail) |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "WID+STORY",
    "SELECTIONS": [
      {
        "WALL_IDS": {
          "KEYS": [
            1,
            3
          ]
        },
        "STORY": [
          "3F"
        ]
      },
      {
        "WALL_IDS": {
          "TO": "10to12"
        },
        "STORY": [
          "3F"
        ]
      }
    ],
    "PRI_SORT": 1,
    "RESULT": 0,
    "TABLE_NAME": "RC Wall Check Result",
    "UNIT": {
      "FORCE": "kN",
      "DIST": "m"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "COMPONENTS": [
      "WID",
      "Story",
      "Wall Mark",
      "Pu",
      "Rat-Py",
      "Rat-Pz",
      "Mcy",
      "Mcz",
      "Rat-My",
      "Rat-Mz",
      "Vu",
      "phiVn",
      "Rat-V",
      "CHK_STR",
      "CHK_RBR"
    ]
  }
}
```

**Response Body**（DATA 5 个对象，每个对象的键数 = COMPONENTS 15 个）

```json
{
  "TABLE_NAME": "RC Wall Check Result",
  "TABLE_TYPE": "WID+STORY",
  "UNIT": {
    "FORCE": "kN",
    "DIST": "m"
  },
  "STYLES": {
    "FORMAT": "Fixed",
    "PLACE": 3
  },
  "COMPONENTS": [
    "WID",
    "Story",
    "Wall Mark",
    "Pu",
    "Rat-Py",
    "Rat-Pz",
    "Mcy",
    "Mcz",
    "Rat-My",
    "Rat-Mz",
    "Vu",
    "phiVn",
    "Rat-V",
    "CHK_STR",
    "CHK_RBR"
  ],
  "DATA": [
    {
      "WID": 1,
      "Story": "3F",
      "Wall Mark": "W3F-01",
      "Pu": 1280.45,
      "Rat-Py": 0.382,
      "Rat-Pz": 0.417,
      "Mcy": 245.72,
      "Mcz": 318.64,
      "Rat-My": 0.536,
      "Rat-Mz": 0.624,
      "Vu": 186.33,
      "phiVn": 406.834,
      "Rat-V": 0.458,
      "CHK_STR": "OK",
      "CHK_RBR": "OK"
    },
    {
      "WID": 3,
      "Story": "3F",
      "Wall Mark": "W3F-03",
      "Pu": 1545.82,
      "Rat-Py": 0.461,
      "Rat-Pz": 0.489,
      "Mcy": 312.56,
      "Mcz": 405.21,
      "Rat-My": 0.642,
      "Rat-Mz": 0.711,
      "Vu": 224.78,
      "phiVn": 406.474,
      "Rat-V": 0.553,
      "CHK_STR": "OK",
      "CHK_RBR": "OK"
    },
    {
      "WID": 10,
      "Story": "3F",
      "Wall Mark": "W3F-10",
      "Pu": 1842.37,
      "Rat-Py": 0.573,
      "Rat-Pz": 0.618,
      "Mcy": 438.92,
      "Mcz": 512.68,
      "Rat-My": 0.782,
      "Rat-Mz": 0.846,
      "Vu": 286.54,
      "phiVn": 412.882,
      "Rat-V": 0.694,
      "CHK_STR": "OK",
      "CHK_RBR": "OK"
    },
    {
      "WID": 11,
      "Story": "3F",
      "Wall Mark": "W3F-11",
      "Pu": 2168.94,
      "Rat-Py": 0.684,
      "Rat-Pz": 0.732,
      "Mcy": 526.34,
      "Mcz": 638.15,
      "Rat-My": 0.891,
      "Rat-Mz": 0.957,
      "Vu": 342.61,
      "phiVn": 421.933,
      "Rat-V": 0.812,
      "CHK_STR": "OK",
      "CHK_RBR": "OK"
    },
    {
      "WID": 12,
      "Story": "3F",
      "Wall Mark": "W3F-12",
      "Pu": 2385.76,
      "Rat-Py": 0.745,
      "Rat-Pz": 0.801,
      "Mcy": 612.48,
      "Mcz": 724.93,
      "Rat-My": 0.936,
      "Rat-Mz": 1.034,
      "Vu": 398.27,
      "phiVn": 450.532,
      "Rat-V": 0.884,
      "CHK_STR": "NG",
      "CHK_RBR": "OK"
    }
  ]
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WC-TABLE"

# 以墙ID+层为单位查询 3F 的墙 1,3 及墙 10~12 的验算结果
payload = {
    "Argument": {
        "TABLE_TYPE": "WID+STORY",
        "SELECTIONS": [
            {"WALL_IDS": {"KEYS": [1, 3]}, "STORY": ["3F"]},
            {"WALL_IDS": {"TO": "10to12"}, "STORY": ["3F"]},
        ],
        "PRI_SORT": 1,
        "RESULT": 0,
        "TABLE_NAME": "RC Wall Check Result",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "COMPONENTS": ["WID", "Story", "Wall Mark", "Rat-My", "Rat-Mz", "Rat-V", "CHK_STR", "CHK_RBR"],
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
body = res.json()
for rec in body["DATA"]:      # DATA 为对象(dict)的数组
    print(rec["WID"], rec["Story"], rec["Wall Mark"], rec["CHK_STR"])
```

---

## 65. `DESIGN/RC/KDS-41-20-2022/WC-REPORT` — RC Wall Check Report (RC 墙体验算报告)

> **功能：** 将 RC 墙体验算结果导出为文件。墙体通过 `REPORT_TYPE` 决定输出单位（`"WID+STORY"`/`"WID"`），并分别用 `CURRENT_MODE_WID_STORY`/`CURRENT_MODE_WID` 指定模式（Graphic·Detail·Summary·PMCurve）。对象用 `SELECTIONS` 指定。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/WC-REPORT
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
      "properties": {
        "REPORT_TYPE": {
          "type": "string",
          "enum": [
            "WID+STORY",
            "WID"
          ],
          "default": "WID+STORY"
        },
        "CURRENT_MODE_WID_STORY": {
          "type": "string",
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
            },
            {
              "title": "PM Curve (JPG image)",
              "const": "PMCurve"
            }
          ]
        },
        "CURRENT_MODE_WID": {
          "type": "string",
          "oneOf": [
            {
              "title": "Graphic (JPG image)",
              "const": "Graphic"
            },
            {
              "title": "Summary (TXT text)",
              "const": "Summary"
            },
            {
              "title": "PM Curve (JPG image)",
              "const": "PMCurve"
            }
          ]
        },
        "SELECTIONS": {
          "type": "array",
          "minItems": 0,
          "items": {
            "type": "object",
            "properties": {
              "WALL_IDS": {
                "type": "object",
                "properties": {
                  "KEYS": {
                    "type": "array",
                    "items": {
                      "type": "integer"
                    }
                  },
                  "TO": {
                    "type": "string"
                  }
                },
                "oneOf": [
                  {
                    "required": [
                      "KEYS"
                    ],
                    "not": {
                      "required": [
                        "TO"
                      ]
                    }
                  },
                  {
                    "required": [
                      "TO"
                    ],
                    "not": {
                      "required": [
                        "KEYS"
                      ]
                    }
                  }
                ]
              },
              "STORY": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "OUTPUT_NAME": {
          "type": "string"
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
| 2 | 输出单位（`"WID+STORY"` / `"WID"`） | `"REPORT_TYPE"` | String (enum) | `"WID+STORY"` | **必填** |
| 3 | WID+STORY 模式（`Graphic`/`Detail`/`Summary`/`PMCurve`） | `"CURRENT_MODE_WID_STORY"` | String (oneOf) | — | 条件 |
| 4 | WID 模式（`Graphic`/`Summary`/`PMCurve`，不支持 Detail） | `"CURRENT_MODE_WID"` | String (oneOf) | — | 条件 |
| 5 | 墙/层选择列表（省略时全部） | `"SELECTIONS"` | Array[Object] | — | 可选 |
| 5.1 | 墙 ID（`KEYS` 或 `TO`） | `"WALL_IDS"` | Object | — | 可选 |
| 5.2 | 楼层名称列表 | `"STORY"` | Array[String] | — | 可选 |
| 6 | 报告保存目录路径 | `"EXPORT_PATH"` | String | — | **必填** |
| 7 | 输出文件基础名 | `"OUTPUT_NAME"` | String | — | **必填** |


### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "REPORT_TYPE": "WID+STORY",
    "CURRENT_MODE_WID_STORY": "Detail",
    "SELECTIONS": [
      {
        "WALL_IDS": {
          "KEYS": [
            1,
            3
          ]
        },
        "STORY": [
          "3F"
        ]
      },
      {
        "WALL_IDS": {
          "TO": "10to12"
        },
        "STORY": [
          "3F"
        ]
      }
    ],
    "EXPORT_PATH": "C:\\MIDAS\\Report\\",
    "OUTPUT_NAME": "RC_Wall_Report.jpg"
  }
}
```

**Response Body**

```json
{
  "SUCCESS": true,
  "FILE_PATH": "C:\\MIDAS\\Result\\RC_Wall_Report.jpg",
  "MESSAGE": ""
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/WC-REPORT"

# 保存 3F 的墙 1,3 及墙 10~12 的 Detail 报告（以 WID+STORY 为单位）
payload = {
    "Argument": {
        "REPORT_TYPE": "WID+STORY",
        "CURRENT_MODE_WID_STORY": "Detail",
        "SELECTIONS": [
            {"WALL_IDS": {"KEYS": [1, 3]}, "STORY": ["3F"]},
            {"WALL_IDS": {"TO": "10to12"}, "STORY": ["3F"]},
        ],
        "EXPORT_PATH": "C:\\MIDAS\\Report\\",
        "OUTPUT_NAME": "RC_Wall_Report.jpg",
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # {"SUCCESS": true, "FILE_PATH": "...", "MESSAGE": ""}
```

---
## 66. `DESIGN/RC/KDS-41-20-2022/CDESIGN` — RC Concrete Design Result (RC 混凝土综合设计结果)

> **功能：** 在屏幕上显示 RC 混凝土设计（梁·柱·支撑·墙体整合）结果并**截图为图像文件**。精细设置显示荷载组合、强度比成分（轴力/抗剪/受弯/组合）、配筋显示、构件种类过滤、数值/图例等图形选项。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/CDESIGN
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
        "FIGURE_NAME",
        "RESULT_GRAPHIC"
      ],
      "additionalProperties": false,
      "properties": {
        "EXPORT_PATH": {
          "type": "string",
          "description": "Image file save path and file name"
        },
        "FIGURE_NAME": {
          "type": "string",
          "description": "Smart report image name"
        },
        "WIDTH": {
          "type": "integer",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "HEIGHT": {
          "type": "integer",
          "default": 1000,
          "minimum": 100,
          "maximum": 10000
        },
        "STAGE_NAME": {
          "type": "string",
          "description": "Construction stage name"
        },
        "SET_HIDDEN": {
          "type": "boolean",
          "default": false
        },
        "ACTIVE": {
          "type": "object",
          "description": "View/Active settings"
        },
        "ANGLE": {
          "type": "object",
          "description": "View/Angle settings"
        },
        "DISPLAY": {
          "type": "object",
          "description": "View/Display settings"
        },
        "PERSPECTIVE": {
          "type": "boolean",
          "default": false
        },
        "ZOOM_LEVEL": {
          "type": "number",
          "default": 100,
          "minimum": 25,
          "maximum": 200
        },
        "BGCOLOR_TOP": {
          "type": "object",
          "properties": {
            "R": {
              "type": "integer"
            },
            "G": {
              "type": "integer"
            },
            "B": {
              "type": "integer"
            }
          }
        },
        "BGCOLOR_BOTTOM": {
          "type": "object",
          "properties": {
            "R": {
              "type": "integer"
            },
            "G": {
              "type": "integer"
            },
            "B": {
              "type": "integer"
            }
          }
        },
        "RESULT_GRAPHIC": {
          "type": "object",
          "required": [
            "LOAD_CASE_COMB"
          ],
          "properties": {
            "LOAD_CASE_COMB": {
              "type": "object",
              "required": [
                "TYPE",
                "NAME"
              ],
              "properties": {
                "TYPE": {
                  "type": "string",
                  "oneOf": [
                    {
                      "title": "Concrete Design Load Combination",
                      "const": "CBC"
                    }
                  ]
                },
                "NAME": {
                  "type": "string"
                }
              }
            },
            "COMPONENTS": {
              "type": "string",
              "default": "Combined",
              "oneOf": [
                {
                  "const": "Axial"
                },
                {
                  "const": "Shear-y"
                },
                {
                  "const": "Shear-z"
                },
                {
                  "const": "Bend-y"
                },
                {
                  "const": "Bend-z"
                },
                {
                  "const": "Combined"
                }
              ]
            },
            "TYPE_OF_DISPLAY": {
              "type": "object",
              "properties": {
                "CONTOUR": {
                  "type": "object"
                },
                "LEGEND": {
                  "type": "object"
                },
                "VALUES": {
                  "type": "object"
                }
              }
            },
            "REINFORCEMENT": {
              "type": "boolean",
              "default": true
            },
            "REINFORCEMENT_TYPE": {
              "type": "string",
              "default": "REBAR",
              "oneOf": [
                {
                  "const": "REBAR"
                },
                {
                  "const": "AREA"
                },
                {
                  "const": "RATIO"
                }
              ]
            },
            "DISPLAY_MEMBERS": {
              "type": "object",
              "properties": {
                "BEAM": {
                  "type": "boolean",
                  "default": true
                },
                "COLUMN": {
                  "type": "boolean",
                  "default": true
                },
                "BRACE": {
                  "type": "boolean",
                  "default": true
                },
                "WALL": {
                  "type": "boolean",
                  "default": true
                }
              }
            },
            "OUTPUT_COMPONENT": {
              "type": "object",
              "properties": {
                "RATIO_AXIAL_STRESS": {
                  "type": "boolean",
                  "default": true
                },
                "MAIN_REBAR": {
                  "type": "boolean",
                  "default": true
                },
                "SHEAR_REINFORCEMENT": {
                  "type": "boolean",
                  "default": true
                }
              }
            },
            "COLUMN_SECTION_SIZE": {
              "type": "object",
              "properties": {
                "SCALE_FACTOR": {
                  "type": "number",
                  "default": 1,
                  "minimum": 0.1,
                  "maximum": 100
                }
              }
            },
            "VALUE_OPTION": {
              "type": "object",
              "properties": {
                "DECIMAL_PLACES": {
                  "type": "integer",
                  "default": 2,
                  "minimum": 0,
                  "maximum": 15
                },
                "EXPONENTIAL": {
                  "type": "boolean",
                  "default": false
                }
              }
            },
            "OUTPUT_SECT_LOCATION": {
              "type": "object",
              "properties": {
                "OPT_I": {
                  "type": "boolean",
                  "default": false
                },
                "OPT_CENTER_MID": {
                  "type": "boolean",
                  "default": false
                },
                "OPT_J": {
                  "type": "boolean",
                  "default": false
                },
                "OPT_MAX": {
                  "type": "boolean",
                  "default": true
                },
                "OPT_ALL": {
                  "type": "boolean",
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
| 1 | Argument 包装 | `"Argument"` | Object | — | **必填** |
| 2 | 图像保存路径+文件名 | `"EXPORT_PATH"` | String | — | **必填** |
| 3 | 智能报告图像名称 | `"FIGURE_NAME"` | String | — | **必填** |
| 4 | 图像横向像素（100–10000） | `"WIDTH"` | Integer | `1000` | 可选 |
| 5 | 图像纵向像素（100–10000） | `"HEIGHT"` | Integer | `1000` | 可选 |
| 6 | 施工阶段名称 | `"STAGE_NAME"` | String | — | 可选 |
| 7 | Hidden 显示选项 | `"SET_HIDDEN"` | Boolean | `false` | 可选 |
| 8 | 画面 Active/Angle/Display 设置 | `"ACTIVE"`/`"ANGLE"`/`"DISPLAY"` | Object | — | 可选 |
| 9 | 透视（近大远小）视图 | `"PERSPECTIVE"` | Boolean | `false` | 可选 |
| 10 | 缩放级别（25=缩小，100=fit，200=最大） | `"ZOOM_LEVEL"` | Number | `100` | 可选 |
| 11 | 背景色上/下（RGB） | `"BGCOLOR_TOP"`/`"BGCOLOR_BOTTOM"` | Object | — | 可选 |
| 12 | 设计结果图形设置 | `"RESULT_GRAPHIC"` | Object | — | **必填** |
| 12.1 | 荷载工况/组合（`TYPE`=`"CBC"`，`NAME`） | `"LOAD_CASE_COMB"` | Object | — | **必填** |
| 12.2 | 强度比成分（`Axial`/`Shear-y`/`Shear-z`/`Bend-y`/`Bend-z`/`Combined`） | `"COMPONENTS"` | String (oneOf) | `"Combined"` | 可选 |
| 12.3 | 显示选项（`CONTOUR`/`LEGEND`/`VALUES`） | `"TYPE_OF_DISPLAY"` | Object | — | 可选 |
| 12.4 | 是否显示配筋 | `"REINFORCEMENT"` | Boolean | `true` | 可选 |
| 12.5 | 配筋显示类型（`REBAR`/`AREA`/`RATIO`） | `"REINFORCEMENT_TYPE"` | String (oneOf) | `"REBAR"` | 可选 |
| 12.6 | 显示构件种类（`BEAM`/`COLUMN`/`BRACE`/`WALL`） | `"DISPLAY_MEMBERS"` | Object | — | 可选 |
| 12.7 | 输出成分（`RATIO_AXIAL_STRESS`/`MAIN_REBAR`/`SHEAR_REINFORCEMENT`） | `"OUTPUT_COMPONENT"` | Object | — | 可选 |
| 12.8 | 显示柱截面尺寸（`SCALE_FACTOR` 0.1–100） | `"COLUMN_SECTION_SIZE"` | Object | — | 可选 |
| 12.9 | 数值显示格式（`DECIMAL_PLACES`/`EXPONENTIAL`） | `"VALUE_OPTION"` | Object | — | 可选 |
| 12.10 | 输出截面位置（`OPT_I`/`OPT_CENTER_MID`/`OPT_J`/`OPT_MAX`/`OPT_ALL`） | `"OUTPUT_SECT_LOCATION"` | Object | — | 可选 |

> `RESULT_GRAPHIC.LOAD_CASE_COMB` 为必填，其中 `TYPE` 是表示混凝土设计荷载组合的 `"CBC"`，`NAME` 为组合名称。仅当成分（`COMPONENTS`）为 `"Combined"` 时，`REINFORCEMENT` 相关的细粒度选项才有效。

### Request / Response JSON

> 手册中未另行发布 CDESIGN 的 Request/Response 示例。下面为**按 schema 必填字段构造的代表性请求**，响应为图像截图类端点的标准成功响应格式。

**POST Request Body**

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\Images\\rc_design.jpg",
    "FIGURE_NAME": "RC Concrete Design Result",
    "WIDTH": 1600,
    "HEIGHT": 1000,
    "SET_HIDDEN": true,
    "PERSPECTIVE": false,
    "ZOOM_LEVEL": 100,
    "RESULT_GRAPHIC": {
      "LOAD_CASE_COMB": {
        "TYPE": "CBC",
        "NAME": "cLCB1"
      },
      "COMPONENTS": "Combined",
      "REINFORCEMENT": true,
      "REINFORCEMENT_TYPE": "REBAR",
      "DISPLAY_MEMBERS": {
        "BEAM": true,
        "COLUMN": true,
        "BRACE": true,
        "WALL": true
      },
      "OUTPUT_COMPONENT": {
        "RATIO_AXIAL_STRESS": true,
        "MAIN_REBAR": true,
        "SHEAR_REINFORCEMENT": true
      },
      "OUTPUT_SECT_LOCATION": {
        "OPT_MAX": true
      }
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

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/CDESIGN"

# 将混凝土设计组合 cLCB1 的组合强度比（Combined）结果截图为图像
payload = {
    "Argument": {
        "EXPORT_PATH": "C:\\MIDAS\\Images\\rc_design.jpg",
        "FIGURE_NAME": "RC Concrete Design Result",
        "WIDTH": 1600,
        "HEIGHT": 1000,
        "SET_HIDDEN": True,
        "ZOOM_LEVEL": 100,
        "RESULT_GRAPHIC": {
            "LOAD_CASE_COMB": {"TYPE": "CBC", "NAME": "cLCB1"},
            "COMPONENTS": "Combined",
            "REINFORCEMENT": True,
            "REINFORCEMENT_TYPE": "REBAR",
            "DISPLAY_MEMBERS": {"BEAM": True, "COLUMN": True, "BRACE": True, "WALL": True},
            "OUTPUT_SECT_LOCATION": {"OPT_MAX": True},
        },
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
print(res.json())   # 成功时在指定路径生成图像文件
```

---

## 67. `DESIGN/RC/KDS-41-20-2022/TABLE` — Column Design Forces (柱设计内力)

> **功能：** 按荷载组合提取 RC 设计用 **柱（Column）构件设计内力**（三轴力·弯矩）。

> **共享 URI：** 第 67·68·69 项（柱·支撑·梁设计内力）**全部使用同一 URI `DESIGN/RC/KDS-41-20-2022/TABLE`(POST)**，仅以请求体的 `Argument.TABLE_TYPE` 取值（`"COLUMNDESIGNFORCES"`）区分。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`（本节固定为 `"COLUMNDESIGNFORCES"`）。主要属性如下。

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
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "COLUMNDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          },
          "oneOf": [
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
        "PARTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part2/4",
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
| 2 | 响应表格标题 | `"TABLE_NAME"` | String | `""` | 可选 |
| 3 | 结果表格类型（固定值 `"COLUMNDESIGNFORCES"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 4 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 5 | 单位设置（`FORCE`,`DIST`,`HEAT`,`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 6 | 数字格式（`FORMAT`,`PLACE`） | `"STYLES"` | Object | System | 可选 |
| 7 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |
| 8 | 节点/单元选择（`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一） | `"NODE_ELEMS"` | Object (oneOf) | — | 可选 |
| 9 | 单元部位（`"PartI"`/`"Part2/4"`/`"PartJ"`） | `"PARTS"` | Array[String] | `["All"]` | 可选 |


**`TABLE_TYPE` 取值：** `"COLUMNDESIGNFORCES"`

**Response HEAD 列说明**（在 `<TABLE_TYPE>` 键下以 `HEAD`/`DATA` 返回）：

| 列(HEAD) | 含义 |
|------|------|
| `Index` | 行索引 |
| `Memb` | 构件（单元）编号 |
| `Part` | 构件位置（I / 2·4 分点 / J） |
| `LComName` | 设计荷载组合名称 |
| `Type` | 极值种类（Max / Min） |
| `Fx` | 轴力（构件坐标系 x） |
| `Fy` | 剪力（y） |
| `Fz` | 剪力（z） |
| `Mx` | 扭转弯矩 |
| `My` | 弯矩（y 轴） |
| `Mz` | 弯矩（z 轴） |


> **参考：** 响应顶层键跟随请求的 `TABLE_NAME`。未指定 `TABLE_NAME` 时如示例那样以 `"empty"` 为键，指定文件路径时该字符串成为键。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "COLUMNDESIGNFORCES",
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
      "PartI"
    ],
    "NODE_ELEMS": {
      "KEYS": [
        915
      ]
    }
  }
}
```

**Response Body**（代表 DATA 3 行，每行长度 = HEAD 11 列）

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
        "915",
        "I",
        "cLCB5",
        "Max",
        "117.7094",
        "1.8682",
        "1.4004",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "2",
        "915",
        "I",
        "cLCB6",
        "Max",
        "134.8031",
        "2.2316",
        "1.8042",
        "0.0000",
        "0.0000",
        "0.0000"
      ],
      [
        "3",
        "915",
        "I",
        "cLCB7",
        "Max",
        "185.2628",
        "3.2994",
        "2.3477",
        "0.0000",
        "0.0000",
        "0.0000"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TABLE"   # 67·68·69 共用 URI

# 查询柱单元 915 的 I 端设计内力
payload = {
    "Argument": {
        "TABLE_TYPE": "COLUMNDESIGNFORCES",   # 选择柱设计内力
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
        "PARTS": ["PartI"],
        "NODE_ELEMS": {"KEYS": [915]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = next(iter(res.json().values()))   # 顶层键为 TABLE_NAME（未指定时为 "empty"）
print("HEAD:", table["HEAD"])
for row in table["DATA"][:5]:
    print(row)
```

---

## 68. `DESIGN/RC/KDS-41-20-2022/TABLE` — Brace Design Forces (支撑设计内力)

> **功能：** 提取 RC 设计用 **支撑（Brace）构件设计内力**（三轴力·弯矩）。响应列结构与柱相同。

> **共享 URI：** 第 67·68·69 项（柱·支撑·梁设计内力）**全部使用同一 URI `DESIGN/RC/KDS-41-20-2022/TABLE`(POST)**，仅以请求体的 `Argument.TABLE_TYPE` 取值（`"BRACEDESIGNFORCES"`）区分。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`（本节固定为 `"BRACEDESIGNFORCES"`）。主要属性如下。

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
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "BRACEDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
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
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          },
          "oneOf": [
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
        "PARTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part2/4",
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
| 2 | 响应表格标题 | `"TABLE_NAME"` | String | `""` | 可选 |
| 3 | 结果表格类型（固定值 `"BRACEDESIGNFORCES"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 4 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 5 | 单位设置（`FORCE`,`DIST`,`HEAT`,`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 6 | 数字格式（`FORMAT`,`PLACE`） | `"STYLES"` | Object | System | 可选 |
| 7 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |
| 8 | 节点/单元选择（`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一） | `"NODE_ELEMS"` | Object (oneOf) | — | 可选 |
| 9 | 单元部位（`"PartI"`/`"Part2/4"`/`"PartJ"`） | `"PARTS"` | Array[String] | `["All"]` | 可选 |


**`TABLE_TYPE` 取值：** `"BRACEDESIGNFORCES"`

**Response HEAD 列说明**（在 `<TABLE_TYPE>` 键下以 `HEAD`/`DATA` 返回）：

| 列(HEAD) | 含义 |
|------|------|
| `Index` | 行索引 |
| `Memb` | 构件（单元）编号 |
| `Part` | 构件位置（I / 2·4 分点 / J） |
| `LComName` | 设计荷载组合名称 |
| `Type` | 极值种类（Max / Min） |
| `Fx` | 轴力（构件坐标系 x） |
| `Fy` | 剪力（y） |
| `Fz` | 剪力（z） |
| `Mx` | 扭转弯矩 |
| `My` | 弯矩（y 轴） |
| `Mz` | 弯矩（z 轴） |


> **参考：** 响应顶层键跟随请求的 `TABLE_NAME`。未指定 `TABLE_NAME` 时如示例那样以 `"empty"` 为键，指定文件路径时该字符串成为键。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "BRACEDESIGNFORCES",
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
      "PartI"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        1039
      ]
    }
  }
}
```

**Response Body**（代表 DATA 3 行，每行长度 = HEAD 11 列）

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
        "1039",
        "I",
        "cLCB5",
        "Max",
        "0.000",
        "0.000",
        "19.261",
        "0.000",
        "-5.636",
        "0.000"
      ],
      [
        "2",
        "1039",
        "I",
        "cLCB6",
        "Max",
        "0.000",
        "0.000",
        "24.089",
        "0.000",
        "-6.988",
        "0.000"
      ],
      [
        "3",
        "1039",
        "I",
        "cLCB7",
        "Max",
        "0.000",
        "0.000",
        "34.656",
        "0.000",
        "-9.946",
        "0.000"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TABLE"   # 67·68·69 共用 URI

# 查询支撑单元 1039 的 I 端设计内力（KN、m、小数 3 位）
payload = {
    "Argument": {
        "TABLE_TYPE": "BRACEDESIGNFORCES",    # 选择支撑设计内力
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fx", "Fy", "Fz", "Mx", "My", "Mz"],
        "PARTS": ["PartI"],
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [1039]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = next(iter(res.json().values()))
for row in table["DATA"][:5]:
    print(row)
```

---

## 69. `DESIGN/RC/KDS-41-20-2022/TABLE` — Beam Design Forces (梁设计内力)

> **功能：** 提取 RC 设计用 **梁（Beam）构件设计内力**。提供受弯设计基准的剪力·扭转·正/负弯矩。

> **共享 URI：** 第 67·68·69 项（柱·支撑·梁设计内力）**全部使用同一 URI `DESIGN/RC/KDS-41-20-2022/TABLE`(POST)**，仅以请求体的 `Argument.TABLE_TYPE` 取值（`"BEAMDESIGNFORCES"`）区分。

### Input URI

```
{base url} + DESIGN/RC/KDS-41-20-2022/TABLE
```

### Active Methods

`POST`

### JSON Schema

`Argument` 的必填键为 `"TABLE_TYPE"`（本节固定为 `"BEAMDESIGNFORCES"`）。主要属性如下。

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
          "default": ""
        },
        "TABLE_TYPE": {
          "type": "string",
          "enum": [
            "BEAMDESIGNFORCES"
          ]
        },
        "EXPORT_PATH": {
          "type": "string"
        },
        "UNIT": {
          "type": "object",
          "properties": {
            "FORCE": {
              "type": "string"
            },
            "DIST": {
              "type": "string"
            },
            "HEAT": {
              "type": "string"
            },
            "TEMP": {
              "type": "string"
            }
          },
          "default": "System"
        },
        "STYLES": {
          "type": "object",
          "properties": {
            "FORMAT": {
              "type": "string",
              "enum": [
                "Default",
                "Fixed",
                "Scientific",
                "General"
              ]
            },
            "PLACE": {
              "type": "integer",
              "minimum": 0,
              "maximum": 15
            }
          },
          "default": "System"
        },
        "COMPONENTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "Index",
              "Memb",
              "Part",
              "LComName",
              "Type",
              "Fz",
              "Mx",
              "My(-)",
              "My(+)"
            ]
          }
        },
        "NODE_ELEMS": {
          "type": "object",
          "properties": {
            "KEYS": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            },
            "TO": {
              "type": "string"
            },
            "STRUCTURE_GROUP_NAME": {
              "type": "string"
            }
          },
          "oneOf": [
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
        "PARTS": {
          "type": "array",
          "items": {
            "type": "string",
            "enum": [
              "PartI",
              "Part2/4",
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
| 2 | 响应表格标题 | `"TABLE_NAME"` | String | `""` | 可选 |
| 3 | 结果表格类型（固定值 `"BEAMDESIGNFORCES"`） | `"TABLE_TYPE"` | String (enum) | — | **必填** |
| 4 | 结果保存路径 | `"EXPORT_PATH"` | String | — | 可选 |
| 5 | 单位设置（`FORCE`,`DIST`,`HEAT`,`TEMP`） | `"UNIT"` | Object | System | 可选 |
| 6 | 数字格式（`FORMAT`,`PLACE`） | `"STYLES"` | Object | System | 可选 |
| 7 | 输出列列表 | `"COMPONENTS"` | Array[String] | — | 可选 |
| 8 | 节点/单元选择（`KEYS`/`TO`/`STRUCTURE_GROUP_NAME` 之一） | `"NODE_ELEMS"` | Object (oneOf) | — | 可选 |
| 9 | 单元部位（`"PartI"`/`"Part2/4"`/`"PartJ"`） | `"PARTS"` | Array[String] | `["All"]` | 可选 |


**`TABLE_TYPE` 取值：** `"BEAMDESIGNFORCES"`

**Response HEAD 列说明**（在 `<TABLE_TYPE>` 键下以 `HEAD`/`DATA` 返回）：

| 列(HEAD) | 含义 |
|------|------|
| `Index` | 行索引 |
| `Memb` | 构件（单元）编号 |
| `Part` | 构件位置（I / 2·4 分点 / J） |
| `LComName` | 设计荷载组合名称 |
| `Type` | 极值种类（Max / Min） |
| `Fz` | 剪力（z） |
| `Mx` | 扭转弯矩 |
| `My(-)` | 负（-）弯矩 |
| `My(+)` | 正（+）弯矩 |


> **参考：** 响应顶层键跟随请求的 `TABLE_NAME`。未指定 `TABLE_NAME` 时如示例那样以 `"empty"` 为键，指定文件路径时该字符串成为键。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "C:\\MIDAS\\Result\\Beamresult.json",
    "TABLE_TYPE": "BEAMDESIGNFORCES",
    "COMPONENTS": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(-)",
      "My(+)"
    ],
    "PARTS": [
      "PartJ"
    ],
    "UNIT": {
      "FORCE": "KN",
      "DIST": "M"
    },
    "STYLES": {
      "FORMAT": "Fixed",
      "PLACE": 3
    },
    "NODE_ELEMS": {
      "KEYS": [
        984
      ]
    }
  }
}
```

**Response Body**（代表 DATA 3 行，每行长度 = HEAD 9 列）

```json
{
  "C:\\MIDAS\\Result\\Beamresult.json": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index",
      "Memb",
      "Part",
      "LComName",
      "Type",
      "Fz",
      "Mx",
      "My(-)",
      "My(+)"
    ],
    "DATA": [
      [
        "1",
        "984",
        "J",
        "cLCB100",
        "Max",
        "3.564",
        "0.000",
        "0.000",
        "3.845"
      ],
      [
        "2",
        "984",
        "J",
        "cLCB101",
        "Max",
        "3.884",
        "0.000",
        "0.000",
        "4.668"
      ],
      [
        "3",
        "984",
        "J",
        "cLCB102",
        "Max",
        "6.624",
        "0.000",
        "0.000",
        "6.045"
      ]
    ]
  }
}
```

### Python 示例

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"MAPI-Key": "在此填入已签发的密钥", "Content-Type": "application/json"}
URI = f"{BASE_URL}/DESIGN/RC/KDS-41-20-2022/TABLE"   # 67·68·69 共用 URI

# 查询梁单元 984 的 J 端设计内力，并同时保存为文件
payload = {
    "Argument": {
        "TABLE_NAME": "C:\\MIDAS\\Result\\Beamresult.json",  # 该字符串成为响应顶层键
        "TABLE_TYPE": "BEAMDESIGNFORCES",     # 选择梁设计内力
        "COMPONENTS": ["Index", "Memb", "Part", "LComName", "Type", "Fz", "Mx", "My(-)", "My(+)"],
        "PARTS": ["PartJ"],
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [984]},
    }
}
res = requests.post(URI, headers=HEADERS, json=payload)
res.raise_for_status()
table = next(iter(res.json().values()))
print("HEAD:", table["HEAD"])
for row in table["DATA"][:5]:
    print(row)
```

---
