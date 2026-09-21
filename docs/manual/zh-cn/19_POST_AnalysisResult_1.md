# 19. POST – Analysis Result Tables (Part 1)

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头部：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../19_POST_AnalysisResult_1.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分涉及分析结果表格中的**反力·位移·桁架·拉索·梁·同时节点力（Concurrent Joint Force）**结果。所有端点均使用**通用 URI `{base url}/post/TABLE`**，且仅支持 `POST` 方法。请求体的 `"Argument"` 对象中以 `TABLE_TYPE` 值决定表格种类。

---

## 通用事项

### Input URI（分析结果表格通用）

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 通用 Request 结构与参数

相比前处理表格（第18章）为扩展结构，支持 `UNIT`·`STYLES`·`COMPONENTS`·`NODE_ELEMS`·`LOAD_CASE_NAMES`·`OPT_CS`·`STAGE_STEP`。**下方参数表对13个表格全部通用适用**，各节仅另行记述 `TABLE_TYPE` enum、响应 `HEAD` 列与代表性示例。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 响应表格标题 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表格类型（按表格区分的 enum，参见各节） | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 结果表格保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 4-1 | └ 力（Force） | `UNIT.FORCE` | String | — | Optional |
| 4-2 | └ 长度（Length） | `UNIT.DIST` | String | — | Optional |
| 4-3 | └ 热（Heat） | `UNIT.HEAT` | String | — | Optional |
| 4-4 | └ 温度（Temperature） | `UNIT.TEMP` | String | — | Optional |
| 5 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 5-1 | └ 数字格式 · `"Default"` / `"Fixed"` / `"Scientific"` / `"General"` | `STYLES.FORMAT` | String | — | Optional |
| 5-2 | └ 小数位数（0~15） | `STYLES.PLACE` | Integer | — | Optional |
| 6 | 结果表格显示列 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 节点/单元指定（下列3种方式之一） | `"NODE_ELEMS"` | Object | All | Optional |
| 7-1 | 方式1：分别指定 ID（例：`[101, 102, 103]`） | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 7-2 | 方式2：指定 ID 范围（例：`"101 to 105"`） | `NODE_ELEMS.TO` | String | — | Optional |
| 7-3 | 方式3：指定结构组名（例：`"SG1"`） | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |
| 8 | 荷载名称与类型（下列后缀规则） | `"LOAD_CASE_NAMES"` | Array [String] | All | Optional |
| 9 | 激活施工阶段步骤（下列 ⚠️ — 取值不同行为不同） | `"OPT_CS"` | Boolean | `false`（标注写法上） | Optional |
| 10 | 施工阶段步骤名称 | `"STAGE_STEP"` | Array [String] | All | Optional |

**`LOAD_CASE_NAMES` 后缀规则**

| 荷载类型 | 表示 |
|-----------|------|
| 静力荷载工况 | `NAME(ST)` |
| 一般组合 | `NAME(CB)` / `NAME(CB:all)` / `NAME(CB:max)` / `NAME(CB:min)` |
| 施工阶段 | `NAME(CS)` |
| 反应谱 | `NAME(RS)` |
| 移动荷载 | `NAME(MV:all)` / `NAME(MV:max)` / `NAME(MV:min)` |
| 沉降荷载 | `NAME(SM:all)` / `NAME(SM:max)` / `NAME(SM:min)` |

> **参考：** `OPT_CS`·`STAGE_STEP` 用于查询施工阶段结果（Reaction 的 Local–Surface Spring
> 变体、Beam Force (Static Prestress)、Concurrent Joint Force 不支持这两个字段
> — 参见各节）。`STAGE_STEP` 项为 `"CS1:001(first)"`、`"CS1:002(last)"` 格式。

> ⚠️ **`OPT_CS` 为3状态 —— 省略与 `false` 的行为彼此不同（2026-09-15 确认）。**
> 由于 2026-09-11 原文更新，Reaction 文章（`36009349748249`）的 Specifications 表中
> 补充了按取值区分的行为说明。
>
> | 发送值 | 行为 |
> | --- | --- |
> | `true` | 切换到 Construction Stage（**第一个阶段**）返回 CS 结果 |
> | `false` | 切换到 PostCS（**最终阶段**）返回 Post 结果 |
> | **省略字段** | **保持当前视图模式**，并返回与之对应的 Post/CS 结果 |
>
> 即显式发送 `"OPT_CS": false` 并非「不使用施工阶段」，而是**切换到最终阶段
> 视图**的指令，与完全不发送时的结果可能不同。
>
> 但同一张表的 Default 列仍写为 `false`，与该说明不一致。既然已单独
> 记述了省略时的行为，就不宜把 Default 视为 `false`，因此在上表默认值一格中加注了
> 「（标注写法上）」。**实际 API 行为未经验证** — 待报错项。
>
> 该说明截至 2026-09-15 **仅见于 Reaction 文章**。同一 `post/TABLE` 端点的兄弟
> 文章（Displacements `36009638400281`、Beam Stress `36011455813273` 等）目前仍
> 只有一行 "Activation - Construction Stage Step"。由于是同一字段，行为应当相同是自然的
> 推断，但需说明原文依据仅 Reaction 一处。

### 通用 Response 结构

```json
{
  "<TABLE_NAME>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

## 表格列表

| No. | 表格 | `TABLE_TYPE` |
|-----|--------|--------------|
| 1 | [Reaction](#1-reaction) | `REACTIONG` / `REACTIONL` / `REACTIONSURFACESPRING` |
| 2 | [Displacements](#2-displacements) | `DISPLACEMENTG` / `DISPLACEMENTL` |
| 3 | [Truss Force](#3-truss-force) | `TRUSSFORCE` |
| 4 | [Truss Stress](#4-truss-stress) | `TRUSSSTRESS` |
| 5 | [Cable Force](#5-cable-force) | `CABLEFORCE` |
| 6 | [Cable Configuration](#6-cable-configuration) | `CABLECONFIG` |
| 7 | [Cable Efficiency](#7-cable-efficiency) | `CABLEEFFIENCY` |
| 8 | [Beam Force](#8-beam-force) | `BEAMFORCE` / `BEAMFORCEVBM` |
| 9 | [Beam Force (Static Prestress)](#9-beam-force-static-prestress) | `BEAMFORCESTP` |
| 10 | [Beam Stress](#10-beam-stress) | `BEAMSTRESS` / `BEAMSTRESS7DOF` / `BEAMSTRESSVBM` |
| 11 | [Beam Stress (Equivalent)](#11-beam-stress-equivalent) | `BEAMSTRESSDETAIL` |
| 12 | [Beam Stress (PSC)](#12-beam-stress-psc) | `BEAMSTRESSPSC` / `BEAMSTRESS7DOFPSC` |
| 13 | [Concurrent Joint Force](#13-concurrent-joint-force) | `CONCURRENT_JOINT_FORCE` |

---

## 1. Reaction

> **功能：** 提取支座反力（全局/局部/面弹簧局部）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"REACTIONG"` | Global（全局坐标系） |
| `"REACTIONL"` | Local（局部坐标系） |
| `"REACTIONSURFACESPRING"` | Local – Surface Spring（面弹簧局部） |

