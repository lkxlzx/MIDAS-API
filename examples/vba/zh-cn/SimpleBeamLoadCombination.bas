Attribute VB_Name = "SimpleBeamLoadCombination"
Option Explicit

' 语言：简体中文译文 | 原文：[韩文原文](../SimpleBeamLoadCombination.bas) · 译文生成：2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）
'
' MIDAS NX Open API - Excel VBA 示例：简支梁荷载组合
'
' 把 10m 简支梁（两端铰/滚动支承）20 等分来创建节点/单元，
' 在施加自重(DL) + 均布梁单元荷载(SIDL)之后再构成荷载组合的示例。
' 与 examples/python/simple_beam_load_combination.py 流程相同的 VBA 版本。
'
' 出处：MIDAS Support - Example: Excel VBA
' https://support.midasuser.com/hc/en-us/articles/30506684736665-Example-Excel-VBA
' （按本仓库风格重构官方教程文章的版本。
'  原文教程文章中单元生成循环的上限写的是 "0 To num_division"，
'  因此存在引用并不存在的第 (num_division+2) 个节点的 off-by-one 错误。
'  下方代码已改为 "0 To num_division - 1" —— 这也与同一文章组的
'  Python 版本(examples/python/simple_beam_load_combination.py)的循环范围一致。）
'
' 事前准备：
'   1) 导入 JsonConverter.bas (VBA-JSON, https://github.com/VBA-tools/VBA-JSON)
'   2) 工具 → 引用 → 勾选 "Microsoft Scripting Runtime"
'   3) 在工作表中填写输入值（参考 README.md 的"工作表输入布局"）

' REST API 调用辅助函数
Function WebRequest(Method As String, Command As String, body As String) As String

    Dim TCRequestItem As Object
    Dim baseURL As String
    Dim URL As String
    Dim MAPI_Key As Variant

    Set TCRequestItem = CreateObject("WinHttp.WinHttpRequest.5.1")

    'SetTimeouts(resolveTimeout, ConnectTimeout, SendTimeout, ReceiveTimeout)
    TCRequestItem.SetTimeouts 200000, 200000, 200000, 200000

    baseURL = Cells(15, "H").Value
    MAPI_Key = Cells(16, "H").Value

    URL = baseURL & Command
    TCRequestItem.Open Method, URL, False
    TCRequestItem.SetRequestHeader "Content-type", "application/json"
    TCRequestItem.SetRequestHeader "MAPI-Key", MAPI_Key
    TCRequestItem.Send body
    WebRequest = TCRequestItem.ResponseText

    Debug.Print Command & " : " & TCRequestItem.Status & " - " & TCRequestItem.StatusText

End Function

