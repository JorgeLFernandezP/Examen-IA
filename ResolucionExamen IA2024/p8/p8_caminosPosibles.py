# -*- coding: utf-8 -*-
"""
8. Selecciones un grafo del AGENTE-VIAJERO
 con al menos 8 nodos, de los cuales obtenga 
 todos los posibles caminos con Python 
 (no solucione, solo obtenga todas las combinaciones)
"""

import itertools

# Definir el vector con elementos no numéricos
vector = ['a', 'b', 'c','d','e','f','g','h']

# Generar todas las permutaciones
permutaciones = list(itertools.permutations(vector))

# Imprimir las permutaciones
for i, perm in enumerate(permutaciones):
    print(f"camino {i+1}: {perm}")
