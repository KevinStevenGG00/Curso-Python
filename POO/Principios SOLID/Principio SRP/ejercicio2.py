class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def get_nombre(self):
        return self.nombre

    def get_salario(self):
        return self.salario

class CalculadoraNomina:
    def calcular_salario_neto(self, empleado):
        # Lógica para calcular el salario neto (después de impuestos, etc.)
        salario_neto = empleado.get_salario() * 0.85  # Suponiendo una tasa de impuestos del 15%
        return salario_neto

class GeneradorReporte:
    def generar_reporte(self, empleado):
        # Lógica para generar un reporte
        reporte = f"Información del empleado:\nNombre: {empleado.get_nombre()}\nSalario: {empleado.get_salario()}\n"
        return reporte

# Uso de las clases
empleado1 = Empleado("Juan", 5000)
calculadora_nomina = CalculadoraNomina()
generador_reporte = GeneradorReporte()

salario_neto = calculadora_nomina.calcular_salario_neto(empleado1)
reporte = generador_reporte.generar_reporte(empleado1)

print("Salario neto de", empleado1.get_nombre(), ":", salario_neto)
print("Reporte del empleado:", reporte)
