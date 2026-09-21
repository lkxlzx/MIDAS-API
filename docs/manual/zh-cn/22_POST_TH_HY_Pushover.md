# 22. POST – TH / HY / Pushover Result Tables（时程·水化热·推覆结果）

> **适用产品：** MIDAS Gen NX · MIDAS Civil NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头：** `MAPI-Key: <已签发密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../22_POST_TH_HY_Pushover.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

本部分处理**时程（Time History）· 水化热（Heat of Hydration）· 推覆（Pushover）**分析结果，共由 **28个Endpoint** 组成。与前面的第19~21章不同，本部分的Endpoint分属**互不相同的4个URI组**，因此各组的请求结构不同。

| 组 | 内容 | 公共 URI | 方法 | Endpoint 数 |
|------|------|----------|--------|:---:|
| **A** | 时程 / 推覆文本结果 | `POST {base url}/post/TEXT` | `POST` | 10 |
| **B** | 非弹性铰（Inelastic Hinge）时程结果表格 | `POST {base url}/post/TABLE` | `POST` | 9 |
| **C** | 水化热分析结果图形显示 | `POST {base url}/view/RESULTGRAPHIC` | `POST` | 5 |
| **D** | 时程智能图表定义 DB | `{base url}/db/THR*` | `POST · GET · PUT · DELETE` | 4 |

### 全部 Endpoint 汇总 (28个)

| # | 节 | Endpoint(标题) | 组 | URI | 方法 |
|---|-----|------------------|:---:|-----|--------|
| 1 | [A-1](#a-1-time-history-text--node-results) | Time History Text – Node Results | A | `post/TEXT` | POST |
| 2 | [A-2](#a-2-time-history-text--element-resulttruss-beam-plane-stressstrain-solid) | TH Text – Element (Truss/Beam/Plane/Solid) | A | `post/TEXT` | POST |
| 3 | [A-3](#a-3-time-history-text--element-resultplate) | TH Text – Element (Plate) | A | `post/TEXT` | POST |
| 4 | [A-4](#a-4-time-history-text--element-resultwall) | TH Text – Element (Wall) | A | `post/TEXT` | POST |
| 5 | [A-5](#a-5-time-history-text--general-link-result) | TH Text – General Link | A | `post/TEXT` | POST |
| 6 | [A-6](#a-6-pushover-text--displacement) | Pushover Text – Displacement | A | `post/TEXT` | POST |
| 7 | [A-7](#a-7-pushover-text--element-resultbeam-truss) | Pushover Text – Element (Beam, Truss) | A | `post/TEXT` | POST |
| 8 | [A-8](#a-8-pushover-text--element-resultwall) | Pushover Text – Element (Wall) | A | `post/TEXT` | POST |
| 9 | [A-9](#a-9-pushover-text--general-link) | Pushover Text – General Link | A | `post/TEXT` | POST |
| 10 | [A-10](#a-10-pushover-text--elastic-link) | Pushover Text – Elastic Link | A | `post/TEXT` | POST |
| 11 | [B-1](#b-1-inelastic-hinge-event-time) | Inelastic Hinge Event Time | B | `post/TABLE` | POST |
| 12 | [B-2](#b-2-inelastic-hinge-beam-summary) | Inelastic Hinge Beam Summary | B | `post/TABLE` | POST |
| 13 | [B-3](#b-3-inelastic-hinge-truss-summary) | Inelastic Hinge Truss Summary | B | `post/TABLE` | POST |
| 14 | [B-4](#b-4-inelastic-hinge-general-link-summary) | Inelastic Hinge General Link Summary | B | `post/TABLE` | POST |
| 15 | [B-5](#b-5-inelastic-hinge-force) | Inelastic Hinge Force | B | `post/TABLE` | POST |
| 16 | [B-6](#b-6-inelastic-hinge-deformation) | Inelastic Hinge Deformation | B | `post/TABLE` | POST |
| 17 | [B-7](#b-7-inelastic-hinge-element-rotation) | Inelastic Hinge Element Rotation | B | `post/TABLE` | POST |
| 18 | [B-8](#b-8-inelastic-hinge-ductility-factordd1) | Inelastic Hinge Ductility Factor (D/D1) | B | `post/TABLE` | POST |
| 19 | [B-9](#b-9-inelastic-hinge-ductility-factordd2) | Inelastic Hinge Ductility Factor (D/D2) | B | `post/TABLE` | POST |
| 20 | [C-1](#c-1-stress--heat-of-hydration) | Stress | C | `view/RESULTGRAPHIC` | POST |
| 21 | [C-2](#c-2-temperature--heat-of-hydration) | Temperature | C | `view/RESULTGRAPHIC` | POST |
| 22 | [C-3](#c-3-displacements--heat-of-hydration) | Displacements | C | `view/RESULTGRAPHIC` | POST |
| 23 | [C-4](#c-4-allowable-tensile-stress--heat-of-hydration) | Allowable Tensile Stress | C | `view/RESULTGRAPHIC` | POST |
| 24 | [C-5](#c-5-crack-ratio--heat-of-hydration) | Crack Ratio | C | `view/RESULTGRAPHIC` | POST |
| 25 | [D-1](#d-1-element-force-smart-graph--dbthre) | Element Force Smart Graph | D | `db/THRE` | POST·GET·PUT·DELETE |
| 26 | [D-2](#d-2-general-link-smart-graph--dbthrg) | General Link Smart Graph | D | `db/THRG` | POST·GET·PUT·DELETE |
| 27 | [D-3](#d-3-inelastic-hinge-smart-graph--dbthri) | Inelastic Hinge Smart Graph | D | `db/THRI` | POST·GET·PUT·DELETE |
| 28 | [D-4](#d-4-seismic-devices-smart-graph--dbthrs) | Seismic Devices Smart Graph | D | `db/THRS` | POST·GET·PUT·DELETE |

---

## A 组. Time History / Pushover Text 结果 (`post/TEXT`)

时程·推覆分析的详细结果以**文本（JSON）表格**形式提取。反力·位移表格（第19章）使用的是 `post/TABLE` + `TABLE_TYPE`，而本组使用的是 **`post/TEXT` + `TEXT_TYPE`**。

### Input URI（A 组公共）

```
{base url}/post/TEXT
```

### Active Methods

`POST`

### 公共 Request 结构与参数

在请求体的 `"Argument"` 对象中用 `TEXT_TYPE` 选择结果种类。**下表对A组的10个Endpoint全部通用**，各节仅另行说明 `TEXT_TYPE` enum、响应 `HEAD` 和代表示例。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 结果文本类型（按Endpoint的enum，各节参照） | `"TEXT_TYPE"` | String | — | **Required** |
| 2 | 结果保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 3 | 响应单位设置 | `"UNIT"` | Object | System | Optional |
| 3-1 | └ 力(Force) | `UNIT.FORCE` | String | — | Optional |
| 3-2 | └ 长度(Length) | `UNIT.DIST` | String | — | Optional |
| 3-3 | └ 热(Heat) | `UNIT.HEAT` | String | — | Optional |
| 3-4 | └ 温度(Temperature) | `UNIT.TEMP` | String | — | Optional |
| 4 | 响应数字格式 | `"STYLES"` | Object | System | Optional |
| 4-1 | └ 数字格式 · `"Fixed"` / `"Exponential"` | `STYLES.FORMAT` | String | — | Optional |
| 4-2 | └ 小数位数 (0~15) | `STYLES.PLACE` | Integer | — | Optional |
| 5 | 结果表格显示列 | `"COMPONENTS"` | Array [String] | All | Optional |
| 6 | 节点/单元指定（下列方式之一） | `"NODE_ELEMS"` | Object | — | **Required** |
| 6-1 | 方式1：逐个指定 ID（例：`[101, 102, 103]`） | `NODE_ELEMS.KEYS` | Array [Integer] | — | Optional |
| 6-2 | 方式2：指定 ID 范围（例：`"101 to 105"`） | `NODE_ELEMS.TO` | String | — | Optional |
| 6-3 | 方式3：指定结构组名（例：`"SG1"`） | `NODE_ELEMS.STRUCTURE_GROUP_NAME` | String | — | Optional |
| 7 | 单元结果输出位置（仅单元结果） | `"PARTS"` | Array [String] | — | Optional |
| 8 | **时程荷载工况**（仅 TH 结果） | `"TH_CASE_NAME"` | Array [String] | — | **Required** |
| 9 | **推覆荷载工况**（仅 Pushover 结果） | `"PO_CASE_NAME"` | Array [String] | — | **Required** |
| 10 | 指定输出步 | `"STEP"` | Object | — | **Required** |
| 10-1 | └ 起始时间/步 | `STEP.FROM` | Number | — | Required |
| 10-2 | └ 结束时间/步 | `STEP.TO` | Number | — | Required |
| 10-3 | └ 时间间隔/步间隔 | `STEP.STEPS` | Integer | — | Required |
| 11 | 基准点(方式1) · `"Ground"` / `"AddGroundMotion"` | `"REF_PT"` | String | `"Ground"` | Optional |
| 12 | 基准点(方式2) · 指定其他节点 | `"ANR_NODE"` | Integer | — | Optional |

> **参考**
> - **`TH_CASE_NAME` vs `PO_CASE_NAME`：** 时程结果(A-1~A-5)用 `TH_CASE_NAME`，推覆结果(A-6~A-10)用 `PO_CASE_NAME`。
> - **`STEP`：** 时程中 `FROM`/`TO` 是**时间(秒)**，推覆中是**步编号**。
> - **`PARTS`：** 梁/桁架/墙结果用 `["PartI", "PartJ"]`，平板(Plate)4节点单元用 `["PartI", "PartJ", "PartK", "PartL"]`。节点结果·一般连接结果不使用。
> - **`REF_PT`/`ANR_NODE`：** 惯性响应(位移/速度/加速度)的基准点设置。在节点结果·位移结果中使用。
>
> ⚠️ 2026-08-26 确认（article id `36704969941913` 等A组全部）：官方 JSON Schema 把选择结果种类的
> 字段名误记为 `"TABLE_TYPE"`（疑似复制了 `post/TABLE` 的规格）。但所有 Request/Response 示例实际
> 使用的都是 `"TEXT_TYPE"`，只有照此取值才能得到响应（示例优先于表/Schema —— CLAUDE.md 判断原则）。
> 本仓库从一开始就正确记为 `"TEXT_TYPE"`，没有需要更正的内容，但留下本注释，以免下次同步时以 Schema
> 侧的 `"TABLE_TYPE"` 写法为依据回改。

### 公共 Response 结构

```json
{
  "<TEXT_TYPE>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."], ["2", "..."]]
  }
}
```

---

### A-1. Time History Text – Node Results

> **功能：** 在时程分析中按时间步提取节点（Node）的**位移·速度·加速度**。

#### `TEXT_TYPE`

| 值 | 说明 |
|----|------|
| `"TH_DISP"` | 位移(Displacement) |
| `"TH_VELOCITY"` | 速度(Velocity) |
| `"TH_ACCEL"` | 加速度(Acceleration) |

#### Response HEAD

`["Index", "Node", "Load", "Time/Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"]`

#### Request / Response JSON

**POST Request Body — 位移(TH_DISP)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_DISP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_Displacement_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Node", "Load", "Time/Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "NODE_ELEMS": { "KEYS": [10] },
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.5, "STEPS": 1 },
    "REF_PT": "Ground"
  }
}
```

