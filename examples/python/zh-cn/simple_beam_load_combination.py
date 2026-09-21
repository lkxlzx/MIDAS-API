#!/usr/bin/env python3
# 语言：简体中文译文 | 原文：[韩文原文](../simple_beam_load_combination.py) · 译文生成：2026-09-21（机器辅助翻译，术语见 [GLOSSARY](../../../docs/zh-cn/GLOSSARY.md)）
"""
MIDAS NX Open API - Python 示例：简支梁荷载组合

把 10m 简支梁（两端铰/滚动支承）20 等分来创建节点/单元，
在施加自重(DL) + 均布梁单元荷载(SIDL)之后再构成荷载组合的示例。
相比 basic_example.py（只有 1 根柱的最小示例），展示了更贴近实战一步的流程。

出处：MIDAS Support - Example: Python
https://support.midasuser.com/hc/en-us/articles/30230181806361-Example-Python
（按本仓库的风格/命名重构官方教程文章的版本）

事前准备：
  1) 运行 MIDAS Civil NX 或 Gen NX
  2) 在 Open API 菜单中获取 MAPI-Key
  3) 设置下方 MAPI_KEY / BASE_URL（或使用环境变量）

运行：
  pip install requests
  python simple_beam_load_combination.py
"""

import os
import json
import requests

# ── 设置 ────────────────────────────────────────────────────────────────
BASE_URL = os.getenv("MIDAS_BASE_URL", "https://moa-engineers.midasit.com:443/civil")
MAPI_KEY = os.getenv("MIDAS_MAPI_KEY", "your-mapi-key-here")

HEADERS = {
    "MAPI-Key": MAPI_KEY,
    "Content-Type": "application/json",
}


def MidasAPI(method: str, command: str, body: dict | None = None) -> dict:
    """MIDAS NX Open API 调用辅助函数。"""
    url = BASE_URL + command
    fn = getattr(requests, method.lower())
    res = fn(url, headers=HEADERS, json=body, timeout=10)
    print(f"{method:6} {command:14} -> {res.status_code}")
    try:
        return res.json()
    except json.JSONDecodeError:
        return {"raw": res.text}


def main() -> None:
    print("🚀 MIDAS NX Open API - 简支梁荷载组合示例")
    print(f"📍 Base URL: {BASE_URL}\n")

    # ── 输入值 ──────────────────────────────────────────────────────────
    unit_dist, unit_force = "M", "KN"

    length, height, width = 10.0, 1.0, 0.8   # 梁长度/截面高度/宽度 (m)
    beam_load = -30.0                        # 附加均布荷载 (kN/m, SIDL)

    mat_standard, mat_grade = "AS17(RC)", "C32"

    material_id, section_id = 1, 1
    num_divisions = 20                       # 把梁 20 等分

    # 1) 新建文档
    MidasAPI("POST", "/doc/new", {})

    # 2) 单位
    MidasAPI("PUT", "/db/unit", {"Assign": {"1": {"DIST": unit_dist, "FORCE": unit_force}}})

    # 3) 材料（RC C32）
    MidasAPI("POST", "/db/matl", {"Assign": {material_id: {
        "TYPE": "CONC", "NAME": mat_grade,
        "PARAM": [{"P_TYPE": 1, "STANDARD": mat_standard, "DB": mat_grade}],
    }}})

    # 4) 截面（矩形数值输入截面）
    MidasAPI("POST", "/db/sect", {"Assign": {section_id: {
        "SECTTYPE": "DBUSER", "SECT_NAME": "Rectangular",
        "SECT_BEFORE": {
            "USE_SHEAR_DEFORM": True, "SHAPE": "SB", "DATATYPE": 2,
            "SECT_I": {"vSIZE": [height, width]},
        },
    }}})

    # 5) 节点（把 0 ~ length 按 num_divisions 等分）
    interval = length / num_divisions
    node_assign = {
        i + 1: {"X": round(i * interval, 6), "Y": 0.0, "Z": 0.0}
        for i in range(num_divisions + 1)
    }
    MidasAPI("POST", "/db/node", {"Assign": node_assign})

    # 6) 单元（按顺序把相邻节点用 BEAM 连接）
    elem_assign = {
        i + 1: {"TYPE": "BEAM", "MATL": material_id, "SECT": section_id, "NODE": [i + 1, i + 2]}
        for i in range(num_divisions)
    }
    MidasAPI("POST", "/db/elem", {"Assign": elem_assign})

    # 7) 支承条件（起始端铰支，末端滚动支承）
    last_node_id = num_divisions + 1
    MidasAPI("POST", "/db/cons", {"Assign": {
        1: {"ITEMS": [{"ID": 1, "CONSTRAINT": "1111000"}]},
        last_node_id: {"ITEMS": [{"ID": 1, "CONSTRAINT": "0111000"}]},
    }})

    # 8) 荷载工况（自重用 DL，附加荷载用 SIDL）
    MidasAPI("POST", "/db/stld", {"Assign": {
        1: {"NAME": "DL", "TYPE": "USER", "DESC": "Dead Load"},
        2: {"NAME": "SIDL", "TYPE": "USER", "DESC": "Super Imposed Dead Load"},
    }})

    # 9) 自重（在 DL 荷载工况上 -Z 方向 1 倍）
    MidasAPI("POST", "/db/bodf", {"Assign": {"1": {"LCNAME": "DL", "FV": [0, 0, -1]}}})

    # 10) 均布梁单元荷载（所有单元施加 SIDL）
    bmld_assign = {
        i + 1: {"ITEMS": [{
            "ID": 1, "LCNAME": "SIDL", "CMD": "BEAM", "TYPE": "UNILOAD",
            "DIRECTION": "GZ", "D": [0, 1], "P": [beam_load, beam_load],
        }]}
        for i in range(num_divisions)
    }
    MidasAPI("POST", "/db/bmld", {"Assign": bmld_assign})

    # 11) 荷载组合（DL*1.2 + SIDL*1.5）
    MidasAPI("POST", "/db/lcom-gen", {"Assign": {1: {
        "NAME": "Comb1", "ACTIVE": "ACTIVE", "iTYPE": 0,
        "vCOMB": [
            {"ANAL": "ST", "LCNAME": "DL", "FACTOR": 1.2},
            {"ANAL": "ST", "LCNAME": "SIDL", "FACTOR": 1.5},
        ],
    }}})

    # 12) 保存
    MidasAPI("POST", "/doc/save")

    print("\n✅ 完成！请在 MIDAS NX 界面中确认简支梁与荷载组合。")


if __name__ == "__main__":
    main()
