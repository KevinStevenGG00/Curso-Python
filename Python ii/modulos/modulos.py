##1ra forma de importar
#import funcion_saludar as saludo             ## "as" nombramiento a un modulo, tambien se puede renombrar una funcion
   
##2da forma de importar(más específica)
#from funcion_saludar import saludar,saludar_raro as saludo_informal  #si se quiere importar mas de una funcion utilizar ","

##orientada a la 1ra forma
##la funcion se convierte en méthodo
#resultado = saludo.saludar("Kevin")

##orientada a la 2da forma
##se utiliza como funcion
#resultado = saludar("Kevin")
#resultado0 = saludo_informal("Kemi")

##importar una funcion dentro de una carpeta ubicada a la par
from funciones.saludar import saludito
resultado1 = saludito("Clarita")
print(resultado1)