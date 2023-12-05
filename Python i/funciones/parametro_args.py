#funcion base
def suma(a,b):
    return a+b
resultado = suma(2,9)
print(resultado)

#suma varios valores
def suma_lista(lista):
    suma_total = 0
    for numero in lista:
        suma_total = suma_total + numero
    return suma_total

resultado0 = suma_lista([1,2,3,4])
print(resultado0)

#utilizando parametro args "*"
#0
def sumita_base(numero):
    return sum([*numero])
resultado3=sumita_base([1,2,3,4,5,6,7])
print(resultado3)
#1
def sumita(*num):
    return sum(num)                    #sum() funcion de suma de una lista
resultado1=sumita(1,2,3,4,5)
print(resultado1)
#2
def sumita0(nombre,*num):
    return f"{nombre} tu suma es {sum(num)}"
resultado2=sumita0("kevin",1,2,3,4,5,6)
print(resultado2)