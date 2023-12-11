#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos\\Problemas_de_archivos_resueltos\\datos.csv")

print(type(df["edad"][0]))

df["edad"] = df["edad"].astype(str)
print(type(df["edad"][0]))

#reemplazar un valor por otro
df["nombre"].replace("kevin","kevincito",inplace=True)
print(df["nombre"])

#eliminar filas con datos faltantes
print("\n")
print(df)
print("-------------------------------------")
print(df.dropna())           #como parametro puede ir axis=0 (fila, por defecto) o axis=1 (columna)

#eliminando filas repetidas
print("-------------------------------------")
df = df.drop_duplicates()
print(df)

#creando un CSV con un df
df.to_csv("archivos\\Problemas_de_archivos_resueltos\\datos_generados.csv")