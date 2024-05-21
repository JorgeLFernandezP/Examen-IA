import random

# Definir los nodos del grafo
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Número total de combinaciones a mostrar
total_combinaciones = 50


# Mostrar combinaciones aleatorias
for i in range(total_combinaciones):
    combinacion_aleatoria = random.sample(nodos, len(nodos))
    print(f"Combinación {i+1}: {combinacion_aleatoria}")
