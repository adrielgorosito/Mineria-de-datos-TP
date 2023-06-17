# El clustering jerárquico es un método de agrupamiento que busca organizar los datos en grupos o 
# clusters de manera jerárquica, formando una estructura de árbol o dendrograma. En lugar de asignar 
# los datos directamente a un número fijo de clusters como en el caso del clustering k-means, el 
# clustering jerárquico construye una estructura de clusters anidados, donde cada cluster puede 
# contener subclusters más pequeños.

# Una ventaja del clustering jerárquico es que no requiere especificar previamente el número de 
# clusters. Además, puede ser útil cuando se desea explorar diferentes niveles de granularidad en la 
# estructura de clusters.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Importe de datos
path = "CSV/Dest_pred CSV.csv"
df = pd.read_csv(path, sep=';', encoding="utf-8")

print("Vista previa de las variables:\n\n")
df.info()


# Selecciona solo las variables numéricas
df_num = df.select_dtypes(include=['number'])


# Estandariza los valores para que tengan media 0 y desviación estándar 1
# scaler = StandardScaler()
scaler = MinMaxScaler()
df_est = pd.DataFrame(scaler.fit_transform(df_num), columns=df_num.columns)

print("\n\n\nVerificación de la estandarización:")
print(df_est['IngresoAnual'])


# Eliminación de variables despreciables
df_est = df_est.drop(["IdCiudad", "prediction(ComproBicicleta)", "Propietario"], axis=1)


# La función linkage() se utiliza para calcular las distancias y fusiones entre los clusters en el 
# clustering jerárquico. 
Z = linkage(df_est, method='centroid', metric='euclidean')


# Crea un dendrograma
plt.figure(figsize=(10, 6))
dendrogram(Z)
plt.title('Dendrograma de Clustering Jerárquico')
plt.xlabel('Muestras')
plt.ylabel('Distancia')
plt.show()


# Asigna los clústeres a las muestras
num_clusteres = 3
asignaciones = fcluster(Z, num_clusteres, criterion='maxclust')


# Agrega la variable "Cluster"
df_est['Cluster'] = asignaciones

# Observaciones por cluster
cluster_counts = df_est['Cluster'].value_counts()

# Gráfica de barras de observaciones por cluster
plt.bar(cluster_counts.index, cluster_counts.values)
plt.xlabel('Cluster')
plt.ylabel('Cantidad de Observaciones')
plt.title('Distribución de Observaciones por Cluster')
plt.show()




# # Subset de 100 observaciones
# df_subset = df_est.head(100)

# Z = linkage(df_subset, method='centroid', metric='euclidean')

# # Filtrar las asignaciones de clusters correspondientes a las primeras 100 observaciones
# num_clusteres = 3
# asignaciones = fcluster(Z, num_clusteres, criterion='distance')
# asignaciones_subset = asignaciones[:100]
# df_subset['Cluster'] = asignaciones
# cluster_counts = df_subset['Cluster'].value_counts()

# # Gráfica de barras de observaciones por cluster
# plt.bar(cluster_counts.index, cluster_counts.values)
# plt.xlabel('Cluster')
# plt.ylabel('Cantidad de Observaciones')
# plt.title('Distribución de Observaciones por Cluster')
# plt.show()