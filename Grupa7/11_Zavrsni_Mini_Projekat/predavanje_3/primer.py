#!/usr/bin/env python3
# âââââââââââââââââââââââââââââââââââââââ
# Å KOLICA â Grupa7: TRAVEL PLANNER CLI
# âââââââââââââââââââââââââââââââââââââââ
import json, os, datetime

class Trip:
    def __init__(self, dest, km, cena, datum=""):
        self.dest = dest
        self.km = km
        self.cena = cena
        self.datum = datum or datetime.date.today().strftime("%d.%m.%Y")
        self.done = False
    def to_dict(self):
        return {"dest": self.dest, "km": self.km, "cena": self.cena, "datum": self.datum, "done": self.done}

class Storage:
    def __init__(self, path="data/trips.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
    def ucitaj(self):
        if not os.path.exists(self.path): return []
        with open(self.path, 'r', encoding='utf-8') as f: return json.load(f)
    def sacuvaj(self, d):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

def meni():
    print("\n" + "=" * 48)
    print("  âï¸  TRAVEL PLANNER â Grupa7")
    print("=" * 48)
    print("  1. Dodaj destinaciju")
    print("  2. PrikaÅ¾i plan")
    print("  3. OznaÄi poseÄenu")
    print("  4. ObriÅ¡i")
    print("  5. Statistika")
    print("  6. Izlaz")
    print("-" * 48)

def dodaj(st):
    dest = input("  Destinacija: ").strip()
    if not dest: print("  Prazno!"); return
    try:
        km = int(input("  Udaljenost (km): "))
        cena = float(input("  Cena (EUR): "))
    except ValueError:
        print("  Neispravan unos!"); return
    data = st.ucitaj()
    data.append(Trip(dest, km, cena).to_dict())
    st.sacuvaj(data)
    print(f"  Dodato: {dest}")

def prikazi(st):
    data = st.ucitaj()
    if not data: print("\n  Nema destinacija."); return
    print(f"\n  Plan ({len(data)} dest):")
    for i, t in enumerate(data):
        st_icon = "Done" if t["done"] else "Plan"
        print(f"  {i+1}. [{st_icon}] {t['dest']} â {t['km']}km, {t['cena']}EUR ({t['datum']})")

def poseti(st):
    prikazi(st)
    data = st.ucitaj()
    if not data: return
    try:
        rb = int(input("  Broj: ")) - 1
        if 0 <= rb < len(data):
            data[rb]["done"] = True
            st.sacuvaj(data)
            print(f"  PoseÄena: {data[rb]['dest']}")
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
            print(f"  Obrisano: {o['dest']}")
    except ValueError: print("  Neispravan unos")

def stats(st):
    data = st.ucitaj()
    if not data: print("  Nema podataka."); return
    ukupno_km = sum(t["km"] for t in data)
    ukupno_eur = sum(t["cena"] for t in data)
    done = sum(1 for t in data if t["done"])
    print(f"\n  Destinacija: {len(data)}")
    print(f"  PoseÄene: {done}/{len(data)}")
    print(f"  Ukupno km: {ukupno_km:,}")
    print(f"  Ukupno EUR: {ukupno_eur:,.2f}")
    if data: print(f"  Prosek EUR: {ukupno_eur/len(data):,.2f}")

def main():
    st = Storage()
    while True:
        meni()
        c = input("  Izbor: ").strip()
        if c == "1": dodaj(st)
        elif c == "2": prikazi(st)
        elif c == "3": poseti(st)
        elif c == "4": obrisi(st)
        elif c == "5": stats(st)
        elif c == "6": print("\n  DoviÄenja! â Grupa7"); break
        else: print("  Nepoznato.")

if __name__ == '__main__': main()