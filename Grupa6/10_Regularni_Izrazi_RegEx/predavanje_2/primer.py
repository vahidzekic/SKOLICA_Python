#!/usr/bin/env python3
# Grupa6 / 10 / P2 â Grupe, validacija
import re

print("=== Grupe ===")
email = "info@musicshop.rs"
m = re.match(r"([\w.]+)@([\w.]+)\.(\w+)", email)
if m:
    print(f"  User: {m.group(1)}, Domain: {m.group(2)}.{m.group(3)}")

print("\n=== Imenovane grupe ===")
fajl = "Pink_Floyd-Dark_Side-1973.mp3"
m = re.match(r"(?P<bend>[\w]+)-(?P<album>[\w]+)-(?P<god>\d{4})\.(?P<ext>\w+)", fajl)
if m:
    print(f"  Bend: {m.group('bend')}, Album: {m.group('album')}, Godina: {m.group('god')}")

print("\n=== Validacija ===")
def val(pat, t, opis):
    ok = 'OK' if re.match(pat, t) else 'FAIL'
    print(f"  {ok} {opis}: '{t}'")
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'ok@t.rs', 'Email')
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'bad@', 'Email')