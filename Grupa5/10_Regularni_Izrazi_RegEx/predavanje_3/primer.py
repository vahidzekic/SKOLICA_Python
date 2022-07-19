#!/usr/bin/env python3
# Grupa5 / 10 / P3 â PraktiÄno
import re

print("=== ÄiÅ¡Äenje ===")
neuredan = "  PreviÅ¡e   razmaka  "
print(f"  '{re.sub(r'\s+', ' ', neuredan).strip()}'")

print("\n=== URL ===")
html = '<a href="https://fss.rs">FSS</a> <a href="https://uefa.com">UEFA</a>'
for u in re.findall(r'href="(https?://[^"]+)"', html):
    print(f"  {u}")

print("\n=== Log ===")
logs = ["[INFO] Start", "[ERROR] DB fail", "[WARN] Slow"]
pat = re.compile(r"\[(?P<l>\w+)\] (?P<m>.+)")
for l in logs:
    m = pat.search(l)
    if m: print(f"  [{m.group('l')}] {m.group('m')}")

print("\n=== Mask ===")
t = "Email: a@b.rs, tel: 065-111-2222"
t = re.sub(r"[\w.]+@[\w.]+", "***", t)
t = re.sub(r"\d{3}-\d{3}-\d{4}", "***", t)
print(f"  {t}")