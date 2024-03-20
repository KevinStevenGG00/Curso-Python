class CalculadoraSuma:
    def sumar(self, a, b):
        return a + b

class CalculadoraResta:
    def restar(self, a, b):
        return a - b

# Uso de las clases separadas
calculadora_suma = CalculadoraSuma()
resultado_suma = calculadora_suma.sumar(5, 3)
print("Resultado de la suma:", resultado_suma)

calculadora_resta = CalculadoraResta()
resultado_resta = calculadora_resta.restar(5, 3)
print("Resultado de la resta:", resultado_resta)
