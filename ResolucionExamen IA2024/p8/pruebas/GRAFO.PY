import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    'A': {'B': 2, 'C': 3, 'D': 5, 'E': 4},
    'B': {'A': 2, 'C': 4, 'D': 6, 'F': 3},
    'C': {'A': 3, 'B': 4, 'D': 7, 'G': 5},
    'D': {'A': 5, 'B': 6, 'C': 7, 'H': 4},
    'E': {'A': 4, 'F': 2, 'G': 3, 'H': 5},
    'F': {'B': 3, 'E': 2, 'G': 4, 'H': 6},
    'G': {'C': 5, 'E': 3, 'F': 4, 'H': 7},
    'H': {'D': 4, 'E': 5, 'F': 6, 'G': 7}
}


G = nx.Graph()

for nodo, vecinos in grafo.items():
    for vecino, peso in vecinos.items():
        G.add_edge(nodo, vecino, weight=peso)

pos = nx.spring_layout(G)
etiquetas = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
plt.show()
