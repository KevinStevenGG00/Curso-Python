# Definimos la abstracción para el tipo de notificación
class Notificacion:
    def enviar(self, mensaje):
        pass

# Implementación de notificación por correo electrónico
class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        print("Enviando correo electrónico:", mensaje)

# Implementación de notificación por SMS
class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        print("Enviando SMS:", mensaje)

# Implementación de notificación por notificación push
class NotificacionPush(Notificacion):
    def enviar(self, mensaje):
        print("Enviando notificación push:", mensaje)

# Clase de alto nivel que depende de la abstracción, no de la implementación concreta
class SistemaNotificacion:
    def __init__(self, notificacion):
        self.notificacion = notificacion

    def enviar_notificacion(self, mensaje):
        self.notificacion.enviar(mensaje)

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos una instancia de SistemaNotificacion con un objeto de NotificacionSMS
    notificacion_sms = NotificacionSMS()
    sistema = SistemaNotificacion(notificacion_sms)
    sistema.enviar_notificacion("¡Hola, este es un mensaje de prueba por SMS!")

    # También podemos cambiar la implementación de notificación fácilmente
    notificacion_correo = NotificacionCorreo()
    sistema = SistemaNotificacion(notificacion_correo)
    sistema.enviar_notificacion("¡Hola, este es un mensaje de prueba por correo electrónico!")
