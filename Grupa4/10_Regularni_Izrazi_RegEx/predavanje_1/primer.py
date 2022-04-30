#!/usr/bin/env python3
# Grupa4 / 10 / P1 â re osnove
import re

tekst = "Pozovite 011-222-3333 ili 065-999-8888."

print("=== search ===")
m = re.search(r"\d{3}-\d{3}-\d{4}", tekst)
if m: print(f"  PronaÄen: {m.group()}")

print("\n=== findall ===")
svi = re.findall(r"\d{3}-\d{3}-\d{4}", tekst)
print(f"  Svi: {svi}")

print("\n=== sub ===")
cenz = re.sub(r"\d{3}-\d{3}-\d{4}", "[SKRIVENO]", tekst)
print(f"  {cenz}")

print("\n=== split ===")
csv = "Vahid;Zekic,34|NP"
print(f"  {re.split(r'[;,|]', csv)}")

print("\n=== Brojevi ===")
t2 = "Cena 150 din, popust 20%"
print(f"  {re.findall(r'\d+', t2)}")