# Predavanje 1 — Uvod u API i HTTP

## 1.1 Šta je API?

API (Application Programming Interface) definiše kako softverske komponente komuniciraju.
REST API koristi HTTP metode: GET, POST, PUT, DELETE.

## 1.2 HTTP Metode

| Metoda | CRUD | Opis |
|---|---|---|
| GET | Read | Dohvata podatke |
| POST | Create | Šalje nove podatke |
| PUT | Update | Ažurira podatke |
| DELETE | Delete | Briše podatke |

## 1.3 HTTP Status Kodovi

| Kod | Značenje |
|---|---|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Server Error |

## 1.4 requests biblioteka

```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()
```

## Rezime
- REST API = HTTP metode + URL endpointi + JSON podaci
- `requests` biblioteka za slanje HTTP zahteva
- `.json()` za parsiranje JSON odgovora
