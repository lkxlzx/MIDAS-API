# MIDAS NX Open API — 简体中文文档层

本目录（以及仓库内各处 `zh-cn/` 目录与 `*.zh-cn.md` 文件）是 **简体中文译文的并行层**。
韩文原文一律未改动，中文内容全部以镜像文件并存，便于随时回退与逐篇对照。

## 语言现状

| 语言 | 地位 | 位置 |
| --- | --- | --- |
| 한국어 | **权威原文**，与官方 Zendesk `ko` locale 对应 | 各目录下的既有文件 |
| English | 官方 `en-us` locale 抓取的译文 | `docs/plugin_cases/articles_en/` |
| 繁體中文 | 官方无此 locale，人工译文 | `docs/plugin_cases/articles_zh-tw/` |
| 简体中文 | 官方无此 locale，本层新增译文 | 本页 + 各处 `zh-cn/` |

官方 `support.midasuser.com` 仅提供 `ko / en-us / ja` 三个 locale（2026-09-21 复核），
**不存在中文原文**，因此中文只能由翻译派生。

## 镜像位置一览

| 内容 | 原文 | 简体中文 |
| --- | --- | --- |
| 仓库首页 | `README.md` | [`README.zh-cn.md`](../../README.zh-cn.md) |
| AI 作业规程 | `CLAUDE.md` | [`CLAUDE.zh-cn.md`](../../CLAUDE.zh-cn.md) |
| 认证与 Quick Tips | `docs/AUTHENTICATION.md` | [`AUTHENTICATION.md`](./AUTHENTICATION.md) |
| 官方错误核验记录 | `docs/error_reports/` | [`error_reports/`](./error_reports/) |
| **JSON Manual（27 章 + 索引）** | `docs/manual/` | [`../manual/zh-cn/INDEX.md`](../manual/zh-cn/INDEX.md) |
| Plug-in 目录与指南 | `docs/plugin/` | [`../plugin/zh-cn/INDEX.md`](../plugin/zh-cn/INDEX.md) |
| Plug-in 工具文档（63 篇） | `docs/plugin/tools/` | [`../plugin/zh-cn/tools/`](../plugin/zh-cn/tools/) |
| 应用案例文章（20 篇） | `docs/plugin_cases/articles/` | [`../plugin_cases/articles_zh-cn/`](../plugin_cases/articles_zh-cn/) |
| 应用案例规划文档（20 篇） | `docs/plugin_cases/planning/` | [`../plugin_cases/planning_zh-cn/`](../plugin_cases/planning_zh-cn/) |
| 案例总目录 | `docs/plugin_cases/INDEX.md` | [`../plugin_cases/zh-cn/INDEX.md`](../plugin_cases/zh-cn/INDEX.md) |
| 多语言示例 | `examples/` | [`../../examples/zh-cn/OTHER_LANGUAGES.md`](../../examples/zh-cn/OTHER_LANGUAGES.md) |
| 同步与抓取工具说明 | `scripts/*/README.md` | [`../../scripts/manual_sync/zh-cn/README.md`](../../scripts/manual_sync/zh-cn/README.md) |

## 翻译规约

用词与格式契约见 **[GLOSSARY.md](./GLOSSARY.md)**：术语表（韩 → 简体结构工程用语）、不译清单
（JSON、Key 名、端点、URL、article ID）、标题与锚点规则、`⚠️` 依据注释必须完整保留等。

## 已知限制

1. **译文会滞后。** `scripts/manual_sync/` 的定期同步（含 `.github/workflows/manual-sync.yml`
   每周一定时触发）只修补 `docs/manual/*.md` 与 `docs/plugin/**/*.md` 的韩文原文，
   不会自动更新 zh-cn 镜像。每次官方同步后需按 GLOSSARY 重跑受影响章节的本地化。
2. **技术判断以原文为准。** 原文中「示例优先于表格」「韩英 locale 分歧」等裁决依据在译文里被完整
   保留，但如与原文冲突，一律以韩文原文及官方 `en-us` / `ko` 页面为准，并回报译文偏差。
3. **术语存在地区差异。** 本层用大陆结构工程用语（节点／单元／截面／荷载工况），与
   `articles_zh-tw/` 的繁體用语（節點／單元／截面／荷重案例）不一致，两者不可互相套用。

## 校验

```bash
python scripts/manual_sync/validate_manual.py        # JSON 块可解析 + 页内锚点可解析（含 zh-cn 目录）
python scripts/zh-cn_localize/fix_links.py --check    # 跨文件链接/锚点重定向 + 标题数配平 + 韩文残留
```

两条命令都应为 0 问题。`fix_links.py` 负责把译文里照抄来的相对链接按各文件真实深度重写，
并把指向韩文原文的链接改指 zh-cn 镜像；跨文件的 `path#anchor` 依「标题序号」映射。
