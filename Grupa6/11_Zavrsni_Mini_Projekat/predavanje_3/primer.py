#!/usr/bin/env python3
# âââââââââââââââââââââââââââââââââââââââ
# Å KOLICA â Grupa6: QUIZ GAME CLI
# âââââââââââââââââââââââââââââââââââââââ
import json, os, random

class Pitanje:
    def __init__(self, tekst, opcije, tacan, kat="OpÅ¡te"):
        self.tekst = tekst
        self.opcije = opcije
        self.tacan = tacan
        self.kat = kat
    def to_dict(self):
        return {"tekst": self.tekst, "opcije": self.opcije, "tacan": self.tacan, "kat": self.kat}
    @classmethod
    def from_dict(cls, d):
        return cls(d["tekst"], d["opcije"], d["tacan"], d.get("kat","OpÅ¡te"))

class Storage:
    def __init__(self, path="data/quiz.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
    def ucitaj(self):
        if not os.path.exists(self.path):
            self._init_default()
        with open(self.path, 'r', encoding='utf-8') as f: return json.load(f)
    def sacuvaj(self, d):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
    def _init_default(self):
        defaults = [
            {"tekst": "Koji bend je napisao 'Bohemian Rhapsody'?", "opcije": ["Beatles", "Queen", "Zeppelin", "Floyd"], "tacan": 1, "kat": "Muzika"},
            {"tekst": "Koliko nota ima u oktavi?", "opcije": ["5", "7", "8", "12"], "tacan": 2, "kat": "Muzika"},
            {"tekst": "Ko je napisao '1984'?", "opcije": ["Huxley", "Orwell", "Bradbury", "Asimov"], "tacan": 1, "kat": "Knjige"},
            {"tekst": "Glavna nota orkestra za Å¡timovanje?", "opcije": ["C", "D", "A", "E"], "tacan": 2, "kat": "Muzika"},
            {"tekst": "Koji instrument ima 88 dirki?", "opcije": ["Gitara", "Klavir", "Violina", "Flauta"], "tacan": 1, "kat": "Muzika"},
        ]
        self.sacuvaj(defaults)

def meni():
    print("\n" + "=" * 45)
    print("  ð¯ QUIZ GAME â Grupa6")
    print("=" * 45)
    print("  1. Igraj kviz")
    print("  2. Dodaj pitanje")
    print("  3. PrikaÅ¾i sva pitanja")
    print("  4. Statistika")
    print("  5. Izlaz")
    print("-" * 45)

def igraj(st):
    pitanja = st.ucitaj()
    if len(pitanja) < 3:
        print("  Premalo pitanja (min 3)!"); return 0, 0
    izabrana = random.sample(pitanja, min(5, len(pitanja)))
    tacni = 0
    for rb, pd in enumerate(izabrana, 1):
        p = Pitanje.from_dict(pd)
        print(f"\n  Pitanje {rb}/{len(izabrana)} [{p.kat}]")
        print(f"  {p.tekst}")
        for i, o in enumerate(p.opcije):
            print(f"    {chr(65+i)}. {o}")
        odg = input("  Tvoj odgovor (A/B/C/D): ").strip().upper()
        idx = ord(odg) - 65 if odg in "ABCD" else -1
        if p.tacan == idx:
            print("  TaÄno!")
            tacni += 1
        else:
            print(f"  NetaÄno! TaÄan: {chr(65+p.tacan)}. {p.opcije[p.tacan]}")
    print(f"\n  Rezultat: {tacni}/{len(izabrana)} ({tacni/len(izabrana)*100:.0f}%)")
    return tacni, len(izabrana)

def dodaj_pitanje(st):
    tekst = input("  Pitanje: ").strip()
    if not tekst: print("  Prazno!"); return
    opcije = []
    for i in range(4):
        o = input(f"  Opcija {chr(65+i)}: ").strip()
        if o: opcije.append(o)
    if len(opcije) < 2: print("  Min 2 opcije!"); return
    try:
        tacan = int(input("  TaÄan odgovor (0-based indeks): "))
    except ValueError: tacan = 0
    kat = input("  Kategorija: ").strip() or "OpÅ¡te"
    data = st.ucitaj()
    data.append(Pitanje(tekst, opcije, tacan, kat).to_dict())
    st.sacuvaj(data)
    print("  Dodato!")

def prikazi(st):
    data = st.ucitaj()
    if not data: print("  Nema pitanja."); return
    for i, p in enumerate(data):
        print(f"  {i+1}. [{p.get('kat','?')}] {p['tekst']}")

def main():
    st = Storage()
    total_t, total_p = 0, 0
    while True:
        meni()
        c = input("  Izbor: ").strip()
        if c == "1":
            t, p = igraj(st)
            total_t += t; total_p += p
        elif c == "2": dodaj_pitanje(st)
        elif c == "3": prikazi(st)
        elif c == "4":
            print(f"\n  Ukupno taÄnih: {total_t}/{total_p}")
            if total_p: print(f"  Procenat: {total_t/total_p*100:.0f}%")
        elif c == "5": print("\n  DoviÄenja! â Grupa6"); break
        else: print("  Nepoznato.")

if __name__ == '__main__': main()