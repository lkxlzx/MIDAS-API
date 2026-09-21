# Inertial Forces Controller

> **原文：** [Inertial Forces Controller](https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller)
> **原文撰写：** 2024-12-03 · **原文最后编辑：** 2025-08-01

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../tools/Inertial_Forces_Controller.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

## 概述

自动转换作用于曲线桥桥墩的惯性力（inertial force）方向的Plug-in。
在曲线桥上施加惯性力时，无需逐个桥墩手工计算并输入荷载方向。以全局坐标系或自定义角度
为基准，把水平惯性力转换并施加到各桥墩最接近的方向上。对桥墩与全局坐标系错位的复杂
桥梁线形建模尤其有用，可简化地震分析工作流。

## 支持版本

`MIDAS CIVIL NX 2024 (v1.1) US`

## 主要功能

在MIDAS CIVIL中为曲线桥桥墩施加惯性力时，传统做法需要逐个桥墩手工计算并输入荷载方向，
既耗时又易出错。本Plug-in只需输入一个或多个旋转角，即自动生成对应的荷载工况。无需人工
转换与重复输入即可简化过程，既节省时间又保证准确性。

## 使用方法

| 步骤 | 说明 |
| --- | --- |
| 选择Time History Load Cases | 显示分析方法（Analysis Method）设置为"Static"的时程荷载工况列表 |
| 选择Static Load | 仅显示已指定"Nodal Body Force"与"Nodal Loads"的工况 |
| 选择Time History Functions | 显示产品设置中Time Forcing Functions Data以"Normal"类型构成的函数。默认同时提供"Linear"函数（Preset: Linear） |
| 输入Scale Factor（④） | 输入时程函数的倍率（scale factor） |
| 输入水平荷载角度（⑥） | X轴绕全局坐标系Z轴的旋转角，与地面加速度水平分量方向对齐。可输入正的实数，并可用"+"按钮（⑤）定义多个旋转角 |
| Create（⑦） | 单击后新建已添加节点体积力（nodal body force）的静力荷载工况、时程荷载工况、时程函数与时变静力荷载 |

> ⚠️ **注意（原文）：** Scale Factor（④）必须大于0。各角度（⑥）之间不得定义为相同的值。

新增的nodal body force按"Static Load名称_角度deg"（角度以度（degree）为单位，以"Static
Load"设置为基准）的形式生成。原有已输入的nodal body force荷载按荷载角度进行坐标转换。

## 参考/限制事项

坐标转换计算（Coordinate-transformation Calculation）示例：若按30度方向生成，则会自动
生成由原静力荷载坐标转换而来的静力荷载工况。

## 相关JSON API Endpoint

Plug-in明确说明会生成的数据，与`docs/manual`中的下列Endpoint对应。

- [`/db/STLD` — Static Load Cases](../../../manual/zh-cn/06_DB_Static_Loads.md)
- [`/db/NBOF` — Nodal Body Force](../../../manual/zh-cn/06_DB_Static_Loads.md)
- [`/db/THIS` — Time History Load Cases](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)
- [`/db/THFC` — Time History Functions](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)
- [`/db/THSL` — Time Varying Static Loads](../../../manual/zh-cn/09_DB_Dynamic_Loads.md)

## 结论（原文）

Inertial Forces Controller Plug-in以brace数量为基准，自动转换所应施加的惯性力的荷载方向，
为用户节省时间并消除潜在的人为失误。用户只需输入以全局坐标系Z轴为基准的水平方向，
即可轻松控制惯性力。

## 原文链接

[https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller](https://support.midasuser.com/hc/en-us/articles/40706127836953-Inertial-Forces-Controller)
