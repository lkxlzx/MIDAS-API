# JavaScript 示例

> **语言：** 简体中文译文  
> **原文：** [韩文原文](./README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../docs/zh-cn/GLOSSARY.md)）

## 事前准备

1. **运行 MIDAS Gen NX**
2. 在 Open API 菜单中获取 **MAPI-Key**

## Node.js 安装

```bash
npm init -y
npm install axios
```

## 基本示例

```javascript
const axios = require("axios");

const client = axios.create({
  baseURL: "https://moa-engineers.midasit.com:443/gen", // Civil NX: /civil
  headers: {
    "MAPI-Key": process.env.MIDAS_MAPI_KEY, // ⚠️ 不是 Authorization Bearer
    "Content-Type": "application/json",
  },
});

async function main() {
  // 1) 新建文档
  await client.post("/doc/new", {});

  // 2) 单位
  await client.put("/db/unit", { Assign: { 1: { DIST: "M", FORCE: "TONF" } } });

  // 3) 2 个节点
  await client.post("/db/node", {
    Assign: { 1: { X: 0, Y: 0, Z: 0 }, 2: { X: 0, Y: 0, Z: 3.2 } },
  });

  // 4) 柱单元
  await client.post("/db/elem", {
    Assign: { 1: { TYPE: "BEAM", MATL: 1, SECT: 1, NODE: [1, 2], ANGLE: 0 } },
  });

  // 5) 保存
  await client.post("/doc/save");
  console.log("完成!");
}

main().catch((e) => console.error(e.response?.status, e.message));
```

## 在浏览器中使用

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const BASE_URL = "https://moa-engineers.midasit.com:443/gen";
  const MAPI_KEY = "your-mapi-key-here";

  axios.get(`${BASE_URL}/db/node`, {
    headers: { "MAPI-Key": MAPI_KEY, "Content-Type": "application/json" },
  })
  .then((res) => console.log(res.data))
  .catch((err) => console.error(err));
</script>
```

> 参考：所有 `/db/*` 请求都使用 `{ Assign: { "<ID>": { ... } } }` 形式。

---

## 示例文件 / Example Files

### [auto-save-before-analysis.html](./zh-cn/auto-save-before-analysis.html)

**ZH-CN** — 执行分析前的自动保存模式。核心流程：

1. `GET /mapikey/verify` → 确认连接状态（`j.user` 仅用于显示，不用于构成保存路径）
2. 用调用者指定的保存文件夹（`saveDir`，未指定时回退到 `C:/Temp`）构成文件路径
3. `POST /doc/saveas` → 保存完成后
4. `POST /doc/anal` → 执行分析

注意事项：
- 必须先调用 `/doc/saveas`，**再**调用 `/doc/anal`。顺序颠倒时 Gen NX 会弹出保存对话框，自动化流程因此中断。
- `%USERPROFILE%` 之类的环境变量 MAPI 服务器无法识别。
- ⚠️ 不要拿登录邮箱（`/mapikey/verify` 返回的 `j.user`）的前半部分当作 Windows 用户名去推断 `C:/Users/{邮箱前半部分}/...` 路径 —— 登录邮箱账号与 PC 上实际的 Windows 账号名可能不同。保存文件夹必须由调用者直接指定一个真实存在的路径。
- `/doc/SAVEAS` 官方文档并未说明目标文件夹不存在时的行为，但**已通过真实 MAPI 调用确认**（2026-08-31）：文件夹不存在时 Gen NX 会弹出"存在无效路径"错误对话框，MAPI 调用超时，文件夹不会被自动创建。提前创建该文件夹即可正常保存并返回 `200 OK`（`C:/Temp` 也不是 Windows 默认文件夹，可能需要自行创建）。
- 请在创建模型（`PUT /db/node` 等）**之前**用 `PUT /db/unit` 设置单位制。若 Gen NX 正以其他单位打开，坐标会被错误解析，从而产生分析警告。

**EN** — Auto-save pattern before running structural analysis. Key flow:

1. `GET /mapikey/verify` → confirm the connection (`j.user` is for display only, not used to build the save path)
2. Build the file path inside a caller-provided save folder (`saveDir`, falls back to `C:/Temp`)
3. `POST /doc/saveas` → save the file first
4. `POST /doc/anal` → then run analysis

Important notes:
- Always call `/doc/saveas` **before** `/doc/anal`. Reversing the order causes Gen NX to show a save dialog, which blocks automation.
- Environment variables like `%USERPROFILE%` are **not** resolved by the MAPI server.
- ⚠️ Don't guess a Windows folder from the local part of the login email (`j.user` from `/mapikey/verify`) — the login email account and the PC's actual Windows account name can differ. Always pass a real, existing folder as the save directory yourself.
- The official `/doc/SAVEAS` doc does not state what happens if the target folder doesn't exist, but this was **verified with a live MAPI call** (2026-08-31): if the folder is missing, Gen NX shows an "invalid path" error dialog and the MAPI call times out — the folder is not auto-created. Creating it beforehand results in a normal `200 OK` save (`C:/Temp` is not a default Windows folder either, so you may need to create it yourself).
- Set the unit system via `PUT /db/unit` **before** creating model entities (`PUT /db/node`, etc.). If Gen NX is open in a different unit, coordinates will be misinterpreted and analysis warnings will occur.
