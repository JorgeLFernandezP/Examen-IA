# -*- coding: utf-8 -*-
"""
a. Con Python sin uso de librerías, 
calcule del ultimo cuartil, 
percentil 80 por columna; 
explique qué significa en cada caso.

"""
import pandas as pd

print("TERCER QUARTIL (75%), SIN LIBRERIAS")
# Cargar el conjunto de datos
data = pd.read_csv('accidentesnumericos.csv')

# Obtener el nombre de todas las columnas
columnas = data.columns

# Calcular el cuartil para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
    
    # Ordenar los valores de la columna actual
    sorted_column = sorted(columna_actual)
    
    # Calcular el índice correspondiente al cuartil deseado
    cuartil_index = int(len(sorted_column) * 0.75)
    
    # Obtener el valor del cuartil
    cuartil_valor = sorted_column[cuartil_index]
    
    # Imprimir el cuartil de la columna actual
    print(f" Tercer Cuartil de la columna '{columna}': {cuartil_valor}")

#-------------------------------------------------------
print("QUARTILES USANDO SOLO FUNCIONES")
# Calcular el cuartil para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
    
    # Ordenar los valores de la columna actual
    sorted_column = sorted(columna_actual)
    n = len(sorted_column)
    
    # Calcular los índices para los cuartiles
    nquartile = n // 2
    i = nquartile // 2
    q3i = 0
    
    # Calcular Q1, Q2 (mediana) y Q3
    if nquartile % 2 == 0:
        q1 = (sorted_column[i-1] + sorted_column[i]) / 2
        median = (sorted_column[n // 2 - 1] + sorted_column[n // 2]) / 2
        q3 = (sorted_column[q3i + nquartile + i - 1] + sorted_column[q3i + nquartile + i]) / 2
    else:
        q1 = sorted_column[i]
        median = sorted_column[n // 2]
        q3 = sorted_column[q3i + nquartile + i]
    
    # Imprimir los cuartiles de la columna actual
    print(f"Cuartiles de la columna '{columna}':")
    print("Q1 =", q1)
    print("Q2 (Mediana) =", median)
    print("Q3 =", q3)
    print("Interquartile =", q3 - q1)
    print()

#---------------------------------------------------------




#*********************************************************************************
