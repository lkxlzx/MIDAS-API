# WALL STACKER

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60809600655385-WALL-STACKER
- 视频：[01_WALL_STACKER.mp4](../videos/01_WALL_STACKER.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Wall%20Stacker%20SE_%ED%95%98%EB%A6%AC%EB%B3%B4.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/01_WALL_STACKER.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

本插件利用结构图纸自动建立墙体与外围过梁（Lintel Beam）模型。自动分割墙体交接处，
并将因图纸坐标微小误差而产生的邻近节点自动对齐、合并，快速生成单元间无断开、无多余节点的精确分析模型。

## 主要功能

**01. 面向首次使用者的分步引导**
通过顶部状态提示栏与输入项的脉动高亮效果，直观呈现当前进度与下一步操作，让首次使用的用户也能
轻松掌握完整工作流程。

**02. 按楼层提取、分析 DXF 墙体**
自动从各楼层 DXF 图纸中提取、分析中心线与墙体信息，构成建模对象。

**03. 墙体与过梁自动建模**
基于分析后的图纸，自动对各楼层墙体与洞口过梁进行建模。

**04. 交接点自动分割**
自动识别墙体交接点并分割单元，生成节点共享、连接性高的分析模型。

**05. 邻近节点自动合并**
避免因图纸坐标微小误差在同一接头处生成多个节点，并在设定的校正范围内自动对齐、合并邻近节点。
