# Python 示例

> **语言：** 简体中文译文  
> **原文：** [韩文原文](./README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../docs/zh-cn/GLOSSARY.md)）

## 事前准备

1. **运行 MIDAS Gen NX**（API 与正在运行的产品通信）
2. 在 Open API 菜单中获取 **MAPI-Key**

## 安装

```bash
pip install requests python-dotenv
```

## 环境变量设置

创建 `.env` 文件并输入以下内容（建议把 `.env` 加入 `.gitignore`）：

```env
MIDAS_BASE_URL=https://moa-engineers.midasit.com:443/gen
MIDAS_MAPI_KEY=your-mapi-key-here
```

## 运行

```bash
python basic_example.py
python simple_beam_load_combination.py
```

成功时，MIDAS Gen NX 界面中会创建 1 个方形柱。

## 示例文件

- `basic_example.py` — `MidasAPI()` 辅助函数 + 新建文档→单位→材料→截面→节点→单元→支承→保存
- `simple_beam_load_combination.py` — 把简支梁 20 等分，循环创建节点/单元，并串联自重（`/db/bodf`）+
  均布梁单元荷载（`/db/bmld`）+ 荷载组合（`/db/lcom-gen`）的示例。重构自 [MIDAS Support "Example: Python"](https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python) 教程文章。

## 核心模式

```python
def MidasAPI(method, command, body=None):
    url = BASE_URL + command
    headers = {"MAPI-Key": MAPI_KEY, "Content-Type": "application/json"}
    return getattr(requests, method.lower())(url, headers=headers, json=body).json()

# 所有 /db/* 请求都使用 Assign 包装器
MidasAPI("POST", "/db/node", {"Assign": {1: {"X": 0, "Y": 0, "Z": 0}}})
```
