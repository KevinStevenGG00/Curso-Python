lista=list(["Kevin Steven","Godoy Goicochea",23])
#una buen práctica es crear una lista vacía, es decir, sin elementos

resultado0=len(lista) #cantidad de elementos

#agregando con append
lista.append("Ing. Sistemas")

#agregando con insert, con un índice
lista.insert(3,"UNHEVAL")

#agregando varios elementos con extend
lista.extend(["Egresado","Huánuco",2023])

#eliminar un elemento
lista.pop(6) #si no se pone índice se elimina el último dato, o también -1

#remueve un elemento de la lista por su valor
lista.remove(2023)

#eliminar todo los elementos
#lista.clear()

lista0=list([1,2,3,4,5,0,9,True,False])

#ordenando asc
lista0.sort()

#ordenando des
lista0.sort(reverse=True)

lista1=list(["hola","mundo"])
#OJO: tupla se crea con parentesis() en vez de [], y el conjunto con SET
tupla=tuple(("tengo",23))
conjunto=set(["lassy","godoy"])
print(tupla,conjunto)

#revirtiendo
lista1.reverse()

#RECORDANDO
resultado1=lista.index(23)

#conjuntos y tuplas son inmutables