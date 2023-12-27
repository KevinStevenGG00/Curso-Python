import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\Problemas_de_graficos\\data_ingresos.csv")

#creando el grafico
sns.barplot(x="fuente",y="ingresos",data=df)

#obteniendo total de ingresos
total=df["ingresos"].sum()

#mostrando total
print(f"El ingreso total es de: {total} soles")

#mostrando el gráfico
plt.show()
