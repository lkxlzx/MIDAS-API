# Plant Frame Builder

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60728306572441-PlantFrameBuilder
- 视频：[11_PlantFrameBuilder.mp4](../videos/11_PlantFrameBuilder.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Plant%20Frame%20Builder_Haydn.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/11_PlantFrameBuilder.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本款 GEN NX API 插件仅需输入 Bay 间距、层高等数值，即可自动创建双列多层 Pipe Rack 用于初始结构分析的
钢框架模型（Node/Column/Beam/Brace/Support）。

## 主要功能

**01. 基于参数的超高速自动建模（消除重复输入、提升实务灵活性）**
无需繁琐的手工作业，仅输入参数（Bay 间距、层高等）即可瞬间完成 Pipe Rack 骨架。既可读取已有模型的
材料（Material）与截面（Section），也可在 UI 内即时新建并指定，因此即使是空模型也能立即开始。从形状
到支承条件一并处理，有效缩短重复建模所占用的时间。

**02. 实时 3D 预览与完备的事前验证（拦截人为失误）**
参数变更时实时刷新 3D 预览，可直观确认形状。在即将反映到 GEN NX 模型之前，会校验预期构件数量、将被
赋予的 ID 范围，以及与既有模型是否冲突。仅在通过验证的安全状态下创建模型，从而拦截人为失误。
