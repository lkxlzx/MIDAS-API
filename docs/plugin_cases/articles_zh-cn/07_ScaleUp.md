# SCALE UP

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60728766698777-ScaleUp
- 视频：[07_ScaleUp.mp4](../videos/07_ScaleUp.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Scale%20Up%20SE_%ED%95%98%EB%A6%AC%EB%B3%B4.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/07_ScaleUp.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本插件依据抗震设计标准自动计算反应谱分析的修正系数 Cm，并在 GEN NX 中自动生成设计用荷载组合。
确定 Cm 所需的分析结果与荷载工况信息均自动从 GEN NX 读取，无需在结果表或计算表之间来回切换，
即可从确认分析结果、确定 Cm、生成设计用荷载组合直至输出报告，以一条连续的工作流程完成。

## 主要功能

**01. 面向首次使用者的分步引导**
通过顶部状态提示栏与输入项的脉动高亮效果，直观呈现当前进度与下一步操作，让首次使用的用户也能
轻松掌握完整工作流程。

**02. 自动计算修正系数 Cm**
按方向对比等效静力分析与反应谱分析的基底剪力，并依据抗震设计标准自动计算反应谱分析的修正系数 Cm。

**03. 自动联动 GEN NX 分析信息**
自动从 GEN NX 读取确定 Cm 所需的分析结果与荷载工况信息，无需反复确认结果和手动输入即可便捷完成计算。

**04. 生成荷载组合并输出报告**
自动在 GEN NX 中生成采用所计算 Cm 的设计用荷载组合，并提供整理 Cm 计算过程与套用依据的报告输出功能。