> ⚠️ 2026-08-26 确认（article id `36009349748249`）：官方 Specifications 表与 JSON Schema enum
> 均一致写作 `"REACTIONSURFACESPRING"`，仅 "Reaction(Local-Surface Spring)" 的 Request Example
> 一处使用了 `"REACTIONLSURFACESPRING"`（多出 L）。采纳了表与 schema 这2处一致的一方，并判断为示例
> 一侧的一次性笔误，但实际 API 行为未经验证，故保留为报错对象。

### Response HEAD

响应列构成随 `TABLE_TYPE` 取值而不同。

- `REACTIONG`(Global)：`["Index", "Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"]`（查询施工阶段时在 `Load` 之后追加 `Stage`/`Step`）
- `REACTIONL`(Local)：`["Index", "Node", "Load", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "Mb"]`（与 Global 结构相同，但字段名为小写）
- `REACTIONSURFACESPRING`(Local-Surface Spring)：`["Index", "ElementType", "SurfaceSpringType", "Element", "Load", "Node&Part", "Reaction/Area", "Reaction/Length", "Displacement"]`（完全不同的结构）

> ⚠️ 2026-08-26 确认：`REACTIONG` 响应除 `DATA` 数组外还在最外层新增 `SUB_TABLES` 数组，
> 其内包含 `SUMMATIONOFREACTIONFORCESPRINTOUT` 子表格（`HEAD`：`["Load", "FX(kN)",
> "FY(kN)", "FZ(kN)"]`，查询施工阶段时追加 `Stage`/`Step`）。此前版本文档未反映该内容，故已补入
> 下方示例。`REACTIONL`/`REACTIONSURFACESPRING` 没有 `SUB_TABLES`。

### Request / Response JSON

