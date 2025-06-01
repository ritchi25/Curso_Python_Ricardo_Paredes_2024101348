clientes_registrados = {"4133266": "Cliente válido"}

def consultar_cliente(ci):
    if ci in clientes_registrados:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        }
    return {
        "accion": "Cliente no está en el sistema",
        "codRes": "ERROR",
        "menRes": "Error cliente",
        "ci": ci
    }