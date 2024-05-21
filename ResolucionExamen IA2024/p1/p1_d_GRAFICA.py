import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

print("MEDIA - MEDIANA - MODA - MGEOMETRICA")

# Cargar el conjunto de datos
data = pd.read_csv('accidentesnumericos.csv')

# Obtener el nombre de todas las columnas
columnas = data.columns

# Iterar sobre cada columna
for columna in columnas:
    # Seleccionar la columna actual
    columna_actual = data[columna]
        
    # Crear un histograma de la columna actual
    plt.figure()
    plt.hist(columna_actual, bins=30, color='skyblue', edgecolor='black')
    plt.title(f"Histograma de la columna '{columna}'")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()
