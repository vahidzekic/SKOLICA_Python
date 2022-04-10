#!/usr/bin/env python3
# Grupa4 / 07 / P1 â try/except

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Deljenje nulom!")

try:
    int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

try:
    [1,2][5]
except IndexError:
    print("Index van opsega!")

try:
    rez = 100 / 4
except ZeroDivisionError:
    print("GreÅ¡ka!")
else:
    print(f"OK: {rez}")
finally:
    print("Finally.")