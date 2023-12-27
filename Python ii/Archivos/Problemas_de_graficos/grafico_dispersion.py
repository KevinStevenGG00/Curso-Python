import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\Problemas_de_graficos\\data_tiempo_dinero.csv")

#creando el grafico
sns.scatterplot(x="tiempo",y="dinero",data=df)

#mostrando el gráfico
plt.show()
