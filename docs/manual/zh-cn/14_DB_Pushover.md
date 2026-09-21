# 14. DB – Pushover

> **适用产品：** MIDAS Civil NX · MIDAS Gen NX  
> **Base URL:**
> ```
> https://moa-engineers.midasit.com:443/civil   # Civil NX
> https://moa-engineers.midasit.com:443/gen     # Gen NX
> ```
> **认证头：** `MAPI-Key: <已获取的密钥>`  
> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/en-us/articles/33016922742937)

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../14_DB_Pushover.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## Endpoint 列表

| No. | Endpoint | 功能 | Active Methods |
|-----|----------|------|----------------|
| 1 | [`/db/POGD`](#1-dbpogd--pushover-analysis-control-data) | 推覆分析（Pushover）控制数据 | POST, GET, PUT, DELETE |
| 2 | [`/db/POGD-M1`](#2-dbpogd-m1--pushover-global-control-hyper-s) | 推覆分析全局控制 (Hyper-S) | GET, PUT, DELETE |
| 3 | [`/db/IEPI`](#3-dbiepi--ignore-elements-for-pushover-initial-load) | 推覆分析初始荷载忽略单元 | POST, GET, PUT, DELETE |
| 4 | [`/db/PHGE`](#4-dbphge--assign-pushover-hinge-properties) | 推覆分析铰属性指派 | POST, GET, PUT, DELETE |
| 5 | [`/db/POLC`](#5-dbpolc--pushover-load-cases) | 推覆分析荷载工况 | POST, GET, PUT, DELETE |
| 6 | [`/db/POLC-M1`](#6-dbpolc-m1--pushover-load-case-hyper-s) | 推覆分析荷载工况 (Hyper-S) | GET, PUT, DELETE |

> **参考：** Hyper-S 求解器专用端点（`-M1`）**不支持 POST。** 数据的创建与修改用 `PUT`，查询用 `GET`，删除用 `DELETE`。

---

## 1. `/db/POGD` — Pushover Analysis Control Data

> **功能：** 定义推覆分析（静力非线性）的全局控制数据。包含几何非线性选项、初始荷载方法、非线性分析选项（收敛条件·分析停止条件）、纤维模型选项、铰数据选项。

### Input URI

```
{base url}/db/POGD
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "POGD": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "GEOMNONLINEAR_TYPE": { "description": "GeometricNonlinearityType", "type": "string" },
      "INITLOADMETHOD": { "description": "InitialLoadAnalysisMethod", "type": "string" },
      "INITLOAD": {
        "description": "InitialLoadCaseList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "LC_NAME": { "description": "LoadCaseName", "type": "string" },
            "LC_TYPE": { "description": "LoadCaseType", "type": "string" },
            "SF": { "description": "ScaleFactor", "type": "number" }
          }
        }
      },
      "bCONSIGNOREELEM": { "description": "ConsiderIgnoreElementsforNL.AnalysisInitialLoad", "type": "boolean" },
      "NONL_OPT": {
        "description": "NonlinearAnalysisOption",
        "type": "object",
        "properties": {
          "bPERMITFAIL": { "description": "NonlinearAnalysisPermitConvergenceFailure", "type": "boolean" },
          "SUBSTEP": { "description": "NonlinearAnalysisMaxNum.ofSubsteps", "type": "integer" },
          "MAXITER": { "description": "MaximumIteration", "type": "integer" },
          "bDISPLNORM": { "description": "UseConvergenceCriteriaDisplacementNorm", "type": "boolean" },
          "bFORCENORM": { "description": "UseConvergenceCriteriaForceNorm", "type": "boolean" },
          "bENERGYNORM": { "description": "UseConvergenceCriteriaEnergyNorm", "type": "boolean" },
          "DISPLNORM": { "description": "DisplacementNorm", "type": "number" },
          "FORCENORM": { "description": "ForceNorm", "type": "number" },
          "ENERGYNORM": { "description": "EnergyNorm", "type": "number" },
          "bSHEARYIELDSTOP": { "description": "UseAnalysisStop-ShearComp.Yield", "type": "boolean" },
          "BSHEARYIELDSTOPBEAM": { "description": "UseAnalysisStop-ShearComp.Yield-Beam/Column", "type": "boolean" },
          "bSHEARYIELDSTOPWALL": { "description": "UseAnalysisStop-ShearComp.Yield-Wall", "type": "boolean" },
          "bAXIALYIELDSTOP": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling", "type": "boolean" },
          "bAXIALYIELDSTOPBEAM": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling-Beam/Column", "type": "boolean" },
          "bAXIALYIELDSTOPWALL": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling-Wall", "type": "boolean" },
          "bAXIALYIELDSTOPTRUSS": { "description": "UseAnalysisStop-AxialComp.Collapse/Buckling-Truss", "type": "boolean" },
          "bSUPPORTDZDIRSTOP": { "description": "UseAnalysisStop-SupportUplifting/Collapse:Dz-Direction", "type": "boolean" },
          "bSUPPORTSTOPUPLIFTING": { "description": "UseAnalysisStop-Uplifting:Dz-Direction", "type": "boolean" },
          "bSUPPORTSTOPCOLLAPSE": { "description": "UseAnalysisStop-Collapse:Dz-Direction", "type": "boolean" }
        }
      },
      "PHOP_OPT": {
        "description": "NonlinearAnalysisOption",
        "type": "object",
        "properties": {
          "bCONSREBARAREA1D": { "description": "FiberModelOption-ConsiderBeam/ColumnReinforcementArea", "type": "boolean" },
          "BEAM_CORE_SIZE": { "description": "FiberModelOption-Beam-ColumnCoreAreasSizeType", "type": "string" },
          "BEAM_CORE_DIV_Y": { "description": "FiberModelOption-Beam-ColumnCoreDivision(y-dir)", "type": "integer" },
          "BEAM_CORE_DIV_Z": { "description": "FiberModelOption-Beam-ColumnCoreDivision(z-dir)", "type": "integer" },
          "BEAM_COVER_SIZE": { "description": "FiberModelOption-Beam-ColumnCoverAreasSizeType", "type": "string" },
          "BEAM_COVER_DIV_Y": { "description": "FiberModelOption-Beam-ColumnCoverDivision(y-dir)", "type": "integer" },
          "BEAM_COVER_DIV_Z": { "description": "FiberModelOption-Beam-ColumnCoverDivision(z-dir)", "type": "integer" },
          "bCONSREBARAREAWALL": { "description": "FiberModelOption-ConsiderWallReinforcementArea", "type": "boolean" },
          "bWALLCONSOUT": { "description": "FiberModelOption-WallConsiderOut-of-planeNonlinearityofPlateType", "type": "boolean" },
          "WALL_CORE_SIZE": { "description": "FiberModelOption-WallCoreFiberAreasSizeType", "type": "string" },
          "WALL_CORE_DIV_Z": { "description": "FiberModelOption-WallCoreDivision(z-dir)", "type": "integer" },
          "WALL_CORE_DIV_Y": { "description": "FiberModelOption-WallCoreDivision(y-dir)", "type": "integer" },
          "WALL_COVER_SIZE": { "description": "FiberModelOption-WallCoverAreasSizeType", "type": "string" },
          "WALL_COVER_DIV_Z": { "description": "FiberModelOption-WallCoverDivision(z-dir)", "type": "integer" },
          "WALL_COVER_DIV_Y": { "description": "FiberModelOption-WallCoverDivision(y-dir)", "type": "integer" },
          "SHEAR_R": { "description": "FiberModelOption-SpringShear", "type": "number" },
          "bASSIGNBYMEMBER": { "description": "AssignHingePropertiestoMemberonlyforMoment-RotationBeam/Column", "type": "boolean" },
          "bTRI_SYM": { "description": "UseTrilinearDefaultStiffnessReductionSymmetrical", "type": "boolean" },
          "TRI_TENS_A1": { "description": "TrilinearDefaultStiffnessReduction-Tens.a1", "type": "number" },
          "TRI_TENS_A2": { "description": "TrilinearDefaultStiffnessReduction-Tens.a2", "type": "number" },
          "TRI_COMP_A1": { "description": "TrilinearDefaultStiffnessReduction-Comp.a1", "type": "number" },
          "TRI_COMP_A2": { "description": "TrilinearDefaultStiffnessReduction-Comp.a2", "type": "number" },
          "bBI_SYM": { "description": "UseBilinearDefaultStiffnessReductionSymmetrical", "type": "boolean" },
          "BI_TENS_A1": { "description": "BilinearDefaultStiffnessReduction-Tens.a1", "type": "number" },
          "BI_COMP_A1": { "description": "BilinearDefaultStiffnessReduction-Comp.a1", "type": "number" },
          "PSPR_APPLY_TYPE": { "description": "PointSpringSupportApplyType", "type": "string" },
          "ELNK_APPLY_TYPE": { "description": "ElasticLinkApplyType", "type": "string" },
          "bUSEAUTOCALCREFERENCE": { "description": "ReferenceCode/ManualforAuto-Calculation", "type": "boolean" },
          "RCDGNCODE": { "description": "RCReferenceDesignCode", "type": "string" },
          "LOC_BEAM": { "description": "ReferenceLocationofBeam/DistributedHinges", "type": "string" },
          "LOC_COLUMN": { "description": "ReferenceLocationofColumn", "type": "string" },
          "SF_WALL": { "description": "ScaleFactorforUltimateRotation-WallScaleFactor", "type": "number" },
          "bSF_BRITTLE": { "description": "ScaleFactorforUltimateRotation-UseBrittleScaleFactor", "type": "boolean" },
          "SF_BRITTLE": { "description": "ScaleFactorforUltimateRotation-BrittleScaleFactor", "type": "number" },
          "bSF_EARTHQUAKE": { "description": "ScaleFactorforUltimateRotation-UseEarthquakeScaleFactor", "type": "boolean" },
          "SF_EARTHQUAKE": { "description": "ScaleFactorforUltimateRotation-EarthquakeScaleFactor", "type": "number" },
          "bSF_SMOOTH_BAR": { "description": "ScaleFactorforUltimateRotation-UseSmoothbarScaleFactor", "type": "boolean" },
          "SF_SMOOTH_BAR": { "description": "ScaleFactorforUltimateRotation-SmoothbarScaleFactor", "type": "number" },
          "SND_SEIS_GRUP": { "description": "SecondarySeismicElementsGroupName", "type": "string" },
          "CONFIDENCE": { "description": "ConfidenceFactor", "type": "number" },
          "bBUCKLING": { "description": "CalcYieldSurfaceofBeamconsideringBuckling", "type": "boolean" },
          "bCALCAXIALFORCE": { "description": "CalcMcConsideringAxialForce(AIJ)", "type": "boolean" }
        }
      },
      "NODECONNECTIVITY": { "description": "WallNodeConnectivity", "type": "string" },
      "bSHOWGRAPHAFTER": { "description": "Misc...-ShowPushoverCurveResultAfterAnalysis", "type": "boolean" },
      "bSHOWGRAPGHDURING": { "description": "Misc...-ShowPushoverCurveduringAnalysis", "type": "boolean" }
    }
  }
}
```

### Parameters

**顶层项**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 几何非线性类型 · None: `"NONE"` / Large Displacements: `"LARGE_DISP"` | `"GEOMNONLINEAR_TYPE"` | String | `"NONE"` | Optional |
| 2 | 初始荷载方法 · 执行非线性静力分析: `"PERFORM_ANAL"` / 导入静力·施工阶段分析结果: `"IMPORT_RESULT"` | `"INITLOADMETHOD"` | String | `"PERFORM_ANAL"` | Optional |
| 3 | 初始荷载工况列表 | `"INITLOAD"` | Array [Object] | — | Optional |
| — | (INITLOAD) 荷载工况名 | `"LC_NAME"` | String | — | Required |
| — | (INITLOAD) 荷载工况类型 | `"LC_TYPE"` | String | — | Required |
| — | (INITLOAD) 缩放系数 | `"SF"` | Number | — | Required |
| 4 | 初始荷载为非线性静力分析时，是否考虑忽略单元(IEPI) | `"bCONSIGNOREELEM"` | Boolean | `false` | Optional |
| 5 | 非线性分析选项 | `"NONL_OPT"` | Object | — | **Required** |
| 6 | 推覆分析铰数据选项 | `"PHOP_OPT"` | Object | — | Optional |
| 7 | 墙单元节点连接性 · 铰接: `"PINNED"` / 固接: `"FIXED"` | `"NODECONNECTIVITY"` | String | — | Required |
| 8 | 分析后显示推覆曲线结果 | `"bSHOWGRAPHAFTER"` | Boolean | — | Required |
| 9 | 分析过程中显示推覆曲线 | `"bSHOWGRAPGHDURING"` | Boolean | — | Required |

**`NONL_OPT`（非线性分析选项）明细**

| 分组 | Key | 说明 | 类型 | 默认值 |
|------|-----|------|------|--------|
| 通用 | `bPERMITFAIL` | 允许收敛失败 | Boolean | `false` |
| 通用 | `SUBSTEP` | 子步最大数 | Integer | — |
| 通用 | `MAXITER` | 最大迭代次数 | Integer | — |
| 收敛条件 | `bDISPLNORM` / `DISPLNORM` | 位移范数 是否使用/取值 | Boolean/Number | `false` / `0` |
| 收敛条件 | `bFORCENORM` / `FORCENORM` | 荷载范数 是否使用/取值 | Boolean/Number | `false` / `0` |
| 收敛条件 | `bENERGYNORM` / `ENERGYNORM` | 能量范数 是否使用/取值 | Boolean/Number | `false` / `0` |
| 分析停止 | `bSHEARYIELDSTOP` | 剪切分量屈服时停止 | Boolean | `false` |
| 分析停止 | `BSHEARYIELDSTOPBEAM` | 〃 – 梁/柱 | Boolean | `false` |
| 分析停止 | `bSHEARYIELDSTOPWALL` | 〃 – 墙 | Boolean | `false` |
| 分析停止 | `bAXIALYIELDSTOP` | 轴力分量破坏/屈曲时停止 | Boolean | `false` |
| 分析停止 | `bAXIALYIELDSTOPBEAM` | 〃 – 梁/柱 | Boolean | `false` |
| 分析停止 | `bAXIALYIELDSTOPWALL` | 〃 – 墙 | Boolean | `false` |
| 分析停止 | `bAXIALYIELDSTOPTRUSS` | 〃 – 桁架 | Boolean | `false` |
| 分析停止 | `bSUPPORTDZDIRSTOP` | 支座抬起/破坏(Dz方向)时停止 | Boolean | `false` |
| 分析停止 | `bSUPPORTSTOPUPLIFTING` | 〃 – 抬起(Uplifting) | Boolean | `false` |
| 分析停止 | `bSUPPORTSTOPCOLLAPSE` | 〃 – 破坏(Collapse) | Boolean | `false` |

**`PHOP_OPT`（推覆分析铰数据选项）明细**

| 分组 | Key | 说明 | 类型 |
|------|-----|------|------|
| 纤维(梁-柱) | `bCONSREBARAREA1D` | 考虑配筋量 | Boolean |
| 纤维(梁-柱) | `BEAM_CORE_SIZE` | 核心区尺寸类型 · Auto: `"AUTO"` / Equal: `"EQUAL"` | String |
| 纤维(梁-柱) | `BEAM_CORE_DIV_Y` / `BEAM_CORE_DIV_Z` | 核心区分分数 (y/z) | Integer |
| 纤维(梁-柱) | `BEAM_COVER_SIZE` | 保护层区尺寸类型 | String |
| 纤维(梁-柱) | `BEAM_COVER_DIV_Y` / `BEAM_COVER_DIV_Z` | 保护层区分分数 (y/z) | Integer |
| 纤维(墙) | `bCONSREBARAREAWALL` | 考虑配筋量 | Boolean |
| 纤维(墙) | `bWALLCONSOUT` | 考虑板类型面外非线性 | Boolean |
| 纤维(墙) | `WALL_CORE_SIZE` / `WALL_COVER_SIZE` | 核心区/保护层区尺寸类型 | String |
| 纤维(墙) | `WALL_CORE_DIV_Z` / `WALL_CORE_DIV_Y` | 核心区分分数 (z/y) | Integer |
| 纤维(墙) | `WALL_COVER_DIV_Z` / `WALL_COVER_DIV_Y` | 保护层区分分数 (z/y) | Integer |
| 纤维(墙) | `SHEAR_R` | 弹簧剪切系数 | Number |
| 铰选项 | `bASSIGNBYMEMBER` | 仅将弯矩-转角梁/柱铰属性指派给构件 | Boolean |
| 刚度折减(三线性) | `bTRI_SYM` | 是否对称 | Boolean |
| 刚度折减(三线性) | `TRI_TENS_A1` / `TRI_TENS_A2` | 受拉 α1/α2 | Number |
| 刚度折减(三线性) | `TRI_COMP_A1` / `TRI_COMP_A2` | 受压 α1/α2 | Number |
| 刚度折减(双线性) | `bBI_SYM` | 是否对称 | Boolean |
| 刚度折减(双线性) | `BI_TENS_A1` / `BI_COMP_A1` | 受拉/受压 α1 | Number |
| 弹簧/连接非线性 | `PSPR_APPLY_TYPE` · `"APPLY"` / `"ASSUME"` | 点弹簧支承应用类型 | String |
| 弹簧/连接非线性 | `ELNK_APPLY_TYPE` · `"APPLY"` / `"ASSUME"` | 弹性连接应用类型 | String |
| 强度自动计算 | `bUSEAUTOCALCREFERENCE` | 使用参考规范/手册 | Boolean |
| 强度自动计算 | `RCDGNCODE` · `"KISTEC2019"` / `"KISTEC2013"` / `"MOE2019"` / `"MOE2018"` / `"AIK-G-001-2021"` | RC 参考设计标准 | String |
| 强度自动计算 | `LOC_BEAM` · I端: `"I"` / J端: `"J"` / 跨中: `"M"` | 梁/分布铰基准位置 | String |
| 强度自动计算 | `LOC_COLUMN` | 柱基准位置 | String |
| 极限转动缩放系数 | `SF_WALL` | 墙缩放系数 | Number |
| 极限转动缩放系数 | `bSF_BRITTLE` / `SF_BRITTLE` | 脆性缩放系数 是否使用/取值 | Boolean/Number |
| 极限转动缩放系数 | `bSF_EARTHQUAKE` / `SF_EARTHQUAKE` | 地震缩放系数 是否使用/取值 | Boolean/Number |
| 极限转动缩放系数 | `bSF_SMOOTH_BAR` / `SF_SMOOTH_BAR` | 光圆钢筋缩放系数 是否使用/取值 | Boolean/Number |
| 其他 | `SND_SEIS_GRUP` | 二级抗震构件组名 | String |
| 其他 | `CONFIDENCE` | 置信度系数 | Number |
| 其他 | `bBUCKLING` | 考虑屈曲的屈服面计算 | Boolean |
| 其他 | `bCALCAXIALFORCE` | 考虑轴力的 Mc 计算(AIJ) | Boolean |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "GEOMNONLINEAR_TYPE": "NONE",
      "INITLOADMETHOD": "PERFORM_ANAL",
      "INITLOAD": [],
      "bCONSIGNOREELEM": true,
      "NONL_OPT": {
        "bPERMITFAIL": true,
        "SUBSTEP": 10,
        "MAXITER": 10,
        "bDISPLNORM": true,
        "bFORCENORM": false,
        "bENERGYNORM": false,
        "DISPLNORM": 0.001,
        "FORCENORM": 0.001,
        "ENERGYNORM": 0.001,
        "bSHEARYIELDSTOP": false,
        "BSHEARYIELDSTOPBEAM": true,
        "bSHEARYIELDSTOPWALL": false,
        "bAXIALYIELDSTOP": false,
        "bAXIALYIELDSTOPBEAM": true,
        "bAXIALYIELDSTOPWALL": false,
        "bAXIALYIELDSTOPTRUSS": false,
        "bSUPPORTDZDIRSTOP": false,
        "bSUPPORTSTOPUPLIFTING": false,
        "bSUPPORTSTOPCOLLAPSE": false
      },
      "PHOP_OPT": {
        "bCONSREBARAREA1D": false,
        "BEAM_CORE_SIZE": "AUTO",
        "BEAM_CORE_DIV_Y": 15,
        "BEAM_CORE_DIV_Z": 15,
        "BEAM_COVER_SIZE": "EQUAL",
        "BEAM_COVER_DIV_Y": 15,
        "BEAM_COVER_DIV_Z": 15,
        "bCONSREBARAREAWALL": false,
        "bWALLCONSOUT": true,
        "WALL_CORE_SIZE": "AUTO",
        "WALL_CORE_DIV_Z": 8,
        "WALL_CORE_DIV_Y": 8,
        "WALL_COVER_SIZE": "AUTO",
        "WALL_COVER_DIV_Z": 8,
        "WALL_COVER_DIV_Y": 1,
        "SHEAR_R": 0.4,
        "bASSIGNBYMEMBER": true,
        "bTRI_SYM": true,
        "TRI_TENS_A1": 0.1,
        "TRI_TENS_A2": 0.05,
        "TRI_COMP_A1": 0.1,
        "TRI_COMP_A2": 0.05,
        "bBI_SYM": true,
        "BI_TENS_A1": 0.05,
        "BI_COMP_A1": 0.05,
        "PSPR_APPLY_TYPE": "ASSUME",
        "ELNK_APPLY_TYPE": "APPLY",
        "bUSEAUTOCALCREFERENCE": true,
        "RCDGNCODE": "KISTEC2019",
        "LOC_BEAM": "M",
        "LOC_COLUMN": "I",
        "SF_WALL": 1.6,
        "bSF_BRITTLE": false,
        "SF_BRITTLE": 1.6,
        "bSF_EARTHQUAKE": false,
        "SF_EARTHQUAKE": 0.85,
        "bSF_SMOOTH_BAR": false,
        "SF_SMOOTH_BAR": 0.575,
        "CONFIDENCE": 1,
        "bBUCKLING": true,
        "bCALCAXIALFORCE": true
      },
      "NODECONNECTIVITY": "PINNED",
      "bSHOWGRAPHAFTER": true,
      "bSHOWGRAPGHDURING": false
    }
  }
}
```

**GET Response Body**

```json
{
  "POGD": {
    "1": {
      "GEOMNONLINEAR_TYPE": "NONE",
      "INITLOADMETHOD": "PERFORM_ANAL",
      "INITLOAD": [],
      "bCONSIGNOREELEM": true,
      "NONL_OPT": { "SUBSTEP": 10, "MAXITER": 10 },
      "PHOP_OPT": { "BEAM_CORE_SIZE": "AUTO" },
      "NODECONNECTIVITY": "PINNED",
      "bSHOWGRAPHAFTER": true,
      "bSHOWGRAPGHDURING": false
    }
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

# ── POST: 创建推覆分析控制数据 ──────────────────────────────
payload = {
    "Assign": {
        "1": {
            "GEOMNONLINEAR_TYPE": "NONE",
            "INITLOADMETHOD": "PERFORM_ANAL",
            "INITLOAD": [],
            "bCONSIGNOREELEM": True,
            "NONL_OPT": {
                "bPERMITFAIL": True,
                "SUBSTEP": 10,
                "MAXITER": 10,
                "bDISPLNORM": True,
                "bFORCENORM": False,
                "bENERGYNORM": False,
                "DISPLNORM": 0.001,
                "FORCENORM": 0.001,
                "ENERGYNORM": 0.001,
                "bSHEARYIELDSTOP": False,
                "BSHEARYIELDSTOPBEAM": True,
                "bSHEARYIELDSTOPWALL": False,
                "bAXIALYIELDSTOP": False,
                "bAXIALYIELDSTOPBEAM": True,
                "bAXIALYIELDSTOPWALL": False,
                "bAXIALYIELDSTOPTRUSS": False,
                "bSUPPORTDZDIRSTOP": False,
                "bSUPPORTSTOPUPLIFTING": False,
                "bSUPPORTSTOPCOLLAPSE": False
            },
            "PHOP_OPT": {
                "bCONSREBARAREA1D": False,
                "BEAM_CORE_SIZE": "AUTO",
                "BEAM_CORE_DIV_Y": 15,
                "BEAM_CORE_DIV_Z": 15,
                "BEAM_COVER_SIZE": "EQUAL",
                "BEAM_COVER_DIV_Y": 15,
                "BEAM_COVER_DIV_Z": 15,
                "bCONSREBARAREAWALL": False,
                "bWALLCONSOUT": True,
                "WALL_CORE_SIZE": "AUTO",
                "WALL_CORE_DIV_Z": 8,
                "WALL_CORE_DIV_Y": 8,
                "WALL_COVER_SIZE": "AUTO",
                "WALL_COVER_DIV_Z": 8,
                "WALL_COVER_DIV_Y": 1,
                "SHEAR_R": 0.4,
                "bASSIGNBYMEMBER": True,
                "bTRI_SYM": True,
                "TRI_TENS_A1": 0.1,
                "TRI_TENS_A2": 0.05,
                "TRI_COMP_A1": 0.1,
                "TRI_COMP_A2": 0.05,
                "bBI_SYM": True,
                "BI_TENS_A1": 0.05,
                "BI_COMP_A1": 0.05,
                "PSPR_APPLY_TYPE": "ASSUME",
                "ELNK_APPLY_TYPE": "APPLY",
                "bUSEAUTOCALCREFERENCE": True,
                "RCDGNCODE": "KISTEC2019",
                "LOC_BEAM": "M",
                "LOC_COLUMN": "I",
                "SF_WALL": 1.6,
                "bSF_BRITTLE": False,
                "SF_BRITTLE": 1.6,
                "bSF_EARTHQUAKE": False,
                "SF_EARTHQUAKE": 0.85,
                "bSF_SMOOTH_BAR": False,
                "SF_SMOOTH_BAR": 0.575,
                "CONFIDENCE": 1,
                "bBUCKLING": True,
                "bCALCAXIALFORCE": True
            },
            "NODECONNECTIVITY": "PINNED",
            "bSHOWGRAPHAFTER": True,
            "bSHOWGRAPGHDURING": False
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/POGD", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询推覆分析控制数据 ──────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/POGD", headers=HEADERS)
print("GET:", resp.json())
```

---

## 2. `/db/POGD-M1` — Pushover Global Control (Hyper-S)

> **功能：** 定义 Hyper-S(MEC) 求解器专用 Pushover(静力非线性抗震性能评估)分析的全局控制选项。可设置几何非线性类型、初始荷载处理、分析中止条件、迭代(Iteration)控制、铰(Hinge)选项、图形显示选项等。

### Input URI

```
{base url}/db/POGD-M1
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
      "description": "Keys are string indices (e.g. \"1\"); each value is a Pushover Global Control settings object.",
      "minProperties": 1,
      "additionalProperties": {
        "type": "object",
        "unevaluatedProperties": false,
        "required": [
          "GEO_NONL_TYPE",
          "INIT_LOAD_TYPE",
          "ITER_CTRL"
        ],
        "allOf": [
          {
            "type": "object",
            "properties": {
              "GEO_NONL_TYPE": {
                "type": "integer",
                "enum": [0, 1, 2],
                "description": "None / P-Delta / Large Displacements"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "INIT_LOAD_TYPE": {
                "type": "integer",
                "enum": [0, 1],
                "description": "Perform Nonlinear Static Analysis for Initial Load / Import Static Analysis / Construction Stage Analysis Results"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "INIT_LOAD_LIST": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": ["LC_NAME", "LC_TYPE", "SF"],
                  "properties": {
                    "LC_NAME": {
                      "type": "string",
                      "minLength": 1,
                      "description": "Load Case / Scale Factor / 목록"
                    },
                    "LC_TYPE": {
                      "type": "string",
                      "enum": ["STATIC", "STAGE"],
                      "description": "Load Case / Scale Factor / 목록"
                    },
                    "SF": {
                      "type": "number",
                      "not": { "const": 0 },
                      "description": "Load Case / Scale Factor / 목록"
                    }
                  }
                },
                "description": "Load Case / Scale Factor / 목록 (각 엔트리 {LC_NAME, LC_TYPE, SF}. LC_TYPE='STATIC' 또는 'STAGE')"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "IGNORE_ELEM": {
                "type": "boolean",
                "description": "Consider 'Ignore Elements for Initial Load'"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "ANALYSIS_STOP": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "SHEAR_YIELD": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
                      },
                      "BEAM_COLUMN": { "type": "boolean", "description": "Beam/Column" },
                      "WALL": { "type": "boolean", "description": "Wall" }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is true, at least one of BEAM_COLUMN or WALL must be true.",
                        "if": {
                          "properties": { "OPT_USE": { "const": true } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "anyOf": [
                            { "properties": { "BEAM_COLUMN": { "const": true } }, "required": ["BEAM_COLUMN"] },
                            { "properties": { "WALL": { "const": true } }, "required": ["WALL"] }
                          ]
                        }
                      },
                      {
                        "description": "If OPT_USE is false, BEAM_COLUMN and WALL must not be provided.",
                        "if": {
                          "properties": { "OPT_USE": { "const": false } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["BEAM_COLUMN"] },
                              { "required": ["WALL"] }
                            ]
                          }
                        }
                      }
                    ]
                  },
                  "AXIAL_YIELD": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
                      },
                      "BEAM": { "type": "boolean", "description": "Beam" },
                      "WALL": { "type": "boolean", "description": "Wall" },
                      "TRUSS": { "type": "boolean", "description": "Truss" }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is true, at least one of BEAM, WALL, or TRUSS must be true.",
                        "if": {
                          "properties": { "OPT_USE": { "const": true } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "anyOf": [
                            { "properties": { "BEAM": { "const": true } }, "required": ["BEAM"] },
                            { "properties": { "WALL": { "const": true } }, "required": ["WALL"] },
                            { "properties": { "TRUSS": { "const": true } }, "required": ["TRUSS"] }
                          ]
                        }
                      },
                      {
                        "description": "If OPT_USE is false, BEAM, WALL, and TRUSS must not be provided.",
                        "if": {
                          "properties": { "OPT_USE": { "const": false } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["BEAM"] },
                              { "required": ["WALL"] },
                              { "required": ["TRUSS"] }
                            ]
                          }
                        }
                      }
                    ]
                  },
                  "SUPPORT_DZ_DIR": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
                      },
                      "UPLIFT": { "type": "boolean", "description": "Uplift" },
                      "COLLAPSE": { "type": "boolean", "description": "Collapse" }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is true, at least one of UPLIFT or COLLAPSE must be true.",
                        "if": {
                          "properties": { "OPT_USE": { "const": true } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "anyOf": [
                            { "properties": { "UPLIFT": { "const": true } }, "required": ["UPLIFT"] },
                            { "properties": { "COLLAPSE": { "const": true } }, "required": ["COLLAPSE"] }
                          ]
                        }
                      },
                      {
                        "description": "If OPT_USE is false, UPLIFT and COLLAPSE must not be provided.",
                        "if": {
                          "properties": { "OPT_USE": { "const": false } },
                          "required": ["OPT_USE"]
                        },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["UPLIFT"] },
                              { "required": ["COLLAPSE"] }
                            ]
                          }
                        }
                      }
                    ]
                  }
                },
                "description": "Shear Component Yield / Axial Component Collapse / Support Uplifting-Collapse"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "ITER_CTRL": {
                "type": "object",
                "additionalProperties": false,
                "required": ["MAX_ITER", "NORM_CTRL", "STIFF_UPD_SCHEME"],
                "properties": {
                  "PERMIT_FAIL": {
                    "type": "boolean",
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "MAX_ITER": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "NORM_CTRL": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["DISP", "FORCE", "ENERGY"],
                    "properties": {
                      "DISP": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": ["OPT_USE"],
                        "properties": {
                          "OPT_USE": { "type": "boolean", "description": "Norm option on/off" },
                          "VALUE": { "type": "number", "exclusiveMinimum": 0, "description": "Norm tolerance value" }
                        },
                        "allOf": [
                          {
                            "description": "If OPT_USE is true, VALUE is required.",
                            "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                            "then": { "required": ["VALUE"] }
                          },
                          {
                            "description": "If OPT_USE is false, VALUE must not be provided.",
                            "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                            "then": { "not": { "required": ["VALUE"] } }
                          }
                        ],
                        "description": "Displacement norm"
                      },
                      "FORCE": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": ["OPT_USE"],
                        "properties": {
                          "OPT_USE": { "type": "boolean", "description": "Norm option on/off" },
                          "VALUE": { "type": "number", "exclusiveMinimum": 0, "description": "Norm tolerance value" }
                        },
                        "allOf": [
                          {
                            "description": "If OPT_USE is true, VALUE is required.",
                            "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                            "then": { "required": ["VALUE"] }
                          },
                          {
                            "description": "If OPT_USE is false, VALUE must not be provided.",
                            "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                            "then": { "not": { "required": ["VALUE"] } }
                          }
                        ],
                        "description": "Force norm"
                      },
                      "ENERGY": {
                        "type": "object",
                        "additionalProperties": false,
                        "required": ["OPT_USE"],
                        "properties": {
                          "OPT_USE": { "type": "boolean", "description": "Norm option on/off" },
                          "VALUE": { "type": "number", "exclusiveMinimum": 0, "description": "Norm tolerance value" }
                        },
                        "allOf": [
                          {
                            "description": "If OPT_USE is true, VALUE is required.",
                            "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                            "then": { "required": ["VALUE"] }
                          },
                          {
                            "description": "If OPT_USE is false, VALUE must not be provided.",
                            "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                            "then": { "not": { "required": ["VALUE"] } }
                          }
                        ],
                        "description": "Energy norm"
                      }
                    },
                    "anyOf": [
                      { "properties": { "DISP": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] } } },
                      { "properties": { "FORCE": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] } } },
                      { "properties": { "ENERGY": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] } } }
                    ],
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "STIFF_UPD_SCHEME": {
                    "type": "integer",
                    "enum": [0, 1, 2],
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "ITER_BEF_UPDATE": {
                    "type": "integer",
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "MAX_BISECT_LEVEL": {
                    "type": "integer",
                    "default": 5,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "SMART_BISECT": {
                    "type": "boolean",
                    "default": false,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "DIVERGENCE_THRESHOLD": {
                    "type": "number",
                    "default": 3,
                    "description": "Permit Convergence Failure / Maximum Iteration / Norm 3종 / Stiffness Update / Bisection / Divergence"
                  },
                  "LINE_SEARCH": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["OPT_USE"],
                    "properties": {
                      "OPT_USE": {
                        "type": "boolean",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "LINE_SEARCH_OPT": {
                        "type": "string",
                        "enum": ["AUTO", "USER"],
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "START_ITER_NO": {
                        "type": "integer",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "MAX_LINE_SEARCH_ITER": {
                        "type": "integer",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      },
                      "LINE_SEARCH_TOL": {
                        "type": "number",
                        "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                      }
                    },
                    "allOf": [
                      {
                        "description": "If OPT_USE is false, LINE_SEARCH detail fields must not be provided.",
                        "if": { "properties": { "OPT_USE": { "const": false } }, "required": ["OPT_USE"] },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["LINE_SEARCH_OPT"] },
                              { "required": ["START_ITER_NO"] },
                              { "required": ["MAX_LINE_SEARCH_ITER"] },
                              { "required": ["LINE_SEARCH_TOL"] }
                            ]
                          }
                        }
                      },
                      {
                        "description": "If OPT_USE is true, LINE_SEARCH_OPT is required.",
                        "if": { "properties": { "OPT_USE": { "const": true } }, "required": ["OPT_USE"] },
                        "then": { "required": ["LINE_SEARCH_OPT"] }
                      },
                      {
                        "description": "If LINE_SEARCH_OPT is AUTO, START_ITER_NO, MAX_LINE_SEARCH_ITER, and LINE_SEARCH_TOL must not be provided.",
                        "if": { "properties": { "LINE_SEARCH_OPT": { "const": "AUTO" } }, "required": ["LINE_SEARCH_OPT"] },
                        "then": {
                          "not": {
                            "anyOf": [
                              { "required": ["START_ITER_NO"] },
                              { "required": ["MAX_LINE_SEARCH_ITER"] },
                              { "required": ["LINE_SEARCH_TOL"] }
                            ]
                          }
                        }
                      },
                      {
                        "description": "If LINE_SEARCH_OPT is USER, START_ITER_NO, MAX_LINE_SEARCH_ITER, and LINE_SEARCH_TOL are required.",
                        "if": { "properties": { "LINE_SEARCH_OPT": { "const": "USER" } }, "required": ["LINE_SEARCH_OPT"] },
                        "then": { "required": ["START_ITER_NO", "MAX_LINE_SEARCH_ITER", "LINE_SEARCH_TOL"] }
                      }
                    ],
                    "description": "Enable Line Search / Auto·User / Max Line Search Iter / Tol"
                  }
                },
                "allOf": [
                  {
                    "description": "If STIFF_UPD_SCHEME is 0, ITER_BEF_UPDATE is required.",
                    "if": { "properties": { "STIFF_UPD_SCHEME": { "const": 0 } }, "required": ["STIFF_UPD_SCHEME"] },
                    "then": { "required": ["ITER_BEF_UPDATE"] }
                  },
                  {
                    "description": "If STIFF_UPD_SCHEME is 1 or 2, ITER_BEF_UPDATE must not be provided.",
                    "if": { "properties": { "STIFF_UPD_SCHEME": { "enum": [1, 2] } }, "required": ["STIFF_UPD_SCHEME"] },
                    "then": { "not": { "required": ["ITER_BEF_UPDATE"] } }
                  }
                ],
                "description": "(복합) (세부 필드는 서브 §4 Iteration Control 과 중복 — 메인 대화상자에서 접근 가능)"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "PO_HINGE_OPT": {
                "type": "object",
                "additionalProperties": false,
                "required": ["ASSIGN_BY_MEMBER", "NONL_TYPE", "TRILINEAR", "BILINEAR", "LOC_BEAM", "CALC_YIELDS"],
                "properties": {
                  "ASSIGN_BY_MEMBER": {
                    "type": "boolean",
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "NONL_TYPE": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["PSPRING_SUP", "EL"],
                    "properties": {
                      "PSPRING_SUP": { "type": "integer", "enum": [0, 1], "description": "Apply nonlinear / Linear" },
                      "EL": { "type": "integer", "enum": [0, 1], "description": "Apply nonlinear / Linear" }
                    },
                    "description": "Apply nonlinear / Linear"
                  },
                  "TRILINEAR": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["TENS_A1", "TENS_A2", "COMP_A1", "COMP_A2", "SYMMETRIC"],
                    "properties": {
                      "TENS_A1": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "TENS_A2": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "COMP_A1": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "COMP_A2": { "type": "number", "description": "Trilinear default stiffness reduction" },
                      "SYMMETRIC": { "type": "boolean", "description": "Trilinear default stiffness reduction" }
                    },
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "BILINEAR": {
                    "type": "object",
                    "additionalProperties": false,
                    "required": ["TENS_A1", "COMP_A1", "SYMMETRIC"],
                    "properties": {
                      "TENS_A1": { "type": "number", "description": "Bilinear default stiffness reduction" },
                      "COMP_A1": { "type": "number", "description": "Bilinear default stiffness reduction" },
                      "SYMMETRIC": { "type": "boolean", "description": "Bilinear default stiffness reduction" }
                    },
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "LOC_BEAM": {
                    "type": "integer",
                    "enum": [0, 1, 2],
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  },
                  "CALC_YIELDS": {
                    "type": "boolean",
                    "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
                  }
                },
                "description": "Hinge Property 옵션 그룹 (TRILINEAR/BILINEAR 강성 저감, LOC_BEAM (I/Mid/J), CALC_YIELDS (Buckling))"
              }
            }
          },
          {
            "type": "object",
            "properties": {
              "MISC": {
                "type": "object",
                "additionalProperties": false,
                "required": ["SHOW_GRAPH_AFTER", "SHOW_GRAPH_DURING"],
                "properties": {
                  "SHOW_GRAPH_AFTER": { "type": "boolean", "description": "Show Pushover Curve Result After Analysis" },
                  "SHOW_GRAPH_DURING": { "type": "boolean", "description": "Show Pushover Curve during Analyzing" }
                },
                "description": "Pushover Misc Options"
              }
            }
          },
          {
            "description": "If GEO_NONL_TYPE is Large Displacements or P-Delta, INIT_LOAD_TYPE must be 0.",
            "if": {
              "properties": { "GEO_NONL_TYPE": { "enum": [1, 2] } },
              "required": ["GEO_NONL_TYPE"]
            },
            "then": { "properties": { "INIT_LOAD_TYPE": { "const": 0 } } }
          },
          {
            "description": "If INIT_LOAD_TYPE is 1, IGNORE_ELEM must not be provided.",
            "if": {
              "properties": { "INIT_LOAD_TYPE": { "const": 1 } },
              "required": ["INIT_LOAD_TYPE"]
            },
            "then": { "not": { "required": ["IGNORE_ELEM"] } }
          }
        ]
      }
    }
  }
}
```

### Parameters

在 `Assign` 对象下以 `"1"`、`"2"` 等字符串索引为键，定义各项 Pushover Global Control 设置。

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 几何非线性类型 (None: 0 / Large Displacements: 1 / P-Delta: 2)。GEO_NONL_TYPE 为 1 或 2 时，INIT_LOAD_TYPE 必须为 0 | `GEO_NONL_TYPE` | integer (enum) | - | 必填 |
| 2 | 初始荷载类型 (执行非线性静力分析: 0 / 导入静力·施工阶段分析结果: 1) | `INIT_LOAD_TYPE` | integer (enum) | - | 必填 |
| 3 | 初始荷载工况列表 (INIT_LOAD_TYPE=1 时不可指定 IGNORE_ELEM) | `INIT_LOAD_LIST` | array [object] | - | 可选 |
| 3-1 | └ 荷载工况名称 (长度 ≥1) | `INIT_LOAD_LIST[].LC_NAME` | string | - | 必填 (使用数组时) |
| 3-2 | └ 荷载工况类型 (Static: STATIC / Stage: STAGE) | `INIT_LOAD_LIST[].LC_TYPE` | string (enum) | - | 必填 (使用数组时) |
| 3-3 | └ 比例系数(Scale Factor)，不可为 0 | `INIT_LOAD_LIST[].SF` | number | - | 必填 (使用数组时) |
| 4 | 计算初始荷载时忽略单元选项 (Ignore Elements for Initial Load)。INIT_LOAD_TYPE=1 时不可提供 | `IGNORE_ELEM` | boolean | - | 可选 |
| 5 | 分析中止(Analysis Stop)条件分组 | `ANALYSIS_STOP` | object | - | 可选 |
| 5-1 | └ 剪切分量屈服(Shear Component Yield) | `ANALYSIS_STOP.SHEAR_YIELD` | object | - | 可选 |
| 5-1-a | 　　└ 是否使用 | `ANALYSIS_STOP.SHEAR_YIELD.OPT_USE` | boolean | - | 必填。为 true 时 BEAM_COLUMN/WALL 中至少 1 个为 true，为 false 时两者均不填 |
| 5-1-b | 　　└ Beam/Column | `ANALYSIS_STOP.SHEAR_YIELD.BEAM_COLUMN` | boolean | - | 可选 |
| 5-1-c | 　　└ Wall | `ANALYSIS_STOP.SHEAR_YIELD.WALL` | boolean | - | 可选 |
| 5-2 | └ 轴向分量破坏/屈曲(Axial Component Collapse) | `ANALYSIS_STOP.AXIAL_YIELD` | object | - | 可选 |
| 5-2-a | 　　└ 是否使用 | `ANALYSIS_STOP.AXIAL_YIELD.OPT_USE` | boolean | - | 必填。为 true 时 BEAM/WALL/TRUSS 中至少 1 个为 true，为 false 时均不填 |
| 5-2-b | 　　└ Beam | `ANALYSIS_STOP.AXIAL_YIELD.BEAM` | boolean | - | 可选 |
| 5-2-c | 　　└ Wall | `ANALYSIS_STOP.AXIAL_YIELD.WALL` | boolean | - | 可选 |
| 5-2-d | 　　└ Truss | `ANALYSIS_STOP.AXIAL_YIELD.TRUSS` | boolean | - | 可选 |
| 5-3 | └ 支座抬起/破坏 : Dz 方向(Support Uplifting/Collapse) | `ANALYSIS_STOP.SUPPORT_DZ_DIR` | object | - | 可选 |
| 5-3-a | 　　└ 是否使用 | `ANALYSIS_STOP.SUPPORT_DZ_DIR.OPT_USE` | boolean | - | 必填。为 true 时 UPLIFT/COLLAPSE 中至少 1 个为 true，为 false 时两者均不填 |
| 5-3-b | 　　└ Uplift | `ANALYSIS_STOP.SUPPORT_DZ_DIR.UPLIFT` | boolean | - | 可选 |
| 5-3-c | 　　└ Collapse | `ANALYSIS_STOP.SUPPORT_DZ_DIR.COLLAPSE` | boolean | - | 可选 |
| 6 | 迭代控制(Iteration Controls) | `ITER_CTRL` | object | - | 必填 |
| 6-1 | └ 允许收敛失败(Permit Convergence Failure) | `ITER_CTRL.PERMIT_FAIL` | boolean | - | 可选 |
| 6-2 | └ 最大迭代次数(Maximum Iteration)，≥1 | `ITER_CTRL.MAX_ITER` | integer | - | 必填 |
| 6-3 | └ 收敛准则(Convergence Criteria) | `ITER_CTRL.NORM_CTRL` | object | - | 必填。DISP/FORCE/ENERGY 中至少 1 个 OPT_USE=true |
| 6-3-a | 　　└ 位移范数(Displacement norm) | `ITER_CTRL.NORM_CTRL.DISP` | object | - | 必填 |
| 6-3-a-i | 　　　　└ 是否使用 | `ITER_CTRL.NORM_CTRL.DISP.OPT_USE` | boolean | - | 必填 |
| 6-3-a-ii | 　　　　└ 容差值 (>0)。DISP.OPT_USE=true 时必填，false 时不可提供 | `ITER_CTRL.NORM_CTRL.DISP.VALUE` | number | - | 条件必填 |
| 6-3-b | 　　└ 荷载范数(Force norm) | `ITER_CTRL.NORM_CTRL.FORCE` | object | - | 必填 |
| 6-3-b-i | 　　　　└ 是否使用 | `ITER_CTRL.NORM_CTRL.FORCE.OPT_USE` | boolean | - | 必填 |
| 6-3-b-ii | 　　　　└ 容差值 (>0)。FORCE.OPT_USE=true 时必填，false 时不可提供 | `ITER_CTRL.NORM_CTRL.FORCE.VALUE` | number | - | 条件必填 |
| 6-3-c | 　　└ 能量范数(Energy norm) | `ITER_CTRL.NORM_CTRL.ENERGY` | object | - | 必填 |
| 6-3-c-i | 　　　　└ 是否使用 | `ITER_CTRL.NORM_CTRL.ENERGY.OPT_USE` | boolean | - | 必填 |
| 6-3-c-ii | 　　　　└ 容差值 (>0)。ENERGY.OPT_USE=true 时必填，false 时不可提供 | `ITER_CTRL.NORM_CTRL.ENERGY.VALUE` | number | - | 条件必填 |
| 6-4 | └ 刚度更新方式 (Custom: 0 / Full Newton-Raphson: 1 / Initial Stiffness: 2) | `ITER_CTRL.STIFF_UPD_SCHEME` | integer (enum) | - | 必填 |
| 6-5 | └ 刚度更新前的迭代次数。STIFF_UPD_SCHEME=0 时必填，为 1·2 时不可提供 | `ITER_CTRL.ITER_BEF_UPDATE` | integer | - | 条件必填 |
| 6-6 | └ 最大二分法(Bisection)层级 | `ITER_CTRL.MAX_BISECT_LEVEL` | integer | 5 | 可选 |
| 6-7 | └ 是否使用 Smart Bisection | `ITER_CTRL.SMART_BISECT` | boolean | false | 可选 |
| 6-8 | └ 发散阈值(Divergence Threshold) | `ITER_CTRL.DIVERGENCE_THRESHOLD` | number | 3 | 可选 |
| 6-9 | └ 是否使用 Line Search | `ITER_CTRL.LINE_SEARCH` | object | - | 可选 |
| 6-9-a | 　　└ 是否使用。false 时全部明细字段均不可提供，true 时 LINE_SEARCH_OPT 必填 | `ITER_CTRL.LINE_SEARCH.OPT_USE` | boolean | - | 必填 |
| 6-9-b | 　　└ Line Search 选项 (Auto: AUTO / User: USER)。AUTO 时明细值不可提供，USER 时明细值全部必填 | `ITER_CTRL.LINE_SEARCH.LINE_SEARCH_OPT` | string (enum) | - | 条件必填 |
| 6-9-c | 　　└ Line Search 起始迭代次数 (USER 时必填) | `ITER_CTRL.LINE_SEARCH.START_ITER_NO` | integer | - | 条件必填 |
| 6-9-d | 　　└ 每次迭代的最大 Line Search 次数 (USER 时必填) | `ITER_CTRL.LINE_SEARCH.MAX_LINE_SEARCH_ITER` | integer | - | 条件必填 |
| 6-9-e | 　　└ Line Search 容差 (USER 时必填) | `ITER_CTRL.LINE_SEARCH.LINE_SEARCH_TOL` | number | - | 条件必填 |
| 7 | Pushover 铰数据选项 | `PO_HINGE_OPT` | object | - | 可选 |
| 7-1 | └ 仅对构件指定铰属性 | `PO_HINGE_OPT.ASSIGN_BY_MEMBER` | boolean | - | 必填 |
| 7-2 | └ Skeleton Curve 默认刚度折减比 (Trilinear) | `PO_HINGE_OPT.TRILINEAR` | object | - | 必填 |
| 7-2-a | 　　└ α1 (+) | `PO_HINGE_OPT.TRILINEAR.TENS_A1` | number | - | 必填 |
| 7-2-b | 　　└ α2 (+) | `PO_HINGE_OPT.TRILINEAR.TENS_A2` | number | - | 必填 |
| 7-2-c | 　　└ α1 (-) | `PO_HINGE_OPT.TRILINEAR.COMP_A1` | number | - | 必填 |
| 7-2-d | 　　└ α2 (-) | `PO_HINGE_OPT.TRILINEAR.COMP_A2` | number | - | 必填 |
| 7-2-e | 　　└ 是否对称(SYMMETRIC) | `PO_HINGE_OPT.TRILINEAR.SYMMETRIC` | boolean | - | 必填 |
| 7-3 | └ 铰属性默认刚度折减比 (Bilinear) | `PO_HINGE_OPT.BILINEAR` | object | - | 必填 |
| 7-3-a | 　　└ α1 (+) | `PO_HINGE_OPT.BILINEAR.TENS_A1` | number | - | 必填 |
| 7-3-b | 　　└ α1 (-) | `PO_HINGE_OPT.BILINEAR.COMP_A1` | number | - | 必填 |
| 7-3-c | 　　└ 是否对称(SYMMETRIC) | `PO_HINGE_OPT.BILINEAR.SYMMETRIC` | boolean | - | 必填 |
| 7-4 | └ 点弹簧支承 & 弹性连接非线性类型 | `PO_HINGE_OPT.NONL_TYPE` | object | - | 必填 |
| 7-4-a | 　　└ 点弹簧支承应用方式 (Apply Nonlinear: 0 / Linear: 1) | `PO_HINGE_OPT.NONL_TYPE.PSPRING_SUP` | integer (enum) | - | 必填 |
| 7-4-b | 　　└ 弹性连接应用方式 (Apply Nonlinear: 0 / Linear: 1) | `PO_HINGE_OPT.NONL_TYPE.EL` | integer (enum) | - | 必填 |
| 7-5 | └ 分布铰基准位置 (I-End: 0 / Mid-span: 1 / J-End: 2) | `PO_HINGE_OPT.LOC_BEAM` | integer (enum) | - | 必填 |
| 7-6 | └ 考虑屈曲的 Beam 屈服面计算 | `PO_HINGE_OPT.CALC_YIELDS` | boolean | - | 必填 |
| 8 | Pushover 其他(Misc)选项 | `MISC` | object | - | 可选 |
| 8-1 | └ 分析后显示 Pushover 曲线结果 | `MISC.SHOW_GRAPH_AFTER` | boolean | - | 必填 |
| 8-2 | └ 分析过程中显示 Pushover 曲线 | `MISC.SHOW_GRAPH_DURING` | boolean | - | 必填 |

> ⚠️ **2026-08-26 确认：** `GEO_NONL_TYPE` 的 enum 顺序此前误记为 None:0/P-Delta:1/Large
> Displacements:2。原文 JSON Schema 的 description 单词罗列顺序为
> "None / P-Delta / Large Displacements"，直接照此记录应为成因，但原文
> Specifications 表却明确按 None:0/**Large Displacements:1**/**P-Delta:2** 编
> 号（Schema 说明文字与表格互相矛盾——以表为准）。第 09 章 `/db/THGC-M1` 的同名字段
> `GEO_NONL_TYPE` 也是 0=None/1=Large Disp/2=P-Delta 的相同顺序，可交叉验证（article id
> `56511008007705`）。

### Request / Response JSON

**PUT Request Body**
```json
{
  "Assign": {
    "1": {
      "GEO_NONL_TYPE": 0,
      "INIT_LOAD_TYPE": 0,
      "INIT_LOAD_LIST": [
        { "LC_NAME": "DL", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "LL", "LC_TYPE": "STATIC", "SF": 0.25 },
        { "LC_NAME": "EQX", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "EQY", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "STAGE_FINAL", "LC_TYPE": "STAGE", "SF": 1 }
      ],
      "IGNORE_ELEM": true,
      "ANALYSIS_STOP": {
        "SHEAR_YIELD": { "OPT_USE": true, "BEAM_COLUMN": true, "WALL": true },
        "AXIAL_YIELD": { "OPT_USE": true, "BEAM": true, "WALL": true, "TRUSS": true },
        "SUPPORT_DZ_DIR": { "OPT_USE": true, "UPLIFT": true, "COLLAPSE": true }
      },
      "ITER_CTRL": {
        "PERMIT_FAIL": false,
        "MAX_ITER": 30,
        "NORM_CTRL": {
          "DISP": { "OPT_USE": true, "VALUE": 0.001 },
          "FORCE": { "OPT_USE": true, "VALUE": 0.001 },
          "ENERGY": { "OPT_USE": true, "VALUE": 0.0001 }
        },
        "STIFF_UPD_SCHEME": 0,
        "ITER_BEF_UPDATE": 5,
        "MAX_BISECT_LEVEL": 8,
        "SMART_BISECT": true,
        "DIVERGENCE_THRESHOLD": 3,
        "LINE_SEARCH": {
          "OPT_USE": true,
          "LINE_SEARCH_OPT": "USER",
          "START_ITER_NO": 3,
          "MAX_LINE_SEARCH_ITER": 10,
          "LINE_SEARCH_TOL": 0.8
        }
      },
      "PO_HINGE_OPT": {
        "ASSIGN_BY_MEMBER": true,
        "NONL_TYPE": { "PSPRING_SUP": 1, "EL": 1 },
        "TRILINEAR": { "TENS_A1": 0.1, "TENS_A2": 0.05, "COMP_A1": 0.1, "COMP_A2": 0.05, "SYMMETRIC": true },
        "BILINEAR": { "TENS_A1": 0.1, "COMP_A1": 0.1, "SYMMETRIC": true },
        "LOC_BEAM": 0,
        "CALC_YIELDS": true
      },
      "MISC": {
        "SHOW_GRAPH_AFTER": true,
        "SHOW_GRAPH_DURING": true
      }
    }
  }
}
```

**GET Response Body**
```json
{
  "POGD-M1": {
    "1": {
      "GEO_NONL_TYPE": 0,
      "INIT_LOAD_TYPE": 0,
      "INIT_LOAD_LIST": [
        { "LC_NAME": "DL", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "LL", "LC_TYPE": "STATIC", "SF": 0.25 },
        { "LC_NAME": "EQX", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "EQY", "LC_TYPE": "STATIC", "SF": 1 },
        { "LC_NAME": "STAGE_FINAL", "LC_TYPE": "STAGE", "SF": 1 }
      ],
      "IGNORE_ELEM": true,
      "ANALYSIS_STOP": {
        "SHEAR_YIELD": { "OPT_USE": true, "BEAM_COLUMN": true, "WALL": true },
        "AXIAL_YIELD": { "OPT_USE": true, "BEAM": true, "WALL": true, "TRUSS": true },
        "SUPPORT_DZ_DIR": { "OPT_USE": true, "UPLIFT": true, "COLLAPSE": true }
      },
      "ITER_CTRL": {
        "PERMIT_FAIL": false,
        "MAX_ITER": 30,
        "NORM_CTRL": {
          "DISP": { "OPT_USE": true, "VALUE": 0.001 },
          "FORCE": { "OPT_USE": true, "VALUE": 0.001 },
          "ENERGY": { "OPT_USE": true, "VALUE": 0.0001 }
        },
        "STIFF_UPD_SCHEME": 0,
        "ITER_BEF_UPDATE": 5,
        "MAX_BISECT_LEVEL": 8,
        "SMART_BISECT": true,
        "DIVERGENCE_THRESHOLD": 3,
        "LINE_SEARCH": {
          "OPT_USE": true,
          "LINE_SEARCH_OPT": "USER",
          "START_ITER_NO": 3,
          "MAX_LINE_SEARCH_ITER": 10,
          "LINE_SEARCH_TOL": 0.8
        }
      },
      "PO_HINGE_OPT": {
        "ASSIGN_BY_MEMBER": true,
        "NONL_TYPE": { "PSPRING_SUP": 1, "EL": 1 },
        "TRILINEAR": { "TENS_A1": 0.1, "TENS_A2": 0.05, "COMP_A1": 0.1, "COMP_A2": 0.05, "SYMMETRIC": true },
        "BILINEAR": { "TENS_A1": 0.1, "COMP_A1": 0.1, "SYMMETRIC": true },
        "LOC_BEAM": 0,
        "CALC_YIELDS": true
      },
      "MISC": {
        "SHOW_GRAPH_AFTER": true,
        "SHOW_GRAPH_DURING": true
      }
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

# ── PUT: 注册/修改 Pushover Global Control(Hyper-S) ───────────────
def put_pushover_global_control():
    payload = {
        "Assign": {
            "1": {
                "GEO_NONL_TYPE": 0,       # None
                "INIT_LOAD_TYPE": 0,      # 以非线性静力分析计算初始荷载
                "INIT_LOAD_LIST": [
                    {"LC_NAME": "DL", "LC_TYPE": "STATIC", "SF": 1},
                    {"LC_NAME": "LL", "LC_TYPE": "STATIC", "SF": 0.25},
                    {"LC_NAME": "EQX", "LC_TYPE": "STATIC", "SF": 1},
                    {"LC_NAME": "EQY", "LC_TYPE": "STATIC", "SF": 1},
                    {"LC_NAME": "STAGE_FINAL", "LC_TYPE": "STAGE", "SF": 1}
                ],
                "IGNORE_ELEM": True,
                "ANALYSIS_STOP": {
                    "SHEAR_YIELD": {"OPT_USE": True, "BEAM_COLUMN": True, "WALL": True},
                    "AXIAL_YIELD": {"OPT_USE": True, "BEAM": True, "WALL": True, "TRUSS": True},
                    "SUPPORT_DZ_DIR": {"OPT_USE": True, "UPLIFT": True, "COLLAPSE": True}
                },
                "ITER_CTRL": {
                    "PERMIT_FAIL": False,
                    "MAX_ITER": 30,
                    "NORM_CTRL": {
                        "DISP": {"OPT_USE": True, "VALUE": 0.001},
                        "FORCE": {"OPT_USE": True, "VALUE": 0.001},
                        "ENERGY": {"OPT_USE": True, "VALUE": 0.0001}
                    },
                    "STIFF_UPD_SCHEME": 0,       # Custom -> ITER_BEF_UPDATE 必填
                    "ITER_BEF_UPDATE": 5,
                    "MAX_BISECT_LEVEL": 8,
                    "SMART_BISECT": True,
                    "DIVERGENCE_THRESHOLD": 3,
                    "LINE_SEARCH": {
                        "OPT_USE": True,
                        "LINE_SEARCH_OPT": "USER",   # USER -> 明细值必填
                        "START_ITER_NO": 3,
                        "MAX_LINE_SEARCH_ITER": 10,
                        "LINE_SEARCH_TOL": 0.8
                    }
                },
                "PO_HINGE_OPT": {
                    "ASSIGN_BY_MEMBER": True,
                    "NONL_TYPE": {"PSPRING_SUP": 1, "EL": 1},
                    "TRILINEAR": {"TENS_A1": 0.1, "TENS_A2": 0.05, "COMP_A1": 0.1, "COMP_A2": 0.05, "SYMMETRIC": True},
                    "BILINEAR": {"TENS_A1": 0.1, "COMP_A1": 0.1, "SYMMETRIC": True},
                    "LOC_BEAM": 0,
                    "CALC_YIELDS": True
                },
                "MISC": {
                    "SHOW_GRAPH_AFTER": True,
                    "SHOW_GRAPH_DURING": True
                }
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/POGD-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("PUT:", resp.status_code, resp.json())

# ── GET: 查询 Pushover Global Control(Hyper-S) ────────────────────
def get_pushover_global_control():
    resp = requests.get(f"{BASE_URL}/db/POGD-M1", headers=HEADERS)
    resp.raise_for_status()
    print("GET:", resp.json())

put_pushover_global_control()
get_pushover_global_control()
```

---

## 3. `/db/IEPI` — Ignore Elements for Pushover Initial Load

> **功能：** 指定非线性（推覆）分析计算初始荷载时忽略的单元。Assign Key 为单元 ID。

### Input URI

```
{base url}/db/IEPI
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "IEPI": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "B_IGNORE": { "description": "IgnoreElementsforNL.AnalysisInitialLoad", "type": "boolean" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 非线性分析初始荷载用单元是否忽略 | `"B_IGNORE"` | Boolean | `false` | Optional |

> **参考：** Assign Key 为**单元 ID**（不是序号）。

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "59": { "B_IGNORE": true },
    "60": { "B_IGNORE": true },
    "61": { "B_IGNORE": true },
    "62": { "B_IGNORE": true },
    "63": { "B_IGNORE": true },
    "64": { "B_IGNORE": true },
    "65": { "B_IGNORE": true },
    "66": { "B_IGNORE": true },
    "67": { "B_IGNORE": true },
    "68": { "B_IGNORE": true },
    "69": { "B_IGNORE": true },
    "70": { "B_IGNORE": true }
  }
}
```

**GET Response Body**

```json
{
  "IEPI": {
    "59": { "B_IGNORE": true },
    "60": { "B_IGNORE": true }
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

# ── POST: 指定特定单元在初始荷载计算中被忽略 ─────────────────────
ignore_elements = [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
payload = {
    "Assign": {
        str(elem_id): {"B_IGNORE": True} for elem_id in ignore_elements
    }
}
resp = requests.post(f"{BASE_URL}/db/IEPI", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询忽略单元列表 ───────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/IEPI", headers=HEADERS)
ignored = resp.json().get("IEPI", {})
print(f"被忽略的单元数: {len(ignored)}")
print(f"单元 ID 列表: {list(ignored.keys())}")

# ── DELETE: 从忽略列表中移除特定单元 ─────────────────────────
resp = requests.delete(f"{BASE_URL}/db/IEPI/59", headers=HEADERS)
print("DELETE:", resp.status_code)
```

---

## 4. `/db/PHGE` — Assign Pushover Hinge Properties

> **功能：** 为单元指派推覆分析铰属性。Assign Key 为指派序号，单元 ID（`ID`）与单元类型（`TYPE`）以独立字段指定。

### Input URI

```
{base url}/db/PHGE
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "PHGE": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "ID": { "description": "ID", "type": "integer" },
      "TYPE": { "description": "ElementType", "type": "string" },
      "HINGE_TYPE": { "description": "PushoverHingeType", "type": "string" },
      "FIBER_KEY": { "description": "FiberKey", "type": "integer" }
    }
  }
}
```

### Parameters

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|-----------|--------|------|
| 1 | 单元 ID | `"ID"` | Integer | — | **Required** |
| 2 | 单元类型 · Beam/Column: `"BEAM"` / Wall(⚠️ Gen NX 专用): `"WALL"` / Truss: `"TRUSS"` / General Link: `"G-LINK"` | `"TYPE"` | String | — | **Required** |
| 3 | 推覆分析铰类型 (例: `"Myz_15"`) | `"HINGE_TYPE"` | String | — | **Required** |
| 4 | 纤维键 | `"FIBER_KEY"` | Integer | — | **Required** |

> ⚠️ **2026-08-26 确认：** 原文中 `TYPE` 是限定为 `"BEAM"`/`"WALL"`/`"TRUSS"`/`"G-LINK"`
> 4 个值的 enum，且 `"WALL"` 在原文中带有 "MIDAS GEN NX only" 图标——此前文档以
> "例:" 的写法非限定列举，并遗漏了 `"G-LINK"`（article id `35992838417049`）。

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "15": {
      "ID": 1,
      "TYPE": "BEAM",
      "HINGE_TYPE": "Myz_15",
      "FIBER_KEY": 0
    }
  }
}
```

**GET Response Body**

```json
{
  "PHGE": {
    "15": {
      "ID": 1,
      "TYPE": "BEAM",
      "HINGE_TYPE": "Myz_15",
      "FIBER_KEY": 0
    }
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

# ── POST: 为单元指派推覆分析铰属性 ──────────────────────────
payload = {
    "Assign": {
        "15": {
            "ID": 1,
            "TYPE": "BEAM",
            "HINGE_TYPE": "Myz_15",
            "FIBER_KEY": 0
        },
        "16": {
            "ID": 2,
            "TYPE": "BEAM",
            "HINGE_TYPE": "Myz_15",
            "FIBER_KEY": 0
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/PHGE", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询已指派的铰属性 ─────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/PHGE", headers=HEADERS)
hinges = resp.json().get("PHGE", {})
for key, val in hinges.items():
    print(f"  [{key}] Element ID={val['ID']} ({val['TYPE']}) → {val['HINGE_TYPE']}")
```

---

## 5. `/db/POLC` — Pushover Load Cases

> **功能：** 定义推覆分析（静力非线性）荷载工况。可设置增量方法（荷载控制/位移控制）、分析停止条件、荷载模式（静力荷载/均匀加速度/振型/归一化振型）。

### Input URI

```
{base url}/db/POLC
```

### Active Methods

`POST` · `GET` · `PUT` · `DELETE`

### JSON Schema

```json
{
  "POLC": {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
      "LCNAME": { "description": "LoadCaseName", "type": "string" },
      "DESC": { "description": "Description", "type": "string" },
      "INCRE_STEP": { "description": "IncrementSteps", "type": "integer" },
      "bCONS_PDELTA": { "description": "ConsiderP-DeltaEffect", "type": "boolean" },
      "bUSEINITIAL": { "description": "UseInitialLoad", "type": "boolean" },
      "bREACOUTPUT": { "description": "CumulativeReaction/StoryShearbyInitialLoad", "type": "boolean" },
      "INCRE_METHOD": { "description": "IncrementMethod", "type": "string" },
      "STEPCTRLOPTION": { "description": "SteppingControlOption", "type": "string" },
      "INCFUNC_KEY": { "description": "IncrementalControlFunctionKey", "type": "integer" },
      "STIFF_RATIO": { "description": "AnalysisStoppingConditionCurrentStiffnessRatio", "type": "number" },
      "bLIMITDEFORMANGLE": { "description": "UseLimitInter-StoryDeformationAngle", "type": "boolean" },
      "LIMITDEFORMANGLE": { "description": "LimitInter-StoryDeformationAngle(1/[rad])", "type": "number" },
      "bDRIFTMAX": { "description": "MaximumDriftofAllVerticalElements", "type": "boolean" },
      "bDRIFTCENTER": { "description": "DriftattheCenterofFloorDiaphragm(StoryCenter)", "type": "boolean" },
      "bDRIFTAVER": { "description": "DriftcalculatedbyAverageDisplacementofStory", "type": "boolean" },
      "DISPCTRLOPTION": { "description": "DisplacementControlOption", "type": "string" },
      "GLOBAL_MAX_DISP": { "description": "GlobalMaxTranslationalDisplacement", "type": "number" },
      "MASTERNODE": { "description": "MasterNodeKey", "type": "integer" },
      "MASTERDIRECTION": { "description": "MasterNodeDirection", "type": "string" },
      "MASTERMAXDISP": { "description": "MasterNodeDisplacement", "type": "number" },
      "LOADPATTERNTYPE": { "description": "LoadPatternType", "type": "string" },
      "LOADPATTERN": {
        "description": "LoadPatternDataList",
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "LCNAME": { "description": "LoadCaseName(ifUsedLoadPattern=LOAD)", "type": "string" },
            "DIR": { "description": "Direction(ifUsedLoadPattern=ACC)", "type": "string" },
            "MODE": { "description": "ModeNumber(ifUsedLoadPattern=MODE,NOR_MODE)", "type": "integer" },
            "SF": { "description": "ScaleFactor", "type": "number" }
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
| 2 | 说明 | `"DESC"` | String | `""` | Optional |
| 3 | 增量步数 | `"INCRE_STEP"` | Integer | — | **Required** |
| 4 | 考虑 P-Delta 效应 | `"bCONS_PDELTA"` | Boolean | `false` | **Required** |
| 5 | 是否使用初始荷载 | `"bUSEINITIAL"` | Boolean | `false` | Optional |
| 6 | 输出初始荷载引起的累计反力/层剪力 | `"bREACOUTPUT"` | Boolean | `false` | Optional |
| 7 | 增量方法 · 荷载控制: `"LOAD"` / 位移控制: `"DISP"` | `"INCRE_METHOD"` | String | — | **Required** |
| 8 | 逐步控制选项（`INCRE_METHOD="LOAD"` 时）· 自动: `"AUTO"` / 等分(1/nstep): `"EQUAL"` / 增量控制函数: `"INC_FUNC"` | `"STEPCTRLOPTION"` | String | — | **Required** |
| 9 | 增量控制函数键 (`STEPCTRLOPTION="INC_FUNC"` 时) | `"INCFUNC_KEY"` | Integer | — | **Required** |
| 10 | 当前刚度比(Cs) (`INCRE_METHOD="LOAD"` 时) | `"STIFF_RATIO"` | Number | — | **Required** |
| 11 | 位移控制选项（`INCRE_METHOD="DISP"` 时）· 整体: `"GLOBAL"` / 主节点: `"NODE"` | `"DISPCTRLOPTION"` | String | — | **Required** |
| 12 | 最大平移位移(`DISPCTRLOPTION="GLOBAL"`) | `"GLOBAL_MAX_DISP"` | Number | — | **Required** |
| 13 | 主节点 ID(`DISPCTRLOPTION="NODE"`) | `"MASTERNODE"` | Integer | — | **Required** |
| 14 | 主节点方向 · `"DX"` / `"DY"` / `"DZ"` | `"MASTERDIRECTION"` | String | — | **Required** |
| 15 | 主节点最大位移 | `"MASTERMAXDISP"` | Number | — | **Required** |
| 16 | 启用层间变形角限制 | `"bLIMITDEFORMANGLE"` | Boolean | `false` | Optional |
| 17 | 层间变形角限制值 (1/[rad]) | `"LIMITDEFORMANGLE"` | Number | — | **Required** |
| 18 | 所有竖向构件的最大层间位移 | `"bDRIFTMAX"` | Boolean | `false` | Optional |
| 19 | 楼层隔板中心层间位移 | `"bDRIFTCENTER"` | Boolean | `false` | Optional |
| 20 | 按楼层平均位移计算的层间位移 | `"bDRIFTAVER"` | Boolean | `false` | Optional |
| 21 | 荷载模式类型 · 静力荷载: `"LOAD"` / 均匀加速度: `"ACC"` / 振型: `"MODE"` / 归一化振型×质量: `"NOR_MODE"` | `"LOADPATTERNTYPE"` | String | — | **Required** |
| 22 | 荷载模式列表 | `"LOADPATTERN"` | Array [Object] | — | **Required** |

**`LOADPATTERN` 数组项 – 按 `LOADPATTERNTYPE` 区分的字段**

| `LOADPATTERNTYPE` | 字段 | 说明 | 类型 |
|--------------------|------|------|------|
| `"LOAD"` (静力荷载工况) | `LCNAME` | 荷载工况名 | String |
| `"LOAD"` | `SF` | 缩放系数 | Number |
| `"ACC"` (均匀加速度) | `DIR` · `"DX"`/`"DY"`/`"DZ"` | 方向 | String |
| `"ACC"` | `SF` | 缩放系数 | Number |
| `"MODE"` / `"NOR_MODE"` (振型) | `MODE` | 振型编号 | Integer |
| `"MODE"` / `"NOR_MODE"` | `SF` | 缩放系数 | Number |

### Request / Response JSON

**POST / PUT Request Body**

```json
{
  "Assign": {
    "1": {
      "LCNAME": "Mode_X",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": true,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "DISP",
      "STEPCTRLOPTION": "AUTO",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "NODE",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 134,
      "MASTERDIRECTION": "DX",
      "MASTERMAXDISP": 1,
      "LOADPATTERNTYPE": "MODE",
      "LOADPATTERN": [
        { "MODE": 1, "SF": 1 }
      ]
    },
    "2": {
      "LCNAME": "Uni_X",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": false,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "LOAD",
      "STEPCTRLOPTION": "EQUAL",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "GLOBAL",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 0,
      "MASTERDIRECTION": "",
      "MASTERMAXDISP": 0,
      "LOADPATTERNTYPE": "ACC",
      "LOADPATTERN": [
        { "DIR": "DX", "SF": 1 }
      ]
    }
  }
}
```

**GET Response Body**

```json
{
  "POLC": {
    "1": {
      "LCNAME": "Mode_X",
      "INCRE_STEP": 10,
      "INCRE_METHOD": "DISP",
      "DISPCTRLOPTION": "NODE",
      "MASTERNODE": 134,
      "MASTERDIRECTION": "DX",
      "MASTERMAXDISP": 1,
      "LOADPATTERNTYPE": "MODE",
      "LOADPATTERN": [ { "MODE": 1, "SF": 1 } ]
    }
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

# ── POST: 创建 4 种推覆分析荷载工况 (振型 X/Y、均匀荷载 X/Y) ──
payload = {
    "Assign": {
        "1": {
            "LCNAME": "Mode_X", "DESC": "", "INCRE_STEP": 10,
            "bCONS_PDELTA": True, "bUSEINITIAL": False, "bREACOUTPUT": False,
            "INCRE_METHOD": "DISP", "STEPCTRLOPTION": "AUTO", "INCFUNC_KEY": 0,
            "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 10,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "NODE", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 134, "MASTERDIRECTION": "DX", "MASTERMAXDISP": 1,
            "LOADPATTERNTYPE": "MODE",
            "LOADPATTERN": [{"MODE": 1, "SF": 1}]
        },
        "2": {
            "LCNAME": "Mode_Y", "DESC": "", "INCRE_STEP": 10,
            "bCONS_PDELTA": True, "bUSEINITIAL": False, "bREACOUTPUT": False,
            "INCRE_METHOD": "DISP", "STEPCTRLOPTION": "AUTO", "INCFUNC_KEY": 0,
            "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 10,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "NODE", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 134, "MASTERDIRECTION": "DY", "MASTERMAXDISP": 1,
            "LOADPATTERNTYPE": "MODE",
            "LOADPATTERN": [{"MODE": 2, "SF": 1}]
        },
        "3": {
            "LCNAME": "Uni_X", "DESC": "", "INCRE_STEP": 10,
            "bCONS_PDELTA": False, "bUSEINITIAL": False, "bREACOUTPUT": False,
            "INCRE_METHOD": "LOAD", "STEPCTRLOPTION": "EQUAL", "INCFUNC_KEY": 0,
            "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 10,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "GLOBAL", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 0, "MASTERDIRECTION": "", "MASTERMAXDISP": 0,
            "LOADPATTERNTYPE": "ACC",
            "LOADPATTERN": [{"DIR": "DX", "SF": 1}]
        }
    }
}
resp = requests.post(f"{BASE_URL}/db/POLC", json=payload, headers=HEADERS)
print("POST:", resp.status_code, resp.json())

# ── GET: 查询荷载工况 ──────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/POLC", headers=HEADERS)
cases = resp.json().get("POLC", {})
for key, val in cases.items():
    print(f"  [{key}] {val['LCNAME']} | {val['INCRE_METHOD']} 控制 | 模式={val['LOADPATTERNTYPE']}")
```

---

## 6. `/db/POLC-M1` — Pushover Load Case (Hyper-S)

> **功能：** 定义用于 Hyper-S(MEC) 求解器专用 Pushover（静力非线性）分析的荷载工况（控制方式、增量阶段、荷载模式等）。

### Input URI

```
{base url}/db/POLC-M1
```

### Active Methods

`GET` · `PUT` · `DELETE`

> ⚠️ **2026-08-26 确认：** 原文 article 的 Active Methods 表标注为 `POST, GET, PUT, DELETE`
> （article id `56506753403673`），但本章其他所有 Hyper-S（`-M1`）端点以及章首提示
> （"Hyper-S 求解器专用端点不支持 POST"）都一致地以不支持 POST 为前提。究竟是原文复制
> 其他端点的模板时未作删减，还是确实只有该端点支持 POST，仅凭原文无法判断，因此在实际
> 操作确认之前保留 `GET`/`PUT`/`DELETE`。

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
      "description": "Keys are string indices; each value is a Pushover Load Case (Add/Modify) request item.",
      "minProperties": 1,
      "additionalProperties": {
        "type": "object",
        "unevaluatedProperties": false,
        "allOf": [
          {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "LCNAME",
              "INCRE_STEP",
              "NLTYPE",
              "bUSEINITIAL",
              "INCRE_METHOD",
              "CTRL_OPT",
              "LOADPATTERNTYPE",
              "LOADPATTERN"
            ],
            "properties": {
              "LCNAME": {
                "type": "string",
                "description": "Name (길이 1~20, 중복 불가)"
              },
              "DESC": {
                "type": "string",
                "default": "",
                "description": "Description (길이 ≤80)"
              },
              "INCRE_STEP": {
                "type": "integer",
                "minimum": 1,
                "description": "Increment Steps (nstep) (값 > 0. UI 기본 20)"
              },
              "NLTYPE": {
                "type": "string",
                "enum": ["NONE", "PDELTA", "LARGE"],
                "description": "None / P-Delta / Large Displacements (UI 3개 라디오가 단일 enum으로 병합)"
              },
              "bUSEINITIAL": {
                "type": "boolean",
                "description": "Use Initial Load (true일 때 bREACOUTPUT 필수)"
              },
              "bREACOUTPUT": {
                "type": "boolean",
                "description": "Cumulative Reaction / Story Shear (bUSEINITIAL == false 일 때 제공 시 오류)"
              },
              "INCRE_METHOD": {
                "type": "string",
                "enum": ["LOAD", "DISP"],
                "description": "Load Control / Displacement Control (UI 2개 라디오가 단일 enum으로 병합)"
              },
              "CTRL_OPT": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "STEPCTRLOPTION": {
                    "type": "string",
                    "enum": ["AUTO", "EQUAL", "INC_FUNC"],
                    "description": "Auto-Stepping Control (LOAD 분기)"
                  },
                  "INCFUNC_NAME": {
                    "type": "string",
                    "description": "Increment Function Name (POFC 이름 참조)"
                  },
                  "DISPCTRLOPTION": {
                    "type": "string",
                    "enum": ["GLOBAL", "NODE"],
                    "description": "Global / Master Node (DISP 분기)"
                  },
                  "GLOBAL_MAX_DISP": {
                    "type": "number",
                    "exclusiveMinimum": 0,
                    "description": "Max. Translational Displacement (값 > 0 필수)"
                  },
                  "MASTERNODE": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Node (ExistNode 통과 필요)"
                  },
                  "MASTERDIRECTION": {
                    "type": "string",
                    "enum": ["DX", "DY", "DZ"],
                    "description": "Direction"
                  },
                  "MASTERMAXDISP": {
                    "type": "number",
                    "not": { "const": 0 },
                    "description": "Max. Displacement (값 != 0.0 필수)"
                  },
                  "STIFF_RATIO": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 100,
                    "description": "Current Stiffness Ratio (Cs) ([0, 100] 범위)"
                  }
                },
                "allOf": [
                  {
                    "description": "When STEPCTRLOPTION = INC_FUNC, INCFUNC_NAME is required",
                    "if": { "properties": { "STEPCTRLOPTION": { "const": "INC_FUNC" } }, "required": ["STEPCTRLOPTION"] },
                    "then": { "required": ["INCFUNC_NAME"] }
                  },
                  {
                    "description": "When STEPCTRLOPTION = AUTO or EQUAL, INCFUNC_NAME must not be provided",
                    "if": { "properties": { "STEPCTRLOPTION": { "enum": ["AUTO", "EQUAL"] } }, "required": ["STEPCTRLOPTION"] },
                    "then": { "not": { "required": ["INCFUNC_NAME"] } }
                  },
                  {
                    "description": "When DISPCTRLOPTION = GLOBAL, GLOBAL_MAX_DISP is required and node-control fields must not be provided",
                    "if": { "properties": { "DISPCTRLOPTION": { "const": "GLOBAL" } }, "required": ["DISPCTRLOPTION"] },
                    "then": {
                      "required": ["GLOBAL_MAX_DISP"],
                      "not": {
                        "anyOf": [
                          { "required": ["MASTERNODE"] },
                          { "required": ["MASTERDIRECTION"] },
                          { "required": ["MASTERMAXDISP"] }
                        ]
                      }
                    }
                  },
                  {
                    "description": "When DISPCTRLOPTION = NODE, MASTERNODE, MASTERDIRECTION, and MASTERMAXDISP are required and GLOBAL_MAX_DISP must not be provided",
                    "if": { "properties": { "DISPCTRLOPTION": { "const": "NODE" } }, "required": ["DISPCTRLOPTION"] },
                    "then": {
                      "required": ["MASTERNODE", "MASTERDIRECTION", "MASTERMAXDISP"],
                      "not": { "required": ["GLOBAL_MAX_DISP"] }
                    }
                  }
                ],
                "description": "Control Option (INCRE_METHOD 분기 컨테이너)"
              },
              "LOADPATTERNTYPE": {
                "type": "string",
                "enum": ["LOAD", "ACC", "MODE", "NOR_MODE"],
                "description": "Load Type (배열 크기 제약: ACC/MODE/NOR_MODE는 배열 원소 1개만 허용)"
              },
              "LOADPATTERN": {
                "type": "array",
                "minItems": 1,
                "description": "Load Pattern 배열 (크기 ≥ 1)",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "LCNAME": {
                      "type": "string",
                      "description": "Load Case (ExistStld 통과 필요, Static Load Case 이름)"
                    },
                    "DIR": {
                      "type": "string",
                      "enum": ["DX", "DY", "DZ"],
                      "description": "Direction (Uniform Acceleration용)"
                    },
                    "MODE": {
                      "type": "integer",
                      "minimum": 1,
                      "description": "Mode (값 > 0. 1개 항목만 허용)"
                    },
                    "SF": {
                      "type": "number",
                      "not": { "const": 0 },
                      "description": "Scale Factor (값 != 0.0. UI 기본 1.0)"
                    }
                  }
                }
              }
            },
            "allOf": [
              {
                "description": "When bUSEINITIAL = true, bREACOUTPUT is required",
                "if": { "properties": { "bUSEINITIAL": { "const": true } }, "required": ["bUSEINITIAL"] },
                "then": { "required": ["bREACOUTPUT"] }
              },
              {
                "description": "When bUSEINITIAL = false, bREACOUTPUT must not be provided",
                "if": { "properties": { "bUSEINITIAL": { "const": false } }, "required": ["bUSEINITIAL"] },
                "then": { "not": { "required": ["bREACOUTPUT"] } }
              },
              {
                "description": "When INCRE_METHOD = LOAD, CTRL_OPT requires STEPCTRLOPTION and STIFF_RATIO and must not contain displacement-control fields",
                "if": { "properties": { "INCRE_METHOD": { "const": "LOAD" } }, "required": ["INCRE_METHOD"] },
                "then": {
                  "properties": {
                    "CTRL_OPT": {
                      "required": ["STEPCTRLOPTION", "STIFF_RATIO"],
                      "not": {
                        "anyOf": [
                          { "required": ["DISPCTRLOPTION"] },
                          { "required": ["GLOBAL_MAX_DISP"] },
                          { "required": ["MASTERNODE"] },
                          { "required": ["MASTERDIRECTION"] },
                          { "required": ["MASTERMAXDISP"] }
                        ]
                      }
                    }
                  }
                }
              },
              {
                "description": "When INCRE_METHOD = DISP, CTRL_OPT requires DISPCTRLOPTION and must not contain load-control fields",
                "if": { "properties": { "INCRE_METHOD": { "const": "DISP" } }, "required": ["INCRE_METHOD"] },
                "then": {
                  "properties": {
                    "CTRL_OPT": {
                      "required": ["DISPCTRLOPTION"],
                      "not": {
                        "anyOf": [
                          { "required": ["STEPCTRLOPTION"] },
                          { "required": ["INCFUNC_NAME"] },
                          { "required": ["STIFF_RATIO"] }
                        ]
                      }
                    }
                  }
                }
              },
              {
                "description": "When LOADPATTERNTYPE = LOAD, LOADPATTERN items must be load-case items (LCNAME + SF required; DIR, MODE forbidden)",
                "if": { "properties": { "LOADPATTERNTYPE": { "const": "LOAD" } }, "required": ["LOADPATTERNTYPE"] },
                "then": {
                  "properties": {
                    "LOADPATTERN": {
                      "items": {
                        "required": ["LCNAME", "SF"],
                        "not": { "anyOf": [ { "required": ["DIR"] }, { "required": ["MODE"] } ] }
                      }
                    }
                  }
                }
              },
              {
                "description": "When LOADPATTERNTYPE = ACC, LOADPATTERN must contain exactly one acceleration item (DIR + SF required; LCNAME, MODE forbidden)",
                "if": { "properties": { "LOADPATTERNTYPE": { "const": "ACC" } }, "required": ["LOADPATTERNTYPE"] },
                "then": {
                  "properties": {
                    "LOADPATTERN": {
                      "maxItems": 1,
                      "items": {
                        "required": ["DIR", "SF"],
                        "not": { "anyOf": [ { "required": ["LCNAME"] }, { "required": ["MODE"] } ] }
                      }
                    }
                  }
                }
              },
              {
                "description": "When LOADPATTERNTYPE = MODE or NOR_MODE, LOADPATTERN must contain exactly one mode item (MODE + SF required; LCNAME, DIR forbidden)",
                "if": { "properties": { "LOADPATTERNTYPE": { "enum": ["MODE", "NOR_MODE"] } }, "required": ["LOADPATTERNTYPE"] },
                "then": {
                  "properties": {
                    "LOADPATTERN": {
                      "maxItems": 1,
                      "items": {
                        "required": ["MODE", "SF"],
                        "not": { "anyOf": [ { "required": ["LCNAME"] }, { "required": ["DIR"] } ] }
                      }
                    }
                  }
                }
              }
            ]
          }
        ]
      }
    }
  }
}
```

> 参考：原始 Schema 把 `CTRL_OPT`/`LOADPATTERN` 的条件（`if`/`then`）规则，表达为在 `allOf` 之下配合 `unevaluatedProperties: false`、按各分支（LOAD/DISP、LOAD/ACC/MODE/NOR_MODE）重新声明全部字段的方式。上述 Schema 省略了字段定义的重复，只给出条件性 `required`/`not` 规则，实际字段列表·类型·enum 与上方 `CTRL_OPT`/`LOADPATTERN.items` 的定义相同。
>
> ⚠️ **2026-08-26 确认：** 原文 JSON Schema 把 `LOADPATTERN.items` 的 `DIR`·`MODE` 字段
> description 都误写成了 `"Load Case (...)"`（推测是复制粘贴了 `LCNAME` 的说明）。
> 上述 Schema 已按实际含义订正后收录（`DIR`="Direction (用于 Uniform Acceleration)"、
> `MODE`="Mode (值 > 0. 仅允许 1 个条目)")，下次同步时不要因为与原文不同就改回去
> （article id `56506753403673`）。同样的原因，`NLTYPE`/`INCRE_METHOD`/
> `DISPCTRLOPTION` 的 schema description 原文也有截断（例如 `NLTYPE` 只剩 "None"，
> "/ P-Delta / Large Displacements" 被漏掉），下表已按 Specifications 表补全为完整 enum。

### Parameters

在 `Assign` 对象下以 `"1"`、`"2"` 等字符串索引为键，定义各项 Pushover Load Case。

| No. | 说明 | Key | 值类型 | 默认值/enum | 必填 |
|-----|------|-----|-----------|-------------|------|
| 1 | 名称 (长度 1~20，不可重复) | `LCNAME` | string | - | 必填 |
| 2 | 说明 (长度 ≤80) | `DESC` | string | `""` | 可选 |
| 3 | 增量步数(nstep)，值 > 0 (UI 默认 20) | `INCRE_STEP` | integer | - | 必填 |
| 4 | 几何非线性类型 (None: NONE / P-Delta: PDELTA / Large Displacements: LARGE) | `NLTYPE` | string (enum) | - | 必填 |
| 5 | 是否使用初始荷载。true 时 bREACOUTPUT 必填，false 时不可提供 | `bUSEINITIAL` | boolean | - | 必填 |
| 6 | 初始荷载引起的累计反力/层剪力 (bUSEINITIAL=true 时必填) | `bREACOUTPUT` | boolean | - | 条件必填 |
| 7 | 增量方法 (Load Control: LOAD / Displacement Control: DISP) | `INCRE_METHOD` | string (enum) | - | 必填 |
| 8 | 控制选项容器 | `CTRL_OPT` | object | - | 必填 |
| **当 INCRE_METHOD = "LOAD" 时** (CTRL_OPT 内 DISP 系列字段不可提供) |
| 8-1 | └ 自动增量控制 (Auto-Stepping: AUTO / Equal Step: EQUAL / Incremental Control Function: INC_FUNC) | `CTRL_OPT.STEPCTRLOPTION` | string (enum) | - | 必填 |
| 8-2 | └ 增量函数名称 (STEPCTRLOPTION="INC_FUNC" 时必填，其他情况不可提供) | `CTRL_OPT.INCFUNC_NAME` | string | - | 条件必填 |
| 8-3 | └ 当前刚度比(Cs)，[0, 100] 范围 | `CTRL_OPT.STIFF_RATIO` | number | - | 必填 |
| **当 INCRE_METHOD = "DISP" 时** (CTRL_OPT 内 LOAD 系列字段不可提供) |
| 9-1 | └ 位移控制选项 (Global: GLOBAL / Master Node: NODE) | `CTRL_OPT.DISPCTRLOPTION` | string (enum) | - | 必填 |
| 9-2 | └ 最大平移位移(GLOBAL 时必填，值 > 0) | `CTRL_OPT.GLOBAL_MAX_DISP` | number | - | 条件必填 |
| 9-3 | └ 节点编号(NODE 时必填，需通过 ExistNode) | `CTRL_OPT.MASTERNODE` | integer | - | 条件必填 |
| 9-4 | └ 方向 (DX: DX / DY: DY / DZ: DZ) (NODE 时必填) | `CTRL_OPT.MASTERDIRECTION` | string (enum) | - | 条件必填 |
| 9-5 | └ 最大位移(NODE 时必填，值 != 0.0) | `CTRL_OPT.MASTERMAXDISP` | number | - | 条件必填 |
| 10 | 荷载模式类型 (静力荷载工况: LOAD / 均匀加速度: ACC / 振型: MODE / 归一化振型: NOR_MODE) | `LOADPATTERNTYPE` | string (enum) | - | 必填 |
| 11 | 荷载模式数组 (大小 ≥ 1; ACC/MODE/NOR_MODE 限定为 1 个元素) | `LOADPATTERN` | array [object] | - | 必填 |
| **当 LOADPATTERNTYPE = "LOAD" 时** (不可提供 DIR、MODE) |
| 11-1 | └ 荷载工况名称 (需通过 ExistStld，Static Load Case 名称) | `LOADPATTERN[].LCNAME` | string | - | 必填 |
| 11-2 | └ 比例系数(Scale Factor)，值 != 0.0 (UI 默认 1.0) | `LOADPATTERN[].SF` | number | - | 必填 |
| **当 LOADPATTERNTYPE = "ACC" 时** (数组元素恰好 1 个；不可提供 LCNAME、MODE) |
| 12-1 | └ 方向 (DX: DX / DY: DY / DZ: DZ) | `LOADPATTERN[].DIR` | string (enum) | - | 必填 |
| 12-2 | └ 比例系数(Scale Factor)，值 != 0.0 | `LOADPATTERN[].SF` | number | - | 必填 |
| **当 LOADPATTERNTYPE = "MODE" 或 "NOR_MODE" 时** (数组元素恰好 1 个；不可提供 LCNAME、DIR) |
| 13-1 | └ 振型编号，值 > 0 | `LOADPATTERN[].MODE` | integer | - | 必填 |
| 13-2 | └ 比例系数(Scale Factor)，值 != 0.0 | `LOADPATTERN[].SF` | number | - | 必填 |

### Request / Response JSON

**PUT Request Body — Increment Method: Load Control**
```json
{
  "Assign": {
    "1": {
      "LCNAME": "PUSH_LOAD_X",
      "DESC": "Pushover load control case in X direction",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "LOAD",
      "CTRL_OPT": {
        "STEPCTRLOPTION": "INC_FUNC",
        "INCFUNC_NAME": "POFC_01",
        "STIFF_RATIO": 80
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    }
  }
}
```

**PUT Request Body — Increment Method: Displacement Control**
```json
{
  "Assign": {
    "1": {
      "LCNAME": "PUSH_DISP_X",
      "DESC": "Pushover displacement control case using master node",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "DISP",
      "CTRL_OPT": {
        "DISPCTRLOPTION": "NODE",
        "MASTERNODE": 1001,
        "MASTERDIRECTION": "DX",
        "MASTERMAXDISP": 0.25
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    }
  }
}
```

**GET Response Body**
```json
{
  "POLC-M1": {
    "1": {
      "LCNAME": "PUSH_LOAD_X",
      "DESC": "Pushover load control case in X direction",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "LOAD",
      "CTRL_OPT": {
        "STEPCTRLOPTION": "INC_FUNC",
        "INCFUNC_NAME": "POFC_01",
        "STIFF_RATIO": 80
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
      ]
    },
    "2": {
      "LCNAME": "PUSH_DISP_X",
      "DESC": "Pushover displacement control case using master node",
      "INCRE_STEP": 20,
      "NLTYPE": "PDELTA",
      "bUSEINITIAL": true,
      "bREACOUTPUT": true,
      "INCRE_METHOD": "DISP",
      "CTRL_OPT": {
        "DISPCTRLOPTION": "NODE",
        "MASTERNODE": 1001,
        "MASTERDIRECTION": "DX",
        "MASTERMAXDISP": 0.25
      },
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        { "LCNAME": "DEAD", "SF": 1 },
        { "LCNAME": "LIVE", "SF": 0.5 }
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

# ── PUT: Pushover Load Case(Hyper-S) - Load Control 方式 ─────────
def put_pushover_load_case_load_control():
    payload = {
        "Assign": {
            "1": {
                "LCNAME": "PUSH_LOAD_X",
                "DESC": "Pushover load control case in X direction",
                "INCRE_STEP": 20,
                "NLTYPE": "PDELTA",
                "bUSEINITIAL": True,
                "bREACOUTPUT": True,          # bUSEINITIAL=True，故必填
                "INCRE_METHOD": "LOAD",
                "CTRL_OPT": {
                    "STEPCTRLOPTION": "INC_FUNC",   # INC_FUNC -> INCFUNC_NAME 必填
                    "INCFUNC_NAME": "POFC_01",
                    "STIFF_RATIO": 80
                },
                "LOADPATTERNTYPE": "LOAD",
                "LOADPATTERN": [
                    {"LCNAME": "DEAD", "SF": 1},
                    {"LCNAME": "LIVE", "SF": 0.5}
                ]
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/POLC-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("PUT (Load Control):", resp.status_code, resp.json())

# ── PUT: Pushover Load Case(Hyper-S) - Displacement Control 方式 ─
def put_pushover_load_case_disp_control():
    payload = {
        "Assign": {
            "2": {
                "LCNAME": "PUSH_DISP_X",
                "DESC": "Pushover displacement control case using master node",
                "INCRE_STEP": 20,
                "NLTYPE": "PDELTA",
                "bUSEINITIAL": True,
                "bREACOUTPUT": True,
                "INCRE_METHOD": "DISP",
                "CTRL_OPT": {
                    "DISPCTRLOPTION": "NODE",     # NODE -> MASTERNODE/DIRECTION/MAXDISP 必填
                    "MASTERNODE": 1001,
                    "MASTERDIRECTION": "DX",
                    "MASTERMAXDISP": 0.25
                },
                "LOADPATTERNTYPE": "LOAD",
                "LOADPATTERN": [
                    {"LCNAME": "DEAD", "SF": 1},
                    {"LCNAME": "LIVE", "SF": 0.5}
                ]
            }
        }
    }
    resp = requests.put(f"{BASE_URL}/db/POLC-M1", json=payload, headers=HEADERS)
    resp.raise_for_status()
    print("PUT (Displacement Control):", resp.status_code, resp.json())

# ── GET: 全量查询 Pushover Load Case(Hyper-S) ────────────────────
def get_pushover_load_case():
    resp = requests.get(f"{BASE_URL}/db/POLC-M1", headers=HEADERS)
    resp.raise_for_status()
    print("GET:", resp.json())

put_pushover_load_case_load_control()
put_pushover_load_case_disp_control()
get_pushover_load_case()
```

---

## End-to-End Workflow

以下为用于抗震性能评估的推覆分析完整设置工作流。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/gen"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_MAPI_KEY"
}

# ── STEP 1: 初始荷载忽略单元设置 (IEPI) ─────────────────────────
# 指定施工阶段临时构件等在初始荷载计算中排除的单元
iepi_payload = {
    "Assign": {
        str(eid): {"B_IGNORE": True} for eid in [101, 102, 103]
    }
}
r1 = requests.post(f"{BASE_URL}/db/IEPI", json=iepi_payload, headers=HEADERS)
print(f"STEP1 IEPI: {r1.status_code}")

# ── STEP 2: 推覆分析铰属性指派 (PHGE) ───────────────────────────
phge_payload = {
    "Assign": {
        "1": {"ID": 1, "TYPE": "BEAM", "HINGE_TYPE": "Myz_15", "FIBER_KEY": 0},
        "2": {"ID": 2, "TYPE": "BEAM", "HINGE_TYPE": "Myz_15", "FIBER_KEY": 0}
    }
}
r2 = requests.post(f"{BASE_URL}/db/PHGE", json=phge_payload, headers=HEADERS)
print(f"STEP2 PHGE: {r2.status_code}")

# ── STEP 3: 推覆分析控制数据设置 (POGD) ─────────────────────────
pogd_payload = {
    "Assign": {
        "1": {
            "GEOMNONLINEAR_TYPE": "NONE",
            "INITLOADMETHOD": "PERFORM_ANAL",
            "INITLOAD": [],
            "bCONSIGNOREELEM": True,
            "NONL_OPT": {
                "bPERMITFAIL": True, "SUBSTEP": 10, "MAXITER": 30,
                "bDISPLNORM": True, "bFORCENORM": False, "bENERGYNORM": False,
                "DISPLNORM": 0.001, "FORCENORM": 0.001, "ENERGYNORM": 0.001,
                "bSHEARYIELDSTOP": False, "BSHEARYIELDSTOPBEAM": True,
                "bSHEARYIELDSTOPWALL": False, "bAXIALYIELDSTOP": False,
                "bAXIALYIELDSTOPBEAM": True, "bAXIALYIELDSTOPWALL": False,
                "bAXIALYIELDSTOPTRUSS": False, "bSUPPORTDZDIRSTOP": False,
                "bSUPPORTSTOPUPLIFTING": False, "bSUPPORTSTOPCOLLAPSE": False
            },
            "PHOP_OPT": {
                "bCONSREBARAREA1D": True, "BEAM_CORE_SIZE": "AUTO",
                "BEAM_CORE_DIV_Y": 15, "BEAM_CORE_DIV_Z": 15,
                "BEAM_COVER_SIZE": "EQUAL", "BEAM_COVER_DIV_Y": 15, "BEAM_COVER_DIV_Z": 15,
                "bCONSREBARAREAWALL": True, "bWALLCONSOUT": True,
                "WALL_CORE_SIZE": "AUTO", "WALL_CORE_DIV_Z": 8, "WALL_CORE_DIV_Y": 8,
                "WALL_COVER_SIZE": "AUTO", "WALL_COVER_DIV_Z": 8, "WALL_COVER_DIV_Y": 1,
                "SHEAR_R": 0.4, "bASSIGNBYMEMBER": True,
                "bTRI_SYM": True, "TRI_TENS_A1": 0.1, "TRI_TENS_A2": 0.05,
                "TRI_COMP_A1": 0.1, "TRI_COMP_A2": 0.05,
                "bBI_SYM": True, "BI_TENS_A1": 0.05, "BI_COMP_A1": 0.05,
                "PSPR_APPLY_TYPE": "ASSUME", "ELNK_APPLY_TYPE": "APPLY",
                "bUSEAUTOCALCREFERENCE": True, "RCDGNCODE": "KISTEC2019",
                "LOC_BEAM": "M", "LOC_COLUMN": "I",
                "SF_WALL": 1.6, "bSF_BRITTLE": False, "SF_BRITTLE": 1.6,
                "bSF_EARTHQUAKE": False, "SF_EARTHQUAKE": 0.85,
                "bSF_SMOOTH_BAR": False, "SF_SMOOTH_BAR": 0.575,
                "CONFIDENCE": 1, "bBUCKLING": True, "bCALCAXIALFORCE": True
            },
            "NODECONNECTIVITY": "PINNED",
            "bSHOWGRAPHAFTER": True,
            "bSHOWGRAPGHDURING": False
        }
    }
}
r3 = requests.post(f"{BASE_URL}/db/POGD", json=pogd_payload, headers=HEADERS)
print(f"STEP3 POGD: {r3.status_code}")

# ── STEP 4: 推覆分析荷载工况定义 (POLC) ─────────────────────────
polc_payload = {
    "Assign": {
        "1": {
            "LCNAME": "PUSH_MODE_X", "DESC": "1차 모드 X방향 가력",
            "INCRE_STEP": 20, "bCONS_PDELTA": True, "bUSEINITIAL": True,
            "bREACOUTPUT": True, "INCRE_METHOD": "DISP", "STEPCTRLOPTION": "AUTO",
            "INCFUNC_KEY": 0, "STIFF_RATIO": 0,
            "bLIMITDEFORMANGLE": True, "LIMITDEFORMANGLE": 25,
            "bDRIFTMAX": True, "bDRIFTCENTER": False, "bDRIFTAVER": False,
            "DISPCTRLOPTION": "NODE", "GLOBAL_MAX_DISP": 0,
            "MASTERNODE": 134, "MASTERDIRECTION": "DX", "MASTERMAXDISP": 1.5,
            "LOADPATTERNTYPE": "MODE",
            "LOADPATTERN": [{"MODE": 1, "SF": 1}]
        }
    }
}
r4 = requests.post(f"{BASE_URL}/db/POLC", json=polc_payload, headers=HEADERS)
print(f"STEP4 POLC: {r4.status_code}")

# ── STEP 5: 定义切割线后执行分析 ────────────────────────────────
r5 = requests.post(f"{BASE_URL}/doc/ANAL", json={"Argument": {}}, headers=HEADERS)
print(f"STEP5 ANAL: {r5.status_code}")

# ── 确认全部设置 ─────────────────────────────────────────────────
print("\n=== 推覆分析设置确认 ===")
for ep in ["IEPI", "PHGE", "POGD", "POLC"]:
    r = requests.get(f"{BASE_URL}/db/{ep}", headers=HEADERS)
    data = r.json().get(ep, {})
    print(f"  {ep}: {len(data)} 条")
```

---

## POGD vs POGD-M1 / POLC vs POLC-M1 对比小结

| 项目 | 一般(General) | Hyper-S(-M1) |
|------|:--------------:|:------------:|
| Active Methods | POST, GET, PUT, DELETE | GET, PUT, DELETE (不支持 POST) |
| 字段命名规则 | 缩写式扁平结构 (`GEOMNONLINEAR_TYPE`) | 分组式 Enum/嵌套结构 (`GEO_NONL_TYPE`: 0/1/2) |
| JSON Schema 风格 | 简单 `properties` 罗列 | `allOf` / `if-then` 条件 Schema |
| 适用对象 | Civil NX / Gen NX 通用 | Hyper-S 求解器专用模型 |
