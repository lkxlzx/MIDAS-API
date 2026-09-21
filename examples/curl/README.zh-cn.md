# cURL 示例

> **语言：** 简体中文译文  
> **原文：** [韩文原文](./README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../docs/zh-cn/GLOSSARY.md)）

## 事前准备

1. **运行 MIDAS Gen NX**
2. 在 Open API 菜单中获取 **MAPI-Key**

## 基本用法

```bash
#!/bin/bash

BASE_URL="https://moa-engineers.midasit.com:443/gen"   # Civil NX: /civil
MAPI_KEY="your-mapi-key-here"

curl -X GET "${BASE_URL}/db/node" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json"
```

> ⚠️ 认证头部不是 `Authorization: Bearer`，而是 **`MAPI-Key`**。
> 所有 `/db/*` 请求都使用 `{"Assign": {...}}` 形式。

## 示例

### 1. 新建文档

```bash
curl -X POST "${BASE_URL}/doc/new" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### 2. 设置单位

```bash
curl -X PUT "${BASE_URL}/db/unit" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "Assign": { "1": { "DIST": "M", "FORCE": "TONF" } } }'
```

### 3. 创建节点

```bash
curl -X POST "${BASE_URL}/db/node" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "Assign": { "1": { "X": 0, "Y": 0, "Z": 0 }, "2": { "X": 0, "Y": 0, "Z": 3.2 } } }'
```

### 4. 创建单元（柱）

```bash
curl -X POST "${BASE_URL}/db/elem" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json" \
  -d '{ "Assign": { "1": { "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0 } } }'
```

### 5. 查询节点

```bash
curl -X GET "${BASE_URL}/db/node" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json"
```

### 6. 保存文档

```bash
curl -X POST "${BASE_URL}/doc/save" \
  -H "MAPI-Key: ${MAPI_KEY}" \
  -H "Content-Type: application/json"
```
