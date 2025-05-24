from flask import Flask, request, jsonify
from cliente import procesar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():
    try:
        datos = request.get_json()  # Recibe el JSON {"cl": "4133266"}
        ci = datos.get("cl")       # Extrae la cédula

        if not ci:
            return jsonify({"error": "Campo 'cl' es requerido"}), 400

        respuesta = procesar_cliente(ci)
        return jsonify(respuesta), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5003)  # ¡Inicia el servidor en el puerto 5003!
