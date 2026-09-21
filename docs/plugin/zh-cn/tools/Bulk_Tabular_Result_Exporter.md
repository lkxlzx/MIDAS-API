# Bulk Tabular Result Exporter

> **原文：** [Bulk Tabular Result Exporter](https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter)
> **原文创建：** 2026-08-06 · **原文最后编辑：** 2026-08-06

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Bulk_Tabular_Result_Exporter.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

在桥梁模型中，若要跨多个荷载组合·施工阶段提取前处理数据（节点·单元·截面）与后处理分析结果（反力、构件内力、位移、应力等），通常得逐张表格进行选择、设置并手工导出，然后再拼装成一个工作簿。本 Plug-in 把这一过程压缩为单一操作：将所需的全部表格一次性定义为 Job，针对实际模型预览后，一次写入结构化 Excel 文件中的各个工作表。整套选择配置还可保存为预设，供下一个模型·下一个修订版本复用。

## 支持版本

`MIDAS CIVIL NX 2026 (v1.1.0)`

## 主要功能

- **One workbook, every table** — 前处理模型数据与后处理结果可一并导出。每个 Job 写入名称清晰的独立工作表，**Contents & Export Log** 表则记录请求与返回明细。
- **Complete table coverage** — 可访问 100 个以上的引导式（guided）模型数据端点以及全部内置结果表格。借助 **Any DB Table**·**Any Result Table** 模式，连引导清单中没有的表格也可访问。
- **Model-aware selection** — Structure Group、施工阶段、分析步骤标签均直接从关联的模型读取并作为筛选项提供（并非手工输入）。
- **Report-ready output** — 列头包含单位、表头样式化、列宽自动调整、应用 AutoFilter，数值保持数字格式，ID 以文本形式保留。
- **Repeatable workflow** — 整套表格选择配置可保存为预设，在后续会话·修改后的模型·下一个项目中一次性还原。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 1 | 选择表格来源 — 在 **Pre-processing**（模型数据）/ **Post-processing**（分析结果）之间切换 |
| 2 | 添加 Table Job — 在目录中检索并选择后添加。每个 Job 对应一张工作表，可按需添加任意多个 |
| 3 | 设置 Job — 仅选择所需的结果分量，按节点/单元 ID·数值范围·Structure Group 过滤，用 MIDAS 后缀输入荷载工况·荷载组合 |
| 4 | （需要时）设置施工阶段 — 读取模型中保存的施工阶段，选择要导出的确切步骤 |
| 5 | 设置单位·精度 — 按 Job 指定力的单位、长度单位、数值格式、小数位数 |
| 6 | Preview — 在生成工作簿前与实际模型对照，确认将要返回的列与数据 |
| 7 | Export all to Excel — 提取所有已启用的 Job 并写入一个工作簿。即使有 Job 失败，其余成功的 Job 仍予保留，失败信息记入 Export Log |
| 8 | 保存预设 — 将整套选择配置保存为 `.mrxpreset.json` 文件，供此后复用 |

## 参考/限制事项

正如 Plug-in 自身所述，它并非包装某个特定端点的工具，而是可访问“100 个以上引导式模型数据端点 + 全部内置结果表格”的**通用批量导出工具**。

## 相关 JSON API 端点

不向某个特定端点收窄地给出链接 —— 原文自我声明其为“前处理（`/db/*`）+ 后处理（`/post/*`）整体覆盖的通用工具”，只链接单个端点反而会引起范围上的误解。实际对应的对象是 `docs/manual/` 全部内容。

## 结论（原文）

每次模型改版时，报表工作中繁琐且易错的部分 —— 重复选择同样的表格、输入同样的筛选、合并同样的电子表格 —— 都由本 Plug-in 消除。工作簿只需定义一次并针对模型预览，此后每当分析发生变化，几秒即可重新生成。工程师的时间因此用于解读结果，而不是收集结果。

## 原文链接

[https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter](https://support.midasuser.com/hc/ko/articles/60848073556633-Bulk-Tabular-Result-Exporter)
