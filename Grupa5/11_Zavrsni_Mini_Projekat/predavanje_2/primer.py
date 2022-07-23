#!/usr/bin/env python3
# Grupa5 / 11 / P2 â Storage
import json, os

class ExpenseStorage:
    def __init__(self, path="data/expenses.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def ucitaj(self):
        if not os.path.exists(self.path): return []
        with open(self.path, 'r', encoding='utf-8') as f: return json.load(f)

    def sacuvaj(self, d):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

    def dodaj(self, t):
        data = self.ucitaj()
        data.append(t)
        self.sacuvaj(data)
        return len(data)

    def obrisi(self, i):
        data = self.ucitaj()
        if 0 <= i < len(data):
            o = data.pop(i)
            self.sacuvaj(data)
            return o
        return None

st = ExpenseStorage('data/test_exp.json')
st.dodaj({"iznos": 500, "kat": "Hrana", "opis": "test", "datum": "01.01"})
print(f"Count: {len(st.ucitaj())}")
st.obrisi(0)
os.remove('data/test_exp.json')
print("OK")