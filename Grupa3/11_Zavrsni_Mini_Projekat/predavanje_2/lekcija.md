# Predavanje 2 — Storage Modul i CRUD Operacije

## 2.1 Storage Pattern

Razdvajanje logike čuvanja podataka od poslovne logike:

```python
class Storage:
    def ucitaj(self) -> list
    def sacuvaj(self, podaci: list)
    def dodaj(self, kontakt)
    def obrisi(self, email)
    def pretrazi(self, upit)
```

## 2.2 JSON Persistencija

Podaci se čuvaju u JSON fajlu između pokretanja programa.

## Rezime
- Storage klasa enkapsulira čitanje/pisanje
- CRUD: Create, Read, Update, Delete
- Validacija pre čuvanja
