# CS454 Load Assessment Combinations

> **原文：** [CS454 Load Assessment Combinations](https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations)
> **原文创建：** 2026-08-10 · **原文最后编辑：** 2026-08-10

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/CS454_Load_Assessment_Combinations.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

CS 454 Assessment Combination 定义简单，实际配置却很耗时。Table A.1 对承载能力极限状态（ULS）·正常使用极限状态（SLS）的 4 个组合，为每一项作用（action）指定各自的分项系数，并要求按该作用属不利（adverse）还是有利（relieving）再取不同数值。

可变荷载（live load）模型须保持相互排斥，以免正常交通（normal-traffic）工况与其替代者特殊车辆（abnormal vehicle）工况出现在同一组合中；所有永久作用（permanent action）都要按有利·不利两个方向各取一遍；且每当增加荷载工况或改变系数，就得重新生成整套 —— 这些都是在 Load Combinations 表中手工录入之前必须先处理完的工作。

**CS 454 Load Assessment Combinations** Plug-in 把这一过程压缩为一次定义：从关联的模型读取荷载工况，将各自映射到 Table A.1 的作用，应用用户确认的系数，并通过一次确认步骤把整套组合及其 envelope 写入 CIVIL NX。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.0.1)`

## 主要功能

- **完全照搬 Table A.1：** 所有组合均严格遵循 CS 454 version 1.1.0、Appendix A、Table A.1 —— 逐项作用的有利/不利 γ<sub>fL</sub>、铸铁（cast iron）结构专用系数组，以及 γ<sub>f3</sub> 是计入组合系数还是留作抗力验算，均有反映。
- **从模型映射，无需重复输入：** 从关联的模型读取静力·施工阶段·沉降·移动荷载工况，分别映射到 CS 454 的作用；移动荷载还进一步指定到荷载模型（ALL Model 1·2、SV、SOV、STGO、SO、HB 以及相关的正常交通·人行道荷载）。未映射的工况不会被悄然按默认值处理，而是直接阻止组合生成；且 Prestress 属 CS 455 范畴，根本不允许映射。
- **精确处理可变荷载的互斥性：** 可按类别指定共同作用/独立/互斥，故正常交通工况不会与其替代者的特殊车辆进入同一组合；对无法用类别规则表达的情形，还可设置跨类别的排除（exclude）/要求（require）。
- **永久作用双向自动生成：** 设为 both 的永久荷载组会同时生成有利与不利两侧，全部排列组合无需手工完成。
- **在规范允许的范围内缩减组合数量：** 把互斥组归并为一个 Envelope 子组合、令其按 Table A.1 系数引用，从而减少实际登记到模型中的行数。
- **以英文呈现可读名称：** 不用压缩代码，而按 `ULS2-ALL1s-W2-Adv` 形式写入，极限状态·组合编号·可变荷载模型·风荷载子工况·永久作用变体在 MIDAS 表格中可直接读出；description 中也把同样内容用完整语句写明。
- **写入前校验：** Preview 以完整台账（ledger）形式列出所有组合的组成要素·算式·每一项的生成条款与系数；在 commit 确认之前，模型中不会反映任何内容。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 在 CIVIL NX 中打开目标模型并运行 Plug-in。连接信息自动填入，若状态徽标不是 **CIVIL NX connected** 则使用 **Connection** |
| 2 | **Read Model Validation** — 在生成前报告结构类型与模型的荷载工况。铸铁（cast iron）结构按 Section 8 以容许应力准则评估，故切换到专用系数列并禁用 SLS 范围。圬工拱（masonry arch）不在本次版本范围内 |
| 3 | 在 **Load Cases & Mapping** 中为所有已启用的工况指定 CS 454 Table A.1 的作用，并为所有移动荷载工况指定 CS 454 荷载模型与评估等级。若 MIDAS 中设置了 **Auto Live Load Combination**，则“仅 ULS/仅 SLS”的限制会被自动识别并报告，因此 SLS 车辆不会误反映到 ULS 组合中 |
| 4 | 在 **Combinations Scope** 中勾选所需的 1~4 号组合与极限状态 — 仅生成被勾选的项 |
| 5 | 确认系数 — 显示完整的 Table A.1，可按作用修改不利/有利 γ<sub>fL</sub> 以适配评估，并设置 γ<sub>f3</sub> 是计入组合系数还是留作抗力验算 |
| 6 | 在 **Groups & Relations** 中按类别构建分组或套用模板，设置类别动作（共同/独立/互斥）、是否允许某类别完全缺省、互斥组是否归并为 Envelope 子组合。可增补跨类别的排除/要求，并将永久荷载组设为不利/有利/双向 |
| 7 | 复核 **Preview** — 列出生成的所有组合及其名称·系列·可变荷载模型·组成要素数·警告；单独选择某一组合时，可查看算式及每一项所依据的 Table A.1 行与系数，即完整台账 |
| 8 | **Commit** — 选择目标表格、决定既有 Load Combinations 的处理方式、名称冲突时添加前缀、勾选是否按系列记录 Envelope。通过发送前的摘要确认实际将被写入的内容 |

## 参考/限制事项

- 铸铁（Cast iron）结构按 Section 8 转为容许应力准则评估，且 SLS 范围被禁用。
- 圬工拱（Masonry arch）本次版本不支持。
- Prestress 荷载工况被视为 CS 455 范畴，映射本身即被拒绝。
- 若存在未映射的荷载工况，不会按默认值悄然处理，而是阻断组合生成。

## 相关 JSON API 端点

Plug-in 最终写入 CIVIL NX 的荷载组合，与 `docs/manual` 中的以下端点对应。

- [`/db/LCOM-GEN` — Load Combinations – General](../../../manual/zh-cn/13_DB_Load_Combinations.md)

## 结论（原文）

CS 454 Load Assessment Combinations Plug-in 消除了 DMRB 评估中最缓慢、最易出错的环节 —— 就 4 个组合·2 个极限状态逐项翻阅 Table A.1、维持可变荷载模型的互斥性、把每个永久荷载按双向各取一遍、再把结果手工录入。映射只需定义一次并经 Preview 确认，此后每当荷载工况·系数·范围发生变化，几秒即可重新生成整套，使工程师的时间用于评估本身，而非整理台账。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations](https://support.midasuser.com/hc/ko/articles/60997850893209-CS454-Load-Assessment-Combinations)
