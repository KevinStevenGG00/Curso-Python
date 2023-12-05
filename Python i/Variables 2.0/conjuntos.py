#creando un conjunto
conjunto0 = set(["Dato1","Dato2"])

conjunto1 = set(["Dato1",("dato2","dato3")]) #tupla dentro de un conjunto

#Conjunto dentro de un conjunto
conjunto2 = frozenset(["dato0","dato1"])
conjunto3 = {"dato2",conjunto2}

print(conjunto3)

#Teoria de conjuntos
c1 = {1,2,3,4,5,6,7}
c2 = {2,4,6}

#Verificando si es un subconjunto
resultado0 = c2.issubset(c1)
resultado1 = c2 <= c1

#Verificando si es un superconjunto
resultado2 = c1.issuperset(c2)
resultado3 = c1 > c2

#verificando si no tiene ningun elemento en comun
resultado4 = c1.isdisjoint(c2) #False, porque tienen elementos en comun