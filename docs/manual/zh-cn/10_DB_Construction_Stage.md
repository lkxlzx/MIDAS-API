# 10. DB – Construction Stage / Heat of Hydration

施工阶段（Construction Stage）与水化热（Heat of Hydration）相关的数据库 API。

> **Base URL**
> - MIDAS CIVIL NX : `https://moa-engineers.midasit.com:443/civil`
> - MIDAS GEN NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **认证** ：所有请求头中需包含 `MAPI-Key: <your-api-key>`

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../10_DB_Construction_Stage.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

### Construction Stage Loads

| # | Endpoint | 说明 |
|---|----------|------|
| 1 | [/db/STAG](#1-dbstag--define-construction-stage) | 施工阶段定义 |
| 2 | [/db/CSCS](#2-dbcscs--composite-section-for-construction-stage) | 施工阶段组合截面 |
| 3 | [/db/TMLD](#3-dbtmld--time-loads-for-construction-stage) | 施工阶段时间荷载 |
| 4 | [/db/STBK](#4-dbstbk--set-back-loads-for-nonlinear-construction-stage) | 非线性施工阶段 Set-Back 荷载 |
| 5 | [/db/CMCS](#5-dbcmcs--camber-for-construction-stage) | 施工阶段预拱度 |
| 6 | [/db/CRPC](#6-dbcrpc--creep-coefficient-for-construction-stage) | 施工阶段徐变系数 |

### Heat of Hydration Loads

| # | Endpoint | 说明 |
|---|----------|------|
| 7 | [/db/ETFC](#7-dbetfc--ambient-temperature-functions) | 环境温度函数 |
| 8 | [/db/CCFC](#8-dbccfc--convection-coefficient-functions) | 对流系数函数 |
| 9 | [/db/HECB](#9-dbhecb--element-convection-boundary) | 单元对流边界 |
| 10 | [/db/HSPT](#10-dbhspt--prescribed-temperature) | 规定温度 |
| 11 | [/db/HSFC](#11-dbhsfc--heat-source-functions) | 热源函数 |
| 12 | [/db/HAHS](#12-dbhahs--assign-heat-source) | 指定热源 |
| 13 | [/db/HPCE](#13-dbhpce--pipe-cooling) | 水管冷却 |
| 14 | [/db/HSTG](#14-dbhstg--define-construction-stage-for-hydration) | 水化热施工阶段定义 |

---

## 1. /db/STAG – Define Construction Stage

定义施工阶段。逐阶段设置结构组·边界组·荷载组的激活/失效。

### 1-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/STAG` | 查询全部施工阶段 |
| `GET` | `{base_url}/db/STAG/{id}` | 查询特定 ID 的施工阶段 |
| `POST` | `{base_url}/db/STAG` | 创建施工阶段 |
| `PUT` | `{base_url}/db/STAG` | 修改全部施工阶段 |
| `PUT` | `{base_url}/db/STAG/{id}` | 修改特定 ID 的施工阶段 |
| `DELETE` | `{base_url}/db/STAG` | 删除全部施工阶段 |
| `DELETE` | `{base_url}/db/STAG/{id}` | 删除特定 ID 的施工阶段 |

### 1-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 施工阶段名 | `NAME` | String | - | Required |
| 2 | 施工阶段持续时间（天） | `DURATION` | Number | - | Required |
| 3 | 结果存储 – 阶段 | `bSV_RSLT` | Boolean | false | Optional |
| 4 | 结果存储 – 附加步 | `bSV_STEP` | Boolean | false | Optional |
| 5 | 是否使用材料非线性分析所需的荷载增量步 | `bLOAD_STEP` | Boolean | false | Optional |
| 6 | 荷载增量步数（bLOAD_STEP=true 时） | `INCRE_STEP` | Integer | - | Required |
| 7 | 附加步列表 | `ADD_STEP` | Array[Number] | [] | Optional |
| 8 | 结构组激活列表 | `ACT_ELEM` | Array[Object] | [] | Optional |
| (1) | 待激活的结构组名 | `GRUP_NAME` | String | - | Required |
| (2) | 材料龄期（天） | `AGE` | Number | 0 | Optional |
| 9 | 结构组失效列表 | `DACT_ELEM` | Array[Object] | [] | Optional |
| (1) | 待失效的结构组名 | `GRUP_NAME` | String | - | Required |
| (2) | 单元力重分配（%） | `REDIST` | Number | 0 | Optional |
| 10 | 边界组激活列表 | `ACT_BNGR` | Array[Object] | [] | Optional |
| (1) | 待激活的边界组名 | `BNGR_NAME` | String | - | Required |
| (2) | 支座/弹簧位置（`"DEFORMED"` / `"ORIGINAL"`） | `POS` | String | - | Required |
| 11 | 待失效的边界组名列表 | `DACT_BNGR` | Array[String] | [] | Optional |
| 12 | 荷载组激活列表 | `ACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 待激活的荷载组名 | `LOAD_NAME` | String | - | Required |
| (2) | 激活日（`"FIRST"` / `"LAST"` / 数字字符串） | `DAY` | String | `"FIRST"` | Optional |
| 13 | 荷载组失效列表 | `DACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 待失效的荷载组名 | `LOAD_NAME` | String | - | Required |
| (2) | 失效日（`"FIRST"` / `"LAST"` / 数字字符串） | `DAY` | String | `"FIRST"` | Optional |

### 1-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "CS01",
      "DURATION": 10,
      "bSV_RSLT": true,
      "bSV_STEP": true,
      "bLOAD_STEP": true,
      "INCRE_STEP": 5,
      "ADD_STEP": [5, 8],
      "ACT_ELEM": [
        {"GRUP_NAME": "SG_01", "AGE": 10}
      ],
      "ACT_BNGR": [
        {"BNGR_NAME": "BG_01", "POS": "DEFORMED"}
      ],
      "ACT_LOAD": [
        {"LOAD_NAME": "LG_01", "DAY": "5.000000"}
      ]
    },
    "2": {
      "NAME": "CS02",
      "DURATION": 20,
      "bSV_RSLT": true,
      "bSV_STEP": false,
      "bLOAD_STEP": false,
      "ADD_STEP": [],
      "ACT_ELEM": [
        {"GRUP_NAME": "SG_02", "AGE": 20}
      ],
      "ACT_BNGR": [
        {"BNGR_NAME": "BG_02", "POS": "DEFORMED"}
      ],
      "ACT_LOAD": [
        {"LOAD_NAME": "LG_02", "DAY": "FIRST"}
      ]
    },
    "3": {
      "NAME": "CS03",
      "DURATION": 10,
      "bSV_RSLT": true,
      "bSV_STEP": false,
      "bLOAD_STEP": false,
      "ADD_STEP": [],
      "DACT_ELEM": [
        {"GRUP_NAME": "SG_02", "REDIST": 100}
      ],
      "DACT_BNGR": ["BG_02"],
      "DACT_LOAD": [
        {"LOAD_NAME": "LG_02", "DAY": "FIRST"}
      ]
    }
  }
}
```

### 1-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建 3 个施工阶段 ──────────────────────────────────────────────────────
stages = {
    "Assign": {
        "1": {
            "NAME": "CS01",
            "DURATION": 14,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "PIER_01", "AGE": 14}],
            "ACT_BNGR": [{"BNGR_NAME": "FND_01", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_01", "DAY": "FIRST"}]
        },
        "2": {
            "NAME": "CS02",
            "DURATION": 28,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "GIRDER_01", "AGE": 28}],
            "ACT_BNGR": [{"BNGR_NAME": "BRG_01", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_02", "DAY": "FIRST"}]
        },
        "3": {
            "NAME": "CS03",
            "DURATION": 60,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_LOAD": [{"LOAD_NAME": "SDL", "DAY": "FIRST"}]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/STAG", json=stages, headers=HEADERS)
print("STAG POST:", resp.status_code)

# ── 查询全部施工阶段 ───────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/STAG", headers=HEADERS)
print("STAG GET:", resp.status_code)

# ── 修改特定阶段 ───────────────────────────────────────────────────────────
update = {
    "Assign": {
        "1": {
            "NAME": "CS01",
            "DURATION": 21,    # 14天 → 改为 21天
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "PIER_01", "AGE": 21}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_01", "DAY": "FIRST"}]
        }
    }
}
resp = requests.put(f"{BASE_URL}/db/STAG/1", json=update, headers=HEADERS)
print("STAG PUT/1:", resp.status_code)
```

---

## 2. /db/CSCS – Composite Section for Construction Stage

定义按施工阶段的组合截面。设置各 Part 的材料·龄期·刚度信息。

### 2-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/CSCS` | 查询全部 |
| `GET` | `{base_url}/db/CSCS/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/CSCS` | 创建 |
| `PUT` | `{base_url}/db/CSCS` | 修改全部 |
| `PUT` | `{base_url}/db/CSCS/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/CSCS` | 删除全部 |
| `DELETE` | `{base_url}/db/CSCS/{id}` | 删除特定 ID |

### 2-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 截面 ID | `SEC` | Integer | - | Required |
| 2 | 激活施工阶段名 | `ASTAGE` | String | - | Required |
| 3 | 组合类型（`"GENERAL"` / `"USER"`） | `TYPE` | String | - | Required |
| 4 | 是否为变截面类型 | `bTAP` | Boolean | false | Optional |
| 5 | Part 信息列表 | `vPARTINFO` | Array[Object] | - | Required |
| (1) | 组合截面 Part 编号 | `PART` | Integer | - | Required |
| (2) | 材料类型（`"ELEM"` / `"MATL"`） | `MTYPE` | String | - | Required |
| (3) | 材料 ID（MATL 类型：材料编号字符串，ELEM 类型：空字符串） | `MAT` | String | - | Optional |
| (4) | 组合阶段（激活阶段：空字符串，目标阶段：施工阶段名） | `CSTAGE` | String | Blank | Optional |
| (5) | 材料龄期（天） | `AGE` | Number | 0 | Optional |
| (6) | 构件的公称尺寸（h） | `PARTINFO_H` | Number | AUTO | Optional |
| (7) | 体积-表面积比（v/s） | `PARTINFO_VS` | Number | 0 | Optional |
| (8) | 暴露表面的模数（M） | `PARTINFO_M` | Number | 0 | Optional |
| (9) | 截面面积刚度缩放系数 | `AREA` | Number | 1 | Optional |
| (10) | 有效剪切面积（y轴）刚度缩放系数 | `ASY` | Number | 1 | Optional |
| (11) | 有效剪切面积（z轴）刚度缩放系数 | `ASZ` | Number | 1 | Optional |
| (12) | 抗扭刚度缩放系数 | `IXX` | Number | 1 | Optional |
| (13) | 惯性矩（y轴）刚度缩放系数 | `IYY` | Number | 1 | Optional |
| (14) | 惯性矩（z轴）刚度缩放系数 | `IZZ` | Number | 1 | Optional |
| (15) | 自重刚度缩放系数 | `WAREA` | Number | 1 | Optional |
| (16) | 翘曲常数刚度缩放系数 | `IW` | Number | 1 | Optional |
| 6 | 公称尺寸(h) 自动计算选项 | `OPT_UPDATE_ALL_H` | Boolean | - | Optional |

> ⚠️ **2026-08-25 确认：** `WAREA`（自重缩放系数）在原文 Specifications 表中，(14) `IZZ`
> 的下一项直接就是 (15) `IW`，该项完全缺失；但 JSON Schema 与 Request Example
> （下方 2-3 示例各 Part 中的 `"WAREA": 1`）里明确列在 `IZZ` 与 `IW` 之间 — 这是原文表自身的
> 遗漏，且示例优先于表（CLAUDE.md 原则），故已反映（文章 id `35987625234201`）。
> `OPT_UPDATE_ALL_H` 在原文表·示例中均无、仅存在于 JSON Schema — 需说明这是未经示例验证的
> Schema 专用字段。

`vPARTINFO` 的各 Part 除此之外还有下列仅存在于 JSON Schema、原文表与示例中均未出现的
字段。其用途（推测：至中性轴的距离为 GET 响应时的计算结果，`STIFF_USER*` 3 种是
`TYPE="USER"` 时的用户自定义刚度输入）系由字段名·说明推测而来，官方文档中没有说明，
故尚未确定。

| 说明 | Key | 值类型 | 备注 |
| --- | --- | --- | --- |
| Y轴至中性轴的距离 | `CY` | Number | （推测）查询结果时的值 |
| Z轴至中性轴的距离 | `CZ` | Number | （推测）查询结果时的值 |
| Y轴至中性轴的距离 – I端（变截面） | `CYI` | Number | （推测）查询结果时的值 |
| Z轴至中性轴的距离 – I端（变截面） | `CZI` | Number | （推测）查询结果时的值 |
| Y轴至中性轴的距离 – J端（变截面） | `CYJ` | Number | （推测）查询结果时的值 |
| Z轴至中性轴的距离 – J端（变截面） | `CZJ` | Number | （推测）查询结果时的值 |
| 用户自定义刚度（一般） | `STIFF_USER` | Object | （推测）`TYPE="USER"` 时使用 |
| 用户自定义刚度 – I端（变截面） | `STIFF_USER_TAPERED_I` | Object | （推测）`TYPE="USER"`+变截面时使用 |
| 用户自定义刚度 – J端（变截面） | `STIFF_USER_TAPERED_J` | Object | （推测）`TYPE="USER"`+变截面时使用 |

`STIFF_USER`/`STIFF_USER_TAPERED_I`/`STIFF_USER_TAPERED_J` 3 种均具有相同的子结构
（`AREA`/`ASY`/`ASZ`/`IXX`/`IYY`/`IZZ`/`CYP`/`CYM`/`CZP`/`CZM`/`QYB`/`QZB`/`X1`~`X4`/`Y1`~`Y4`/`IW`,
全部为 Number，说明在 Schema 上仅标注为 "Partial stiffness"）。

### 2-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "SEC": 1,
      "ASTAGE": "CS01",
      "TYPE": "GENERAL",
      "bTAP": false,
      "vPARTINFO": [
        {
          "PART": 1,
          "MTYPE": "ELEM",
          "MAT": "",
          "CSTAGE": "",
          "AGE": 2,
          "PARTINFO_H": 1.5,
          "PARTINFO_VS": 1.5,
          "PARTINFO_M": 1.5,
          "AREA": 1,
          "ASY": 1,
          "ASZ": 1,
          "IXX": 1,
          "IYY": 1,
          "IZZ": 1,
          "WAREA": 1,
          "IW": 1
        },
        {
          "PART": 2,
          "MTYPE": "MATL",
          "MAT": "3",
          "CSTAGE": "CS02",
          "AGE": 5,
          "PARTINFO_H": 0.245,
          "PARTINFO_VS": 0,
          "PARTINFO_M": 0,
          "AREA": 1,
          "ASY": 1,
          "ASZ": 1,
          "IXX": 1,
          "IYY": 1,
          "IZZ": 1,
          "WAREA": 1,
          "IW": 1
        }
      ]
    }
  }
}
```

### 2-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建施工阶段组合截面 ──────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "SEC": 1,
            "ASTAGE": "CS01",
            "TYPE": "GENERAL",
            "bTAP": False,
            "vPARTINFO": [
                {
                    "PART": 1,
                    "MTYPE": "ELEM",     # 使用单元材料
                    "MAT": "",
                    "CSTAGE": "",        # 激活阶段
                    "AGE": 3,
                    "PARTINFO_H": 1.2,
                    "PARTINFO_VS": 1.0,
                    "PARTINFO_M": 0.0,
                    "AREA": 1, "ASY": 1, "ASZ": 1,
                    "IXX": 1, "IYY": 1, "IZZ": 1,
                    "WAREA": 1, "IW": 1
                },
                {
                    "PART": 2,
                    "MTYPE": "MATL",     # 使用指定材料
                    "MAT": "2",          # 材料编号 2号
                    "CSTAGE": "CS02",    # 在 CS02 阶段组合
                    "AGE": 7,
                    "PARTINFO_H": 0.3,
                    "PARTINFO_VS": 0.0,
                    "PARTINFO_M": 0.0,
                    "AREA": 1, "ASY": 1, "ASZ": 1,
                    "IXX": 1, "IYY": 1, "IZZ": 1,
                    "WAREA": 1, "IW": 1
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/CSCS", json=payload, headers=HEADERS)
print("CSCS POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CSCS", headers=HEADERS)
print("CSCS GET:", resp.status_code)
```

---

## 3. /db/TMLD – Time Loads for Construction Stage

定义施工阶段中的时间荷载。为特定施工阶段(ID)指定荷载组与施加日。

### 3-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/TMLD` | 查询全部 |
| `GET` | `{base_url}/db/TMLD/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/TMLD` | 创建 |
| `PUT` | `{base_url}/db/TMLD` | 修改全部 |
| `PUT` | `{base_url}/db/TMLD/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/TMLD` | 删除全部 |
| `DELETE` | `{base_url}/db/TMLD/{id}` | 删除特定 ID |

### 3-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 施工阶段时间荷载列表 | `ITEMS` | Array[Object] | - | Required |
| (1) | 序号 | `ID` | Integer | 0 | Optional |
| (2) | 荷载组名 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 时间荷载（天） | `DAY` | Number | - | Required |

> **注意**：Assign 的键(ID)是施工阶段编号。时间荷载将应用于该施工阶段。

### 3-3. Request Body 示例

```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "DL_BC_2", "DAY": 35}
      ]
    },
    "11": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "DL_BC_2", "DAY": 25}
      ]
    }
  }
}
```

### 3-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建施工阶段时间荷载 ──────────────────────────────────────────────────
# Assign 键是施工阶段编号（STAG 的 ID）
payload = {
    "Assign": {
        "1": {    # 应用于施工阶段 1号
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SDL", "DAY": 30}
            ]
        },
        "2": {    # 应用于施工阶段 2号
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SDL",  "DAY": 45},
                {"ID": 2, "GROUP_NAME": "LIVE", "DAY": 60}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/TMLD", json=payload, headers=HEADERS)
print("TMLD POST:", resp.status_code)

# ── 查询特定施工阶段的时间荷载 ─────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/TMLD/1", headers=HEADERS)
print("TMLD GET/1:", resp.json())
```

---

## 4. /db/STBK – Set-Back Loads for Nonlinear Construction Stage

定义非线性施工阶段分析中的 Set-Back 荷载（基于节点位移）。

### 4-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/STBK` | 查询全部 |
| `GET` | `{base_url}/db/STBK/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/STBK` | 创建 |
| `PUT` | `{base_url}/db/STBK` | 修改全部 |
| `PUT` | `{base_url}/db/STBK/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/STBK` | 删除全部 |
| `DELETE` | `{base_url}/db/STBK/{id}` | 删除特定 ID |

### 4-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 节点 1 | `NODE1` | Integer | - | Required |
| 2 | 节点 2 | `NODE2` | Integer | - | Required |
| 3 | X 方向位移 | `DX` | Number | 0 | Optional |
| 4 | Y 方向位移 | `DY` | Number | 0 | Optional |
| 5 | Z 方向位移 | `DZ` | Number | 0 | Optional |
| 6 | 荷载工况名 | `LCNAME` | String | - | Required |
| 7 | 荷载组名 | `GROUP_NAME` | String | Blank | Optional |

### 4-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NODE1": 39,
      "NODE2": 22,
      "DX": 0.1,
      "DY": 0.2,
      "DZ": 0.3,
      "LCNAME": "LiveLoad",
      "GROUP_NAME": ""
    },
    "2": {
      "NODE1": 28,
      "NODE2": 21,
      "DX": 0.6,
      "DY": 0.1,
      "DZ": 0.1,
      "LCNAME": "DeadLoad",
      "GROUP_NAME": ""
    }
  }
}
```

### 4-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建 Set-Back 荷载 ───────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NODE1": 10,
            "NODE2": 20,
            "DX": 0.0,
            "DY": 0.005,   # Y 方向 5mm 位移
            "DZ": 0.0,
            "LCNAME": "DL",
            "GROUP_NAME": "LG_CS01"
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/STBK", json=payload, headers=HEADERS)
print("STBK POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/STBK", headers=HEADERS)
print("STBK GET:", resp.status_code)
```

---

## 5. /db/CMCS – Camber for Construction Stage

定义按施工阶段的节点预拱度（初始变形）。

### 5-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/CMCS` | 查询全部 |
| `GET` | `{base_url}/db/CMCS/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/CMCS` | 创建 |
| `PUT` | `{base_url}/db/CMCS` | 修改全部 |
| `PUT` | `{base_url}/db/CMCS/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/CMCS` | 删除全部 |
| `DELETE` | `{base_url}/db/CMCS/{id}` | 删除特定 ID |

### 5-2. 参数

> Assign 的键(ID)是节点编号。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 变形预拱度 | `DEFORM` | Number | - | Required |
| 2 | 用户自定义预拱度 | `USER` | Number | - | Required |

### 5-3. Request Body 示例

```json
{
  "Assign": {
    "23": {"DEFORM": 0.0,  "USER": 0.00 },
    "25": {"DEFORM": 0.1,  "USER": 0.17 },
    "27": {"DEFORM": 0.0,  "USER": 0.28 },
    "28": {"DEFORM": 0.0,  "USER": 0.34 },
    "29": {"DEFORM": 0.0,  "USER": 0.39 },
    "31": {"DEFORM": 0.0,  "USER": 0.46 },
    "33": {"DEFORM": 0.0,  "USER": 0.49 }
  }
}
```

### 5-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建节点预拱度 ───────────────────────────────────────────────────────────
# Assign 键是节点编号
camber_data = {}
node_cambers = {
    25: (0.10, 0.17),
    27: (0.00, 0.28),
    29: (0.00, 0.39),
    31: (0.00, 0.46),
    33: (0.00, 0.49),
}
for node_id, (deform, user) in node_cambers.items():
    camber_data[str(node_id)] = {"DEFORM": deform, "USER": user}

payload = {"Assign": camber_data}

resp = requests.post(f"{BASE_URL}/db/CMCS", json=payload, headers=HEADERS)
print("CMCS POST:", resp.status_code)

# ── 查询特定节点的预拱度 ──────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/CMCS/25", headers=HEADERS)
print("CMCS GET/25:", resp.json())
```

---

## 6. /db/CRPC – Creep Coefficient for Construction Stage

定义按施工阶段的徐变系数。

### 6-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/CRPC` | 查询全部 |
| `GET` | `{base_url}/db/CRPC/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/CRPC` | 创建 |
| `PUT` | `{base_url}/db/CRPC` | 修改全部 |
| `PUT` | `{base_url}/db/CRPC/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/CRPC` | 删除全部 |
| `DELETE` | `{base_url}/db/CRPC/{id}` | 删除特定 ID |

### 6-2. 参数

> Assign 的键(ID)是施工阶段编号。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 徐变系数列表 | `ITEMS` | Array[Object] | - | Required |
| (1) | 序号 | `ID` | Integer | 0 | Optional |
| (2) | 荷载组名 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 徐变系数 | `CREEP` | Number | - | Required |

### 6-3. Request Body 示例

```json
{
  "Assign": {
    "25": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "2ndDeadLoad", "CREEP": 1.2}
      ]
    },
    "26": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "Selfweight", "CREEP": 1.5}
      ]
    }
  }
}
```

### 6-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建施工阶段徐变系数 ────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {    # 施工阶段 1号
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SW",  "CREEP": 1.5},
                {"ID": 2, "GROUP_NAME": "SDL", "CREEP": 1.2}
            ]
        },
        "2": {    # 施工阶段 2号
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SW",  "CREEP": 2.0}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/CRPC", json=payload, headers=HEADERS)
print("CRPC POST:", resp.status_code)
```

---

## 7. /db/ETFC – Ambient Temperature Functions

定义水化热分析使用的环境温度函数。

### 7-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/ETFC` | 查询全部 |
| `GET` | `{base_url}/db/ETFC/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/ETFC` | 创建 |
| `PUT` | `{base_url}/db/ETFC` | 修改全部 |
| `PUT` | `{base_url}/db/ETFC/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/ETFC` | 删除全部 |
| `DELETE` | `{base_url}/db/ETFC/{id}` | 删除特定 ID |

### 7-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 函数名 | `NAME` | String | - | Required |
| 2 | 函数类型（`"CONST"` / `"SINE"` / `"USER"`） | `TYPE` | String | - | Required |

**Constant 类型（TYPE="CONST"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 温度 | `TEMP` | Number | 0 | Optional |

**Sine Function 类型（TYPE="SINE"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 最高温度（T） | `MAX_TEMP` | Number | 0 | Optional |
| 平均温度（To） | `MEAN_TEMP` | Number | 0 | Optional |
| 延迟时间（to） | `DELAY_TIME` | Number | 0 | Optional |

**User 类型（TYPE="USER"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 缩放系数 | `SCALE_FACTOR` | Number | - | Required |
| 函数数据列表 | `ITEM` | Array[Object] | - | Required |
| - 时间 | `TIME` | Number | - | Required |
| - 温度 | `VALUE` | Number | - | Required |

### 7-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "AmbientTemp_Const",
      "TYPE": "CONST",
      "TEMP": 30
    },
    "2": {
      "NAME": "AmbientTemp_User",
      "TYPE": "USER",
      "SCALE_FACTOR": 1,
      "ITEM": [
        {"TIME": 0, "VALUE": 20},
        {"TIME": 1, "VALUE": 30},
        {"TIME": 2, "VALUE": 40}
      ]
    },
    "3": {
      "NAME": "AmbientTemp_Sine",
      "TYPE": "SINE",
      "MAX_TEMP": 20,
      "MEAN_TEMP": 0,
      "DELAY_TIME": 1
    }
  }
}
```

### 7-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建环境温度函数 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "AT_Summer",
            "TYPE": "SINE",
            "MAX_TEMP": 35.0,    # 最高温度 35°C
            "MEAN_TEMP": 20.0,   # 平均温度 20°C
            "DELAY_TIME": 6.0    # 延迟时间 6小时
        },
        "2": {
            "NAME": "AT_Winter",
            "TYPE": "CONST",
            "TEMP": 5.0          # 恒定温度 5°C
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/ETFC", json=payload, headers=HEADERS)
print("ETFC POST:", resp.status_code)
```

---

## 8. /db/CCFC – Convection Coefficient Functions

定义水化热分析使用的对流系数函数。

### 8-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/CCFC` | 查询全部 |
| `GET` | `{base_url}/db/CCFC/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/CCFC` | 创建 |
| `PUT` | `{base_url}/db/CCFC` | 修改全部 |
| `PUT` | `{base_url}/db/CCFC/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/CCFC` | 删除全部 |
| `DELETE` | `{base_url}/db/CCFC/{id}` | 删除特定 ID |

### 8-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 函数名 | `NAME` | String | - | Required |
| 2 | 函数类型（`"CONST"` / `"USER"`） | `TYPE` | String | - | Required |

**Constant 类型（TYPE="CONST"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 对流系数 | `COEF` | Number | - | Required |

**User 类型（TYPE="USER"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 缩放系数 | `SCALE_FACTOR` | Number | - | Required |
| 函数数据列表 | `ITEM` | Array[Object] | - | Required |
| - 时间 | `TIME` | Number | - | Required |
| - 对流系数 | `VALUE` | Number | - | Required |

### 8-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "CC_Const",
      "TYPE": "CONST",
      "COEF": 15
    },
    "2": {
      "NAME": "CC_User",
      "TYPE": "USER",
      "SCALE_FACTOR": 1.2,
      "ITEM": [
        {"TIME": 0, "VALUE": 25},
        {"TIME": 1, "VALUE": 35}
      ]
    }
  }
}
```

### 8-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建对流系数函数 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "CC_Standard",
            "TYPE": "CONST",
            "COEF": 12.0    # 对流系数 12 W/(m²·K)
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/CCFC", json=payload, headers=HEADERS)
print("CCFC POST:", resp.status_code)
```

