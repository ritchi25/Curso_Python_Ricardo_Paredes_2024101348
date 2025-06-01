from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)
@cliente.route('/cliente', methods=['POST'])
def llamarServicioSet():
    ci = request.json.get('ci')


    codRes, menRes, accion = inicializarVariables(ci)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'ci': ci,
        'accion': accion
    }
    return jsonify(salida)

def inicializarVariables(ci):
    userLocal = "RParedes"
    passLocal = "unida123"
    codRes = 'SIN_ERROR'
    menRes = 'OK'

    try:
        print("Verificar cliente")
        if ci == ci:
            print("Cliente Valido")
            accion = "Success"
        else:
            print("Cliente no existe")
            accion = 'Cliente no esta en el sistema',
            codRes = 'ERROR',
            menRes = "Error cliente",
            ci = "5125841"

    except Exception as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"
    return codRes, menRes, accion