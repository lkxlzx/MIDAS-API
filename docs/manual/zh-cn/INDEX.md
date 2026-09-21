# MIDAS NX Open API — JSON Manual Index

> **出处：** [MIDAS API Online Manual](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **首次生成：** 2024.05.28 · **官方最后编辑：** 2026.07.30 · **本文件同步：** 2026-07-30  
> **适用产品：** MIDAS Civil NX · MIDAS Gen NX

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../INDEX.md) · **原文同步日期：** 2026-07-30  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录结构

| 文件 | 章节 | 说明 |
|------|------|------|
| [01_DOC.md](./01_DOC.md) | DOC | 文档创建·打开·保存·关闭·执行分析（11个） |
| [02_DB_Project_Structure.md](./02_DB_Project_Structure.md) | DB – Project / Structure | 项目信息·单位·结构类型·组·楼层数据（15个） |
| [03_DB_Node_Element.md](./03_DB_Node_Element.md) | DB – Node / Element | 节点·单元·局部轴·域（6个） |
| [04_DB_Properties.md](./04_DB_Properties.md) | DB – Properties | 材料·截面·厚度·铰·纤维截面（32个） |
| [05_DB_Boundary.md](./05_DB_Boundary.md) | DB – Boundary | 支承·弹簧·连接·释放·抗震装置（24个） |
| [06_DB_Static_Loads.md](./06_DB_Static_Loads.md) | DB – Static Loads | 静力荷载工况·自重·梁单元荷载·楼面荷载·风荷载·地震作用（21个） |
| [07_DB_Temperature_Prestress.md](./07_DB_Temperature_Prestress.md) | DB – Temperature / Prestress | 温度·预应力束·预应力荷载（12个） |
| [08_DB_Moving_Loads.md](./08_DB_Moving_Loads.md) | DB – Moving Loads | 移动荷载（桥梁专用，28个） |
| [09_DB_Dynamic_Loads.md](./09_DB_Dynamic_Loads.md) | DB – Dynamic Loads | 反应谱·时程（12个） |
| [10_DB_Construction_Stage.md](./10_DB_Construction_Stage.md) | DB – Construction Stage / Hydration | 施工阶段·水化热（14个） |
| [11_DB_Settlement_Misc_Loads.md](./11_DB_Settlement_Misc_Loads.md) | DB – Settlement / Misc Loads | 沉降·波浪·非线性初始荷载等（9个） |
| [12_DB_Analysis_Control.md](./12_DB_Analysis_Control.md) | DB – Analysis Control | 分析控制数据（21个） |
| [13_DB_Load_Combinations.md](./13_DB_Load_Combinations.md) | DB – Load Combinations / Results | 荷载组合·结果设置（8个） |
| [14_DB_Pushover.md](./14_DB_Pushover.md) | DB – Pushover | 推覆分析控制·铰·荷载（6个） |
| [15_OPE.md](./15_OPE.md) | OPE | GUI 联动操作函数（19个） |
| [16_VIEW.md](./16_VIEW.md) | VIEW | 视图控制·截取·结果显示（7个） |
| [17_DB_Bridge.md](./17_DB_Bridge.md) | DB – Bridge Specialization | 主梁·预拱度·拉索结果设置（5个） |
| [18_POST_PreProcess.md](./18_POST_PreProcess.md) | POST – Pre-Process Tables | 重量·质量·荷载·材料·截面·楼层汇总（约10个） |
| [19_POST_AnalysisResult_1.md](./19_POST_AnalysisResult_1.md) | POST – Analysis Result Tables Part 1 | 反力·位移·桁架·拉索·梁结果（13个） |
| [20_POST_AnalysisResult_2.md](./20_POST_AnalysisResult_2.md) | POST – Analysis Result Tables Part 2 | 板·平面·轴对称·实体·连接·模态·预应力束·施工阶段·墙（39个） |
| [21_POST_StoryTables.md](./21_POST_StoryTables.md) | POST – Analysis Story Tables | 层位移·层剪力·层扭转·不规则审查（17个） |
| [22_POST_TH_HY_Pushover.md](./22_POST_TH_HY_Pushover.md) | POST – TH / HY / Pushover Result Tables | 时程·水化热·推覆分析结果（28个） |
| [23_POST_Design.md](./23_POST_Design.md) | POST – Design Tables | P-M·Steel·RC·SRC·冷弯薄壁型钢设计结果（约10个） |
| [24_DB_Design.md](./24_DB_Design.md) | DB – Design | RC·Steel 设计代码·构件·未支撑长度（13个） |
| [25_Design_Steel_KDS41302022.md](./25_Design_Steel_KDS41302022.md) | Design Code – STEEL KDS 41 30:2022 | 钢结构设计代码设置·构件·未支撑长度·屈曲·设计验算（28个） |
| [26_Design_RC_KDS41202022.md](./26_Design_RC_KDS41202022.md) | Design Code – RC KDS 41 20:2022 | RC 设计代码设置·梁·柱·墙·板设计（70个） |
| [27_Design_SRC_AIKSRC2K.md](./27_Design_SRC_AIKSRC2K.md) | Design Code – SRC AIK-SRC2K | SRC 组合构件设计代码设置·梁·柱设计（27个） |