---

## 9. /db/HECB – Element Convection Boundary

定义水化热分析中单元的对流边界条件。

### 9-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/HECB` | 查询全部 |
| `GET` | `{base_url}/db/HECB/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/HECB` | 创建 |
| `PUT` | `{base_url}/db/HECB` | 修改全部 |
| `PUT` | `{base_url}/db/HECB/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/HECB` | 删除全部 |
| `DELETE` | `{base_url}/db/HECB/{id}` | 删除特定 ID |

### 9-2. 参数

> Assign 的键(ID)是施工阶段编号。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 单元对流边界列表 | `ITEMS` | Array[Object] | - | Required |
| (1) | 序号 | `ID` | Integer | 0 | Optional |
| (2) | 边界组名 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 面编号（Face#1 ~ Face#6） | `FACE_NO` | Integer | - | Required |
| (4) | 对流系数函数名 | `CCFC_NAME` | String | - | Required |
| (5) | 环境温度函数名 | `ETFC_NAME` | String | - | Required |

### 9-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "FACE_NO": 1,
          "CCFC_NAME": "CC_Standard",
          "ETFC_NAME": "AT_Summer"
        },
        {
          "ID": 2,
          "GROUP_NAME": "",
          "FACE_NO": 2,
          "CCFC_NAME": "CC_Standard",
          "ETFC_NAME": "AT_Summer"
        }
      ]
    }
  }
}
```

### 9-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建单元对流边界 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {    # 施工阶段 1号
            "ITEMS": [
                {
                    "ID": 1,
                    "GROUP_NAME": "BG_SURF",
                    "FACE_NO": 1,              # 上表面（Face #1）
                    "CCFC_NAME": "CC_Standard",
                    "ETFC_NAME": "AT_Summer"
                },
                {
                    "ID": 2,
                    "GROUP_NAME": "BG_SIDE",
                    "FACE_NO": 2,              # 侧面（Face #2）
                    "CCFC_NAME": "CC_Standard",
                    "ETFC_NAME": "AT_Summer"
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HECB", json=payload, headers=HEADERS)
print("HECB POST:", resp.status_code)
```

