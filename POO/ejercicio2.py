class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def datosPersona(self):
        print(f"La persona se llama {self.nombre} y tiene {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado =grado
    def datosEstudiante(self):
        print(f"El estudiante tiene el grado de {self.grado}")
        
estudiante1 = Estudiante("Kevin",23,"Bachiller")
print(estudiante1.grado)

estudiante1.datosPersona()
estudiante1.datosEstudiante()