---

## INTRODUCTION

本手册是面向 MIDAS NX 系列（Civil NX · Gen NX）的 **MIDAS API JSON 结构手册**。  
MIDAS API 基于 RESTful API 运行，提供各功能的 Endpoint、Method、JSON 结构与示例。

### Base URL

```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```

### 认证头部

```http
MAPI-Key: <Gen NX 应用中获取的密钥>
Content-Type: application/json
```

### Endpoint 分类概述

---

## DOC

文档（Document）部分的操作。**仅使用 POST 方法**。  
请求体以 `"Argument"` 键起始，请求体为空时使用 `{}`。

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/doc/NEW` | New Project |
| 2 | `/doc/OPEN` | Open Project |
| 3 | `/doc/CLOSE` | Close Project |
| 4 | `/doc/SAVE` | Save |
| 5 | `/doc/SAVEAS` | Save As |
| 6 | `/doc/STAGAS` | Save Current Stage As |
| 7 | `/doc/IMPORT` | Import to JSON |
| 8 | `/doc/IMPORTMXT` | Import to mct/mgt |
| 9 | `/doc/EXPORT` | Export to JSON |
| 10 | `/doc/EXPORTMXT` | Export to mct/mgt |
| 11 | `/doc/ANAL` | Perform Analysis |

---

## DB

保存到 MIDAS NX 文件中的数据。与 MCT/MGT 功能作用相同。  
通常使用 POST/GET/PUT/DELETE 方法，但**单位·结构类型等新建文件必需数据仅支持 GET/PUT**。

请求体以 `"Assign"` 键起始，使用编号键（ID）→ 数据结构的形式。

### Project

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/PJCF` | Project Information |
| 2 | `/db/UNIT` | Unit System |
| 3 | `/db/STYP` | Structure Type |
| 4 | `/db/STYP-M1` | Structure Type (Hyper-S) |
| 5 | `/db/GRUP` | Structure Group |
| 6 | `/db/BNGR` | Boundary Group |
| 7 | `/db/LDGR` | Load Group |
| 8 | `/db/TDGR` | Tendon Group |

### View

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/NPLN` | Named Plane |
| 2 | `/db/CO_M` | Material Color |
| 3 | `/db/CO_S` | Section Color |
| 4 | `/db/CO_T` | Thickness Color |
| 5 | `/db/CO_F` | Floor Load Color |

### Structure

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/SPAN` | Span Information |
| 2 | `/db/STOR` | Story Data |