Sub CreateSimpleBeam()

    Dim i As Long

    ' 从工作表读取输入值
    Dim dist As String
    Dim force As String
    Dim length As Double
    Dim height As Double
    Dim width As Double
    Dim direction As String
    Dim loadValue As Double
    Dim modelID As Range
    Dim loadCase As Range
    Dim matSt As String
    Dim matDB As String

    dist = UCase(Cells(5, "E").Value)
    force = UCase(Cells(6, "E").Value)

    length = Cells(8, "E").Value
    height = Cells(9, "E").Value
    width = Cells(10, "E").Value

    direction = Cells(9, "I").Value
    loadValue = Cells(9, "J").Value

    matSt = Cells(5, "J").Value
    matDB = Cells(6, "J").Value

    Set loadCase = Range(Cells(12, "I"), Cells(13, "J"))
    Set modelID = Range(Cells(12, "E"), Cells(15, "E"))

    Dim dicMain As Scripting.Dictionary
    Dim dicSub1 As Scripting.Dictionary
    Dim dicSub2 As Scripting.Dictionary
    Dim dicSub3 As Scripting.Dictionary
    Dim dicSub4 As Scripting.Dictionary
    Dim response As String
    Dim body As String

    Dim num_division As Long
    Dim interval As Double
    num_division = 20
    interval = length / num_division

    ' 1) 新建文档
    response = WebRequest("POST", "/doc/new", "{}")
    Debug.Print response

    ' 2) 单位
    Set dicMain = New Dictionary
    Set dicSub1 = New Dictionary: Set dicSub2 = New Dictionary

    dicSub2.Add "DIST", dist
    dicSub2.Add "FORCE", force
    dicSub1.Add "1", dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("PUT", "/db/unit", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing: Set dicSub2 = Nothing

    ' 3) 材料（RC）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

    dicSub3.Add "P_TYPE", 1
    dicSub3.Add "STANDARD", matSt
    dicSub3.Add "DB", matDB

    dicSub2.Add "TYPE", "CONC"
    dicSub2.Add "NAME", matDB
    dicSub2.Add "PARAM", Array(dicSub3)

    dicSub1.Add modelID(1, 1), dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/matl", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing: Set dicSub3 = Nothing

    ' 4) 截面（矩形数值输入截面）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary: Set dicSub4 = New Dictionary

    dicSub4.Add "vSIZE", Array(height, width)

    dicSub3.Add "USE_SHEAR_DEFORM", True
    dicSub3.Add "SHAPE", "SB"
    dicSub3.Add "DATATYPE", 2
    dicSub3.Add "SECT_I", dicSub4

    dicSub2.Add "SECTTYPE", "DBUSER"
    dicSub2.Add "SECT_NAME", "Rectangular"
    dicSub2.Add "SECT_BEFORE", dicSub3

    dicSub1.Add modelID(2, 1), dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/sect", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing: Set dicSub3 = Nothing: Set dicSub4 = Nothing

    ' 5) 节点（把 0 ~ length 按 num_division 等分 → num_division+1 个）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To num_division
        Set dicSub2 = New Dictionary

        dicSub2.Add "X", i * interval
        dicSub2.Add "Y", 0
        dicSub2.Add "Z", 0

        dicSub1.Add modelID(3, 1) + i, dicSub2

        Set dicSub2 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/node", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 6) 单元（按顺序把相邻节点用 BEAM 连接 → num_division 个）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To num_division - 1
        Set dicSub2 = New Dictionary

        dicSub2.Add "TYPE", "BEAM"
        dicSub2.Add "MATL", modelID(1, 1)
        dicSub2.Add "SECT", modelID(2, 1)
        dicSub2.Add "NODE", Array(modelID(3, 1) + i, modelID(3, 1) + i + 1)

        dicSub1.Add modelID(4, 1) + i, dicSub2

        Set dicSub2 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/elem", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 7) 支承条件（起始端铰支，末端滚动支承）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

    dicSub3.Add "ID", 1
    dicSub3.Add "CONSTRAINT", "1111000"
    dicSub2.Add "ITEMS", Array(dicSub3)
    dicSub1.Add modelID(3, 1), dicSub2

    Set dicSub2 = Nothing: Set dicSub3 = Nothing
    Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

    dicSub3.Add "ID", 1
    dicSub3.Add "CONSTRAINT", "0111000"
    dicSub2.Add "ITEMS", Array(dicSub3)
    dicSub1.Add modelID(3, 1) + num_division, dicSub2

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/cons", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing: Set dicSub3 = Nothing

    ' 8) 荷载工况（自重用 DL，附加荷载用 SIDL — loadCase 工作表区域 2 行）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To loadCase.Rows.Count - 1
        Set dicSub2 = New Dictionary

        dicSub2.Add "NAME", loadCase(i + 1, 2)
        dicSub2.Add "TYPE", "USER"

        dicSub1.Add i + 1, dicSub2

        Set dicSub2 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/stld", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 9) 自重（在第 1 行荷载工况上 -Z 方向 1 倍）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary

    dicSub2.Add "LCNAME", loadCase(1, 2)
    dicSub2.Add "FV", Array(0, 0, -1)
    dicSub1.Add "1", dicSub2

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/bodf", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing

    ' 10) 均布梁单元荷载（第 2 行荷载工况，应用于所有单元）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary

    For i = 0 To num_division - 1
        Set dicSub2 = New Dictionary: Set dicSub3 = New Dictionary

        dicSub3.Add "ID", 1
        dicSub3.Add "LCNAME", loadCase(2, 2)
        dicSub3.Add "CMD", "BEAM"
        dicSub3.Add "TYPE", "UNILOAD"
        dicSub3.Add "DIRECTION", direction
        dicSub3.Add "D", Array(0, 1)
        dicSub3.Add "P", Array(loadValue, loadValue)

        dicSub2.Add "ITEMS", Array(dicSub3)
        dicSub1.Add modelID(4, 1) + i, dicSub2

        Set dicSub2 = Nothing: Set dicSub3 = Nothing
    Next i

    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/bmld", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing

    ' 11) 荷载组合（原样使用 loadCase 工作表区域的系数·LC 名称）
    Set dicMain = New Dictionary: Set dicSub1 = New Dictionary
    Set dicSub2 = New Dictionary

    Dim vCOMB() As Object
    ReDim vCOMB(loadCase.Rows.Count - 1)

    For i = 0 To loadCase.Rows.Count - 1
        Set dicSub3 = New Dictionary

        dicSub3.Add "ANAL", "ST"
        dicSub3.Add "LCNAME", loadCase(i + 1, 2)
        dicSub3.Add "FACTOR", loadCase(i + 1, 1)

        Set vCOMB(i) = dicSub3

        Set dicSub3 = Nothing
    Next i

    dicSub2.Add "NAME", "Comb1"
    dicSub2.Add "ACTIVE", "ACTIVE"
    dicSub2.Add "iTYPE", 0
    dicSub2.Add "vCOMB", vCOMB

    dicSub1.Add "1", dicSub2
    dicMain.Add "Assign", dicSub1

    body = JsonConverter.ConvertToJson(dicMain)
    response = WebRequest("POST", "/db/lcom-gen", body)
    Debug.Print response

    Set dicMain = Nothing: Set dicSub1 = Nothing
    Set dicSub2 = Nothing

    ' 12) 保存
    response = WebRequest("POST", "/doc/save", "{}")
    Debug.Print response

    MsgBox "完成！请在 MIDAS NX 界面中确认简支梁与荷载组合。"

End Sub
