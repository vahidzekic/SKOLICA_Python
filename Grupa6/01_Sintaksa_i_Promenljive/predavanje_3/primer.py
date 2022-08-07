#!/usr/bin/env python3
# Grupa6 / 01 / Predavanje 3 — Operatori, input()

a, b = 19, 4
print("=== Aritmetika ===")
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} // {b} = {a//b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} ** {b} = {a**b}")
print("")

x = 100
x += 15; print(f"+= 15 -> {x}")
x -= 5;  print(f"-= 5  -> {x}")
x *= 3;  print(f"*= 3  -> {x}")
x //= 7; print(f"//= 7 -> {x}")
print("")

print("=== Konvertor valuta ===")
eur = float(input("Iznos u EUR: "))
kurs = 117.5
rsd = eur * kurs
print(f"{eur:.2f} EUR = {rsd:,.2f} RSD (kurs: {kurs})")
