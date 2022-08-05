#!/usr/bin/env python3
# Grupa6 / 01 / Predavanje 2 — Promenljive, tipovi

album = "Abbey Road"
bend = "The Beatles"
godina = 1969
ocena = 9.8
vinil = True

print("=== Album info ===")
print(f"Album: {album}")
print(f"Bend: {bend}")
print(f"Godina: {godina}")
print(f"Ocena: {ocena}/10")
print(f"Na vinilu: {vinil}")
print("")

print("=== type() ===")
print(f"album -> {type(album)}")
print(f"godina -> {type(godina)}")
print(f"ocena -> {type(ocena)}")
print(f"vinil -> {type(vinil)}")
print("")

print("=== Konverzija ===")
t = "1975"
print(f"str '{t}' -> int {int(t)}")
print(f"bool(0)={bool(0)}, bool(1)={bool(1)}")

print("\n=== f-string ===")
pi = 3.14159
print(f"PI: {pi:.3f}")
cena = 2499.5
print(f"Cena: {cena:>10,.2f} RSD")

x, y = 10, 20
x, y = y, x
print(f"Swap: x={x}, y={y}")
