#!/usr/bin/env python3
# Grupa4 / 10 / P2 â Grupe, validacija
import re

print("=== Grupe ===")
email = "vahid.zekic@skolica.rs"
m = re.match(r"([\w.]+)@([\w.]+)\.(\w+)", email)
if m:
    print(f"  User: {m.group(1)}")
    print(f"  Domain: {m.group(2)}.{m.group(3)}")

print("\n=== Imenovane grupe ===")
log = "2024-03-15 14:30 [ERROR] Disk pun"
m = re.match(r"(?P<datum>[\d-]+) (?P<vreme>[\d:]+) \[(?P<nivo>\w+)\] (?P<msg>.+)", log)
if m:
    print(f"  {m.group('nivo')}: {m.group('msg')}")

print("\n=== Validacija ===")
def val(pat, t, opis):
    ok = 'OK' if re.match(pat, t) else 'FAIL'
    print(f"  {ok}: {opis} '{t}'")

val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'ok@test.rs', 'Email')
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'bad@', 'Email')
val(r'^\+?\d{10,15}$', '+381651234567', 'Tel')
val(r'^(?=.*[A-Z])(?=.*\d).{8,}$', 'Abcdefg1', 'Pass')
val(r'^(?=.*[A-Z])(?=.*\d).{8,}$', 'slaba', 'Pass')