# Privado
class Clase:
    def __init__(self):
        self._atributo_privado = "Valor"

objeto = Clase()
print(objeto._atributo_privado)

# Muy privado (ERROR)
class Clase:
    def __init__(self):
        self.__atributo_privado = "Valor"
    def __hablar(self):                        #también existen métodos muy privados
        print("Hi")

objeto = Clase()
#print(objeto.__hablar())                      #error
#print(objeto._atributo_privado)               #error