**POST Request Body — 全局反力（一般/Post CS）**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Global)",
    "TABLE_TYPE": "REACTIONG",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Request Body — 全局反力（施工阶段）**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Global)",
    "TABLE_TYPE": "REACTIONG",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Node", "Load", "Stage", "Step", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS1:001(first)", "CS1:002(last)"]
  }
}
```

**POST Response Body — 全局反力（General/Post CS）**

```json
{
  "Reaction(Global)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "FX", "FY", "FZ", "MX", "MY", "MZ", "Mb"],
    "DATA": [
      ["1", "1", "DL", "3.082169679668", "0.536339553582", "160.905188552207", "-0.531870057302", "3.112177384191", "0.000000000000", "0.000000000000"]
    ],
    "SUB_TABLES": [
      {
        "SUMMATIONOFREACTIONFORCESPRINTOUT": {
          "HEAD": ["Load", "FX(kN)", "FY(kN)", "FZ(kN)"],
          "DATA": [
            ["DL", "0.000000000000", "0.000000000000", "686.683352297500"]
          ]
        }
      }
    ]
  }
}
```

**POST Request Body — 局部反力（Local）**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Local)",
    "TABLE_TYPE": "REACTIONL",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Node", "Load", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "Mb"],
    "NODE_ELEMS": { "KEYS": [9] },
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body — 局部反力（Local）**

```json
{
  "Reaction(Local)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "Fx", "Fy", "Fz", "Mx", "My", "Mz", "Mb"],
    "DATA": [
      ["1", "9", "DL", "-9.528467668945", "108.534577627514", "105.577135693819", "-2.014716071930", "-6.655711206332", "6.655708849960", "0.000000000000"]
    ]
  }
}
```

**POST Request Body — 面弹簧局部反力（Local-Surface Spring）**

```json
{
  "Argument": {
    "TABLE_NAME": "Reaction(Local-SurfaceSpring)",
    "TABLE_TYPE": "REACTIONSURFACESPRING",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 }
  }
}
```

**POST Response Body — 面弹簧局部反力（Local-Surface Spring）**

```json
{
  "Reaction(Local-SurfaceSpring)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "ElementType", "SurfaceSpringType", "Element", "Load", "Node&Part", "Reaction/Area", "Reaction/Length", "Displacement"],
    "DATA": [
      ["1", "PLATE", "Planar(Face)", "9", "UL", "5", "1.768850000000", "-", "-0.000901864"]
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

# ── POST: 提取1号节点的 DL 荷载工况全局反力 ──────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Reaction",
        "TABLE_TYPE": "REACTIONG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Reaction", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Node {d['Node']} ({d['Load']}): FZ={d['FZ']}")
```

---

## 2. Displacements

> **功能：** 提取节点位移（全局/局部）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"DISPLACEMENTG"` | Global（全局坐标系） |
| `"DISPLACEMENTL"` | Local（局部坐标系） |

### Response HEAD

`["Index", "Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"]`（查询施工阶段时在 `Load` 之后追加 `Stage`/`Step`）

### 施工阶段（Construction Stage）专用参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 激活施工阶段步骤（按取值区分的行为见[通用参数表](#通用-request-结构与参数) ⚠️ 注释） | `"OPT_CS"` | Boolean | `false`（标注写法上） | Optional |
| 2 | 施工阶段步骤名称列表 | `"STAGE_STEP"` | Array [String] | All | Optional |
| 3 | 位移显示方式 · 累计：`"Accumulative"` / 当前：`"Current"` / 实际：`"Real"` | `"DISP_OPT"` | String | `"Accumulative"` | Optional |

> ⚠️ 2026-08-26 确认（article id `36009638400281`）：`DISP_OPT` 在此前版本文档中有遗漏
> — 该字段仅在 `OPT_CS=true`（查询施工阶段）时有意义，官方 Specifications 表与 JSON Schema
> 两侧均存在。

### Request / Response JSON

**POST Request Body — 全局位移（General/Post CS）**

```json
{
  "Argument": {
    "TABLE_NAME": "Displacement",
    "TABLE_TYPE": "DISPLACEMENTG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 3 },
    "COMPONENTS": ["Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "LOAD_CASE_NAMES": ["Self(ST)"]
  }
}
```

**POST Response Body — 全局位移（General/Post CS）**

```json
{
  "Displacement": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Node", "Load", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "43", "Self", "5.047e+00", "5.234e-10", "-6.718e-07", "0.000e+00", "-5.108e-03", "1.903e-07"]
    ]
  }
}
```

**POST Request Body — 全局位移（施工阶段）**

```json
{
  "Argument": {
    "TABLE_NAME": "Displacement",
    "TABLE_TYPE": "DISPLACEMENTG",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 6 },
    "COMPONENTS": ["Node", "Load", "Stage", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [43] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS16:001(first)", "CS16:002(last)"],
    "DISP_OPT": "Accumulative"
  }
}
```

**POST Response Body — 全局位移（施工阶段）**

```json
{
  "Displacement": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Node", "Load", "Stage", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "43", "Summation", "CS16", "001(first)", "-1.950282e+01", "-5.770649e-09", "-5.955365e-07", "0.000000e+00", "1.629373e-03", "2.975638e-06"],
      ["2", "43", "Summation", "CS16", "002(last)", "-7.132734e+01", "2.112468e-08", "-6.235268e-07", "0.000000e+00", "1.215839e-03", "8.756069e-06"]
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

# ── POST: 提取全局位移表格 ────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Displacement",
        "TABLE_TYPE": "DISPLACEMENTG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 3},
        "LOAD_CASE_NAMES": ["Self(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Displacement", {})
print(f"位移结果 {len(table.get('DATA', []))}行")
```

---

## 3. Truss Force

> **功能：** 提取桁架单元的构件内力（I端·J端轴力）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TRUSSFORCE"` | 桁架构件内力 |

### Response HEAD

`["Index", "Elem", "Load", "Force-I", "Force-J"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TrussForce",
    "TABLE_TYPE": "TRUSSFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Force-I", "Force-J"],
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "TrussForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Force-I", "Force-J"],
    "DATA": [
      ["1", "33", "DL", "788.459634387094", "772.759634387094"]
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

# ── POST: 提取桁架构件内力 ───────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TrussForce",
        "TABLE_TYPE": "TRUSSFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TrussForce", {})
for row in table.get("DATA", []):
    print(f"  Elem {row[1]}: Force-I={row[3]}, Force-J={row[4]}")
```

---

## 4. Truss Stress

> **功能：** 提取桁架单元的应力（I端·J端）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"TRUSSSTRESS"` | 桁架应力 |

### Response HEAD

`["Index", "Elem", "Load", "Stress-I", "Stress-J"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "TrussStress",
    "TABLE_TYPE": "TRUSSSTRESS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Stress-I", "Stress-J"],
    "LOAD_CASE_NAMES": ["DL(ST)"]
  }
}
```

**POST Response Body**

```json
{
  "TrussStress": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Stress-I", "Stress-J"],
    "DATA": [
      ["1", "33", "DL", "157691.926877418999", "154551.926877418999"]
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

# ── POST: 提取桁架应力 ─────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "TrussStress",
        "TABLE_TYPE": "TRUSSSTRESS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["DL(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("TrussStress", {})
print(f"桁架应力 {len(table.get('DATA', []))}行")
```

---

## 5. Cable Force

> **功能：** 提取拉索单元的张力（Tension）与分力（FX/FY/FZ），按 I端·J端分别给出。按施工阶段步骤（`Step`）查询。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"CABLEFORCE"` | 拉索构件内力 |

### Response HEAD

- General/Post CS：`["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"]`（后4个 `Tension`·`FX`·`FY`·`FZ` 为 J端分量）
- 施工阶段（Construction Stage）：在 `Step` 之前追加 `Stage` 的 `["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"]`

> ⚠️ 2026-08-26 确认（article id `36010315199001`）：此前版本文档在 General/Post CS 响应示例上
> 错误地拼接了 `OPT_CS: true`·`STAGE_STEP: ["nl_001"]`·`LOAD_CASE_NAMES: ["SelfWeight(CS)"]` 请求，
> 实际上是不匹配的请求/响应组合（`nl_001` 并非施工阶段步骤，而是 Post-CS
> 非线性步骤的自动标签）。下方已按两个场景（General/Post CS、施工阶段）拆分为正确的请求/响应
> 对予以更正。

### Request / Response JSON

**POST Request Body — General/Post CS**

```json
{
  "Argument": {
    "TABLE_NAME": "CableForce",
    "TABLE_TYPE": "CABLEFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
  }
}
```

**POST Response Body — General/Post CS**

```json
{
  "CableForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "1", "2", "SelfWeight", "nl_001", "27419.266299103001", "-26808.034545985502", "-0.002024057832", "-5757.208365377180", "27431.024313956001", "26808.034545985502", "0.002024057832", "5812.949225142650"]
    ]
  }
}
```

**POST Request Body — 施工阶段（Construction Stage）**

```json
{
  "Argument": {
    "TABLE_NAME": "CableForce",
    "TABLE_TYPE": "CABLEFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS2:001(last)"]
  }
}
```

**POST Response Body — 施工阶段（Construction Stage）**

```json
{
  "CableForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "Tension", "FX", "FY", "FZ", "Tension", "FX", "FY", "FZ"],
    "DATA": [
      ["1", "1", "1", "2", "Summation", "CS2", "001(last)", "15538.648867201100", "-15187.887452924801", "-0.000971965905", "-3282.938216819810", "15550.520996389199", "15187.887452924801", "0.000971965905", "3338.679076585290"]
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

# ── POST: 提取拉索张力（一般/Post CS） ──────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableForce",
        "TABLE_TYPE": "CABLEFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CableForce", {})
for row in table.get("DATA", []):
    print(f"  Cable {row[1]}: Tension(I)={row[6]}")
```

---

## 6. Cable Configuration

> **功能：** 提取拉索单元的形状信息（总长度·伸长量·无应变长度·垂度·水平/垂直距离·坡度·Skew角等）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"CABLECONFIG"` | 拉索形状 |

### Response HEAD

- General/Post CS：`["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient", "SkewAngle/IEnd", "SkewAngle/JEnd"]`
- 施工阶段（Construction Stage）：在 `Step` 之前追加 `Stage`，同时后方的 `SkewAngle/IEnd`·`SkewAngle/JEnd` 2列不在响应中出现 — `["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient"]`（14列）

> ⚠️ 2026-08-26 确认（article id `36011013418905`）：此前版本文档在 General/Post CS 响应示例上
> 错误地拼接了 `OPT_CS: true`·`STAGE_STEP: ["nl_001"]`·`LOAD_CASE_NAMES: ["SelfWeight(CS)"]` 请求，
> 实际上是不匹配的请求/响应组合（与第5节 Cable Force 同样的问题）。下方已按两个
> 场景拆分为正确的请求/响应对予以更正。施工阶段响应完全省略 `SkewAngle` 2列，
> 是原文自身的特异之处 — 原文的施工阶段 Request Example 在 `COMPONENTS` 中明确请求了
> `"IEnd"`/`"JEnd"`，实际响应却不反映，属自相矛盾 — 待报错项。

### Request / Response JSON

**POST Request Body — General/Post CS**

```json
{
  "Argument": {
    "TABLE_NAME": "CableConfig",
    "TABLE_TYPE": "CABLECONFIG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
  }
}
```

**POST Response Body — General/Post CS**

```json
{
  "CableConfig": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient", "SkewAngle/IEnd", "SkewAngle/JEnd"],
    "DATA": [
      ["1", "1", "1", "2", "SelfWeight", "nl_001", "16.511543914801", "0.055076495942", "16.456467418860", "0.004194907068", "16.140012646203", "3.482956316281", "0.215796380872", "12.121120396140", "12.233836223754"]
    ]
  }
}
```

**POST Request Body — 施工阶段（Construction Stage）**

```json
{
  "Argument": {
    "TABLE_NAME": "CableConfiguration",
    "TABLE_TYPE": "CABLECONFIG",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS2:001(last)"]
  }
}
```

**POST Response Body — 施工阶段（Construction Stage）**

```json
{
  "CableConfiguration": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Stage", "Step", "TotalLength", "Elongation", "UnstrainedLength", "Sag", "HorizontalDistance", "VerticalDistance", "Gradient"],
    "DATA": [
      ["1", "1", "1", "2", "Summation", "CS2", "001(last)", "16.487684968322", "0.031217549462", "16.456467418860", "0.007390270826", "16.109363292361", "3.511679349731", "0.217989953172"]
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

# ── POST: 提取拉索形状信息（一般/Post CS） ─────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableConfig",
        "TABLE_TYPE": "CABLECONFIG",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CableConfig", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Cable {d['Elem']}: 总长度={d['TotalLength']}, 无应变长度={d['UnstrainedLength']}")
```

---

## 7. Cable Efficiency

> **功能：** 提取拉索单元的效率（Efficiency，等效刚度折减指标）相关值（弦长·ExA·重量·张力·修正 ExA·效率）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"CABLEEFFIENCY"` | 拉索效率（照原文拼写） |

> **注意：** `TABLE_TYPE` 取值按原文 API 为 `"CABLEEFFIENCY"`，不是 `EFFICIENCY` 而是 `EFFIENCY`（拼写错误已原样反映在 API 规格中）。

### Response HEAD

`["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "ChordLength", "ExA", "Weight", "Tension", "ExA(mod)", "Efficiency"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "CableEfficiency",
    "TABLE_TYPE": "CABLEEFFIENCY",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "LOAD_CASE_NAMES": ["SelfWeight(CS)"],
    "OPT_CS": true,
    "STAGE_STEP": ["nl_001"]
  }
}
```

**POST Response Body**

```json
{
  "CableEfficiency": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "NodeI", "NodeJ", "Load", "Step", "ChordLength", "ExA", "Weight", "Tension", "ExA(mod)", "Efficiency"],
    "DATA": [
      ["1", "1", "1", "2", "SelfWeight", "nl_001", "16.511541203676", "8194436.740000000224", "55.740859765477", "27425.145306529499", "8193631.458022129722", "0.999901728209"]
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

# ── POST: 提取拉索效率 ─────────────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "CableEfficiency",
        "TABLE_TYPE": "CABLEEFFIENCY",   # 照原文拼写（EFFIENCY）
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["SelfWeight(CS)"],
        "OPT_CS": True,
        "STAGE_STEP": ["nl_001"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("CableEfficiency", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Cable {d['Elem']}: 效率={d['Efficiency']}")
```

---

## 8. Beam Force

> **功能：** 提取梁单元的构件内力/力矩（轴力·剪力·扭转·弯矩·双力矩等），按构件位置（Part）分别给出。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BEAMFORCE"` | 梁构件内力（按构件位置） |
| `"BEAMFORCEVBM"` | 梁构件内力（按最大值，View by Max Value） |

> ✅ **2026-09-06 解决确认**（article id `36011262919705`）：仅官方 JSON Schema 的 enum
> 误写为 `"BEAMFORCEBYMAX"`（Request Example 与 Specifications 表原本就是 `"BEAMFORCEVBM"`），
> 已由 2026-09-01 原文更新更正 — 复确认时原文中 `BEAMFORCEBYMAX`
> 出现0次，enum 为 `["BEAMFORCE", "BEAMFORCEVBM"]`。上表从一开始就以示例·表为准，故无
> 需修改。应为 2026-08-27 报错（Jira `MAPI-2484`）的反映结果。

### 构件位置（Parts）指定 — 第8~12节通用

`Beam Force`/`Beam Force (Static Prestress)`/`Beam Stress`/`Beam Stress (Equivalent)`/
`Beam Stress (PSC)` 这5个表格可用下方 `PARTS` 参数指定要查询的构件位置
（省略时为全部位置）。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 11 | 构件位置 · I端：`"PartI"` / 1/4点：`"Part1/4"` / 2/4点：`"Part2/4"` / 3/4点：`"Part3/4"` / J端：`"PartJ"` | `"PARTS"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 确认：官方 Specifications 表的取值写法为含空格的 `"Part I"`/`"Part J"`，
> JSON Schema 的 `enum` 却写作 `"Part1"`（数字1，而非 I），而实际 Request
> Example 使用的是与两者都不同的、无空格的 `"PartI"`/`"PartJ"`。以示例为准采纳。

### Response HEAD

- `BEAMFORCE`：`["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Bi-Moment", "T-Moment", "W-Moment"]`
- `BEAMFORCEVBM`：在 `Part` 之后新增用于表示哪个分量产生最大值的 `Component` 列，且没有 Bi/T/W-Moment — `["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

### Request / Response JSON

**POST Request Body — BEAMFORCE**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForce",
    "TABLE_TYPE": "BEAMFORCE",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "TO": "1 to 10" },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
  }
}
```

**POST Response Body — BEAMFORCE**

```json
{
  "BeamForce": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z", "Bi-Moment", "T-Moment", "W-Moment"],
    "DATA": [
      ["1", "1", "Selfweight", "I", "0.0000", "0.0000", "12.5000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000"],
      ["2", "1", "Selfweight", "J", "0.0000", "0.0000", "-12.5000", "0.0000", "25.0000", "0.0000", "0.0000", "0.0000", "0.0000"]
    ]
  }
}
```

**POST Request Body — BEAMFORCEVBM（View by Max Value）**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForceViewByMaxValue",
    "TABLE_TYPE": "BEAMFORCEVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [2833] },
    "LOAD_CASE_NAMES": ["STLENV_STR(CB:max)", "STLENV_STR(CB:min)"],
    "PARTS": ["PartI", "PartJ"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]
  }
}
```

