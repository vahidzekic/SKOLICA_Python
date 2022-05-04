#!/usr/bin/env python3
# Grupa4 / 10 / P3 â PraktiÄna primena
import re

print("=== ÄiÅ¡Äenje ===")
neuredan = "  PreviÅ¡e   razmaka   svuda  "
ociscen = re.sub(r"\s+", " ", neuredan).strip()
print(f"  '{ociscen}'")

print("\n=== URL ekstrakcija ===")
html = '<a href="https://skolica.rs">S</a> <a href="https://python.org">P</a>'
urls = re.findall(r'href="(https?://[^"]+)"', html)
for u in urls: print(f"  {u}")

print("\n=== Log parsiranje ===")
logs = ["[INFO] Start", "[ERROR] DB down", "[WARN] Retry"]
pat = re.compile(r"\[(?P<lvl>\w+)\] (?P<msg>.+)")
for l in logs:
    m = pat.search(l)
    if m:
        icon = {"INFO": "i", "ERROR": "!", "WARN": "?"}.get(m.group('lvl'), '.')
        print(f"  [{icon}] {m.group('msg')}")

print("\n=== Maskiranje ===")
t = "Email: vahid@test.rs, tel: 065-123-4567"
t = re.sub(r"[\w.]+@[\w.]+", "***@***", t)
t = re.sub(r"\d{3}-\d{3}-\d{4}", "***", t)
print(f"  {t}")