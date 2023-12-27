import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos\\Problemas_de_graficos\\data_categoria_valor.csv")

#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#mostrando el gráfico
plt.show()