### Node / Element

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/NODE` | Node |
| 2 | `/db/ELEM` | Element |
| 3 | `/db/SKEW` | Node Local Axis |
| 4 | `/db/MADO` | Define Domain |
| 5 | `/db/SBDO` | Define Sub-Domain |
| 6 | `/db/DOEL` | Domain-Element |

### Properties

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/MATL` | Material Properties |
| 2 | `/db/MATL-M1` | Material Properties (Hyper-S) |
| 3 | `/db/IMFM` | Inelastic Material Properties for Fiber Model |
| 4 | `/db/IMFM-M1` | Inelastic Material Link for Auto Generation (Hyper-S) |
| 5 | `/db/TDMF` | Time Dependent Material – User Defined |
| 6 | `/db/TDMT` | Time Dependent Material – Creep/Shrinkage |
| 7 | `/db/TDME` | Time Dependent Material – Compressive Strength |
| 8 | `/db/EDMP` | Change Property |
| 9 | `/db/TMAT` | Time Dependent Material Link |
| 10 | `/db/EPMT` | Plastic Material |
| 11 | `/db/EPMT-M1` | Plastic Material (Hyper-S) |
| 12 | `/db/SECT` | Section Properties (Common / DB·User / Value / SRC / PSC / Tapered 等) |
| 13 | `/db/THIK` | Thickness (Value / Stiffened DB·User·Value) |
| 14 | `/db/TSGR` | Tapered Group |
| 15 | `/db/SECF` | Section Manager – Stiffness |
| 16 | `/db/RPSC` | Section Manager – Reinforcements |
| 17 | `/db/STRPSSM` | Section Manager – Stress Points |
| 18 | `/db/PSSF` | Section Manager – Plate Stiffness Scale Factor |
| 19 | `/db/VBEM` | Virtual Beam |
| 20 | `/db/VSEC` | Virtual Section |
| 21 | `/db/EWSF` | Effective Width Scale Factor |
| 22 | `/db/IEHC` | Inelastic Hinge Control Data |
| 23 | `/db/IEHG` | Assign Inelastic Hinge Properties |
| 24 | `/db/IEHG-BEAM-M1` | Assign Inelastic Hinges – Beam (Hyper-S) |
| 25 | `/db/IEHG-TRUSS-M1` | Assign Inelastic Hinges – Truss (Hyper-S) |
| 26 | `/db/IEHG-GL-M1` | Assign Inelastic Hinges – General Link (Hyper-S) |
| 27 | `/db/IEHG-PSS-M1` | Assign Inelastic Hinges – Point Spring Support (Hyper-S) |
| 28 | `/db/FIMP` | Inelastic Material Properties |
| 29 | `/db/FIBR` | Fiber Division of Section |
| 30 | `/db/GRDP` | Group Damping |
| 31 | `/db/ESSF` | Element Stiffness Scale Factor |
| 32 | `/db/MATD` | Modify Concrete Materials |

