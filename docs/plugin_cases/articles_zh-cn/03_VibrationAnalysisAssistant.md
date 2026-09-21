# Vibration Analysis Assistant

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60809469562649-VibrationAnalysisAssistant
- 视频：[03_VibrationAnalysisAssistant.mp4](../videos/03_VibrationAnalysisAssistant.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Vibration%20Analysis%20Assistant_%EB%82%98%EB%8A%94%EA%B0%90%EC%9E%90.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/03_VibrationAnalysisAssistant.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

Vibration Analysis Assistant 是一款插件，支持在 MIDAS GEN NX 分析模型中，于同一界面内输入、复核并应用
楼板或梁构件的人行荷载振动验算所需的 Time History Function、Time History Load Case、Dynamic Nodal Load。
可通过图形与表格直接确认荷载特性，并利用 GEN NX API 将 Time History 数据快速反映到模型中。

## 主要功能

**01. 人行荷载批量输入**
将人行荷载验算所需的动力荷载函数、分析工况、阻尼条件与节点荷载输入整合到同一界面中进行设置。

**02. 荷载函数实时复核**
输入值一经变更，IABSE 人行荷载时间函数的图形与表格即同步刷新，可立即确认荷载大小、持续时间与时间间隔。

**03. 通过 GEN NX API 自动应用输入数据**
以 API 创建、修改、删除 Time History Function、Time History Load Case、Dynamic Nodal Load
等输入数据，可直接应用到 GEN NX 模型中。

**04. 执行重复作业并减少输入错误**
减少在分散的多个功能窗口之间来回手动输入的过程，可按同一基准快速、一致地生成振动验算条件。
