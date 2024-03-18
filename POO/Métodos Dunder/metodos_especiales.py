class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # def __str__(self):
    #     return f"Objeto con nombre {self.nombre} y edad {self.edad}"

    def __repr__(self):
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    

persona1 = Persona("Kevin",23) 
representacion = repr(persona1)
clon_persona1 = eval(representacion)

print(persona1) 
print(representacion)
print(clon_persona1)
print(clon_persona1.nombre)