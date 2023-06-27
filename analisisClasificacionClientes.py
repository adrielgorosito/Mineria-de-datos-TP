import pandas as pd                 # Análisis de datos
import numpy as np                  # Funciones matemáticas
import matplotlib.pyplot as plt     # Gráficas
import seaborn as sns               # Gráficas mejoradas

# Importe de datos
path = "CSV/clasificacion_clientes.csv"
data = pd.read_csv(path, sep=';', encoding='utf-8')



# Previsualización de datos
print(data.head())
data.info()
print(data.describe())



# Gráfico de barras para cada variable en relación al tipo de bicicleta
variables = ['TotalHijos', 'CantHijosEnCasa', 'CantAutomoviles', 'Ocupacion', 'Educacion', 'EstadoCivil', 'Propietario', 'Region', 'Genero']
bicicleta_values = ['Basic', 'Kinder y Sports']

for variable in variables:
    variable_categories = data[variable].unique()
    frequencies = data.groupby([variable, 'Tipo Bicicleta']).size().unstack(fill_value=0)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.arange(len(variable_categories))
    bar_width = 0.35
    
    for value in bicicleta_values:
        bars = ax.bar(x, frequencies[value], bar_width, label=value)
        x = x + bar_width
    
    ax.set_xticks(np.arange(len(variable_categories)) + bar_width / 2)
    ax.set_xticklabels(variable_categories)
    ax.set_xlabel(variable)
    ax.set_ylabel('Frecuencia')
    ax.set_title(f'Frecuencia de categorías de bicicleta por {variable}')
    ax.legend()

    plt.show()



# Gráfico de barras para cada variable en relación al número de cluster
variables = ['TotalHijos', 'CantHijosEnCasa', 'CantAutomoviles', 'Ocupacion', 'Educacion', 'EstadoCivil', 'Propietario', 'Region', 'Genero']
cluster_values = ['Cluster-1', 'Cluster-2', 'Cluster-3']  # Valores de la variable "$T-Bietápico"
new_labels = {'Cluster-1': 'Basic', 'Cluster-2': 'Kinder y Sports', 'Cluster-3': 'Basic'}

for variable in variables:
    variable_categories = data[variable].unique()
    frequencies = data.groupby([variable, '$T-Bietápico']).size().unstack(fill_value=0)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    bar_width = 0.2
    cluster_spacing = 0
    value_spacing = 0.5
    
    for i, value in enumerate(cluster_values):
        x = np.arange(len(variable_categories))
        bars = ax.bar(x + (bar_width + cluster_spacing) * i, frequencies[value], bar_width, label=value + ": " + new_labels[value])
    
    ax.set_xticks(np.arange(len(variable_categories)) + ((bar_width + cluster_spacing) * len(cluster_values)) / 2)
    ax.set_xticklabels(variable_categories)
    ax.set_xlabel(variable)
    ax.set_ylabel('Frecuencia')
    ax.set_title(f'Frecuencia de categorías de Cluster por {variable}')
    ax.legend()
    plt.subplots_adjust(wspace=value_spacing)
    
    plt.show()