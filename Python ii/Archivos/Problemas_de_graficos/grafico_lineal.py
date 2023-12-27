import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\Problemas_de_graficos\\data.csv")

#creando el grafico
sns.lineplot(x="fecha",y="hrs_estudio",data=df)

#creando un punto en cierto momento
plt.plot("01-06",3,"o")

#mostrando el gráfico
plt.show()