### Boundary

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/CONS` | Constraint Support |
| 2 | `/db/NSPR` | Point Spring |
| 3 | `/db/GSTP` | Define General Spring Type |
| 4 | `/db/GSPR` | Assign General Spring Supports |
| 5 | `/db/SSPS` | Surface Spring |
| 6 | `/db/ELNK` | Elastic Link |
| 7 | `/db/RIGD` | Rigid Link |
| 8 | `/db/NLLP` | General Link Properties |
| 9 | `/db/NLNK` | General Link |
| 10 | `/db/NLNK-M1` | General Link (Hyper-S) |
| 11 | `/db/CGLP` | Change General Link Property |
| 12 | `/db/FRLS` | Beam End Release |
| 13 | `/db/OFFS` | Beam End Offsets |
| 14 | `/db/PRLS` | Plate End Release |
| 15 | `/db/MLFC` | Force-Deformation Function |
| 16 | `/db/SDVI` | Seismic Device – Viscous/Oil Damper |
| 17 | `/db/SDVE` | Seismic Device – Viscoelastic Damper |
| 18 | `/db/SDST` | Seismic Device – Steel Damper |
| 19 | `/db/SDHY` | Seismic Device – Hysteretic Isolator (MSS) |
| 20 | `/db/SDIS` | Seismic Device – Isolator (MSS) |
| 21 | `/db/MCON` | Linear Constraints |
| 22 | `/db/PZEF` | Panel Zone Effects |
| 23 | `/db/CLDR` | Define Constraints Label Direction |
| 24 | `/db/DRLS` | Diaphragm Disconnect |

### Static Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/STLD` | Static Load Cases |
| 2 | `/db/BODF` | Self-Weight |
| 3 | `/db/CNLD` | Nodal Loads |
| 4 | `/db/BMLD` | Beam Loads |
| 5 | `/db/SDSP` | Specified Displacements of Support |
| 6 | `/db/NMAS` | Nodal Masses |
| 7 | `/db/LTOM` | Loads to Masses |
| 8 | `/db/NBOF` | Nodal Body Force |
| 9 | `/db/PSLT` | Define Pressure Load Type |
| 10 | `/db/PRES` | Assign Pressure Loads |
| 11 | `/db/PNLD` | Define Plane Load Type |
| 12 | `/db/PNLA` | Assign Plane Loads |
| 13 | `/db/FBLD` | Define Floor Load Type |
| 14 | `/db/FBLA` | Assign Floor Loads |
| 15 | `/db/FMLD` | Finishing Material Loads |
| 16 | `/db/POSP` | Parameter of Soil Properties |
| 17 | `/db/EPST` | Static Earth Pressure |
| 18 | `/db/EPSE` | Seismic Earth Pressure |
| 19 | `/db/POSL` | Parameter of Seismic Loads |
| 20 | `/db/SWIND` | Static Wind Load (KDS 41-12:2022 / User Type) |
| 21 | `/db/SSEIS` | Static Seismic Load (KDS 41-17-00:2019 / User Type) |

### Temperature Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/ETMP` | Element Temperature |
| 2 | `/db/GTMP` | Temperature Gradient |
| 3 | `/db/BTMP` | Beam Section Temperature |
| 4 | `/db/STMP` | System Temperature |
| 5 | `/db/NTMP` | Nodal Temperature |

### Prestress Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/TDNT` | Tendon Property |
| 2 | `/db/TDNA` | Tendon Profile |
| 3 | `/db/TDCS` | Tendon Location for Composite Section |
| 4 | `/db/TDPL` | Tendon Prestress |
| 5 | `/db/PRST` | Prestress Beam Loads |
| 6 | `/db/PTNS` | Pretension Loads |
| 7 | `/db/EXLD` | External Type Load Case for Pretension |

### Moving Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/MVCD` | Moving Load Code |
| 2 | `/db/LLAN` | Traffic Line Lanes |
| 3 | `/db/LLANch` | Traffic Line Lanes – China |
| 4 | `/db/LLANid` | Traffic Line Lanes – India |
| 5 | `/db/LLANtr` | Traffic Line Lanes – Transverse |
| 6 | `/db/LLANop` | Traffic Line Lanes – Moving Load Optimization |
| 7 | `/db/SLAN` | Traffic Surface Lanes |
| 8 | `/db/SLANch` | Traffic Surface Lanes – China |
| 9 | `/db/SLANop` | Traffic Surface Lanes – Moving Load Optimization |
| 10 | `/db/MVHL` | Vehicles (AASHTO / LRFD / Canada / BS / Eurocode / Korea 等) |
| 11 | `/db/MVHLtr` | Vehicles – Transverse |
| 12 | `/db/MVLD` | Moving Load Cases |
| 13 | `/db/MVLDch` | Moving Load Cases – China |
| 14 | `/db/MVLDid` | Moving Load Cases – India |
| 15 | `/db/MVLDbs` | Moving Load Cases – BS |
| 16 | `/db/MVLDeu` | Moving Load Cases – Eurocode |
| 17 | `/db/MVLDpl` | Moving Load Cases – Poland |
| 18 | `/db/MVLDtr` | Moving Load Cases – Transverse |
| 19 | `/db/CRGR` | Concurrent Reaction Group |
| 20 | `/db/CJFG` | Concurrent Joint Force Group |
| 21 | `/db/MVHC` | Vehicle Classes |
| 22 | `/db/SINF` | Plate Element for Influence Surface |
| 23 | `/db/MLSP` | Lane Support – Negative Moments at Interior Piers |
| 24 | `/db/MLSR` | Lane Support – Reactions at Interior Piers |
| 25 | `/db/DYLA` | Dynamic Load Allowance |
| 26 | `/db/IMPF` | Additional Impact Factor |
| 27 | `/db/DYFG` | Railway Dynamic Factor |
| 28 | `/db/DYNF` | Railway Dynamic Factor by Element |

