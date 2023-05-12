import pandas as pd                 # Análisis de datos
import numpy as np                  # Funciones matemáticas
import matplotlib.pyplot as plt     # Gráficas
import seaborn as sns               # Gráficas mejoradas
import statsmodels.api as sm        # ?
import pylab as py                  # ?

# Importe de datos
path = "CSV/clientes.csv"
data = pd.read_csv(path, sep=',', encoding='latin-1')


# # Previsualización de datos
# print(data.head())                   # Para corroborar que se importó correctamente
# data.info()                          # Para ver las columnas y tipos de datos de forma general
# print(data.describe())               # Para ver algunas medidas estadísticas


# # Generamos todos los valores que adquieren las columnas "Propietario" y "ComproBicicleta"
# # con el objetivo de asegurar que solo toman los valores 0 y 1.
# print(data["Propietario"].value_counts())
# print(data["ComproBicicleta"].value_counts())


# # Diagrama de caja y bigotes con cuatro subplots
# sns.set_style("whitegrid")

# fig, ax = plt.subplots(2, 2, figsize=(11, 6))               # Crea la figura de dos filas y dos columnas
# plt.subplots_adjust(bottom=0.2, wspace=0.5, hspace=0.4)     # Ajusta los márgenes para evitar solapamientos

# sns.boxplot(data=data, x="IngresoAnual", ax=ax[0, 0], color="steelblue")
# ax[0, 0].set_title("Boxplot de IngresoAnual")

# sns.boxplot(data=data, x="Edad", ax=ax[0, 1], color="steelblue")
# ax[0, 1].set_title("Boxplot de la Edad")

# sns.boxplot(data=data, x="TotalHijos", ax=ax[1, 0], color="steelblue")
# ax[1, 0].set_title("Boxplot de TotalHijos")

# sns.boxplot(data=data, x="CantAutomoviles", ax=ax[1, 1], color="steelblue")
# ax[1, 1].set_title("Boxplot de CantAutomoviles")

# plt.show()


# # Matriz S para analizar si hay alguna relación con "ComproBicicletas"
# data_numeric = data.select_dtypes(include=['float64', 'int64'])     # Nuevo DataFrame con solo columnas numéricas
# print(data_numeric.corr())

# # Matriz R para analizar la relación de otra forma
# # Debido a que los datos varían mucho, no es muy recomendable ver esta matriz
# print(data_numeric.cov())


# # Gráfica de dispersión de "ComproBicicleta" vs "Edad"
# sns.scatterplot(data=data, x="ComproBicicleta", y="Edad", color="grey")
# plt.title("Gráfica de dispersión ComproBicicleta vs Edad")

# plt.show()


# Rellenamos los datos nulos de "IngresoAnual"
c_ingAnual_na = data["IngresoAnual"].isna()                     # Generamos la serie booleana

print(data[c_ingAnual_na])                                      # Imprime 10 nulos

data.loc[c_ingAnual_na, "IngresoAnual"] = data.IngresoAnual.median()    # Rellenamos con la mediana

c_ingAnual_na2 = data["IngresoAnual"].isna()                    # Generamos otra serie booleana para corroborar

print(data[c_ingAnual_na2])                                     # No imprime nada (empty DataFrame)

print(data.describe())