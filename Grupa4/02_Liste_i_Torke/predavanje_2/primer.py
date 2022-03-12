#!/usr/bin/env python3
# Grupa4 / 02 / Predavanje 2 — Comprehension, enumerate, zip

# Comprehension
print("=== Comprehension ===")
kubovi = [x**3 for x in range(1, 11)]
print(f"Kubovi: {kubovi}")
deljivi = [x for x in range(1, 31) if x % 3 == 0]
print(f"Deljivi sa 3: {deljivi}")
reci = ["python", "java", "go"]
velika = [r.upper() for r in reci]
print(f"Upper: {velika}")
print("")

# enumerate
print("=== enumerate() ===")
predmeti = ["Matematika", "Fizika", "Hemija", "Informatika"]
for rb, p in enumerate(predmeti, 1):
    print(f"  {rb}. {p}")
print("")

# zip
print("=== zip() ===")
studenti = ["Enes", "Kemo", "Ahmed"]
proseci = [8.7, 9.1, 7.5]
for s, p in zip(studenti, proseci):
    print(f"  {'*' if p >= 9 else ' '} {s}: {p}")
print("")

# Matrica
print("=== Matrica ===")
m = [[1,2,3],[4,5,6],[7,8,9]]
for red in m:
    print(f"  {red}")
flat = [el for red in m for el in red]
print(f"Flat: {flat}")
