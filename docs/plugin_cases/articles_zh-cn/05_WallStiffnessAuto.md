# WallStiffnessAuto

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60729084287897-WallStiffnessAuto
- 视频：[05_WallStiffnessAuto.mp4](../videos/05_WallStiffnessAuto.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/WallStiffnessAuto_%EB%AF%BC%EC%84%B1.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/05_WallStiffnessAuto.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

WallStiffnessAuto 通过 GEN NX API 直接查询 RC 墙体设计（KDS-41-20-2022）结果，对超出限值的墙体自行
逐步降低其刚度增减系数（WSSF），直至 NG 全部消除为止。

## 主要功能

**01. 自动查找 NG 构件**
执行结构分析与墙体设计后，按楼层/Wall ID 自动提取超出限值的墙体，并同时显示控制应力比。

**02. 设置降低条件**
设定每次降低量、系数下限与最大迭代次数后，即在该范围内自动进行迭代。

**03. 自动迭代降低**
每次迭代按「应用刚度 → 分析 → 重新确认设计」的顺序进行，当 NG 全部消除或系数达到下限时自动中止。

**04. 系数恢复**
迭代过程中已降低的系数，可随时通过一个按钮恢复至降低前的值（1.0）。