**POST Response Body**

```json
{
  "TH_DISP": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Node", "Load", "Time/Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "DATA": [
      ["1", "10", "Elcent", "0.100", "-0.212573", "-0.367424", "-0.374784", "0.000018", "-0.000011", "0.000022"],
      ["2", "10", "Elcent", "0.200", "-0.748871", "-1.793398", "-1.889303", "0.000136", "-0.000116", "0.000139"],
      ["3", "10", "Elcent", "0.300", "-2.190583", "-6.156868", "-6.706040", "0.000636", "-0.000576", "0.000505"],
      ["4", "10", "Elcent", "0.400", "-2.740721", "-12.268332", "-14.108861", "0.001874", "-0.001677", "0.001110"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 在0.1~0.5秒区间提取节点10号的时程位移 ─────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_DISP",                 # 位移结果
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [10]},           # 节点10号
        "TH_CASE_NAME": ["Elcent"],             # 时程荷载工况名
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
        "REF_PT": "Ground",                     # 基准点：地面
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
table = res["TH_DISP"]
print("HEAD:", table["HEAD"])
for row in table["DATA"]:
    print(f"  t={row[3]}s  Dx={row[4]}  Dy={row[5]}  Dz={row[6]}")
```

---

### A-2. Time History Text – Element Result(Truss, Beam, Plane Stress/Strain, Solid)

> **功能：** 提取时程分析中**桁架·梁·平面应力·平面应变·实体**单元的构件内力/应力。共有10个 `TEXT_TYPE`，各类型的响应 `HEAD` 不同。

#### `TEXT_TYPE` 及 Response HEAD

| `TEXT_TYPE` | 说明 | Response `HEAD` |
|-------------|------|-----------------|
| `"TH_TRUSSFORCE"` | 桁架构件内力 | `["Index", "Elem", "Load", "Time/Step", "Force-I", "Force-J"]` |
| `"TH_TRUSSSTRESS"` | 桁架应力 | `["Index", "Elem", "Load", "Time/Step", "Stress-I", "Stress-J"]` |
| `"TH_BEAMFORCE"` | 梁构件内力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]` |
| `"TH_BEAMSTRESS"` | 梁应力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Bend(+y)", "Bend(-y)", "Bend(+z)", "Bend(-z)"]` |
| `"TH_PLANE_STRESS_FORCE"` | 平面应力构件内力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fx", "Fy"]` |
| `"TH_PLANESTRESS"` | 平面应力应力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx", "Sig-yy", "Sig-xy"]` |
| `"TH_PLANE_STRAIN_FORCE"` | 平面应变构件内力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fx", "Fy", "Fz"]` |
| `"TH_PLANE_STRAIN_STRESS"` | 平面应变应力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy"]` |
| `"TH_SOLIDFORCE"` | 实体构件内力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fx", "Fy", "Fz"]` |
| `"TH_SOLIDSTRESS"` | 实体应力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx", "Sig-yy", "Sig-zz", "Sig-xy", "Sig-yz", "Sig-xz"]` |

#### Request / Response JSON

