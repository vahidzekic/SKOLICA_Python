#!/usr/bin/env python3
# Grupa6 / 04 / P2 â FOR

print("=== Playlist ===")
pesme = ["Imagine", "Yesterday", "Let It Be", "Hey Jude", "Help!"]
for i, p in enumerate(pesme, 1):
    print(f"  {i}. {p}")

print("\n=== range ===")
print(f"Parni: {list(range(2, 21, 2))}")
print(f"Obrnuto: {list(range(5, 0, -1))}")

print("\n=== zip ===")
pesme_z = ["Imagine", "Yesterday", "Hey Jude"]
trajanja = [3.03, 2.05, 7.11]
for p, t in zip(pesme_z, trajanja):
    print(f"  {p}: {t} min")

print("\n=== Nota generator ===")
note = ["C", "D", "E", "F", "G", "A", "B"]
for oktava in range(3, 6):
    for nota in note:
        print(f"{nota}{oktava}", end=" ")
    print("")