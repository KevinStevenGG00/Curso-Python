with open("archivos\\texto_kevin.txt",'w',encoding="UTF-8") as archivo:  #permiso de escritura 'w'
    #sobreescribiendo archivo
    archivo.write("Quiero jugar!!!")
    
    #escribiendo texto, solo se puede poner un argumento
    archivo.writelines("\nHola jugador de albion que sobreescribe su propia historia")
    
    #con una lista, varios argumentos
    archivo.writelines(["\nmmoRPG","\nMUNDO ABIERTO"])
    
with open("archivos\\texto_kevin.txt",'a',encoding="UTF-8") as archivo:  #permiso para agregar
    archivo.write("\nKemi vam juá")
    archivo.write("\nñeeeee")
    for i in range(5):
        archivo.write(f"\nCerrando sesión para DG {i+1}")