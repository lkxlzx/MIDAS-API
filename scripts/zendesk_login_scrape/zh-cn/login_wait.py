#语言：简体中文译文 · 原文：[韩文原文](../login_wait.py) · 译文生成：2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）
"""针对专用 profile 打开一个真实（headed）Chrome 窗口，让用户手动登录，
登录成功后保存渲染完成的目标页面。本脚本绝不接触密码/cookie —— 由人在可见的窗口里登录。
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config

options = Options()
options.add_argument(f"--user-data-dir={config.PROFILE_DIR}")
options.add_argument("--profile-directory=Default")
options.add_argument("--window-size=1280,900")
options.add_argument("--lang=ko-KR")
# 注意：这里不要加 --headless。本站的 Cloudflare 机器人管理即便对持有有效已登录会话的
# 无头浏览器也只返回空壳页面。

driver = webdriver.Chrome(options=options)
driver.get(config.TARGET_URL)

print("请在浏览器窗口中登录。将自动检测登录完成（最多等待 10 分钟）...")

deadline = time.time() + 600
success = False
while time.time() < deadline:
    time.sleep(3)
    url = driver.current_url
    if not any(marker in url for marker in config.LOGIN_DOMAIN_MARKERS):
        success = True
        break

if success:
    driver.get(config.TARGET_URL)
    time.sleep(3)
    with open(config.LIST_PAGE_HTML, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"SUCCESS -> {config.LIST_PAGE_HTML}")
else:
    print("TIMEOUT -- 未检测到登录完成。请重新运行。")

driver.quit()
