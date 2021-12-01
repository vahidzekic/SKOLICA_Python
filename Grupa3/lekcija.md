# Grupa 3 — Kontrolne Strukture (Uslovno Grananje)

## 3.1 Šta su kontrolne strukture?

Kontrolne strukture su konstrukti koji omogućavaju programu da **donosi odluke** na osnovu uslova. Bez njih, program bi se uvek izvršavao sekvencijalno — liniju po liniju, bez ikakvog grananja.

U Python-u postoje tri forme uslovnog grananja:
1. **`if`** — jednostavan uslov
2. **`if...else`** — uslov sa alternativom
3. **`if...elif...else`** — lanac više uslova

---

## 3.2 Operatori poređenja

Pre nego što koristimo uslove, moramo razumeti operatore poređenja:

| Operator | Značenje | Primer | Rezultat |
|---|---|---|---|
| `==` | Jednako | `5 == 5` | `True` |
| `!=` | Nije jednako | `5 != 3` | `True` |
| `<` | Manje od | `3 < 5` | `True` |
| `>` | Veće od | `5 > 3` | `True` |
| `<=` | Manje ili jednako | `5 <= 5` | `True` |
| `>=` | Veće ili jednako | `5 >= 3` | `True` |

### Logički operatori:

| Operator | Značenje | Primer |
|---|---|---|
| `and` | I (oba uslova moraju biti True) | `x > 0 and x < 100` |
| `or` | ILI (bar jedan uslov True) | `x < 0 or x > 100` |
| `not` | Negacija | `not True` → `False` |

---

## 3.3 IF — Jednostavan uslov

Blok koda unutar `if` se izvršava **samo ako je uslov True**:

```python
prviBroj = 89
drugiBroj = 100

if prviBroj < drugiBroj:
    print("Prvi broj je manji od drugog.")
```

> **Kritično:** Python koristi **indentaciju** (4 razmaka ili 1 tab) za definisanje bloka koda. Bez indentacije, Python javlja `IndentationError`.

---

## 3.4 IF...ELSE — Uslov sa alternativom

Kada želimo različito ponašanje za ispunjen i neispunjen uslov:

```python
if prviBroj < drugiBroj:
    print("Prvi je manji.")
else:
    print("Prvi je veći ili jednak.")
```

### Tok izvršavanja:
```
Uslov? ──True──> Blok IF
  │
  └──False──> Blok ELSE
```

---

## 3.5 IF...ELIF...ELSE — Lanac uslova

Za više od dva moguća scenarija koristimo `elif` (skraćeno od *else if*):

```python
if prviBroj < drugiBroj:
    print("Manji")
elif prviBroj == drugiBroj:
    print("Jednaki")
else:
    print("Veći")
```

### Tok izvršavanja:
```
Uslov 1? ──True──> Blok 1
  │
  └──False──> Uslov 2? ──True──> Blok 2
                  │
                  └──False──> Blok ELSE
```

> **Napomena:** Python čita uslove **odozgo nadole** i izvršava **samo prvi koji je ispunjen**.

---

## 3.6 Switch statement u Python-u

Za razliku od JavaScript-a i C-a, Python **nema** klasičan `switch-case` statement. Umesto toga, Python 3.10+ uvodi `match-case`:

```python
# Python 3.10+
match komanda:
    case "start":
        pokreni()
    case "stop":
        zaustavi()
    case _:
        print("Nepoznata komanda")
```

> U starijim verzijama Python-a, `switch` se simulira sa `if...elif...else` lancem ili rečnikom (dictionary dispatch).

---

## 3.7 Ugnežđeni uslovi (Nested If)

Uslove možemo ugnežđavati jedan unutar drugog:

```python
godine = 25
if godine >= 18:
    if godine >= 21:
        print("Punoletna osoba (21+)")
    else:
        print("Punoletna osoba (18-20)")
else:
    print("Maloletna osoba")
```

> **Savet:** Izbegavajte previše nivoa ugnežđavanja — korišćenje `elif` je čitljivije.

---

## Rezime Grupe 3

| Konstrukt | Kada koristiti |
|---|---|
| `if` | Jedna provera, jedno dejstvo |
| `if...else` | Dva moguća ishoda |
| `if...elif...else` | Tri ili više ishoda |
| `match...case` | Poređenje sa fiksnim vrednostima (Python 3.10+) |
