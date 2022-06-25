#!/usr/bin/env python3
# Grupa5 / 07 / P1 â try/except

try: print(10 / 0)
except ZeroDivisionError: print("Deljenje nulom!")

try: int("xyz")
except ValueError as e: print(f"ValueError: {e}")

try: [1,2][9]
except IndexError: print("Index van opsega!")

try:
    r = 100 / 5
except ZeroDivisionError:
    print("GreÅ¡ka!")
else:
    print(f"OK: {r}")
finally:
    print("Finally.")