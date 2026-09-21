# Introduction to MIDAS Plug-in

> **原文：** [Introduction to MIDAS Plug-in](https://support.midasuser.com/hc/en-us/articles/35693347852569-Introduction-to-MIDAS-Plug-in)
> **原文创建：** 2024-07-30 · **原文最后编辑：** 2024-11-27

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../guide/01_Introduction.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## MIDAS Plug-in 是什么

MIDAS API 因术语与概念陌生，可能存在一定的入门门槛。为降低这一门槛，MIDAS 同时提供了**可直接使用的 API 应用**——**MIDAS Plug-in**。Civil NX 用户即使不懂 API 或编程语言，也能发挥 MIDAS API 的能力。

此前 Civil 用户在建模过程中，为了重复计算·数据转输一直并行使用 CAD 与 Excel。Plug-in 减少了这类重复作业与数据转输过程。MIDAS API 是基于 Web 的 API，扩展可能性很大 — JSON（数据格式）在绝大多数与 Web 兼容的语言中都可处理，Python 则拥有丰富的数学函数，可用于几何计算等。**MIDAS API + Python 数学函数**的组合，正是强大的"MIDAS Plug-in"。

最基本的例子：想用生成 API 创建 20 个节点时，a) 逐个硬编码坐标，或 b) 使用 Python 的 for 循环。在大学结构课程中用过 VBA 或 MATLAB 的 for 循环的工程师，会对这种方式很熟悉。

## MIDAS Plug-in的优势

### a) 更快的模型创建·修改

其设计让没有 API 概念或编程背景的用户也能无门槛地体验 API。为有编码经验的用户，同时提供了可自行开发的高级环境。首次发布时推出了 12 个从用户想法出发的 Plug-in。

### b) 实时更新

在基于 Web 的 Plug-in 环境中，Civil NX 的更新会立即反映。无需等待产品正式发布，仅刷新页面即可立即使用最新的 Plug-in。这也使用户能够自行开发·集成针对新设计标准的 Plug-in — 例如为新西兰新抗震荷载标准制作的 Design Response Spectrum Generator Plug-in，就是产品在正式纳入该标准之前，用户即可把新标准应用于设计的案例。

### c) 工作流定制

想使用 API 的人大多是为了减少重复作业，或通过重复计算自动优化模型 — 即希望实现工作流自动化。Plug-in 填补用户需求与软件功能之间的空白，使工作流自动化·简化，并可以补入基础软件起初不支持的功能。

例如 Alignment Creator Plug-in 自动生成节点·单元·节点局部轴，简化项目初期作业；Concrete Material Set Plug-in 简化了具有时间相关材料特性的材料组创建。除此之外，桥墩·墩帽·桩·桩基础等结构构件的生成、温度梯度引起的残余应力计算、预应力束坐标的相对·绝对坐标转换等复杂数据作业也由 Plug-in 代为处理，大幅减少工作量。

## 结论

将 Plug-in 用于 Civil NX 工作流，已超越单纯的便利功能，是随工程师与设计者不断变化的需求而演进的变革性工具。由此用户可提升效率·生产性，并为积极协作的专家社区作出贡献。
