# -*- coding: utf-8 -*-
"""
a. Con Python sin uso de librerías, 
calcule del ultimo cuartil, 
percentil 80 por columna; 
explique qué significa en cada caso.
"""

import pandas as pd

print("PERCENTIL 80, SIN LIBRERIAS")
# Cargar el conjunto de datos
data = pd.read_csv('accidentesnumericos.csv')

# Obtener el nombre de todas las columnas
columnas = data.columns

# Calcular el percentil 80 para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
    
    # Ordenar los valores de la columna actual
    sorted_column = sorted(columna_actual)
    
    # Calcular el índice correspondiente al percentil 80
    percentil_80_index = int(len(sorted_column) * 0.80)
    
    # Obtener el valor del percentil 80
    percentil_80_valor = sorted_column[percentil_80_index]
    
    # Imprimir el percentil 80 de la columna actual
    print(f"Percentil 80 de la columna '{columna}': {percentil_80_valor}")
    
#----------------------------------------------------------------------------------------------------
