#!/usr/bin/env python3
# Grupa5 / 07 / P2 â raise, custom

def proveri_rezultat(golovi):
    if not isinstance(golovi, int): raise TypeError("Mora int")
    if golovi < 0: raise ValueError(f"Negativno: {golovi}")
    return golovi

for t in [3, -1, "x", 0]:
    try:
        proveri_rezultat(t)
        print(f"  OK: {t}")
    except (ValueError, TypeError) as e:
        print(f"  ERR {t}: {e}")

class NedovoljnoIgraca(Exception):
    def __init__(self, n): super().__init__(f"Samo {n}/11 igraÄa!")

def formacija(igraci):
    if len(igraci) < 11: raise NedovoljnoIgraca(len(igraci))
    return "Tim spreman!"

try: formacija(["A","B","C"])
except NedovoljnoIgraca as e: print(f"  {e}")