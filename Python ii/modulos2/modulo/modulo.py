#si el modulo estuviera dentro de una carpeta en la misma ruta

import sys
#agregar un modulo según su ubicación
sys.path.append("c:\\Users\\7408950068-PC\\Desktop\\Kevin\\PYTHON\\modulos2\\funciones")
#sys.path.append("C:\\Users\\740899500754-PC\\Desktop\\Kevin\\Curso-Python\\Python ii\\modulos2\\funciones")

#imprimir todos los modulos
print(sys.path)

#llamando a la funcion
import funciones
print(funciones.saludo_a("Godoy"))
