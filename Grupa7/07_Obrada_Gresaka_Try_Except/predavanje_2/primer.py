#!/usr/bin/env python3
# Grupa7 / 07 / P2 â raise, custom

def proveri_budzet(iznos):
    if not isinstance(iznos, (int, float)): raise TypeError("Mora broj")
    if iznos < 0: raise ValueError(f"Negativan: {iznos}")
    return iznos

for t in [500, -100, "mnogo", 0]:
    try:
        proveri_budzet(t)
        print(f"  OK: {t} EUR")
    except (ValueError, TypeError) as e:
        print(f"  ERR {t}: {e}")

class DestinacijaNePostoji(Exception):
    def __init__(self, grad): super().__init__(f"Destinacija '{grad}' ne postoji!")

def nadji(grad, baza):
    if grad not in baza: raise DestinacijaNePostoji(grad)
    return baza[grad]

baza = {"Istanbul": 594, "Rim": 1060}
for g in ["Istanbul", "Mars"]:
    try: print(f"  {g}: {nadji(g, baza)}km")
    except DestinacijaNePostoji as e: print(f"  {e}")