---

## 10. /db/HSPT – Prescribed Temperature

定义水化热分析中节点的规定温度。

### 10-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/HSPT` | 查询全部 |
| `GET` | `{base_url}/db/HSPT/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/HSPT` | 创建 |
| `PUT` | `{base_url}/db/HSPT` | 修改全部 |
| `PUT` | `{base_url}/db/HSPT/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/HSPT` | 删除全部 |
| `DELETE` | `{base_url}/db/HSPT/{id}` | 删除特定 ID |

### 10-2. 参数

> Assign 的键(ID)是施工阶段编号。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 规定温度列表 | `ITEMS` | Array[Object] | - | Required |
| (1) | 序号 | `ID` | Integer | 0 | Optional |
| (2) | 边界组名 | `GROUP_NAME` | String | Blank | Optional |
| (3) | 温度 | `TEMPER` | Number | - | Required |

### 10-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "", "TEMPER": 25}
      ]
    },
    "2": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "", "TEMPER": 25}
      ]
    },
    "3": {
      "ITEMS": [
        {"ID": 1, "GROUP_NAME": "", "TEMPER": 20}
      ]
    }
  }
}
```

### 10-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建规定温度 ───────────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {    # 施工阶段 1号
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "BG_BASE", "TEMPER": 15.0}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HSPT", json=payload, headers=HEADERS)
print("HSPT POST:", resp.status_code)
```

