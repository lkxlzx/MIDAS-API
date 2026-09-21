# 09. DB – Dynamic Loads

动态荷载相关的数据库 API。  
包含反应谱（Response Spectrum）函数与荷载工况、时程（Time History）全局控制、函数、荷载工况。

> **Base URL**
> - MIDAS CIVIL NX : `https://moa-engineers.midasit.com:443/civil`
> - MIDAS GEN NX   : `https://moa-engineers.midasit.com:443/gen`
>
> **认证** ：所有请求头中需包含 `MAPI-Key: <your-api-key>`

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../09_DB_Dynamic_Loads.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 目录

| # | Endpoint | 说明 |
|---|----------|------|
| 1 | [/db/SPFC](#1-dbspfc--response-spectrum-functions) | 反应谱函数 |
| 2 | [/db/SPLC](#2-dbsplc--response-spectrum-load-cases) | 反应谱荷载工况 |
| 3 | [/db/THGC](#3-dbthgc--time-history-global-control) | 时程全局控制 |
| 4 | [/db/THGC-M1](#4-dbthgc-m1--time-history-global-control-hyper-s) | 时程全局控制（Hyper-S） |
| 5 | [/db/THOO-M1](#5-dbthoo-m1--time-history-output-option-hyper-s) | 时程输出选项（Hyper-S） |
| 6 | [/db/THIS](#6-dbthis--time-history-load-cases) | 时程荷载工况 |
| 7 | [/db/THIS-M1](#7-dbthis-m1--time-history-load-cases-hyper-s) | 时程荷载工况（Hyper-S） |
| 8 | [/db/THFC](#8-dbthfc--time-history-functions) | 时程函数 |
| 9 | [/db/THGA](#9-dbthga--ground-acceleration) | 地面加速度 |
| 10 | [/db/THNL](#10-dbthnl--dynamic-nodal-loads) | 动态节点荷载 |
| 11 | [/db/THSL](#11-dbthsl--time-varying-static-loads) | 时变静力荷载 |
| 12 | [/db/THMS](#12-dbthms--multiple-support-excitation) | 多点激励 |

---

## 1. /db/SPFC – Response Spectrum Functions

定义反应谱函数。  
`STR.SPEC_CODE` 的取值支持 User 自定义、韩国规范、美国规范、Eurocode、中国、印度、台湾等多种设计标准。

### 1-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/SPFC` | 查询全部反应谱函数 |
| `GET` | `{base_url}/db/SPFC/{id}` | 查询特定 ID 的反应谱函数 |
| `POST` | `{base_url}/db/SPFC` | 创建反应谱函数 |
| `PUT` | `{base_url}/db/SPFC` | 修改全部反应谱函数 |
| `PUT` | `{base_url}/db/SPFC/{id}` | 修改特定 ID 的反应谱函数 |
| `DELETE` | `{base_url}/db/SPFC` | 删除全部反应谱函数 |
| `DELETE` | `{base_url}/db/SPFC/{id}` | 删除特定 ID 的反应谱函数 |

### 1-2. 公共参数（所有代码类型）

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | RS 函数名 | `NAME` | String | - | Required |
| 2 | 谱数据类型（1=归一化加速度，2=加速度，3=速度，4=位移） | `iTYPE` | Integer | - | Required |
| 3 | 缩放方法（0=Scale Factor，1=Max Value） | `iMETHOD` | Integer | 0 | Optional |
| 4 | 缩放值 | `SCALE` | Number | - | Required |
| 5 | 重力加速度（仅归一化加速度类型适用） | `GRAV` | Number | - | Required |
| 6 | 阻尼比 | `DRATIO` | Number | 0.05 | Optional |
| 7 | 说明 | `DESC` | String | Blank | Optional |

---

#### 1-2-A. User Type

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 8 | 函数数据数组 | `aFUNC` | Array[Object] | - | Required |
| (1) | 周期（sec） | `PERIOD` | Number | - | Required |
| (2) | 值（随数据类型而异） | `VALUE` | Number | - | Required |

**Request Body 示例（User Type）**

```json
{
  "Assign": {
    "1": {
      "NAME": "RS_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "DESC": "",
      "aFUNC": [
        { "PERIOD": 0,    "VALUE": 0.11  },
        { "PERIOD": 0.06, "VALUE": 0.308 },
        { "PERIOD": 0.12, "VALUE": 0.308 },
        { "PERIOD": 0.3,  "VALUE": 0.308 },
        { "PERIOD": 0.36, "VALUE": 0.2567},
        { "PERIOD": 0.6,  "VALUE": 0.154 },
        { "PERIOD": 1.2,  "VALUE": 0.077 }
      ]
    }
  }
}
```

---

#### 1-2-B. Korea Type

通过 `STR` 对象的 `SPEC_CODE` 取值选择韩国设计标准。

| SPEC_CODE 取值 | 说明 |
|---|---|
| `"KDS(41-17-00:2019)"` | KDS 41 17 00 : 2019 抗震设计标准 |
| `"KDS(17-10-00:2018)"` | KDS 17 10 00 : 2018 公路桥抗震设计标准 |
| `"KS_BRG"` | 韩国桥梁标准 |
| `"KBC2016"` | KBC 2016 |
| `"KBC2009"` | KBC 2009 |
| `"KBC2005"` | KBC 2005 |
| `"KS2000"` | KS 2000 |

**KDS(41-17-00:2019) 附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 8 | 代码数据（STR 对象） | `STR` | Object | - | Required |
| (1) | 设计谱代码 | `SPEC_CODE` | `"KDS(41-17-00:2019)"` | - | Required |
| 9 | 选项数据（OPT 对象） | `OPT` | Object | - | Optional |
| (1) | 场地分类（0=S1, 1=S2, 2=S3, 3=S4, 4=S5, 5=S6） | `SC_` | Integer | 0 | Optional |
| (2) | 地震分区（0=1 区, 1=2 区） | `iSEISZONE` | Integer | 0 | Optional |
| 10 | 系数数据（VAL 对象） | `VAL` | Object | - | Required |
| (1) | 谱反应加速度 [Sds, Sd1] | `aSRA` | Array[Number, 2] | - | Required |
| (2) | 场地放大系数 [Fa, Fv] | `aSCP` | Array[Number, 2] | - | Required |
| (3) | 最大周期 | `PERIOD` | Number | - | Required |
| (4) | 重要性系数 (Ie) | `IE` | Number | - | Required |
| (5) | 反应修改系数 (R) | `R_` | Number | - | Required |
| (6) | EPA（分区系数） | `ZONEFACTOR` | Number | - | Required |
| 11 | 计算选项 | `CALC_OPT` | Boolean | false | Create Only |

**KDS(17-10-00:2018) 附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| (1) | 场地分类（0=S1 ~ 5=S6） | `SC_` | Integer | 0 | Optional |
| (2) | 地震分区（0=1 区, 1=2 区） | `iSEISZONE` | Integer | 0 | Optional |
| VAL.(1) | 场地放大系数 [Fa, Fv] | `aSCP` | Array[Number, 2] | - | Required |
| VAL.(2) | 最大周期 | `PERIOD` | Number | - | Required |
| VAL.(3) | 地震危险系数 (I) | `IE` | Number | - | Required |

**KS_BRG（韩国桥梁）附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| VAL.(1) | 地震分区系数 (Ar)：Area I=0.11, Area II=0.07 | `EPA` | Number | - | Required |
| VAL.(2) | 最大周期 | `PERIOD` | Number | - | Required |
| VAL.(3) | 场地剖面类型（S1=1.0, S2=1.2, S3=1.5, S4=2.0） | `SPTYPE` | Number | - | Required |
| VAL.(4) | 重要性系数 (I) | `IE` | Number | - | Required |
| VAL.(5) | 反应修改系数 (R) | `R_` | Number | - | Required |

**Request Body 示例（KDS 41-17-00:2019）**

```json
{
  "Assign": {
    "2": {
      "NAME": "KDS_2019_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "KDS(41-17-00:2019)" },
      "OPT": { "SC_": 2, "iSEISZONE": 0 },
      "VAL": {
        "aSRA": [0.22, 0.154],
        "aSCP": [1.0, 1.5],
        "PERIOD": 4.0,
        "IE": 1.2,
        "R_": 5.0,
        "ZONEFACTOR": 0.22
      }
    }
  }
}
```

---

#### 1-2-C. US Type

| SPEC_CODE 取值 | 说明 |
|---|---|
| `"AASHTO-LRFD12"` | AASHTO LRFD 2012 |
| `"IBC2012"` | IBC 2012 |
| `"IBC2009"` | IBC 2009 |
| `"IBC2000"` | IBC 2000 |
| `"UBC97"` | UBC 1997 |
| `"UBC88"` | UBC 1988 |

**Request Body 示例（IBC 2012）**

```json
{
  "Assign": {
    "3": {
      "NAME": "IBC2012_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "IBC2012" },
      "OPT": { "SC_": 2 },
      "VAL": {
        "aSRA": [0.5, 0.2],
        "aSCP": [1.0, 1.5],
        "PERIOD": 4.0,
        "IE": 1.0,
        "R_": 5.0
      }
    }
  }
}
```

---

#### 1-2-D. Eurocode Type

| SPEC_CODE 取值 | 说明 |
|---|---|
| `"EURO2004"` | Eurocode 8 (2004) |
| `"EURO1996"` | Eurocode 8 (1996) |
| `"EURO1996_ELA"` | Eurocode 8 (1996) Elastic |

**EURO2004 主要附加参数**

| 说明 | Key | 备注 |
|------|-----|------|
| 谱类型（1=Elastic, 2=Design） | `SPECTYPE` | OPT 对象 |
| 场地类型（0=A, 1=B, 2=C, 3=D, 4=E） | `GROUTYPE` | OPT 对象 |
| 国家附录代码 | `NATIONALANNEX` | OPT 对象 |

**Request Body 示例（EURO2004）**

```json
{
  "Assign": {
    "4": {
      "NAME": "EURO2004_func",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "EURO2004" },
      "OPT": {
        "SPECTYPE": 1,
        "GROUTYPE": 1,
        "NATIONALANNEX": "EN"
      },
      "VAL": {
        "ag": 0.25,
        "PERIOD": 4.0,
        "IE": 1.0
      }
    }
  }
}
```

---

#### 1-2-E. China Type

> ⚠️ 2026-08-25 确认：此前的文档完全没有文档化 China/Japan/Taiwan/India/Other Countries Type
> （与 MVHL 同一类型的遗漏）。按原文
> [Response Spectrum Functions - China](https://support.midasuser.com/hc/en-us/articles/39473334759065)
> 为准，9 个代码中仅对最新、最具代表性的 GB50011-2010 文档化全部字段，其余 8 个
> 整理为 SPEC_CODE 映射表（SECT/TDMT 原则）。

| SPEC_CODE 取值 | 说明 |
| --- | --- |
| `"CH2010"` | China (GB50011-2010) — 下方代表性示例 |
| `"GB50111_2006"` | China (GB50111-2006) |
| `"CH2001"` | China (GB50011-2001) |
| `"CHSH2003"` | China Shanghai (DGJ08-9-2003) |
| `"CH_BRG89"` | China (JTJ004-89) |
| `"JTG/T 2231-01-2020"` | China (JTG/T 2231-01-2020) |
| `"JTG/T B02-01-2008"` | China (JTG/T B02-01-2008) |
| `"CH_GBJ111_87"` | China (GBJ11-87) |
| `"CJJ 166-2011"` | China (CJJ 166-2011) |

**GB50011-2010 附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 8-(2) | 抗震设防烈度（Seismic Fortification Intensity） | `SFI`(STR) | String | `"0.05g"` | Optional |
| 8-(3) | 场地类别（I0/I1/II/III/IV） | `SC_`(STR) | String | `"I0"` | Optional |
| 8-(4) | 地震影响（Frequent/Middle/Scarce） | `EQ_`(STR) | String | – | Required |
| 9-(1) | 震源类型（0/1/2） | `NSC`(OPT) | Integer | 0 | Optional |
| 9-(2) | 名义水平力（0=剪力法, 1=惯性力） | `nLForce`(OPT) | Integer | 0 | Optional |
| 10-(1) | 设计特征周期 [Tg, Tg1, Tg2]（GB50011-2010 仅使用 Tg） | `aTG`(VAL) | Array[Number,3] | – | Required |
| 10-(2) | 阻尼比 | `DP`(VAL) | Number | – | Required |
| 10-(3) | 最大地震影响系数 | `MaxEQ`(VAL) | Number | – | Required |
| 10-(4) | 最大周期 | `PERIOD`(VAL) | Number | – | Required |

**Request Body 示例（GB50011-2010）**

```json
{
  "Assign": {
    "5": {
      "NAME": "China(GB50011-10)",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "CH2010", "SFI": "0.10g", "SC_": "II", "EQ_": "MIDDLE" },
      "OPT": { "NSC": 1, "nLForce": 0 },
      "VAL": { "aTG": [0.4, 0, 0], "DP": 0.05, "MaxEQ": 0.23, "PERIOD": 6 },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-F. Japan Type

| SPEC_CODE 取值 | 说明 |
| --- | --- |
| `"JPN2000"` | Japan (Arch. 2000) |
| `"JP_BRG2017"` | Japan (Bridge 2017, MIDAS CIVIL NX JP 版本专用) |
| `"JP_BRG2012"` | Japan (Bridge 2012, MIDAS CIVIL NX JP 版本专用) |
| `"JP_BRG2002"` | Japan (Bridge 2002) |

**JPN2000(Arch.2000) 附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 地震地区系数（Z）0=1.0/1=0.9/2=0.8/3=0.7 | `iSEISZONEFACTOR`(OPT) | Integer | 0 | Optional |
| 9-(2) | 场地类别（I/II/III） | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 10-(1) | 最大周期 | `PERIOD`(VAL) | Number | – | Required |
| 10-(2) | 基底剪力系数（Co） | `CO`(VAL) | Number | – | Required |

**Bridge2017/2012/2002 公共附加参数**（仅 SPEC_CODE 不同）

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 场地类别（I/II/III） | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 9-(2) | 地震地区（Bridge2017/2012: A1/A2/B1/B2/C, Bridge2002: A/B/C） | `iSEISZONE`(OPT) | Integer | 0 | Optional |
| 9-(3) | 地震输入方法（Level1/Level2 Type I/Level2 Type II） | `iEQMETHOD`(OPT) | Integer | 0 | Optional |
| 10-(1) | 最大周期 | `PERIOD`(VAL) | Number | – | Required |
| 10-(2) | 修正系数（Cz）— ⚠️ MIDAS 会以其他取值自动计算，输入值被忽略 | `CZ`(VAL) | Number | – | Required |

**Request Body 示例（JPN2000）**

```json
{
  "Assign": {
    "6": {
      "NAME": "JP2000",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "JPN2000" },
      "OPT": { "iSEISZONEFACTOR": 2, "SOILCLASS": 1 },
      "VAL": { "PERIOD": 6, "CO": 0.2 },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-G. Taiwan Type

> ⚠️ 原文 [Response Spectrum Functions - Taiwan](https://support.midasuser.com/hc/en-us/articles/39473471043737)
> 本身是涵盖 7 个代码的长篇文档，因此仅对最新的 Taiwan(2022) 文档化全部字段。

| SPEC_CODE 取值 | 说明 |
| --- | --- |
| `"TAIWAN(2022)"` | Taiwan 2022 — 下方代表性示例 |
| `"TAIWAN06"` | Taiwan 2006 |
| `"TAIWAN99H"` | Taiwan 1999 Horizontal |
| `"TAIWAN99V"` | Taiwan 1999 Vertical |
| `"TAIWAN(2011)"` | Taiwan Bridge 98 |
| `"TAIWAN89H_BRG"` | Taiwan Bridge 89 Horizontal |
| `"TAIWAN89V_BRG"` | Taiwan Bridge 89 Vertical |

**Taiwan(2022) 附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 场地类别（Type1/2/3/User Input） | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 9-(2) | 地震分区（General/Near Fault/Taipei Basin） | `iSEISZONE`(OPT) | Integer | 0 | Optional |
| 9-(3) | 谱方向（0=水平/1=竖直） | `iSPECTYPE`(OPT) | Integer | 0 | Optional |
| 9-(4) | 谱用途（0=Design/1=Small-Medium/2=Maximum） | `iSPECUSE`(OPT) | Integer | 0 | Optional |
| 9-(5) | 细分分区（Taipei Basin I~IV/User Input，分区为 Taipei Basin 时） | `iSUBZONE`(OPT) | Integer | 0 | Optional |
| 10-(1) | 水平谱加速度 [Sds,Sd1,Sms,Sm1]（General/Near Fault 分区） | `aSRA`(VAL) | Array[Number,4] | – | Required |
| 10-(2) | 台北盆地谱加速度 [Sds_t,Sd1_t,Sms_t,Sm1_t]（Taipei Basin 分区） | `aSRA_T`(VAL) | Array[Number,4] | – | Required |
| 10-(3) | 近断层地震影响 [Nda,Ndv,Nma,Nmv]（Near Fault 分区） | `aNSF`(VAL) | Array[Number,4] | – | Required |
| 10-(4) | 场地放大系数 [Fda,Fdv,Fma,Fmv]（General/Near Fault 分区） | `aSMF`(VAL) | Array[Number,4] | – | Required |
| 10-(5) | 阻尼比（%） | `DP`(VAL) | Number | – | Required |
| 10-(6) | 最大周期 | `PERIOD`(VAL) | Number | – | Required |
| 10-(7) | 重要性系数（I） | `IF`(VAL) | Number | – | Required |
| 10-(8) | 地震放大系数（ay） | `SMFACTOR`(VAL) | Number | – | Required |
| 10-(9) | 反应修改系数（R） | `RMFACTOR`(VAL) | Number | – | Required |
| 10-(10) | 基本周期（T1） | `FUNDAMENTAL_PERIOD`(VAL) | Number | – | Required |

**Request Body 示例（Taiwan 2022, Near Fault Zone）**

```json
{
  "Assign": {
    "7": {
      "NAME": "Taiwan(2022)",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "TAIWAN(2022)" },
      "OPT": {"SOILCLASS": 0, "iSEISZONE": 1, "iSPECTYPE": 0, "iSPECUSE": 1, "iSUBZONE": 0},
      "VAL": {
        "aSRA": [0.5, 0.3, 0.7, 0.4],
        "aSRA_T": [0.6, 0.8, 1.6, 1.6],
        "aNSF": [0.8, 0.45, 1, 0.6],
        "aSMF": [1, 1, 1, 1],
        "DP": 5, "PERIOD": 6, "IF": 1, "SMFACTOR": 1, "RMFACTOR": 1.6,
        "FUNDAMENTAL_PERIOD": 0.09
      },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-H. India Type

| SPEC_CODE 取值 | 说明 |
| --- | --- |
| `"IS1893(2016)"` | India (IS1893:2016) |
| `"IS2002"` | India (IS1893:2002) |
| `"IRC:SP:114-2018"` | India (IRC:SP:114-2018) |

**公共附加参数（3 个代码通用）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 场地类别（I=Rock/Hard·II=Medium·III=Soft） | `SOILCLASS`(OPT) | Integer | 0 | Optional |
| 9-(2) | 地震分区（II 0.10/III 0.16/IV 0.24/V 0.36，IRC:SP:114-2018 还支持 User Defined=4） | `iSEISZONE`(OPT) | Integer | 0 | Optional |
| 10-(1) | 阻尼比（%） | `DP`(VAL) | Number | – | Required |
| 10-(2) | 最大周期 | `PERIOD`(VAL) | Number | – | Required |
| 10-(3) | 重要性系数（I） | `IE`(VAL) | Number | – | Required |
| 10-(4) | 反应降低系数（R） | `R_`(VAL) | Number | – | Required |
| 10-(5) | 阻尼倍数系数（固定为值 1） | `DPFAC`(VAL) | Integer | – | Required |
| 10-(6) | 用户自定义地震分区取值（IRC:SP:114-2018，仅 `iSEISZONE`=4 时） | `USERDEFSEISZONE`(VAL) | Number | – | Required |

**Request Body 示例（IS1893:2016）**

```json
{
  "Assign": {
    "8": {
      "NAME": "IS1893(2016)",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "IS1893(2016)" },
      "OPT": { "SOILCLASS": 0, "iSEISZONE": 0 },
      "VAL": { "DP": 5, "PERIOD": 6, "IE": 1, "R_": 3, "DPFAC": 1 },
      "CALC_OPT": true
    }
  }
}
```

---

#### 1-2-I. Other Countries Type

> ⚠️ 原文 [Response Spectrum Functions - Other Countries](https://support.midasuser.com/hc/en-us/articles/39508838720153)
> 是涵盖 8 个国家代码的长篇文档，因此仅对字段最简单的 Canada(NBC95) 完整文档化，
> 其余仅保留 SPEC_CODE 映射。

| SPEC_CODE 取值 | 说明 |
| --- | --- |
| `"NBC95"` | Canada (NBC 1995) — 下方代表性示例 |
| `"NTC2018"` | Italy (NTC 2018) |
| `"DPWH-LRFD BSDS(2013)"` | Philippines (DPWH-LRFD BSDS 2013) |
| `"AS 5100.2(2017)"` | Australia (AS 5100.2:2017) |
| `"NSR-10"` | Colombia (NSR-10) |
| `"P100-1(2013)"` | Romania (P100-1:2013) |
| `"SP 268.1325800.2016"` | Russia (SP 268.1325800.2016) |
| `"DPT.1301/1302-61:2018"` | Thailand (DPT.1301/1302-61:2018) |

**Canada NBC95 附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
| --- | --- | --- | --- | --- | --- |
| 9-(1) | 加速度分区（Za, 0~6） | `ZA`(OPT) | Integer | 0 | Optional |
| 9-(2) | 速度分区（Zv, 0~6） | `ZV`(OPT) | Integer | 0 | Optional |
| 10-(1) | 最大周期 | `PERIOD`(VAL) | Number | – | Required |
| 10-(2) | 分区速度比（v） | `V`(VAL) | Number | – | Required |

**Request Body 示例（Canada NBC95）**

```json
{
  "Assign": {
    "9": {
      "NAME": "NBC1995",
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "DRATIO": 0.05,
      "STR": { "SPEC_CODE": "NBC95" },
      "OPT": { "ZA": 2, "ZV": 3 },
      "VAL": { "PERIOD": 6, "V": 0.15 },
      "CALC_OPT": true
    }
  }
}
```

---

### 1-3. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 1) 创建 User Type 反应谱函数 ────────────────────────────────────
payload_user = {
    "Assign": {
        "1": {
            "NAME": "RS_UserDefined",
            "iTYPE": 1,       # Normalized Acceleration
            "iMETHOD": 0,     # Scale Factor
            "SCALE": 1.0,
            "GRAV": 9.806,
            "DRATIO": 0.05,
            "aFUNC": [
                {"PERIOD": 0.0,  "VALUE": 0.110},
                {"PERIOD": 0.06, "VALUE": 0.308},
                {"PERIOD": 0.12, "VALUE": 0.308},
                {"PERIOD": 0.30, "VALUE": 0.308},
                {"PERIOD": 0.60, "VALUE": 0.154},
                {"PERIOD": 1.20, "VALUE": 0.077},
                {"PERIOD": 4.00, "VALUE": 0.023}
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/SPFC", json=payload_user, headers=HEADERS)
print("User SPFC POST:", resp.status_code)

# ── 2) 创建 KDS 41-17-00:2019 反应谱函数 ────────────────────────────
payload_kds = {
    "Assign": {
        "2": {
            "NAME": "RS_KDS2019",
            "iTYPE": 1,
            "iMETHOD": 0,
            "SCALE": 1.0,
            "GRAV": 9.806,
            "DRATIO": 0.05,
            "STR": {"SPEC_CODE": "KDS(41-17-00:2019)"},
            "OPT": {"SC_": 2, "iSEISZONE": 0},
            "VAL": {
                "aSRA": [0.22, 0.154],
                "aSCP": [1.0, 1.5],
                "PERIOD": 4.0,
                "IE": 1.2,
                "R_": 5.0,
                "ZONEFACTOR": 0.22
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/SPFC", json=payload_kds, headers=HEADERS)
print("KDS SPFC POST:", resp.status_code)

# ── 3) 查询全部 ─────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/SPFC", headers=HEADERS)
print("SPFC GET:", resp.status_code, resp.json())

# ── 4) 删除特定 ID ──────────────────────────────────────────────────────────
resp = requests.delete(f"{BASE_URL}/db/SPFC/1", headers=HEADERS)
print("SPFC DELETE/1:", resp.status_code)
```

---

## 2. /db/SPLC – Response Spectrum Load Cases

定义反应谱荷载工况。

### 2-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/SPLC` | 查询全部 |
| `GET` | `{base_url}/db/SPLC/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/SPLC` | 创建 |
| `PUT` | `{base_url}/db/SPLC` | 修改全部 |
| `PUT` | `{base_url}/db/SPLC/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/SPLC` | 删除全部 |
| `DELETE` | `{base_url}/db/SPLC/{id}` | 删除特定 ID |

### 2-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 荷载工况名 | `NAME` | String | - | Required |
| 2 | 说明 | `DESC` | String | Blank | Optional |
| 3 | 方向（`"XY"` 或 `"Z"`） | `DIR` | String | `"XY"` | Optional |
| 4 | 激励角度 | `ANGLE` | Number | 0 | Optional |
| 5 | 缩放系数 | `SCALE` | Number | - | Required |
| 6 | 周期修正系数 | `PMFT` | Number | - | Required |
| 7 | 谱函数名列表 | `aFUNCNAME` | Array[String] | - | Required |
| 8 | 谱数据插值方法（`"LINEAR"` / `"LOG"`） | `INTERP` | String | `"LINEAR"` | Optional |
| 9 | 振型组合方法（`"SRSS"` / `"CQC"` / `"ABS"` / `"Linear"`） | `COMTYPE` | String | `"CQC"` | Optional |
| 10 | 结果添加符号 | `bADDSIGN` | Boolean | false | Optional |
| 11 | 添加符号方法（0=主振型方向，1=绝对最大值方向） | `iSIGNTYPE` | Integer | 1 | Optional |
| 12 | 振型选择 | `bMODE` | Boolean | - | Optional |
| 13 | 所用振型列表 | `aUSEMODE` | Array[Object] | - | Optional |
| (1) | 是否使用该振型 | `bUSE` | Boolean | - | Optional |
| (2) | 振型系数 | `MSFACTOR` | Number | - | Optional |
| 14 | 是否应用阻尼方法 | `bDAMP` | Boolean | false | Optional |
| 15 | 是否修正阻尼比 | `bCDAMP` | Boolean | false | Optional |
| 16 | 阻尼方法（1=Modal, 2=Mass&Stiff, 3=StrainEnergy） | `iMDTYPE` | Integer | - | Required（bDAMP=true 时） |

**Modal 阻尼附加参数**

| 说明 | Key | 值类型 |
|------|-----|------------|
| 全部振型阻尼比 | `DALL` | Number |
| 各振型阻尼比列表 | `aDAMPING` | Array[Object] |
| - 振型编号 | `iMODE` | Integer |
| - 阻尼比 | `DAMPING` | Number |

**Mass & Stiffness Proportional 阻尼附加参数**

| 说明 | Key | 值类型 | 备注 |
|------|-----|------------|------|
| 阻尼类型（1=直接指定，2=由模态阻尼计算） | `iCOEF` | Integer | Required |
| 是否质量比例 | `bMASSP` | Boolean | - |
| 是否刚度比例 | `bSTIFFP` | Boolean | - |
| 质量比例系数（iCOEF=1） | `MASSC` | Number | - |
| 刚度比例系数（iCOEF=1） | `STIFFC` | Number | - |
| 计算方法（1=频率，2=周期） | `iCALC` | Integer | iCOEF=2 时 |
| 振型 1 频率/周期 | `FP1` | Number | iCOEF=2 时 |
| 振型 2 频率/周期 | `FP2` | Number | iCOEF=2 时 |
| 振型 1 阻尼比 | `DR1` | Number | iCOEF=2 时 |
| 振型 2 阻尼比 | `DR2` | Number | iCOEF=2 时 |

**偶然偏心（Accidental Eccentricity）参数** *(GEN NX only)*

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 24 | 应用偶然偏心 | `bACCECC` | Boolean | false | Optional |
| 25 | 偏心数据（true=自动，false=用户自定义） | `bACCECC_AUTO` | Boolean | - | Required |
| 26 | 偏心比例 | `ACCECC_PERCENT` | Number | - | Required |
| 27 | 是否考虑 GL 以下偏心 | `bACCECC_CONSIDER_GL` | Boolean | - | Required |
| 28 | 最小偶然扭转力矩限制 | `bACCECC_MINIMUM_TORSION` | Boolean | - | Required |
| 29 | 偏心列表 | `aACCECC_ECCEN_LIST` | Array[Object] | - | Required |
| (1) | 楼层名称 | `STORY` | String | - | Required |
| (2) | Cross 方向位置 | `CROSS` | Number | - | Required |
| (3) | Along 方向位置 | `ALONG` | Number | - | Required |

> ✅ **2026-09-06 核实已解决：** 此前（2026-08-25）原文 Specifications 表把 `ACCECC_PERTCENT`
> （拼写错误）与第 28 项 Key 重复误写为同第 27 项的 `bACCECC_CONSIDER_GL`；由于该字段无请求
> 示例，曾依据 JSON Schema 予以更正。2026-09-01 原文更新后**两处均已更正**
> （再次确认：`ACCECC_PERCENT` 2 次·`PERTCENT` 0 次，`bACCECC_MINIMUM_TORSION` 2 次）。上表原本即为
> 正确写法，故不作修改（原文
> [Response Spectrum Load Cases](https://support.midasuser.com/hc/en-us/articles/35963719599641)).
>
> ⚠️ 剩余不一致：29-(3) 偏心列表的 Key，原文表写作 `"Along"`，JSON Schema 写作 `"ALONG"`（无请求示例）。
> 上表按 Schema 取 `ALONG` — 属待报告的剩余错误。
>
> ✅ **2026-09-18 经实机验证确认 Schema 写法正确。** 以 `aACCECC_ECCEN_LIST[0].ALONG`
> （大写）发送的取值被原样保存并原样查询。原文表的 `"Along"` 写法有误，上表
> 保持原样即可，请勿回退。验证详见
> [live_verification_feedback_20260918.md](../../zh-cn/error_reports/live_verification_feedback_20260918.md)。

**非耗能构件设计参数** *(GEN NX only)*

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 30 | 非耗能构件设计 | `bNDP` | Boolean | false | Optional |
| (1) | 非耗能系数 | `NDP` | Number | - | Required |

### 2-3. Request Body 示例

**基本（无阻尼）**

```json
{
  "Assign": {
    "1": {
      "NAME": "LC_RS_XY",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": false,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [
        {"bUSE": true, "MSFACTOR": 1},
        {"bUSE": true, "MSFACTOR": 1},
        {"bUSE": true, "MSFACTOR": 1}
      ]
    }
  }
}
```

**应用 Modal 阻尼**

```json
{
  "Assign": {
    "2": {
      "NAME": "LC_RS_Modal_Damp",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": true,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [
        {"bUSE": true, "MSFACTOR": 1},
        {"bUSE": true, "MSFACTOR": 1}
      ],
      "bCDAMP": true,
      "iMDTYPE": 1,
      "DALL": 0.05,
      "aDAMPING": [
        {"iMODE": 1, "DAMPING": 0.06},
        {"iMODE": 2, "DAMPING": 0.07}
      ]
    }
  }
}
```

**Mass & Stiffness Proportional 阻尼（直接指定）**

```json
{
  "Assign": {
    "3": {
      "NAME": "LC_RS_M_S_Direct",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": true,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [{"bUSE": true, "MSFACTOR": 1}],
      "bCDAMP": false,
      "iMDTYPE": 2,
      "iCOEF": 1,
      "bMASSP": true,
      "MASSC": 1.1,
      "bSTIFFP": true,
      "STIFFC": 1.2
    }
  }
}
```

**Mass & Stiffness Proportional 阻尼（由模态阻尼计算）**

```json
{
  "Assign": {
    "4": {
      "NAME": "LC_RS_M_S_Calc",
      "DIR": "Z",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": true,
      "INTERP": "LOG",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": ["RS_func"],
      "aUSEMODE": [{"bUSE": true, "MSFACTOR": 1}],
      "bCDAMP": false,
      "iMDTYPE": 2,
      "iCOEF": 2,
      "bMASSP": true,
      "bSTIFFP": true,
      "iCALC": 1,
      "FP1": 0.6,
      "FP2": 0.7,
      "DR1": 0.05,
      "DR2": 0.06
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

# ── 创建反应谱荷载工况 ──────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "RS_EQ_X",
            "DIR": "XY",
            "ANGLE": 0.0,
            "SCALE": 1.0,
            "PMFT": 1.0,
            "bDAMP": True,
            "INTERP": "LOG",
            "COMTYPE": "CQC",
            "bADDSIGN": True,
            "iSIGNTYPE": 0,
            "bMODE": True,
            "aFUNCNAME": ["RS_KDS2019"],
            "aUSEMODE": [
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1}
            ],
            "bCDAMP": True,
            "iMDTYPE": 1,      # Modal 阻尼
            "DALL": 0.05,
            "aDAMPING": []
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/SPLC", json=payload, headers=HEADERS)
print("SPLC POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/SPLC", headers=HEADERS)
print("SPLC GET:", resp.json())

# ── 修改特定 ID ─────────────────────────────────────────────────────────────
payload["Assign"]["1"]["SCALE"] = 1.2
resp = requests.put(f"{BASE_URL}/db/SPLC/1", json=payload, headers=HEADERS)
print("SPLC PUT/1:", resp.status_code)
```

---

## 3. /db/THGC – Time History Global Control

定义时程分析全局控制参数。

> **CIVIL NX 专用**（GEN NX 不可使用）

### 3-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THGC` | 查询全局控制 |
| `POST` | `{base_url}/db/THGC` | 创建全局控制 |
| `PUT` | `{base_url}/db/THGC` | 修改全局控制 |
| `DELETE` | `{base_url}/db/THGC` | 删除全局控制 |

### 3-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 几何非线性类型（0=None, 1=Large Disp, 2=P-Delta） | `GNT` | Integer | - | Required |
| 2 | 初始荷载类型（0=非线性静力分析，1=引入静力/施工阶段结果） | `ILT` | Integer | 0 | Required |
| 3 | 初始荷载列表 | `aILL` | Array[Object] | [] | Optional |
| (1) | 静力荷载工况名 | `SLC` | String | - | Required |
| (2) | 缩放系数 | `SF` | Real | - | Required |
| (3) | 荷载工况类型（1=Static, 18=Construction） | `LCT` | Integer | - | Required |
| 4 | NL 初始荷载忽略单元选项 | `IEPI` | Boolean | true | Optional |
| 5 | 增量步数 | `NSTEP` | Integer | 1 | Optional |
| 6 | 结果输出方式（false=仅最终步，true=按步增量） | `bROT` | Boolean | false | Optional |
| 7 | 输出步增量数 | `SNIO` | Integer | 1 | Optional |
| 8 | 允许收敛失败 | `bPCF` | Boolean | true | Required |
| 9 | 最大子步数 | `MAXNS` | Integer | 10 | Required |
| 10 | 最大迭代次数 | `MAXIT` | Integer | 10 | Required |
| 11 | 使用位移范数 | `bDN` | Boolean | true | Optional |
| 12 | 使用荷载范数 | `bFN` | Boolean | false | Optional |
| 13 | 使用能量范数 | `bEN` | Boolean | false | Optional |
| 14 | 位移范数值 | `DN` | Real | 0.001 | Optional |
| 15 | 荷载范数值 | `FN` | Real | 0 | Optional |
| 16 | 能量范数值 | `EN` | Real | 0 | Optional |
| 17 | 使用线性搜索方法 | `bULSM` | Boolean | false | Optional |
| 18 | 线性搜索起始迭代数 | `ULSM` | Integer | 5 | Optional |
| 19 | 输出时程能量结果 | `ENERGYRESULT` | Boolean | true | Optional |
| 20 | 黏性阻尼器 / 油阻尼器结果 | `SDVI` | Boolean | true | Optional |
| 21 | 黏弹性阻尼器结果 | `SDVE` | Boolean | true | Optional |
| 22 | 钢阻尼器结果 | `SDST` | Boolean | true | Optional |
| 23 | 滞回隔震装置结果 | `SDHY` | Boolean | true | Optional |
| 24 | 隔震装置结果 | `SDIS` | Boolean | true | Optional |
| 25 | 模型屈服状态 | `bMSSSTATUS` | Boolean | true | Optional |

### 3-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "GNT": 0,
      "ILT": 0,
      "aILL": [
        {"SLC": "Pretension",   "SF": 1.0, "LCT": 1},
        {"SLC": "EarthPressure","SF": 1.2, "LCT": 1}
      ],
      "IEPI": true,
      "NSTEP": 1,
      "bROT": false,
      "SNIO": 1,
      "bPCF": true,
      "MAXNS": 10,
      "MAXIT": 10,
      "bDN": true,
      "bFN": false,
      "bEN": false,
      "DN": 0.001,
      "FN": 0.001,
      "EN": 0.001,
      "bULSM": false,
      "ULSM": 5,
      "ENERGYRESULT": false,
      "SDVI": false,
      "SDVE": false,
      "SDST": false,
      "SDHY": false,
      "SDIS": false,
      "bMSSSTATUS": false
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

# ── 创建时程全局控制 ──────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "GNT": 0,           # 无几何非线性
            "ILT": 0,           # 以非线性静力分析处理初始荷载
            "aILL": [
                {"SLC": "DL", "SF": 1.0, "LCT": 1}
            ],
            "IEPI": True,
            "NSTEP": 1,
            "bROT": False,
            "SNIO": 1,
            "bPCF": True,
            "MAXNS": 10,
            "MAXIT": 30,
            "bDN": True,
            "bFN": True,
            "bEN": False,
            "DN": 0.001,
            "FN": 0.001,
            "EN": 0.001,
            "bULSM": True,
            "ULSM": 5,
            "ENERGYRESULT": True,
            "SDVI": True,
            "SDVE": True,
            "SDST": True,
            "SDHY": True,
            "SDIS": True,
            "bMSSSTATUS": True
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THGC", json=payload, headers=HEADERS)
print("THGC POST:", resp.status_code)
```

---

## 4. /db/THGC-M1 – Time History Global Control (Hyper-S)

定义 Hyper-S 非线性时程全局控制。

> **CIVIL NX 专用**（GEN NX 不可使用）

### 4-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THGC-M1` | 查询 |
| `PUT` | `{base_url}/db/THGC-M1` | 修改 |
| `DELETE` | `{base_url}/db/THGC-M1` | 删除 |

### 4-2. 参数

**主参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 几何非线性类型（0=None, 1=Large Disp, 2=P-Delta） | `GEO_NONL_TYPE` | Integer(enum) | - | Required |
| 2 | 初始荷载类型（0=非线性静力分析，0=引入静力/施工阶段结果） | `INIT_LOAD_TYPE` | Integer(enum) | - | Required |
| 3 | 初始荷载列表 | `INIT_LOAD_LIST` | Array[Object] | - | Optional |
| (1) | 荷载工况名 | `LC_NAME` | String | - | Required |
| (2) | 缩放系数 | `SF` | Number | - | Required |
| (3) | 荷载工况类型 | `LC_TYPE` | String | - | Required |
| 4 | 初始荷载工况增量步 | `INCREMENT_STEP` | Object | - | Optional |
| 5 | 迭代参数 | `ITER_PARAM` | Object | - | Required |
| 6 | 非线性分析初始荷载是否忽略单元 | `IGNORE_ELEM` | Boolean | false | Optional |
| 7 | 适用位移基准（0=未变形，1=变形） | `SEQ_LOAD_TYPE` | Integer(enum) | 1 | Optional |
| 8 | 非弹性铰数据选项 | `HINGE_OPT` | Object | - | Optional |

**INCREMENT_STEP 子参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 增量步数 | `NSTEP` | Integer | 1 | Optional |
| 结果输出类型（0=仅最终步，1=按步增量） | `OUT_TYPE` | Integer(enum) | 0 | Optional |
| 步增量数（OUT_TYPE=1 时） | `STEP_INC` | Integer | 1 | Required |

**ITER_PARAM 子参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| 允许收敛失败 | `PERMIT_FAIL` | Boolean | true | Optional |
| 最大迭代次数 | `MAX_ITER` | Integer | - | Required |
| 收敛判定基准（NORM_CTRL） | `NORM_CTRL` | Object | - | Optional |
| - 位移范数 | `DISP` → `{OPT_USE, VALUE}` | Object | - | Optional |
| - 荷载范数 | `FORCE` → `{OPT_USE, VALUE}` | Object | - | Optional |
| - 能量范数 | `ENERGY` → `{OPT_USE, VALUE}` | Object | - | Optional |
| 刚度更新方式（0=Custom, 1=FullNR, 2=InitStiff） | `STIFF_UPD_SCHEME` | Integer(enum) | 1 | Optional |
| 刚度更新前迭代次数（STIFF_UPD_SCHEME=0 时） | `ITER_BEF_UPDATE` | Integer | 5 | Required |
| 最大二分法层级 | `MAX_BISECT_LEVEL` | Integer | 5 | Optional |
| 智能二分法 | `SMART_BISECT` | Boolean | false | Optional |
| 发散阈值 | `DIVERGENCE_THRESHOLD` | Number | 3 | Optional |
| 线性搜索选项（LINE_SEARCH） | `LINE_SEARCH` | Object | - | Optional |
| - 是否使用线性搜索 | `OPT_USE` | Boolean | true | Required |
| - 线性搜索选项（0=自动，1=用户自定义） | `LINE_SEARCH_OPT` | Integer(enum) | 0 | Required |
| - 线性搜索起始迭代编号 | `START_ITER_NO` | Integer | - | Required |
| - 最大线性搜索迭代次数 | `MAX_LINE_SEARCH_ITER` | Integer | - | Required |
| - 线性搜索容差 | `LINE_SEARCH_TOL` | Number | - | Required |

**HINGE_OPT 子参数**

| 说明 | Key | 值类型 | 默认值 | 必填 |
|------|-----|------------|---------|----------|
| Point Spring Support（0=应用非线性特性，1=按线性处理） | `PSPRING_SUP` | Integer(enum) | 0 | Optional |
| Elastic Link（0=应用非线性特性，1=按线性处理） | `EL` | Integer(enum) | 1 | Optional |

> ⚠️ 2026-08-25 确认：此前文档仅把 `PSPRING_SUP` 记作“P-弹簧支点处理”、把 `EL` 记作“单元数据”，
> 其实际含义（二者均为 0/1 enum — 是否应用非线性特性）与默认值均被遗漏。按原文
> [Time History Global Control (THGC-M1)](https://support.midasuser.com/hc/en-us/articles/56510942223513)
> 予以更正。

### 4-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "GEO_NONL_TYPE": 1,
      "INIT_LOAD_TYPE": 0,
      "INIT_LOAD_LIST": [
        {"LC_NAME": "DL", "SF": 0.75, "LC_TYPE": "ST"}
      ],
      "INCREMENT_STEP": {
        "NSTEP": 10,
        "OUT_TYPE": 1,
        "STEP_INC": 1
      },
      "ITER_PARAM": {
        "PERMIT_FAIL": true,
        "MAX_ITER": 30,
        "NORM_CTRL": {
          "DISP":   {"OPT_USE": true, "VALUE": 0.001},
          "FORCE":  {"OPT_USE": true, "VALUE": 0.001},
          "ENERGY": {"OPT_USE": true, "VALUE": 0.001}
        },
        "STIFF_UPD_SCHEME": 0,
        "ITER_BEF_UPDATE": 5,
        "MAX_BISECT_LEVEL": 5,
        "SMART_BISECT": false,
        "DIVERGENCE_THRESHOLD": 3,
        "LINE_SEARCH": {
          "OPT_USE": true,
          "LINE_SEARCH_OPT": 1,
          "START_ITER_NO": 3,
          "MAX_LINE_SEARCH_ITER": 4,
          "LINE_SEARCH_TOL": 0.5
        }
      },
      "IGNORE_ELEM": false,
      "SEQ_LOAD_TYPE": 1,
      "HINGE_OPT": {
        "PSPRING_SUP": 0,
        "EL": 1
      }
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

# ── 修改 Hyper-S 时程全局控制 ─────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "GEO_NONL_TYPE": 1,
            "INIT_LOAD_TYPE": 0,
            "INIT_LOAD_LIST": [
                {"LC_NAME": "DL", "SF": 1.0, "LC_TYPE": "ST"}
            ],
            "INCREMENT_STEP": {
                "NSTEP": 10,
                "OUT_TYPE": 1,
                "STEP_INC": 1
            },
            "ITER_PARAM": {
                "PERMIT_FAIL": True,
                "MAX_ITER": 30,
                "NORM_CTRL": {
                    "DISP": {"OPT_USE": True, "VALUE": 0.001}
                },
                "STIFF_UPD_SCHEME": 1,
                "MAX_BISECT_LEVEL": 5,
                "SMART_BISECT": False,
                "DIVERGENCE_THRESHOLD": 3,
                "LINE_SEARCH": {
                    "OPT_USE": False
                }
            },
            "IGNORE_ELEM": False,
            "SEQ_LOAD_TYPE": 1
        }
    }
}

resp = requests.put(f"{BASE_URL}/db/THGC-M1", json=payload, headers=HEADERS)
print("THGC-M1 PUT:", resp.status_code)
```

---

## 5. /db/THOO-M1 – Time History Output Option (Hyper-S)

定义 Hyper-S 非线性时程输出选项。

> **CIVIL NX 专用**（GEN NX 不可使用）

### 5-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THOO-M1` | 查询 |
| `PUT` | `{base_url}/db/THOO-M1` | 修改 |
| `DELETE` | `{base_url}/db/THOO-M1` | 删除 |

### 5-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 非线性分析结果输出选项 | `OUT_OPT` | Object | - | Required |
| (1) | 非弹性铰按步输出选项（0=全部单元，1=选择单元，2=不输出） | `HINGE_OUT` | Integer(enum) | - | Required |
| (2) | 是否共通设置（true=FIBER_OUT 与 HINGE_OUT 相同） | `COMMON_OPT` | Boolean | - | Required |
| (3) | 纤维截面按步输出选项（0=全部单元，1=选择单元，2=不输出） | `FIBER_OUT` | Integer(enum) | - | Required（COMMON_OPT=false 时） |
| 2 | 时程结果选项 | `RESULT_SELECTION` | Object | - | Required |
| (1) | 输出能量结果 | `ENERGY_RESULT` | Boolean | true | Optional |
| (2) | 黏性阻尼器 / 油阻尼器结果 | `SDVI` | Boolean | true | Optional |
| (3) | 黏弹性阻尼器结果 | `SDVE` | Boolean | true | Optional |
| (4) | 钢阻尼器结果 | `SDST` | Boolean | true | Optional |
| (5) | 滞回隔震装置结果 | `SDHY` | Boolean | true | Optional |
| (6) | 隔震装置结果 | `SDIS` | Boolean | true | Optional |

### 5-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "OUT_OPT": {
        "HINGE_OUT": 1,
        "COMMON_OPT": false,
        "FIBER_OUT": 1
      },
      "RESULT_SELECTION": {
        "ENERGY_RESULT": true,
        "SDVI": true,
        "SDVE": true,
        "SDST": true,
        "SDHY": true,
        "SDIS": true
      }
    }
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

# ── 修改 Hyper-S 输出选项 ───────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "OUT_OPT": {
                "HINGE_OUT": 0,    # 输出全部非弹性单元
                "COMMON_OPT": True  # 与 HINGE_OUT 相同
            },
            "RESULT_SELECTION": {
                "ENERGY_RESULT": True,
                "SDVI": True,
                "SDVE": False,
                "SDST": False,
                "SDHY": True,
                "SDIS": True
            }
        }
    }
}

resp = requests.put(f"{BASE_URL}/db/THOO-M1", json=payload, headers=HEADERS)
print("THOO-M1 PUT:", resp.status_code)
```

---

## 6. /db/THIS – Time History Load Cases

定义时程荷载工况。  
`COMMON.iATYPE`（Linear/Nonlinear）× `COMMON.iAMETHOD`（Modal/Direct/Static）的不同组合需要不同的附加参数。

### 6-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THIS` | 查询全部 |
| `GET` | `{base_url}/db/THIS/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THIS` | 创建 |
| `PUT` | `{base_url}/db/THIS` | 修改全部 |
| `PUT` | `{base_url}/db/THIS/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THIS` | 删除全部 |
| `DELETE` | `{base_url}/db/THIS/{id}` | 删除特定 ID |

### 6-2. COMMON 公共参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 公共设置对象 | `COMMON` | Object | - | Required |
| (1) | 荷载工况名 | `NAME` | String | - | Required |
| (2) | 说明 | `DESC` | String | Blank | Optional |
| (3) | 分析类型（1=Linear, 2=Nonlinear） | `iATYPE` | Integer | - | Required |
| (4) | 分析方法（1=Modal, 2=Direct Integration, 3=Static） | `iAMETHOD` | Integer | - | Required |
| (5) | 时程类型（1=Transient, 2=Periodic） | `iTHTYPE` | Integer | - | Required |

### 6-3. Linear + Modal (Transient / Periodic)

COMMON 附加参数：

| 说明 | Key | 值类型 | 必填 |
|------|-----|------------|----------|
| 结束时间 | `ENDTIME` | Number | Required |
| 时间增量 | `INC` | Number | Required |
| 输出步增量数 | `iOUT` | Integer | Required |
| 荷载施加方法（`"ORDER"`） | `INITMETHOD` | String | Required |
| 阻尼方法（1=Modal, 2=M&S, 3=StrainEnergy） | `iMDTYPE` | Integer | Required |

**使用 ORDER 方法时的顺序荷载参数**

| 说明 | Key | 值类型 | 必填 |
|------|-----|------------|----------|
| 是否使用后荷载选项 | `bSUBSEQ` | Boolean | Optional |
| 后荷载类型（0=荷载工况，1=初始单元内力） | `SUBSEQ` | Integer | Optional |
| 荷载工况类型（`"ST"` / `"CS"` / `"TH"`） | `LCTYPE` | String | Optional |
| 荷载工况名 | `CASE` | String | Optional |

**使用 INIT 方法时的参数**

| 说明 | Key | 值类型 | 必填 |
|------|-----|------------|----------|
| 是否使用初始荷载（0=使用，1=不使用） | `INITLOAD` | Integer | Optional |
| 累计 D/V/A 结果 | `bDVA` | Boolean | Optional |
| 保持最终步荷载 | `bKEEP` | Boolean | Optional |

### 6-4. Linear + Direct Integration (Transient)

COMMON 附加参数：`ENDTIME`、`INC`、`iOUT`、`INITMETHOD`、`iMDTYPE`

附加参数：

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 2 | Newmark 方法类型（1=Constant Accel, 2=Linear Accel, 3=User Input） | `iNMM` | Integer | - | Required |
| 3 | Gamma 值（User Input 时） | `GAMMA` | Number | 0.5 | Optional |
| 4 | Beta 值（User Input 时） | `BETA` | Number | 0.25 | Optional |

### 6-5. Nonlinear + Modal (Transient)

COMMON 附加参数：`ENDTIME`、`INC`、`iOUT`、`INITMETHOD`、`iMDTYPE`

附加参数：下方 [6-8. 迭代控制参数 (Nonlinear 共通)](#6-8-迭代控制参数-nonlinear-共通) 的公共字段 +

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 2 | 最小步长 | `MINSSS` | Number | - | Required |

### 6-6. Nonlinear + Direct Integration (Transient)

COMMON 附加参数：`ENDTIME`、`INC`、`iOUT`、`iGEOM`、`INITMETHOD`、`iMDTYPE`（1=Modal,
2=Mass & Stiffness Proportional, 3=Strain Energy Proportional, **4=Element Mass & Stiffness
Proportional** — ⚠️ 第 4 个取值在此前的文档中被遗漏）

附加参数：

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 2 | Newmark 方法类型（1=Constant Accel, 2=Linear Accel, 3=User Input） | `iNMM` | Integer | - | Required |
| 3 | Gamma 值 | `GAMMA` | Number | 0.5 | Optional |
| 4 | Beta 值 | `BETA` | Number | 0.25 | Optional |
| 5 | 是否执行迭代 | `bITER` | Boolean | true | Optional |
| 6 | 是否更新阻尼矩阵（Modal·Strain Energy：不使用 / M&S·Element M&S：使用） | `DMUPDATE` | Boolean | false | Optional |

附加参数（下方 [6-8. 迭代控制参数 (Nonlinear 共通)](#6-8-迭代控制参数-nonlinear-共通) 的公共字段 +）：

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| A | 允许收敛失败 | `bCONV` | Boolean | true | Optional |
| B | 最小步长 | `MINSSS` | Number | - | Required |
| C | 使用能量范数 | `bEN` | Boolean | false | Optional |
| D | 能量范数值（bEN=true 时） | `EN` | Number | 0.001 | Optional |

### 6-7. Nonlinear + Static

COMMON 附加参数：`ENDTIME`、`iISTEP`（增量步）、`iOUT`、`iGEOM`、`INITMETHOD`

附加参数：

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 2 | 输出累计荷载增量历史 | `bCUMULATE` | Boolean | false | Optional |
| 3 | 是否执行迭代 | `bITER` | Boolean | true | Optional |
| 4 | 增量方法（0=荷载控制，1=位移控制） | `iINCCTRL` | Integer | 0 | Optional |

**增量方法（iINCCTRL）细分参数**

> ⚠️ 2026-08-25 确认：此前文档仅介绍了 `iINCCTRL` 选项，各方式（荷载控制/位移控制）的
> 实际子字段完全未被文档化。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| Load Control (iINCCTRL=0) | | | | | |
| (1) | Scale Factor | `SCALE` | Number | 1 | Required |
| Displacement Control (iINCCTRL=1) | | | | | |
| (1) | Displacement Control Option (0=Global Control, 1=Master Node Control) | `iCTRL` | Integer | - | Required |
| (2) | Displacement（Global：最大平移位移 / Master Node：最大位移） | `TINC` | Number | - | Required |
| (3) | Master Node No.（iCTRL=1 时） | `MNODE` | Integer | - | Required |
| (4) | Master Direction（1=DX, 2=DY, 3=DZ, iCTRL=1 时） | `MDIR` | Integer | - | Required |

附加参数（下方 [6-8. 迭代控制参数 (Nonlinear 共通)](#6-8-迭代控制参数-nonlinear-共通) 的公共字段 +）：

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| A | 允许收敛失败 | `bCONV` | Boolean | true | Optional |
| B | 最大子步数 | `iMSTEP` | Integer | - | Required |
| C | 使用能量范数 | `bEN` | Boolean | false | Optional |
| D | 能量范数值（bEN=true 时） | `EN` | Number | 0.001 | Optional |

### 6-8. 迭代控制参数 (Nonlinear 共通)

> ⚠️ 2026-08-25 确认：适用于 Nonlinear + Modal/Direct Integration/Static 3 种模式的
> 公共迭代控制字段（`iMAXITER`~`dTOL`）在此前的文档中完全没有。按原文
> [Time History Load Cases](https://support.midasuser.com/hc/en-us/articles/35963903917593)
> 中 "Iteration Control for Nonlinear Type" 的脚注予以补充。

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 最大迭代次数 | `iMAXITER` | Integer | - | Required |
| 2 | 使用位移范数 | `bDN` | Boolean | true | Optional |
| 3 | 位移范数值（bDN=true 时） | `DN` | Number | 0.001 | Optional |
| 4 | 使用荷载范数 | `bFN` | Boolean | false | Optional |
| 5 | 荷载范数值（bFN=true 时） | `FN` | Number | 0.001 | Optional |
| 6 | 使用线性搜索方法 | `bULSM` | Boolean | false | Optional |
| 7 | 线性搜索起始迭代数（bULSM=true 时） | `ULSM` | Integer | 5 | Optional |
| 8 | Runge-Kutta 方法（0=Fehlberg, 1=Cash-Karp） | `iRKM` | Integer | 0 | Optional |
| 9 | 容差 | `dTOL` | Number | 1e-08 | Optional |

在此表之外，Modal（6-5）另加 `MINSSS`，Direct Integration（6-6）另加 `bCONV`/`MINSSS`/`bEN`/`EN`，
Static（6-7）另加 `bCONV`/`iMSTEP`/`bEN`/`EN`，按模式分别追加。

### 6-9. 阻尼参数

**Modal 阻尼（iMDTYPE=1）**

| 说明 | Key | 值类型 |
|------|-----|------------|
| 全部振型阻尼比 | `DALL` | Number |
| 各振型阻尼比覆盖列表 | `aDAMP` | Array[Object] |
| - 振型编号 | `iMODE` | Integer |
| - 阻尼比 | `DAMPING` | Number |

> ⚠️ 2026-08-25 确认：此前文档把 Key 错误记为 `aMDAMPING`（原文 Schema 与所有
> Request 示例均为 `aDAMP`）。该错误在实际调用 API 时可能导致字段被忽略。

**Mass & Stiffness Proportional 阻尼（iMDTYPE=2）**

> ⚠️ 2026-08-25 确认：该阻尼方式的子字段在此前文档（§6 THIS）中完全未被文档化
> （仅文档化了 §2 SPLC 的同一项）。

| No. | 说明 | Key | 值类型 | 必填 |
|-----|------|-----|------------|----------|
| 1 | 系数确定方式（1=直接指定，2=由模态阻尼计算） | `iCOEF` | Integer | Required |
| iCOEF=1（直接指定） | | | | |
| 2 | 是否使用质量比例 | `bMASSP` | Boolean | Required |
| 3 | 质量比例系数（bMASSP=true 时） | `MASSC` | Number | Required |
| 4 | 是否使用刚度比例 | `bSTIFFP` | Boolean | Required |
| 5 | 刚度比例系数（bSTIFFP=true 时） | `STIFFC` | Number | Required |
| iCOEF=2（由模态阻尼计算） | | | | |
| 2 | 计算方法（1=频率，2=周期） | `iCALC` | Integer | Required |
| 3 | 振型 1 频率/周期 | `FP1` | Number | Required |
| 4 | 振型 1 阻尼比 | `DR1` | Number | Required |
| 5 | 振型 2 频率/周期 | `FP2` | Number | Required |
| 6 | 振型 2 阻尼比 | `DR2` | Number | Required |

### 6-10. Request Body 示例

**Linear + Modal + Transient**

```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "TH_Linear_Modal",
        "DESC": "선형 모달 시간이력",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "ENDTIME": 30.0,
        "INC": 0.01,
        "iOUT": 1,
        "INITMETHOD": "INIT",
        "INITLOAD": 0,
        "bDVA": false,
        "bKEEP": false,
        "iMDTYPE": 1
      },
      "DALL": 0.05
    }
  }
}
```

**Nonlinear + Direct Integration + Transient**

```json
{
  "Assign": {
    "2": {
      "COMMON": {
        "NAME": "TH_NL_Direct",
        "DESC": "비선형 직접적분 시간이력",
        "iATYPE": 2,
        "iAMETHOD": 2,
        "iTHTYPE": 1,
        "ENDTIME": 20.0,
        "INC": 0.005,
        "iOUT": 2,
        "iGEOM": 0,
        "INITMETHOD": "INIT",
        "INITLOAD": 0,
        "bDVA": false,
        "bKEEP": false,
        "iMDTYPE": 2
      },
      "iNMM": 1,
      "bITER": true,
      "DMUPDATE": false
    }
  }
}
```

**Nonlinear + Static (Load Control)**

```json
{
  "Assign": {
    "3": {
      "COMMON": {
        "NAME": "TH_NL_Static",
        "DESC": "비선형 정적 시간이력",
        "iATYPE": 2,
        "iAMETHOD": 3,
        "ENDTIME": 10.0,
        "iISTEP": 100,
        "iOUT": 1,
        "iGEOM": 0,
        "INITMETHOD": "INIT"
      },
      "bCUMULATE": true,
      "iINCCTRL": 0,
      "SCALE": 1,
      "bITER": true,
      "bCONV": true,
      "iMSTEP": 10,
      "iMAXITER": 10,
      "bDN": true,
      "DN": 0.001,
      "bFN": true,
      "FN": 0.001,
      "bEN": true,
      "EN": 0.001,
      "iRKM": 0,
      "dTOL": 1e-08,
      "bULSM": true,
      "ULSM": 5
    }
  }
}
```

**Nonlinear + Static (Displacement Control – Master Node)**

```json
{
  "Assign": {
    "4": {
      "COMMON": {
        "NAME": "TH_NL_Static_Disp",
        "DESC": "",
        "iATYPE": 2,
        "iAMETHOD": 3,
        "iISTEP": 1,
        "iOUT": 1,
        "iGEOM": 0,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": true,
        "SUBSEQ": 1
      },
      "bCUMULATE": false,
      "iINCCTRL": 1,
      "iCTRL": 1,
      "TINC": 0.02,
      "MNODE": 1,
      "MDIR": 2,
      "bITER": true,
      "bCONV": true,
      "iMSTEP": 10,
      "iMAXITER": 10,
      "bDN": true,
      "DN": 0.001,
      "iRKM": 0,
      "dTOL": 1e-08,
      "bULSM": false,
      "ULSM": 5
    }
  }
}
```

### 6-11. Python 示例代码

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── 1) 创建 Linear Modal Transient ────────────────────────────────────────────
payload_linear_modal = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "TH01_Linear_Modal",
                "iATYPE": 1,       # Linear
                "iAMETHOD": 1,     # Modal
                "iTHTYPE": 1,      # Transient
                "ENDTIME": 30.0,
                "INC": 0.01,
                "iOUT": 1,
                "INITMETHOD": "INIT",
                "INITLOAD": 0,
                "bDVA": False,
                "bKEEP": False,
                "iMDTYPE": 1       # Modal 阻尼
            },
            "DALL": 0.05
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THIS", json=payload_linear_modal, headers=HEADERS)
print("THIS POST (Linear Modal):", resp.status_code)

# ── 2) 创建 Nonlinear Direct Integration Transient ───────────────────────────
payload_nl_di = {
    "Assign": {
        "2": {
            "COMMON": {
                "NAME": "TH02_NL_DI",
                "iATYPE": 2,       # Nonlinear
                "iAMETHOD": 2,     # Direct Integration
                "iTHTYPE": 1,      # Transient
                "ENDTIME": 20.0,
                "INC": 0.005,
                "iOUT": 2,
                "iGEOM": 0,
                "INITMETHOD": "INIT",
                "INITLOAD": 0,
                "bDVA": False,
                "bKEEP": False,
                "iMDTYPE": 2       # Mass & Stiffness Proportional
            },
            "iNMM": 1,             # Constant Acceleration
            "bITER": True,
            "DMUPDATE": False
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THIS", json=payload_nl_di, headers=HEADERS)
print("THIS POST (NL DI):", resp.status_code)

# ── 3) 查询全部 ─────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THIS", headers=HEADERS)
print("THIS GET:", resp.status_code)
```

---

## 7. /db/THIS-M1 – Time History Load Cases (Hyper-S)

定义 Hyper-S 非线性时程荷载工况。  
与既有 THIS 不同，采用嵌套对象结构（ANAL_CASE, DAMPING, NONL_CTRL_PARAM）。

> **CIVIL NX 专用**（GEN NX 不可使用）

### 7-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THIS-M1` | 查询全部 |
| `GET` | `{base_url}/db/THIS-M1/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THIS-M1` | 创建 |
| `PUT` | `{base_url}/db/THIS-M1` | 修改全部 |
| `PUT` | `{base_url}/db/THIS-M1/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THIS-M1` | 删除全部 |
| `DELETE` | `{base_url}/db/THIS-M1/{id}` | 删除特定 ID |

### 7-2. 参数

**公共参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 荷载工况名 | `NAME` | String | - | Required |
| 2 | 说明 | `DESC` | String | - | Optional |
| 3 | 分析工况选项 | `ANAL_CASE` | Object | - | Required |
| (1) | 分析类型（0=Linear, 1=Nonlinear） | `ANAL_TYPE` | Integer(enum) | - | Required |
| (2) | 分析方法（0=Modal, 1=Direct Integration, **2=Static**） | `ANAL_METHOD` | Integer(enum) | - | Required |
| (3) | 时程类型（0=Transient, 1=Periodic）— Nonlinear+Direct Integration/Static 会拒绝 Periodic | `TH_TYPE` | Integer(enum) | - | Optional |
| 3-a | 几何非线性类型（0=None, 1=P-Delta, 2=Large Displacements, ANAL_TYPE=Nonlinear 时） | `GEOM_NL_TYPE` | Integer(enum) | 0 | Optional |
| 4 | 结束时间 | `ENDTIME` | Number | - | Required |
| 5 | 时间增量 | `TIME_INC` | Number | - | Required |
| 6 | 输出步增量数 | `OUTPUT_STEP` | Integer | 1 | Required |
| 6-a | 增量步数（Nonlinear+Static 时事实上必填） | `INC_STEP` | Integer | 1 | Optional |
| 7 | 初始荷载方法（`"INIT"` / `"ORDER"`） | `INIT_METHOD` | String(enum) | - | Required |
| 8 | 使用初始荷载（INIT_METHOD=INIT 时） | `USE_INIT_LOAD` | Boolean | - | Required |
| 9 | 累计 D/V/A 结果（USE_INIT_LOAD=true 时） | `CUM_DVA` | Boolean | false | Required |
| 10 | 保持最终步荷载 | `KEEP_LOAD` | Boolean | false | Required |
| 11 | 后荷载选项（INIT_METHOD=ORDER 时） | `SUBSEQ` | Object | - | Required |
| (1) | 使用后荷载 | `OPT_USE` | Boolean | false | Optional |
| (2) | 后荷载类型（0=荷载工况，1=初始单元内力，2=几何刚度初始力） | `SUBSEQ_LOAD` | Integer(enum) | - | Required |
| (3) | 荷载工况类型（`"ST"` / `"CS"` / `"TH"`） | `LCTYPE` | String(enum) | - | Required |
| (4) | 荷载工况名 | `CASE` | String | - | Required |
| 12 | 保持最终步加速度 | `KEEP_ACC` | Boolean | false | Optional |
| 13 | 阻尼设置 | `DAMPING` | Object | - | Required |
| (1) | 阻尼方法（0=Direct Modal, 1=M&S Proportional, 2=Strain Energy, 3=Element M&S — Modal+Element(3) 组合会被拒绝） | `DAMPING_METHOD` | Integer(enum) | - | Required |
| (2) | 全部振型阻尼比（DAMPING_METHOD=0 时） | `ALL_DAMPING_RATIO` | Number | - | Required |
| (3) | 各振型阻尼比覆盖列表 | `MODAL_DAMPING_RATIO` | Array[Object] | - | Optional |
| - 振型编号 | `MODE_NO` | Integer | - | Required |
| - 阻尼比 | `DAMPING` | Number | - | Required |
| 14 | 非线性控制参数（ANAL_TYPE=1 时） | `NONL_CTRL_PARAM` | Object | - | Optional |
| (1) | 是否执行迭代 | `PERFORM_ITER` | Boolean | - | Required |
| (2) | 迭代控制参数 | `ITER_CTRL` | Object | - | Required |
| - 允许收敛失败 | `PERMIT_FAIL` | Boolean | - | - |
| - 最大迭代次数 | `MAX_ITER` | Integer | - | - |
| - 收敛判定基准（NORM_CTRL） | `NORM_CTRL` | Object | - | - |
| - 刚度更新方式 | `STIFF_UPD_SCHEME` | Integer | - | - |
| - 刚度更新前迭代次数（仅 STIFF_UPD_SCHEME=0 时可指定） | `ITER_BEF_UPDATE` | Integer | - | - |
| - 最大二分法层级 | `MAX_BISECT_LEVEL` | Integer | - | - |
| - 智能二分法 | `SMART_BISECT` | Boolean | - | - |
| - 发散阈值 | `DIVERGENCE_THRESHOLD` | Number | - | - |
| - 线性搜索选项（LINE_SEARCH） | `LINE_SEARCH` | Object | - | - |
| (3) | 阻尼矩阵更新（0/1/2，仅 DAMPING_METHOD 为 M&S(1)/Element M&S(3) 时） | `DAMP_UPDATE` | Integer(enum) | - | Optional |

> ⚠️ 2026-08-25 确认：此前文档完全遗漏了以下 3 项（按原文
> [Time History Load Cases (THIS-M1)](https://support.midasuser.com/hc/en-us/articles/56538335819673)
> 为准）。ANAL_METHOD 的第 3 个取值（Static=2，但 Linear+Static 组合由服务器拒绝）在规格中
> 整体缺失；`GEOM_NL_TYPE` 的 Schema 说明本身写明“Schema 值 1↔DB 值 2、Schema 值
> 2↔DB 值 1”，存储时会互换，故按原文照录，实际对接前建议再次确认。`DAMPING_METHOD=1`
> （M&S Proportional）的细分系数输入结构也完全没有。

**M&S Proportional 阻尼细分字段（DAMPING_METHOD=1）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 系数确定方式（0=Direct Specification, 1=Calculate from Modal Damping） | `COEF_INPUT` | Integer(enum) | - | Required |
| COEF_INPUT=0 | | | | | |
| 2 | 使用质量比例（USE_MASS/USE_STIFF 中至少 1 个为 true） | `USE_MASS` | Boolean | - | Optional |
| 3 | 质量系数（Rm） | `MASS_VALUE` | Number | - | Optional |
| 4 | 使用刚度比例 | `USE_STIFF` | Boolean | - | Optional |
| 5 | 刚度系数（Rk） | `STIFF_VALUE` | Number | - | Optional |
| COEF_INPUT=1 | | | | | |
| 2 | 计算基准（0=Frequency, 1=Period） | `COEF_CALC` | Integer(enum) | - | Required |
| 3 | 振型 1 频率（COEF_CALC=0）/ 周期（COEF_CALC=1） | `FREQ1`/`PERIOD1` | Number | - | Required |
| 4 | 振型 1 阻尼比 | `DR1` | Number | - | Required |
| 5 | 振型 2 频率（FREQ1≠FREQ2）/周期（PERIOD1≠PERIOD2） | `FREQ2`/`PERIOD2` | Number | - | Required |
| 6 | 振型 2 阻尼比 | `DR2` | Number | - | Required |

**增量控制（仅 ANAL_METHOD=2 Static，`INC_CTRL`）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 增量方法（0=Load Control, 1=Displacement Control） | `INC_METHOD` | Integer(enum) | - | Required |
| INC_METHOD=0 | | | | | |
| 2 | Scale Factor | `SF` | Number | 1 | Optional |
| INC_METHOD=1（`DISP_CTRL` 对象） | | | | | |
| 2 | 控制选项（0=Global, 1=Master Node Control） | `CTRL_OPT` | Integer(enum) | - | Required |
| 3 | 最大平移位移（仅 Global） | `MAX_TRANS_DISP` | Number | - | Optional |
| 4 | Master Node No.（仅 Master Node Control） | `MASTER_NODE` | Integer | - | Optional |
| 5 | Master Direction（0/1/2，仅 Master Node Control） | `MASTER_DIR` | Integer(enum) | - | Optional |
| 6 | 最大位移（仅 Master Node Control） | `MAX_DISP` | Number | - | Optional |

**时间积分方法（仅 ANAL_METHOD=1 Direct Integration，`TIME_PARAM`）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 积分方法（0=Newmark, 1=HHT） | `METHOD` | Integer(enum) | - | Required |
| 2 | Newmark 方法类型（METHOD=0）0=Constant/1=Linear Accel./2=User Input | `NEWMARK_METHOD` | Integer(enum) | - | Optional |
| 3 | Gamma（NEWMARK_METHOD=2 时） | `GAMMA` | Number | 0.5 | Optional |
| 4 | Beta（NEWMARK_METHOD=2 时） | `BETA` | Number | 0.25 | Optional |

**非线性边界单元分析（`BOUNDARY_NL_ANAL`）**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 积分法（0=Fehlberg, 1=Cash-Karp, 2=Dormand-Prince） | `METHOD` | Integer(enum) | 0 | Optional |
| 2 | 容差 | `TOL` | Number | 1e-08 | Optional |

### 7-3. Request Body 示例

**Linear + Modal + Transient**

```json
{
  "Assign": {
    "1": {
      "NAME": "LC_LINEAR_MODAL_TRANS",
      "DESC": "Linear Modal Transient case",
      "ANAL_CASE": {
        "ANAL_TYPE": 0,
        "ANAL_METHOD": 0,
        "TH_TYPE": 0
      },
      "ENDTIME": 10,
      "TIME_INC": 0.01,
      "OUTPUT_STEP": 1,
      "INIT_METHOD": "INIT",
      "USE_INIT_LOAD": true,
      "CUM_DVA": true,
      "KEEP_LOAD": true,
      "DAMPING": {
        "DAMPING_METHOD": 0,
        "ALL_DAMPING_RATIO": 0.05,
        "MODAL_DAMPING_RATIO": [
          {"MODE_NO": 1, "DAMPING": 0.05},
          {"MODE_NO": 2, "DAMPING": 0.04}
        ]
      }
    }
  }
}
```

**Nonlinear + Modal + Transient**

```json
{
  "Assign": {
    "2": {
      "NAME": "LC_NONLINEAR_MODAL_TRANS",
      "ANAL_CASE": {
        "ANAL_TYPE": 1,
        "ANAL_METHOD": 0,
        "TH_TYPE": 0
      },
      "ENDTIME": 10,
      "TIME_INC": 0.01,
      "OUTPUT_STEP": 1,
      "INIT_METHOD": "INIT",
      "USE_INIT_LOAD": true,
      "CUM_DVA": true,
      "KEEP_LOAD": true,
      "DAMPING": {
        "DAMPING_METHOD": 0,
        "ALL_DAMPING_RATIO": 0.05,
        "MODAL_DAMPING_RATIO": [
          {"MODE_NO": 1, "DAMPING": 0.05}
        ]
      },
      "NONL_CTRL_PARAM": {
        "PERFORM_ITER": true,
        "ITER_CTRL": {
          "PERMIT_FAIL": true,
          "MAX_ITER": 30,
          "NORM_CTRL": {
            "DISP": {"OPT_USE": true, "VALUE": 0.001}
          },
          "STIFF_UPD_SCHEME": 0,
          "ITER_BEF_UPDATE": 5,
          "MAX_BISECT_LEVEL": 5,
          "SMART_BISECT": false,
          "DIVERGENCE_THRESHOLD": 3,
          "LINE_SEARCH": {
            "OPT_USE": true,
            "LINE_SEARCH_OPT": 1,
            "START_ITER_NO": 3,
            "MAX_LINE_SEARCH_ITER": 4,
            "LINE_SEARCH_TOL": 0.5
          }
        }
      }
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

# ── 创建 Hyper-S Linear Modal Transient ─────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "HyperS_Linear_Modal",
            "ANAL_CASE": {
                "ANAL_TYPE": 0,     # Linear
                "ANAL_METHOD": 0,   # Modal
                "TH_TYPE": 0        # Transient
            },
            "ENDTIME": 30.0,
            "TIME_INC": 0.01,
            "OUTPUT_STEP": 1,
            "INIT_METHOD": "INIT",
            "USE_INIT_LOAD": True,
            "CUM_DVA": False,
            "KEEP_LOAD": False,
            "DAMPING": {
                "DAMPING_METHOD": 0,
                "ALL_DAMPING_RATIO": 0.05
            }
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THIS-M1", json=payload, headers=HEADERS)
print("THIS-M1 POST:", resp.status_code)

# ── 查询 ─────────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THIS-M1", headers=HEADERS)
print("THIS-M1 GET:", resp.status_code)
```

---

## 8. /db/THFC – Time History Functions

定义时程函数（时间-值对或正弦波函数）。

### 8-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THFC` | 查询全部 |
| `GET` | `{base_url}/db/THFC/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THFC` | 创建 |
| `PUT` | `{base_url}/db/THFC` | 修改全部 |
| `PUT` | `{base_url}/db/THFC/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THFC` | 删除全部 |
| `DELETE` | `{base_url}/db/THFC/{id}` | 删除特定 ID |

### 8-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 函数名 | `NAME` | String | - | Required |
| 2 | 说明 | `DESC` | String | Blank | Optional |
| 3 | 数据类型（1=归一化加速度，2=加速度，3=力，4=力矩，5=Normal） | `iTYPE` | Integer | - | Required |
| 4 | 重力加速度 | `GRAV` | Number | - | Required |
| 5 | 函数类型（1=Time Function, 2=Sinusoidal） | `FUNCTYPE` | Integer | - | Required |

**Time Function（FUNCTYPE=1）附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 6 | 缩放方法（0=Scale Factor, 1=Max Value） | `iMETHOD` | Integer | - | Required |
| 7a | 缩放系数（iMETHOD=0 时） | `SCALE` | Number | - | Required |
| 7b | 最大值（iMETHOD=1 时） | `MAXVALUE` | Number | 0 | Optional |
| 8 | 时间-值数据列表 | `aFUNCDATA` | Array[Object] | - | Required |
| (1) | 时间 | `TIME` | Number | - | Required |
| (2) | 值 | `VALUE` | Number | - | Required |

**Sinusoidal（FUNCTYPE=2）附加参数**

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 6 | 常数 A | `CONS_A` | Number | - | Required |
| 7 | 常数 C | `CONS_C` | Number | - | Required |
| 8 | 频率 | `FREQUENCY` | Number | - | Required |
| 9 | 阻尼系数 | `DAMP_FACTOR` | Number | - | Required |
| 10 | 相位角 | `PHASE_ANGLE` | Number | - | Required |

### 8-3. Request Body 示例

**Time Function (Scale Factor)**

```json
{
  "Assign": {
    "1": {
      "NAME": "ElCentro_Scale",
      "FUNCTYPE": 1,
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1.0,
      "GRAV": 9.806,
      "aFUNCDATA": [
        {"TIME": 0.02, "VALUE":  0.00517},
        {"TIME": 0.04, "VALUE":  0.00421},
        {"TIME": 0.06, "VALUE":  0.00324},
        {"TIME": 0.08, "VALUE": -0.00102}
      ],
      "DESC": "1940 El Centro EW"
    }
  }
}
```

**Time Function (Max Value)**

```json
{
  "Assign": {
    "2": {
      "NAME": "ElCentro_MaxVal",
      "FUNCTYPE": 1,
      "iTYPE": 1,
      "iMETHOD": 1,
      "MAXVALUE": 0.2,
      "GRAV": 9.806,
      "aFUNCDATA": [
        {"TIME": 0.02, "VALUE":  0.00517},
        {"TIME": 0.04, "VALUE":  0.00421}
      ]
    }
  }
}
```

**Sinusoidal**

```json
{
  "Assign": {
    "3": {
      "NAME": "Sinusoidal_1Hz",
      "FUNCTYPE": 2,
      "iTYPE": 1,
      "GRAV": 9.806,
      "CONS_A": 0.05,
      "CONS_C": 0.01,
      "FREQUENCY": 1.0,
      "DAMP_FACTOR": 0.1,
      "PHASE_ANGLE": 0.0,
      "DESC": "1Hz Sinusoidal"
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

# ── 1) 创建 Time Function（Scale Factor） ─────────────────────────────────────
payload_tf = {
    "Assign": {
        "1": {
            "NAME": "EQ_EW",
            "FUNCTYPE": 1,
            "iTYPE": 1,        # Normalized Acceleration
            "iMETHOD": 0,      # Scale Factor
            "SCALE": 1.0,
            "GRAV": 9.806,
            "aFUNCDATA": [
                {"TIME": 0.02, "VALUE":  0.00517},
                {"TIME": 0.04, "VALUE":  0.00421},
                {"TIME": 0.06, "VALUE":  0.00324},
            ],
            "DESC": "El Centro EW Component"
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THFC", json=payload_tf, headers=HEADERS)
print("THFC POST (Time Function):", resp.status_code)

# ── 2) 创建 Sinusoidal 函数 ──────────────────────────────────────────────────
payload_sin = {
    "Assign": {
        "2": {
            "NAME": "SIN_1Hz",
            "FUNCTYPE": 2,
            "iTYPE": 3,        # Force
            "GRAV": 9.806,
            "CONS_A": 100.0,   # 振幅 100 kN
            "CONS_C": 0.0,
            "FREQUENCY": 1.0,
            "DAMP_FACTOR": 0.0,
            "PHASE_ANGLE": 0.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THFC", json=payload_sin, headers=HEADERS)
print("THFC POST (Sinusoidal):", resp.status_code)

# ── 3) 查询特定函数 ────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THFC/1", headers=HEADERS)
print("THFC GET/1:", resp.json())
```

---

## 9. /db/THGA – Ground Acceleration

定义施加于时程荷载工况的地面加速度。

### 9-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THGA` | 查询全部 |
| `GET` | `{base_url}/db/THGA/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THGA` | 创建 |
| `PUT` | `{base_url}/db/THGA` | 修改全部 |
| `PUT` | `{base_url}/db/THGA/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THGA` | 删除全部 |
| `DELETE` | `{base_url}/db/THGA/{id}` | 删除特定 ID |

### 9-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 时程荷载工况名 | `NAME` | String | - | Required |
| 2 | 水平地面加速度角度 | `ANGLE` | Number | 0 | Optional |
| 3 | X 方向函数名 | `FUNCX` | String | - | Required |
| 4 | X 方向缩放系数 | `SCALEX` | Number | - | Required |
| 5 | X 方向到达时间 | `ATIMEX` | Number | 0 | Optional |
| 6 | Y 方向函数名 | `FUNCY` | String | - | Required |
| 7 | Y 方向缩放系数 | `SCALEY` | Number | - | Required |
| 8 | Y 方向到达时间 | `ATIMEY` | Number | 0 | Optional |
| 9 | Z 方向函数名 | `FUNCZ` | String | - | Required |
| 10 | Z 方向缩放系数 | `SCALEZ` | Number | - | Required |
| 11 | Z 方向到达时间 | `ATIMEZ` | Number | 0 | Optional |

### 9-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "NAME": "GA_ElCentro",
      "ANGLE": 0,
      "FUNCX": "ElCentro_EW",
      "SCALEX": 1.0,
      "ATIMEX": 0,
      "FUNCY": "ElCentro_NS",
      "SCALEY": 0.85,
      "ATIMEY": 0,
      "FUNCZ": "ElCentro_UD",
      "SCALEZ": 0.65,
      "ATIMEZ": 0
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

# ── 创建地面加速度荷载 ────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "NAME": "GA_3Dir",
            "ANGLE": 0.0,
            "FUNCX": "EQ_EW",    # X 方向：水平（EW）
            "SCALEX": 1.0,
            "ATIMEX": 0.0,
            "FUNCY": "EQ_NS",    # Y 方向：水平（NS）
            "SCALEY": 1.0,
            "ATIMEY": 0.0,
            "FUNCZ": "EQ_UD",    # Z 方向：竖直（UD）
            "SCALEZ": 0.667,
            "ATIMEZ": 0.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THGA", json=payload, headers=HEADERS)
print("THGA POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THGA", headers=HEADERS)
print("THGA GET:", resp.json())
```

---

## 10. /db/THNL – Dynamic Nodal Loads

定义施加于时程荷载工况的动态节点荷载。

> **注意**：`FUNC_NAME` 仅可使用 Force 或 Moment 类型的时程函数。

### 10-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THNL` | 查询全部 |
| `GET` | `{base_url}/db/THNL/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THNL` | 创建 |
| `PUT` | `{base_url}/db/THNL` | 修改全部 |
| `PUT` | `{base_url}/db/THNL/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THNL` | 删除全部 |
| `DELETE` | `{base_url}/db/THNL/{id}` | 删除特定 ID |

### 10-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 动态节点荷载列表 | `ITEMS` | Array[Object] | - | Required |
| (1) | 序号 | `ID` | Integer | 0 | Optional |
| (2) | 时程荷载工况名 | `THLCNAME` | String | - | Required |
| (3) | 时程函数名（仅可使用 Force/Moment 类型） | `FUNC_NAME` | String | - | Required |
| (4) | 方向（`"X"` / `"Y"` / `"Z"`） | `DIR` | String | - | Required |
| (5) | 到达时间 | `ARRIVAL_TIME` | Number | - | Required |
| (6) | 缩放系数 | `SCALE_FACTOR` | Number | - | Required |

### 10-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "THLCNAME": "TH01_Linear_Modal",
          "FUNC_NAME": "SIN_1Hz",
          "DIR": "Y",
          "ARRIVAL_TIME": 0.0,
          "SCALE_FACTOR": 1.0
        },
        {
          "ID": 2,
          "THLCNAME": "TH01_Linear_Modal",
          "FUNC_NAME": "SIN_1Hz",
          "DIR": "Z",
          "ARRIVAL_TIME": 5.0,
          "SCALE_FACTOR": 0.5
        }
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

# ── 创建动态节点荷载 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "ID": 1,
                    "THLCNAME": "TH01_Linear_Modal",
                    "FUNC_NAME": "SIN_1Hz",     # Force/Moment 类型函数
                    "DIR": "Y",
                    "ARRIVAL_TIME": 0.0,
                    "SCALE_FACTOR": 1.0
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THNL", json=payload, headers=HEADERS)
print("THNL POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THNL", headers=HEADERS)
print("THNL GET:", resp.json())
```

---

## 11. /db/THSL – Time Varying Static Loads

定义施加于时程荷载工况的时变静力荷载。

> **注意**：`THIS_FUNCNAME` 仅可使用 Normal 类型的时程函数。

### 11-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THSL` | 查询全部 |
| `GET` | `{base_url}/db/THSL/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THSL` | 创建 |
| `PUT` | `{base_url}/db/THSL` | 修改全部 |
| `PUT` | `{base_url}/db/THSL/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THSL` | 删除全部 |
| `DELETE` | `{base_url}/db/THSL/{id}` | 删除特定 ID |

### 11-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 时程荷载工况名 | `THIS_LCNAME` | String | - | Required |
| 2 | 静力荷载工况名 | `SLOAD` | String | - | Required |
| 3 | 时程函数名（仅可使用 Normal 类型） | `THIS_FUNCNAME` | String | - | Required |
| 4 | 到达时间 | `ATIME` | Number | 0 | Optional |
| 5 | 缩放系数 | `SCALE` | Number | - | Required |

### 11-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "THIS_LCNAME": "TH01_Linear_Modal",
      "SLOAD": "SW",
      "THIS_FUNCNAME": "NormFunc_SW",
      "ATIME": 0.0,
      "SCALE": 1.0
    },
    "2": {
      "THIS_LCNAME": "TH01_Linear_Modal",
      "SLOAD": "Pretension",
      "THIS_FUNCNAME": "NormFunc_PT",
      "ATIME": 3.0,
      "SCALE": 1.0
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

# ── 创建时变静力荷载 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "THIS_LCNAME": "TH01_Linear_Modal",
            "SLOAD": "SW",               # 静力荷载工况名
            "THIS_FUNCNAME": "NormFunc",  # Normal 类型时程函数
            "ATIME": 0.0,
            "SCALE": 1.0
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THSL", json=payload, headers=HEADERS)
print("THSL POST:", resp.status_code)

# ── 删除特定工况 ─────────────────────────────────────────────────────────
resp = requests.delete(f"{BASE_URL}/db/THSL/1", headers=HEADERS)
print("THSL DELETE/1:", resp.status_code)
```

---

## 12. /db/THMS – Multiple Support Excitation

定义多点激励。

> **注意**：`FUNCX` / `FUNCY` / `FUNCZ` 仅可使用 Normalized Acceleration 或 Acceleration 类型的时程函数。

### 12-1. HTTP 方法与 URL

| 方法 | URL | 说明 |
|--------|-----|------|
| `GET` | `{base_url}/db/THMS` | 查询全部 |
| `GET` | `{base_url}/db/THMS/{id}` | 查询特定 ID |
| `POST` | `{base_url}/db/THMS` | 创建 |
| `PUT` | `{base_url}/db/THMS` | 修改全部 |
| `PUT` | `{base_url}/db/THMS/{id}` | 修改特定 ID |
| `DELETE` | `{base_url}/db/THMS` | 删除全部 |
| `DELETE` | `{base_url}/db/THMS/{id}` | 删除特定 ID |

### 12-2. 参数

| No. | 说明 | Key | 值类型 | 默认值 | 必填 |
|-----|------|-----|------------|---------|----------|
| 1 | 多点激励列表 | `ITEMS` | Array[Object] | - | Required |
| (1) | 序号 | `ID` | Integer | 0 | Optional |
| (2) | 时程荷载工况名 | `LCNAME` | String | - | Required |
| (3) | 水平地面加速度角度 | `ANGLE` | Number | 0 | Optional |
| (4) | X 方向函数名（仅 NormAccel/Acceleration 类型） | `FUNCX` | String | - | Required |
| (5) | X 方向缩放系数 | `SCALEX` | Number | - | Required |
| (6) | X 方向到达时间 | `ATIMEX` | Number | 0 | Optional |
| (7) | Y 方向函数名 | `FUNCY` | String | - | Optional |
| (8) | Y 方向缩放系数 | `SCALEY` | Number | - | Optional |
| (9) | Y 方向到达时间 | `ATIMEY` | Number | 0 | Optional |
| (10) | Z 方向函数名 | `FUNCZ` | String | - | Optional |
| (11) | Z 方向缩放系数 | `SCALEZ` | Number | - | Optional |
| (12) | Z 方向到达时间 | `ATIMEZ` | Number | 0 | Optional |

### 12-3. Request Body 示例

```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "TH01_Linear_Modal",
          "ANGLE": 0,
          "FUNCX": "ElCentro_EW",
          "SCALEX": 1.0,
          "ATIMEX": 0,
          "FUNCY": "ElCentro_NS",
          "SCALEY": 1.0,
          "ATIMEY": 0,
          "FUNCZ": "ElCentro_UD",
          "SCALEZ": 0.667,
          "ATIMEZ": 0
        }
      ]
    }
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

# ── 创建多点激励 ──────────────────────────────────────────────────────
payload = {
    "Assign": {
        "1": {
            "ITEMS": [
                {
                    "ID": 1,
                    "LCNAME": "TH01_Linear_Modal",
                    "ANGLE": 0.0,
                    "FUNCX": "ElCentro_EW",
                    "SCALEX": 1.0,
                    "ATIMEX": 0.0,
                    "FUNCY": "ElCentro_NS",
                    "SCALEY": 1.0,
                    "ATIMEY": 0.0,
                    "FUNCZ": "ElCentro_UD",
                    "SCALEZ": 0.667,
                    "ATIMEZ": 0.0
                }
            ]
        }
    }
}

resp = requests.post(f"{BASE_URL}/db/THMS", json=payload, headers=HEADERS)
print("THMS POST:", resp.status_code)

# ── 查询全部 ────────────────────────────────────────────────────────────────
resp = requests.get(f"{BASE_URL}/db/THMS", headers=HEADERS)
print("THMS GET:", resp.json())
```

---

## End-to-End 工作流示例

本示例展示反应谱分析与时程分析的典型设置顺序。

```python
import requests

BASE_URL = "https://moa-engineers.midasit.com:443/civil"
HEADERS = {
    "Content-Type": "application/json",
    "MAPI-Key": "YOUR_API_KEY"
}

# ── STEP 1: 创建反应谱函数（KDS 41-17-00:2019） ─────────────────────
spfc = {
    "Assign": {
        "1": {
            "NAME": "RS_KDS2019",
            "iTYPE": 1,
            "iMETHOD": 0,
            "SCALE": 1.0,
            "GRAV": 9.806,
            "DRATIO": 0.05,
            "STR": {"SPEC_CODE": "KDS(41-17-00:2019)"},
            "OPT": {"SC_": 2, "iSEISZONE": 0},
            "VAL": {
                "aSRA": [0.22, 0.154],
                "aSCP": [1.0, 1.5],
                "PERIOD": 4.0,
                "IE": 1.2,
                "R_": 5.0,
                "ZONEFACTOR": 0.22
            }
        }
    }
}
r = requests.post(f"{BASE_URL}/db/SPFC", json=spfc, headers=HEADERS)
print("STEP 1 - SPFC:", r.status_code)

# ── STEP 2: 创建反应谱荷载工况 ──────────────────────────────────
splc = {
    "Assign": {
        "1": {
            "NAME": "RS_EQ_XY",
            "DIR": "XY",
            "ANGLE": 0.0,
            "SCALE": 1.0,
            "PMFT": 1.0,
            "bDAMP": True,
            "INTERP": "LOG",
            "COMTYPE": "CQC",
            "bADDSIGN": True,
            "iSIGNTYPE": 0,
            "bMODE": True,
            "aFUNCNAME": ["RS_KDS2019"],
            "aUSEMODE": [
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1},
                {"bUSE": True, "MSFACTOR": 1}
            ],
            "bCDAMP": True,
            "iMDTYPE": 1,
            "DALL": 0.05
        }
    }
}
r = requests.post(f"{BASE_URL}/db/SPLC", json=splc, headers=HEADERS)
print("STEP 2 - SPLC:", r.status_code)

# ── STEP 3: 创建时程函数（El Centro 地震波） ────────────────────────────
thfc = {
    "Assign": {
        "1": {
            "NAME": "ElCentro_EW",
            "FUNCTYPE": 1,
            "iTYPE": 1,
            "iMETHOD": 1,
            "MAXVALUE": 0.348,
            "GRAV": 9.806,
            "aFUNCDATA": [
                {"TIME": 0.02, "VALUE":  0.00517},
                {"TIME": 0.04, "VALUE":  0.00421},
                # ... 追加实际数据 ...
            ]
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THFC", json=thfc, headers=HEADERS)
print("STEP 3 - THFC:", r.status_code)

# ── STEP 4: 设置时程全局控制 ─────────────────────────────────────────
thgc = {
    "Assign": {
        "1": {
            "GNT": 0,
            "ILT": 0,
            "aILL": [{"SLC": "DL", "SF": 1.0, "LCT": 1}],
            "IEPI": True,
            "NSTEP": 1,
            "bROT": False,
            "SNIO": 1,
            "bPCF": True,
            "MAXNS": 10,
            "MAXIT": 30,
            "bDN": True,
            "bFN": False,
            "bEN": False,
            "DN": 0.001,
            "FN": 0.001,
            "EN": 0.001,
            "bULSM": False,
            "ULSM": 5,
            "ENERGYRESULT": True,
            "SDVI": True,
            "SDVE": True,
            "SDST": True,
            "SDHY": True,
            "SDIS": True,
            "bMSSSTATUS": True
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THGC", json=thgc, headers=HEADERS)
print("STEP 4 - THGC:", r.status_code)

# ── STEP 5: 创建时程荷载工况（Linear Modal Transient） ───────────────
this = {
    "Assign": {
        "1": {
            "COMMON": {
                "NAME": "TH_EQ_Linear",
                "iATYPE": 1,        # Linear
                "iAMETHOD": 1,      # Modal
                "iTHTYPE": 1,       # Transient
                "ENDTIME": 40.0,
                "INC": 0.01,
                "iOUT": 1,
                "INITMETHOD": "INIT",
                "INITLOAD": 0,
                "bDVA": False,
                "bKEEP": False,
                "iMDTYPE": 1        # Modal 阻尼
            },
            "DALL": 0.05
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THIS", json=this, headers=HEADERS)
print("STEP 5 - THIS:", r.status_code)

# ── STEP 6: 施加地面加速度 ────────────────────────────────────────────────
thga = {
    "Assign": {
        "1": {
            "NAME": "TH_EQ_Linear",
            "ANGLE": 0.0,
            "FUNCX": "ElCentro_EW",
            "SCALEX": 1.0,
            "ATIMEX": 0.0,
            "FUNCY": "ElCentro_EW",
            "SCALEY": 0.85,
            "ATIMEY": 0.0,
            "FUNCZ": "ElCentro_EW",
            "SCALEZ": 0.667,
            "ATIMEZ": 0.0
        }
    }
}
r = requests.post(f"{BASE_URL}/db/THGA", json=thga, headers=HEADERS)
print("STEP 6 - THGA:", r.status_code)

print("\n=== 动态荷载设置完成 ===")
```

---

*下一部分：[10_DB_Construction_Stage.md](./10_DB_Construction_Stage.md)*
