class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def abrir(self):
        print("Abriendo el archivo:", self.nombre)

class ArchivoTexto(Archivo):
    def abrir(self):
        print("Abriendo archivo de texto:", self.nombre)

class ArchivoImagen(Archivo):
    def abrir(self):
        print("Abriendo archivo de imagen:", self.nombre)

def abrir_archivos(archivos):
    for archivo in archivos:
        archivo.abrir()

# Crear instancias de diferentes tipos de archivos
archivo_texto = ArchivoTexto("documento.txt")
archivo_imagen = ArchivoImagen("foto.jpg")

# Lista de archivos
archivos = [archivo_texto, archivo_imagen]

# Abrir los archivos
abrir_archivos(archivos)
