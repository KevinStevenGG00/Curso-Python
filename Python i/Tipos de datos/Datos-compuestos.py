lista = ["Kevin Godoy","Goicochea",True,23]
tupla = ("Kevin Godoy","Goicochea",True,23)       #no se pueden modificar pero si redefinir

lista[2]=False

conjunto={"Kevin Godoy","Goicochea",True,23}      #datos sin un orden, sin datos duplicados, los conjuntos o set se pueden redefinir
conjunto={"datos modificados"}

print(lista[2])
print(tupla[0])
print(conjunto)                                   #no se pueden acceder a los datos del conjunto por el índice

diccionario = {
    'nombre': 'Kevin',
    'apellidos': 'Godoy Goicochea',
    'edad': 23,
    'activo': True
}

print(diccionario["edad"])