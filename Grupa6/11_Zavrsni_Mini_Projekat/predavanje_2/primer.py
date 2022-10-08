#!/usr/bin/env python3
# Grupa6 / 11 / P2 â Storage
import json, os

class QuizStorage:
    def __init__(self, path="data/quiz.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def ucitaj(self):
        if not os.path.exists(self.path): return []
        with open(self.path, 'r', encoding='utf-8') as f: return json.load(f)

    def sacuvaj(self, d):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

    def dodaj(self, pitanje):
        data = self.ucitaj()
        data.append(pitanje)
        self.sacuvaj(data)
        return len(data)

    def obrisi(self, i):
        data = self.ucitaj()
        if 0 <= i < len(data):
            data.pop(i)
            self.sacuvaj(data)
            return True
        return False

st = QuizStorage('data/test_quiz.json')
st.dodaj({"tekst": "2+2?", "opcije": ["3","4","5"], "tacan": 1})
print(f"Count: {len(st.ucitaj())}")
st.obrisi(0)
os.remove('data/test_quiz.json')
print("OK")