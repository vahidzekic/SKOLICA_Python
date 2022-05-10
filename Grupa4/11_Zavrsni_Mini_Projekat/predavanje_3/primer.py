#!/usr/bin/env python3
# âââââââââââââââââââââââââââââââââââââââââââ
# Å KOLICA â Grupa4: TODO MANAGER CLI
# âââââââââââââââââââââââââââââââââââââââââââ
import json, os, datetime

class Zadatak:
    def __init__(self, naslov, prioritet="srednji"):
        self.naslov = naslov
        self.prioritet = prioritet
        self.zavrsen = False
        self.kreiran = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    def to_dict(self):
        return {"naslov": self.naslov, "prioritet": self.prioritet,
                "zavrsen": self.zavrsen, "kreiran": self.kreiran}

class Storage:
    def __init__(self, path="data/todos.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
    def ucitaj(self):
        if not os.path.exists(self.path): return []
        with open(self.path, 'r', encoding='utf-8') as f: return json.load(f)
    def sacuvaj(self, d):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

def meni():
    print("\n" + "=" * 40)
    print("  TODO MANAGER â Grupa4")
    print("=" * 40)
    print("  1. Dodaj  2. PrikaÅ¾i  3. ZavrÅ¡i")
    print("  4. ObriÅ¡i 5. Stats    6. Izlaz")
    print("-" * 40)

def dodaj(st):
    n = input("  Naslov: ").strip()
    if not n: print("  Prazno!"); return
    p = input("  Prioritet (v/s/n): ").strip()
    p = {"v":"visok","s":"srednji","n":"nizak"}.get(p, "srednji")
    z = Zadatak(n, p)
    data = st.ucitaj()
    data.append(z.to_dict())
    st.sacuvaj(data)
    print(f"  Dodat: {n}")

def prikazi(st):
    data = st.ucitaj()
    if not data: print("\n  Nema zadataka."); return
    print(f"\n  Zadaci ({len(data)}):")
    for i, z in enumerate(data):
        s = "DONE" if z["zavrsen"] else "TODO"
        print(f"  {i+1}. [{s}] {z['naslov']} ({z['prioritet']})")

def zavrsi(st):
    prikazi(st)
    data = st.ucitaj()
    if not data: return
    try:
        rb = int(input("  Broj: ")) - 1
        if 0 <= rb < len(data):
            data[rb]["zavrsen"] = True
            st.sacuvaj(data)
            print(f"  ZavrÅ¡en: {data[rb]['naslov']}")
    except ValueError: print("  Neispravan unos")

def obrisi(st):
    prikazi(st)
    data = st.ucitaj()
    if not data: return
    try:
        rb = int(input("  Broj: ")) - 1
        if 0 <= rb < len(data):
            o = data.pop(rb)
            st.sacuvaj(data)
            print(f"  Obrisan: {o['naslov']}")
    except ValueError: print("  Neispravan unos")

def stats(st):
    data = st.ucitaj()
    uk = len(data)
    zav = sum(1 for z in data if z["zavrsen"])
    print(f"\n  Ukupno: {uk}, ZavrÅ¡eni: {zav}, Preostali: {uk-zav}")
    if uk: print(f"  Progres: {zav/uk*100:.0f}%")

def main():
    st = Storage()
    while True:
        meni()
        c = input("  Izbor: ").strip()
        if c == "1": dodaj(st)
        elif c == "2": prikazi(st)
        elif c == "3": zavrsi(st)
        elif c == "4": obrisi(st)
        elif c == "5": stats(st)
        elif c == "6": print("\n  DoviÄenja! â Grupa4"); break
        else: print("  Nepoznato.")

if __name__ == '__main__': main()