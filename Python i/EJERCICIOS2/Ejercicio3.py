#serie de fibonacci hasta el numero dado
def fibonacci_hasta(num):
    a,b = 0,1
    lista=[]
    for i in range(num):                             #error en el num podria ser cualquier numero mayor
        if b > num: return lista
        else:
            lista.append(b)
            a,b = b,a+b 
            
resultado = fibonacci_hasta(34)
print(resultado)
