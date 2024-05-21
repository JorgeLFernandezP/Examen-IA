nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
matriz = [[0] * len(nodos) for _ in range(len(nodos))]

grafo = {
    'A': {'B': 2, 'C': 3, 'D': 5, 'E': 4, 'F': 7, 'G': 6, 'H': 9},
    'B': {'A': 2, 'C': 8, 'D': 9, 'E': 7, 'F': 1, 'G': 4, 'H': 3},
    'C': {'A': 3, 'B': 8, 'D': 5, 'E': 4, 'F': 1, 'G': 2, 'H': 3},
    'D': {'A': 5, 'B': 9, 'C': 5, 'E': 9, 'F': 7, 'G': 1, 'H': 8},
    'E': {'A': 4, 'B': 7, 'C': 4, 'D': 9, 'F': 2, 'G': 3, 'H': 5},
    'F': {'A': 7, 'B': 1, 'C': 1, 'D': 7, 'E': 2, 'G': 4, 'H': 6},
    'G': {'A': 6, 'B': 4, 'C': 2, 'D': 1, 'E': 3, 'F': 4, 'H': 7},
    'H': {'A': 9, 'B': 3, 'C': 3, 'D': 8, 'E': 5, 'F': 6, 'G': 7}
}

for nodo, conexiones in grafo.items():
    for destino, peso in conexiones.items():
        matriz[nodos.index(nodo)][nodos.index(destino)] = peso

print(matriz)
#for fila in matriz:
 #   print(fila)
