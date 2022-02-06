# Predavanje 2 — Grupe, Lookahead i Praktični Obrasci

## 2.1 Grupe

```python
m = re.search(r"(\w+)@(\w+)\.(\w+)", email)
m.group(0)  # Ceo match
m.group(1)  # Korisničko ime
m.group(2)  # Domen
```

## 2.2 Imenovane grupe

```python
m = re.search(r"(?P<ime>\w+) (?P<prezime>\w+)", tekst)
print(m.group("ime"))
```

## 2.3 Korisni obrasci

| Obrazac | Opis |
|---|---|
| `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` | Email |
| `^\+?[0-9]{10,15}$` | Telefon |
| `^(?=.*[A-Z])(?=.*\d).{8,}$` | Jaka lozinka |

## Rezime
- `()` za grupe, `(?P<ime>)` za imenovane
- Lookahead: `(?=...)` pozitivan, `(?!...)` negativan
- Koristiti raw stringove: `r"obrazac"`
