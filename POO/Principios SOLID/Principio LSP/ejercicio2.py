from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self):
        pass

class ProductoFisico(Producto):
    def __init__(self, nombre, precio, peso):
        super().__init__(nombre, precio)
        self.peso = peso

    def calcular_precio_final(self):
        costo_envio = 5 + self.peso * 0.1
        return self.precio + costo_envio

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, tamano_mb):
        super().__init__(nombre, precio)
        self.tamano_mb = tamano_mb

    def calcular_precio_final(self):
        return self.precio

# Crear instancias de diferentes tipos de productos
libro = ProductoFisico("Libro", 20, 1.5)
software = ProductoDigital("Software", 50, 100)

# Calcular el precio final de los productos
precio_final_libro = libro.calcular_precio_final()
precio_final_software = software.calcular_precio_final()

print("Precio final del libro:", precio_final_libro)
print("Precio final del software:", precio_final_software)
