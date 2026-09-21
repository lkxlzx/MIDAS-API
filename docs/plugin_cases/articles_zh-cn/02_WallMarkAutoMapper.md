# WallMark Auto Mapper

- 原文（韩文）：https://support.midasuser.com/hc/ko/articles/60809496186521-WallMarkAutoMapper
- 视频：[02_WallMarkAutoMapper.mp4](../videos/02_WallMarkAutoMapper.mp4)
- 原始视频：https://landing.midasuser.com/hubfs/outsourcing/page/KR/GEN%20NX/%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EC%BB%A8%ED%85%90%EC%B8%A0/Wall%20Mark%20Auto%20Mapper_%EB%82%98%EB%8A%94%EA%B0%90%EC%9E%90.mp4
- 参考资料：GEN NX API CHALLENGE 2026

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../articles/02_WallMarkAutoMapper.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../zh-cn/GLOSSARY.md)）

---

WallMark Auto Mapper 是一款从 DXF 结构平面图中提取墙体名称与位置信息，与 MIDAS GEN NX 分析模型中
既有各 Wall ID 的墙体位置自动进行匹配的插件，它将图纸上的墙体名称指认为对应 Wall ID 的 Wall Mark
并加以管理。自动匹配结果可在 Preview（预览）与结果表中查看、修改，之后按需选择性地应用到模型中。

## 主要功能

**01. 提取 DXF 图纸的墙体名称与位置信息**
从所选 DXF 结构平面图的指定图层中提取墙体名称与位置信息，自动构成用于与 GEN NX 模型匹配的图纸侧数据。

**02. 按 GEN NX Wall ID 计算墙体中心坐标**
筛选出所选楼层与 Wall Type（Membrane 或 Plate）对应的墙单元，并利用该墙单元的 Node 与 Element
信息，计算既有各 Wall ID 的墙体中心坐标。

**03. 图纸墙体信息与 Wall ID 自动匹配**
以允许距离为基准，将从 DXF 结构平面图中提取的墙体名称与位置信息和 GEN NX 分析模型中各 Wall ID
的墙体中心坐标进行比较，连接最接近的候选项。匹配结果分为匹配成功、需复核、匹配失败三类，并显示在
Preview 与结果表中。

**04. Wall Mark 的复核、应用与管理**
在 Preview 与结果表中确认、修改图纸墙体名称与 Wall ID 的匹配结果后，将所选的图纸墙体名称指认为对应
一个或多个 Wall ID 的 Wall Mark。支持对既有 Wall Mark 进行新增、修改、删除，以及 Excel 导入与导出、
PDF 结果表输出。
