# 抓取需要登录的 Zendesk 分类（Selenium 成功案例）

> **语言：** 简体中文译文  
> **原文：** [韩文原文](../README.md)  
> **译文生成：** 2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）

`support.midasuser.com` 的部分分类（例：会员专用 "Plugin 案例"）无法用 `manual_sync` 所使用的
公开 Help Center API（`/api/v2/help_center/...`）访问。本文件夹把攻下这类**需要登录的分类**
的真实成功案例整理成了可复用的脚本。

## 为什么 curl/API 不行（先试过但失败的方法）

1. **curl + 从浏览器复制的会话 cookie** → 不断被 302 重定向回登录页。
   从 Cloudflare 的 `__cf_bm` 每个请求都重新签发来看，会话被绑定在浏览器的 TLS/设备指纹上，
   因此来自其他 IP/客户端（curl）的请求即使 cookie 值正确也不会被信任。
2. **Zendesk Help Center REST API + 会话 cookie** → API 根本不承认 cookie。只接受 Basic
   Auth（邮箱+密码）或 API token，而本站使用的是 `members.midasuser.com` 自定义
   SSO，压根不存在 Zendesk 原生密码。（参考：`manual_sync` 之所以成功，是因为那些分类
   **本来就不需要登录、属于公开分类** — 与本方法无关。）
3. **Selenium + headless 模式** → 登录是成功了（cookie 已存进 profile），但之后的页面请求中
   Cloudflare 识别出无头模式，只返回空壳页面（`<title>` 就是域名本身）。→ **必须关掉 headless、
   以有界面的浏览器启动才能通过**。

## 成功的方法

**真浏览器（Selenium，headed）+ 专用 profile 目录 + 人在屏幕上亲自登录。**

1. 运行 `login_wait.py` → Chrome 以专用 `chrome_profile/` 目录启动（不是 headless）。
2. 用户在该窗口中照常登录（绝不把密码交给 Claude/脚本）。
3. 脚本轮询 URL，直到其跳出登录域名 → 自动检测到登录完成 → 保存目标页面 HTML。
4. 之后的抓取（`scrape_pages.py`）**复用同一个 `chrome_profile/`** — Chrome 会把 cookie 存到
   磁盘，因此不必每次重新登录。但此时同样**禁止 headless**（原因见上文第 3 条）。

## 文件组成

| 文件 | 作用 |
|---|---|
| `login_wait.py` | 用目标 URL 启动 Chrome，自动检测登录完成并保存渲染后的 HTML |
| `parse_links.py` | 从已保存的分类/列表页 HTML 中抽取下级 article 链接（标题+URL） |
| `scrape_pages.py` | 遍历链接列表，抽取各页面的标题/正文/视频（iframe·video src） |
| `download_assets.py` | 把抽取到的视频等附件 URL 下载为实际文件 |

## 本地运行顺序

```bash
cd scripts/zendesk_login_scrape

# 1) 在 config.py 中把 TARGET_URL、LOGIN_DOMAIN_MARKERS 等改成新对象

# 2) 等待登录 + 保存列表页（Chrome 窗口弹出后在其中直接登录）
python login_wait.py

# 3) 从列表页抽取下级链接
python parse_links.py

# 4) 抓取各下级页面（保持 headed，复用同一 profile）
python scrape_pages.py

# 5) 下载视频/附件
python download_assets.py
```

## 复用时的检查清单

- 把 `config.py` 的 `TARGET_URL`、`OUT_DIR` 改成新对象对应的值。
- `chrome_profile/` 是存有会话（登录状态）的目录。可以复用，但会话过期时
  重新运行 `login_wait.py` 弹出重新登录窗口即可。删掉重新开始也无妨（重新登录即可）。
- **绝对不要做**：把密码以明文交给对话窗口/脚本、误把其他域名（例：Google 账号）的
  cookie 复制粘贴过来 — 实际发生过一次这样的失误。索要浏览器 cookie 时必须确认
  它是**目标站点域名**的 cookie（`Cookie:` 头部值应以
  `_help_center_session=...`、`_zendesk_session=...` 这类名字开头才正常）。
- 在本站（启用了 Cloudflare 机器人管理）无法使用 headless。复用到其他站点时先试
  headless，若只出现空白页面或只有标题就切到 headed。

## 实际成功案例

- 2026-08-07：`support.midasuser.com/hc/ko/categories/60103640613785`
  （"API 应用案例" — Plugin 20 种，需要登录）→ 文档 20 个 + 视频 20 个（mp4，共 1.8GB）
  全量采集成功。产出物：`docs/plugin_cases/`。
