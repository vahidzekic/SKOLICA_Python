#!/usr/bin/env python3
# Grupa7 / 10 / P1 â re osnove
import re

tekst = "Let BEG-IST 15.07.2025 u 14:30, cena 199 EUR. Povratak 22.07.2025."

print("=== search ===")
m = re.search(r"\d{2}\.\d{2}\.\d{4}", tekst)
if m: print(f"  Datum: {m.group()}")

print("\n=== findall ===")
datumi = re.findall(r"\d{2}\.\d{2}\.\d{4}", tekst)
print(f"  Datumi: {datumi}")
broj = re.findall(r"\d+", tekst)
print(f"  Brojevi: {broj}")

print("\n=== sub ===")
cenz = re.sub(r"\d{2}\.\d{2}\.\d{4}", "[DATUM]", tekst)
print(f"  {cenz}")

print("\n=== split ===")
ruta = "BEG-IST-ATH-ROM"
print(f"  {re.split(r'-', ruta)}")