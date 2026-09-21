# Series Load

> **原文：** [Series Load](https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load)
> **原文编写：** 2025-04-09 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Series_Load.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

Series Load Plug-in 将 MIDAS CIVIL NX 中连续结构物按一定间距施加自定义静力梁荷载（集中荷载、分布荷载、离心荷载）的过程自动化。它简化了在曲线或样条（spline）排列的单元上重复定义荷载的过程，适用于桥梁或圆形结构物。

### 主要特点（原文）

- 将静力荷载组合作为活荷载（live load）施加。
- 支持方向由节点样条几何决定的离心力（centrifugal force）。
- 与从 i 节点开始的连续结构物兼容。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

- **高效性：** 消除跨越长跨径的重复荷载手动输入。
- **精确性：** 自动计算垂直于样条切线的离心力方向。
- **灵活性：** 与集中荷载、分布荷载、离心荷载共同工作。
- **高级样条选项：** 为获得平滑的荷载排列，采用 Monotone Cubic Hermite Spline（推荐）。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 输入 Vertical Loads | 作用于梁的集中荷载 |
| 输入 Distributed Loads | 作用于梁的分布荷载 |
| 输入 Impact Loads | 竖向荷载的冲击系数（magnification factor） |
| 输入 Centrifugal Loads | 与竖向荷载一同施加 |
| 选择 Beam Geometry | — |
| 选择·输入通用设置 | 选择预设荷载，并以各工况之间的距离确定静力荷载工况数量 |
| 输入 Load Points Setting | 荷载点设置（集中荷载间距） |
| 输入·选择控制面板 | 确认静力荷载生成选项 |
| 应用 | 完成上述全部输入后选择要施加的单元，点击 **APPLY SERIES LOADS** |
| 确认 | 查看生成的静力荷载工况 |

## 参考/限制事项

- **仅限连续结构物：** 无法在不连续（disjointed）的单元上施加荷载。
- **依赖样条：** 离心力方向由相连节点样条的切线导出。
- **输入校验：** 所有荷载的大小必须大于 0。

## 相关 JSON API 端点

Plug-in 生成的荷载与 `docs/manual` 中的以下端点对应。

- [`/db/STLD` — Static Load Cases](../../../manual/zh-cn/06_DB_Static_Loads.md)
- [`/db/BMLD` — Beam Loads](../../../manual/zh-cn/06_DB_Static_Loads.md)

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load](https://support.midasuser.com/hc/en-us/articles/45545604010521-Series-Load)