### Dynamic Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/SPFC` | Response Spectrum Functions (User / Korea / US / Eurocode / China 等) |
| 2 | `/db/SPLC` | Response Spectrum Load Cases |
| 3 | `/db/THGC` | Time History Global Control |
| 4 | `/db/THGC-M1` | Time History Global Control (Hyper-S) |
| 5 | `/db/THOO-M1` | Time History Output Option (Hyper-S) |
| 6 | `/db/THIS` | Time History Load Cases |
| 7 | `/db/THIS-M1` | Time History Load Cases (Hyper-S) |
| 8 | `/db/THFC` | Time History Functions |
| 9 | `/db/THGA` | Ground Acceleration |
| 10 | `/db/THNL` | Dynamic Nodal Loads |
| 11 | `/db/THSL` | Time Varying Static Loads |
| 12 | `/db/THMS` | Multiple Support Excitation |

### Construction Stage Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/STAG` | Define Construction Stage |
| 2 | `/db/CSCS` | Composite Section for Construction Stage |
| 3 | `/db/TMLD` | Time Loads for Construction Stage |
| 4 | `/db/STBK` | Set-Back Loads for Nonlinear Construction Stage |
| 5 | `/db/CMCS` | Camber for Construction Stage |
| 6 | `/db/CRPC` | Creep Coefficient for Construction Stage |

### Heat of Hydration Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/ETFC` | Ambient Temperature Functions |
| 2 | `/db/CCFC` | Convection Coefficient Functions |
| 3 | `/db/HECB` | Element Convection Boundary |
| 4 | `/db/HSPT` | Prescribed Temperature |
| 5 | `/db/HSFC` | Heat Source Functions |
| 6 | `/db/HAHS` | Assign Heat Source |
| 7 | `/db/HPCE` | Pipe Cooling |
| 8 | `/db/HSTG` | Define Construction Stage for Hydration |

### Settlement Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/SMPT` | Settlement Group |
| 2 | `/db/SMLC` | Settlement Load Cases |

### Miscellaneous Loads

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/PLCB` | Pre-composite Section |
| 2 | `/db/LDSQ` | Load Sequence for Nonlinear |
| 3 | `/db/WVLD` | Wave Loads |
| 4 | `/db/IELC` | Ignore Elements for Load Cases |
| 5 | `/db/IFGS` | Large Displacement – Initial Forces for Geometric Stiffness |
| 6 | `/db/EFCT` | Small Displacement – Initial Force Control Data |
| 7 | `/db/INMF` | Small Displacement – Initial Element Force |

### Analysis Control

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/ACTL` | Main Control Data |
| 2 | `/db/ACTL-M1` | Main Control Data (Hyper-S) |
| 3 | `/db/PDEL` | P-Delta Analysis Control |
| 4 | `/db/BUCK` | Buckling Analysis Control |
| 5 | `/db/EIGV` | Eigenvalue Analysis Control |
| 6 | `/db/EIGV-M1` | Eigenvalue Analysis Control (Hyper-S) |
| 7 | `/db/HHCT` | Heat of Hydration Analysis Control |
| 8 | `/db/HHCT-M1` | Heat of Hydration Analysis Control (Hyper-S) |
| 9 | `/db/MVCT` | Moving Load Analysis Control |
| 10 | `/db/MVCTch` | Moving Load Analysis Control – China |
| 11 | `/db/MVCTid` | Moving Load Analysis Control – India |
| 12 | `/db/MVCTbs` | Moving Load Analysis Control – BS |
| 13 | `/db/MVCTtr` | Moving Load Analysis Control – Transverse |
| 14 | `/db/SMCT` | Settlement Analysis Control Data |
| 15 | `/db/NLCT` | Nonlinear Analysis Control Data |
| 16 | `/db/NLCT-M1` | Nonlinear Analysis Control (Hyper-S) |
| 17 | `/db/STCT` | Construction Stage Analysis Control Data |
| 18 | `/db/STCT-M1` | Construction Stage Analysis Control Data (Hyper-S) |
| 19 | `/db/BCCT` | Boundary Change Assignment |
| 20 | `/db/BCGD-M1` | Define Boundary Combination (Hyper-S) |
| 21 | `/db/BCGA-M1` | Assign Boundary Combination (Hyper-S) |

