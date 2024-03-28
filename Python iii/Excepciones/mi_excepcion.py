class MiPropiaExcepcion(Exception):
    def __init__(self, mensaje="Ocurrió un error"):
        self.mensaje = mensaje

# Ejemplo de uso de la excepción personalizada
def dividir(a, b):
    if b == 0:
        raise MiPropiaExcepcion("No se puede dividir por cero")
    return a / b

# Uso de la función dividir con la excepción personalizada
try:
    resultado = dividir(10, 0)
except MiPropiaExcepcion as e:
    print("Se produjo un error personalizado:", e)
