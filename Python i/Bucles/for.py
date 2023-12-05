frutas =["manzana","platano","granada","mango","pera"]
numeros =[2,3,4,1]
for fruta in frutas:
    if fruta == "pera":
        continue
    print(f"Hoy comeré {fruta}")

print("----------------------------")

for fruta in frutas:
    print(f"comere {fruta}")
    if fruta =="granada":
        print("me hizo mal no comeré más")
        break #no se ejecuta nada mas, se sale del for, de todo
    
#recorriendo una cadena de texto
usuario="kevin steven godoy"
for c in usuario:
    print(f"se tiene el caracter {c}")
    
#for en una linea
numeros2 = [x**2 for x in numeros]