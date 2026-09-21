# Load Combination Contribution Analyzer

> **原文：** [Load Combination Contribution Analyzer](https://support.midasuser.com/hc/ko/articles/61258768334233-Load-Combination-Contribution-Analyzer)
> **原文撰写：** 2026-08-18 · **原文最后编辑：** 2026-08-18

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Load_Combination_Contribution_Analyzer.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

组合（combination）结果给出了答案，却没有说明答案从何而来。当主梁弯矩由一个包含8个荷载
工况的组合控制时，计算书中真正关键的问题是：哪个工况贡献了结果的哪一部分 — 设计究竟由
交通envelope控制还是由温度项控制，以及各占多少。

若要手工作答，就得把各组成工况全部重新运行一遍、整理成表、施加系数，再核对算术是否闭合。
**Load Combination Contribution Analyzer**直接完成这一计算 — 从模型中读取组合，把嵌套的
子组合全部展开，随后在所有输出位置计算每个组成荷载工况的带符号贡献值（signed
contribution），再把这些贡献值重新累加并与CIVIL NX实际上报的值对照校验，之后才显示结果。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.0.0)`

## 主要功能

- **非抽样而是全部位置：** 将Beam·Truss·Plate·Plane Stress·Plane Strain·Axisymmetric·
  Solid·Link结果按单元·部位（part）·成分（component）为单位，在局部轴与全局轴两个方向
  受支持的范围内全部分解。
- **每次都与CIVIL NX对照校验：** 将各分解结果重新累加，在同一请求批次内与模型针对同一
  组合·同一位置实际上报的值比较 — 若出现超出容差的偏差则中止运行，且没有可将其关闭的选项。
- **请求全精度而非显示精度：** 结果按9位有效数字请求，而非模型的显示格式（力为小数点后
  2位）— 在由8个项构成的真实组合中，重新累加误差须从5e-3降到1.4e-7，自校验才有意义。
- **正确解析嵌套组合：** 对可经多条路径到达的荷载工况，有效系数按各路径系数乘积之和计算
  而非单次查询 — 既被直接包含又同时位于子组合内的工况只被反映一次，并且准确。
- **Envelope按选择处理，不作为占比处理：** 对每个单元·部位·成分·符号分别判定控制工况
  （governing case），并按结果项逐条报告 — 由于它沿构件走向确实会变化，因此不做平均、
  不做笼统合并。
- **与MIDAS一致的筛选基准：** 可按结构组·边界组·截面·厚度·材料·单元类型进行筛选，
  各项均同时显示单元数量；按基准记住勾选状态并加以组合，直接输入的单元编号在其上以
  并集方式追加。
- **不可能的情形直接拒绝而不猜测：** 非线性·屈曲分析（pushover）、徐变·干燥收缩、
  预应力束一次·二次效应、时程结果，以及von Mises·主应力等派生量对荷载工况不具线性，
  因此连同理由一并明确拒绝。
- **面向计算书的输出：** 支持浅色/深色主题、位数对齐的数字显示，以及贡献度与控制工况图
  （governing map）的CSV导出。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在CIVIL NX中打开已完成分析的模型并运行Plug-in — 一旦MAPI Key校验通过，即开始加载组合·单元·选择集·施工阶段列表 |
| 2 | 在**Combination**中选择组合 — 显示模型中定义的全部LCOM表项，并在下方**Combination tree**中确认其如何展开、是否为envelope值（max/min成对） |
| 3 | 选择结果表 — 在Beam·Truss·Plate·Plane Stress·Plane Strain·Axisymmetric·Solid·Link中选择力或应力、局部轴或全局轴。随所选内容自动过滤单元类型·显示成分·可选单元 |
| 4 | 在**Select elements by**中按结构组·边界组·截面·厚度·材料·单元类型选择集 — 所选结果表无法处理的类型的集成员不会被静默遗漏，而是跳过并以数量显示 |
| 5 | 必要时在**Elements**中按`700-760, 1200, 1310-1315`这样的范围追加输入单个单元编号（以并集方式加到已勾选的集上） |
| 6 | 勾选待分解的成分 — 列表随所选结果表而变化，并已预选合理的默认值 |
| 7 | 仅在施工阶段结果时以`CS3:002(last)`格式输入**Stage:step**（施工后阶段结果留空）— 阶段不匹配时不做任意推测而直接拒绝 |
| 8 | 执行**Run decomposition** — 针对单元范围以尽量少的请求批量处理所有组成工况，并在结果显示之前先完成自校验 |
| 9 | 在**Results**标签中用Element·Part·Component·Sense筛选器选择位置 — 查看各工况的系数·原始结果值·带符号贡献值·占总量（gross）比例·占净值（net）比例，以及net·gross·抵消率（cancellation ratio）·CIVIL NX上报值 |
| 10 | 在**Charts**标签中以共享0轴的带符号柱状图，或以gross占比为基准的饼图查看同一结果（抵消较大时，饼图按相对影响而非比例表示） |
| 11 | 对于envelope组合，打开**Governing map**确认按单元·部位·成分·符号的控制工况 |
| 12 | 在**Results**或**Governing map**标签中导出CSV — 同时包含单位、API返回的精度与组合树信息，因此单独看表也能解读 |

## 参考/限制事项

- 非线性·屈曲分析（pushover）、徐变·干燥收缩、预应力束一次/二次效应、时程结果，
  以及von Mises·主应力等派生量对荷载工况不具线性，因此拒绝分解。
- 若重新累加的结果与CIVIL NX上报值之间的偏差超出容差，则不显示结果并中止运行，
  且不存在绕过该检查的选项。
- 查询施工阶段结果时，若`Stage:step`格式不匹配，不做任意推测而直接拒绝。

## 相关JSON API Endpoint

Plug-in读取组合结构所使用的Endpoint，看起来与`docs/manual`中的下列条目对应。
但结果分解实际使用的按单元类型的结果表Endpoint（Beam/Plate/Solid等存在多个候选）
原文未指明，因此未凭推测添加链接。

- [`/db/LCOM-GEN` — Load Combinations – General](../../../manual/zh-cn/13_DB_Load_Combinations.md) *（推测为组合树查询，结果分解Endpoint未确认）*

## 结论（原文）

Load Combination Contribution Analyzer回答了仅凭组合结果无法回答的问题 — 究竟哪个荷载
工况实际控制设计、控制到什么程度。它取消了人工重跑与表格整理，按CIVIL NX实际的处理方式
展开嵌套组合与envelope；在会产生无意义贡献值的情形下，拒绝输出而非直接打印数值。
显示的每一个数字都先由自身组成部分重构，并与模型对照校验之后才出现 —
这正是该结果可以写入计算书的原因。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/61258768334233-Load-Combination-Contribution-Analyzer](https://support.midasuser.com/hc/ko/articles/61258768334233-Load-Combination-Contribution-Analyzer)
