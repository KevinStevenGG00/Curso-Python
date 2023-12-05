with open("archivos\\texto_kevin.txt",encoding="UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)

#no es necesario cerrar al usar with open