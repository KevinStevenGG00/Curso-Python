archivo = open("Archivos\\texto_kevin.txt",encoding="UTF-8") #abrir el archivo, poniendo utf8 para caracteres adicionales
#grupo1
#archivo_leido = archivo.read()              #leer el archivo
#print(archivo_leido)                   

#grupo2
linea_1 = archivo.readline()      #leer la primera linea
archivo.close()         #cerrar archivo leido, siempre se cierra despues de leerlo
print(linea_1)       #se almaceno en la varibale antes de cerrarlo


#grupo3
#linea_1 = archivo.readline(5)      #leer la primera linea hasta 5
#print(linea_1)

#grupo4
#lineas = archivo.readlines()
#print(lineas)