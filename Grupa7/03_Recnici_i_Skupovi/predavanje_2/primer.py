#!/usr/bin/env python3
# Grupa7 / 03 / P2 â Skupovi

posecene_2023 = {"Istanbul", "Rim", "BeÄ", "BudimpeÅ¡ta"}
posecene_2024 = {"Rim", "Pariz", "Istanbul", "Barcelona"}

print("=== Set operacije ===")
print(f"2023: {posecene_2023}")
print(f"2024: {posecene_2024}")
print(f"Obe god: {posecene_2023 & posecene_2024}")
print(f"Ukupno: {posecene_2023 | posecene_2024}")
print(f"Samo 2023: {posecene_2023 - posecene_2024}")
print(f"Samo 2024: {posecene_2024 - posecene_2023}")

kupovine = ["suvenir","karta","suvenir","mapa","karta"]
print(f"\nBez duplikata: {list(set(kupovine))}")