# -*- coding: utf-8 -*-
"""
Del dataset del punto 1 realice en PYTHON, 
cinco algoritmos de preprocesamiento; 
dos de ellos deben ser onehotencoder y otro escalado
"""
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Cargar el conjunto de datos original
data = pd.read_csv('accident.csv')

print(data['SCH_BUS'])

# Aplicación de OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)  # Usa 'sparse_output' en lugar de 'sparse'
encoded_data = encoder.fit_transform(data[['SCH_BUS']])

# Mostrar el resultado usando 'get_feature_names_out' en lugar de 'get_feature_names'
encoded_COLUMNA = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['SCH_BUS']))
print(encoded_COLUMNA)