---

## 11. /db/HSFC – Heat Source Functions

定义水化热分析使用的热源函数。支持 Constant、Code（函数）、User 类型。

### 11-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/HSFC` | 查询全部 |
| `GET` | `{base_url}/db/HSFC/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/HSFC` | 创建 |
| `PUT` | `{base_url}/db/HSFC` | 修改全部 |
| `PUT` | `{base_url}/db/HSFC/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/HSFC` | 删除全部 |
| `DELETE` | `{base_url}/db/HSFC/{id}` | 删除特定 ID |

### 11-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 函数名 | `NAME` | String | - | Required |
| 2 | 函数类型（`"CONST"` / `"FUNC"` / `"USER"`） | `TYPE` | String | - | Required |

**Constant 类型（TYPE="CONST"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 热源温度 | `TEMP_CONST` | Number | 0 | Optional |

**Code 类型（TYPE="FUNC"）– 不使用混凝土数据的附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 是否使用混凝土数据（`false`） | `OPT_USE_CONC_DATA` | Boolean | false | Optional |
| 最大绝热温升（K） | `K` | Number | 0 | Optional |
| 反应速率系数（a） | `ALPHA` | Number | 0 | Optional |

**Code 类型（TYPE="FUNC"）– 使用混凝土数据的附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 是否使用混凝土数据（`true`） | `OPT_USE_CONC_DATA` | Boolean | false | Optional |
| 水泥类型（0=普通，1=中热，2=早强，3=高炉矿渣，4=粉煤灰） | `CEMENT_TYPE` | Integer | 0 | Optional |
| 温度（0=10°C，1=20°C，2=30°C） | `TEMP_FUNC` | Integer | 0 | Optional |
| 水泥含量 | `CEMENT_CONT` | Number | 0 | Optional |

