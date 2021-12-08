# Predavanje 3 — Aritmetičke Operacije i Korisnički Unos

## 3.1 Aritmetički operatori

| Operator | Operacija | Primer | Rezultat |
|---|---|---|---|
| `+` | Sabiranje | `11 + 7` | `18` |
| `-` | Oduzimanje | `11 - 7` | `4` |
| `*` | Množenje | `11 * 7` | `77` |
| `/` | Deljenje | `11 / 7` | `1.571...` |
| `//` | Celobrojno deljenje | `11 // 7` | `1` |
| `%` | Modulo (ostatak) | `11 % 7` | `4` |
| `**` | Stepenovanje | `2 ** 10` | `1024` |

## 3.2 Operatori dodele

| Operator | Ekvivalent | Primer |
|---|---|---|
| `+=` | `x = x + 5` | `x += 5` |
| `-=` | `x = x - 5` | `x -= 5` |
| `*=` | `x = x * 5` | `x *= 5` |
| `/=` | `x = x / 5` | `x /= 5` |

## 3.3 Funkcija `input()`

`input()` čita tekst sa tastature. **Uvek vraća string!**

```python
ime = input("Unesite ime: ")
broj = int(input("Unesite broj: "))    # Konverzija u int
cena = float(input("Unesite cenu: "))  # Konverzija u float
```

## 3.4 Redosled operacija (PEMDAS)

1. **P**arentheses — Zagrade `()`
2. **E**xponents — Stepenovanje `**`
3. **M**ultiplication/**D**ivision — Množenje/Deljenje `* / // %`
4. **A**ddition/**S**ubtraction — Sabiranje/Oduzimanje `+ -`

## Rezime
- 7 aritmetičkih operatora: `+ - * / // % **`
- `input()` uvek vraća `str` — konvertovati sa `int()` ili `float()`
- Operatori dodele: `+= -= *= /=`
