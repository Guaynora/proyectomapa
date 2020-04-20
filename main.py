from flask import Flask, jsonify, request, render_template,redirect, url_for
import json

app = Flask(__name__)

#creacion de los datos de las iglesias
#mas adelante despues de lograr solucionar algunos inconvenientes que tenemos sobre los marcadores en el mapa 
#con la obtencion de la data en formato json, se estara indexando a traves de elastic search para asi crear la
#consulta de los datos y ponerlos en el mapa con js
iglesias = [
    {
            "nombre": "IPUL 24 de Diciembre",
            "pastor": "Juan Pablo Guzman",
            "provincia":"Panama",
            "punto": {"type": "Point", "coordinates": [9.090700, -79.361271]},
            "can-asistentes": "100"
        },        
        {
            "nombre": "IPUL Mañanitas",
            "pastor": "Ricardo Gallardo",
            "provincia":"Panama",
            "punto": {"type": "Point", "coordinates": [9.083224, -79.406489]},
            "can-asistentes": "85"
        },
        {
            "nombre": "IPUL Central",
            "pastor": "desconocido",
            "provincia":"Panama",
            "punto": {"type": "Point", "coordinates": [9.015055, -79.485709]},
            "can-asistentes": "120"
        },
        {
            "nombre": "Vacamonte",
            "pastor": "desconocido2",
            "provincia":"Panama",
            "punto": {"type": "Point", "coordinates": [8.909378, -79.709208]},
            "can-asistentes": "75"
        },
        {
            "nombre": "IPUL Juan Diaz",
            "provincia":"Panama",
            "pastor": "Jose Antonio Carrascal",
            "punto": {"type": "Point", "coordinates": [9.045985, -79.447671]},
            "can-asistentes": "80"
        }   
]


#redireccion hacia el html que se presentara con el mapa
@app.route('/')
def index():
    return render_template('index.html',iglesias = iglesias)


#ruta donde estaran los datos de las iglesias en formato json
@app.route('/iglesias', methods = ['GET'])
def getAllIglesias():
    return jsonify(iglesias),200

if __name__ == "__main__":
    app.run(debug=True)