**User 类型（TYPE="USER"）附加参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 数据类型（false=热源，true=温度） | `IS_ADIABATIC_TEMP` | Boolean | true | Optional |
| 缩放系数 | `SCALE_FACTOR` | Number | - | Required |
| 函数数据列表 | `ITEM` | Array[Object] | - | Required |
| - 时间 | `TIME` | Number | - | Required |
| - 值（温度或热源） | `VALUE` | Number | - | Required |

### 11-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "HS_User",
      "TYPE": "USER",
      "IS_ADIABATIC_TEMP": false,
      "SCALE_FACTOR": 1,
      "ITEM": [
        {"TIME": 0, "VALUE": 0},
        {"TIME": 1, "VALUE": 5},
        {"TIME": 2, "VALUE": 10}
      ]
    },
    "2": {
      "NAME": "HS_Const",
      "TYPE": "CONST",
      "TEMP_CONST": 10
    },
    "3": {
      "NAME": "HS_Code_NoConc",
      "TYPE": "FUNC",
      "OPT_USE_CONC_DATA": false,
      "K": 20,
      "ALPHA": 0
    },
    "4": {
      "NAME": "HS_Code_Conc",
      "TYPE": "FUNC",
      "OPT_USE_CONC_DATA": true,
      "CEMENT_TYPE": 0,
      "TEMP_FUNC": 1,
      "CEMENT_CONT": 2400
    }
  }
}
```

### 11-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建热源函数（3 种类型）──────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "HSF_Adiabatic",
            "TYPE": "FUNC",
            "OPT_USE_CONC_DATA": True,
            "CEMENT_TYPE": 0,   # 普通硅酸盐水泥
            "TEMP_FUNC": 1,     # 20°C
            "CEMENT_CONT": 300  # 水泥含量 300 kg/m³
        },
        "2": {
            "NAME": "HSF_UserDefined",
            "TYPE": "USER",
            "IS_ADIABATIC_TEMP": True,   # 绝热温度数据
            "SCALE_FACTOR": 1.0,
            "ITEM": [
                {"TIME": 0,  "VALUE":  0.0},
                {"TIME": 1,  "VALUE":  8.5},
                {"TIME": 3,  "VALUE": 18.2},
                {"TIME": 7,  "VALUE": 25.6},
                {"TIME": 14, "VALUE": 30.1},
                {"TIME": 28, "VALUE": 33.5}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HSFC", json=payload, headers=HEADERS)
print("HSFC POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/HSFC", headers=HEADERS)
print("HSFC GET:", resp.status_code)
```

