# -*- coding: utf-8 -*-
"""
6. En PYTHON grafique el arbol de decisión
 (puede no ser aplicable,
  pero obtenga una representación cercana).

"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz

# Leer el archivo de Excel
data = pd.read_csv('TREEACCIDENT.csv')

# Convertir variables categóricas a variables numéricas
data_encoded = pd.get_dummies(data)

# Separar las características y la variable objetivo
# Asumiendo que la última columna es la variable objetivo
X = data_encoded.iloc[:, :-1]  # Todas las columnas excepto la última
y = data_encoded.iloc[:, -1]   # La última columna

# Crear y entrenar el modelo de árbol de decisión
clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

# Exportar el árbol a formato DOT
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=X.columns,  
                                class_names=[str(cls) for cls in clf.classes_],  
                                filled=True, rounded=True,  
                                special_characters=True)  

# Crear un gráfico con Graphviz
graph = graphviz.Source(dot_data)  

# Renderizar el gráfico a un archivo y visualizarlo
graph.render("accident_tree")  # Esto creará un archivo accident_tree.pdf por defecto
graph.view()  # Esto abrirá el archivo en el visor predeterminado de tu sistema

# Concatenar las columnas de cada fila separadas por comas
data['concatenated'] = data.apply(lambda row: ','.join(row.values.astype(str)), axis=1)

# Guardar el DataFrame con la nueva columna en un nuevo archivo CSV
data.to_csv('Accident_concatenado.csv', index=False)




