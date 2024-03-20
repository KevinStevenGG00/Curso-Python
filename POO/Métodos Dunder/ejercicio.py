# Crear personajes con indicadores de fuerza y velocidad, que se puedan fusionar y al fusionarse incrementar sus indicadores
# indicador nuevo = promedio elevado al 1.5 (indicadores enteros)
class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    def __repr__(self):
        return f"{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})"
    
    def __add__(self, otro):
        new_nombre = self.nombre + "-" + otro.nombre
        new_fuerza = round(((self.fuerza + otro.fuerza)/2)**1.5)
        new_velocidad = round(((self.velocidad + otro.velocidad)/2)**1.5)
        return Personaje(new_nombre, new_fuerza, new_velocidad)
    
p1 = Personaje("Kevin", 100, 90)
p2 = Personaje("Kemi", 90, 95)
p3 = Personaje("Chris", 85, 95)
p4 = p1 + p2
p5 = p4 + p3
print(p4)
print(p5)