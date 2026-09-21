# Iterative Response Spectrum

> **原文：** [Iterative Response Spectrum](https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum)
> **原文撰写：** 2025-09-24 · **原文最后编辑：** 2025-10-14

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Iterative_Response_Spectrum.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

使工程师在考虑地基非线性的同时仍能执行反应谱（Response Spectrum）线性分析的Plug-in。
在MIDAS Civil NX中自动化反应谱分析的迭代刚度更新。处理点弹簧（point spring）并提取
位移结果，反复更新刚度直至收敛。用户可以跟踪整个迭代（iteration）过程中的刚度变化，
并高效地比较各次结果。

## 支持版本

`MIDAS CIVIL NX 2025 (v2.1) US`

## 主要功能

自动化迭代反应谱分析过程：基于位移结果更新弹簧刚度直至收敛。无需手工调整刚度并重跑
分析，因此大幅节省时间并减少错误。刚度变化可轻松跟踪，全部结果均可导出为Excel。
对MIDAS Civil NX中的非线性土-结构相互作用（soil-structure interaction）算例尤其有用。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 创建空边界组（Empty Boundary Group） |
| 2 | 单击**Connect** → 打开Marketplace并运行Iterative Response Spectrum Plug-in |
| 3 | 选择Empty Boundary Group、Response Spectrum case与Tolerance值，然后单击**Run Analysis** |
| 4 | 分析收敛后，可以Excel格式下载所有迭代（iteration）的结果 |

## 参考/限制事项 — Plug-in所考虑的假定

1. **Force-deformation Function：** 视为关于正（+）/负（-）方向对称。例：定义在+Dx/-Dx
   方向的弹簧将转换为+Dx。F-D函数中不得出现负（negative）斜率。
2. **线性弹簧刚度：** 若某一节点仅在一个方向上存在多线性（multi-linear）弹簧定义，
   则第一次迭代之后，其他方向会被施加最小刚度（仅对平动自由度为0.001）。
3. **恒定强度（Uniform capacity）：** 当变形超过Force-deformation Function中定义的范围时，
   ITR脚本会把最后定义点的力保持恒定，一直延续到新获得的变形处。
4. **节点局部轴：** 若多线性弹簧定义中已定义节点局部轴，则割线（secant）刚度计算采用
   节点局部位移；若未定义，则采用全局节点位移。
5. **施工阶段（CS）：** 若未定义施工阶段，则所有含多线性定义的节点都成为ITR脚本的
   迭代对象。若已定义施工阶段，则查看最后施工阶段中激活的边界组，并在其中识别带有
   线性/多线性点弹簧的节点作为迭代对象。属于`Default`选项/组的边界参数在本Plug-in中
   不予考虑。
6. **Tolerance：** 以比率形式输入（例：`0.05` = 5%）。对全部平动自由度（局部/全局）
   进行检查，比较相对上一次迭代的节点位移。例：Tolerance为0.01、上次位移为5、新位移为
   6时，`(6-5)/5 = 0.2 > 0.01`，因此Plug-in会对新位移插值求力并计算刚度，然后重新执行分析。

## 相关JSON API Endpoint

Plug-in所处理的边界组与反应谱荷载工况，与`docs/manual`中的下列Endpoint对应。
但点弹簧本身对应哪个Endpoint（`/db/NSPR`、`/db/GSPR`等）原文并未指明，因此未添加链接。

- [`/db/BNGR` — Boundary Group](../../../manual/zh-cn/02_DB_Project_Structure.md)
- [`/db/SPLC` — Response Spectrum Load Cases](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)

## 结论（原文）

Iterative Response Spectrum Plug-in通过自动化直至收敛的刚度更新，简化了非线性反应谱
分析。用户以极少的输入即可完成准确的地基-结构相互作用分析，从而减少人工操作并提高
可靠性。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum](https://support.midasuser.com/hc/en-us/articles/50959239482393-Iterative-Response-Spectrum)