### Analysis Results / Load Combinations

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/LCOM-GEN` | Load Combinations – General |
| 2 | `/db/LCOM-CONC` | Load Combinations – Concrete Design |
| 3 | `/db/LCOM-STEEL` | Load Combinations – Steel Design |
| 4 | `/db/LCOM-SRC` | Load Combinations – SRC Design |
| 5 | `/db/LCOM-STLCOMP` | Load Combinations – Composite Steel Girder Design |
| 6 | `/db/LCOM-SEISMIC` | Load Combinations – Seismic Design |
| 7 | `/db/CUTL` | Cutting Line |
| 8 | `/db/CLWP` | Plate Cutting Line Diagram |

### Bridge Specialization Results

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/GSBG` | Bridge Girder Diagrams |
| 2 | `/db/GCMB` | General Camber Control |
| 3 | `/db/CAMB` | FCM Camber Control |
| 4 | `/db/ULFC` | Cable Control – Unknown Load Factor Constraints |

### Pushover

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/POGD` | Pushover Analysis Control Data |
| 2 | `/db/POGD-M1` | Pushover Global Control (Hyper-S) |
| 3 | `/db/IEPI` | Ignore Elements for Pushover Initial Load |
| 4 | `/db/PHGE` | Assign Pushover Hinge Properties |
| 5 | `/db/POLC` | Pushover Load Cases |
| 6 | `/db/POLC-M1` | Pushover Load Case (Hyper-S) |

### Design (DB)

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/db/DCON` | RC Design Code |
| 2 | `/db/DSTL` | Design Steel Code |
| 3 | `/db/RCHK` | Rebar Input for Checking - Beam/Column |
| 4 | `/db/LENG` | Unbraced Length |
| 5 | `/db/MEMB` | Member Assignment |
| 6 | `/db/DCTL` | Definition of Frame |
| 7 | `/db/LTSR` | Limiting Slenderness Ratio |
| 8 | `/db/MBTP` | Modify Member Type |
| 9 | `/db/WMAK` | Modify Wall Mark Design |
| 10 | `/db/REBB` | Modify Beam Rebar Data |
| 11 | `/db/REBC` | Modify Column Rebar Data (仅 POST) |
| 12 | `/db/REBW` | Modify Wall Rebar Data |
| 13 | `/db/REBR` | Modify Brace Rebar Data |

---

## OPE

