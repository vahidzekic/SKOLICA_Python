#!/usr/bin/env python3
# Grupa5 / 01 / Predavanje 3 — Operatori, input()

a, b = 23, 7
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
print("=== Dodela ===")
x += 25; print(f"+= 25 -> {x}")
x -= 10; print(f"-= 10 -> {x}")
x *= 2;  print(f"*= 2  -> {x}")
x //= 3; print(f"//= 3 -> {x}")
print("")

print("=== BMI Kalkulator ===")
tezina = float(input("Težina (kg): "))
visina = float(input("Visina (m): "))
bmi = tezina / (visina ** 2)
print(f"BMI: {bmi:.1f}")
if bmi < 18.5: print("Pothranjenost")
elif bmi < 25: print("Normalna težina")
elif bmi < 30: print("Prekomerna težina")
else: print("Gojaznost")
