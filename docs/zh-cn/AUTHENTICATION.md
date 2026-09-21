# 认证设置指南

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../AUTHENTICATION.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](./GLOSSARY.md)）

MIDAS NX Open API 通过 **`MAPI-Key`** 头部进行认证。

---

## 🔑 MAPI-Key 签发

`MAPI-Key` 直接在 **MIDAS Gen NX（或 Civil NX）应用**中签发。

1. 启动 MIDAS Gen NX。
2. 在 Open API / Apps 菜单中选择 **API Key 签发**。
3. 复制生成的密钥（长字符串）。

> `MAPI-Key` 是**临时密钥**。服务器用该密钥识别要连接哪个产品（正在运行的 Gen NX）。
> 可随时重新签发，是由几乎无法随机猜到的长字符/数字组合构成。

---

## 📍 Base URL

```
https://moa-engineers.midasit.com:443/gen      # MIDAS Gen NX
https://moa-engineers.midasit.com:443/civil    # MIDAS Civil NX
```

> 提供按地区划分的备用服务器。请确认符合自身使用环境的服务器地址。

---

## 🔐 认证头部

所有请求头部需包含以下内容。

```
MAPI-Key: YOUR_MAPI_KEY
Content-Type: application/json
```

> ⚠️ 认证使用的是 **`MAPI-Key`** 头部，而不是 `Authorization: Bearer`。

---

## 💻 各语言设置

### Python

```python
import requests, os

BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

headers = {
    "MAPI-Key": MAPI_KEY,
    "Content-Type": "application/json",
}

res = requests.get(f"{BASE_URL}/db/node", headers=headers)
print(res.status_code, res.json())
```

### JavaScript (Node.js)

```javascript
const axios = require("axios");

const client = axios.create({
  baseURL: "https://moa-engineers.midasit.com:443/gen",
  headers: {
    "MAPI-Key": process.env.MIDAS_MAPI_KEY,
    "Content-Type": "application/json",
  },
});

client.get("/db/node").then(r => console.log(r.data));
```

### cURL

```bash
curl -X GET "https://moa-engineers.midasit.com:443/gen/db/node" \
  -H "MAPI-Key: $MIDAS_MAPI_KEY" \
  -H "Content-Type: application/json"
```

### Excel VBA

```vb
Sub GetNodes()
    Dim http As Object
    Set http = CreateObject("MSXML2.XMLHTTP")
    http.Open "GET", "https://moa-engineers.midasit.com:443/gen/db/node", False
    http.SetRequestHeader "MAPI-Key", "your-mapi-key-here"
    http.SetRequestHeader "Content-Type", "application/json"
    http.Send
    MsgBox http.responseText
End Sub
```

---

## 💡 实战技巧

### 找不到 JSON Schema 时 — GET → 修改 → PUT/POST

当某类数据的 JSON 结构在手册中一眼找不到时，不去翻查手册，而是直接从产品里提取的方法。

1. 在 MIDAS Gen/Civil NX GUI 中直接输入所需数据。
2. 以 `GET` 查询对应资源，确认实际的 JSON 格式。
3. 把响应的顶层键（例：`"NODE"`）**改为 `"Assign"`**，其余原样复用为 `PUT`/`POST` 请求体。
4. 反过来，也可以在产品中删掉数据后，用 `POST` 输入期望值进行验证。

```python
# 1) 用 GET 确认在 GUI 中创建的数据
resp = requests.get(f"{BASE_URL}/db/node", headers=HEADERS).json()
# resp == {"NODE": {"1": {"X": 0, "Y": 0, "Z": 0}, ...}}

# 2) 只把顶层键换成 "Assign"，其余原样复用
body = {"Assign": resp["NODE"]}
requests.put(f"{BASE_URL}/db/node", headers=HEADERS, json=body)
```

### `/info/db/...` — DB 资源 Schema 内省

