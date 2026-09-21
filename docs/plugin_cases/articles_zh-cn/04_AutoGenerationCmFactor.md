# AutoGenerationCmFactor

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60729138404761-AutoGenerationCmFactor
- 视频：[04_AutoGenerationCmFactor.mp4](../videos/04_AutoGenerationCmFactor.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Auto%20Generation%20Cm%20Factor_%EC%A0%9C%EB%A1%9C.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/04_AutoGenerationCmFactor.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本插件自动计算 MIDAS GEN NX 生成荷载组合时地震作用所需的 Cm Factor（修正系数）。

## 主要功能

**01. 确定地震作用修正系数**
自动计算 MIDAS GEN NX 生成荷载组合时地震作用所需的 Cm Factor（修正系数）。

**02. 自动输入**
可一次性读取建模中已输入的、确定修正系数所需的各项数值。

**03. 套用 KDS 41 17 00 第 4.2.2 条规定**
自动判断并套用以下两项规定：(2) 当基岩深度超过 20m 且地基平均剪切波速达 360m/s 以上时，套用表 4.2-2
规定的 Fv 值的 80%；(3) 当地基分类为 S5 且基岩深度不明时，套用表 4.2-1 与表 4.2-2 规定的 Fa 和 Fv
值的 110%。

**04. 输出地震作用修正系数计算书**
提供修正系数确定依据计算书的输出功能，说明该系数是基于哪些数据计算而得。
