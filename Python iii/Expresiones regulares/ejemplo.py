import re

# Definir una cadena de texto
texto = "Hoy es un buen día para aprender Python."

# Buscar la palabra "Python" en el texto
patron = r"Python"
resultado = re.search(patron, texto)
if resultado:
    print("Se encontró 'Python' en el texto.")
else:
    print("No se encontró 'Python' en el texto.")

# Buscar todas las ocurrencias de "Python" en el texto
ocurrencias = re.findall(patron, texto)
print("Número de ocurrencias de 'Python':", len(ocurrencias))

# Reemplazar todas las ocurrencias de "Python" con "Java"
nuevo_texto = re.sub(patron, "Java", texto)
print("Texto después de reemplazar 'Python' con 'Java':", nuevo_texto)

# Dividir una cadena basada en un patrón
nueva_lista = re.split(r"\s", texto)  # Dividir en espacios en blanco
print("Lista después de dividir el texto:", nueva_lista)