---

## 12. /db/HAHS – Assign Heat Source

为单元指定热源函数。

### 12-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/HAHS` | 查询全部 |
| `GET` | `{base_url}/db/HAHS/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/HAHS` | 创建 |
| `PUT` | `{base_url}/db/HAHS` | 修改全部 |
| `PUT` | `{base_url}/db/HAHS/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/HAHS` | 删除全部 |
| `DELETE` | `{base_url}/db/HAHS/{id}` | 删除特定 ID |

### 12-2. 参数

> Assign 的键(ID)是单元编号。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 热源函数名 | `FUNC_NAME` | String | - | Required |

### 12-3. Request Body 示例

```json
{
  "Assign": {
    "358": {"FUNC_NAME": "HSF_Adiabatic"},
    "359": {"FUNC_NAME": "HSF_Adiabatic"},
    "360": {"FUNC_NAME": "HSF_UserDefined"}
  }
}
```

### 12-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 为单元指定热源函数 ────────────────────────────────────────────────────
# Assign 键是单元编号
elem_ids = list(range(100, 150))  # 单元 100 ~ 149号
payload = {
    "Assign": {
        str(eid): {"FUNC_NAME": "HSF_Adiabatic"}
        for eid in elem_ids
    }
}

resp = requests.post(f"{BASE_URL}/db/HAHS", json=payload, headers=HEADERS)
print("HAHS POST:", resp.status_code)

