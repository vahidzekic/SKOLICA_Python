#!/usr/bin/env python3
# ŠKOLICA Python — Grupa4 / 01 / Predavanje 2
# Tema: Promenljive, tipovi, konverzija, f-string

grad = "Novi Pazar"
drzava = "Srbija"
stanovnika = 100000
visina = 496.0
ima_uni = True

print("=== Info o gradu ===")
print(f"Grad: {grad}, {drzava}")
print(f"Stanovnika: {stanovnika:,}")
print(f"Nadmorska visina: {visina}m")
print(f"Ima univerzitet: {ima_uni}")
print("")

# Tipovi
print("=== type() ===")
print(f"'{grad}' -> {type(grad)}")
print(f"'{stanovnika}' -> {type(stanovnika)}")
print(f"'{visina}' -> {type(visina)}")
print(f"'{ima_uni}' -> {type(ima_uni)}")
print("")

# Konverzija
print("=== Konverzija ===")
t = "256"
print(f"str '{t}' -> int {int(t)} -> float {float(t)}")
print(f"bool(0)={bool(0)}, bool(1)={bool(1)}")
print(f"bool('')={bool('')}, bool('x')={bool('x')}")
print("")

# f-string
print("=== f-string ===")
pi = 3.141592653589793
print(f"PI na 2 dec: {pi:.2f}")
print(f"PI na 6 dec: {pi:.6f}")
cena = 1499.99
print(f"Cena: {cena:>10.2f} RSD")

# Swap
a, b = 10, 20
print(f"\nPre swap: a={a}, b={b}")
a, b = b, a
print(f"Posle swap: a={a}, b={b}")
