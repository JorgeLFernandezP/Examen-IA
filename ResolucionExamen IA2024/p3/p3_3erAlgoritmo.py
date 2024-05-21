# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:08:59 2024

@author: USUARIO
"""

import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np

# Cargar el conjunto de datos original
data = pd.read_csv('accidentesnumericosP3.csv')
print(data)

# Crear el SimpleImputer
pepo = SimpleImputer(missing_values=np.NaN, strategy="mean")

# Aplicar el SimpleImputer a todo el DataFrame
dataN = pepo.fit_transform(data)

# Convertir el resultado de nuevo en DataFrame
data_imputed = pd.DataFrame(dataN, columns=data.columns)

print(data_imputed)