# ── 查询特定单元 ───────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/HAHS/100", headers=HEADERS)
print("HAHS GET/100:", resp.json())
```

---

## 13. /db/HPCE – Pipe Cooling

定义水化热分析中的水管冷却系统。

### 13-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/HPCE` | 查询全部 |
| `GET` | `{base_url}/db/HPCE/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/HPCE` | 创建 |
| `PUT` | `{base_url}/db/HPCE` | 修改全部 |
| `PUT` | `{base_url}/db/HPCE/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/HPCE` | 删除全部 |
| `DELETE` | `{base_url}/db/HPCE/{id}` | 删除特定 ID |

### 13-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 水管冷却名称 | `NAME` | String | - | Required |
| 2 | 管径 | `DIAMETER` | Number | 0 | Optional |
| 3 | 对流系数 | `COEF` | Number | 0 | Optional |
| 4 | 比热 | `HEAT` | Number | 0 | Optional |
| 5 | 单位重量密度 | `DENSITY` | Number | 0 | Optional |
| 6 | 进水温度 | `TEMPER` | Number | 0 | Optional |
| 7 | 流量 | `FLOW_RATE` | Number | 0 | Optional |
| 8 | 通水开始时间 | `START_TIME` | Integer | 0 | Optional |
| 9 | 通水结束时间 | `END_TIME` | Integer | 0 | Optional |
| 10 | 节点列表 | `ITEMS` | Array[Integer] | - | Required |

### 13-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "PC_Row1",
      "DIAMETER": 0.025,
      "COEF": 850,
      "HEAT": 4200,
      "DENSITY": 1000,
      "TEMPER": 15,
      "FLOW_RATE": 20,
      "START_TIME": 0,
      "END_TIME": 168,
      "ITEMS": [1, 2, 3, 4, 5, 6]
    }
  }
}
```

### 13-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建水管冷却 ─────────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "PC_Layer1",
            "DIAMETER": 0.025,    # 管径 25mm
            "COEF": 850,          # 对流系数 850 W/(m²·K)
            "HEAT": 4200,         # 比热 4200 J/(kg·K)（水）
            "DENSITY": 1000,      # 密度 1000 kg/m³（水）
            "TEMPER": 15.0,       # 进水温度 15°C
            "FLOW_RATE": 15.0,    # 流量 15 L/min
            "START_TIME": 0,      # 通水开始 0小时
            "END_TIME": 168,      # 通水结束 7天（168小时）
            "ITEMS": [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HPCE", json=payload, headers=HEADERS)
print("HPCE POST:", resp.status_code)
```

---

## 14. /db/HSTG – Define Construction Stage for Hydration

定义水化热分析专用的施工阶段。

### 14-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/HSTG` | 查询全部 |
| `GET` | `{base_url}/db/HSTG/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/HSTG` | 创建 |
| `PUT` | `{base_url}/db/HSTG` | 修改全部 |
| `PUT` | `{base_url}/db/HSTG/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/HSTG` | 删除全部 |
| `DELETE` | `{base_url}/db/HSTG/{id}` | 删除特定 ID |

### 14-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 水化热阶段名 | `NAME` | String | - | Required |
| 2 | 是否使用初始温度 | `bINITAL_TEMP` | Boolean | false | Optional |
| 3 | 初始温度 | `INITIAL_TEMP` | Number | - | Optional |
| 4 | 附加步列表 | `ADD_STEP` | Array[Number] | - | Required |
| 5 | 激活结构组列表 | `ACT_ELEM` | Array[String] | - | Required |
| 6 | 激活边界组列表 | `ACT_BNGR` | Array[String] | - | Required |
| 7 | 失效边界组列表 | `DACT_BNGR` | Array[String] | - | Required |
| 8 | 激活荷载组列表 | `ACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 荷载工况名 | `LOAD_NAME` | String | - | Optional |
| (2) | 激活日 | `DAY` | String | - | Optional |
| 9 | 失效荷载组列表 | `DACT_LOAD` | Array[Object] | [] | Optional |
| (1) | 荷载工况名 | `LOAD_NAME` | String | - | Optional |
| (2) | 失效日 | `DAY` | String | - | Optional |

### 14-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "HY_CS01",
      "bINITAL_TEMP": true,
      "INITIAL_TEMP": 25,
      "ADD_STEP": [10, 20, 30, 45, 60, 80, 100, 130, 170, 250, 350, 500, 700, 1000],
      "ACT_ELEM": ["GR2", "GR1"],
      "ACT_BNGR": ["BNGR3", "BNGR2", "BNGR1"],
      "DACT_BNGR": ["BNGR4"],
      "ACT_LOAD": [
        {"LOAD_NAME": "LG01", "DAY": "10.000000"}
      ],
      "DACT_LOAD": [
        {"LOAD_NAME": "LG02", "DAY": "80.000000"}
      ]
    }
  }
}
```

