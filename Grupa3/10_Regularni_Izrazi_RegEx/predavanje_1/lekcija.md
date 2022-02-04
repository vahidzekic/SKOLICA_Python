# Predavanje 1 — Uvod u Regularne Izraze

## 1.1 Šta su regularni izrazi?

Regularni izraz (RegEx) je **obrazac za pretragu teksta**. Python koristi `re` modul.

## 1.2 Osnovni obrasci

| Obrazac | Značenje |
|---|---|
| `.` | Bilo koji karakter |
| `\d` | Cifra (0-9) |
| `\w` | Slovo, cifra ili `_` |
| `\s` | Razmak, tab, novi red |
| `^` | Početak stringa |
| `$` | Kraj stringa |
| `*` | 0 ili više ponavljanja |
| `+` | 1 ili više ponavljanja |
| `?` | 0 ili 1 ponavljanje |
| `{n}` | Tačno n ponavljanja |
| `[abc]` | Jedan od a, b, c |

## 1.3 re funkcije

| Funkcija | Opis |
|---|---|
| `re.search()` | Prva pojava u stringu |
| `re.match()` | Samo na početku |
| `re.findall()` | Sve pojave (lista) |
| `re.sub()` | Zamena |
| `re.split()` | Razdvajanje |

## Rezime
- `import re` za rad sa regex-om
- `r"obrazac"` — raw string za regex
- `re.findall()` najčešće korišćena funkcija
