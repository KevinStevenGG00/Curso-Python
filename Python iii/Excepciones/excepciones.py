def sumar_dos():
    i = 0
    while True:
        i += 1
        a = input("Escribe el 1er número: ")
        b = input("Escribe el 2do número: ")
        try:
            suma = int(a) + int(b)
        except ValueError:
            print("Error en el valor de la suma, se tiene que sumar sólo números")
        else:
            break
        finally:
            print(f"Finalización de la iteración número: {i}")
    return suma
print(sumar_dos())