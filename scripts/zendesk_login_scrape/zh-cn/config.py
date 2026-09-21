#语言：简体中文译文 · 原文：[韩文原文](../config.py) · 译文生成：2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）
"""按目标站点修改这里。本文件夹内其他文件针对新的运行都不需要改动。"""
import os

# --- 目标 ---
TARGET_URL = "https://support.midasuser.com/hc/ko/categories/60103640613785?page=1&tab=all"
# 登录前 URL 中会包含以下字符串之一（登录完成的判定依据）
LOGIN_DOMAIN_MARKERS = ["members.midasuser.com", "zendesk.com/access"]

# --- 输出路径 ---
HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(HERE, "chrome_profile")
OUT_DIR = os.path.join(HERE, "output")
LIST_PAGE_HTML = os.path.join(OUT_DIR, "list_page.html")
LINKS_JSON = os.path.join(OUT_DIR, "links.json")
PAGES_DIR = os.path.join(OUT_DIR, "pages")
PAGES_INDEX_JSON = os.path.join(OUT_DIR, "pages_index.json")
ASSETS_DIR = os.path.join(OUT_DIR, "assets")

# 认定为 article 链接的 URL 模式（Zendesk 标准）。复用到其他站点时需修改。
ARTICLE_HREF_MARKERS = ["/hc/ko/articles/", "/hc/ko/sections/"]

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

for d in (OUT_DIR, PAGES_DIR, ASSETS_DIR):
    os.makedirs(d, exist_ok=True)
