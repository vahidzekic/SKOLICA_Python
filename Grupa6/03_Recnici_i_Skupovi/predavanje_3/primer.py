#!/usr/bin/env python3
# Grupa6 / 03 / P3 â Comprehension, Counter
from collections import Counter, defaultdict

print("=== Dict Comprehension ===")
note = {n: round(261.63 * 2**(i/12), 1) for i, n in enumerate(["C","C#","D","D#","E","F","F#","G"])}
for n, hz in note.items():
    print(f"  {n}: {hz} Hz")

print("\n=== Counter ===")
zanrovi = ["Rock","Pop","Rock","Jazz","Pop","Rock","Blues","Jazz","Pop","Rock"]
br = Counter(zanrovi)
print(f"Å½anrovi: {dict(br)}")
print(f"Top 2: {br.most_common(2)}")

print("\n=== defaultdict ===")
po_zanru = defaultdict(list)
pesme = [("Rock","Bohemian"),("Pop","Thriller"),("Rock","Stairway"),("Jazz","So What")]
for z, p in pesme:
    po_zanru[z].append(p)
for z, ps in po_zanru.items():
    print(f"  {z}: {ps}")