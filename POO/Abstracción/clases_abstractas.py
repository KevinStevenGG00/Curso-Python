from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, actividad):
        self.nombre = nombre
        self.edad = edad
        self.actividad = actividad
    
    @abstractclassmethod
    def ver_actividad(self):
        pass
    
    def saludar(self):
        print(f"Hola me llamo {self.nombre} tengo {self.edad} años.")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, actividad):
        super().__init__(nombre, edad, actividad)
    
    def ver_actividad(self):
        print(f"Estoy estudiando {self.actividad}.")

class Trabajador(Persona):
    def __init__(self, nombre, edad, actividad):
        super().__init__(nombre, edad, actividad)
    
    def ver_actividad(self):
        print(f"Estoy trabajando en el rubro de {self.actividad}.")
        
persona1 = Estudiante("Kemi", 23, "arquitectura")
persona2 = Trabajador("Kevin", 24, "programación")

persona1.saludar()
persona1.ver_actividad()
persona2.saludar()
persona2.ver_actividad()