**POST Response Body — BEAMFORCEVBM（View by Max Value）**

```json
{
  "BeamForceViewByMaxValue": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "2833", "STLENV_STR(max)", "I[781]", "Axial", "182.614058593750", "0.041735554695", "6.277819091797", "0.006796598315", "21.295148437500", "0.051163814545"],
      ["2", "2833", "STLENV_STR(max)", "I[781]", "Shear-y", "180.999328125000", "0.041774380684", "6.222307861328", "0.006750476599", "21.106847412109", "0.051366916656"]
    ]
  }
}
```

> ⚠️ 2026-08-26 确认：`ITEM_TO_DISPLAY`（`BEAMFORCEVBM` 专用，enum：`Axial`/`Shear-y`/`Shear-z`/
> `Torsion`/`Moment-y`/`Moment-z`）在此前版本文档中有遗漏 — 该字段用于指定计算最大值的对象
> 分量，与显示的 `Component` 值相对应。

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 提取1~10号梁单元的构件内力 ─────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamForce",
        "TABLE_TYPE": "BEAMFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "NODE_ELEMS": {"TO": "1 to 10"},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamForce", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} ({d['Part']}): Moment-y={d['Moment-y']}")
```

---

## 9. Beam Force (Static Prestress)

> **功能：** 提取静力预应力（Static Prestress）荷载的梁构件内力。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BEAMFORCESTP"` | 梁构件内力（静力预应力） |

