# Guiding for writing Python Code (Planning/Development Collaboration)

> **原文：** [Guiding for writing Python Code (Planning/Development Collaboration)](https://support.midasuser.com/hc/ko/articles/44321576105497-Guiding-for-writing-Python-Code-Planning-Development-Collaboration)
> **原文创建/编辑：** 2025-03-10

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../guide/03_Python_Coding_Guide.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 目的

即使 Plug-in 规划者不必向开发者长篇解释意图，只要先写好**承载意图的 Python 代码**，就能缩短开发着手时间。原文的提议是：把文件简单地结构化为 3 个类别，只定义好 `main` 与 `components`，无需单独的设计文档，仅凭设计 + Python 代码即可直接开始开发。

## 基本规则

- 截至本使用说明的时点，网页环境中可用的 Python 版本为 **3.11.2**。
- 所有 Python 代码都要**以函数封装**。
- 不直接执行代码，而是定义 `def do():` 并调用 `do()` 进行测试。

```python
# 常规写法的 main.py
a = 1
b = 1
value = a + b
print(value)
```

```python
# 函数化后的 main.py
def summation(a, b):
    return a + b

# 把下面三行注释掉，Python 代码就不会立即执行。
a = 1
b = 1
summation(a, b)
```

填入 UI 的数据也用 Python 代码编写。例如只想把 `NODE` 数据的 `X` 值填入 Drop List 时，按如下方式编写。

```python
# components.py
def getNodeX4CompDropList():
    civil = MidasAPI(Product.CIVIL, "KR")
    nodeEntries = civil.dbRead("NODE")
    nodeXs = []
    for entry_id, entry_values in nodeEntries.items():
        x_value = entry_values.get("X")
        if x_value is not None:
            nodeXs.append(x_value)
    return nodeXs  # [1, 2, 3, ...] NODE 的 X 值
```

> `MidasAPI(...).dbRead("NODE")` 看起来是通过这个 Python 包装器调用 JSON Manual 的 [`GET /db/NODE`](../../../manual/zh-cn/03_DB_Node_Element.md) Endpoint。开发 Plug-in 时传给 `dbRead`/`dbWrite` 等的表代码（`"NODE"`、`"ELEM"` 等）与 `docs/manual/` 中整理的 `/db/*` Endpoint 的 URI 代码互相对应，因此阅读 Plug-in 代码时一并参考对应的 Endpoint 文档，就可以快速掌握 Schema。

`main.py` 中的函数要写成接收参数的形式。例如若存在把 Drop List 中选定的某个 Node 的 X 值放大 2 倍的主逻辑，就采用把选中的 Node X 值作为参数传入的方式编写。

```python
# main.py
def main(selectedNodeX):
    result = selectedNodeX * 2
    print(result)

# 测试用代码
selectedNodeX = 1  # 假设在 Drop List(Node X) 中选择了 1
main(selectedNodeX)  # 输出：2
```

## Python 文件的 3 个类别

| 文件 | 作用 |
| --- | --- |
| `main.py` | 定义接收 UI 的值后最终执行的逻辑 |
| `components.py` | 定义填入 UI 组件的值。因返回实际数据，无需设计文档说明即可直接填入 UI |
| （命名自由，例：`sub_logics.py`） | 定义辅助 `main` 函数的逻辑。把所有代码都塞进 `main` 会降低可读性，故拆分为一个或多个文件 |

```python
# main.py
from multiple import calc2x

def main(selectedNodeX):
    result = calc2x(selectedNodeX)
    print(result)

selectedNodeX = 1
main(selectedNodeX)
```

```python
# multiple.py（辅助逻辑文件 — 名称自由）
def calc2x(value):
    return value * 2
```

## Python 代码测试指南

在 Plug-in Item 开发环境中直接运行 Python 代码，即可编写能直接应用的代码。

1. 在 VS Code 中安装 **Live Server** 扩展 — 保存即可启动可立即运行的本地服务器并打开网页。
2. 获取 `engineers-api-python` 仓库，添加 `pyscript_tester` 目录。
3. 要开始新项目时，复制 `pyscript_tester` 生成新文件夹。
4. 在 VS Code 中把复制后的文件夹作为项目打开。
5. 在左侧树中点击 `index.html`，然后点击右下角的 **Go Live**。若 Live Server 正常安装，右下角会显示 "Go Live"。
6. 浏览器打开并出现测试画面，即表示测试环境配置完成。

基本结构是运行 `pyscript_main.py` 的方式。要编写辅助 Python 文件时，先创建辅助文件，再把文件名添加到 `pyscript_config.json` 即可。

> ⚠️ 原文中提到了 `engineers-api-python` 仓库·截图，但实际仓库 URL 未出现在原文文本里（仅以图片形式提供），因此本文档中没有凭推测填入。需要时请直接打开原文文章，确认图片中的链接。