GUI 或预处理计算值控制函数。属于不保存到 DB 的数据。

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/ope/PROJECTSTATUS` | Project Status |
| 2 | `/ope/DIVIDEELEM` | Divide Elements |
| 3 | `/ope/SECTPROP` | Section Properties Calculation Results |
| 4 | `/ope/USLC` | Using Load Combinations |
| 5 | `/ope/LINEBMLD` | Line Beam Load |
| 6 | `/ope/AUTOMESH` | Auto-Mesh Planar Area |
| 7 | `/ope/SSPS` | Surface Spring |
| 8 | `/ope/EDMP` | Change Property |
| 9 | `/ope/STOR` | Story Calculation |
| 10 | `/ope/STORY_PARAM` | Story Check Parameter |
| 11 | `/ope/STORY_IRR_PARAM` | Story Irregularity Check Parameter |
| 12 | `/ope/STORYPROP` | Story Properties |
| 13 | `/ope/MEMB` | Member Assignment |
| 14 | `/ope/GUSTFACTOR` | Gust Factor Calculator |
| 15 | `/ope/LCOM-GEN` | Load Combination (General) – KDS:2022 / AIK-SRC2K |
| 16 | `/ope/LCOM-CONC` | Load Combination (Concrete) – KDS 41 20:2022 |
| 17 | `/ope/LCOM-STEEL` | Load Combination (Steel) – KDS 41 30:2022 |
| 18 | `/ope/LCOM-SRC` | Load Combination (SRC) – KDS 41 SRC:2022 / AIK-SRC2K |
| 19 | `/ope/GSBG` | Bridge Girder Diagram Image Generation |

---

## VIEW

模型视图控制。Capture 可与 Angle·Active·Display·ResultGraphic 一起使用。

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/view/SELECT` | Select |
| 2 | `/view/CAPTURE` | Capture |
| 3 | `/view/PRECAPTURE` | Dialog Capture |
| 4 | `/view/ANGLE` | Viewpoint |
| 5 | `/view/ACTIVE` | Active |
| 6 | `/view/DISPLAY` | Display |
| 7 | `/view/RESULTGRAPHIC` | Type of Display / 反力·位移·桁架·梁·板·应力等结果显示 |

---

## POST

用于提取前处理·后处理表格。详细用法参见 *Designing with Intent: The Vision Behind POST/TABLE*。

### Pre-Process Table

| No. | 表类型 |
|-----|------------|
| 1 | Element Weight Table |
| 2 | Nodal Body Force Table |
| 3 | Mass Summary Table |
| 4 | Load Summary Table |
| 5 | Material Table |
| 6 | Section Table |
| 7 | Restraint Support Table |
| 8 | Story Mass Summary Table |
| 9 | Story Load Summary Table |
| 10 | Story Weight Table |

### Analysis Result Table (主要)

反力·位移·桁架·拉索·梁·板·实体·Elastic Link·General Link·振型·屈曲模态·预应力束等 24种

### Analysis Story Table

层间位移·层位移·层剪力·层模态形状·扭转·倾覆力矩·轴力合力·稳定系数·不规则审查等 16种

### Design (POST)

| No. | Endpoint | 功能 |
|-----|----------|------|
| 1 | `/post/PM` | P-M Interaction Diagram |
| 2 | `/post/STEELCODECHECK` | Steel Code Check |
| 3 | `/post/BEAMDESIGNFORCES` | Concrete – Beam Design Forces |
| 4 | `/post/COLUMNDESIGNFORCES` | Concrete – Column Design Forces |
| 5 | `/post/BRACEDESIGNFORCES` | Concrete – Brace Design Forces |
| 6 | `/post/WALLDESIGNFORCES` | Concrete – Wall Design Forces |
| 7 | `/post/STEELMEMBERDESIGNFORCES` | Steel – Member Design Forces |
| 8 | `/post/SRCBEAMDESIGNFORCES` | SRC – Beam Design Forces |
| 9 | `/post/SRCCOLUMNDESIGNFORCES` | SRC – Column Design Forces |
| 10 | `/post/COLDFORMEDSTEELMEMBERDESIGNFORCES` | Cold Formed – Member Design Forces |

---

## Design (Code Design)

基于设计代码的结构构件验算 API 表。

### STEEL
| Code | 详情 |
|------|------|
| `KDS-41-30-2022` | KDS 41 30 : 2022 |

### RC
| Code | 详情 |
|------|------|
| `KDS-41-20-2022` | KDS 41 20 : 2022 |

### SRC
| Code | 详情 |
|------|------|
| `AIK-SRC2K` | AIK-SRC2K |

---

> **图例：**  
> ᴴˢ⁾ = 仅 Hyper-S 求解器  
> ᴶ⁾ = 仅 MIDAS Civil NX JP 版本专用
