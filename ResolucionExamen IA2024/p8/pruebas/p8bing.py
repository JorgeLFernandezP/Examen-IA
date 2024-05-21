import itertools

# Definimos los nodos del grafo
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Obtenemos todas las permutaciones de los nodos
# Cada permutación representa un camino posible
caminos = list(itertools.permutations(nodos))

# Imprimimos los caminos
for camino in caminos:
    print(camino)
