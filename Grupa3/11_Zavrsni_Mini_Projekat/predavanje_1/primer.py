#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa3 / 11_Zavrsni_Mini_Projekat / Predavanje 1
# Tema: Modul za model podataka — klasa Kontakt
# =============================================================================
import re

class Kontakt:
    """Model kontakta sa validacijom."""

    def __init__(self, ime, prezime, email, telefon):
        self.ime = ime
        self.prezime = prezime
        self.email = self._validiraj_email(email)
        self.telefon = self._validiraj_telefon(telefon)

    @staticmethod
    def _validiraj_email(email):
        obrazac = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(obrazac, email):
            raise ValueError(f"Neispravan email: {email}")
        return email

    @staticmethod
    def _validiraj_telefon(telefon):
        obrazac = r"^\+?[0-9]{9,15}$"
        cist = telefon.replace(" ", "").replace("-", "")
        if not re.match(obrazac, cist):
            raise ValueError(f"Neispravan telefon: {telefon}")
        return cist

    def to_dict(self):
        return {
            "ime": self.ime,
            "prezime": self.prezime,
            "email": self.email,
            "telefon": self.telefon
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["ime"], data["prezime"], data["email"], data["telefon"])

    def __str__(self):
        return f"{self.ime} {self.prezime} | 📧 {self.email} | 📱 {self.telefon}"

# --- Test ---
if __name__ == "__main__":
    print("=== Test klase Kontakt ===\n")
    try:
        k1 = Kontakt("Vahid", "Zekic", "vahid@skolica.rs", "+381651234567")
        print(f"  ✅ {k1}")
        print(f"  Dict: {k1.to_dict()}")
    except ValueError as e:
        print(f"  ❌ {e}")

    try:
        k2 = Kontakt("Test", "User", "invalid-email", "123")
    except ValueError as e:
        print(f"  ❌ Očekivana greška: {e}")
