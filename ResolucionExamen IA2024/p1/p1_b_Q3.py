# -*- coding: utf-8 -*-
"""
b. Realice lo mismo del inciso (a) con el uso de numpy y pandas
"""

import pandas as pd
print("TERCER QUARTIL (75%), CON LIBRERIAS PANDAS")

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
    cuartil_valor = columna_actual.quantile(0.75)
    
    # Imprimir el cuartil de la columna actual
    print(f" Tercer Cuartil de la columna '{columna}': {cuartil_valor}")
#---------------------------------

import numpy as np
print("TERCER QUARTIL (75%), CON LIBRERIAS NUMPY")
# Calcular el cuartil para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
        
    # Obtener el valor del cuartil
    
    cuartil_valor = np.percentile(columna_actual, 75, axis=0)
    
    # Imprimir el cuartil de la columna actual
    print(f" Tercer Cuartil de la columna '{columna}': {cuartil_valor}")



#*********************************************************************************
