# Predavanje 3 — Praktičan Rad sa Javnim API-jem

## 3.1 Rad sa query parametrima

```python
params = {"q": "python", "page": 1, "per_page": 10}
response = requests.get(url, params=params)
```

## 3.2 Session objekat

Za višestruke zahteve sa istim podešavanjima:

```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer TOKEN"})
r1 = session.get(url1)
r2 = session.get(url2)
```

## 3.3 Timeout i Retry

```python
try:
    response = requests.get(url, timeout=5)
except requests.Timeout:
    print("Zahtev je istekao!")
except requests.ConnectionError:
    print("Nema konekcije!")
```

## Rezime
- `params={}` za query parametre
- `Session()` za ponovljene zahteve
- `timeout=` za sprečavanje beskonačnog čekanja
