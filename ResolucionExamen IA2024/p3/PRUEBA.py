from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Datos de ejemplo
data = {'color': ['rojo', 'azul', 'verde', 'azul']}

df = pd.DataFrame(data)
print(df)

# Aplicación de OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)  # Usa 'sparse_output' en lugar de 'sparse'
encoded_data = encoder.fit_transform(df[['color']])

# Mostrar el resultado usando 'get_feature_names_out' en lugar de 'get_feature_names'
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['color']))
print(encoded_df)
