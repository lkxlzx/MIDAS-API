# RCRebarOptimizer

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60728648218265-RCRebarOptimizer
- 视频：[09_RCRebarOptimizer.mp4](../videos/09_RCRebarOptimizer.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/RCRebarOptimizer_%ED%94%BC%EC%B9%B4%ED%94%BC%EC%B9%B4%EB%B6%80.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/09_RCRebarOptimizer.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本插件利用 MIDAS GEN NX 的 RC 设计 API（DCRM·CD/BD-ANAL·设计结果表），对 RC 柱、梁的主筋按候选规格
自动进行扫描设计，算出满足验算比（CHK）的各构件最小钢筋配筋量，并将相同截面（柱标记·梁标记）统一为
一份标准配筋。

## 主要功能

**01. 结果设计**
利用 MIDAS GEN NX 的 RC 设计 API（DCRM·CD/BD-ANAL·设计结果表），对 RC 柱、梁的主筋按候选规格
自动进行扫描设计。

**02. 构件复核**
算出满足验算比（CHK）的各构件最小钢筋配筋量，并将相同截面（柱标记·梁标记）统一为一份标准配筋的插件。

**03. 构件设计**
所有标准配筋均经 GEN NX 重新设计对验算比进行再验证，因而保证安全性；并通过控制因素诊断，给出哪些
构件还可以进一步减少。

**04. 结果复核**
配筋表与比较结果可即时以 PDF 输出，大幅缩短设计、工程量统计与审查文档的编制时间。
