#!/usr/bin/env python3
# Grupa7 / 10 / P2 â Grupe
import re

print("=== Grupe ===")
email = "booking@travelco.rs"
m = re.match(r"([\w.]+)@([\w.]+)\.(\w+)", email)
if m:
    print(f"  User: {m.group(1)}, Domain: {m.group(2)}.{m.group(3)}")

print("\n=== Imenovane grupe ===")
let = "BEG-IST-2025-07-15"
m = re.match(r"(?P<od>[A-Z]{3})-(?P<do>[A-Z]{3})-(?P<datum>\d{4}-\d{2}-\d{2})", let)
if m:
    print(f"  {m.group('od')} -> {m.group('do')} na {m.group('datum')}")

print("\n=== Validacija ===")
def val(pat, t, opis):
    ok = 'OK' if re.match(pat, t) else 'FAIL'
    print(f"  {ok} {opis}: '{t}'")
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'ok@t.rs', 'Email')
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'bad@', 'Email')
val(r'^[A-Z]{3}$', 'BEG', 'IATA kod')
val(r'^[A-Z]{3}$', 'be', 'IATA kod')