# MIDAS Plug-in Manual Index

> **出处：** [Plug-in Online Manual](https://support.midasuser.com/hc/en-us/articles/35639730101529-Plug-in-Online-Manual) ·
> Zendesk 分类 [Plug-in](https://support.midasuser.com/hc/en-us/sections/35681419399961-Plug-in)
> （`section_id = 35681419399961`）
> **首次生成：** 2026-08-04
> **适用产品：** MIDAS Civil NX · MIDAS Gen NX

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../INDEX.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 本文件夹是什么

与 `docs/manual/` 处理 MIDAS NX Open API 的 **JSON Schema 参考**（Zendesk "JSON Manual" 分类，`section_id = 30087500371097`）不同，本文件夹处理的是 **MIDAS Plug-in** —— 把 MIDAS API 与 Python 结合而成、内嵌于 GUI 的成品自动化工具。

Plug-in 内部同样调用 MIDAS API，因此"借助 API 的实现方式"这一大框架与 JSON Manual 相同，但文档性质不同：

| | `docs/manual/`（JSON Manual） | `docs/plugin/`（本文件夹） |
| --- | --- | --- |
| 目标读者 | 直接调用 REST API 的开发者 | 在 GUI 中使用成品工具的工程师（+想自行制作 Plug-in 的开发者） |
| 原文性质 | 按 Endpoint 的 Key/Value Schema 表 | 基于截图的 GUI 使用方法走查 |
| 文档单位 | 章（Endpoint 分组） | 1 个 Plug-in 工具 = 1 个文件 |
| Zendesk 分类 | JSON Manual（651 篇文章） | Plug-in（Introduction 4 篇 + Plug-in Item 65 篇，另有 2 篇已废止） |

**因此不沿用 `docs/manual` 的 "TABLE_TYPE 表 → Response HEAD → Request/Response JSON → Python 示例" 惯例。** 而是遵循[下方模板](#toolsmd-单篇文档模板)。

---

## 进行状态

本 INDEX.md 既是目录，也是工作跟踪表。"状态"列为 ⬜（待撰写）的条目尚无独立文档 —— 目前仅确认了原文链接。需要时（用户请求时）重新抓取对应原文，按 `tools/*.md` 模板填写，并把本表的状态更新为 ✅。规模较大时原样复用 CLAUDE.md 的调研/编辑分离子代理模式。**⚠️ 已废止**指一度出现在落地页面、也已撰写独立文档，但此后官方站点把文章本身删除（404）的条目 —— 文档作为过往记录留存，但不再是同步检查对象（也从 `common.py` 的 `PLUGIN_ARTICLE_IDS` 中剔除）。

- Guide：4/4 已完成
- Plug-in Item：登载 65 篇（已完成 61 + 已废止 2 + 待撰写 2）。沿革：原文 53 篇中 "Image Capture Generator" 是 "Easy Capture Generator" 同一 URL 的别名，故合并为 1 篇 + 2026-08-06 新发现 4 篇 + 2026-08-15 新发现 2 篇 + 2026-08-24 新发现 5 篇 + 2026-08-30 定期检查时新发现 2 篇（"Point to Patch Convertor"·"Model Report Builder"），以及同日确认原有 2 篇（"Floor Load Table Generator"·"Easy Result Table"）已从官方站点删除、据此转为已废止一事。"Response Spectrum Generator" 在落地页面也按地区代码别名（"[Peru E.030:2026]"、"[SNZ TS 1170.5:2025]"）另列两次，但属同一篇文章，不计入篇数 —— 相关代码已反映在 [Response_Spectrum_Generator.md](./tools/Response_Spectrum_Generator.md) 的"适用标准"中）

---

## Guide — 概念·开发指南（4篇）

| No. | 名称 | 文件 | 状态 | 原文链接 |
| --- | --- | --- | --- | --- |
| 1 | Introduction to MIDAS Plug-in | [guide/01_Introduction.md](./guide/01_Introduction.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35693347852569-Introduction-to-MIDAS-Plug-in) |
| 2 | How to use MIDAS Plug-ins | [guide/02_How_to_Use.md](./guide/02_How_to_Use.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35694950947353-How-to-use-MIDAS-Plug-ins) |
| 3 | Guiding for writing Python Code (Planning/Development Collaboration) | [guide/03_Python_Coding_Guide.md](./guide/03_Python_Coding_Guide.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/44321576105497-Guiding-for-writing-Python-Code-Planning-Development-Collaboration) |
| 4 | A Guide to Creating Plug-in for Developers | [guide/04_Developer_Guide.md](./guide/04_Developer_Guide.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/44321750649369-A-Guide-to-Creating-Plug-in-for-Developers) |

---

## Plug-in Item — 单个工具（67篇，其中已废止 2篇）

原文页面是不含子分类、按字母顺序排列的 flat 列表，因此本表也原样遵循原文顺序。
文件名不编号，而是把工具名称 slug 化 —— 即使新增 Plug-in，也无须为既有文件重新编号。

| No. | 名称 | 文件 | 状态 | 原文链接 |
| --- | --- | --- | --- | --- |
| 1 | 6x6 General Spring for Pile Foundation (KR) | [tools/6x6_General_Spring_for_Pile_Foundation_KR.md](./tools/6x6_General_Spring_for_Pile_Foundation_KR.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35651992652441-Pile-Spring) |
| 2 | Alignment Editor | [tools/Alignment_Editor.md](./tools/Alignment_Editor.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60307252076441-Alignment-Editor) |
| 3 | Alignment Local Axis for Element | [tools/Alignment_Local_Axis_for_Element.md](./tools/Alignment_Local_Axis_for_Element.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35679369131289-Alignment-Local-Axis-for-Element) |
| 4 | Alignment Generator | [tools/Alignment_Generator.md](./tools/Alignment_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/40709970824729-Alignment-Generator) |
| 5 | Artificial Earthquake Generator | [tools/Artificial_Earthquake_Generator.md](./tools/Artificial_Earthquake_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35656036758937-Artificial-Earthquake-Generator) |
| 6 | Artificial Earthquake Correlation Checker | [tools/Artificial_Earthquake_Correlation_Checker.md](./tools/Artificial_Earthquake_Correlation_Checker.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35650468767385-Artificial-Earthquake-Correlation-Checker) |
| 7 | [AS/NZS 1170.2:2021] Building Wind Loads Generator | [tools/AS_NZS_1170_22021_Building_Wind_Loads_Generator.md](./tools/AS_NZS_1170_22021_Building_Wind_Loads_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/46935970426905--AS-1170-2-2021-Building-Wind-Loads-Generator) |
| 8 | [AS 1170.4:2024] Static Seismic Loads Generator | [tools/AS_1170_42024_Static_Seismic_Loads_Generator.md](./tools/AS_1170_42024_Static_Seismic_Loads_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/46857988729753--AS-1170-4-2024-Static-Seismic-Loads-Generator) |
| 9 | Assign Floor Loads | [tools/Assign_Floor_Loads.md](./tools/Assign_Floor_Loads.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/52564358801049-Assign-Floor-Loads) |
| 10 | Auto Saver | [tools/Auto_Saver.md](./tools/Auto_Saver.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35661003551385-Auto-Saver) |
| 11 | Breakdown Load Combination | [tools/Breakdown_Load_Combination.md](./tools/Breakdown_Load_Combination.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35845551989401-Breakdown-Load-Combination) |
| 12 | Concrete Material Set EN1992-1-1 | [tools/Concrete_Material_Set_EN1992_1_1.md](./tools/Concrete_Material_Set_EN1992_1_1.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45536334603161-Concrete-Material-Set-EN1992-1-1) |
| 13 | Concurrent Force Calculator | [tools/Concurrent_Force_Calculator.md](./tools/Concurrent_Force_Calculator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60341711486361-Concurrent-Force-Calculator) |
| 14 | Convert Load Combination into SDS Format | [tools/Convert_Load_Combination_into_SDS_Format.md](./tools/Convert_Load_Combination_into_SDS_Format.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45496104876313-Convert-Load-Combinations-into-SDS-Format) |
| 15 | Customized Load Combination | [tools/Customized_Load_Combination.md](./tools/Customized_Load_Combination.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/41509743351193-Customized-Load-Combination) |
| 16 | CS Report Generator | [tools/CS_Report_Generator.md](./tools/CS_Report_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/56841756166681-CS-Report-Generator) |
| 17 | Dynamic Analysis of Rail Bridge | [tools/Dynamic_Analysis_of_Rail_Bridge.md](./tools/Dynamic_Analysis_of_Rail_Bridge.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60340982021529-Dynamic-Analysis-of-Rail-Bridge) |
| 18 | Easy Capture Generator[^1] | [tools/Easy_Capture_Generator.md](./tools/Easy_Capture_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35639906272025-Easy-Capture-Generator) |
| 19 | Easy Load Combinations | [tools/Easy_Load_Combinations.md](./tools/Easy_Load_Combinations.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45543036560921-Easy-Load-Combinations) |
| 20 | Element Information | [tools/Element_Information.md](./tools/Element_Information.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35649982873625-Element-Information) |
| 21 | [Eurocode] Fatigue Analysis for Composite Girder Bridge | [tools/Eurocode_Fatigue_Analysis_for_Composite_Girder_Bridge.md](./tools/Eurocode_Fatigue_Analysis_for_Composite_Girder_Bridge.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/49393118303897-Road-bridge-Concrete-Fatigue-for-Composite-Section) |
| 22 | Flared Pier | [tools/Flared_Pier.md](./tools/Flared_Pier.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45352026157593-Flared-Pier) |
| 23 | Floor Transition | [tools/Floor_Transition.md](./tools/Floor_Transition.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35681919947673-Floor-Transition) |
| 24 | GEN NX to Staad Converter | [tools/GEN_NX_to_Staad_Converter.md](./tools/GEN_NX_to_Staad_Converter.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/56728677543321-GEN-NX-to-Staad-Converter) |
| 25 | Group Pile | [tools/Group_Pile.md](./tools/Group_Pile.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45354275911321-Group-Pile) |
| 26 | Inertial Forces Controller | [tools/Inertial_Forces_Controller.md](./tools/Inertial_Forces_Controller.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller) |
| 27 | Iterative Response Spectrum | [tools/Iterative_Response_Spectrum.md](./tools/Iterative_Response_Spectrum.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum) |
| 28 | Line to Plate Converter | [tools/Line_to_Plate_Converter.md](./tools/Line_to_Plate_Converter.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60469083421593-Line-To-Plate-Converter) |
| 29 | Load Effect for Load Combination | [tools/Load_Effect_for_Load_Combination.md](./tools/Load_Effect_for_Load_Combination.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35649669387289-Load-Effect-for-Load-Combination) |
| 30 | Local Axis | [tools/Local_Axis.md](./tools/Local_Axis.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45537498601881-Local-Axis) |
| 31 | Mirror Tapered Section | [tools/Mirror_Tapered_Section.md](./tools/Mirror_Tapered_Section.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35651585867801-Mirror-Tapered-Section) |
| 32 | [MS 1553:2002] Building Wind Loads Generator | [tools/MS_15532002_Building_Wind_Loads_Generator.md](./tools/MS_15532002_Building_Wind_Loads_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/47130265330841--MS-1553-2002-Building-Wind-Loads-Generator) |
| 33 | Nastran Importer | [tools/Nastran_Importer.md](./tools/Nastran_Importer.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45548001795865-Nastran-Importer) |
| 34 | Node Controller | [tools/Node_Controller.md](./tools/Node_Controller.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35654598923161-Node-Controller) |
| 35 | P-Y Curve Generator | [tools/P_Y_Curve_Generator.md](./tools/P_Y_Curve_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/52596776672537-P-Y-Curve-Generator) |
| 36 | Rebar Auto Generator | [tools/Rebar_Auto_Generator.md](./tools/Rebar_Auto_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60470400396953-Rebar-Auto-Generator) |
| 37 | Rebar Spacing Converter | [tools/Rebar_Spacing_Converter.md](./tools/Rebar_Spacing_Converter.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35649267067545-Rebar-Spacing-Converter) |
| 38 | Response Spectrum Generator | [tools/Response_Spectrum_Generator.md](./tools/Response_Spectrum_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45716286965273-Response-Spectrum-Generator) |
| 39 | Rigid Link Generator | [tools/Rigid_Link_Generator.md](./tools/Rigid_Link_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35651417232025-Rigid-Link-Generator) |
| 40 | Seismic Hazard Map | [tools/Seismic_Hazard_Map.md](./tools/Seismic_Hazard_Map.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35658068066841-Seismic-Hazard-Map) |
| 41 | Series Load | [tools/Series_Load.md](./tools/Series_Load.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load) |
| 42 | SPACE GASS Converter | [tools/SPACE_GASS_Converter.md](./tools/SPACE_GASS_Converter.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35824220762521-SPACE-GASS-Converter) |
| 43 | Stiffness Auto Tuner | [tools/Stiffness_Auto_Tuner.md](./tools/Stiffness_Auto_Tuner.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/58178248491161-Stiffness-Auto-Tuner) |
| 44 | Substructure Generator | [tools/Substructure_Generator.md](./tools/Substructure_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60317101122329-Substructure-Generator) |
| 45 | [TAIWAN2014] Building Wind Loads Generator | [tools/TAIWAN2014_Building_Wind_Loads_Generator.md](./tools/TAIWAN2014_Building_Wind_Loads_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/52808991968665--TAIWAN2014-Building-Wind-Loads-Generator) |
| 46 | Temperature Gradient Stress Generator | [tools/Temperature_Gradient_Stress_Generator.md](./tools/Temperature_Gradient_Stress_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/40708129121817-Temperature-Gradient-Stress-Generator) |
| 47 | Temperature Load Calculator for Bridges (HK) | [tools/Temperature_Load_Calculator_for_Bridges_HK.md](./tools/Temperature_Load_Calculator_for_Bridges_HK.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/40663607747737-Temperature-Load-Calculator-for-bridges-HK) |
| 48 | Tendon Profile | [tools/Tendon_Profile.md](./tools/Tendon_Profile.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/45306728128921-Tendon-Profile) |
| 49 | Traffic Lane Generator | [tools/Traffic_Lane_Generator.md](./tools/Traffic_Lane_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/60315550956825-Traffic-Lane-Generator) |
| 50 | Thailand DPT Code Auto Searching | [tools/Thailand_DPT_Code_Auto_Searching.md](./tools/Thailand_DPT_Code_Auto_Searching.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/52715682940313-Thailand-DPT-Code-Auto-Searching) |
| 51 | Tunnel Lining Generator | [tools/Tunnel_Lining_Generator.md](./tools/Tunnel_Lining_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/35655721814937-Tunnel-Lining-Model) |
| 52 | Wind Load Calculator for Bridges (HK) | [tools/Wind_Load_Calculator_for_Bridges_HK.md](./tools/Wind_Load_Calculator_for_Bridges_HK.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/en-us/articles/40645303004697-Wind-Load-Calculator-for-bridges-HK) |
| 53 | Floor Load Table Generator | [tools/Floor_Load_Table_Generator.md](./tools/Floor_Load_Table_Generator.md) | ⚠️ 已废止（2026-08-30 确认，原文 404） | ~~[原文](https://support.midasuser.com/hc/ko/articles/49475987573657-Floor-Load-Table-Generator)~~ |
| 54 | Easy Result Table | [tools/Easy_Result_Table.md](./tools/Easy_Result_Table.md) | ⚠️ 已废止（2026-08-30 确认，原文 404） | ~~[原文](https://support.midasuser.com/hc/ko/articles/49504449511705-Easy-Result-Table)~~ |
| 55 | Bulk Tabular Result Exporter | [tools/Bulk_Tabular_Result_Exporter.md](./tools/Bulk_Tabular_Result_Exporter.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter) |
| 56 | Skew Grillage Geometry Generator | [tools/Skew_Grillage_Geometry_Generator.md](./tools/Skew_Grillage_Geometry_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator) |
| 57 | CS454 Load Assessment Combinations | [tools/CS454_Load_Assessment_Combinations.md](./tools/CS454_Load_Assessment_Combinations.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations) |
| 58 | CS454 Moving Load Generator | [tools/CS454_Moving_Load_Generator.md](./tools/CS454_Moving_Load_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/60998764028185-CS454-Moving-Load-Generator) |
| 59 | CS454 Auto Lane Generator | [tools/CS454_Auto_Lane_Generator.md](./tools/CS454_Auto_Lane_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/61259225090329-CS454-Auto-Lane-Generator) |
| 60 | Eurocode Auto Lane Generator | [tools/Eurocode_Auto_Lane_Generator.md](./tools/Eurocode_Auto_Lane_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/61259174909849-Eurocode-Auto-Lane-Generator) |
| 61 | Eurocode Load Combinations Plugin | [tools/Eurocode_Load_Combinations_Plugin.md](./tools/Eurocode_Load_Combinations_Plugin.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/61259382041369-Eurocode-Load-Combinations) |
| 62 | Eurocode Moving Load Case Generator | [tools/Eurocode_Moving_Load_Case_Generator.md](./tools/Eurocode_Moving_Load_Case_Generator.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/61259043302041-Eurocode-Moving-Load-Case-Generator) |
| 63 | Load Combination Contribution Analyzer | [tools/Load_Combination_Contribution_Analyzer.md](./tools/Load_Combination_Contribution_Analyzer.md) | ✅ 已完成 | [原文](https://support.midasuser.com/hc/ko/articles/61258768334233-Load-Combination-Contribution-Analyzer) |
| 64 | Point to Patch Convertor | — | ⬜ 待撰写 | [原文](https://support.midasuser.com/hc/en-us/articles/61486703401753-Point-to-Patch-Convertor) |
| 65 | Model Report Builder | — | ⬜ 待撰写 | [原文](https://support.midasuser.com/hc/en-us/articles/61655350763289-Model-Report-Builder) |
| 66 | RC Slab and Shell Assessment | — | ⬜ 待撰写 | [原文](https://support.midasuser.com/hc/en-us/articles/61971621469849-RC-Slab-and-Shell-Assessment) |
| 67 | Concurrent Force Reporter | — | ⬜ 待撰写 | [原文](https://support.midasuser.com/hc/en-us/articles/62123537156889-Concurrent-Force-Reporter) |

[^1]: 原文页面还以 "Image Capture Generator" 之名另列一次，但指向的是同一 URL（`35639906272025-Easy-Capture-Generator`），属同一篇文章。

> **2026-08-06 发现：** No. 53~56 共 4 篇是新发现的文章，是在落地页面（`Plug-in Online Manual`，id `35639730101529`）的 `updated_at` 更新后复核时新发现的。其中 "Floor Load Table Generator"·"Easy Result Table" 的原文生成日期为 2025-08-04/05，此前就已存在，只是近期才被链接到落地页面；"Bulk Tabular Result Exporter"·"Skew Grillage Geometry Generator" 是 2026-08-06 当天生成的新文章。
>
> **2026-08-15 发现：** No. 57~58 共 2 篇同样是在落地页面 `updated_at` 更新（2026-08-10）之际复核时发现的。两篇文章均为 2026-08-10 当天生成的新文章（"C" 分类，在落地页面按 "CS Report Generator" 之后的顺序链接），且只有英文原文存在（未提供韩文翻译）。
>
> **2026-08-24 发现：** No. 59~63 共 5 篇也是在定期检查中借落地页面 `updated_at` 更新（2026-08-10 → 2026-08-18）之际复核时发现的。5 篇均为 2026-08-18 当天生成的新文章（"C" 分类下 CS454 Auto Lane Generator，"E" 分类下 Eurocode 3 项，"L" 分类下 Load Combination Contribution Analyzer），虽仅以 `/ko/` 路径链接，但正文只用英文撰写（未提供韩文翻译）。"Eurocode Load Combinations Plugin" 一文与其他文档不同，采用的不是 GUI 用法而是版本发布说明格式，因此该文档的"使用方法"一节留空。
>
> **2026-08-30 定期检查（变更）：** 借落地页面 `updated_at` 更新（2026-08-18 → 2026-08-28）之际复核的结果，新发现 2 篇文章（"Point to Patch Convertor" 原文生成 2026-08-24，"Model Report Builder" 原文生成 2026-08-28，二者均以 No. 64~65 待撰写状态新增），同时发现原有 No. 53（"Floor Load Table Generator"）·54（"Easy Result Table"）已从落地页面的链接列表中消失。直接查询这两篇文章的结果均为 404 —— 确认已被官方站点删除，故把状态转为 ⚠️ 已废止（文档文件保留），并从 `common.py` 的 `PLUGIN_ARTICLE_IDS` 中移除了这两个 id（没有理由在每次检查时都对已无法查询的文章以 404 重复确认）。

---

## `tools/*.md` 单篇文档模板

各 Plug-in 文档不沿用 `docs/manual` 的 Key/Value 规格表惯例，而遵循以下顺序：

1. **概述** —— 本 Plug-in 做什么（Intro）
2. **支持版本** —— 原文的 "Developed with"（例：`MIDAS CIVIL NX 2026 (v1.1)`）
3. **主要功能** —— 原文若有 Benefits 一节则加以整理
4. **使用方法** —— 按 UI 选项/字段分别说明。建议采用表格式：`| 字段 | 说明 | 选项·默认值 |`
5. **参考/限制事项** —— 原文的 Note、限制条件
6. **相关 JSON API Endpoint** *（可选）* —— 若确认本 Plug-in 内部调用了
   `docs/manual/*` 的 Endpoint，则相互链接。未确认时不要凭推测填入。
7. **原文链接**

## 自动同步

与 `docs/manual` 一样，`scripts/manual_sync/` 也会一并检测本分类（`plugin`）的变更。
详细内容参见 [scripts/manual_sync/README.md](../../../scripts/manual_sync/zh-cn/README.md)。
