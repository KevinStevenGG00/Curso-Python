from abc import ABC, abstractmethod

# Definimos una clase base para los vehículos
class Vehiculo(ABC):
    @abstractmethod
    def calcular_tarifa_peaje(self):
        pass

# Implementaciones de diferentes tipos de vehículos
class Coche(Vehiculo):
    def calcular_tarifa_peaje(self):
        return 2.0  # Tarifa de peaje para coches

class Camion(Vehiculo):
    def calcular_tarifa_peaje(self):
        return 5.0  # Tarifa de peaje para camiones

# Clase de gestión de peajes
class GestorPeajes:
    def calcular_total_peajes(self, vehiculos):
        total = 0
        for vehiculo in vehiculos:
            total += vehiculo.calcular_tarifa_peaje()
        return total

# Uso del sistema de peajes
coche1 = Coche()
coche2 = Coche()
camion1 = Camion()

gestor_peajes = GestorPeajes()
total_peajes = gestor_peajes.calcular_total_peajes([coche1, coche2, camion1])
print("Total de peajes a pagar:", total_peajes)
