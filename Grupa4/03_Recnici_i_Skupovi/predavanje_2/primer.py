#!/usr/bin/env python3
# Grupa4 / 03 / P2 â Skupovi

backend = {"Python", "Java", "Go", "Rust"}
frontend = {"JavaScript", "TypeScript", "Python", "Go"}

print("=== Operacije ===")
print(f"Backend: {backend}")
print(f"Frontend: {frontend}")
print(f"Unija: {backend | frontend}")
print(f"Presek: {backend & frontend}")
print(f"Samo backend: {backend - frontend}")

# Duplikati
kupovine = ["mleko","hleb","mleko","jaja","hleb"]
print(f"\nBez duplikata: {list(set(kupovine))}")