> ✅ **2026-09-06 解决确认**（article id `36011373070745`）：仅官方 JSON Schema enum
> 误写为 `"BEAMFORCESIP"`（Request Example 与 Specifications 表原本就是
> `"BEAMFORCESTP"`），已由 2026-09-01 原文更新更正 — 复确认时原文中 `BEAMFORCESIP` 出现0次，
> `BEAMFORCESTP` 出现3次。上表无需修改。应为 2026-08-27 报错（Jira `MAPI-2484`）的反映结果。
> `PARTS`（参见第8节通用参数，值例：`"PartI"`/`"PartJ"`）也适用于本表格，但此前
> 版本中有遗漏。

### Response HEAD

`["Index", "Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamForcePS",
    "TABLE_TYPE": "BEAMFORCESTP",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"],
    "LOAD_CASE_NAMES": ["Prestress(ST)"],
    "PARTS": ["PartI", "PartJ"]
  }
}
```

**POST Response Body**

```json
{
  "BeamForcePS": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Type", "Axial", "Shear-z", "Moment-y"],
    "DATA": [
      ["1", "1", "Prestress", "I", "Pre", "-1200.0000", "50.0000", "0.0000"]
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

# ── POST: 提取静力预应力梁构件内力 ─────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamForcePS",
        "TABLE_TYPE": "BEAMFORCESTP",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "LOAD_CASE_NAMES": ["Prestress(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamForcePS", {})
print(f"预应力构件内力 {len(table.get('DATA', []))}行")
```

---

## 10. Beam Stress

> **功能：** 提取梁单元的应力（轴应力·剪应力·弯曲应力·组合应力）。支持包含 7th DOF（翘曲，Warping）的选项。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BEAMSTRESS"` | 梁应力 |
| `"BEAMSTRESS7DOF"` | 梁应力（含 7th DOF – Warping） |
| `"BEAMSTRESSVBM"` | 梁应力（按最大值，View by Max Value） |

> ⚠️ 2026-08-26 确认（article id `36011455813273`）：`BEAMSTRESSVBM` 在此前版本文档中有遗漏
> — 官方 JSON Schema 的 enum 中没有该值，但 Specifications 表与完整的 Request/Response
> 示例均存在，故判断为实际存在的取值并加以补全（属 schema 落后于示例·表的案例）。

### 构件位置·截面位置（Parts / Section Position）指定

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 11 | 构件位置 · I端：`"PartI"` / 1/4点：`"Part1/4"` / 2/4点：`"Part2/4"` / 3/4点：`"Part3/4"` / J端：`"PartJ"` | `"PARTS"` | Array [String] | All | Optional |
| 12 | 截面位置（`BEAMSTRESS7DOF` 专用） · `"Pos-1"`/`"Pos-2"`/`"Pos-3"`/`"Pos-4"`/`"Max"` | `"SECTION_POSITION"` | Array [String] | All | Optional |
| 13 | 最大值计算对象分量（`BEAMSTRESSVBM` 专用） · `Axial`/`Shear-y`/`Shear-z`/`Bend(+y)`/`Bend(-y)`/`Bend(+z)`/`Bend(-z)` | `"ITEM_TO_DISPLAY"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 确认：上述3个参数（`PARTS`/`SECTION_POSITION`/`ITEM_TO_DISPLAY`）在此
> 前版本文档中均有遗漏。

### 施工阶段（Construction Stage）专用参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 激活施工阶段步骤（按取值区分的行为见[通用参数表](#通用-request-结构与参数) ⚠️ 注释） | `"OPT_CS"` | Boolean | `false`（标注写法上） | Optional |
| 2 | 施工阶段步骤名称列表 | `"STAGE_STEP"` | Array [String] | All | Optional |

> ⚠️ 2026-08-30 定期检查确认（article id `36011455813273`，原文更新 2026-08-27）：原文已新增/补强
> `BEAMSTRESS`·`BEAMSTRESS7DOF` 的施工阶段（CS）查询示例，但此前版本文档未
> 反映 — 通过 `OPT_CS`/`STAGE_STEP`（通用参数）按施工阶段步骤查询结果，
> `BEAMSTRESSVBM` 原文没有 CS 专用示例（仅存在非 CS 示例）。

### Response HEAD

- `BEAMSTRESS`：`["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"]`（查询施工阶段时在 `Load` 之后追加 `Stage`/`Step`）
- `BEAMSTRESSVBM`：除在 `Part` 之后新增 `Component` 列外与 `BEAMSTRESS` 相同 — `["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"]`
- `BEAMSTRESS7DOF`：完全不同的结构 — `["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"]`（查询施工阶段时在 `Load` 之后追加 `Stage`/`Step`）

> ⚠️ 2026-08-26 确认：此前版本文档只标注了单一 HEAD，容易让人误以为 `BEAMSTRESS7DOF` 也使用与
> `BEAMSTRESS` 相同的 HEAD，实则明确为使用 7th DOF 专用列（`SectionPosition`、
> `Sax(Warping)`、`Ssy/Ssz(Mt/Mw)`、`Cb(Ssy/Ssz)`）的独立结构。

### Request / Response JSON

**POST Request Body — BEAMSTRESS（General）**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress",
    "TABLE_TYPE": "BEAMSTRESS",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)"],
    "NODE_ELEMS": { "TO": "1 to 10" },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
  }
}
```

**POST Response Body — BEAMSTRESS（General）**

```json
{
  "BeamStress": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "DATA": [
      ["1", "1", "Selfweight", "I", "0.0000", "0.0000", "1250.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000", "0.0000"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS（施工阶段）**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress",
    "TABLE_TYPE": "BEAMSTRESS",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Stage", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "PARTS": ["PartI", "PartJ"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS3:001(first)", "CS3:002(last)"]
  }
}
```

**POST Response Body — BEAMSTRESS（施工阶段）**

