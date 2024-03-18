class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"Hola papay soy {self.nombre} toy hablando")
        
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

empleado2 = Empleado("Kemi", 24,"Shuco","Arquitecto",8000)


print(empleado2.nacionalidad)
empleado2.hablar()