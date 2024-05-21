import random
import itertools

# Definir el grafo del agente viajero
grafo = {
    'A': {'B': 2, 'C': 3, 'D': 5},
    'B': {'A': 2, 'C': 4, 'D': 6},
    'C': {'A': 3, 'B': 4, 'D': 7},
    'D': {'A': 5, 'B': 6, 'C': 7}
}

# Obtener todos los nodos del grafo
nodos = list(grafo.keys())

# Obtener todas las permutaciones de los nodos para la población inicial
poblacion_inicial = list(itertools.permutations(nodos))

# Función para calcular la distancia total de un camino
def calcular_distancia(camino):
    distancia_total = 0
    for i in range(len(camino) - 1):
        distancia_total += grafo[camino[i]][camino[i+1]]
    distancia_total += grafo[camino[-1]][camino[0]]  # Añadir la distancia de regreso al inicio
    return distancia_total

# Algoritmo genético
# Algoritmo genético
def algoritmo_genetico(poblacion_inicial, n_generaciones):
    poblacion = poblacion_inicial
    mejores_caminos = []
    for _ in range(n_generaciones):
        # Filtrar la población para incluir solo caminos válidos
        poblacion = [camino for camino in poblacion if all(nodo in camino for nodo in nodos)]
        if not poblacion:  # Verificar si la población está vacía
            break
        # Calcular la aptitud de cada individuo
        fitness = [(individuo, calcular_distancia(individuo)) for individuo in poblacion]
        # Guardar el mejor camino de esta generación
        mejor_camino_actual = min(fitness, key=lambda x: x[1])[0]
        mejores_caminos.append(mejor_camino_actual)
        # Seleccionar a los padres (por ejemplo, selección de torneo)
        padres = random.sample(fitness, k=len(poblacion)//2)
        # Cruzar a los padres para producir hijos (por ejemplo, cruce de un punto)
        hijos = []
        for padre1, padre2 in zip(padres[::2], padres[1::2]):
            punto_cruce = random.randint(1, len(padre1[0])-1)
            hijo1 = padre1[0][:punto_cruce] + padre2[0][punto_cruce:]
            hijo2 = padre2[0][:punto_cruce] + padre1[0][punto_cruce:]
            hijos.extend([hijo1, hijo2])
        # Mutar a los hijos (por ejemplo, intercambio de posición)
        for i in range(len(hijos)):
            if random.random() < tasa_mutacion:
                idx1, idx2 = random.sample(range(len(hijos[i])), k=2)
                hijos[i] = list(hijos[i])
                hijos[i][idx1], hijos[i][idx2] = hijos[i][idx2], hijos[i][idx1]
                hijos[i] = ''.join(hijos[i])
        # Reemplazar a la población con la nueva generación
        poblacion = hijos
    return mejores_caminos


# Parámetros del algoritmo genético
n_generaciones = 10
tasa_mutacion = 0.1

# Ejecutar el algoritmo genético
mejores_caminos = algoritmo_genetico(poblacion_inicial, n_generaciones)

# Mostrar todos los caminos encontrados
for i, camino in enumerate(mejores_caminos):
    distancia = calcular_distancia(camino)
    nodos = [nodo for nodo in camino]
    print(f"Generación {i+1}: {camino} (Distancia: {distancia}, Vector de nodos: {nodos})")
