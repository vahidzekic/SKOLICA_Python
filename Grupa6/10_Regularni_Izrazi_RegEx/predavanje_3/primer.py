#!/usr/bin/env python3
# Grupa6 / 10 / P3 â PraktiÄno
import re

print("=== ÄiÅ¡Äenje ===")
lyrics = "  Imagine   all   the   people  "
clean = re.sub(r"\s+", " ", lyrics).strip()
print(f"  '{clean}'")

print("\n=== URL ===")
html = '<a href="https://spotify.com">S</a> <a href="https://deezer.com">D</a>'
for u in re.findall(r'href="(https?://[^"]+)"', html):
    print(f"  {u}")

print("\n=== Log ===")
logs = ["[INFO] Play", "[ERROR] No file", "[WARN] Buffer"]
pat = re.compile(r"\[(?P<l>\w+)\] (?P<m>.+)")
for l in logs:
    m = pat.search(l)
    if m: print(f"  [{m.group('l')}] {m.group('m')}")

print("\n=== Mask ===")
t = "Email: info@music.rs, tel: 011-222-3333"
t = re.sub(r"[\w.]+@[\w.]+", "***", t)
t = re.sub(r"\d{3}-\d{3}-\d{4}", "***", t)
print(f"  {t}")