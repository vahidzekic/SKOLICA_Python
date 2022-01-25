# Predavanje 3 — Enkapsulacija i Specijalne Metode

## 3.1 Enkapsulacija

| Konvencija | Pristup |
|---|---|
| `self.atribut` | Javni (public) |
| `self._atribut` | Zaštićen (protected) — konvencija |
| `self.__atribut` | Privatni (name mangling) |

## 3.2 Property dekorator

```python
class Osoba:
    @property
    def puno_ime(self):
        return f"{self._ime} {self._prezime}"

    @puno_ime.setter
    def puno_ime(self, vrednost):
        self._ime, self._prezime = vrednost.split()
```

## 3.3 Specijalne (Dunder) metode

| Metoda | Poziv | Opis |
|---|---|---|
| `__str__` | `str(obj)` | String za korisnika |
| `__repr__` | `repr(obj)` | String za developera |
| `__len__` | `len(obj)` | Dužina |
| `__eq__` | `a == b` | Poređenje |
| `__lt__` | `a < b` | Manje od |

## Rezime
- `_` za protected, `__` za private
- `@property` za getter/setter
- Dunder metode za operator overloading
