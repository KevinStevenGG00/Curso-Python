# Un ejemplo para ilustrar el principio ISP sería el diseño de una interfaz 
# para un sistema de gestión de documentos. Supongamos que tenemos una interfaz 
# llamada DocumentManagement, que incluye métodos para cargar, guardar y eliminar documentos

##################################################################
# No óptima
class DocumentOperations:
    def load_document(self):
        pass
    
    def save_document(self):
        pass
    
    def delete_document(self):
        pass

##################################################################
# Óptima
class DocumentLoader:
    def load_document(self):
        pass

class DocumentSaver:
    def save_document(self):
        pass

class DocumentDeleter:
    def delete_document(self):
        pass
    
##################################################################