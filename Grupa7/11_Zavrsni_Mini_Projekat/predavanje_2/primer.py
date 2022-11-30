#!/usr/bin/env python3
# Grupa7 / 11 / P2 â Storage
import json, os

class TripStorage:
    def __init__(self, path="data/trips.json"):
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
            data.pop(i)
            self.sacuvaj(data)
            return True
        return False

st = TripStorage('data/test_trips.json')
st.dodaj({"dest": "Test", "km": 100, "cena": 50, "datum": "01.01", "posecena": False})
print(f"Count: {len(st.ucitaj())}")
st.obrisi(0)
os.remove('data/test_trips.json')
print("OK")