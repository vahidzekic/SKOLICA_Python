#!/usr/bin/env python3
# =============================================================================
# ŠKOLICA Python — Grupa 7: Flask REST API Backend
# Autor: dipl.inz. Vahid Zekic
# Opis: Kompletni REST API sa GET, POST, PUT, DELETE endpointima.
#       Ovaj backend komunicira sa JavaScript frontend-om (SKOLICA_JavaScript).
#
# Pokretanje: python primer.py
# Server:     http://localhost:5000
# =============================================================================

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json
import os
import platform
from datetime import datetime


# =============================================================================
# 1. INICIJALIZACIJA FLASK APLIKACIJE
# =============================================================================

mojaAplikacija = Flask(__name__)

# CORS — dozvoljava JavaScript frontend-u (npr. na localhost:8080)
# da šalje zahteve ovom backend-u (localhost:5000)
CORS(mojaAplikacija)

# Putanja do JSON baze podataka
BAZA_PUTANJA = os.path.join(os.path.dirname(__file__), 'baza.json')


# =============================================================================
# 2. POMOĆNE FUNKCIJE — Čitanje i pisanje JSON baze
# =============================================================================

def ucitaj_bazu():
    """Čita JSON fajl i vraća listu studenata."""
    if not os.path.exists(BAZA_PUTANJA):
        # Ako fajl ne postoji, kreiraj sa inicijalnim podacima
        inicijalni_podaci = [
            {"id": 1, "ime": "Vahid", "prezime": "Zekic",
             "godine": 34, "pol": "muski"},
            {"id": 2, "ime": "Omer", "prezime": "Ljajic",
             "godine": 34, "pol": "muski"},
            {"id": 3, "ime": "Kemo", "prezime": "Plojovic",
             "godine": 27, "pol": "muski"}
        ]
        sacuvaj_bazu(inicijalni_podaci)
        return inicijalni_podaci

    with open(BAZA_PUTANJA, 'r', encoding='utf-8') as fajl:
        return json.load(fajl)


def sacuvaj_bazu(podaci):
    """Čuva listu studenata u JSON fajl."""
    with open(BAZA_PUTANJA, 'w', encoding='utf-8') as fajl:
        json.dump(podaci, fajl, indent=4, ensure_ascii=False)


def sledeci_id(studenti):
    """Generiše sledeći slobodan ID."""
    if not studenti:
        return 1
    return max(s['id'] for s in studenti) + 1


# =============================================================================
# 3. RUTA: POČETNA — Status servera
# =============================================================================

@mojaAplikacija.route('/')
def status_servera():
    """
    GET /
    Vraća status servera sa informacijama o sistemu.
    """
    poruka = {
        "status": "ONLINE",
        "server": "ŠKOLICA Flask REST API",
        "verzija": "1.0.0",
        "platforma": platform.platform(),
        "hostname": platform.node(),
        "vreme": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "python_verzija": platform.python_version()
    }
    return jsonify(poruka)


# =============================================================================
# 4. RUTA: GET — Dohvatanje svih studenata
# =============================================================================

@mojaAplikacija.route('/api/studenti', methods=['GET'])
def dohvati_sve_studente():
    """
    GET /api/studenti
    Vraća JSON listu svih studenata iz baze.
    Ovo je endpoint koji JavaScript frontend poziva sa fetch().
    """
    studenti = ucitaj_bazu()
    return jsonify(studenti)


# =============================================================================
# 5. RUTA: GET po ID-ju — Dohvatanje jednog studenta
# =============================================================================

@mojaAplikacija.route('/api/studenti/<int:student_id>', methods=['GET'])
def dohvati_studenta(student_id):
    """
    GET /api/studenti/<id>
    Vraća jednog studenta po ID-ju.
    Vraća 404 ako student ne postoji.
    """
    studenti = ucitaj_bazu()
    student = next((s for s in studenti if s['id'] == student_id), None)

    if student is None:
        abort(404)

    return jsonify(student)


# =============================================================================
# 6. RUTA: POST — Kreiranje novog studenta
# =============================================================================

@mojaAplikacija.route('/api/studenti', methods=['POST'])
def kreiraj_studenta():
    """
    POST /api/studenti
    Kreira novog studenta.
    Zahteva JSON telo sa poljem 'ime'.
    Vraća 201 Created sa kreiranim studentom.

    Primer zahteva:
    {
        "ime": "Ahmed",
        "prezime": "Kavazovic",
        "godine": 26,
        "pol": "muski"
    }
    """
    # Validacija — zahtev mora sadržati JSON sa poljem 'ime'
    if not request.json or 'ime' not in request.json:
        abort(400)

    studenti = ucitaj_bazu()

    # Kreiranje novog studenta sa auto-generisanim ID-jem
    novi_student = {
        'id': sledeci_id(studenti),
        'ime': request.json['ime'],
        'prezime': request.json.get('prezime', ''),
        'godine': request.json.get('godine', 0),
        'pol': request.json.get('pol', '')
    }

    studenti.append(novi_student)
    sacuvaj_bazu(studenti)

    return jsonify(novi_student), 201


