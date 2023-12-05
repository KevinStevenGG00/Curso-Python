#creando una funcion simple
def saludo():
    print("hola mundo")
    
saludo()

#crear una funcion con parámetros

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "m":
        adjetivo = "maestro"
    elif sexo == "f":
        adjetivo = "maestra"
    else:
        adjetivo = "mmmmmm..."
        
    print(f"Hola {nombre}, cómo estás {adjetivo}, espero que bien")
    
saludar("kevin","M")       #EXTRA: puedo cambiar posicion de mis parámetros (sexo="M",nombre="Kemi")

def doble(num):
    numero = int(num)
    resultado = numero*2
    return resultado, numero          #se puede retornar multiples valores
    
resultado0,resultado1=doble(10)
print(f"el doble es: {resultado0}")
print(f"el numero fue: {resultado1}")
