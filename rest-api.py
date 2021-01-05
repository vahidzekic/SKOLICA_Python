from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import json
import platform

mojaAplikacija = Flask(__name__)
CORS(mojaAplikacija)

studenti = []
with open('rest-api.json') as JsonPodatak:
    studenti = json.load(JsonPodatak)


# GET metoda - Status servera
@mojaAplikacija.route('/')
def statusServer():
    poruka = 'Server je ONLINE '
    status = platform.version()
    ip = platform.node()
    return poruka + status + " IP Adresa je: " + ip


# GET metoda - JSON objekat
@mojaAplikacija.route('/get')
def mojaGetMetoda():
    return jsonify(studenti)


# POST metoda - JSON objekat
@mojaAplikacija.route('/post', methods=['POST'])
def mojaPostMetoda():
    if not request.json or not 'ime' in request.json:
        abort(400)
    student = {
        'id': request.json['id'],
        'ime': request.json['ime'],
        'prezime': request.json['prezime'],
        'godine': request.json['godine'],
        'pol': request.json['pol']
    }
    studenti.append(student)
    with open ('rest-api.json', 'w') as sacuvajJson:
        json.dump(studenti, sacuvajJson)
    return "POST metoda je uspeshno izvrshena."

# DELETE metoda preko IDa - JSON objekat
@mojaAplikacija.route('/brisanje/<int:student_id>', methods=['DELETE'])
def mojaDeleteMetoda(student_id):
    student = [student for student in studenti if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    studenti.remove(student[0])
    with open ('rest-api.json', 'w') as sacuvajJson:
        json.dump(studenti, sacuvajJson)
    return "Student je obrisan."


# DELETE metoda preko IMENA - JSON objekat
@mojaAplikacija.route('/brisanje/<student_ime>', methods=['DELETE'])
def mojaDeleteMetoda2(student_ime):
    student = [student for student in studenti if student['ime'] == student_ime]
    if len(student) == 0:
        abort(404)
    studenti.remove(student[0])
    with open ('rest-api.json', 'w') as sacuvajJson:
        json.dump(studenti, sacuvajJson)
    return "Student je obrisan."



if __name__ == '__main__':
    mojaAplikacija.run(host='0.0.0.0', port=5000, debug=True)
