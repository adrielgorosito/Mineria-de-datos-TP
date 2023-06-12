import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = "CSV/clientes.csv"
data = pd.read_csv(path, sep=',', encoding='latin-1')

# ComproBicicleta
data = [3876, 2524]
labels = ['No', 'Si']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'ComproBicicleta'")
plt.show()

# EstadoCivil
data = [3504, 2894, 2]
labels = ['C', 'S', 'V']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'EstadoCivil'")
plt.show()

# Genero
data = [3177, 3223]
labels = ['F', 'M']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'Género'")
plt.show()

# Educación
data = [1150, 557, 1119, 1774, 1800]
labels = ['Secundaria', 'Secundaria en curso', 'Postgrado', 'Universitario en curso', 'Licenciatura']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'Educación'")
plt.show()

# Ocupación
data = [998, 1098, 821, 1537, 1946]
labels = ['Administrativo', 'Gestión', 'Obrero', 'Obrero especializado', 'Profesional']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'Ocupación'")
plt.show()

# Propietario
data = [2070, 4330]
labels = ['No', 'Si']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'Propietario'")
plt.show()

# CantAutomoviles
data = [1339, 1635, 2308, 578, 480]
labels = ['0', '1', '2', '3', '4']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'CantAutomoviles'")
plt.show()

sns.histplot(data=data, x="CantAutomoviles", color="steelblue")
plt.title("Gráfico de barras de 'CantAutomoviles'")
plt.show()

# TotalHijos
data = [1750, 1191, 1345, 748, 828, 538]
labels = ['0', '1', '2', '3', '4', '5']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'TotalHijos'")
plt.show()

sns.histplot(data=data, x="TotalHijos", color="steelblue")
plt.title("Gráfico de barras de 'TotalHijos'")
plt.show()

# Distancia
data = [2166, 1080, 1114, 1122, 918]
labels = ['0-1 Km.', '1-2 Km.', '2-5 Km.', '5-10 Km.', '10+ Km.']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'Distancia'")
plt.show()

sns.histplot(data=data, x="Distancia", color="steelblue")
plt.title("Gráfico de barras de 'Distancia'")
plt.show()


Región
data = [1880, 1, 3310, 1209]
labels = ['Centro', 'Noroeste', 'Norte', 'Sur']
plt.pie(data, labels=labels, autopct = '%0.0f%%')
plt.title("Variable 'Región'")
plt.show()

sns.histplot(data=data, x="Region", color="steelblue")
plt.title("Gráfico de barras de 'Region'")
plt.show()

# IngresoAnual
sns.histplot(data=data, x="IngresoAnual", color="steelblue")
plt.title("Gráfico de barras de 'IngresoAnual'")
plt.show()

# Edad
sns.histplot(data=data, x="Edad", color="steelblue")
plt.title("Histograma de 'Edad'")
plt.show()