# =============================================================================
# 7. RUTA: PUT — Ažuriranje postojećeg studenta
# =============================================================================

@mojaAplikacija.route('/api/studenti/<int:student_id>', methods=['PUT'])
def azuriraj_studenta(student_id):
    """
    PUT /api/studenti/<id>
    Ažurira postojećeg studenta.
    Menja samo polja koja su prosleđena u zahtevu.
    Vraća 404 ako student ne postoji.

    Primer zahteva:
    {
        "ime": "Novo Ime",
        "godine": 35
    }
    """
    studenti = ucitaj_bazu()
    student = next((s for s in studenti if s['id'] == student_id), None)

    if student is None:
        abort(404)

    if not request.json:
        abort(400)

    # Ažuriramo samo prosleđena polja (parcijalno ažuriranje)
    student['ime'] = request.json.get('ime', student['ime'])
    student['prezime'] = request.json.get('prezime', student['prezime'])
    student['godine'] = request.json.get('godine', student['godine'])
    student['pol'] = request.json.get('pol', student['pol'])

    sacuvaj_bazu(studenti)

    return jsonify(student)


# =============================================================================
# 8. RUTA: DELETE po ID-ju — Brisanje studenta
# =============================================================================

@mojaAplikacija.route('/api/studenti/<int:student_id>', methods=['DELETE'])
def obrisi_studenta_po_id(student_id):
    """
    DELETE /api/studenti/<id>
    Briše studenta po ID-ju.
    Vraća 404 ako student ne postoji.
    """
    studenti = ucitaj_bazu()
    student = next((s for s in studenti if s['id'] == student_id), None)

    if student is None:
        abort(404)

    studenti.remove(student)
    sacuvaj_bazu(studenti)

    return jsonify({"poruka": f"Student '{student['ime']} {student['prezime']}' "
                              f"je uspešno obrisan.",
                    "obrisan": student}), 200


# =============================================================================
# 9. RUTA: DELETE po imenu — Brisanje studenta
# =============================================================================

@mojaAplikacija.route('/api/studenti/ime/<string:student_ime>', methods=['DELETE'])
def obrisi_studenta_po_imenu(student_ime):
    """
    DELETE /api/studenti/ime/<ime>
    Briše prvog studenta sa datim imenom.
    Vraća 404 ako student ne postoji.
    """
    studenti = ucitaj_bazu()
    student = next((s for s in studenti if s['ime'] == student_ime), None)

    if student is None:
        abort(404)

    studenti.remove(student)
    sacuvaj_bazu(studenti)

    return jsonify({"poruka": f"Student '{student_ime}' je obrisan."}), 200


# =============================================================================
# 10. ERROR HANDLERI — Prilagođene poruke grešaka
# =============================================================================

@mojaAplikacija.errorhandler(400)
def los_zahtev(error):
    """Prilagođen odgovor za 400 Bad Request."""
    return jsonify({"greska": "Neispravan zahtev. Proverite JSON format."}), 400


@mojaAplikacija.errorhandler(404)
def nije_pronadjen(error):
    """Prilagođen odgovor za 404 Not Found."""
    return jsonify({"greska": "Resurs nije pronađen."}), 404


@mojaAplikacija.errorhandler(500)
def interna_greska(error):
    """Prilagođen odgovor za 500 Internal Server Error."""
    return jsonify({"greska": "Interna greška servera."}), 500


# =============================================================================
# 11. POKRETANJE SERVERA
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("  ŠKOLICA Flask REST API Server")
    print("  Autor: dipl.inz. Vahid Zekic")
    print("=" * 60)
    print("")
    print("  Endpointi:")
    print("    GET    /                           → Status servera")
    print("    GET    /api/studenti               → Svi studenti")
    print("    GET    /api/studenti/<id>          → Student po ID-ju")
    print("    POST   /api/studenti               → Kreiranje studenta")
    print("    PUT    /api/studenti/<id>          → Ažuriranje studenta")
    print("    DELETE /api/studenti/<id>          → Brisanje po ID-ju")
    print("    DELETE /api/studenti/ime/<ime>     → Brisanje po imenu")
    print("")
    print("  Server se pokreće na: http://0.0.0.0:5000")
    print("=" * 60)

    # host='0.0.0.0' — server je dostupan sa svih mrežnih interfejsa
    # port=5000 — standardni Flask port
    # debug=True — automatski restart pri promenama koda
    mojaAplikacija.run(host='0.0.0.0', port=5000, debug=True)
