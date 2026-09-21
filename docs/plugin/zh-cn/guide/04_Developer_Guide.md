# A Guide to Creating Plug-in for Developers

> **原文：** [A Guide to Creating Plug-in for Developers](https://support.midasuser.com/hc/ko/articles/44321750649369-A-Guide-to-Creating-Plug-in-for-Developers)
> **原文创建：** 2025-03-10 · **原文最后编辑：** 2025-05-19（2026-08-04 复核，内容无变更 — 仅时间戳更新的表面性改动）

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../../guide/04_Developer_Guide.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../zh-cn/GLOSSARY.md)）

---

本文是**面向开发者的 Plug-in 开发指南**。

## 前置要求

- CLI（Command-Line Interface）
- npm（node package manager）
- npx（node package execute）
- 基于 TypeScript 的 React
- Python（视所使用的库而定）

### 推荐 IDE/框架

- Visual Studio Code
- Node.js

## MIDAS IT 提供的库

为简化 Plug-in 开发，MIDAS IT 提供以下库：

| 库（npm） | 说明 |
| --- | --- |
| `@midasit-dev/cra-template-moaui` | 由 React + TypeScript + moaui + Pyscript 构成的 Plug-in 开发模板 |
| `@midasit-dev/cra-template-moaui-light` | 不含 Pyscript 的 React + TypeScript + moaui 模板 |
| `@midasit-dev/moaui-components-v1` | 基于 Material UI、应用 MIDAS IT 设计的 UI 组件 |
| `@midasit-dev/moaui-lab` | 上述组件的 StoryBook |

> **为什么是 Pyscript？** Plug-in 是工程工具，本质上需要数值计算，而 Python 被判断为最适合这类计算的工具，因此被包含进了模板。

## Plug-in 上传

开发好的 Plug-in 可以在产品内注册后使用。步骤如下。

1. 构建后打包为单个 ZIP 文件。
2. 移动到 Plug-in 平台的 **MyWork** 选项卡。
3. 进行上传。

运行已上传的 Plug-in（请事先确认 API 连接）后，会显示按预期开发好的界面。

## FAQ

**Q. 图标如何注册？**
A. 构建文件夹最上层的 `icon.svg` 文件会被识别为 Plug-in 图标（不支持其他格式）。制作 SVG 文件并保存为 `icon.svg`，在把构建结果打包为 ZIP 时务必将其包含进去。

**Q. 说明（Description）如何修改？**
A. 构建文件夹中的 `readme.md` 内容会显示为 Plug-in 说明。在 `readme.md` 中撰写说明，并确保构建时包含该文件。

**Q. 要与其他用户共享 Plug-in 怎么办？**
A. 以原文撰写时点为准，说明正在准备可在 Marketplace 中共享各自开发的 Plug-in 的系统。

> ⚠️ Marketplace 共享功能在 [How to use MIDAS Plug-ins](./02_How_to_Use.md) 中也同样以"准备中"提及。实际是否提供，需在定期检查时再确认。
