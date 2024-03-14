class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"Hiciste la llamada desde un {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada desde un {self.modelo}")
        
        
celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 14 Pro","96MP")

print(celular1.marca)
print(celular2.camara)

celular2.llamar()
celular1.cortar()
