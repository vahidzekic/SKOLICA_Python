#!/usr/bin/env python3
# Grupa4 / 11 / P2 â Storage
import json, os

class TodoStorage:
    def __init__(self, path="data/todos.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def ucitaj(self):
        if not os.path.exists(self.path): return []
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def sacuvaj(self, data):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def dodaj(self, d):
        z = self.ucitaj()
        z.append(d)
        self.sacuvaj(z)
        return len(z)

    def obrisi(self, i):
        z = self.ucitaj()
        if 0 <= i < len(z):
            o = z.pop(i)
            self.sacuvaj(z)
            return o
        return None

st = TodoStorage('data/test_todos.json')
st.dodaj({"naslov": "Test", "prioritet": "visok", "zavrsen": False, "kreiran": "01.01"})
print(f"Count: {len(st.ucitaj())}")
st.obrisi(0)
print(f"After del: {len(st.ucitaj())}")
os.remove('data/test_todos.json')
print("OK")