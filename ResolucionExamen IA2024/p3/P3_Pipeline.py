from sklearn.impute import SimpleImputer
from sklearn.preprocessing import Normalizer, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd

# Cargar el dataset
data = pd.read_csv('accidentesnumericosP3.csv')
print("Original Data:\n", data)

# Crear el pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(missing_values=np.nan, strategy="mean")),
    ('normalizer', Normalizer()),
    ('scaler', StandardScaler())
])

# Crear el ColumnTransformer aplicando el pipeline a cada columna
preprocessor = ColumnTransformer(
    [(f'pipe_{col}', pipeline, [col]) for col in data.columns],
    remainder='passthrough'  # Para manejar cualquier columna que no se procese
)

# Aplicar el preprocesador al DataFrame completo
dataNueva = preprocessor.fit_transform(data)

# Convertir de nuevo a DataFrame
dataNueva_df = pd.DataFrame(dataNueva, columns=data.columns)

print("Transformed Data:\n", dataNueva_df)
