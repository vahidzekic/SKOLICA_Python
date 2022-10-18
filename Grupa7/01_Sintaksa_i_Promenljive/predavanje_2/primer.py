#!/usr/bin/env python3
# Grupa7 / 01 / Predavanje 2 — Promenljive, tipovi

grad = "Istanbul"
drzava = "Turska"
stanovnika = 16_000_000
lat = 41.0082
lon = 28.9784
posecen = True

print("=== Destinacija ===")
print(f"Grad: {grad}, {drzava}")
print(f"Stanovnika: {stanovnika:,}")
print(f"Koordinate: ({lat}, {lon})")
print(f"Posećen: {posecen}")
print("")

print("=== type() ===")
print(f"grad -> {type(grad)}")
print(f"stanovnika -> {type(stanovnika)}")
print(f"lat -> {type(lat)}")
print(f"posecen -> {type(posecen)}")
print("")

print("=== Konverzija ===")
km_str = "594"
print(f"str '{km_str}' -> int {int(km_str)} -> float {float(km_str)}")
print(f"bool(0)={bool(0)}, bool('')={bool('')}")

print("\n=== f-string ===")
print(f"Lat: {lat:.4f}")
budzet = 125000
print(f"Budžet: {budzet:>12,} RSD")

x, y = 44.01, 20.92
x, y = y, x
print(f"Swap: x={x}, y={y}")
