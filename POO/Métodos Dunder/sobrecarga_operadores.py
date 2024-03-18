class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __add__(self,otro):
        suma_nombre = self.nombre + otro.nombre
        suma_edad = self.edad + otro.edad
        return Persona(suma_nombre,suma_edad)
    
p1 = Persona("Kemi",11) 
p2 = Persona("vin",12)
p3 = p1 + p2
print(p3.nombre)
print(p3.edad)