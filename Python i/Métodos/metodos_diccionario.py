diccionario = {
    "nombre" : "Kevin",
    "edad" : 23,
    "egresado" : True,
    "carrera" : "Sistemas"
}

#nos devuelve un objeto dict_item, una clave
claves = diccionario.keys() #también sirve para iterar
print(claves)

#obteniendo un dato, valor de clave
resultado0=diccionario.get("edad") #si no se encuentra te bota null
resultado1=diccionario["nombre"] #si no se encuentra te bota una excepción

#elimina los elementos
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("egresado")

#obteniendo un elemento dict_items iterable
resultado2=diccionario.items()
print(resultado2)


