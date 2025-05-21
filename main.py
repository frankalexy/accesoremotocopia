
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

INFINITYFREE_URL_REGISTRO = "http://accesoremoto.kesug.com/registrar_equipo.php"
INFINITYFREE_URL_OBTENER = "http://accesoremoto.kesug.com/obtener_equipo.php"

@app.route("/registrar", methods=["POST"])
def registrar_equipo():
    id_equipo = request.form.get("id")
    try:
        response = requests.post(
            INFINITYFREE_URL_REGISTRO,
            data={"id": id_equipo},
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        return response.text, response.status_code
    except Exception as e:
        return str(e), 500

@app.route("/obtener", methods=["POST"])
def obtener_equipo():
    id_equipo = request.form.get("id")
    try:
        response = requests.post(
            INFINITYFREE_URL_OBTENER,
            data={"id": id_equipo},
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        return response.text, response.status_code
    except Exception as e:
        return str(e), 500

@app.route("/", methods=["GET"])
def index():
    return "Proxy funcionando correctamente"
