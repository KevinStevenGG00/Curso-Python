#crea funciones anonimas
doble = lambda x: x*2
print(doble(5))

#filter
lista=[1,2,3,4,5,6,7,8,9]

def es_par(num):
    if num%2==0:
        return True
    
numeros_pares = filter(es_par,lista)
print(list(numeros_pares))

#filter pero con lambda
numeros_impares = filter(lambda numero:numero%2!=0,lista)
print(list(numeros_impares))