```json
{
  "BeamStress": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Stage", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "DATA": [
      ["1", "1", "Summation", "CS3", "001(first)", "I[1]", "-0.774105629705", "0.000000000000", "-0.633378895214", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-0.774105629705", "-0.774105629705", "-0.774105629705", "-0.774105629705", "-0.774105629705"],
      ["2", "1", "Summation", "CS3", "001(first)", "J[2]", "-0.787581597130", "0.000000000000", "-0.510199230117", "0.000000000000", "0.000000000000", "-1.517545803005", "1.519418342486", "-2.328225752254", "-2.282028873379", "-2.328225752254", "0.754933827124", "0.708739639195"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS7DOF（General）**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress(7thDOF)",
    "TABLE_TYPE": "BEAMSTRESS7DOF",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["EccentricLoads(ST)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Pos-1", "Max"]
  }
}
```

**POST Response Body — BEAMSTRESS7DOF（General）**

```json
{
  "BeamStress(7thDOF)": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "DATA": [
      ["1", "1", "EccentricLoads", "I[1]", "Pos-1", "0.000000000000", "-0.000769832639", "0.014441854460", "-0.000722966974", "0.009767207099", "0.013672021820", "0.009044240125"],
      ["2", "1", "EccentricLoads", "I[1]", "Max", "0.000000000000", "-0.000769832639", "0.014441854460", "-0.000722966974", "0.009767207099", "0.013672021820", "0.009044240125"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS7DOF（施工阶段）**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress(7thDOF)",
    "TABLE_TYPE": "BEAMSTRESS7DOF",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Stage", "Step", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["Summation(CS)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Pos-1", "Max"],
    "OPT_CS": true,
    "STAGE_STEP": ["CS3:001(first)", "CS3:002(last)"]
  }
}
```

**POST Response Body — BEAMSTRESS7DOF（施工阶段）**

```json
{
  "BeamStress(7thDOF)": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Stage", "Step", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Cb(Ssy)", "Cb(Ssz)"],
    "DATA": [
      ["1", "1", "Summation", "CS3", "001(first)", "I[1]", "Pos-1", "0.000000000000", "-0.202862111996", "69.145522875219", "-0.190512326587", "46.763983379006", "68.942660763224", "46.573471052419"],
      ["2", "1", "Summation", "CS3", "001(first)", "I[1]", "Max", "0.000000000000", "-0.202862111996", "69.145522875219", "-0.190512326587", "46.763983379006", "68.942660763224", "46.573471052419"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESSVBM（View by Max Value）**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStressViewByMaxValue",
    "TABLE_TYPE": "BEAMSTRESSVBM",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "NODE_ELEMS": { "KEYS": [2833] },
    "LOAD_CASE_NAMES": ["STLENV_SER(CB:max)", "STLENV_SER(CB:min)"],
    "PARTS": ["PartI", "PartJ"],
    "ITEM_TO_DISPLAY": ["Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)"]
  }
}
```

**POST Response Body — BEAMSTRESSVBM（View by Max Value）**

```json
{
  "BeamStressViewByMaxValue": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Component", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)", "Cb(min/max)", "Cb1(-y+z)", "Cb2(+y+z)", "Cb3(+y-z)", "Cb4(-y-z)"],
    "DATA": [
      ["1", "2833", "STLENV_SER(max)", "I[781]", "Axial", "14501.204492710700", "10.364105217203", "1287.477776027480", "-190.557266825830", "190.557266825830", "-12261.744480687799", "32108.382246495301", "46800.144006031900", "2430.017278848780", "2048.902745197120", "46419.029472380200", "46800.144006031900"]
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

# ── POST: 提取梁应力（含 7th DOF 时 TABLE_TYPE=BEAMSTRESS7DOF） ─
payload = {
    "Argument": {
        "TABLE_NAME": "BeamStress",
        "TABLE_TYPE": "BEAMSTRESS",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "NODE_ELEMS": {"TO": "1 to 10"},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamStress", {})
print(f"梁应力 {len(table.get('DATA', []))}行")
```

---

## 11. Beam Stress (Equivalent)

> **功能：** 提取梁单元的等效应力（Equivalent，按截面位置的详细应力 – 法向·剪切·Von-Mises·最大剪切·主应力）。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BEAMSTRESSDETAIL"` | 梁等效应力（详细） |

### 构件位置·截面位置（Parts / Section Position）指定

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 11 | 构件位置 · I端：`"PartI"` / 1/4点：`"Part1/4"` / 2/4点：`"Part2/4"` / 3/4点：`"Part3/4"` / J端：`"PartJ"` | `"PARTS"` | Array [String] | All | Optional |
| 12 | 截面位置（方钢管·工形钢截面的应力验算点编号） · 最大值：`"Maximum"` / 1~28号位置：`"1"`~`"28"` | `"SECTION_POSITION"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 确认（article id `36011572000153`）：`PARTS`·`SECTION_POSITION` 在此前版本
> 文档中均有遗漏。注意 `SECTION_POSITION` 的取值体系与第10节（Beam Stress）`BEAMSTRESS7DOF`
> 的 `"Pos-1"`~`"Pos-4"`/`"Max"` 不同，是本表格专用的编号（`"1"`~`"28"`）/`"Maximum"` 体
> 系。

### Response HEAD

`["Index", "Elem", "Load", "Part", "SectionPosition", "Normal", "Tau_xy", "Tau_xz", "Von-Mises", "Max-Shear", "Princ.(max)", "Princ.(min)"]`

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStressEq",
    "TABLE_TYPE": "BEAMSTRESSDETAIL",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Normal", "Tau_xy", "Tau_xz", "Von-Mises", "Max-Shear", "Princ.(max)", "Princ.(min)"],
    "NODE_ELEMS": { "KEYS": [32] },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Maximum", "12"]
  }
}
```

**POST Response Body**

```json
{
  "BeamStressEq": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Normal", "Tau_xy", "Tau_xz", "Von-Mises", "Max-Shear", "Princ.(max)", "Princ.(min)"],
    "DATA": [
      ["1", "32", "Selfweight", "I", "1", "0.0000", "0.0000", "1250.0000", "2165.0635", "1250.0000", "1250.0000", "-1250.0000"]
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

# ── POST: 提取梁等效应力（详细） ──────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamStressEq",
        "TABLE_TYPE": "BEAMSTRESSDETAIL",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [32]},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamStressEq", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 位置{d['SectionPosition']}: Von-Mises={d['Von-Mises']}")
```

---

## 12. Beam Stress (PSC)

> **功能：** 按分量（轴力·弯矩·预应力束·合计·剪力·扭转·主应力等）详细提取 PSC（预应力混凝土）梁单元的应力。支持包含 7th DOF 的选项。

### `TABLE_TYPE`

| 值 | 说明 |
|----|------|
| `"BEAMSTRESSPSC"` | PSC 梁应力 |
| `"BEAMSTRESS7DOFPSC"` | PSC 梁应力（含 7th DOF – Warping） |