### 14-4. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 创建水化热施工阶段 ─────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "HY_Pour_01",
            "bINITAL_TEMP": True,
            "INITIAL_TEMP": 20.0,       # 初始浇筑温度 20°C
            "ADD_STEP": [
                1, 3, 7, 14, 28, 60, 90, 180, 365
            ],
            "ACT_ELEM": ["ConcGroup_01"],
            "ACT_BNGR": ["FormWork_01"],
            "DACT_BNGR": [],
            "ACT_LOAD": [
                {"LOAD_NAME": "HeatSrc_01", "DAY": "1.000000"}
            ],
            "DACT_LOAD": [
                {"LOAD_NAME": "FormWork_Load", "DAY": "14.000000"}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/HSTG", json=payload, headers=HEADERS)
print("HSTG POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/HSTG", headers=HEADERS)
print("HSTG GET:", resp.status_code)
```

---

## End-to-End 工作流示例

桥梁施工阶段分析 + 水化热分析的典型设置流程。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── STEP 1: 定义施工阶段 (STAG) ────────────────────────────────────────────
stag = {
    "Assign": {
        "1": {
            "NAME": "CS01_Pier",
            "DURATION": 14,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "PIER", "AGE": 14}],
            "ACT_BNGR": [{"BNGR_NAME": "FND", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_PIER", "DAY": "FIRST"}]
        },
        "2": {
            "NAME": "CS02_Girder",
            "DURATION": 28,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_ELEM": [{"GRUP_NAME": "GIRDER", "AGE": 28}],
            "ACT_BNGR": [{"BNGR_NAME": "BRG", "POS": "DEFORMED"}],
            "ACT_LOAD": [{"LOAD_NAME": "SW_GIRDER", "DAY": "FIRST"}]
        },
        "3": {
            "NAME": "CS03_SDL",
            "DURATION": 90,
            "bSV_RSLT": True,
            "bSV_STEP": False,
            "bLOAD_STEP": False,
            "ADD_STEP": [],
            "ACT_LOAD": [{"LOAD_NAME": "SDL", "DAY": "FIRST"}]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/STAG", json=stag, headers=HEADERS)
print("STEP 1 - STAG:", r.status_code)

# ── STEP 2: 按施工阶段的徐变系数 (CRPC) ───────────────────────────────────
crpc = {
    "Assign": {
        "2": {    # CS02 阶段
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SW_PIER",   "CREEP": 1.5},
                {"ID": 2, "GROUP_NAME": "SW_GIRDER",  "CREEP": 1.2}
            ]
        },
        "3": {    # CS03 阶段
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "SDL", "CREEP": 2.0}
            ]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/CRPC", json=crpc, headers=HEADERS)
print("STEP 2 - CRPC:", r.status_code)

# ── STEP 3: 水化热环境温度函数 (ETFC) ────────────────────────────────────
etfc = {
    "Assign": {
        "1": {"NAME": "AT_25C", "TYPE": "CONST", "TEMP": 25}
    }
}
r = requests.post(f"{BASE_URL}/db/ETFC", json=etfc, headers=HEADERS)
print("STEP 3 - ETFC:", r.status_code)

# ── STEP 4: 水化热对流系数函数 (CCFC) ────────────────────────────────────
ccfc = {
    "Assign": {
        "1": {"NAME": "CC_12", "TYPE": "CONST", "COEF": 12.0}
    }
}
r = requests.post(f"{BASE_URL}/db/CCFC", json=ccfc, headers=HEADERS)
print("STEP 4 - CCFC:", r.status_code)

# ── STEP 5: 热源函数 (HSFC) ─────────────────────────────────────────────────
hsfc = {
    "Assign": {
        "1": {
            "NAME": "HS_OPC",
            "TYPE": "FUNC",
            "OPT_USE_CONC_DATA": True,
            "CEMENT_TYPE": 0,    # 普通硅酸盐
            "TEMP_FUNC": 1,      # 20°C
            "CEMENT_CONT": 320
        }
    }
}
r = requests.post(f"{BASE_URL}/db/HSFC", json=hsfc, headers=HEADERS)
print("STEP 5 - HSFC:", r.status_code)

# ── STEP 6: 为单元指定热源 (HAHS) ─────────────────────────────────────────
hahs = {
    "Assign": {
        str(eid): {"FUNC_NAME": "HS_OPC"}
        for eid in range(1, 51)    # 单元 1~50号
    }
}
r = requests.post(f"{BASE_URL}/db/HAHS", json=hahs, headers=HEADERS)
print("STEP 6 - HAHS:", r.status_code)

# ── STEP 7: 单元对流边界 (HECB) ───────────────────────────────────────────
hecb = {
    "Assign": {
        "1": {    # 施工阶段 1号
            "ITEMS": [
                {"ID": 1, "GROUP_NAME": "", "FACE_NO": 1, "CCFC_NAME": "CC_12", "ETFC_NAME": "AT_25C"},
                {"ID": 2, "GROUP_NAME": "", "FACE_NO": 2, "CCFC_NAME": "CC_12", "ETFC_NAME": "AT_25C"}
            ]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/HECB", json=hecb, headers=HEADERS)
print("STEP 7 - HECB:", r.status_code)

# ── STEP 8: 定义水化热施工阶段 (HSTG) ─────────────────────────────────────
hstg = {
    "Assign": {
        "1": {
            "NAME": "HY_CS01",
            "bINITAL_TEMP": True,
            "INITIAL_TEMP": 25,
            "ADD_STEP": [1, 3, 7, 14, 28, 60, 90],
            "ACT_ELEM": ["PIER", "GIRDER"],
            "ACT_BNGR": ["FND", "BRG"],
            "DACT_BNGR": [],
            "ACT_LOAD":  [],
            "DACT_LOAD": []
        }
    }
}
r = requests.post(f"{BASE_URL}/db/HSTG", json=hstg, headers=HEADERS)
print("STEP 8 - HSTG:", r.status_code)

print("\n=== 施工阶段 / 水化热设置完成 ===")
```

---

*下一部分：[11_DB_Settlement_Misc_Loads.md](./11_DB_Settlement_Misc_Loads.md)*
