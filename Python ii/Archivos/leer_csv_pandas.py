import pandas as pd
#leemos el archivo csv
df = pd.read_csv("archivos\\datos.csv") 
print(df)
print("\n")

#agregamos encabezado, desplazamos hacia abajo
df0 = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
print(df0)
print("\n")
#obteniendo los datos de la columna "nombre"
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

#accediendo a la cantidad de filas y columnas con shape
filas_columnas = df.shape      #resultado (filas,columnas)
print(filas_columnas)

#desempaquetar primera forma
filas0 = filas_columnas[0]
columnas0 = filas_columnas[1]
print(filas0)
print(columnas0)
print("\n")
#desempaquetar segunda forma (optimamente)
filas1, columnas1 = df.shape
print(filas1)
print(columnas1)
print("\n")

#Obteniendo data estadística del dataframe
df_info = df.describe()
print(df_info)
print("\n")

#accediendo a un elemento específico del df con loc
elemento_especifico0 = df.loc[3,"nombre"]
print(elemento_especifico0)
print("\n")

#accediendo a un elemento con iloc
elemento_especifico1 = df.iloc[1,2] #[columna,fila]
print(elemento_especifico1)
print("\n")

#todas las filas de una columna
nombres = df.iloc[:,0]
print(nombres)
print("\n")

#accediendo a una fila
fila = df.loc[1,:]
print(fila)
print("\n")

#accediendo a filas con edad mayor a 30
mayor_que_30 = df.loc[df["edad"]>30,:]
menor_que_30 = df.loc[df["edad"]<30,:]
print(mayor_que_30)
print("\n")
print(menor_que_30)
print("\n")


#############SLICING##############
cadena = "Kevin"
posicion="01234"
print(cadena[1:4])
##################################
