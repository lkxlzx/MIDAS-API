# Skew Grillage Geometry Generator

> **原文：** [Skew Grillage Geometry Generator](https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator)
> **原文编写：** 2026-08-06 · **原文最后编辑：** 2026-08-06

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Skew_Grillage_Geometry_Generator.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

斜交（skew）梁格（grillage）说起来简单，做起来繁琐：支承线沿桥面宽度方向在跨径上错开，所有纵向主梁都必须在各横向构件位置处分割，端部横梁必须与每根主梁相交，节点、单元编号在整个过程中必须保持一致。而且每当斜交角、跨径、主梁数变化时都要重复这套操作。

本 Plug-in 用一个参数化定义即可完成该过程。输入跨径、桥面宽度、主梁数、横向间距、斜交角后，可通过同时显示节点、单元数量的实时正交（orthographic）预览查看整个梁格；确认后即可一次性写入 CIVIL NX 模型，生成相互连接的节点与梁单元。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.0.2)`

## 主要功能

- **Parametric from end to end** — 修改斜交角、跨径、桥面宽度、主梁数、横向间距时，包含横向构件布置、端部列、斜交边界梁在内的整个梁格会立即重新生成。
- **Seen before it is built** — 以平面视图打开的正交 3D 预览会随输入变化实时显示节点、单元数量、主梁间距、典型开间（bay）间距、支承端偏移，从而在写入模型之前发现错误。
- **Correct connectivity** — 在每个横向构件交点处分割纵向主梁，形成实际结构相连的梁格，而非仅相交未连接的梁。若所选间距无法整除跨径，最后一个开间会自动缩小。
- **Two cross-member conventions** — 支持两种横向构件布置方式：沿斜交支承线布置，或垂直于主梁布置。垂直方式下会自动生成端部横梁，使所有主梁在两侧支承点处相连。
- **Tidied before committing** — 可在预览中测量任意两个节点之间的实际距离；对间距过窄的横向列，可通过删除重复节点并重新连接主梁的方式进行合并。
- **Safe on a live model** — 检查起始节点、单元 ID 是否存在冲突，若已有模型则在替换前给出警告；缺失的材料、截面按模型的单位制自动生成；单元写入失败时回滚新生成的节点。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 CIVIL NX 中打开新模型并运行 Plug-in — 连接信息自动提供，若状态徽章不是 "CIVIL NX connected" 则使用 **Connection** |
| 2 | 输入桥面几何 — 跨径（所有主梁两支承线之间的距离）、桥面宽度、纵向主梁数、横向间距 |
| 3 | 设置斜交角 — 滑杆或直接输入，范围 **-60°~+60°**。`0°` 表示垂直于主梁，正值将 `+Y` 支承端向 `+X` 方向移动 |
| 4 | 选择横向构件方向 — **Parallel to skew**（所有横向构件沿支承线）/ **Perpendicular to girders**（跨越主梁的共同重叠区段，并在各支承点自动添加端部横梁） |
| 5 | 设置 Model origin — 用 Origin X/Y/Z 将桥面中心线起点布置到 CIVIL NX 全局坐标系中（默认值 0，属纯平移，因此几何指标不变） |
| 6 | 设置 Model assignment — 输入材料 ID、纵向/横向截面 ID、首个节点 ID、首个单元 ID。保持勾选 **Create missing default properties** 时，缺失的材料、截面按模型当前单位制自动生成 |
| 7 | 确认预览 — 默认为平面视图，选择 **3D** 或拖拽旋转、滚轮缩放，用 **Reset view** 返回平面视图。可用 **Measure** 查看任意两节点间的 3D 距离与坐标差，用 **Merge beams** 去除重复横向列并重新连接主梁 |
| 8 | Create Geometry — 核对将要新增的节点、单元摘要后确认。模型中已有节点、单元时，会显示既有数量的二次警告 |
| 9 | （必要时）Download API payload — 将生成的节点、单元数据保存为 JSON 文件，以便检查、复用 |

## 参考/限制事项

- 斜交角输入范围限制为 -60°~+60°。
- 修改 Model origin 属纯平移，因此不影响报告的几何指标（主梁间距、开间间距等）。

## 相关 JSON API 端点

Plug-in 生成的节点、梁单元、材料、截面与 `docs/manual` 中的以下端点对应。

- [`/db/NODE` — Node](../../../manual/zh-cn/03_DB_Node_Element.md#1-dbnode)
- [`/db/ELEM` — Element](../../../manual/zh-cn/03_DB_Node_Element.md#2-dbelem) *（梁单元）*
- [`/db/MATL` — Material Properties](../../../manual/zh-cn/04_DB_Properties.md#1-dbmatl) *（缺失时自动生成）*
- [`/db/SECT` — Section Properties](../../../manual/zh-cn/04_DB_Properties.md#12-dbsect) *（缺失时自动生成）*

## 结论（原文）

本 Plug-in 消除了梁格建模中耗时且易错的环节 — 手动计算斜交偏移、在每个横向构件处分割主梁、每当参数变化后重新编排模型编号。桥面只需定义一次并经预览校验，此后每当斜交角、跨径、主梁布置改变时都可在数秒内重新生成。工程师可将时间用于分析，而不是几何生成。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator](https://support.midasuser.com/hc/ko/articles/60848423734169-Skew-Grillage-Geometry-Generator)
