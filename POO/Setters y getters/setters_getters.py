class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre       #dato privado
        self.__edad = edad           #dato privado

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

persona1 = Persona("Kevin", 23)

nombre = persona1.get_nombre()
print(nombre)

persona1.set_nombre("Kemi")
nombre = persona1.get_nombre()
print(nombre)


