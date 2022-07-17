#!/usr/bin/env python3
# Grupa5 / 10 / P2 â Grupe, validacija
import re

print("=== Grupe ===")
email = "marko@sportklub.rs"
m = re.match(r"([\w.]+)@([\w.]+)\.(\w+)", email)
if m:
    print(f"  User: {m.group(1)}, Domain: {m.group(2)}.{m.group(3)}")

print("\n=== Imenovane grupe ===")
rez = "Partizan 3:1 Zvezda"
m = re.match(r"(?P<domacin>\w+) (?P<d>\d+):(?P<g>\d+) (?P<gost>\w+)", rez)
if m:
    print(f"  {m.group('domacin')} {m.group('d')}-{m.group('g')} {m.group('gost')}")

print("\n=== Validacija ===")
def val(pat, t, opis):
    ok = 'OK' if re.match(pat, t) else 'FAIL'
    print(f"  {ok} {opis}: '{t}'")
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'ok@t.rs', 'Email')
val(r'^[\w.+-]+@[\w-]+\.[a-z]{2,}$', 'bad@', 'Email')
val(r'^(?=.*[A-Z])(?=.*\d).{8,}$', 'Test1234', 'Pass')