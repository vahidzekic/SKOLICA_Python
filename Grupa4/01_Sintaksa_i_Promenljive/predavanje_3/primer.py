#!/usr/bin/env python3
# ŠKOLICA Python — Grupa4 / 01 / Predavanje 3
# Tema: Operatori, input(), kalkulator

a, b = 17, 5
print("=== Aritmetika ===")
print(f"{a} + {b}  = {a + b}")
print(f"{a} - {b}  = {a - b}")
print(f"{a} * {b}  = {a * b}")
print(f"{a} / {b}  = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b}  = {a % b}")
print(f"{a} ** {b} = {a ** b}")
print("")

print("=== Operatori dodele ===")
x = 50
print(f"x = {x}")
x += 10; print(f"x += 10 -> {x}")
x -= 3;  print(f"x -= 3  -> {x}")
x *= 2;  print(f"x *= 2  -> {x}")
x //= 7; print(f"x //= 7 -> {x}")
print("")

print("=== Kalkulator ===")
num1 = float(input("Prvi broj: "))
num2 = float(input("Drugi broj: "))
print(f"Zbir: {num1 + num2}")
print(f"Razlika: {num1 - num2}")
print(f"Proizvod: {num1 * num2}")
if num2 != 0:
    print(f"Količnik: {num1 / num2:.4f}")
else:
    print("Količnik: Deljenje nulom!")
