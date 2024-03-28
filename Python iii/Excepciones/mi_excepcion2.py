# Definir una excepción personalizada
class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return f"Error personalizado: {self.mensaje}"

# Función que puede lanzar la excepción personalizada
def dividir(a, b):
    if b == 0:
        raise MiError("No se puede dividir por cero")
    else:
        return a / b

# Uso de la función que podría lanzar la excepción personalizada
try:
    resultado = dividir(10, 0)
    print("El resultado de la división es:", resultado)
except MiError as e:
    print(e)
