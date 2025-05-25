from flask import Flask, request, jsonify
from cliente import consultar_cliente

app = Flask(__name__)  # ¡Esta línea es crucial!

@app.route('/cliente', methods=['POST'])
def handle_consulta():
    try:
        data = request.get_json()
        ci = data.get('ci', '').strip()
        if not ci:
            raise ValueError("CI vacío")
        return jsonify(consultar_cliente(ci))
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    print("🔥 Servidor listo en http://localhost:5003")
    app.run(host='localhost', port=5003)