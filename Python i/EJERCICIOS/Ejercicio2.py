# Suponiendo que cada persona habla 2 palabras en 1 segundo
# Pedir al usuario cualquier texto y calcular

#1. Cuantas palabras dijo
#2. Cuanto tiempo le tomó

texto = input("Escribe lo que tienes que decir: ")
lista_texto = texto.split(" ")
cant_palabras = len(lista_texto)
tiempo = cant_palabras/2

print(f"La cantidad de palabras fue de {cant_palabras}")
print(f"El tiempo que tomará en decir el texto es de {tiempo} segundos")

#3. Si se tarda 10 seg o más mostrar : "Era un texto simple, no un historial!! D:"

if  tiempo>=10 :
    print("Era un texto simple, no un historial!! D:")

#4. Si hablas un 30% más rápido, cuánto demorarías

tiempo_mejorado = 70*tiempo/100
print(f"Si hablas 30% másm rápido, tardarías {tiempo_mejorado} segundos")
