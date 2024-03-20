# Supongamos que estás trabajando en un sistema de gestión de usuarios 
# que requiere diferentes funcionalidades relacionadas con la autenticación 
# y el manejo de roles de usuario.

# Interfaz para la autenticación de usuarios
class Authenticatable:
    def authenticate(self, username, password):
        pass

# Interfaz para el manejo de roles de usuario
class RoleManagable:
    def assign_role(self, username, role):
        pass

    def remove_role(self, username, role):
        pass

# Clase que implementa solo la funcionalidad de autenticación
class Authenticator(Authenticatable):
    def authenticate(self, username, password):
        # Lógica para autenticar al usuario
        pass

# Clase que implementa solo el manejo de roles de usuario
class RoleManager(RoleManagable):
    def assign_role(self, username, role):
        # Lógica para asignar un rol a un usuario
        pass
    
    def remove_role(self, username, role):
        # Lógica para eliminar un rol de un usuario
        pass
