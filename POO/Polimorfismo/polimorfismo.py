class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())
    
    
gatito = Gato()
perrito = Perro()

hacer_sonido(gatito)
hacer_sonido(perrito)