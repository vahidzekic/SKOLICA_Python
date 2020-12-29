from flask import Flask, jsonify

mojaAplikacija = Flask(__name__)

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

# GET metoda
@mojaAplikacija.route('/get')
def mojaGetMetoda():
    return jsonify(studenti)

if __name__ == '__main__':
    mojaAplikacija.run(debug=True)


