# -*- coding: utf-8 -*-

"""
b. Realice lo mismo del inciso (a) con el uso de numpy y pandas
"""

import pandas as pd
print("PERCENTIL 80, CON LIBRERIAS PANDAS")

# Cargar el conjunto de datos
data = pd.read_csv('accidentesnumericos.csv')

# Obtener el nombre de todas las columnas
columnas = data.columns

#---------------------------------


# Calcular el cuartil para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
        
    # Obtener el valor del cuartil
    percentil_valor = columna_actual.quantile(0.80)
    
    # Imprimir el cuartil de la columna actual
    print(f" Percentil 80 de la columna '{columna}': {percentil_valor}")
#---------------------------------

import numpy as np
print("PERCENTIL 80, CON LIBRERIAS NUMPY")
# Calcular el cuartil para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
        
    # Obtener el valor del cuartil
    
    percentil_valor = np.percentile(columna_actual, 80, axis=0)
    
    # Imprimir el cuartil de la columna actual
    print(f" Percentil 80 de la columna '{columna}': {percentil_valor}")



#*********************************************************************************
