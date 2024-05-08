import pandas as pd

import geopandas as gpd
from shapely.geometry import Point

import matplotlib.pyplot as plt


data = pd.read_csv("housing.csv")

# Cargar el shapefile en un GeoDataFrame
gdf_dis = gpd.read_file("California_Counties.shp")

# Ver las primeras filas del GeoDataFrame
print(gdf_dis.head())

# Ver la información del GeoDataFrame
print(gdf_dis.info())

# Ver la geometría de las primeras filas
print(gdf_dis.columns)



# Crear geometrías Point a partir de las columnas de latitud y longitud
# geometrias = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]

# # # Crear un GeoDataFrame a partir del DataFrame original y las geometrías Point
# gdf = gpd.GeoDataFrame(data, geometry=geometrias)

# # Realizar una unión espacial entre los condados y los datos
# datos_con_condados = gpd.sjoin(gdf, gdf_dis, how='left', op='within')

# print(datos_con_condados.head(50))

# 'how' determina el tipo de unión (en este caso, left join)
# 'op' especifica la operación espacial (en este caso, 'within' para determinar la ubicación dentro de los condados)


# print(gdf_dis.describe())
# print(gdf.head(59))

# puntos_en_distritos ahora contiene tus datos de coordenadas con una columna adicional
# que indica en qué distrito de California se encuentra cada punto

# Crear una figura y ejes
# fig, ax = plt.subplots(figsize=(10, 10))

# Dibujar el GeoDataFrame
# gdf_dis.plot(ax=ax, color='lightblue', edgecolor='k')
# gdf.plot(ax=ax, cmap='turbo')  # Puedes cambiar el colormap (cmap) según tu preferencia
# gdf.plot(ax=ax, cmap='turbo', alpha=0.5, markersize=10)

# # Añadir título y etiquetas
# ax.set_title('Distritos de California con Puntos de Datos', fontsize=16)
# ax.set_xlabel('Longitud', fontsize=12)
# ax.set_ylabel('Latitud', fontsize=12)

# # Mostrar la leyenda
# red_patch = plt.Line2D([0], [0], marker='o', color='w', label='Puntos de Datos', markerfacecolor='red', markersize=10)
# ax.legend(handles=[red_patch], loc='upper right')

# Mostrar el mapa
plt.show()

# print(gdf.head())


# data.dropna(inplace=True)
# print(data.describe())
# print(data.sort_values(by="total_bedrooms").head(5))
# print(data.info())
# print(data.describe())