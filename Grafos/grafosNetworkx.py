import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_nodes_from([1,2,3,4])
#G.add_node(5)
G.add_edges_from([(1, 2), (1, 3)])
n = G.number_of_nodes()
m = G.number_of_edges()
print("Número de vértices",n)
print("Número de arestas", m)
print("Vértices:", G.nodes)
print("Arestas: ",G.edges)

for v in G.nodes:
    



####### PLOTANDO O GRAFO ########

options = {
    #'node_color': 'black',
    #'node_size': 100,
    #'width': 3,
    'with_labels': True, 
    'font_weight': 'bold'
}

nx.draw(G, **options)
plt.show()
