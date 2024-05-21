# -*- coding: utf-8 -*-

"""
c. Obtenga la media, mediana, moda y geométrica; 
explique la diferencia de los resultados 
y cuál de ellas se puede utilizar en un artículo científico.
"""

import pandas as pd
import numpy as np
from scipy import stats
print("MEDIA - MEDIANA - MODA - MGEOMETRICA")

# Cargar el conjunto de datos
data = pd.read_csv('accidentesnumericos.csv')

# Obtener el nombre de todas las columnas
columnas = data.columns

#---------------------------------


# Calcular el cuartil para cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
        
    # Calcular la media
    media = np.mean(columna_actual)

    # Calcular la mediana
    mediana = np.median(columna_actual)

    # Calcular la moda
    moda = columna_actual.mode().iloc[0]

    # Calcular la media geométrica
    datos_sin_ceros = columna_actual[columna_actual != 0]
    geometrica = stats.gmean(datos_sin_ceros)
    
    # Imprimir el cuartil de la columna actual
    print(f" Medidas de tendencia para la columna '{columna}':")
    print(f" MEDIA:{media} | MEDIANA:{mediana} | MODA:{moda} | MGEOMERICA: {geometrica}")
    
    
    
#---------------------------------

#*********************************************************************************
