
import random

# Definimos los nodos del grafo
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Usamos random.sample para obtener una permutación aleatoria de los nodos
camino = random.sample(nodos, len(nodos))

# Imprimimos el camino
print(camino)
