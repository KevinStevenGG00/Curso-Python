diccionario = {
    'nombre':'kevin',
    'apellidos':'godoy goicochea',
    'edad':23,
    'carrera':'Ing. sistemas'
}

for key in diccionario:
    print(key)
    
#recorriendo un diccionario con items

for values in diccionario.items():
    print(values)
    
for dato in diccionario.items():
    key = dato[0]
    value = dato[1]
    print(f"{key} es igual a {value}")