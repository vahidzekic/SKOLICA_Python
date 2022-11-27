#!/usr/bin/env python3
# Grupa7 / 10 / P3 â PraktiÄno
import re

print("=== ÄiÅ¡Äenje ===")
opis = "  Predivan   grad   sa   bogatom   istorijom  "
print(f"  '{re.sub(r'\s+', ' ', opis).strip()}'")

print("\n=== URL ===")
html = '<a href="https://booking.com">B</a> <a href="https://airbnb.com">A</a>'
for u in re.findall(r'href="(https?://[^"]+)"', html):
    print(f"  {u}")

print("\n=== Log ===")
logs = ["[INFO] Booking OK", "[ERROR] Payment fail", "[WARN] Slow"]
pat = re.compile(r"\[(?P<l>\w+)\] (?P<m>.+)")
for l in logs:
    m = pat.search(l)
    if m: print(f"  [{m.group('l')}] {m.group('m')}")

print("\n=== Mask ===")
t = "PasoÅ¡: AB1234567, tel: 065-111-2222"
t = re.sub(r"[A-Z]{2}\d{7}", "*********", t)
t = re.sub(r"\d{3}-\d{3}-\d{4}", "***", t)
print(f"  {t}")