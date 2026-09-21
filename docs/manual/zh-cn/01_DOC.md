# 01. DOC — 文档管理 Endpoints

> **出处：** [MIDAS API Online Manual – DOC](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)  
> **官方最后编辑：** 2025.11.04 · **本文件同步：** 2026-06-29  
> **适用产品：** MIDAS Civil NX · MIDAS Gen NX

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../01_DOC.md) · **原文同步日期：** 2026-06-29  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

## 概述

`/doc/*` Endpoint 负责 MIDAS NX 文件（文档）的创建、打开、保存、关闭、导入、导出与执行分析。

**通用规则：**
- **HTTP 方法：** 仅 `POST`
- **请求体：** 以 `"Argument"` 键起始
- 请求体为空时使用 `{"Argument": {}}`

| No. | Endpoint | 功能 | 请求体类型 |
|-----|----------|------|-----------|
| 1 | [`/doc/NEW`](#1-docnew--new-project) | 新建项目 | Empty Object |
| 2 | [`/doc/OPEN`](#2-docopen--open-project) | 打开项目 | File Path (String) |
| 3 | [`/doc/CLOSE`](#3-docclose--close-project) | 关闭项目 | Empty Object |
| 4 | [`/doc/SAVE`](#4-docsave--save) | 保存 | Empty Object |
| 5 | [`/doc/SAVEAS`](#5-docsaveas--save-as) | 另存为 | File Path (String) |
| 6 | [`/doc/STAGAS`](#6-docstagas--save-current-stage-as) | 将当前阶段另存为 | Object |
| 7 | [`/doc/IMPORT`](#7-docimport--import-to-json) | 载入 JSON 文件 | File Path (String) |
| 8 | [`/doc/IMPORTMXT`](#8-docimportmxt--import-to-mctmgt) | 载入 MCT/MGT 文件 | File Path (String) |
| 9 | [`/doc/EXPORT`](#9-docexport--export-to-json) | 导出为 JSON 文件 | File Path (String) |
| 10 | [`/doc/EXPORTMXT`](#10-docexportmxt--export-to-mctmgt) | 导出为 MCT/MGT 文件 | File Path (String) |
| 11 | [`/doc/ANAL`](#11-docanal--perform-analysis) | 执行分析 | Empty Object / Object |

---

## 通用辅助函数（Python）

所有示例代码均以以下辅助函数为前提。

```python
import requests
import os

# 建议从 .env 或环境变量加载
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method: str, endpoint: str, body=None):
    """
    MIDAS NX Open API 调用辅助函数。

    Args:
        method  : HTTP 方法字符串 ("POST", "GET", "PUT", "DELETE")
        endpoint: API 路径（例："/doc/new"）
        body    : 请求体（dict）。为 None 时发送空请求体。

    Returns:
        dict: JSON 响应
    """
    url = BASE_URL + endpoint
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": MAPI_KEY,
    }
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}
```

---

## 1. `/doc/NEW` — New Project

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/NEW` |
| **Method** | `POST` |
| **官方文档** | [New Project ↗](https://support.midasuser.com/hc/en-us/articles/35994078198681) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/NEW",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Request Example

```json
{
  "Argument": {}
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | - | - | - |

### Python 示例

```python
# 新建项目
result = midas_api("POST", "/doc/new", {"Argument": {}})
print(result)
```

---

## 2. `/doc/OPEN` — Open Project

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/OPEN` |
| **Method** | `POST` |
| **官方文档** | [Open Project ↗](https://support.midasuser.com/hc/en-us/articles/35994112560793) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/OPEN",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mcb"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Opened File Path | - | String | - | - |

### Python 示例

```python
# 打开已有项目（绝对路径）
file_path = r"C:\MIDAS\MyProject.mcb"
result = midas_api("POST", "/doc/open", {"Argument": file_path})
print(result)
```

---

## 3. `/doc/CLOSE` — Close Project

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/CLOSE` |
| **Method** | `POST` |
| **官方文档** | [Close Project ↗](https://support.midasuser.com/hc/en-us/articles/35994162529305) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/CLOSE",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Request Example

```json
{
  "Argument": {}
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | Object | - | - |

### Python 示例

```python
# 关闭当前打开的项目
result = midas_api("POST", "/doc/close", {"Argument": {}})
print(result)
```

---

## 4. `/doc/SAVE` — Save

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/SAVE` |
| **Method** | `POST` |
| **官方文档** | [Save ↗](https://support.midasuser.com/hc/en-us/articles/35994210207513) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/SAVE",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {}
    }
  }
}
```

### Request Example

```json
{
  "Argument": {}
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | - | - | - |

### Python 示例

```python
# 保存当前项目
result = midas_api("POST", "/doc/save", {"Argument": {}})
print(result)
```

---

## 5. `/doc/SAVEAS` — Save As

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/SAVEAS` |
| **Method** | `POST` |
| **官方文档** | [Save As ↗](https://support.midasuser.com/hc/en-us/articles/35994277012377) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/SAVEAS",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mcb"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Save File Path | - | String | - | - |

### Python 示例

```python
# 以其他名称保存到其他路径
save_path = r"C:\MIDAS\MyProject_v2.mcb"
result = midas_api("POST", "/doc/saveas", {"Argument": save_path})
print(result)
```

---

## 6. `/doc/STAGAS` — Save Current Stage As

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/STAGAS` |
| **Method** | `POST` |
| **官方文档** | [Save Current Stage As ↗](https://support.midasuser.com/hc/en-us/articles/50707525717401) |

### JSON Schema

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\FASE1.mcb",
    "STAGE_STEP": "Fase1"
  }
}
```

### Request Example

```json
{
  "Argument": {
    "EXPORT_PATH": "C:\\MIDAS\\FASE1.mcb",
    "STAGE_STEP": "Fase1"
  }
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Save File Path | `"EXPORT_PATH"` | String | - | - |
| 2 | Stage Step Name | `"STAGE_STEP"` | String | - | **Required** |

### Python 示例

```python
# 将当前施工阶段保存为独立文件
result = midas_api("POST", "/doc/stagas", {
    "Argument": {
        "EXPORT_PATH": r"C:\MIDAS\Stage1.mcb",  # 保存路径（可选）
        "STAGE_STEP": "Stage1",                  # 阶段名称（必填）
    }
})
print(result)
```

---

## 7. `/doc/IMPORT` — Import to JSON

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/IMPORT` |
| **Method** | `POST` |
| **官方文档** | [Import to Json ↗](https://support.midasuser.com/hc/en-us/articles/35994338816793) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/IMPORT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.json"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | JSON File Path | - | String | - | - |

### Python 示例

```python
# 将 JSON 文件载入到当前项目
json_path = r"C:\MIDAS\ModelData.json"
result = midas_api("POST", "/doc/import", {"Argument": json_path})
print(result)
```

---

## 8. `/doc/IMPORTMXT` — Import to mct/mgt

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/IMPORTMXT` |
| **Method** | `POST` |
| **官方文档** | [Import to mct/mgt ↗](https://support.midasuser.com/hc/en-us/articles/35994365225113) |
| **产品限制** | Civil NX：`.mct` / Gen NX：`.mgt` |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/IMPORTMXT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mct"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | MCT/MGT File Path | - | String | - | - |

> ⚠️ Civil NX 使用 `.mct`，Gen NX 使用 `.mgt` 文件格式。

### Python 示例

```python
# 载入 MCT 文件（Civil NX）
mct_path = r"C:\MIDAS\BridgeModel.mct"
result = midas_api("POST", "/doc/importmxt", {"Argument": mct_path})
print(result)

# 载入 MGT 文件（Gen NX）
mgt_path = r"C:\MIDAS\BuildingModel.mgt"
result = midas_api("POST", "/doc/importmxt", {"Argument": mgt_path})
print(result)
```

---

## 9. `/doc/EXPORT` — Export to JSON

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/EXPORT` |
| **Method** | `POST` |
| **官方文档** | [Export to Json ↗](https://support.midasuser.com/hc/en-us/articles/35994422273305) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/EXPORT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.json"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | JSON File Path | - | String | - | - |

### Python 示例

```python
# 将当前项目导出为 JSON 文件
export_path = r"C:\MIDAS\ModelExport.json"
result = midas_api("POST", "/doc/export", {"Argument": export_path})
print(result)
```

---

## 10. `/doc/EXPORTMXT` — Export to mct/mgt

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/EXPORTMXT` |
| **Method** | `POST` |
| **官方文档** | [Export to mct/mgt ↗](https://support.midasuser.com/hc/en-us/articles/35994462805017) |
| **产品限制** | Civil NX：`.mct` / Gen NX：`.mgt` |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/EXPORTMXT",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "string"
    }
  }
}
```

### Request Example

```json
{
  "Argument": "C:\\MIDAS\\FSM.mct"
}
```

### Specifications

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | MCT/MGT File Path | - | String | - | - |

> ⚠️ Civil NX 使用 `.mct`，Gen NX 使用 `.mgt` 文件格式。

### Python 示例

```python
# 导出为 MCT 文件（Civil NX）
export_path = r"C:\MIDAS\BridgeExport.mct"
result = midas_api("POST", "/doc/exportmxt", {"Argument": export_path})
print(result)
```

---

## 11. `/doc/ANAL` — Perform Analysis

### 基本信息

| 项目 | 值 |
|------|----|
| **Input URI** | `{base url}/doc/ANAL` |
| **Method** | `POST` |
| **官方文档** | [Perform Analysis ↗](https://support.midasuser.com/hc/en-us/articles/35685160815897) |

### JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "doc/ANAL",
  "type": "object",
  "properties": {
    "Argument": {
      "type": "object",
      "properties": {
        "TYPE": {
          "type": "string"
        }
      }
    }
  }
}
```

### Request Examples

**一般分析（Perform Analysis）**
```json
{}
```

**推覆分析（Pushover Analysis）**
```json
{
  "Argument": {
    "TYPE": "Pushover"
  }
}
```

### Specifications

**Perform Analysis**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Empty Object | - | - | - | - |

**Pushover Analysis**

| No. | Description | Key | Value Type | Default | Required |
|-----|-------------|-----|------------|---------|----------|
| 1 | Input Analysis Type · `"Pushover"` | `"TYPE"` | String | - | **Required** |

### Python 示例

```python
# 执行一般线性/非线性分析
result = midas_api("POST", "/doc/anal", {})
print(result)

# 执行推覆分析
result = midas_api("POST", "/doc/anal", {
    "Argument": {
        "TYPE": "Pushover"
    }
})
print(result)
```

---

## 完整工作流示例

典型的建模自动化流程：

```python
import requests
import os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

def midas_api(method: str, endpoint: str, body=None):
    url = BASE_URL + endpoint
    headers = {
        "Content-Type": "application/json",
        "MAPI-Key": MAPI_KEY,
    }
    response = getattr(requests, method.lower())(url, headers=headers, json=body)
    print(f"[{response.status_code}] {method.upper()} {endpoint}")
    return response.json() if response.text else {}


# ── Step 1：新建项目 ──────────────────────────────
midas_api("POST", "/doc/new", {"Argument": {}})

# ── Step 2：录入模型数据（使用 db/* 端点）─────────
# 设置单位、材料、截面、节点、单元、荷载等
# （参见 02_DB_Project_Structure.md ~ 12_DB_Load_Combinations.md）

# ── Step 3：保存 ─────────────────────────────────
midas_api("POST", "/doc/save", {"Argument": {}})

# ── Step 4：执行分析 ────────────────────────────
midas_api("POST", "/doc/anal", {})

# ── Step 5：确认结果后另存为 ──────────────────────
midas_api("POST", "/doc/saveas", {"Argument": r"C:\MIDAS\Result_v1.mcb"})

# ── Step 6：关闭项目（可选）──────────────────────────
midas_api("POST", "/doc/close", {"Argument": {}})
```

---

## HTTP 状态码

| 状态码 | 说明 | 处理建议 |
|------|------|------|
| `200` | 请求成功 | - |
| `400` | 请求错误（JSON/字段错误） | 检查请求体 |
| `401` | 认证失败 | 检查 `MAPI-Key` 头部取值 |
| `403` | 拒绝访问 | 检查密钥权限与授权 |
| `404` | 路径错误 | 检查 Base URL 与 Endpoint 路径 |
| `500` | 服务器错误 | 确认 MIDAS Gen NX 是否已运行 |

> ⚠️ **最常见的错误：** 在 MIDAS Gen NX（或 Civil NX）未运行的状态下调用 API，会发生连接失败或超时。

---

## 相关文档

- [INDEX.md](./INDEX.md) — 全部 Endpoint 目录
- [02_DB_Project_Structure.md](./02_DB_Project_Structure.md) — 项目与单位设置
- [MIDAS API Online Manual (官方)](https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual)
