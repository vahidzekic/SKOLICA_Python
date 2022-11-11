#!/usr/bin/env python3
# Grupa7 / 07 / P1 â try/except

try: print(10 / 0)
except ZeroDivisionError: print("Deljenje nulom!")

try: int("abc")
except ValueError as e: print(f"ValueError: {e}")

try: [1,2][9]
except IndexError: print("Index van opsega!")

try:
    r = 200 / 4
except ZeroDivisionError:
    print("GreÅ¡ka!")
else:
    print(f"OK: {r}")
finally:
    print("Finally.")