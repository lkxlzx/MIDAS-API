# RCBeamDeflectionCheck

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60728330684697-RCBeamDeflectionCheck
- 视频：[10_RCBeamDeflectionCheck.mp4](../videos/10_RCBeamDeflectionCheck.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/RC%20Beam%20Deflection%20Check_%EC%8A%A4%ED%83%80%EB%9F%AC%EB%B8%8C%ED%94%BC%EC%89%AC.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/10_RCBeamDeflectionCheck.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本插件通过 API 读取 MIDAS GEN NX 模型中 RC 梁的截面、材料、配筋以及各荷载工况的分析弯矩，依据
KDS 14 20 30 第 4.2 节标准，采用有效截面刚度（Ie，Branson）自动计算短期与长期挠度，并与允许挠度
进行比较，输出 A4 结构计算书（挠度验算书）。

## 主要功能

**01. 自动读取模型数据**
通过 API 自动提取 RC 梁的截面、材料、配筋与分析弯矩。

**02. 自动计算挠度**
依据 KDS 14 20 30 标准自动计算短期、长期挠度。

**03. 自动复核允许基准**
将计算结果与允许挠度比较，判定是否满足要求。

**04. 自动输出结构计算书**
生成包含计算过程与结果的 A4 挠度验算书。
