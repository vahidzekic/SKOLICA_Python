#!/usr/bin/env python3
# âââââââââââââââââââââââââââââââââââââââ
# Å KOLICA â Grupa5: EXPENSE TRACKER CLI
# âââââââââââââââââââââââââââââââââââââââ
import json, os, datetime

class Trosak:
    def __init__(self, iznos, kat, opis=""):
        self.iznos = iznos
        self.kat = kat
        self.opis = opis
        self.datum = datetime.datetime.now().strftime("%d.%m.%Y")
    def to_dict(self):
        return {"iznos": self.iznos, "kat": self.kat, "opis": self.opis, "datum": self.datum}

class Storage:
    def __init__(self, path="data/expenses.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
    def ucitaj(self):
        if not os.path.exists(self.path): return []
        with open(self.path, 'r', encoding='utf-8') as f: return json.load(f)
    def sacuvaj(self, d):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

KATEGORIJE = ["Hrana", "Transport", "Zabava", "RaÄuni", "Ostalo"]

def meni():
    print("\n" + "=" * 45)
    print("  ð° EXPENSE TRACKER â Grupa5")
    print("=" * 45)
    print("  1. Dodaj troÅ¡ak")
    print("  2. PrikaÅ¾i sve")
    print("  3. Po kategorijama")
    print("  4. ObriÅ¡i")
    print("  5. Statistika")
    print("  6. Izlaz")
    print("-" * 45)

def dodaj(st):
    try:
        iznos = float(input("  Iznos (RSD): "))
    except ValueError:
        print("  Neispravan iznos!"); return
    print("  Kategorije:", ", ".join(f"{i+1}.{k}" for i,k in enumerate(KATEGORIJE)))
    try:
        ki = int(input("  Izbor: ")) - 1
        kat = KATEGORIJE[ki]
    except (ValueError, IndexError):
        kat = "Ostalo"
    opis = input("  Opis: ").strip()
    data = st.ucitaj()
    data.append(Trosak(iznos, kat, opis).to_dict())
    st.sacuvaj(data)
    print(f"  Dodato: {iznos:.2f} RSD ({kat})")

def prikazi(st):
    data = st.ucitaj()
    if not data: print("\n  Nema troÅ¡kova."); return
    print(f"\n  TroÅ¡kovi ({len(data)}):")
    for i, t in enumerate(data):
        print(f"  {i+1}. {t['datum']} | {t['kat']:12} | {t['iznos']:>8.2f} | {t.get('opis','')}" )

def po_kat(st):
    data = st.ucitaj()
    if not data: print("  Nema podataka."); return
    sume = {}
    for t in data:
        sume[t["kat"]] = sume.get(t["kat"], 0) + t["iznos"]
    print("\n  Po kategorijama:")
    for k, s in sorted(sume.items(), key=lambda x: x[1], reverse=True):
        print(f"  {k:12}: {s:>10.2f} RSD")

def obrisi(st):
    prikazi(st)
    data = st.ucitaj()
    if not data: return
    try:
        rb = int(input("  Broj: ")) - 1
        if 0 <= rb < len(data):
            o = data.pop(rb)
            st.sacuvaj(data)
            print(f"  Obrisano: {o['iznos']} ({o['kat']})")
    except ValueError: print("  Neispravan unos")

def stats(st):
    data = st.ucitaj()
    if not data: print("  Nema podataka."); return
    iznosi = [t["iznos"] for t in data]
    print(f"\n  Ukupno: {sum(iznosi):,.2f} RSD")
    print(f"  Prosek: {sum(iznosi)/len(iznosi):,.2f} RSD")
    print(f"  Min: {min(iznosi):,.2f}, Max: {max(iznosi):,.2f}")
    print(f"  Transakcija: {len(data)}")

def main():
    st = Storage()
    while True:
        meni()
        c = input("  Izbor: ").strip()
        if c == "1": dodaj(st)
        elif c == "2": prikazi(st)
        elif c == "3": po_kat(st)
        elif c == "4": obrisi(st)
        elif c == "5": stats(st)
        elif c == "6": print("\n  DoviÄenja! â Grupa5"); break
        else: print("  Nepoznato.")

if __name__ == '__main__': main()