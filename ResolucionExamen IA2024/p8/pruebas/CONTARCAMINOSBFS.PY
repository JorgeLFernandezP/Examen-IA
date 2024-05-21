from collections import deque

def bfs(grafo, inicio):
    visitados = {nodo: False for nodo in grafo}
    visitados[inicio] = True
    cola = deque([(inicio, [inicio])])
    caminos_unicos = set()
    
    while cola:
        nodo_actual, camino = cola.popleft()
        
        for vecino, _ in grafo[nodo_actual].items():
            if not visitados[vecino]:
                visitados[vecino] = True
                nuevo_camino = camino + [vecino]
                cola.append((vecino, nuevo_camino))
                caminos_unicos.add(tuple(nuevo_camino))
    
    return len(caminos_unicos)

def contar_caminos_unicos(grafo):
    total_caminos = 0
    for nodo in grafo:
        total_caminos += bfs(grafo, nodo)
    return total_caminos

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

total_caminos_unicos = contar_caminos_unicos(grafo)
print("El número total de caminos únicos en el grafo es:", total_caminos_unicos)
