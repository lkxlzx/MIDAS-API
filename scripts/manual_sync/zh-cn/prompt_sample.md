# 手册用作业 1 号提示词

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../prompt_sample.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）

# 角色与目标
你是一名技术文档写作者兼抓取/解析专家，负责把官方网页手册完整抓取下来（Fetch/Parsing），构建毫无遗漏的顶级 GitHub Markdown（.md）文档。

# 第 1 步指示事项
1. 对下面提供的【手册对象地址/文本】的数据进行监控与采集（Fetch），必须清晰、不得有文字丢失（遗漏）。
2. 全部分量非常庞大，一次性输出 100% 会在中途断掉或出现省略。因此请先分析全部内容，然后以能合理拆分上传到「GitHub 文件（.md）」的形式，先用列表给出【具体的拆分目录（Index）与作业计划】。
3. 各拆分部分必须按功能关联性（例：01_基础设置、02_节点控制、03_单元控制 等）干净利落地划分。

# 输出结果
- 整体解析摘要与拆分后的目录列表
- 表示已准备好进入下一步的话术（"准备完成了。要从 [Part 1] 开始生成文档吗？"）

---
# 手册对象（URL 或复制的文本）：
https://support.midasuser.com/hc/ko/articles/33016922742937-MIDAS-API-Online-Manual


# 手册用作业 2 号提示词

# 指定要创建的文件名
好，按计划推进。接下来开始创建下一个文件 **[04_DB_Properties.md]**。

# 编写与编辑规则
1. 禁止遗漏：该部分包含的 API Endpoint、HTTP 方法（GET/POST/PUT/DELETE 等）、参数表、Request/Response JSON body，一个都不许省略，全部用 Markdown 表格与代码块书写。
2. 包含实务代码：为了让开发者可以立即对接，请编写带注释的、基于 Python（requests 库）的完整示例代码。
3. 可读性：严格遵守 GFM（GitHub Flavored Markdown）规范，确保直接上传到 GitHub（GitHub）仓库时渲染效果不会破版。

# 下一次作业准备
输出请放进 Markdown 代码块（```md ... ```）里，方便复制粘贴到 GitHub；写完后请提示已准备好进行下一部分 **[05_DB_Boundary.md]**。
