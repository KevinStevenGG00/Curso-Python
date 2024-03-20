# Supongamos que necesitamos manejar tanto los pagos con tarjeta de crédito 
# como los pagos a través de una plataforma de pago en línea, como PayPal. 
# En lugar de tener una interfaz única que abarque todas las formas de pago, 
# podemos aplicar el principio ISP dividiendo las funcionalidades relacionadas 
# con el procesamiento de pagos.

# Interfaz para procesar pagos con tarjeta de crédito
class CreditCardPaymentProcessable:
    def process_credit_card_payment(self, amount, card_number, expiration_date, cvv):
        pass

# Interfaz para procesar pagos a través de PayPal
class PayPalPaymentProcessable:
    def process_paypal_payment(self, amount, email, password):
        pass

# Clase que implementa la funcionalidad de procesamiento de pagos con tarjeta de crédito
class CreditCardPaymentProcessor(CreditCardPaymentProcessable):
    def process_credit_card_payment(self, amount, card_number, expiration_date, cvv):
        # Lógica para procesar el pago con tarjeta de crédito
        pass

# Clase que implementa la funcionalidad de procesamiento de pagos a través de PayPal
class PayPalPaymentProcessor(PayPalPaymentProcessable):
    def process_paypal_payment(self, amount, email, password):
        # Lógica para procesar el pago a través de PayPal
        pass
