import pandas as pd
#leemos el archivo csv
df = pd.read_csv("archivos\\datos.csv") #agregamos encabezado, desplazamos hacia abajo
print(df)
print("\n")

#obteniendo los datos de la columna "nombre"
df0 = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
nombres = df0["name"]      #dataframe
print(nombres)
print("\n")

#ordenando el df por edad
df_ordenado = df.sort_values("edad")
print(df_ordenado)
print("\n")

#ordenando descendentemente
df_ordenado_desc = df.sort_values("edad",ascending=False)
print(df_ordenado_desc)
print("\n")

#concatenar 2 dataframes
df1 = pd.read_csv("archivos\\datos.csv")
df_concatenado = pd.concat([df,df1])
print(df_concatenado)
print("\n")
 
#HEAD primeras filas - TAIL ultimas filas-----------------------
#primera fila
primera_fila = df.head(1)
print(primera_fila)
print("\n")

#3 filas
primera_fila = df.head(3)
print(primera_fila)
print("\n")

#ultimas 3 filas
primera_fila = df.tail(2)
print(primera_fila)
print("\n")

#############SLICING##############
cadena = "Kevin"
posicion="01234"
print(cadena[1:4])
##################################
