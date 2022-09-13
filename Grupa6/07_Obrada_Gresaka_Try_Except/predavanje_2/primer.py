#!/usr/bin/env python3
# Grupa6 / 07 / P2 â raise, custom

def proveri_bpm(bpm):
    if not isinstance(bpm, (int, float)): raise TypeError("BPM mora biti broj")
    if bpm < 20 or bpm > 300: raise ValueError(f"BPM {bpm} van opsega 20-300")
    return bpm

for t in [120, -5, "brzo", 400, 80]:
    try:
        proveri_bpm(t)
        print(f"  OK: {t} BPM")
    except (ValueError, TypeError) as e:
        print(f"  ERR {t}: {e}")

class PraznaPlaylista(Exception):
    def __init__(self): super().__init__("Playlista je prazna!")

def pusti(playlist):
    if not playlist: raise PraznaPlaylista()
    return playlist[0]

try: pusti([])
except PraznaPlaylista as e: print(f"\n  {e}")
print(f"  PuÅ¡tam: {pusti(['Imagine'])}")