**POST Request Body — 梁构件内力(TH_BEAMFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_BeamForce_Out.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Part", "Time/Step", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [5] },
    "PARTS": ["PartI", "PartJ"],
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.5, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "TH_BEAMFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "5", "Elcent", "0.100", "I[10]", "2.856739", "-1.766507", "0.146287", "-0.353369", "0.592988", "-2.089716"],
      ["2", "5", "Elcent", "0.100", "J[34]", "2.856739", "-1.766507", "0.146287", "-0.353369", "0.519845", "-1.206463"],
      ["3", "5", "Elcent", "0.200", "I[10]", "11.636477", "-6.609388", "0.440853", "-1.620535", "3.932866", "-7.363094"],
      ["4", "5", "Elcent", "0.200", "J[34]", "11.636477", "-6.609388", "0.440853", "-1.620535", "3.712440", "-4.058400"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取梁单元5号 I/J 截面的构件内力时程 ────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_BEAMFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [5]},
        "PARTS": ["PartI", "PartJ"],            # 单元结果输出位置
        "TH_CASE_NAME": ["Elcent"],
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
for row in res["TH_BEAMFORCE"]["DATA"]:
    print(f"  elem {row[1]} {row[4]} t={row[3]}  Axial={row[5]}  My={row[9]}")
```

---

### A-3. Time History Text – Element Result(Plate)

> **功能：** 提取时程分析中**平板(Plate)**单元的构件内力·单位构件内力·应力。

#### `TEXT_TYPE` 及 Response HEAD

| `TEXT_TYPE` | 说明 | Response `HEAD` |
|-------------|------|-----------------|
| `"TH_PLATEFORCE"` | 板构件内力 | `["Index", "Elem", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"TH_PLATE_UNIT_FORCE"` | 板单位构件内力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Fxx", "Fyy", "Fxy", "Mxx", "Myy", "Mxy", "Vxx", "Vyy"]` |
| `"TH_PLATESTRESS"` | 板应力 | `["Index", "Elem", "Load", "Time/Step", "Part", "Sig-xx(Top)", "Sig-yy(Top)", "Sig-xy(Top)", "Sig-xx(Bot)", "Sig-yy(Bot)", "Sig-xy(Bot)"]` |

#### Request / Response JSON

**POST Request Body — 板构件内力(TH_PLATEFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_PLATEFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_PlateForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [51] },
    "PARTS": ["PartI", "PartJ", "PartK", "PartL"],
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.3, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "TH_PLATEFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "51", "Elcent", "0.100", "I", "0.383964", "1.085381", "-0.000122", "-0.000976", "0.000148", "0.000000"],
      ["2", "51", "Elcent", "0.100", "J", "0.376184", "-0.912407", "-0.000206", "-0.000988", "-0.000230", "0.000000"],
      ["3", "51", "Elcent", "0.100", "K", "-0.356719", "-0.607889", "0.000128", "-0.000000", "-0.000092", "0.000000"],
      ["4", "51", "Elcent", "0.100", "L", "-0.403429", "0.434915", "0.000200", "-0.000000", "-0.000059", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取板单元51号的4节点(I,J,K,L)板应力时程 ───────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_PLATESTRESS",          # 板应力
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 4},
        "NODE_ELEMS": {"KEYS": [51]},
        "PARTS": ["PartI", "PartJ", "PartK", "PartL"],
        "TH_CASE_NAME": ["Elcent"],
        "STEP": {"FROM": 0.1, "TO": 0.3, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["TH_PLATESTRESS"]["HEAD"])
print("rows:", len(res["TH_PLATESTRESS"]["DATA"]))
```

---

### A-4. Time History Text – Element Result(Wall)

> **功能：** 提取时程分析中**墙体(Wall)**单元的构件内力。

#### `TEXT_TYPE`

| 值 | 说明 |
|----|------|
| `"TH_WALLFORCE"` | 墙体构件内力 |

#### Response HEAD

`["Index", "WallID", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

> ⚠️ 2026-08-26 确认（article id `36705611314585`）：官方文章的 Request/Response 示例
> 配对的值互不一致（请求为 `NODE_ELEMS.KEYS: [466]`·`STEP.TO: 0.2`·`PLACE: 6`，
> 但响应 `DATA` 是 `WallID "12"`·3位指数（例：`-4.386e+02`）的值）。本仓库按响应的
> 实际值把请求示例调整为内部一致（KEYS `[12]`、STEP.TO `0.18`、PLACE `3`）——
> 若原样全文转载官方原文，就会成为请求与响应互不匹配的示例。

#### Request / Response JSON

**POST Request Body — 墙体构件内力(TH_WALLFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_WALLFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_WallForce_Out.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "M" },
    "STYLES": { "FORMAT": "Exponential", "PLACE": 3 },
    "COMPONENTS": ["WallID", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [12] },
    "PARTS": ["PartI", "PartJ"],
    "TH_CASE_NAME": ["EQ1"],
    "STEP": { "FROM": 0.1, "TO": 0.18, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "TH_WALLFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "WallID", "Load", "Time/Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "12", "EQ1", "0.100", "I[308]", "-4.386e+02", "0.000e+00", "6.012e+00", "0.000e+00", "1.492e+02", "0.000e+00"],
      ["2", "12", "EQ1", "0.100", "J[314]", "-4.386e+02", "0.000e+00", "6.012e+00", "0.000e+00", "1.323e+02", "0.000e+00"],
      ["3", "12", "EQ1", "0.120", "I[308]", "-4.381e+02", "0.000e+00", "6.313e+00", "0.000e+00", "1.491e+02", "0.000e+00"],
      ["4", "12", "EQ1", "0.120", "J[314]", "-4.381e+02", "0.000e+00", "6.313e+00", "0.000e+00", "1.314e+02", "0.000e+00"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 以指数(Exponential)格式提取墙体12号的构件内力时程 ──────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_WALLFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "M"},
        "STYLES": {"FORMAT": "Exponential", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [12]},
        "PARTS": ["PartI", "PartJ"],
        "TH_CASE_NAME": ["EQ1"],
        "STEP": {"FROM": 0.1, "TO": 0.18, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
for row in res["TH_WALLFORCE"]["DATA"]:
    print(f"  Wall {row[1]} {row[4]} t={row[3]}  Axial={row[5]}")
```

---

### A-5. Time History Text – General Link Result

> **功能：** 提取时程分析中**一般连接(General Link)**的构件内力和变形。

#### `TEXT_TYPE` 及 Response HEAD

| `TEXT_TYPE` | 说明 | Response `HEAD` |
|-------------|------|-----------------|
| `"TH_GLINKFORCE"` | 一般连接构件内力 | `["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"TH_GLINKDEFORM"` | 一般连接变形 | `["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "DX", "DY", "DZ", "RX", "RY", "RZ"]` |

#### Request / Response JSON

> ⚠️ 2026-08-26 确认（article id `36705822943257`）：旧版本把 `TH_GLINKDEFORM` 请求与
> `TH_GLINKFORCE` 响应配成了一对，请求与响应属于不同的 `TEXT_TYPE`（我方撰稿失误）。已按官方示例
> 为准，把两个 `TEXT_TYPE` 各自的请求·响应正确配对补全。

**POST Request Body — 一般连接变形(TH_GLINKDEFORM)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_GLINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_GlinkDeform_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Time/Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.5, "STEPS": 1 }
  }
}
```

**POST Response Body — 一般连接变形(TH_GLINKDEFORM)**

```json
{
  "TH_GLINKDEFORM": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "18", "10", "Elcent", "0.100", "-0.366319", "0.249123", "-0.138251", "0.000003", "-0.000004", "-0.000018"],
      ["2", "1", "18", "10", "Elcent", "0.200", "-1.862090", "1.407943", "-0.515132", "0.000043", "-0.000107", "-0.000011"]
    ]
  }
}
```

**POST Request Body — 一般连接构件内力(TH_GLINKFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "TH_GLINKFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\TH_GlinkForce_Out.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "PARTS": ["PartI", "PartJ"],
    "TH_CASE_NAME": ["Elcent"],
    "STEP": { "FROM": 0.1, "TO": 0.3, "STEPS": 1 }
  }
}
```

**POST Response Body — 一般连接构件内力(TH_GLINKFORCE)**

```json
{
  "TH_GLINKFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Time/Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "1", "18", "10", "Elcent", "0.100", "I", "-1.216319", "1.099123", "-0.941257", "0.274092", "-0.408692", "-1.029260"],
      ["2", "1", "18", "10", "Elcent", "0.100", "J", "-1.216319", "1.099123", "-0.941257", "0.274092", "-0.408692", "-1.029260"],
      ["3", "1", "18", "10", "Elcent", "0.200", "I", "-2.712090", "2.257943", "-1.365132", "1.280736", "-1.921911", "-0.327463"],
      ["4", "1", "18", "10", "Elcent", "0.200", "J", "-2.712090", "2.257943", "-1.365132", "1.280736", "-1.921911", "-0.327463"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取一般连接1号的变形时程 ─────────────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "TH_GLINKDEFORM",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "TH_CASE_NAME": ["Elcent"],
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
tbl = res["TH_GLINKDEFORM"]
print("HEAD:", tbl["HEAD"])
```

---

### A-6. Pushover Text – Displacement

> **功能：** 在推覆(Pushover)分析中按步提取节点的位移。荷载工况用 `PO_CASE_NAME` 指定。

#### `TEXT_TYPE`

| 值 | 说明 |
|----|------|
| `"PO_DISP"` | 推覆位移(Displacement) |

#### Response HEAD

`["Index", "Node", "Load", "Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"]`

#### Request / Response JSON

**POST Request Body — 推覆位移(PO_DISP)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_DISP",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_Displacement_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Node", "Load", "Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "NODE_ELEMS": { "KEYS": [22] },
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 10, "STEPS": 1 },
    "REF_PT": "Ground"
  }
}
```

**POST Response Body**

```json
{
  "PO_DISP": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Node", "Load", "Step", "Dx", "Dy", "Dz", "Rx", "Ry", "Rz"],
    "DATA": [
      ["1", "22", "PX", "1", "-4.986447", "0.000000", "-0.017857", "0.000000", "0.000403", "0.000000"],
      ["2", "22", "PX", "2", "-9.972893", "0.000000", "-0.035714", "0.000000", "0.000806", "0.000000"],
      ["3", "22", "PX", "3", "-14.959340", "0.000000", "-0.053572", "0.000000", "0.001210", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 在步1~10提取节点22号(控制点)的推覆位移曲线 ────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_DISP",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [22]},
        "PO_CASE_NAME": ["PX"],                 # 推覆荷载工况
        "STEP": {"FROM": 1, "TO": 10, "STEPS": 1},
        "REF_PT": "Ground",
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
for row in res["PO_DISP"]["DATA"]:
    print(f"  step {row[3]}  Dx={row[4]}")
```

---

### A-7. Pushover Text – Element Result(Beam, Truss)

> **功能：** 按步提取推覆分析中**梁·桁架**单元的构件内力/应力。

#### `TEXT_TYPE` 及 Response HEAD

| `TEXT_TYPE` | 说明 | Response `HEAD` |
|-------------|------|-----------------|
| `"PO_BEAMFORCE"` | 梁构件内力 | `["Index", "Elem", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]` |
| `"PO_BEAMSTRESS"` | 梁应力 | `["Index", "Elem", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z"]` |
| `"PO_TRUSSFORCE"` | 桁架构件内力 | `["Index", "Elem", "Load", "Force-I", "Force-J"]` |
| `"PO_TRUSSSTRESS"` | 桁架应力 | `["Index", "Elem", "Load", "Step", "Stress-I", "Stress-J"]` |

#### Request / Response JSON

> ⚠️ 2026-08-26 确认（article id `36706062373657`）：旧版本把 `PO_BEAMFORCE` 请求与
> `PO_TRUSSFORCE` 响应配成了一对，而且该响应的 `DATA` 也不是实际值，而是
> `12.345678`/`24.691356` 之类随意凑出的位数填充值（我方撰稿失误）。已用官方示例的
> 实际值把两个 `TEXT_TYPE` 正确配对替换。

**POST Request Body — 梁构件内力(PO_BEAMFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_BEAMFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_BeamForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Part", "Step", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [16] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 5, "STEPS": 1 }
  }
}
```

**POST Response Body — 梁构件内力(PO_BEAMFORCE)**

```json
{
  "PO_BEAMFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "16", "PX", "1", "I[19]", "270.506367", "0.000000", "13.449733", "0.000000", "27.545039", "0.000000"],
      ["2", "16", "PX", "1", "J[22]", "270.506367", "0.000000", "14.095306", "0.000000", "0.000000", "0.000000"]
    ]
  }
}
```

**POST Request Body — 桁架构件内力(PO_TRUSSFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_TRUSSFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_TrussForce_Out.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Elem", "Load", "Time/Step", "Force-I", "Force-J"],
    "NODE_ELEMS": { "KEYS": [18] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 10, "STEPS": 1 }
  }
}
```

**POST Response Body — 桁架构件内力(PO_TRUSSFORCE)**

```json
{
  "PO_TRUSSFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Force-I", "Force-J"],
    "DATA": [
      ["1", "18", "PX", "-273.752455", "-273.752455"],
      ["2", "18", "PX", "-546.467417", "-546.467417"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 在步1~5提取梁单元16号的推覆构件内力 ─────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_BEAMFORCE",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [16]},
        "PARTS": ["PartI", "PartJ"],
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("rows:", len(res["PO_BEAMFORCE"]["DATA"]))
```

---

### A-8. Pushover Text – Element Result(Wall)

> **功能：** 按步提取推覆分析中**墙体(Wall)**单元的构件内力。

#### `TEXT_TYPE`

| 值 | 说明 |
|----|------|
| `"PO_WALLFORCE"` | 墙体构件内力 |

#### Response HEAD

`["Index", "WallID", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"]`

> ⚠️ 2026-08-26 确认（article id `36706217576217`）：与 [A-4](#a-4-time-history-text--element-resultwall)
> 同类型的官方原文自身矛盾 —— 请求示例为 `NODE_ELEMS.KEYS: [466]`·`STEP.TO: 5`，但响应
> `DATA` 是 `WallID "12"` 的值。本仓库已按响应值把请求调整为内部一致。

#### Request / Response JSON

**POST Request Body — 墙体构件内力(PO_WALLFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_WALLFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_WallForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Exponential", "PLACE": 3 },
    "COMPONENTS": ["WallID", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "NODE_ELEMS": { "KEYS": [12] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 4, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "PO_WALLFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "WallID", "Load", "Step", "Part", "Axial", "Shear-y", "Shear-z", "Torsion", "Moment-y", "Moment-z"],
    "DATA": [
      ["1", "12", "PX", "1", "I[308]", "-2.045e+02", "0.000e+00", "6.953e+01", "0.000e+00", "-6.679e+01", "0.000e+00"],
      ["2", "12", "PX", "1", "J[314]", "-2.045e+02", "0.000e+00", "6.953e+01", "0.000e+00", "1.279e+02", "0.000e+00"],
      ["3", "12", "PX", "2", "I[308]", "-5.294e+01", "0.000e+00", "1.152e+02", "0.000e+00", "-1.675e+02", "0.000e+00"],
      ["4", "12", "PX", "2", "J[314]", "-5.294e+01", "0.000e+00", "1.152e+02", "0.000e+00", "1.551e+02", "0.000e+00"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取墙体12号的推覆构件内力 ──────────────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_WALLFORCE",
        "UNIT": {"FORCE": "KN", "DIST": "M"},
        "STYLES": {"FORMAT": "Exponential", "PLACE": 3},
        "NODE_ELEMS": {"KEYS": [12]},
        "PARTS": ["PartI", "PartJ"],
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 4, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["PO_WALLFORCE"]["HEAD"])
```

---

### A-9. Pushover Text – General Link

> **功能：** 按步提取推覆分析中**一般连接(General Link)**的构件内力·变形。

#### `TEXT_TYPE` 及 Response HEAD

| `TEXT_TYPE` | 说明 | Response `HEAD` |
|-------------|------|-----------------|
| `"PO_GLINKFORCE"` | 一般连接构件内力 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"PO_GLINKDEFORM"` | 一般连接变形 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"]` |

#### Request / Response JSON

**POST Request Body — 一般连接变形(PO_GLINKDEFORM)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_GLINKDEFORM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_GlinkDeform_Out.JSON",
    "UNIT": { "FORCE": "N", "DIST": "MM" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 5, "STEPS": 1 }
  }
}
```

**POST Response Body**

> ⚠️ 2026-08-26 确认（article id `36706344369049`）：旧版本的 `DATA` 值并非实际响应，而是
> `-0.010000`/`-0.020000` 等随意填充值（我方撰稿失误，`Node1`/`Node2` 也未记为实际的
> `20`/`22` 而误写为 `18`/`10`）。已用官方示例的实际值替换。

```json
{
  "PO_GLINKDEFORM": {
    "FORCE": "N",
    "DIST": "mm",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"],
    "DATA": [
      ["1", "1", "20", "22", "PX", "1", "0.013553", "0.000000", "-0.008622", "0.000000", "-0.000407", "0.000000"],
      ["2", "1", "20", "22", "PX", "2", "0.027107", "0.000000", "-0.017094", "0.000000", "-0.000810", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 按步提取一般连接1号的推覆构件内力 ────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_GLINKFORCE",
        "UNIT": {"FORCE": "kN", "DIST": "M"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["PO_GLINKFORCE"]["HEAD"])
```

---

### A-10. Pushover Text – Elastic Link

> **功能：** 按步提取推覆分析中**弹性连接(Elastic Link)**的构件内力·变形。

#### `TEXT_TYPE` 及 Response HEAD

| `TEXT_TYPE` | 说明 | Response `HEAD` |
|-------------|------|-----------------|
| `"PO_ELINKFORCE"` | 弹性连接构件内力 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"]` |
| `"PO_ELINKDEFORM"` | 弹性连接变形 | `["Index", "Key", "Node1", "Node2", "Load", "Step", "DX", "DY", "DZ", "RX", "RY", "RZ"]` |

#### Request / Response JSON

**POST Request Body — 弹性连接构件内力(PO_ELINKFORCE)**

```json
{
  "Argument": {
    "TEXT_TYPE": "PO_ELINKFORCE",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\PO_ElinkForce_Out.JSON",
    "UNIT": { "FORCE": "KN", "DIST": "M" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 6 },
    "COMPONENTS": ["Key", "Node1", "Node2", "Load", "Part", "Step", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "NODE_ELEMS": { "KEYS": [1] },
    "PARTS": ["PartI", "PartJ"],
    "PO_CASE_NAME": ["PX"],
    "STEP": { "FROM": 1, "TO": 5, "STEPS": 1 }
  }
}
```

**POST Response Body**

```json
{
  "PO_ELINKFORCE": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Key", "Node1", "Node2", "Load", "Step", "Part", "FX", "FY", "FZ", "MX", "MY", "MZ"],
    "DATA": [
      ["1", "1", "16", "4", "PX", "1", "I", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"],
      ["2", "1", "16", "4", "PX", "1", "J", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"],
      ["3", "1", "16", "4", "PX", "2", "I", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"],
      ["4", "1", "16", "4", "PX", "2", "J", "0.000000", "0.000060", "0.000547", "-0.063083", "0.000000", "0.000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取弹性连接1号的推覆变形 ────────────────────────────────
payload = {
    "Argument": {
        "TEXT_TYPE": "PO_ELINKDEFORM",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [1]},
        "PO_CASE_NAME": ["PX"],
        "STEP": {"FROM": 1, "TO": 5, "STEPS": 1},
    }
}
res = requests.post(f"{BASE_URL}/post/TEXT", json=payload, headers=HEADERS).json()
print("HEAD:", res["PO_ELINKDEFORM"]["HEAD"])
```

---

## B 组. Inelastic Hinge 时程结果表格 (`post/TABLE`)

以表格形式提取非弹性铰(Inelastic Hinge)的时程结果。本组**与第19章的 `post/TABLE` 公共结构相同**，在 `"Argument"` 对象中用 `TABLE_TYPE` 选择表格种类。

### Input URI（B 组公共）

```
{base url}/post/TABLE
```

### Active Methods

`POST`

### 公共 Request 结构（与第19章公共部分相同）

与第19章一样，使用 `TABLE_NAME`·`TABLE_TYPE`·`EXPORT_PATH`·`UNIT`(FORCE/DIST)·`STYLES`(FORMAT/PLACE)·`COMPONENTS`·`NODE_ELEMS`(KEYS/TO/STRUCTURE_GROUP_NAME)。只有荷载工况使用专用的时程键，这一点不同。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 结果表格标题 | `"TABLE_NAME"` | String | Empty | Optional |
| 2 | 结果表格类型（各节参照） | `"TABLE_TYPE"` | String | — | **Required** |
| 3 | 保存路径 | `"EXPORT_PATH"` | String | — | Optional |
| 4 | 单位 (`FORCE`/`DIST`) | `"UNIT"` | Object | System | Optional |
| 5 | 数字格式 (`FORMAT`/`PLACE`) | `"STYLES"` | Object | System | Optional |
| 6 | 显示列 | `"COMPONENTS"` | Array [String] | All | Optional |
| 7 | 单元指定 (`KEYS`/`TO`/`STRUCTURE_GROUP_NAME`) | `"NODE_ELEMS"` | Object | All | Optional |
| 8 | **时程荷载工况名** | `"TH_LOAD_CASE_NAMES"` | Array [String] | All | Optional |

> **`TH_LOAD_CASE_NAMES` 后缀规则：** 使用 `NAME(all)`(全部步)、`NAME(TH:max)`(最大包络)、`NAME(TH:min)`(最小包络)、`NAME(max)` / `NAME(min)` 等形式。

### `TABLE_TYPE` 后缀(铰类型)的公共含义

| 后缀 | 含义 |
|--------|------|
| `LUMPED` | 集中型(Lumped)铰 |
| `DIST` | 分布型(Distributed)铰 |
| `SPRING` | 弹簧(Spring)铰 |
| `TRUSS` | 桁架(Truss)铰 |
| `WALL` | 墙体(Wall)铰 |

### 公共 Response 结构

```json
{
  "<TABLE_NAME>": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "..."],
    "DATA": [["1", "..."]]
  }
}
```

---

### B-1. Inelastic Hinge Event Time

> **功能：** 按6个分量(Dx~Rz)提取非弹性铰的**一/二/三次屈服发生时刻(Event Time)**。

#### `TABLE_TYPE`

| 值 | 铰类型 |
|----|-----------|
| `"IEHG_EVENT_TIME_LUMPED"` | 集中型 |
| `"IEHG_EVENT_TIME_DIST"` | 分布型 |
| `"IEHG_EVENT_TIME_SPRING"` | 弹簧 |
| `"IEHG_EVENT_TIME_TRUSS"` | 桁架 |
| `"IEHG_EVENT_TIME_WALL"` | 墙体 |

#### Response HEAD（按铰类型）

- **Lumped / Dist / Spring：** `["Index", "Elem", "HingeLocation", "Load", "1stYield/Dx", "1stYield/Dy", "1stYield/Dz", "1stYield/Rx", "1stYield/Ry", "1stYield/Rz", "2ndYield/Dx", "2ndYield/Dy", "2ndYield/Dz", "2ndYield/Rx", "2ndYield/Ry", "2ndYield/Rz", "3rdYield/Dx", "3rdYield/Dy", "3rdYield/Dz", "3rdYield/Rx", "3rdYield/Ry", "3rdYield/Rz"]`
- **Truss：** `["Index", "Elem", "InelasticHingeProp.", "Load", "1stYield/Dx", "2ndYield/Dx", "3rdYield/Dx"]`
- **Wall：** `["Index", "WallID", "Story", "HingeLocation", "Load", "1stYield/Dx", ... , "3rdYield/Rz"]` （在 Lumped 列之前追加 `Story`·`WallID`）
- **一般连接分量(Spring 系列)：** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "1stYield/Dx", ... , "3rdYield/Rz"]`

#### Request / Response JSON

**POST Request Body — 集中型(IEHG_EVENT_TIME_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_EVENT_TIME_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": [
      "Elem", "HingeLocation", "Load",
      "1stYield/Dx", "1stYield/Dy", "1stYield/Dz", "1stYield/Rx", "1stYield/Ry", "1stYield/Rz",
      "2ndYield/Dx", "2ndYield/Dy", "2ndYield/Dz", "2ndYield/Rx", "2ndYield/Ry", "2ndYield/Rz",
      "3rdYield/Dx", "3rdYield/Dy", "3rdYield/Dz", "3rdYield/Rx", "3rdYield/Ry", "3rdYield/Rz"
    ],
    "TH_LOAD_CASE_NAMES": ["Elcent"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "Load", "1stYield/Dx", "1stYield/Dy", "1stYield/Dz", "1stYield/Rx", "1stYield/Ry", "1stYield/Rz", "2ndYield/Dx", "2ndYield/Dy", "2ndYield/Dz", "2ndYield/Rx", "2ndYield/Ry", "2ndYield/Rz", "3rdYield/Dx", "3rdYield/Dy", "3rdYield/Dz", "3rdYield/Rx", "3rdYield/Ry", "3rdYield/Rz"],
    "DATA": [
      ["1", "3", "Center", "Elcent(all)", "1.100000023842", "-", "-", "-", "-", "-", "1.100000023842", "-", "-", "-", "-", "-", "0.000000000000", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Elcent(all)", "-", "0.100000001490", "0.100000001490", "-", "0.300000011921", "0.300000011921", "-", "0.100000001490", "0.100000001490", "-", "0.500000000000", "0.500000000000", "-", "0.000000000000", "0.000000000000", "-", "0.000000000000", "0.000000000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取集中型铰的屈服事件时刻表格 ────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_EVENT_TIME_LUMPED",  # 集中型铰
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 12},
        "TH_LOAD_CASE_NAMES": ["Elcent"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
tbl = res["Lumped"]
print("HEAD 列数:", len(tbl["HEAD"]), "/ DATA 行数:", len(tbl["DATA"]))
```

---

### B-2. Inelastic Hinge Beam Summary

> **功能：** 提取非弹性梁(Beam)铰的**按分量(Dx/Dy/Dz/Ry/Rz)汇总**。在一个表格中同时提供变形·构件内力·延性·状态(Status)·性能(Performance)。

#### `TABLE_TYPE`

| 值 | 分量 |
|----|------|
| `"IEHG_BEAM_SUM_DX"` | Dx |
| `"IEHG_BEAM_SUM_DY"` | Dy |
| `"IEHG_BEAM_SUM_DZ"` | Dz |
| `"IEHG_BEAM_SUM_RY"` | Ry |
| `"IEHG_BEAM_SUM_RZ"` | Rz |

#### Response HEAD

`["Index", "Type", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"]`

#### Request / Response JSON

**POST Request Body — Dx 分量(IEHG_BEAM_SUM_DX)**

```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_BEAM_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Type", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "NODE_ELEMS": { "KEYS": [2, 3] },
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Dx": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Type", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "DATA": [
      ["1", "Distributed", "2", "1-Pos", "Column-1", "Elcent(max)", "3.099999904633", "0.004527841229", "3173.563500000000", "36.361083984375", "25.025245666504", "2ndYield", "5~Level", "672.750118000000", "825.120000000000", "-", "0.000124524377", "0.000180930947", "-"],
      ["2", "Lumped", "3", "Center", "Column", "Elcent(max)", "3.099999904633", "0.004969955422", "3412.418000000000", "39.911506652832", "27.468795776367", "2ndYield", "5~Level", "672.750118000000", "825.120000000000", "-", "0.000124524377", "0.000180930947", "-"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取梁铰单元2,3号的 Dx 汇总(包络 max/min) ─────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Dx",
        "TABLE_TYPE": "IEHG_BEAM_SUM_DX",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 12},
        "NODE_ELEMS": {"KEYS": [2, 3]},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
for row in res["Dx"]["DATA"]:
    # Status=第11列，Performance=第12列
    print(f"  elem {row[2]} {row[3]}: {row[11]} / {row[12]}")
```

---

### B-3. Inelastic Hinge Truss Summary

> **功能：** 提取非弹性桁架(Truss)铰的汇总(Dx)。

#### `TABLE_TYPE`

| 值 | 分量 |
|----|------|
| `"IEHG_TRUSS_SUM_DX"` | Dx |

#### Response HEAD

`["Index", "Truss/Elem", "Truss/Node1", "Truss/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"]`

#### Request / Response JSON

**POST Request Body — Dx(IEHG_TRUSS_SUM_DX)**

```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_TRUSS_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Truss/Elem", "Truss/Node1", "Truss/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "NODE_ELEMS": { "KEYS": [49] },
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Dx": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Truss/Elem", "Truss/Node1", "Truss/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "DATA": [
      ["1", "49", "54", "57", "Truss", "Elcent(min)", "1.799999952316", "-0.000726116123", "-841.719187500000", "0.123781532049", "0.123781532049", "Elastic", "0~1Level", "-0.500000000000", "-1.000000000000", "-", "-0.005866110325", "-0.005866110325", "-"],
      ["2", "49", "54", "57", "Truss", "Elcent(max)", "2.099999904633", "0.001163915265", "832.173000000000", "1.557814478874", "1.072154164314", "2ndYield", "2~3Level", "0.500000000000", "1.000000000000", "-", "0.000747146260", "0.001085585682", "-"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取桁架铰49号的 Dx 汇总 ────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Dx",
        "TABLE_TYPE": "IEHG_TRUSS_SUM_DX",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "NODE_ELEMS": {"KEYS": [49]},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("rows:", len(res["Dx"]["DATA"]))
```

---

### B-4. Inelastic Hinge General Link Summary

> **功能：** 提取非弹性一般连接(General Link)铰的按分量(Dx/Dy/Dz/Rx/Ry/Rz)汇总。

#### `TABLE_TYPE`

| 值 | 分量 |
|----|------|
| `"IEHG_GL_LINK_SUM_DX"` | Dx |
| `"IEHG_GL_LINK_SUM_DY"` | Dy |
| `"IEHG_GL_LINK_SUM_DZ"` | Dz |
| `"IEHG_GL_LINK_SUM_RX"` | Rx |
| `"IEHG_GL_LINK_SUM_RY"` | Ry |
| `"IEHG_GL_LINK_SUM_RZ"` | Rz |

#### Response HEAD

`["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"]`

#### Request / Response JSON

**POST Request Body — Dx(IEHG_GL_LINK_SUM_DX)**

```json
{
  "Argument": {
    "TABLE_NAME": "Dx",
    "TABLE_TYPE": "IEHG_GL_LINK_SUM_DX",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Dx": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Time/Step", "Deform", "Force", "max(D/D1)", "max(D/D2)", "Status", "Performance", "P1", "P2", "P3", "D1", "D2", "D3"],
    "DATA": [
      ["1", "1", "GL_1", "18", "10", "GeneralLink", "Elcent(min)", "2.000000000000", "-0.669099271297", "-669.949250000000", "13381.985351562500", "4460.661621093750", "2ndYield", "3~4Level", "-0.500000000000", "-1.000000000000", "-", "-0.000049999999", "-0.000150000007", "-"],
      ["2", "1", "GL_1", "18", "10", "GeneralLink", "Elcent(max)", "2.400000095367", "0.500326693058", "499.476687500000", "10006.534179687500", "3335.511230468750", "2ndYield", "5~Level", "0.500000000000", "1.000000000000", "-", "0.000049999999", "0.000150000007", "-"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取一般连接铰的 Dx 汇总(包络) ──────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Dx",
        "TABLE_TYPE": "IEHG_GL_LINK_SUM_DX",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("HEAD:", res["Dx"]["HEAD"])
```

---

### B-5. Inelastic Hinge Force

> **功能：** 按6个分量(Fx~Mz)提取非弹性铰的**最大构件内力(Force)与发生时刻(Time)**。

#### `TABLE_TYPE`

| 值 | 铰类型 |
|----|-----------|
| `"IEHG_FORCE_LUMPED"` | 集中型 |
| `"IEHG_FORCE_DIST"` | 分布型 |
| `"IEHG_FORCE_SPRING"` | 弹簧 |
| `"IEHG_FORCE_TRUSS"` | 桁架 |
| `"IEHG_FORCE_WALL"` | 墙体 |

#### Response HEAD（按铰类型）

> ⚠️ 2026-08-26 确认（article id `36020436094105`）：旧版本下面 Truss/Spring 两个 HEAD 的
> 标签互换了（我方撰稿失误）—— 只带单个 `Fx` 分量的一方实际是 Truss，
> 带 `GeneralLink/*` 字段的一方实际是 Spring（一般连接铰）。

- **Lumped / Dist：** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", "Fy/Force", "Fy/Time", "Fz/Force", "Fz/Time", "Mx/Force", "Mx/Time", "My/Force", "My/Time", "Mz/Force", "Mz/Time"]`
- **Truss：** `["Index", "Elem", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time"]`
- **Wall：** `["Index", "WallID", "Story", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", ... , "Mz/Force", "Mz/Time"]`
- **Spring：** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", ... , "Mz/Force", "Mz/Time"]`

#### Request / Response JSON

**POST Request Body — 集中型(IEHG_FORCE_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_FORCE_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", "Fy/Force", "Fy/Time", "Fz/Force", "Fz/Time", "Mx/Force", "Mx/Time", "My/Force", "My/Time", "Mz/Force", "Mz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Fx/Force", "Fx/Time", "Fy/Force", "Fy/Time", "Fz/Force", "Fz/Time", "Mx/Force", "Mx/Time", "My/Force", "My/Time", "Mz/Force", "Mz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "3412.418000000000", "3.099999904633", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "750.083437500000", "3.200000047684", "902.629812500000", "2.599999904633", "-", "-", "2828.398250000000", "2.599999904633", "3067.439000000000", "2.099999904633"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取集中型铰的最大构件内力/发生时刻表格 ────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_FORCE_LUMPED",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("rows:", len(res["Lumped"]["DATA"]))
```

---

### B-6. Inelastic Hinge Deformation

> **功能：** 按6个分量(Dx~Rz)提取非弹性铰的**最大变形(Deform)与发生时刻(Time)**。

#### `TABLE_TYPE`

| 值 | 铰类型 |
|----|-----------|
| `"IEHG_DEFORM_LUMPED"` | 集中型 |
| `"IEHG_DEFORM_DIST"` | 分布型 |
| `"IEHG_DEFORM_SPRING"` | 弹簧 |
| `"IEHG_DEFORM_TRUSS"` | 桁架 |
| `"IEHG_DEFORM_WALL"` | 墙体 |

#### Response HEAD（按铰类型）

> ⚠️ 2026-08-26 确认（article id `36020548520601`）：与 [B-5](#b-5-inelastic-hinge-force) 一样，
> Truss/Spring 标签在旧版本中互换了 —— 更正。

- **Lumped / Dist：** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", "Dy/Deform", "Dy/Time", "Dz/Deform", "Dz/Time", "Rx/Deform", "Rx/Time", "Ry/Deform", "Ry/Time", "Rz/Deform", "Rz/Time"]`
- **Truss：** `["Index", "Elem", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time"]`
- **Wall：** `["Index", "WallID", "Story", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", ... , "Rz/Deform", "Rz/Time"]`
- **Spring：** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", ... , "Rz/Deform", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 集中型(IEHG_DEFORM_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DEFORM_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", "Dy/Deform", "Dy/Time", "Dz/Deform", "Dz/Time", "Rx/Deform", "Rx/Time", "Ry/Deform", "Ry/Time", "Rz/Deform", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/Deform", "Dx/Time", "Dy/Deform", "Dy/Time", "Dz/Deform", "Dz/Time", "Rx/Deform", "Rx/Time", "Ry/Deform", "Ry/Time", "Rz/Deform", "Rz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "0.004969955422", "3.099999904633", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "0.003640656127", "3.200000047684", "0.004381065723", "2.599999904633", "-", "-", "0.053212597966", "2.599999904633", "0.057932153344", "2.099999904633"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取分布型铰的变形表格 ───────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Distributed",
        "TABLE_TYPE": "IEHG_DEFORM_DIST",     # 分布型
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
key = next(iter(res))
print("table:", key, "/ rows:", len(res[key]["DATA"]))
```

---

### B-7. Inelastic Hinge Element Rotation

> **功能：** 以 Ry·Rz 分量提取非弹性铰单元的**旋转(Rotation)与发生时刻(Time)**。分为梁和墙体两种类型。

#### `TABLE_TYPE`

| 值 | 类型 |
|----|------|
| `"IEHG_ELEM_ROT_BEAM"` | 梁(Beam)单元旋转 |
| `"IEHG_ELEM_ROT_WALL"` | 墙体(Wall)单元旋转 |

#### Response HEAD（按类型）

- **Beam：** `["Index", "Elem", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"]`
- **Wall：** `["Index", "Story", "WallID", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 梁(IEHG_ELEM_ROT_BEAM)**

```json
{
  "Argument": {
    "TABLE_NAME": "Beam",
    "TABLE_TYPE": "IEHG_ELEM_ROT_BEAM",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Beam": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "Load", "Part", "Ry/Rotation", "Ry/Time", "Rz/Rotation", "Rz/Time"],
    "DATA": [
      ["1", "2", "Elcent(max)", "I", "0.074839800000", "2.600000000000", "0.096699700000", "3.200000000000"],
      ["2", "2", "Elcent(max)", "J", "0.056081600000", "2.600000000000", "0.080104800000", "3.200000000000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取梁单元的塑性转角(Ry/Rz)与发生时刻 ────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Beam",
        "TABLE_TYPE": "IEHG_ELEM_ROT_BEAM",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
for row in res["Beam"]["DATA"]:
    print(f"  elem {row[1]} {row[3]}  Ry={row[4]} (t={row[5]})  Rz={row[6]} (t={row[7]})")
```

---

### B-8. Inelastic Hinge Ductility Factor(D/D1)

> **功能：** 按6个分量提取非弹性铰的**延性系数 D/D1**（相对于一次屈服）的最大值与发生时刻。

#### `TABLE_TYPE`

| 值 | 铰类型 |
|----|-----------|
| `"IEHG_DUCT_D1_LUMPED"` | 集中型 |
| `"IEHG_DUCT_D1_DIST"` | 分布型 |
| `"IEHG_DUCT_D1_SPRING"` | 弹簧 |
| `"IEHG_DUCT_D1_TRUSS"` | 桁架 |
| `"IEHG_DUCT_D1_WALL"` | 墙体 |

#### Response HEAD（按铰类型）

> ⚠️ 2026-08-26 确认（article id `36020795064089`）：与 [B-5](#b-5-inelastic-hinge-force) 一样，
> Truss/Spring 标签在旧版本中互换了 —— 更正。

- **Lumped：** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"]`
- **Dist：** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max(D/D1)", "Dx/Time", "Dy/max(D/D1)", "Dy/Time", "Dz/max(D/D1)", "Dz/Time", "Rx/max(D/D1)", "Rx/Time", "Ry/max(D/D1)", "Ry/Time", "Rz/max(D/D1)", "Rz/Time"]`
- **Truss：** `["Index", "Elem", "InelasticHingeProp.", "Load", "Dx/max(D/D1)", "Dx/Time"]`
- **Wall：** `["Index", "WallID", "Story", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", ... , "Rz/max", "Rz/Time"]`
- **Spring：** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Dx/max(D/D1)", "Dx/Time", ... , "Rz/max(D/D1)", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 集中型(IEHG_DUCT_D1_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DUCT_D1_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "53.748348", "3.100000", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "16.149096", "3.200000", "20.864525", "2.700000", "-", "-", "609.587769", "2.600000", "663.790100", "3.200000"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取集中型铰延性 D/D1 表格 ──────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_DUCT_D1_LUMPED",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
print("HEAD:", res["Lumped"]["HEAD"])
```

---

### B-9. Inelastic Hinge Ductility Factor(D/D2)

> **功能：** 按6个分量提取非弹性铰的**延性系数 D/D2**（相对于二次屈服）的最大值与发生时刻。

#### `TABLE_TYPE`

| 值 | 铰类型 |
|----|-----------|
| `"IEHG_DUCT_D2_LUMPED"` | 集中型 |
| `"IEHG_DUCT_D2_DIST"` | 分布型 |
| `"IEHG_DUCT_D2_SPRING"` | 弹簧 |
| `"IEHG_DUCT_D2_TRUSS"` | 桁架 |
| `"IEHG_DUCT_D2_WALL"` | 墙体 |

#### Response HEAD（按铰类型）

> ⚠️ 2026-08-26 确认（article id `36020877017497`）：与 [B-5](#b-5-inelastic-hinge-force) 一样，
> Truss/Spring 标签在旧版本中互换了 —— 更正。

- **Lumped：** `["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time", "Dy/max(D/D2)", "Dy/Time", "Dz/max(D/D2)", "Dz/Time", "Rx/max(D/D2)", "Rx/Time", "Ry/max(D/D2)", "Ry/Time", "Rz/max(D/D2)", "Rz/Time"]`
- **Dist / Wall：** `["Index", ... , "Dx/max", "Dx/Time", ... , "Rz/max", "Rz/Time"]` （Dist 使用 `Elem` 列，Wall 使用 `WallID`·`Story` 列）
- **Truss：** `["Index", "Elem", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time"]`
- **Spring：** `["Index", "GeneralLink/No", "GeneralLink/Prop.", "GeneralLink/Node1", "GeneralLink/Node2", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time", ... , "Rz/max(D/D2)", "Rz/Time"]`

#### Request / Response JSON

**POST Request Body — 集中型(IEHG_DUCT_D2_LUMPED)**

```json
{
  "Argument": {
    "TABLE_NAME": "Lumped",
    "TABLE_TYPE": "IEHG_DUCT_D2_LUMPED",
    "EXPORT_PATH": "C:\\MIDAS\\Result\\Output.JSON",
    "UNIT": { "FORCE": "kN", "DIST": "m" },
    "STYLES": { "FORMAT": "Fixed", "PLACE": 12 },
    "COMPONENTS": ["Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max", "Dx/Time", "Dy/max", "Dy/Time", "Dz/max", "Dz/Time", "Rx/max", "Rx/Time", "Ry/max", "Ry/Time", "Rz/max", "Rz/Time"],
    "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"]
  }
}
```

**POST Response Body**

```json
{
  "Lumped": {
    "FORCE": "kN",
    "DIST": "m",
    "HEAD": ["Index", "Elem", "HingeLocation", "InelasticHingeProp.", "Load", "Dx/max(D/D2)", "Dx/Time", "Dy/max(D/D2)", "Dy/Time", "Dz/max(D/D2)", "Dz/Time", "Rx/max(D/D2)", "Rx/Time", "Ry/max(D/D2)", "Ry/Time", "Rz/max(D/D2)", "Rz/Time"],
    "DATA": [
      ["1", "3", "Center", "Column", "Elcent(max)", "27.468795776367", "3.099999904633", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
      ["2", "3", "I", "Column", "Elcent(max)", "-", "-", "0.000000000000", "0.000000000000", "0.000000000000", "0.000000000000", "-", "-", "96.578498840332", "2.599999904633", "105.144279479980", "2.099999904633"]
    ]
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 提取墙体铰延性 D/D2 表格 ────────────────────────────────
payload = {
    "Argument": {
        "TABLE_NAME": "Wall",
        "TABLE_TYPE": "IEHG_DUCT_D2_WALL",     # 墙体铰
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "TH_LOAD_CASE_NAMES": ["Elcent(TH:max)", "Elcent(TH:min)"],
    }
}
res = requests.post(f"{BASE_URL}/post/TABLE", json=payload, headers=HEADERS).json()
key = next(iter(res))
print("table:", key, "/ rows:", len(res[key]["DATA"]))
```

---

## C 组. 水化热分析结果显示 (`view/RESULTGRAPHIC`)

水化热(Heat of Hydration)分析结果不是表格，而是以**模型窗口的图形（等值线等）**显示。因此本组不用 `post/*`，而是以 **`view/RESULTGRAPHIC`** Endpoint 请求，请求结构原样复用**第16章的 RESULTGRAPHIC 结构**。

### Input URI（C 组公共）

```
{base url}/view/RESULTGRAPHIC
```

### Active Methods

`POST`

### 公共 Request 结构

| No. | 说明 | Key | 值类型 | 备注 |
|-----|------|-----|-----------|------|
| 1 | 结果图形模式（按Endpoint的值，各节参照） | `"CURRENT_MODE"` | String | **Required** |
| 2 | 荷载工况/组合 | `"LOAD_CASE_COMB"` | Object | — |
| 2-1 | └ 水化热步索引 | `LOAD_CASE_COMB.STEP_INDEX` | Integer | 水化热分析步 |
| 3 | 选项（部分模式） | `"OPTIONS"` | Object | Stress 模式下使用 |
| 3-1 | └ 坐标系 (`"UCS"` / `"Local"`) | `OPTIONS.LOCAL_UCS.TYPE` | String | — |
| 3-2 | └ 应力计算法 (`"Element"` / `"Avg.Nodal"`) | `OPTIONS.AVERAGE_NODAL.TYPE` | String | — |
| 4 | 分量（部分模式） | `"COMPONENTS"` | Object | Stress·Displacements 模式 |
| 4-1 | └ 分量名 | `COMPONENTS.COMP` | String | 按模式的 enum |
| 5 | 向量选项（`COMP` 为 `"Vector"` 时） | `"VECTOR_OPTION"` | Object | — |
| 5-1 | └ 向量示意图比例 | `VECTOR_OPTION.SCALE_FACTOR_LENGTH` | Number | — |
| 6 | 显示类型（等值线/变形/图例等，参照第16章） | `"TYPE_OF_DISPLAY"` | Object | — |

> **参考：** `TYPE_OF_DISPLAY` 的详细下级键（`CONTOUR`·`VALUES`·`LEGEND`·`DEFORM`·`MIRRORED`·`CUTTING_PLANE`·`ISO_SURFACE` 等）请参照**第16章 `/view/RESULTGRAPHIC`** 手册。下面示例使用等值线(`CONTOUR`)的默认设置。

### 公共 Response 结构

RESULTGRAPHIC 是刷新图形显示的命令，因此响应不是结果数据而是刷新消息（与第16章相同）。

```json
{
  "RESULTGRAPHIC": "Result graphic display updated."
}
```

---

### C-1. Stress – Heat of Hydration

> **功能：** 在指定步以等值线/向量显示水化热分析的**应力(Stress)** 结果。

- `CURRENT_MODE`：`"HY_STRESS"`
- `COMPONENTS.COMP` enum：`"Sig-XX"`, `"Sig-YY"`, `"Sig-ZZ"`, `"Sig-XY"`, `"Sig-YZ"`, `"Sig-XZ"`, `"Sig-P1"`, `"Sig-P2"`, `"Sig-P3"`, `"Tresca"`, `"Sig-EFF"`, `"Sig-Pmax"`, `"Sig-xx"`, `"Sig-yy"`, `"Sig-zz"`, `"Sig-xy"`, `"Sig-yz"`, `"Sig-xz"`, `"Vector"`

#### Request / Response JSON

**POST Request Body — 应力等值线(Sig-XX)**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_STRESS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "OPTIONS": {
      "LOCAL_UCS": { "TYPE": "UCS" },
      "AVERAGE_NODAL": { "TYPE": "Element" }
    },
    "COMPONENTS": { "COMP": "Sig-XX" },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
      }
    }
  }
}
```

**POST Request Body — 应力向量(Vector)**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_STRESS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 3 },
    "OPTIONS": {
      "LOCAL_UCS": { "TYPE": "Local" },
      "AVERAGE_NODAL": { "TYPE": "Element" }
    },
    "COMPONENTS": {
      "COMP": "Vector",
      "VECTOR_OPTION": { "SCALE_FACTOR_LENGTH": 1.0 }
    },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
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

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 以等值线显示水化热步1的 Sig-XX 应力 ───────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_STRESS",
        "LOAD_CASE_COMB": {"STEP_INDEX": 1},     # 水化热分析步编号
        "OPTIONS": {
            "LOCAL_UCS": {"TYPE": "UCS"},
            "AVERAGE_NODAL": {"TYPE": "Element"},
        },
        "COMPONENTS": {"COMP": "Sig-XX"},
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())   # {"RESULTGRAPHIC": "Result graphic display updated."}
```

---

### C-2. Temperature – Heat of Hydration

> **功能：** 在指定步以等值线显示水化热分析的**温度(Temperature)** 分布。

- `CURRENT_MODE`：`"HY_TEMPERATURE"`
- 不指定分量(`COMPONENTS`)，只指定步(`STEP_INDEX`)。

#### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_TEMPERATURE",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
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

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 逐次显示水化热各步的温度分布 ────────────────────────────
for step in range(1, 6):
    payload = {
        "Argument": {
            "CURRENT_MODE": "HY_TEMPERATURE",
            "LOAD_CASE_COMB": {"STEP_INDEX": step},
            "TYPE_OF_DISPLAY": {
                "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
            },
        }
    }
    res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
    print(f"step {step}:", res.json())
```

---

### C-3. Displacements – Heat of Hydration

> **功能：** 在指定步按分量显示水化热分析的**位移(Displacements)**。

- `CURRENT_MODE`：`"HY_DISPLACEMENTS"`
- `COMPONENTS.COMP` enum：`"DX"`, `"DY"`, `"DZ"`, `"RX"`, `"RY"`, `"RZ"`, `"DXY"`, `"DYZ"`, `"DXZ"`, `"DXYZ"`

#### Request / Response JSON

**POST Request Body — DX**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_DISPLACEMENTS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "COMPONENTS": { "COMP": "DX" },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
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

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 以等值线显示水化热位移合(DXYZ) ─────────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_DISPLACEMENTS",
        "LOAD_CASE_COMB": {"STEP_INDEX": 1},
        "COMPONENTS": {"COMP": "DXYZ"},          # 合位移
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())
```

---

### C-4. Allowable Tensile Stress – Heat of Hydration

> **功能：** 在指定步以等值线显示水化热分析的**允许拉应力(Allowable Tensile Stress)**。

- `CURRENT_MODE`：`"HY_ALLOWABLETENSILESTRESS"`

#### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_ALLOWABLETENSILESTRESS",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
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

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 显示水化热允许拉应力等值线 ───────────────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_ALLOWABLETENSILESTRESS",
        "LOAD_CASE_COMB": {"STEP_INDEX": 1},
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())
```

---

### C-5. Crack Ratio – Heat of Hydration

> **功能：** 在指定步以等值线显示水化热分析的**开裂指数(Crack Ratio)**。用于评估由温度应力引发开裂的风险。

- `CURRENT_MODE`：`"HY_CRACKRATIO"`

#### Request / Response JSON

**POST Request Body**

```json
{
  "Argument": {
    "CURRENT_MODE": "HY_CRACKRATIO",
    "LOAD_CASE_COMB": { "STEP_INDEX": 1 },
    "TYPE_OF_DISPLAY": {
      "CONTOUR": {
        "OPT_CHECK": true,
        "NUM_OF_COLOR": 12,
        "COLOR_TYPE": "rgb",
        "GRADIENT_FILL": false,
        "CONTOUR_FILL": false
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

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── 以等值线显示最终步的开裂指数 ─────────────────────────────
payload = {
    "Argument": {
        "CURRENT_MODE": "HY_CRACKRATIO",
        "LOAD_CASE_COMB": {"STEP_INDEX": 10},
        "TYPE_OF_DISPLAY": {
            "CONTOUR": {"OPT_CHECK": True, "NUM_OF_COLOR": 12, "COLOR_TYPE": "rgb"}
        },
    }
}
res = requests.post(f"{BASE_URL}/view/RESULTGRAPHIC", json=payload, headers=HEADERS)
print(res.json())
```

---

## D 组. 时程智能图表 DB (`db/THR*`)

本组是用于创建/查询/修改/删除「以**智能图表(Smart Graph)** 提取时程结果」的定义记录的 **CRUD DB Endpoint**。与结果表格（A/B 组）不同，本组把「用哪个单元·分量成图」登记到数据库中。

### 公共事项（D 组 DB Endpoint）

| 方法 | 动作 | URL |
|--------|------|-----|
| `POST` | 创建/更新（`"Assign"` 请求体，ID 键） | `{base url}/db/THR*` |
| `GET` | 全部查询 | `{base url}/db/THR*` |
| `GET` | 特定 ID 查询 | `{base url}/db/THR*/{id}` |
| `PUT` | 修改（`"Assign"` 请求体，ID 键） | `{base url}/db/THR*` |
| `DELETE` | 删除（特定 ID） | `{base url}/db/THR*/{id}` |

> **参考**
> - 请求体在 `"Assign"` 对象之下以**记录ID（字符串键）**定义条目。
> - `GET` 响应以 URI 名(`THRE`/`THRG`/`THRI`/`THRS`)为最上级键，按 ID 返回记录。
> - `GET` 可以在 URL 路径后附加 ID 进行个别查询，`DELETE` 删除特定 ID。
> - `THIS_NAME` 是目标**时程荷载工况(Time History Load Case)** 的名称。

---

### D-1. Element Force Smart Graph – `db/THRE`

> **功能：** 定义以时程智能图表提取单元构件内力(Element Force)所需的记录。

#### Input URI

```
{base url}/db/THRE
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 属性

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 时程荷载工况名 | `"THIS_NAME"` | String | — | **Required** |
| 2 | 单元类型 · Beam: `0` / Truss: `1` / Wall: `2` | `"TYPE_ELEMENT"` | Integer | — | **Required** |
| 3 | 单元编号 | `"PROPERTY_KEY"` | Integer | — | **Required** |
| 4 | 层名称（`TYPE_ELEMENT` 为 `2`(Wall) 时） | `"STORY_NAME"` | String | Blank | Optional |
| 5 | 结果类型 · Force: `0` | `"TYPE_RES"` | Integer | `0` | Optional |
| 6 | 位置 · I端/Top：`0` / J端/Bottom：`1` | `"LOCATION"` | Integer | `0` | Optional |
| 7 | 分量 · Axial: `0` / Shear-y: `1` / Shear-z: `2` / Torsion: `3` / Moment-y: `4` / Moment-z: `5` | `"COMP"` | Integer | `0` | Optional |

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 102,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "THRE": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 102,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 定义梁单元102号轴力(Axial, I端)的智能图表 ──────────────
payload = {
    "Assign": {
        "1": {
            "THIS_NAME": "HIST1",      # 时程荷载工况名
            "TYPE_ELEMENT": 0,          # 0=Beam
            "PROPERTY_KEY": 102,        # 单元编号
            "STORY_NAME": "",
            "TYPE_RES": 0,              # 0=Force
            "LOCATION": 0,              # 0=I-end/Top
            "COMP": 0,                  # 0=Axial
        }
    }
}
requests.post(f"{BASE_URL}/db/THRE", json=payload, headers=HEADERS)

# ── GET: 查询已定义的单元构件内力智能图表全部 ───────────────────
res = requests.get(f"{BASE_URL}/db/THRE", headers=HEADERS).json()
for gid, rec in res.get("THRE", {}).items():
    print(f"  [{gid}] elem {rec['PROPERTY_KEY']} COMP={rec['COMP']}")

# ── DELETE: 删除1号记录 ───────────────────────────────────────
requests.delete(f"{BASE_URL}/db/THRE/1", headers=HEADERS)
```

---

### D-2. General Link Smart Graph – `db/THRG`

> **功能：** 定义以时程智能图表提取一般连接(General Link)结果所需的记录。

#### Input URI

```
{base url}/db/THRG
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 属性

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 名称(时程荷载工况名) | `"THIS_NAME"` | String | — | **Required** |
| 2 | 结果类型 · Force-Deformation: `0` / Force: `1` / Deformation: `2` | `"TYPE_RES"` | Integer | `0` | Optional |
| 3 | 位置 · i端: `0` / j端: `1` | `"LOCATION"` | Integer | `0` | Optional |
| 4 | 分量 (Force-Deformation/Force/Deformation) · Fx-Dx/Fx/Dx: `0` / Fy-Dy/Fy/Dy: `1` / Fz-Dz/Fz/Dz: `2` / Mx-Rx/Mx/Rx: `3` / My-Ry/My/Ry: `4` / Mz-Rz/Mz/Rz: `5` | `"COMP"` | Integer | `0` | Optional |
| 5 | 一般连接编号 | `"GENERAL_LINK"` | Integer | — | **Required** |

> ⚠️ 2026-08-26 确认（article id `35992341376025`）：官方 Specifications 表把 `COMP` enum 只记为
> `Fx(NL): 0 / Fy: 1 / Fz: 2` 3个（看起来是该表自身漏项），但采用同一结构的
> [D-3 Inelastic Hinge Smart Graph](#d-3-inelastic-hinge-smart-graph--dbthri) 的官方
> Specifications 表中收录了 `Mx-Rx/Mx/Rx: 3`·`My-Ry/My/Ry: 4`·`Mz-Rz/Mz/Rz: 5` 在内的全部6个，
> 且 D-3 的 Request 示例实际也使用了 `COMP: 4`。以同级 Endpoint 交叉确认，保留全部6个。

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 4
    }
  }
}
```

**GET Response Body**

```json
{
  "THRG": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 4
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 定义一般连接1,4号的力-变形(Fx-Dx)智能图表 ───────────────
payload = {
    "Assign": {
        "1": {"THIS_NAME": "HIST1", "TYPE_RES": 0, "LOCATION": 0, "COMP": 0, "GENERAL_LINK": 1},
        "2": {"THIS_NAME": "HIST1", "TYPE_RES": 0, "LOCATION": 0, "COMP": 0, "GENERAL_LINK": 4},
    }
}
requests.post(f"{BASE_URL}/db/THRG", json=payload, headers=HEADERS)

# ── PUT: 把2号记录修改为 Deformation(Dy) ────────────────────────
requests.put(f"{BASE_URL}/db/THRG", headers=HEADERS, json={
    "Assign": {"2": {"THIS_NAME": "HIST1", "TYPE_RES": 2, "LOCATION": 0, "COMP": 1, "GENERAL_LINK": 4}}
})

# ── GET: 查询特定 ID(1号) ──────────────────────────────────────
print(requests.get(f"{BASE_URL}/db/THRG/1", headers=HEADERS).json())
```

---

### D-3. Inelastic Hinge Smart Graph – `db/THRI`

> **功能：** 定义以时程智能图表提取非弹性铰(Inelastic Hinge)结果所需的记录。

#### Input URI

```
{base url}/db/THRI
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 属性

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 名称(时程荷载工况名) | `"THIS_NAME"` | String | — | **Required** |
| 2 | 单元类型 · Beam: `0` / Truss: `1` / General Link: `3` | `"TYPE_ELEMENT"` | Integer | `0` | Optional |
| 3 | 单元选择(单元编号) | `"PROPERTY_KEY"` | Integer | — | **Required** |
| 4 | 层名称 | `"STORY_NAME"` | String | Blank | Optional |
| 5 | 结果类型 · Force-Deformation: `0` / Force: `1` / Deformation: `2` | `"TYPE_RES"` | Integer | `0` | Optional |
| 6 | 位置 · 1-Pos: `0` / 2-Pos: `1` / 3-Pos: `2` | `"LOCATION"` | Integer | `0` | Optional |
| 7 | 分量 (Force-Deformation/Force/Deformation) · Fx-Dx/Fx/Dx: `0` / Fy-Dy/Fy/Dy: `1` / Fz-Dz/Fz/Dz: `2` / Mx-Rx/Mx/Rx: `3` / My-Ry/My/Ry: `4` / Mz-Rz/Mz/Rz: `5` | `"COMP"` | Integer | `0` | Optional |

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2101,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2137,
      "STORY_NAME": "",
      "TYPE_RES": 1,
      "LOCATION": 1,
      "COMP": 0
    },
    "3": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2184,
      "STORY_NAME": "",
      "TYPE_RES": 2,
      "LOCATION": 1,
      "COMP": 4
    }
  }
}
```

**GET Response Body**

```json
{
  "THRI": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2101,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 定义3个非弹性铰(力-变形/力/变形)的智能图表 ─────────────
payload = {
    "Assign": {
        "1": {"THIS_NAME": "HIST1", "TYPE_ELEMENT": 0, "PROPERTY_KEY": 2101,
              "STORY_NAME": "", "TYPE_RES": 0, "LOCATION": 0, "COMP": 0},
        "2": {"THIS_NAME": "HIST1", "TYPE_ELEMENT": 0, "PROPERTY_KEY": 2137,
              "STORY_NAME": "", "TYPE_RES": 1, "LOCATION": 1, "COMP": 0},
        "3": {"THIS_NAME": "HIST1", "TYPE_ELEMENT": 0, "PROPERTY_KEY": 2184,
              "STORY_NAME": "", "TYPE_RES": 2, "LOCATION": 1, "COMP": 4},
    }
}
requests.post(f"{BASE_URL}/db/THRI", json=payload, headers=HEADERS)

# ── GET: 全部查询 ────────────────────────────────────────────
res = requests.get(f"{BASE_URL}/db/THRI", headers=HEADERS).json()
print("已定义的铰图表数量:", len(res.get("THRI", {})))
```

---

### D-4. Seismic Devices Smart Graph – `db/THRS`

> **功能：** 定义以时程智能图表提取地震保护装置(Seismic Devices，阻尼器/隔震装置等)结果所需的记录。

#### Input URI

```
{base url}/db/THRS
```

#### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

#### JSON Schema 属性

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 名称(时程荷载工况名) | `"THIS_NAME"` | String | — | **Required** |
| 2 | 结果类型 · Force-Deformation: `0` / Force: `2` / Deformation: `3` / Ductility Factor: `5` / Energy: `7` | `"TYPE_RES"` | Integer | `0` | Optional |
| 3 | 分量 | `"COMP"` | Integer | `0` | Optional |
| 4 | 一般连接编号 | `"GENERAL_LINK"` | Integer | — | **Required** |

> ⚠️ 2026-08-26 确认（article id `35992460196121`）：官方 Request 示例的第3条记录使用了
> `"TYPE_RES": 4`，而该值在官方 Specifications 表的 `TYPE_RES` enum（`0`/`2`/`3`/`5`/`7`）
> 中并不存在（看起来是官方原文自身的漏项/矛盾，属错误举报对象）。本仓库保留示例的
> 实际值（`4`）。

#### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 2,
      "COMP": 1,
      "GENERAL_LINK": 4
    },
    "3": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 4,
      "COMP": 2,
      "GENERAL_LINK": 4
    }
  }
}
```

**GET Response Body**

```json
{
  "THRS": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    }
  }
}
```

#### Python Example

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}

# ── POST: 定义地震装置(一般连接1,4号)智能图表 ────────────────
payload = {
    "Assign": {
        "1": {"THIS_NAME": "HIST1", "TYPE_RES": 0, "COMP": 0, "GENERAL_LINK": 1},  # 力-变形
        "2": {"THIS_NAME": "HIST1", "TYPE_RES": 2, "COMP": 1, "GENERAL_LINK": 4},  # 力
        "3": {"THIS_NAME": "HIST1", "TYPE_RES": 4, "COMP": 2, "GENERAL_LINK": 4},  # 照抄官方示例原文(TYPE_RES enum 表中没有的值，见上方 ⚠️)
    }
}
requests.post(f"{BASE_URL}/db/THRS", json=payload, headers=HEADERS)

# ── GET: 全部查询后用 DELETE 删除3号 ─────────────────────────
res = requests.get(f"{BASE_URL}/db/THRS", headers=HEADERS).json()
print("已定义的装置图表:", list(res.get("THRS", {}).keys()))
requests.delete(f"{BASE_URL}/db/THRS/3", headers=HEADERS)
```

---

## End-to-End Workflow

用一个脚本展示典型的后处理流程：时程智能图表定义（D 组）→ 节点位移文本结果提取（A 组）→ 非弹性铰构件内力表格提取（B 组）。

```python
import requests

# ── 公共设置 ─────────────────────────────────────────────────────
BASE_URL = "https://moa-engineers.midasit.com:443/gen"   # Gen NX
HEADERS = {"Content-Type": "application/json", "MAPI-Key": "YOUR_MAPI_KEY"}
TH_CASE = "Elcent"    # 时程荷载工况名


def post(uri, body):
    return requests.post(f"{BASE_URL}{uri}", json=body, headers=HEADERS).json()


# 1) [D 组] 定义单元构件内力智能图表记录 (db/THRE) ─────────────────
graph_def = {
    "Assign": {
        "1": {
            "THIS_NAME": TH_CASE,
            "TYPE_ELEMENT": 0,     # 0=Beam
            "PROPERTY_KEY": 5,     # 梁单元5号
            "STORY_NAME": "",
            "TYPE_RES": 0,         # Force
            "LOCATION": 0,         # I端
            "COMP": 4,             # Moment-y
        }
    }
}
requests.post(f"{BASE_URL}/db/THRE", json=graph_def, headers=HEADERS)
print("[1] 智能图表定义完成")

# 2) [A 组] 提取节点10号的时程位移文本结果 (post/TEXT) ──────────────
disp = post("/post/TEXT", {
    "Argument": {
        "TEXT_TYPE": "TH_DISP",
        "UNIT": {"FORCE": "N", "DIST": "MM"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "NODE_ELEMS": {"KEYS": [10]},
        "TH_CASE_NAME": [TH_CASE],
        "STEP": {"FROM": 0.1, "TO": 0.5, "STEPS": 1},
        "REF_PT": "Ground",
    }
})
peak = max(disp["TH_DISP"]["DATA"], key=lambda r: abs(float(r[4])))
print(f"[2] 节点 10 最大 Dx = {peak[4]} mm (t={peak[3]}s)")

# 3) [B 组] 提取非弹性铰(集中型)构件内力表格 (post/TABLE) ───────────
force = post("/post/TABLE", {
    "Argument": {
        "TABLE_NAME": "Lumped",
        "TABLE_TYPE": "IEHG_FORCE_LUMPED",
        "UNIT": {"FORCE": "kN", "DIST": "m"},
        "STYLES": {"FORMAT": "Fixed", "PLACE": 6},
        "TH_LOAD_CASE_NAMES": [f"{TH_CASE}(TH:max)", f"{TH_CASE}(TH:min)"],
    }
})
tbl = force["Lumped"]
print(f"[3] 铰构件内力表格：{len(tbl['DATA'])}行, HEAD {len(tbl['HEAD'])}列")
for row in tbl["DATA"]:
    print(f"     elem {row[1]} {row[2]}  Fx={row[5]} @ t={row[6]}")

print("\n流程完成：图表定义 → 位移提取 → 铰构件内力提取")
```
