#!/usr/bin/env python3
# Grupa5 / 05 / P1 â Funkcije

def pozdrav(ime, pozdrav_rec="Zdravo"):
    return f"{pozdrav_rec}, {ime}!"

def bmi(tezina, visina):
    return round(tezina / visina**2, 1)

def statistika(*nums):
    if not nums: return {}
    return {"min": min(nums), "max": max(nums), "avg": round(sum(nums)/len(nums), 2)}

def profil(**kw):
    for k, v in kw.items():
        print(f"  {k}: {v}")

print(pozdrav("Vahid"))
print(f"BMI: {bmi(80, 1.82)}")
print(f"Stats: {statistika(4, 8, 15, 16, 23, 42)}")
print("\nProfil:")
profil(ime="Vahid", sport="Fudbal", tim="Partizan")