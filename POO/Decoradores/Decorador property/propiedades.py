class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre

objeto_persona = Persona("Kevin")

persona = objeto_persona.nombre
print(persona)

objeto_persona.nombre = "Kemi"
persona = objeto_persona.nombre
print(persona)

del objeto_persona.nombre