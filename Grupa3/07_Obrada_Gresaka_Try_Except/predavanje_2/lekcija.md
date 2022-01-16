# Predavanje 2 — Podizanje i Kreiranje Izuzetaka

## 2.1 raise — Ručno podizanje izuzetka

```python
def podeli(a, b):
    if b == 0:
        raise ValueError("Delilac ne sme biti nula!")
    return a / b
```

## 2.2 Sopstveni izuzeci

```python
class NedovoljnoSredstava(Exception):
    def __init__(self, stanje, iznos):
        self.stanje = stanje
        self.iznos = iznos
        super().__init__(f"Stanje {stanje}, traženo {iznos}")
```

## 2.3 assert — Provera pretpostavki

```python
assert x > 0, "x mora biti pozitivan"
# Baca AssertionError ako je uslov False
```

## Rezime
- `raise` za ručno bacanje izuzetaka
- Sopstveni izuzeci nasleđuju `Exception`
- `assert` za debug-provere (onemogućiti sa `python -O`)
