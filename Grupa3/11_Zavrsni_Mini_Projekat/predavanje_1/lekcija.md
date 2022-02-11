# Predavanje 1 — Planiranje CLI Aplikacije

## 1.1 Šta je CLI aplikacija?

CLI (Command Line Interface) aplikacija se pokreće iz terminala i koristi tekstualni unos/izlaz.

## 1.2 Projektni zadatak: Upravljač Kontaktima

Mini projekat koji integriše sve naučeno:
- **Klase** (OOP) za modelovanje kontakata
- **JSON** za persistenciju podataka
- **RegEx** za validaciju (email, telefon)
- **try/except** za robustnost
- **Petlje** za meni sistem

## 1.3 Arhitektura

```
kontakt_manager/
├── main.py         # Glavni program sa menijem
├── modeli.py       # Klasa Kontakt
├── storage.py      # JSON čitanje/pisanje
└── data/
    └── kontakti.json
```

## Rezime
- CLI = tekstualni interfejs u terminalu
- Podeliti kod u module (modeli, storage, main)
- Koristiti OOP za modelovanje podataka
