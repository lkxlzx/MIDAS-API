# BUOY CHECKER

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60726911770905-BUOY-CHECKER
- 视频：[17_BUOY_CHECKER.mp4](../videos/17_BUOY_CHECKER.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Buoy%20Checker%20SE_%ED%95%98%EB%A6%AC%EB%B3%B4.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/17_BUOY_CHECKER.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本插件以 GEN NX 分析结果与用户输入的设计条件为基础，验算结构物在竣工状态及各施工阶段的抗浮安全性。
验算所需的分析结果均自动从 GEN NX 读取，无需在结果表或计算表之间来回切换，即可从各阶段安全系数验算、
控制水位计算直至输出报告，以一条连续的工作流程完成。

## 主要功能

**01. 面向首次使用者的分步引导**
通过顶部状态提示栏与输入项的脉动高亮效果，直观呈现当前进度与下一步操作，让首次使用的用户也能
轻松掌握完整工作流程。

**02. 自动联动 GEN NX 结果并交叉验证**
自动从 GEN NX 读取各 Story 的固定荷载轴力与基础支座反力，并对两项分析结果进行交叉验证，确认数据
是否缺失或不一致。

**03. 分阶段抗浮安全性与控制水位计算**
自动计算竣工状态与各施工阶段的浮力、抵抗力及抗浮安全系数，并反算出满足目标安全系数所需的各阶段
控制水位。

**04. 输出计算依据报告**
提供报告输出功能，整理输入条件、交叉验证结果、各阶段抗浮安全系数与控制水位的计算依据。