在 `baseURL` 与 `db` 之间插入 `info`，服务器就会直接返回该 DB 资源的 Key 说明与 Value 类型。
字段未收录于手册、或想即时确认最新规格时很有用。

```bash
curl -X GET "https://moa-engineers.midasit.com:443/civil/info/db/node" \
  -H "MAPI-Key: $MIDAS_MAPI_KEY"
```

> 普通端点是 `{base url}/db/NODE`，内省端点则在 `db` 前面加 `info`，
> 形如 `{base url}/info/db/NODE`。

---

## 🛡️ 安全提示

### ✅ 应该做的
- 将 `MAPI-Key` 保存在 `.env` 文件中，通过环境变量使用
- 把 `.env` 加入 `.gitignore`
- 疑似泄露时立即在应用中重新签发

### ❌ 不应做的
- 在代码中硬编码密钥
- 把密钥上传到公开仓库（GitHub 等）

### .env 示例
```env
MIDAS_BASE_URL=https://moa-engineers.midasit.com:443/gen
MIDAS_MAPI_KEY=your-mapi-key-here
```

```python
import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("MIDAS_BASE_URL")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY")
```

---

## ⚠️ 错误解决

| 代码 | 原因 | 解决方法 |
|------|------|------|
| 401 Unauthorized | 密钥错误/缺失 | 确认 `MAPI-Key` 头部取值 |
| 403 Forbidden | 权限不足 | 确认密钥权限/产品许可证 |
| 连接失败/超时 | **Gen NX 未运行** | 确认 MIDAS Gen NX 是否已运行 |
| Base URL 错误(404) | 服务器/路径不正确 | 确认 `/gen` 或 `/civil` 路径 |

> 最常见的失误：**MIDAS Gen NX 处于未运行状态**。服务器必须与正在运行的
> 产品建立 WebSocket 连接才能工作。

### 连接前状态确认 — `/mapikey/verify`

在连续发送多个请求之前，可以先确认产品是否正常连接到服务器。
取 Base URL 中去掉产品路径（`/gen`、`/civil`）后的地址，接上 `/mapikey/verify`，以 `GET` 调用。

```bash
curl -X GET "https://moa-engineers.midasit.com:443/mapikey/verify" \
  -H "MAPI-Key: $MIDAS_MAPI_KEY"
```

```json
{
    "user": "User_ID",
    "program": "civil",
    "connectionID": "Connection_ID",
    "keyVerified": true,
    "status": "connected"
}
```

| 键 | 含义 |
| --- | --- |
| `status` | 产品-服务器连接状态 |
| `keyVerified` | MAPI-Key 是否有效 |
| `user` | 登录到产品的用户 ID |
| `program` | 已连接的产品（`gen` / `civil`） |
| `connectionID` | 用于标识客户端的易失性 ID |

### 内网/防火墙环境连接问题

按下 "Connect" 按钮后状态没有变化时，多数情况是企业内防火墙拦截了对外的
`http(s)`/`WebSocket` 请求。请携带以下信息向网络/安全团队申请放行。

| 项目 | 值 |
| --- | --- |
| Protocol | `https`, `wss` |
| Port | `443` |
| IP | `121.157.60.1/32` (MIDAS Public NAT IP) |
| URI | `https://moa-engineers.midasit.com` |

> **SSL 拦截（SSL Inspection）环境注意：** 企业内代理对所有流量启用 SSL 拦截时，
> 必须把 `moa-engineers.midasit.com` 从拦截对象中排除才能建立连接。
> 已有多家企业客户通过该设置解决了问题 — 即使防火墙/代理本身正常，也可能因
> SSL 拦截导致连接被拒，请把这一点一并告知 network/安全团队。

---

## 📝 下一步

1. [README 快速开始](../../README.zh-cn.md#-快速开始-python) - 创建第一个模型
2. [MIDAS API JSON Manual 目录](../manual/zh-cn/INDEX.md) - 全部端点·JSON Schema
