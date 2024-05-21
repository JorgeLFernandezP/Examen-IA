def encontrar_caminos(grafo, inicio, fin, visitado, camino):
    visitado[inicio] = True
    camino.append(inicio)
    if inicio == fin:
        print("Camino encontrado: ", ' -> '.join(camino))
    else:
        for vecino in grafo[inicio]:
            if visitado[vecino] == False:
                encontrar_caminos(grafo, vecino, fin, visitado, camino)
    camino.pop()
    visitado[inicio] = False

def contar_caminos(grafo):
    nodos = list(grafo.keys())
    total_caminos = 0
    for inicio in nodos:
        for fin in nodos:
            if inicio != fin:
                visitado = {nodo: False for nodo in nodos}
                camino = []
                encontrar_caminos(grafo, inicio, fin, visitado, camino)
                total_caminos += 1
    return total_caminos

grafo = {
    'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'B': ['A', 'C', 'D', 'E', 'F', 'G', 'H'],
    'C': ['A', 'B', 'D', 'E', 'F', 'G', 'H'],
    'D': ['A', 'B', 'C', 'E', 'F', 'G', 'H'],
    'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H'],
    'F': ['A', 'B', 'C', 'D', 'E', 'G', 'H'],
    'G': ['A', 'B', 'C', 'D', 'E', 'F', 'H'],
    'H': ['A', 'B', 'C', 'D', 'E', 'F', 'G']
}

print("Total de caminos únicos: ", contar_caminos(grafo))