### 构件位置·截面位置（Parts / Section Position）指定

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 11 | 构件位置 · I端：`"PartI"` / 1/4点：`"Part1/4"` / 2/4点：`"Part2/4"` / 3/4点：`"Part3/4"` / J端：`"PartJ"` | `"PARTS"` | Array [String] | All | Optional |
| 12 | 截面位置（`BEAMSTRESS7DOFPSC` 专用） · `"Pos-1"`~`"Pos-16"` / 最大值：`"Max"` / 最小值：`"Min"` / 全部：`"All"` | `"SECTION_POSITION"` | Array [String] | All | Optional |

> ⚠️ 2026-08-26 确认（article id `36011704177561`）：`PARTS`·`SECTION_POSITION` 在此前版本
> 文档中均有遗漏。`SECTION_POSITION` 的位置个数（16个）多于第10节 `BEAMSTRESS7DOF`（4个）
> — 推测因 PSC 截面具有更细化的验算点。

### Response HEAD

- `BEAMSTRESSPSC`：`["Index", "Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Moment-z)", "Sig-xx(Bar)", "Sig-xx(Summation)", "Sig-zz", "Sig-xz(shear)", "Sig-xz(torsion)", "Sig-xz(bar)", "Sig-Is(shear)", "Sig-Is(shear+torsion)", "Sig-Ps(Max)", "Sig-Ps(Min)"]`
- `BEAMSTRESS7DOFPSC`：完全不同的结构 — `["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Combined(Ssy)", "Combined(Ssz)"]`

> ⚠️ 2026-08-26 确认：`BEAMSTRESS7DOFPSC` 与第10节 `BEAMSTRESS7DOF` 概念类似（同样的
> Sax/Ssy/Ssz 结构），但最后两列名不写作 `Cb(Ssy)`/`Cb(Ssz)` 而是
> `Combined(Ssy)`/`Combined(Ssz)` — 判断为原文两篇独立撰写的文章之间的命名不一致
> （更像信息性记录而非错误，报错对象）。

### Request / Response JSON

