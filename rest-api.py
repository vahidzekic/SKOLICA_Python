from flask import Flask, jsonify, request, abort
from flask_cors import CORS

mojaAplikacija = Flask(__name__)
CORS(mojaAplikacija)

bazaPodataka = ConnectionAbortedError
 
studenti = [
    { 
        "id": 1,
        "ime": "Vahid",
        "prezime": "Zekic",
        "godine": 34,
        "pol": "muski"
    },{ 
        "id": 2,
        "ime": "Enes",
        "prezime": "Daca",
        "godine": 32,
        "pol": "muski"
    },{ 
        "id": 3,
        "ime": "Omer",
        "prezime": "Ljajic",
        "godine": 16,
        "pol": "muski"
    },{ 
        "id": 4,
        "ime": "Kemo",
        "prezime": "Plojovic",
        "godine": 27,
        "pol": "muski"
    }
    
]


# GET metoda - Status servera
@mojaAplikacija.route('/')
def statusServer():
    return "Server je ONLINE!!!"


# GET metoda - JSON objekat
@mojaAplikacija.route('/get')
def mojaGetMetoda():
    return jsonify(studenti)


# POST metoda - JSON objekat
@mojaAplikacija.route('/post', methods=['POST'])
def mojPostMetoda():
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
    return "POST metoda je uspeshno izvrshena."




if __name__ == '__main__':
    mojaAplikacija.run(debug=True)


