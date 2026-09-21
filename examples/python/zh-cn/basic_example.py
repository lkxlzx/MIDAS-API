#!/usr/bin/env python3
# 语言：简体中文译文 | 原文：[韩文原文](../basic_example.py) · 译文生成：2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）
"""
MIDAS NX Open API - Python 基本示例

在 MIDAS Gen NX 中创建 1 个方形柱的最小示例。

事前准备：
  1) 运行 MIDAS Gen NX
  2) 在 Open API 菜单中获取 MAPI-Key
  3) 设置下方 MAPI_KEY / BASE_URL（或使用环境变量）

运行：
  pip install requests
  python basic_example.py
"""

import os
import json
import requests

# ── 设置 ────────────────────────────────────────────────────────────────
# Gen NX: .../gen   |   Civil NX: .../civil
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/gen")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

HEADERS = {
    "MAPI-Key": MAPI_KEY,          # ⚠️ 不是 Authorization Bearer
    "Content-Type": "application/json",
}


def MidasAPI(method: str, command: str, body: dict | None = None) -> dict:
    """MIDAS NX Open API 调用辅助函数。

    method  : "POST" | "PUT" | "GET" | "DELETE"
    command : "/doc/new", "/db/node" 等
    body    : {"Assign": {...}} 形式的请求体
    """
    url = BASE_URL + command
    fn = getattr(requests, method.lower())
    res = fn(url, headers=HEADERS, json=body, timeout=10)
    print(f"{method:6} {command:14} -> {res.status_code}")
    try:
        return res.json()
    except json.JSONDecodeError:
        return {"raw": res.text}


def main() -> None:
    print("🚀 MIDAS NX Open API - Python 示例")
    print(f"📍 Base URL: {BASE_URL}\n")

    # 1) 新建文档
    MidasAPI("POST", "/doc/new", {})

    # 2) 单位（台湾 RC 惯例：m, tonf）
    MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": "M", "FORCE": "TONF"}}})

    # 3) 材料（RC C32）
    MidasAPI("POST", "/db/matl", {"Assign": {1: {
        "TYPE": "CONC", "NAME": "C32",
        "PARAM": [{"P_TYPE": 1, "STANDARD": "AS17(RC)", "DB": "C32"}],
    }}})

    # 4) 截面（600x600 方形）
    MidasAPI("POST", "/db/sect", {"Assign": {1: {
        "SECTTYPE": "DBUSER", "SECT_NAME": "C600",
        "SECT_BEFORE": {"SHAPE": "SB", "DATATYPE": 2,
                        "SECT_I": {"vSIZE": [0.6, 0.6]}},
    }}})

    # 5) 节点（3.2m 柱）
    MidasAPI("POST", "/db/node", {"Assign": {
        1: {"X": 0, "Y": 0, "Z": 0},
        2: {"X": 0, "Y": 0, "Z": 3.2},
    }})

    # 6) 柱单元（BEAM）
    MidasAPI("POST", "/db/elem", {"Assign": {1: {
        "TYPE": "BEAM", "MATL": 1, "SECT": 1, "NODE": [1, 2], "ANGLE": 0,
    }}})

    # 7) 底部固定支承
    MidasAPI("POST", "/db/cons", {"Assign": {1: {
        "ITEMS": [{"ID": 1, "CONSTRAINT": "1111111"}],
    }}})

    # 8) 保存
    MidasAPI("POST", "/doc/save")

    print("\n✅ 完成！请在 MIDAS Gen NX 界面中确认柱。")


if __name__ == "__main__":
    main()