**POST Request Body — BEAMSTRESSPSC**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStressPSC",
    "TABLE_TYPE": "BEAMSTRESSPSC",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Scientific", "PLACE": 4 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Summation)", "Sig-Ps(Max)", "Sig-Ps(Min)"],
    "NODE_ELEMS": { "TO": "1 to 5" },
    "LOAD_CASE_NAMES": ["Selfweight(ST)"]
  }
}
```

**POST Response Body — BEAMSTRESSPSC**

```json
{
  "BeamStressPSC": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Sig-xx(Axial)", "Sig-xx(Moment-y)", "Sig-xx(Moment-z)", "Sig-xx(Bar)", "Sig-xx(Summation)", "Sig-zz", "Sig-xz(shear)", "Sig-xz(torsion)", "Sig-xz(bar)", "Sig-Is(shear)", "Sig-Is(shear+torsion)", "Sig-Ps(Max)", "Sig-Ps(Min)"],
    "DATA": [
      ["1", "1", "Selfweight", "I", "1", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00", "0.000e+00"]
    ]
  }
}
```

**POST Request Body — BEAMSTRESS7DOFPSC**

```json
{
  "Argument": {
    "TABLE_NAME": "BeamStress(7thDOF)(PSC)",
    "TABLE_TYPE": "BEAMSTRESS7DOFPSC",
    "UNIT": { "FORCE": "N", "DIST": "mm" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Combined(Ssy)", "Combined(Ssz)"],
    "NODE_ELEMS": { "KEYS": [1] },
    "LOAD_CASE_NAMES": ["EccentricLoads(ST)"],
    "PARTS": ["PartI", "PartJ"],
    "SECTION_POSITION": ["Pos-7", "All"]
  }
}
```

**POST Response Body — BEAMSTRESS7DOFPSC**

```json
{
  "BeamStress(7thDOF)(PSC)": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Elem", "Load", "Part", "SectionPosition", "Sax(Warping)", "Ssy(Mt)", "Ssy(Mw)", "Ssz(Mt)", "Ssz(Mw)", "Combined(Ssy)", "Combined(Ssz)"],
    "DATA": [
      ["1", "1", "EccentricLoads", "I[1]", "Pos-7", "0.000000000000", "-0.000020377582", "-0.000013533950", "-0.023715019562", "-0.006463496296", "-0.000033911532", "-0.030178515858"],
      ["2", "1", "EccentricLoads", "I[1]", "All", "0.000000000000", "-0.023715019562", "-0.023273488440", "0.023715021748", "-0.015750538530", "-0.039465558092", "-0.039465558092"]
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

# ── POST: 提取 PSC 梁应力（含 7th DOF 时为 BEAMSTRESS7DOFPSC） ─────
payload = {
    "Argument": {
        "TABLE_NAME": "BeamStressPSC",
        "TABLE_TYPE": "BEAMSTRESSPSC",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Scientific", "PLACE": 4},
        "NODE_ELEMS": {"TO": "1 to 5"},
        "LOAD_CASE_NAMES": ["Selfweight(ST)"]
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("BeamStressPSC", {})
head = table.get("HEAD", [])
for row in table.get("DATA", []):
    d = dict(zip(head, row))
    print(f"  Elem {d['Elem']} 位置{d['SectionPosition']}: 合计应力={d['Sig-xx(Summation)']}")
```

---

## 13. Concurrent Joint Force

> **功能：** 在指定反力节点（`NODE_KEY`）的反力分量取极值（max/min）的时刻，将指定
> 荷载工况列表的节点力作为同时（concurrent）值提取。移动荷载（Moving Load）分析中
> 多与 `(MV:max)` / `(MV:min)` 系列荷载工况配合使用。

### `TABLE_TYPE`

| 值 | 说明 |
| --- | --- |
| `"CONCURRENT_JOINT_FORCE"` | 同时节点力（Concurrent Joint Force） |

> ⚠️ 2026-08-26 确认（article id `59520540732185`）：本表格不使用通用参数表（上方「通用 Request
> 结构与参数」），而是具有**自己独立的 schema**，官方 JSON Schema 上挂了
> `"additionalProperties": false`，因此通用项中的 `NODE_ELEMS`/`OPT_CS`/`STAGE_STEP`
> **在本表格中不存在也无法使用**（发送时可能被拒绝）。允许的字段仅有
> `TABLE_TYPE`/`LOAD_CASE_NAMES`/`TABLE_NAME`/`EXPORT_PATH`/`UNIT`/`STYLES`/`COMPONENTS`/
> `ADDITIONAL` 8个。此外 `LOAD_CASE_NAMES` 与其他12个表格不同（通用表为
> Optional·默认 All），它包含在官方 schema 的 `required` 中，为 **Required**。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 1 | 荷载工况名称列表 | `"LOAD_CASE_NAMES"` | Array [String] | — | **Required** |
| 2 | 反力极值基准附加设置 | `"ADDITIONAL"` | Object | — | **Required** |
| 2-1 | └ 反力节点基准设置 | `ADDITIONAL.SET_REACTION_PARAMS` | Object | — | **Required** |
| 2-1-1 | 　└ 反力节点 ID | `SET_REACTION_PARAMS.NODE_KEY` | Integer | — | **Required** |
| 2-1-2 | 　└ 反力分量使用与否6位（0/1），顺序 Fx·Fy·Fz·Mx·My·Mz | `SET_REACTION_PARAMS.COMPONENT` | String | — | **Required** |

### Response HEAD

响应 `HEAD` 在基本的 `"Index"`/`"Elem."`/`"Load"` 3列之后，将 `"Elem./Component"` + `9[J]/Fx`~
`10[I]/Mz`（夹在反力节点两侧的两个相邻单元 × 6分量 = 12列）13列的块**按反力分量个数
（Fx/Fy/Fz/Mx/My/Mz 最多6个）重复**拼接而成。

`DATA`（与此前版本文档相反）**按每个单元组成一行** — 节点两侧的两个单元（`9[J]`、
`10[I]`）各为一行，每行内上述13列块按反力分量（Fx/Fy/Fz/Mx/My/Mz）个数
重复（每个块的首格为 `"Fx"`~`"Mz"` 标签，其余12格为该分量取极值时刻的同时节点力）。

> ⚠️ 2026-08-26 确认：此前版本文档对该结构的说明是反的（「按分量一行、按单元重复
> 块」）— 实际上如上所述为按单元一行、按分量重复块。下方示例是原样搬运官方示例的（1个荷载
> 工况 × 选择6个反力分量时81列：`Index`/`Elem.`/`Load` 3列 + 13列 ×
> 6块）。

### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "TABLE_TYPE": "CONCURRENT_JOINT_FORCE",
    "LOAD_CASE_NAMES": ["case_01(MV:max)"],
    "TABLE_NAME": "Concurrent Joint Forces",
    "ADDITIONAL": {
      "SET_REACTION_PARAMS": {
        "NODE_KEY": 10,
        "COMPONENT": "111111"
      }
    },
    "UNIT": { "FORCE": "KN", "DIST": "M" }
  }
}
```

**POST Response Body**

```json
{
  "Concurrent Joint Forces": {
    "FORCE": "KN",
    "DIST": "M",
    "HEAD": [
      "Index", "Elem.", "Load",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz",
      "Elem./Component", "9[J]/Fx", "9[J]/Fy", "9[J]/Fz", "9[J]/Mx", "9[J]/My", "9[J]/Mz", "10[I]/Fx", "10[I]/Fy", "10[I]/Fz", "10[I]/Mx", "10[I]/My", "10[I]/Mz"
    ],
    "DATA": [
      [
        "1", "9[J]", "case_01(max)",
        "Fx", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fy", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fz", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000",
        "Mx", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000",
        "My", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000",
        "Mz", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"
      ],
      [
        "2", "10[I]", "case_01(max)",
        "Fx", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fy", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000",
        "Fz", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000", "0.000000000000", "0.000000000000", "437.017000000000", "-558.415000000000", "938.805000000000", "0.000000000000",
        "Mx", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-41.903300000000", "216.858000000000", "190.624000000000", "0.000000000000",
        "My", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000", "0.000000000000", "0.000000000000", "399.782000000000", "-422.014000000000", "1067.630000000000", "0.000000000000",
        "Mz", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000"
      ]
    ]
  }
}
```

> ⚠️ 2026-08-26 确认：官方 Response Example 虽与上述请求（`TABLE_NAME: "Concurrent Joint Forces"`）
> 配对，但响应最外层键不是请求的 `TABLE_NAME` 而是字面量 `"empty"`
> （`{"empty": {...}}`）。与本章节其他所有表格及通用 Response 结构（`{"<TABLE_NAME>": {...}}`）
> 的惯例不符，但因无依据判断这是撰写原文时未替换实际值的复制粘贴失误、还是该端点独有的
> 实际行为，故在「实际 API 行为未经验证」的前提下仅作为报错对象保留，上方示例仍按惯例
> 保留了 `"Concurrent Joint Forces"` 键。

### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── POST: 提取反力节点10取极值时刻的同时节点力 ──────────────────
payload = {
    "Argument": {
        "TABLE_TYPE": "CONCURRENT_JOINT_FORCE",
        "TABLE_NAME": "Concurrent Joint Forces",
        "LOAD_CASE_NAMES": ["case_01(MV:max)"],
        "ADDITIONAL": {
            "SET_REACTION_PARAMS": {"NODE_KEY": 10, "COMPONENT": "111111"}
        },
        "UNIT": {"FORCE": "KN", "DIST": "M"}
    }
}
resp = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS)
table = resp.json().get("Concurrent Joint Forces", {})
print(f"同时节点力 {len(table.get('DATA', []))}行")
```

---

## End-to-End Workflow

以下为执行分析后批量提取反力·位移·构件内力·应力的工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

def get_result(table_type, name, load_cases, extra=None):
    """提取分析结果表格的通用函数"""
    arg = {
        "TABLE_NAME": name,
        "TABLE_TYPE": table_type,
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "LOAD_CASE_NAMES": load_cases
    }
    if extra:
        arg.update(extra)
    resp = requests.post(f"{BASE_URL}/post/TABLE", json={"Argument": arg}, headers=HEADERS)
    return resp.json().get(name, {})

# ── STEP 1: 支座反力（全局） ───────────────────────────────────────
reac = get_result("REACTIONG", "Reaction", ["DL(ST)"])
print(f"STEP1 反力 {len(reac.get('DATA', []))}行")

# ── STEP 2: 节点位移（全局） ───────────────────────────────────────
disp = get_result("DISPLACEMENTG", "Disp", ["DL(ST)"])
print(f"STEP2 位移 {len(disp.get('DATA', []))}行")

# ── STEP 3: 桁架构件内力·应力 ─────────────────────────────────────
tf = get_result("TRUSSFORCE", "TrussF", ["DL(ST)"])
ts = get_result("TRUSSSTRESS", "TrussS", ["DL(ST)"])
print(f"STEP3 桁架: 构件内力 {len(tf.get('DATA', []))}, 应力 {len(ts.get('DATA', []))}")

# ── STEP 4: 梁构件内力·应力（1~10号单元） ───────────────────────────
bf = get_result("BEAMFORCE", "BeamF", ["DL(ST)"], extra={"NODE_ELEMS": {"TO": "1 to 10"}})
bs = get_result("BEAMSTRESS", "BeamS", ["DL(ST)"], extra={"NODE_ELEMS": {"TO": "1 to 10"}})
print(f"STEP4 梁: 构件内力 {len(bf.get('DATA', []))}, 应力 {len(bs.get('DATA', []))}")

# ── STEP 5: 拉索张力（施工阶段） ─────────────────────────────────
cf = get_result("CABLEFORCE", "CableF", ["SelfWeight(CS)"],
                extra={"OPT_CS": True, "STAGE_STEP": ["nl_001"]})
print(f"STEP5 拉索张力 {len(cf.get('DATA', []))}行")
```
