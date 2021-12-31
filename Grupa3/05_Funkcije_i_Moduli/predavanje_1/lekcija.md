# Predavanje 1 — Definicija i Pozivanje Funkcija

## 1.1 Šta je funkcija?

Funkcija je imenovani blok koda koji se može pozvati više puta. Funkcije omogućavaju **DRY** princip (Don't Repeat Yourself).

```python
def ime_funkcije(parametar1, parametar2):
    \"\"\"Docstring — opis funkcije.\"\"\"
    rezultat = parametar1 + parametar2
    return rezultat
```

## 1.2 Parametri i Argumenti

| Tip | Opis | Primer |
|---|---|---|
| Pozicioni | Po redosledu | `f(1, 2)` |
| Default | Podrazumevana vrednost | `def f(x=10):` |
| Keyword | Po imenu | `f(ime="Vahid")` |
| `*args` | Proizvoljno pozicionih | `def f(*args):` |
| `**kwargs` | Proizvoljno imenovanih | `def f(**kwargs):` |

## 1.3 Scope (domet) varijabli

- **Lokalna** — definisana unutar funkcije
- **Globalna** — definisana van funkcije
- **`global`** — ključna reč za pristup globalnoj iz funkcije

## Rezime
- `def` za definiciju, `return` za vraćanje vrednosti
- Docstring u trostrukim navodnicima
- Parametri: pozicioni, default, keyword, *args, **kwargs
