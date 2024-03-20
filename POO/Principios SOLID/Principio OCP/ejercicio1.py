from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2

class CalculadoraArea:
    def calcular_area_total(self, formas):
        area_total = 0
        for forma in formas:
            area_total += forma.calcular_area()
        return area_total

# Uso de las clases
cuadrado = Cuadrado(5)
circulo = Circulo(3)
formas = [cuadrado, circulo]

calculadora_area = CalculadoraArea()
area_total = calculadora_area.calcular_area_total(formas)
print("Área total de todas las formas:", area_total)

