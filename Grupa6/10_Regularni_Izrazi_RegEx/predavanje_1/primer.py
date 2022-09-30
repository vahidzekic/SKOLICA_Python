#!/usr/bin/env python3
# Grupa6 / 10 / P1 â re osnove
import re

tekst = "Album 'Dark Side' (1973) i 'The Wall' (1979) od Pink Floyd."

print("=== search ===")
m = re.search(r"\d{4}", tekst)
if m: print(f"  Godina: {m.group()}")

print("\n=== findall ===")
sve_god = re.findall(r"\d{4}", tekst)
print(f"  Sve godine: {sve_god}")

print("\n=== sub ===")
cenz = re.sub(r"\d{4}", "[YYYY]", tekst)
print(f"  {cenz}")

print("\n=== split ===")
csv = "Beatles;Queen,Floyd|Nirvana"
print(f"  {re.split(r'[;,|]', csv)}")