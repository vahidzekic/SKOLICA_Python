# Predavanje 1 — Rečnici (Dictionaries)

## 1.1 Šta je rečnik?

Rečnik (`dict`) čuva podatke u **ključ-vrednost** parovima. Ključevi moraju biti jedinstveni i nepromenljivi (str, int, tuple).

```python
osoba = {"ime": "Vahid", "prezime": "Zekic", "godine": 34}
```

## 1.2 CRUD Operacije

| Operacija | Sintaksa |
|---|---|
| Čitanje | `d["ključ"]` ili `d.get("ključ", default)` |
| Kreiranje/Izmena | `d["novi_ključ"] = vrednost` |
| Brisanje | `del d["ključ"]` ili `d.pop("ključ")` |
| Provera | `"ključ" in d` |

## 1.3 Metode rečnika

| Metoda | Opis |
|---|---|
| `d.keys()` | Svi ključevi |
| `d.values()` | Sve vrednosti |
| `d.items()` | Svi parovi (ključ, vrednost) |
| `d.update(d2)` | Spaja dva rečnika |
| `d.get(k, default)` | Bezbedno čitanje |

## Rezime
- Rečnik: `{}`, neuređen (Python 3.7+ čuva redosled), ključevi jedinstveni
- `.get()` za bezbedno čitanje bez KeyError-a
- `.items()` za iteraciju kroz parove
