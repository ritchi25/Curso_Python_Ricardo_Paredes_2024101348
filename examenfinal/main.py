#!/usr/bin/env python3
from flask import Flask
from cliente import cliente

app = Flask(__name__)

##servicios rest
app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Mundo'


if __name__ == "__main__":
    
    app.run(host = '0.0.0.0', debug = True, port = 5003)
    app.run(debug = True)
