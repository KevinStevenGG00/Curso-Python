animales = ["perro","gato","loro","cocodrilo","leon"]

#for in
for animal in animales:
    print(animal)
    
numeros = [1,2,3,4,5]

for resultado0 in numeros:
    resultado1=resultado0-10
    print(resultado1)
    
#iterar dos listas a la vez

for animal,resultado in zip(animales,numeros):
    print(f"animal {animal}")
    print(f"numero {resultado}")
    
for num in range(5,9):
    print(num)
    
print("----------------")

for num in range(5):
    print(num)

#forma no optima de recorrer una lista, no funciona con sets
for indice in range(len(animales)):
    print(animales[indice])
    
#forma optima de recorrer una lista
for valor in enumerate(animales):
    print(valor)
for valor in enumerate(animales):
    print(f"el animal {valor[0]+1} es el {valor[1]}")
    
#for con else
for animalito in animales:
    print(f"el {animalito}")
else:
    print("el fin del bucle xd")
    
#funciona de igual forma con las tuplas
#lista = [] tupla = ()