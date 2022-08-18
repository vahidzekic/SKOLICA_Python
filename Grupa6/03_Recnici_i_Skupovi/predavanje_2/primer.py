#!/usr/bin/env python3
# Grupa6 / 03 / P2 â Skupovi

rock = {"Queen", "Beatles", "Nirvana", "Radiohead"}
pop = {"Beatles", "ABBA", "Queen", "Madonna"}

print("=== Set operacije ===")
print(f"Rock: {rock}")
print(f"Pop: {pop}")
print(f"Oba: {rock & pop}")
print(f"Svi: {rock | pop}")
print(f"Samo Rock: {rock - pop}")

zanrovi = ["rock", "pop", "rock", "jazz", "pop", "blues", "jazz"]
print(f"\nBez duplikata: {list(set(zanrovi))}")

ext_ok = {".mp3", ".wav", ".flac", ".aac"}
fajl = "pesma.mp3"
print(f"'{fajl}' OK: {'.'+fajl.split('.')[-1] in ext_ok}")