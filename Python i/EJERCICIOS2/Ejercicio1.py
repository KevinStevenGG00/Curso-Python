#Falto un profesor y los alumnos armarán su propia clase, 1profesor y 1asistente
#Pedir nombre y edad de todos los compañeros, el mayor será el profe, el menor el asistente

def obtener_compañeros(cantidad):
    compañeros=[]
    for i in range(cantidad):
        nombre = input("Ingrese nombre: ")
        edad = int(input("Ingrese edad: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente,profesor = obtener_compañeros(4)
print(f"El profe es: {profesor}")
print(f"El asistente es: {asistente}")
    
