# Grupa 7 — Flask REST API Backend

## 7.1 Šta je REST API?

**REST** (Representational State Transfer) je arhitekturni stil za dizajn mrežnih aplikacija. **API** (Application Programming Interface) je set pravila koji definiše kako aplikacije komuniciraju.

REST API koristi **HTTP metode** za upravljanje resursima (podacima):

| HTTP Metoda | Operacija | CRUD | Opis |
|---|---|---|---|
| `GET` | Čitanje | **R**ead | Dohvata podatke sa servera |
| `POST` | Kreiranje | **C**reate | Šalje nove podatke na server |
| `PUT` | Ažuriranje | **U**pdate | Menja postojeće podatke |
| `DELETE` | Brisanje | **D**elete | Briše podatke sa servera |

---

## 7.2 Flask Framework

**Flask** je lagani Python web framework za kreiranje web aplikacija i REST API-ja.

### Instalacija:
```bash
pip install flask flask-cors
```

### Minimalna Flask aplikacija:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def pocetna():
    return "Server je ONLINE"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Anatomija Flask aplikacije:

| Element | Opis |
|---|---|
| `Flask(__name__)` | Kreiranje Flask instance |
| `@app.route('/')` | Dekorator — definiše URL rutu |
| `methods=['GET']` | Dozvoljene HTTP metode za rutu |
| `jsonify()` | Konvertuje Python dict/list u JSON odgovor |
| `request.json` | Pristupa JSON podacima iz zahteva |
| `abort(404)` | Vraća HTTP grešku |

---

## 7.3 CORS (Cross-Origin Resource Sharing)

Kada JavaScript frontend (npr. na `localhost:3000`) poziva Flask backend (na `localhost:5000`), browser blokira zahtev iz bezbednosnih razloga. **CORS** dozvoljava ove zahteve:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)    # Dozvoljava zahteve sa svih origina
```

---

## 7.4 Rute i Endpointi

Svaka ruta mapira **URL putanju** na **Python funkciju**:

```python
# GET — Dohvata sve studente
@app.route('/api/studenti', methods=['GET'])
def dohvati_sve():
    return jsonify(studenti)

# GET — Dohvata studenta po ID-ju
@app.route('/api/studenti/<int:id>', methods=['GET'])
def dohvati_jednog(id):
    student = next((s for s in studenti if s['id'] == id), None)
    if student is None:
        abort(404)
    return jsonify(student)
```

### Dinamičke rute:

| Sintaksa | Tip | Primer URL-a |
|---|---|---|
| `<int:id>` | Ceo broj | `/api/studenti/1` |
| `<string:ime>` | Tekst | `/api/studenti/Vahid` |
| `<path:putanja>` | Putanja | `/fajlovi/dokumenti/test.pdf` |

---

## 7.5 JSON Persistencija

Za trajno čuvanje podataka, koristimo JSON fajl kao mini bazu:

```python
import json

# Čitanje
with open('baza.json', 'r') as f:
    podaci = json.load(f)

# Pisanje
with open('baza.json', 'w') as f:
    json.dump(podaci, f, indent=4)
```

---

## 7.6 Validacija zahteva

Svaki endpoint treba da validira ulazne podatke:

```python
@app.route('/api/studenti', methods=['POST'])
def kreiraj():
    if not request.json:
        abort(400)                  # Bad Request
    if 'ime' not in request.json:
        abort(400)

    student = {
        'id': request.json['id'],
        'ime': request.json['ime'],
        # ...
    }
    studenti.append(student)
    return jsonify(student), 201    # 201 Created
```

### HTTP Status kodovi:

| Kod | Značenje | Kada koristiti |
|---|---|---|
| `200` | OK | Uspešan GET/PUT |
| `201` | Created | Uspešan POST |
| `204` | No Content | Uspešan DELETE |
| `400` | Bad Request | Nevalidan zahtev |
| `404` | Not Found | Resurs ne postoji |
| `500` | Server Error | Interna greška servera |

---

## 7.7 Veza sa JavaScript Frontend-om

Ovo je **najvažnija cross-language veza** u ŠKOLICA Knowledge Graph-u:

```
┌─────────────────────┐         ┌─────────────────────┐
│  JavaScript Frontend│         │  Python Flask Backend│
│  (SKOLICA_JavaScript│────────>│  (SKOLICA_Python)    │
│   Grupa 7)          │  HTTP   │   Grupa 7)           │
│                     │<────────│                      │
│  fetch('localhost:  │  JSON   │  @app.route('/api/') │
│        5000/api/')  │         │  return jsonify(...)  │
└─────────────────────┘         └─────────────────────┘
```

JavaScript koristi `fetch()` API da pošalje HTTP zahteve:
```javascript
// JavaScript — GET zahtev
const odgovor = await fetch("http://localhost:5000/api/studenti");
const podaci = await odgovor.json();
```

Python Flask vraća JSON odgovor:
```python
# Python — Obrada GET zahteva
@app.route('/api/studenti')
def dohvati():
    return jsonify(studenti)
```

---

## 7.8 Pokretanje servera

```bash
# Pokretanje Flask servera
python primer.py

# Server dostupan na:
# http://localhost:5000
# http://0.0.0.0:5000 (pristupačan sa drugih uređaja u mreži)
```

### Testiranje sa cURL:
```bash
# GET
curl http://localhost:5000/api/studenti

# POST
curl -X POST -H "Content-Type: application/json" \
     -d '{"id": 5, "ime": "Test", "prezime": "Korisnik", "godine": 25}' \
     http://localhost:5000/api/studenti

# PUT
curl -X PUT -H "Content-Type: application/json" \
     -d '{"ime": "Novo Ime"}' \
     http://localhost:5000/api/studenti/1

# DELETE
curl -X DELETE http://localhost:5000/api/studenti/1
```

---

## Rezime Grupe 7

| Koncept | Opis |
|---|---|
| Flask | Python web framework |
| REST API | HTTP-bazirana komunikacija (GET/POST/PUT/DELETE) |
| `@app.route()` | Dekorator za definisanje endpointa |
| `jsonify()` | Python → JSON odgovor |
| `request.json` | Čita JSON iz HTTP zahteva |
| `CORS` | Dozvoljava cross-origin zahteve |
| `abort()` | Vraća HTTP grešku |

> **Veza sa Knowledge Graph-om:** Ovaj Flask backend je **server strana** Full-Stack REST API Ekosistema. JavaScript frontend (SKOLICA_JavaScript, Grupa 7) koristi `fetch()` da komunicira sa ovim endpointima.
