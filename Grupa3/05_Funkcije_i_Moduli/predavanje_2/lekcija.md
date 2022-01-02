# Predavanje 2 — Lambda, Map, Filter i Dekoratori

## 2.1 Lambda funkcije

Lambda je **anonimna** (bezimena) jednolinisjka funkcija:

```python
kvadrat = lambda x: x ** 2
saberi = lambda a, b: a + b
```

## 2.2 map() i filter()

```python
# map() — primenjuje funkciju na svaki element
brojevi = [1, 2, 3, 4, 5]
kvadrati = list(map(lambda x: x**2, brojevi))

# filter() — filtrira elemente po uslovu
parni = list(filter(lambda x: x % 2 == 0, brojevi))
```

## 2.3 Dekoratori

Dekorator je funkcija koja **obavija** drugu funkciju i dodaje joj funkcionalnost:

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def pozdrav(ime):
    return f"Zdravo, {ime}!"
```

## Rezime
- Lambda: `lambda parametri: izraz`
- `map()` transformiše, `filter()` filtrira
- Dekoratori: `@dekorator` iznad definicije funkcije
