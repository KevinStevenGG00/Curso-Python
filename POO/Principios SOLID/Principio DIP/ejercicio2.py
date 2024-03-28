# Definimos la abstracción para el método de pago
class MetodoPago:
    def procesar_pago(self, monto):
        pass

# Implementación de método de pago con tarjeta de crédito
class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago de ${monto} procesado con tarjeta de crédito.")

# Implementación de método de pago con PayPal
class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago de ${monto} procesado con PayPal.")

# Implementación de método de pago con transferencia bancaria
class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago de ${monto} procesado con transferencia bancaria.")

# Clase de alto nivel que depende de la abstracción, no de la implementación concreta
class ProcesadorPagos:
    def __init__(self, metodo_pago):
        self.metodo_pago = metodo_pago

    def realizar_pago(self, monto):
        self.metodo_pago.procesar_pago(monto)

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia de ProcesadorPagos con un objeto de TarjetaCredito
    tarjeta_credito = TarjetaCredito()
    procesador = ProcesadorPagos(tarjeta_credito)
    procesador.realizar_pago(100)

    # También podemos cambiar fácilmente la implementación de método de pago
    paypal = PayPal()
    procesador = ProcesadorPagos(paypal)
    procesador.realizar_pago(50)
