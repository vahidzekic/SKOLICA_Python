#!/usr/bin/env python3
# Grupa5 / 01 / Predavanje 2 — Promenljive, tipovi

sport = "Fudbal"
tim = "FK Partizan"
golova = 48
prosek_po_utakmici = 1.6
u_ligi = True

print("=== Sportski podaci ===")
print(f"Sport: {sport}")
print(f"Tim: {tim}")
print(f"Golova: {golova}")
print(f"Prosek: {prosek_po_utakmici}")
print(f"U ligi: {u_ligi}")
print("")

print("=== type() ===")
print(f"sport -> {type(sport)}")
print(f"golova -> {type(golova)}")
print(f"prosek -> {type(prosek_po_utakmici)}")
print(f"u_ligi -> {type(u_ligi)}")
print("")

print("=== Konverzija ===")
t = "99"
print(f"str '{t}' -> int {int(t)} -> float {float(t)}")
print(f"bool(0)={bool(0)}, bool(42)={bool(42)}")
print("")

print("=== f-string ===")
pi = 3.141592653
print(f"PI 2 dec: {pi:.2f}")
print(f"Golova formatirano: {golova:05d}")

a, b = 5, 10
a, b = b, a
print(f"Swap: a={a}, b={b}")
