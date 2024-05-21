# -*- coding: utf-8 -*-
"""
Del dataset del punto 1 realice en PYTHON, 
cinco algoritmos de preprocesamiento; 
dos de ellos deben ser onehotencoder y otro escalado
"""
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Cargar el conjunto de datos original
data = pd.read_csv('accident.csv')


# Aplicación de LabelEncoder
label_encoder = LabelEncoder()
data['CLIMA_encoded'] = label_encoder.fit_transform(data['weather_lit'])

# Mostrar el resultado
print(data['weather_lit'],data['CLIMA_encoded'])