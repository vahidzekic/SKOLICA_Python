#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 11_Zavrsni_Mini_Projekat / Predavanje 3
# Tema: KOMPLETNA CLI APLIKACIJA — Upravljač Kontaktima
# =============================================================================
import json
import os
import re


# ═══════════════════════════════════════════════════════════════════════════════
# MODEL
# ═══════════════════════════════════════════════════════════════════════════════

class Kontakt:
    def __init__(self, ime, prezime, email, telefon):
        self.ime = ime
        self.prezime = prezime
        self.email = self._val_email(email)
        self.telefon = self._val_telefon(telefon)

    @staticmethod
    def _val_email(email):
        if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.]+$", email):
            raise ValueError(f"Neispravan email: {email}")
        return email

    @staticmethod
    def _val_telefon(tel):
        cist = tel.replace(" ", "").replace("-", "")
        if not re.match(r"^\+?\d{9,15}$", cist):
            raise ValueError(f"Neispravan telefon: {tel}")
        return cist

    def to_dict(self):
        return {"ime": self.ime, "prezime": self.prezime,
                "email": self.email, "telefon": self.telefon}

    def __str__(self):
        return f"{self.ime} {self.prezime} | {self.email} | {self.telefon}"


# ═══════════════════════════════════════════════════════════════════════════════
# STORAGE
# ═══════════════════════════════════════════════════════════════════════════════

class Storage:
    def __init__(self, path="data/kontakti.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def ucitaj(self):
        if not os.path.exists(self.path):
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def sacuvaj(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


# ═══════════════════════════════════════════════════════════════════════════════
# CLI APLIKACIJA
# ═══════════════════════════════════════════════════════════════════════════════

def prikazi_meni():
    print("\n" + "═" * 50)
    print("  📇 UPRAVLJAČ KONTAKTIMA — ŠKOLICA Python")
    print("═" * 50)
    print("  1. Dodaj kontakt")
    print("  2. Prikaži sve kontakte")
    print("  3. Pretraži kontakte")
    print("  4. Obriši kontakt")
    print("  5. Izlaz")
    print("─" * 50)


def dodaj_kontakt(storage):
    print("\n--- Dodavanje kontakta ---")
    try:
        ime = input("  Ime: ").strip()
        prezime = input("  Prezime: ").strip()
        email = input("  Email: ").strip()
        telefon = input("  Telefon: ").strip()

        kontakt = Kontakt(ime, prezime, email, telefon)
        kontakti = storage.ucitaj()

        if any(k["email"] == email for k in kontakti):
            print("  ❌ Kontakt sa tim emailom već postoji!")
            return

        kontakti.append(kontakt.to_dict())
        storage.sacuvaj(kontakti)
        print(f"  ✅ Dodat: {kontakt}")
    except ValueError as e:
        print(f"  ❌ Greška validacije: {e}")


def prikazi_kontakte(storage):
    kontakti = storage.ucitaj()
    if not kontakti:
        print("\n  📭 Nema kontakata.")
        return
    print(f"\n--- Kontakti ({len(kontakti)}) ---")
    for i, k in enumerate(kontakti, 1):
        print(f"  {i}. {k['ime']} {k['prezime']} | "
              f"{k['email']} | {k['telefon']}")


def pretrazi_kontakte(storage):
    upit = input("\n  Pretraga: ").strip().lower()
    kontakti = storage.ucitaj()
    rezultati = [k for k in kontakti
                 if upit in k["ime"].lower()
                 or upit in k["prezime"].lower()
                 or upit in k["email"].lower()]

    if rezultati:
        print(f"  Pronađeno: {len(rezultati)}")
        for k in rezultati:
            print(f"    • {k['ime']} {k['prezime']} — {k['email']}")
    else:
        print("  Nema rezultata.")


def obrisi_kontakt(storage):
    email = input("\n  Email za brisanje: ").strip()
    kontakti = storage.ucitaj()
    nova = [k for k in kontakti if k["email"] != email]

    if len(nova) == len(kontakti):
        print("  ❌ Kontakt nije pronađen.")
    else:
        storage.sacuvaj(nova)
        print("  ✅ Kontakt obrisan.")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    storage = Storage()

    while True:
        prikazi_meni()
        izbor = input("  Vaš izbor (1-5): ").strip()

        if izbor == "1":
            dodaj_kontakt(storage)
        elif izbor == "2":
            prikazi_kontakte(storage)
        elif izbor == "3":
            pretrazi_kontakte(storage)
        elif izbor == "4":
            obrisi_kontakt(storage)
        elif izbor == "5":
            print("\n  👋 Doviđenja! ŠKOLICA Python — Grupa3")
            break
        else:
            print("  ⚠️ Nepoznat izbor. Pokušajte ponovo.")


if __name__ == "__main__":
    main()
