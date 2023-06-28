import pandas as pd                 # Análisis de datos
import numpy as np                  # Funciones matemáticas
import matplotlib.pyplot as plt     # Gráficas
import seaborn as sns               # Gráficas mejoradas

# Importe de datos
path = "CSV/Destinatarios_predecidos.csv"
data = pd.read_csv(path, sep=';', encoding='latin-1')



# Previsualización de datos
print(data.head())
data.info()
print(data.describe())



# Diagrama de caja y bigotes para algunas variables
sns.set_style("whitegrid")
fig, ax = plt.subplots(2, 2, figsize=(11, 6))
plt.subplots_adjust(bottom=0.2, wspace=0.5, hspace=0.4)

sns.boxplot(data=data, x="CantHijosEnCasa", ax=ax[0, 0], color="steelblue")
ax[0, 0].set_title("Boxplot de CantHijosEnCasa")

sns.boxplot(data=data, x="TotalHijos", ax=ax[0, 1], color="steelblue")
ax[0, 1].set_title("Boxplot de TotalHijos")

sns.boxplot(data=data, x="Edad", ax=ax[1, 0], color="steelblue")
ax[1, 0].set_title("Boxplot de la Edad")

sns.boxplot(data=data, x="CantAutomoviles", ax=ax[1, 1], color="steelblue")
ax[1, 1].set_title("Boxplot de CantAutomoviles")

plt.show()



# Histograma para algunas variables
sns.set_style("whitegrid")
fig, ax = plt.subplots(2, 2, figsize=(11, 6))
plt.subplots_adjust(bottom=0.2, wspace=0.5, hspace=0.4)

sns.histplot(data=data, x="CantAutomoviles", ax=ax[0, 0], color="steelblue")
ax[0, 0].set_title("Histograma de la cantidad de autos")

sns.histplot(data=data, x="Edad", ax=ax[0, 1], color="steelblue")
ax[0, 1].set_title("Histograma de la edad")

sns.histplot(data=data, x="TotalHijos", ax=ax[1, 0], color="steelblue")
ax[1, 0].set_title("Histograma del total de hijos")

sns.histplot(data=data, x="CantHijosEnCasa", ax=ax[1, 1], color="steelblue")
ax[1, 1].set_title("Histograma de la cantidad de hijos en casa")

plt.show()



# Gráfico de barras para cada variable en relación a la predicción
variables = ['TotalHijos', 'CantHijosEnCasa', 'CantAutomoviles', 'Ocupacion', 'Educacion', 'EstadoCivil', 'Propietario', 'Region', 'Genero']
prediction_values = [0, 1]

for var in variables:
    variable_categories = data[var].unique()
    frequencies = data.groupby([var, 'prediction(ComproBicicleta)']).size().unstack(fill_value=0)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.arange(len(variable_categories))
    bar_width = 0.35
    
    for value in prediction_values:
        label = "Comprará bicicleta" if value == 1 else "No comprará bicicleta"
        bars = ax.bar(x, frequencies[value], bar_width, label=label)
        x = x + bar_width
    
    ax.set_xticks(np.arange(len(variable_categories)) + bar_width / 2)
    ax.set_xticklabels(variable_categories)
    ax.set_xlabel(var)
    ax.set_ylabel('Frecuencia')
    ax.set_title(f'Frecuencia de predicciones por categoría de {var}')
    ax.legend()
    
    plt.show()