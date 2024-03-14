class Animal:
    def comer(self):
        print("Este animal puede comer")

class Mamifero(Animal):
    def amamantar(self):
        print("Este animal puede amamantar")

class Ave(Animal):
    def volar(self):
        print("Este animal puede volar")

class Muercielago(Mamifero,Ave):
    pass

murcielago1 = Muercielago()

murcielago1.comer()
murcielago1.volar()
murcielago1.amamantar()