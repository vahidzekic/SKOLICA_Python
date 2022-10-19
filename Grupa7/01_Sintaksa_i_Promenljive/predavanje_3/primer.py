#!/usr/bin/env python3
# Grupa7 / 01 / Predavanje 3 — Operatori, input()

a, b = 594, 120
print("=== Aritmetika ===")
print(f"Udaljenost: {a}km, Brzina: {b}km/h")
print(f"Vreme: {a/b:.1f}h")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print("")

x = 1000
x += 250; print(f"+= 250 -> {x}")
x -= 100; print(f"-= 100 -> {x}")
x *= 2;   print(f"*= 2   -> {x}")
x //= 3;  print(f"//= 3  -> {x}")
print("")

print("=== Planer putovanja ===")
km = float(input("Udaljenost (km): "))
gorivo_l = float(input("Potrošnja (l/100km): "))
cena_l = float(input("Cena goriva (RSD/l): "))
ukupno_l = km * gorivo_l / 100
ukupno_rsd = ukupno_l * cena_l
print(f"\nUkupno gorivo: {ukupno_l:.1f}L")
print(f"Ukupno cena: {ukupno_rsd:,.0f} RSD")
