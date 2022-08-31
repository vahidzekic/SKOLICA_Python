#!/usr/bin/env python3
# Grupa6 / 05 / P2 â Lambda, map, filter

print("=== Lambda ===")
bpm_to_genre = lambda bpm: "Fast" if bpm >= 120 else "Slow"
print(f"140 BPM: {bpm_to_genre(140)}")
print(f"80 BPM: {bpm_to_genre(80)}")

print("\n=== map ===")
trajanja_s = [180, 125, 333, 420, 90]
trajanja_min = list(map(lambda s: round(s/60, 2), trajanja_s))
print(f"Sekunde: {trajanja_s}")
print(f"Minuti: {trajanja_min}")

print("\n=== filter ===")
ocene = [3.5, 4.2, 2.8, 4.9, 3.1, 4.7, 2.0]
preporuke = list(filter(lambda o: o >= 4.0, ocene))
print(f"Ocene: {ocene}")
print(f"PreporuÄeno (4+): {preporuke}")

print("\n=== sorted ===")
albumi = [("Abbey Road", 1969), ("Thriller", 1982), ("OK Computer", 1997)]
print(f"Po godini: {sorted(albumi, key=lambda a: a[1])}")