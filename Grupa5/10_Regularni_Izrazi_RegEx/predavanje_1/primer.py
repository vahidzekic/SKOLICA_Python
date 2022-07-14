#!/usr/bin/env python3
# Grupa5 / 10 / P1 â re osnove
import re

tekst = "Rezultat: Partizan 3-1 Zvezda, Vojvodina 2-2 ÄukariÄki."

print("=== search ===")
m = re.search(r"\d+-\d+", tekst)
if m: print(f"  Rezultat: {m.group()}")

print("\n=== findall ===")
svi = re.findall(r"\d+-\d+", tekst)
print(f"  Svi rezultati: {svi}")

print("\n=== sub ===")
cenz = re.sub(r"\d+-\d+", "[X-X]", tekst)
print(f"  {cenz}")

print("\n=== split ===")
csv = "JoviÄ;12,MitroviÄ;18|VlahoviÄ;24"
print(f"  {re.split(r'[;,|]', csv)}")