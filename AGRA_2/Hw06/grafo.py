import matplotlib.pyplot as plt
import networkx as nx

# Lista de aristas (origen, destino, peso)
edges = [
    (18,20,7),(10,2,3),(7,19,29),(0,8,10),(1,7,17),(5,9,35),(7,16,23),(0,18,47),
    (5,15,13),(0,13,21),(17,1,26),(6,8,5),(13,14,33),(2,5,39),(19,17,6),(13,4,23),
    (9,15,50),(13,0,45),(1,17,19),(19,12,22),(13,20,38),(11,9,42),(12,4,30),(4,1,2),
    (10,13,38),(13,6,45),(14,13,37),(2,10,34),(7,1,16),(10,9,28),(8,6,31),(18,12,18),
    (10,3,3),(12,16,11),(16,1,43),(18,0,12),(9,11,38),(15,5,34),(10,18,14)
]

# Crear grafo dirigido
G = nx.DiGraph()

# Agregar aristas con peso
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Posicionamiento de nodos (circular para hacerlo prolijo)
pos = nx.circular_layout(G)

# Dibujar nodos y aristas
plt.figure(figsize=(12,12))
nx.draw(G, pos, with_labels=True, node_size=900, node_color='lightblue', arrows=True)

# Agregar etiquetas de los pesos
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

plt.title("Grafo Dirigido con Pesos", fontsize=15)
plt.show()