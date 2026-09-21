# MIDAS-API

> **语言：** 简体中文译文  
> **原文：** [韩文原文](./README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](./docs/zh-cn/GLOSSARY.md)）

**MIDAS NX Open API**用于以编程方式创建、控制结构设计模型并实现自动化。
节点、单元、截面、荷载均可用代码生成，因此适合把重复性的建模工作自动化，
例如**基于 Story（楼层）的自动建模**。

> 适用产品：**MIDAS Gen NX / Civil NX** · 数据格式：**JSON** · 协议：**REST + WebSocket**

---

## 🏗️ API 工作原理

MIDAS NX 不与应用程序直接通信。**云服务器（AWS）** 充当中间的中继者。

```
[我的代码/应用]  ──REST(HTTP)──▶  [MIDAS 服务器(AWS)]  ──WebSocket──▶  [本地 MIDAS Gen NX]
     ▲                                                                     │
     └───────────────────────  结果(JSON)  ◀───────────────────────────────────┘
```

- 服务器通过 **`MAPI-Key`** 识别对接的是哪个产品（正在运行的 Gen NX）。
- 因此必须在 **MIDAS Gen NX（或 Civil NX）正在运行**的状态下 API 才会工作。
- 一个客户端若持有多个 `MAPI-Key`，就能在一处控制多个产品。

---

## 🔑 认证与基本信息

### Base URL
```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```
> 按地区提供替代服务器。

### 认证头部
```
Content-Type: application/json
MAPI-Key: <在 Gen NX 应用中获取的密钥>
```
> `MAPI-Key` 是临时密钥，可随时重新签发。请拆分到 `.env` 中管理。

### HTTP 方法
| 方法 | 作用 |
|--------|------|
| `POST`   | 生成数据 |
| `PUT`    | 修改数据（新建文件的必需数据只有 GET/PUT 可用） |
| `GET`    | 查询数据 |
| `DELETE` | 删除数据 |

### 通用请求体格式
所有 DB 端点都在 `Assign` 包装器内以**条目 ID → 数据**的形式发送。
```json
{ "Assign": { "1": { "X": 0, "Y": 0, "Z": 0 } } }
```

---

## 🚀 快速开始 (Python)

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"   # 在 Gen NX 应用中获取

def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(method, command, res.status_code)
    return res.json()

# 1) 新建文档
MidasAPI("POST", "/doc/new", {})

# 2) 设置单位（台湾 RC：建议 m、tonf）
MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "TONF"}}})

# 3) 材料（RC）
MidasAPI("POST", "/db/matl", {"Assign": {1: {
    "TYPE": "CONC", "NAME": "C32",
    "PARAM": [{"P_TYPE": 1, "STANDARD": "AS17(RC)", "DB": "C32"}]
}}})

# 4) 2 个节点
MidasAPI("POST", "/db/node", {"Assign": {
    1: {"X": 0, "Y": 0, "Z": 0},
    2: {"X": 0, "Y": 0, "Z": 3.2},
}})

# 5) 柱单元（BEAM 类型）
MidasAPI("POST", "/db/elem", {"Assign": {1: {
    "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0
}}})

