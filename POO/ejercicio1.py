class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def datos(self):
        print(f"""
              \nLos datos del estudiante son: \n\n
              Nombre: {self.nombre}\n
              Edad: {self.edad}\n 
              Grado: {self.grado}\n
              """)
    def accion(self):
        print(f"{self.nombre} está estudiando...")
        
nombre = input("Nombre: ")
edad = input("Edad: ")
grado = input("Grado: ")

estudiante1 = Estudiante(nombre, edad, grado)

estudiante1.datos()

while True:
    accion = input("Quieres que estudie?(s/n): ")
    if (accion.lower() == "s"):
        estudiante1.accion()
        break