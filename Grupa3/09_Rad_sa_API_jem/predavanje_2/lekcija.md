# Predavanje 2 — POST, PUT, DELETE Zahtevi

## 2.1 POST — Kreiranje resursa

```python
data = {"title": "Novi post", "body": "Sadržaj", "userId": 1}
response = requests.post(url, json=data)
```

## 2.2 PUT — Ažuriranje resursa

```python
data = {"title": "Ažuriran naslov"}
response = requests.put(f"{url}/1", json=data)
```

## 2.3 DELETE — Brisanje resursa

```python
response = requests.delete(f"{url}/1")
```

## 2.4 Headers i Autentifikacija

```python
headers = {"Authorization": "Bearer TOKEN", "Content-Type": "application/json"}
response = requests.get(url, headers=headers)
```

## Rezime
- `requests.post(url, json=data)` za POST
- `requests.put(url, json=data)` za PUT
- `requests.delete(url)` za DELETE
- `json=` parametar automatski serijalizuje Python dict
