#!/usr/bin/env python3
# Grupa4 / 07 / P2 â raise, sopstveni izuzeci

def proveri(g):
    if not isinstance(g, int): raise TypeError("Mora biti int")
    if g < 0 or g > 150: raise ValueError(f"Nevalidno: {g}")
    return g

for t in [25, -5, "x", 200]:
    try:
        proveri(t)
        print(f"  OK: {t}")
    except (ValueError, TypeError) as e:
        print(f"  ERR {t}: {e}")

class SlabaLozinka(Exception):
    def __init__(self, r): super().__init__(f"Slaba: {r}")

def check_pwd(p):
    if len(p) < 8: raise SlabaLozinka("< 8 char")
    if not any(c.isupper() for c in p): raise SlabaLozinka("nema veliko")
    if not any(c.isdigit() for c in p): raise SlabaLozinka("nema cifru")

for pwd in ["abc", "abcdefgh", "Abcdefg1"]:
    try:
        check_pwd(pwd)
        print(f"  OK: '{pwd}'")
    except SlabaLozinka as e:
        print(f"  ERR '{pwd}': {e}")