#Definiendo una variable
nombre = "Clara"
numero = 5

numero +=3
bienvenida = 'Hola ' + nombre + ' cómo estás?'  # concatenar
bienvenida_f = f"Hola {nombre} cómo estás?"     # f-string -> convierte a texto la variable llamada

# del numero                                    # para borrar la declaración de una variable

print(numero)
print(nombre)
print(bienvenida)
print(bienvenida_f)
print('Clara' in  bienvenida)                     # buscar cadena en la variable
print('lara' in  bienvenida_f) 
print('Kevin' not in  bienvenida_f)             # not in -> no está