# Predavanje 3 — WHILE Petlja i Obrasci

## 3.1 WHILE petlja

```python
i = 0
while i < 10:
    print(i)
    i += 1     # BEZ OVOGA → beskonačna petlja!
```

## 3.2 WHILE...ELSE

```python
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Petlja završena normalno")
```

> `else` blok se NE izvršava ako je petlja prekinuta sa `break`.

## 3.3 Obrasci sa petljama

### Sentinel petlja (čeka signal za prekid):
```python
while True:
    unos = input("Komanda (q za izlaz): ")
    if unos == "q":
        break
    print(f"Izvršavam: {unos}")
```

### Akumulator obrazac:
```python
suma = 0
for x in brojevi:
    suma += x
```

## Rezime
- `while uslov:` — ponavlja dok je uslov True
- Uvek osigurati izlaz iz petlje (inkrement ili break)
- `while True` + `break` za sentinel petlje
