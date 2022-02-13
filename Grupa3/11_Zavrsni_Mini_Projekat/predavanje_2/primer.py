#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 11_Zavrsni_Mini_Projekat / Predavanje 2
# Tema: Storage modul — JSON persistencija sa CRUD
# =============================================================================
import json
import os

class KontaktStorage:
    """JSON-based storage za kontakte."""

    def __init__(self, putanja="data/kontakti.json"):
        self.putanja = putanja
        os.makedirs(os.path.dirname(putanja), exist_ok=True)

    def ucitaj(self):
        if not os.path.exists(self.putanja):
            return []
        with open(self.putanja, "r", encoding="utf-8") as f:
            return json.load(f)

    def sacuvaj(self, kontakti):
        with open(self.putanja, "w", encoding="utf-8") as f:
            json.dump(kontakti, f, indent=4, ensure_ascii=False)

    def dodaj(self, kontakt_dict):
        kontakti = self.ucitaj()
        # Provera duplikata po emailu
        if any(k["email"] == kontakt_dict["email"] for k in kontakti):
            raise ValueError(f"Kontakt sa emailom {kontakt_dict['email']} već postoji!")
        kontakti.append(kontakt_dict)
        self.sacuvaj(kontakti)
        return kontakt_dict

    def obrisi(self, email):
        kontakti = self.ucitaj()
        nova_lista = [k for k in kontakti if k["email"] != email]
        if len(nova_lista) == len(kontakti):
            raise ValueError(f"Kontakt sa emailom {email} ne postoji!")
        self.sacuvaj(nova_lista)

    def pretrazi(self, upit):
        kontakti = self.ucitaj()
        upit = upit.lower()
        return [k for k in kontakti
                if upit in k["ime"].lower()
                or upit in k["prezime"].lower()
                or upit in k["email"].lower()]

# --- Test ---
if __name__ == "__main__":
    storage = KontaktStorage("data/test_kontakti.json")

    print("=== Test Storage ===\n")

    storage.dodaj({"ime": "Vahid", "prezime": "Zekic",
                    "email": "vahid@skolica.rs", "telefon": "+381651234567"})
    storage.dodaj({"ime": "Enes", "prezime": "Daca",
                    "email": "enes@skolica.rs", "telefon": "+381659876543"})
    print("✅ 2 kontakta dodato")

    kontakti = storage.ucitaj()
    for k in kontakti:
        print(f"  {k['ime']} {k['prezime']} — {k['email']}")

    rezultati = storage.pretrazi("vahid")
    print(f"\n  Pretraga 'vahid': {len(rezultati)} rezultat(a)")

    storage.obrisi("enes@skolica.rs")
    print("  ✅ Enes obrisan")
    print(f"  Preostalo: {len(storage.ucitaj())} kontakt(a)")

    # Čišćenje test fajla
    os.remove("data/test_kontakti.json")
