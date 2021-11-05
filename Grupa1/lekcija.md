# Grupa 1 — Osnove Python Programskog Jezika

## 1.1 Uvod u Python

Python je programski jezik visokog nivoa koji je 1991. godine kreirao **Guido van Rossum**. Dizajniran je sa ciljem da bude čitljiv, jednostavan i efikasan. Python je **interpretirani** jezik — to znači da se kod izvršava liniju po liniju, bez prethodne kompilacije u mašinski kod (za razliku od jezika poput C-a).

### Ključne karakteristike Python-a:
- **Dinamičko tipiziranje** — ne morate eksplicitno deklarisati tip varijable.
- **Čista sintaksa** — indentacija (uvlačenje koda) je obavezna i zamenjuje vitičaste zagrade `{}`.
- **Bogata standardna biblioteka** — ugrađeni moduli za rad sa fajlovima, mrežom, matematikom itd.
- **Multi-paradigmatski** — podržava proceduralno, objektno-orijentisano i funkcionalno programiranje.

---

## 1.2 Varijable i dodela vrednosti

Varijabla je **imenovana lokacija u memoriji** koja čuva neku vrednost. U Python-u varijablu kreirate prostom dodelom:

```python
ime = "Vahid"        # string (tekst)
godine = 34          # integer (ceo broj)
visina = 1.82        # float (decimalni broj)
aktivan = True       # boolean (logička vrednost)
```

### Pravila za imenovanje varijabli:
| Pravilo | Primer (ispravno) | Primer (neispravno) |
|---|---|---|
| Počinje slovom ili `_` | `moj_broj` | `1broj` |
| Ne sme sadržati razmake | `prvi_broj` | `prvi broj` |
| Razlikuje velika/mala slova | `Ime` ≠ `ime` | — |
| Ne sme biti rezervisana reč | `rezultat` | `print`, `for` |

### Višestruka dodela:
Python dozvoljava dodelu više varijabli u jednoj liniji:
```python
x, y, z = 1, 2, 3
a = b = c = 0
```

---

## 1.3 Funkcija `print()`

Funkcija `print()` ispisuje sadržaj na konzolu (standardni izlaz). To je najosnovniji alat za komunikaciju programa sa korisnikom.

```python
print("Zdravo, svete!")           # Ispisuje string
print(42)                         # Ispisuje broj
print("Rezultat:", 10 + 5)        # Više argumenata, odvojenih zarezom
```

### Konkatenacija stringova:
Za spajanje teksta sa brojevima koristimo `str()` konverziju:
```python
ime = "Vahid"
godine = 34
print("Ime: " + ime + ", godine: " + str(godine))
```

---

## 1.4 Aritmetičke operacije

Python podržava standardne matematičke operacije:

| Operator | Operacija | Primer | Rezultat |
|---|---|---|---|
| `+` | Sabiranje | `11 + 7` | `18` |
| `-` | Oduzimanje | `11 - 7` | `4` |
| `*` | Množenje | `11 * 7` | `77` |
| `/` | Deljenje | `11 / 7` | `1.571...` |
| `//` | Celobrojno deljenje | `11 // 7` | `1` |
| `%` | Ostatak deljenja (modulo) | `11 % 7` | `4` |
| `**` | Stepenovanje | `2 ** 3` | `8` |

### Redosled operacija (PEMDAS):
Python poštuje matematički prioritet: zagrade → stepenovanje → množenje/deljenje → sabiranje/oduzimanje.

---

## 1.5 Komentari

Komentari služe za dokumentovanje koda i ignorišu se prilikom izvršavanja:

```python
# Ovo je jednolinijski komentar

"""
Ovo je višelinijski komentar
(zapravo je string literal koji nije dodeljen varijabli)
"""
```

---

## 1.6 Funkcija `input()`

Za čitanje korisničkog unosa sa tastature koristimo `input()`:

```python
ime = input("Unesite vaše ime: ")
broj = int(input("Unesite broj: "))  # Konvertujemo string u int
```

> **Napomena:** `input()` uvek vraća **string**. Za matematičke operacije moramo konvertovati u `int()` ili `float()`.

---

## Rezime Grupe 1

| Koncept | Opis |
|---|---|
| Varijable | Imenovane memorijske lokacije (`x = 5`) |
| `print()` | Ispis na konzolu |
| `input()` | Čitanje korisničkog unosa |
| Aritmetika | `+ - * / // % **` |
| Komentari | `#` jednolinijski, `"""` višelinijski |
| Tipovi | `int`, `float`, `str`, `bool` |
