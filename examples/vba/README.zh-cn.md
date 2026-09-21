# Excel VBA 示例

> **语言：** 简体中文译文  
> **原文：** [韩文原文](./README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../docs/zh-cn/GLOSSARY.md)）

## 事前准备

1. **运行 MIDAS Civil NX 或 Gen NX**
2. 在 Open API 菜单中获取 **MAPI-Key**
3. 在 Excel 中按 `ALT+F11`（VBA 编辑器）或启用"开发工具"选项卡
   （文件 → 选项 → 自定义功能区 → 勾选"开发工具"）

## JSON 处理所需的库安装

VBA 没有处理 JSON 的内置功能，因此需要外部库。

1. 下载 [VBA-JSON](https://github.com/VBA-tools/VBA-JSON) 的 `JsonConverter.bas`
2. VBA 编辑器 → 右键点击模块 → "文件导入" → 选择 `JsonConverter.bas`
3. 在"工具 → 引用"中勾选 **"Microsoft Scripting Runtime"**（Dictionary 的 Early binding 需要）

## 示例文件

- [`SimpleBeamLoadCombination.bas`](./zh-cn/SimpleBeamLoadCombination.bas) — `WebRequest()` 辅助函数（基于 `WinHttp.WinHttpRequest.5.1`）+
  把简支梁 20 等分，循环创建节点/单元，并串联自重（`/db/bodf`）+ 均布梁单元荷载（`/db/bmld`）+ 荷载组合（`/db/lcom-gen`）的示例。
  由于该示例的结构是从 Excel 工作表单元格读取输入值，运行前必须按下表"工作表输入布局"填好数值。
  重构自 [MIDAS Support "Example: Excel VBA"](https://support.midasuser.com/hc/en-us/articles/30506684736665-Example-Excel-VBA) 教程文章。

### 工作表输入布局（依据原文文章）

| 单元格 | 值 | 说明 |
|---|---|---|
| `E5` | 距离单位（例：`M`） | |
| `E6` | 力单位（例：`KN`） | |
| `E8` | 梁长度 | |
| `E9` | 截面高度 | |
| `E10` | 截面宽度 | |
| `E12:E15` | 材料/截面/起始节点/起始单元 ID | 按此顺序 |
| `I9` / `J9` | 梁单元荷载方向（例：`GZ`）/ 大小 | |
| `I12:J13` | 荷载组合系数·荷载工况名称 2 行 | （系数，LC 名称） |
| `J5` / `J6` | 材料标准 / 材料等级（例：`AS17(RC)` / `C32`） | |
| `H15` / `H16` | Base URL / MAPI-Key | |

## 运行

1. 将 `JsonConverter.bas` 与 `SimpleBeamLoadCombination.bas` 都导入项目
2. 在工作表中填写输入值（参考上表）
3. 开发工具 → 插入 → 按钮（窗体控件）→ 关联 `CreateSimpleBeam` 宏
4. 在 MIDAS Civil NX 已运行的状态下点击按钮

## 核心模式

```vb
Function WebRequest(Method As String, Command As String, body As String) As String
    Dim req As Object
    Set req = CreateObject("WinHttp.WinHttpRequest.5.1")
    req.Open Method, baseURL & Command, False
    req.SetRequestHeader "Content-type", "application/json"
    req.SetRequestHeader "MAPI-Key", MAPI_Key
    req.Send body
    WebRequest = req.ResponseText
End Function

' 所有 /db/* 请求都使用 Assign 包装器 (Dictionary → JsonConverter.ConvertToJson)
Dim dicMain As Scripting.Dictionary: Set dicMain = New Dictionary
' ...
dicMain.Add "Assign", dicSub1
body = JsonConverter.ConvertToJson(dicMain)
WebRequest "POST", "/db/node", body
```
