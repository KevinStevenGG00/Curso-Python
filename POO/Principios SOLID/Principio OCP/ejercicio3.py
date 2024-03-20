from abc import ABC, abstractmethod

# Definimos una clase abstracta para los destinatarios
class Destinatario(ABC):
    @abstractmethod
    def enviar_mensaje(self, mensaje):
        pass

# Implementación de destinatario por correo electrónico
class DestinatarioCorreoElectronico(Destinatario):
    def __init__(self, email):
        self.email = email

    def enviar_mensaje(self, mensaje):
        print(f"Enviando mensaje por correo electrónico a {self.email}: {mensaje}")

# Implementación de destinatario por SMS
class DestinatarioSMS(Destinatario):
    def __init__(self, numero):
        self.numero = numero

    def enviar_mensaje(self, mensaje):
        print(f"Enviando mensaje por SMS al número {self.numero}: {mensaje}")

# Definimos una clase abstracta para los tipos de mensajes
class TipoMensaje(ABC):
    @abstractmethod
    def generar_mensaje(self):
        pass

# Implementación de mensaje de saludo
class MensajeSaludo(TipoMensaje):
    def generar_mensaje(self):
        return "¡Hola! Espero que tengas un buen día."

# Implementación de mensaje de recordatorio
class MensajeRecordatorio(TipoMensaje):
    def generar_mensaje(self):
        return "Recuerda completar tu tarea para hoy."

# Clase de gestión de notificaciones
class GestorNotificaciones:
    def __init__(self, destinatario, tipo_mensaje):
        self.destinatario = destinatario
        self.tipo_mensaje = tipo_mensaje

    def enviar_notificacion(self):
        mensaje = self.tipo_mensaje.generar_mensaje()
        self.destinatario.enviar_mensaje(mensaje)

# Uso del sistema de notificaciones
destinatario_email = DestinatarioCorreoElectronico("ejemplo@correo.com")
destinatario_sms = DestinatarioSMS("123456789")

mensaje_saludo = MensajeSaludo()
mensaje_recordatorio = MensajeRecordatorio()

notificacion_email = GestorNotificaciones(destinatario_email, mensaje_saludo)
notificacion_sms = GestorNotificaciones(destinatario_sms, mensaje_recordatorio)

notificacion_email.enviar_notificacion()
notificacion_sms.enviar_notificacion()
