# -*- coding: utf-8 -*-
"""
Del dataset del punto 1 realice en PYTHON, 
cinco algoritmos de preprocesamiento; 
dos de ellos deben ser onehotencoder y otro escalado
"""

import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

# Cargar el conjunto de datos original
data = pd.read_csv('accidentesnumericosP3.csv')
print(data['YEAR'])

# Crear el SimpleImputer
pepo = SimpleImputer(missing_values=np.NaN, strategy="mean")

# Asegurarse de que 'YEAR' es un DataFrame y no una Series
year_data = data[['YEAR']]

# Aplicar el SimpleImputer a la columna 'YEAR'
dataN = pepo.fit_transform(year_data)

# Convertir el resultado de nuevo en DataFrame
data['YEAR'] = dataN

print(data['YEAR'])