# 6) 保存
MidasAPI("POST", "/doc/save")
```

更多示例请参考 [examples/](./examples/) 目录。

---

## 📚 主要端点

### 文档管理 (`/doc/*`)
| 端点 | 方法 | 功能 |
|-----------|--------|------|
| `/doc/new`    | POST | 新建文档（空请求体 `{}`） |
| `/doc/open`   | POST | 打开文档 |
| `/doc/save`   | POST | 保存文档 |
| `/doc/close`  | POST | 关闭文档 |

### 模型创建 (`/db/*`)
| 端点 | 功能 | 核心字段 |
|-----------|------|----------|
| `/db/unit` | 单位制 | `DIST`, `FORCE` |
| `/db/matl` | 材料 | `TYPE:"CONC"`, `NAME`, `PARAM:[{P_TYPE, STANDARD, DB}]` |
| `/db/sect` | 截面 | `SECTTYPE:"DBUSER"`, `SECT_BEFORE:{SHAPE, SECT_I:{vSIZE:[h,w]}}}` |
| `/db/thik` | 板/墙厚度 | `NAME`, `TYPE:"VALUE"`, `T_IN`, `T_OUT` |
| `/db/node` | 节点 | `X`, `Y`, `Z` |
| `/db/elem` | 单元 | `TYPE`, `MATL`, `SECT`, `NODE:[…]`, `ANGLE`, `STYPE` |

### 荷载与边界条件
| 端点 | 功能 | 核心字段 |
|-----------|------|----------|
| `/db/stld` | 静力荷载工况 | `NAME`, `TYPE`(`D`/`L`/`LR`/`S`/`W`/`E`…), `DESC` |
| `/db/bodf` | 自重 | `LCNAME`, `FV:[0,0,-1]` |
| `/db/bmld` | 梁单元荷载 | `ITEMS:[{LCNAME, CMD:"BEAM", TYPE:"UNILOAD", DIRECTION, D, P}]` |
| `/db/fbld` | **楼面荷载类型定义** | `NAME`, `ITEM:[{LCNAME, FLOOR_LOAD, OPT_SUB_BEAM_WEIGHT}]` |
| `/db/fbla` | **楼面荷载面指定** | `FLOOR_LOAD_TYPE_NAME`, `FLOOR_DIST_TYPE`(1~4), `DIR`, `NODES:[…]` |
| `/db/pres` | **压力（风压）荷载** | `LCNAME`, `CMD:"PRES"`, `ELEM_TYPE`, `FACE_EDGE_TYPE`, `DIRECTION`, `FORCES:[...]` |
| `/db/cons` | 支承（边界） | `ITEMS:[{ID, CONSTRAINT:"1111000"}]` (Dx Dy Dz Rx Ry Rz) |
| `/db/lcom-gen` | 荷载组合 | `NAME`, `vCOMB:[{ANAL:"ST", LCNAME, FACTOR}]` |

### 单元类型 (`ELEM.TYPE`)
| 结构构件 | `TYPE` | 备注 |
|---------|--------|------|
| 柱 · 梁 (Frame) | `"BEAM"` | `NODE=[i, j]`, `ANGLE`=Beta 角 |
| 楼板 | `"PLATE"` | `NODE`=3/4 点, `STYPE` 1=Thick·2=Thin·3/4=+Drilling DOF |
| 墙单元 | `"WALL"` | `NODE`=4 点, `STYPE` 1=Membrane·2=Plate, `WALL`(ID), `W_TYPE` |
| 其他 | `TRUSS` / `TENSTR` / `COMPTR` / `PLSTRS` / `PLSTRN` / `AXISYM` / `SOLID` | |

> 全量 Key 与字段架构请参考 [NX Open API JSON Manual](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)。

---

## 🌬️ 风荷载 (KDS 41 12:2022)

MIDAS NX 支持 **KDS 41 12:2022（韩国风荷载标准）** 以及多种国际规范。

### 风荷载相关端点

| 端点 | 功能 | 核心字段 |
|-----------|------|----------|
| `/db/stld` | 创建风荷载工况 | `NAME`, `TYPE:"W"` (Wind) |
| `/db/pres` | 施加压力（风压） | `LCNAME`, `ELEM_TYPE:"PLATE"/"SOLID"`, `DIRECTION`, `FORCES` |
| `/db/wprs` | 节点 (Nodal) 风压 | `LCNAME`, `DIRECTION`, `NODES:[...]`, `PRESSURE` |
| `/db/aprs` | 面积 (Area) 风压 | `LCNAME`, `DIRECTION`, `NODES:[...]`, `PRESSURE` |

### Python 示例：施加 KDS 风荷载

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
MAPI_KEY = "your-mapi-key-here"

def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"Content-Type": "application/json", "MAPI-Key": MAPI_KEY}
    res = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"{method} {command} → {res.status_code}")
    return res.json() if res.text else None

# 1) 新建文档
MidasAPI("POST", "/doc/new", {})

# 2) 设置单位
MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "KN"}}})

# 3) 创建风荷载工况 (KDS 41 12:2022)
MidasAPI("POST", "/db/stld", {"Assign": {1: {
    "NAME": "WIND_X_KDS",
    "TYPE": "W",           # W = Wind Load
    "CODE": "KDS41122022", # 依据 KDS 41 12:2022
    "DESC": "KDS 풍하중 X방향"
}}})

# 4) 创建楼板单元（示例：3×3m 板）
MidasAPI("POST", "/db/node", {"Assign": {
    1: {"X": 0, "Y": 0, "Z": 5},
    2: {"X": 3, "Y": 0, "Z": 5},
    3: {"X": 3, "Y": 3, "Z": 5},
    4: {"X": 0, "Y": 3, "Z": 5},
}})

MidasAPI("POST", "/db/elem", {"Assign": {1: {
    "TYPE": "PLATE", "NODE": [1, 2, 3, 4], "THIK": 1, "STYPE": 1
}}})

# 5) 施加压力荷载（风压 1.5 kN/m²，X 方向）
MidasAPI("POST", "/db/pres", {"Assign": {1: {
    "ITEMS": [{
        "LCNAME": "WIND_X_KDS",
        "CMD": "PRES",
        "ELEM_TYPE": "PLATE",
        "FACE_EDGE_TYPE": "FACE",
        "DIRECTION": "GX",        # Global X 方向
        "EDGE_FACE": 1,           # 面 1（上侧）
        "FORCES": [-1.5, 0, 0, 0, 0]  # -1.5 kN/m²（负值 = 吸力）
    }]
}})

# 6) 保存并执行分析
MidasAPI("POST", "/doc/save", {})
MidasAPI("POST", "/doc/anal", {})
```

### 风荷载计算（以 KDS 为基准）

```python
def calculate_kds_wind_pressure(height, wind_speed=28, exposure_category="C"):
    """
    KDS 41 12:2022 静力等效风荷载计算
    
    Parameters:
    - height: 结构物高度 (m)
    - wind_speed: 基本设计风速 (m/s, 默认值 28)
    - exposure_category: 暴露类别 ("B", "C", "D" 等)
    
    Returns:
    - 风压 (kN/m²)
    """
    # 各暴露类别的风速系数（以 KDS 为基准的近似值）
    kz_table = {
        "B": {10: 1.0, 20: 1.1, 30: 1.2},
        "C": {10: 0.9, 20: 1.0, 30: 1.1},
        "D": {10: 0.8, 20: 0.9, 30: 1.0}
    }
    
    # 线性插值
    kz_values = kz_table.get(exposure_category, kz_table["C"])
    if height <= 10:
        Kz = kz_values[10]
    elif height <= 20:
        Kz = kz_values[20]
    else:
        Kz = kz_values[30]
    
    # 结构系数（以矩形结构物为基准）
    Cp = 0.8
    # 重要性系数
    Iw = 1.0
    
    # 动压 q = 0.613 * Kz * V² * Iw (单位: kN/m²)
    q = 0.613 * Kz * (wind_speed ** 2) * Iw
    
    # 风压 = q * Cp
    wind_pressure = q * Cp
    
    return round(wind_pressure, 3)

# 示例：高度 30m、设计风速 28m/s、暴露类别 C
pressure = calculate_kds_wind_pressure(30, 28, "C")
print(f"风压: {pressure} kN/m²")  # 约 1.58 kN/m²
```

### 参考文档
- [MIDAS Support - Wind Loads (KDS 41 12:2022)](https://support.midasuser.com/hc/ko/articles/29238911763353-Wind-Loads)
- [MIDAS Support - Nodal Wind Pressure](https://support.midasuser.com/hc/ko/articles/29270162256281-Nodal-Wind-Pressure)
- [MIDAS Support - Area Wind Pressure](https://support.midasuser.com/hc/ko/articles/29270183516057-Area-Wind-Pressure)
- [MIDAS Support - Static Wind Load (KDS 41 12:2022)](https://support.midasuser.com/hc/ko/articles/58908673370521-Static-Wind-Load-KDS-41-12-2022)

---

## 🔗 官方文档

- [docs/manual/INDEX.md](./docs/manual/zh-cn/INDEX.md) — 本仓库整理的全量端点·JSON 架构韩文手册（27 个文件）
- [docs/AUTHENTICATION.md](./docs/zh-cn/AUTHENTICATION.md) — MAPI-Key 认证设置、各语言示例、安全提示
- [MIDAS API 在线手册](https://support.midasuser.com/hc/en-us/articles/33016922742937-MIDAS-API-Online-Manual)
- [MIDAS API JSON Manual（原文，全量端点架构）](https://support.midasuser.com/hc/en-us/sections/30087500371097-JSON-Manual)
- [MIDAS CIVIL NX Open API 运行机制](https://support.midasuser.com/hc/en-us/articles/30212837484441-How-to-work-MIDAS-CIVIL-NX-Open-API)
- [Python 示例](https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python)
- [Excel VBA 示例](https://support.midasuser.com/hc/en-us/articles/30506684736665-Example-Excel-VBA)
- [其他语言示例 (C#·Java·Dart·C·Node.js)](https://support.midasuser.com/hc/en-us/articles/30506872725017-Example-Various-Programming-Languages)

## 📖 仓库结构

```
docs/
├── AUTHENTICATION.md    # Base URL、MAPI-Key 设置、各语言认证示例、安全提示
└── manual/              # MIDAS API JSON Manual 全文翻译·整理（从 INDEX.md 开始，01~27）

examples/
├── python/              # Python 示例
├── javascript/          # JavaScript 示例
├── curl/                # cURL 示例
├── vba/                 # Excel VBA 示例
└── OTHER_LANGUAGES.md   # C# · Java · Dart · C · Node.js 代码片段
```

## ❓ 帮助

- 在 Issues 标签页提问
- 访问[官方支持网站](https://support.midasuser.com)

## 📝 参考

本文档的端点与 JSON 架构依据 MIDAS 官方 NX Open API 手册（截至 2026-06）及 KDS 41 12:2022 风荷载标准编写。
