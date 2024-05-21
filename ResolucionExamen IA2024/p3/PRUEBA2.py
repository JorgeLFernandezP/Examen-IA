from sklearn.preprocessing import LabelEncoder
import pandas as pd
# Datos de ejemplo
data = {'color': ['rojo', 'azul', 'verde', 'azul']}
df = pd.DataFrame(data)

# Aplicación de LabelEncoder
label_encoder = LabelEncoder()
df['color_encoded'] = label_encoder.fit_transform(df['color'])

# Mostrar el resultado
print(df)