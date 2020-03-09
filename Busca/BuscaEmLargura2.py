import networkx as nx
import matplotlib.pyplot as plt


def BuscaEmLargura(G,s): 
    for v in G.nodes:
        if v != s:
            G.nodes[v]['visitado'] = 0
            G.nodes[v]['predecessor'] = None

    G.add_node(s) 
    G.nodes[s]['visitado'] = 1
    G.nodes[s]['predecessor'] = s

    F = []
    F.append(s)

    while F != []:
        u = F[0]
        F.pop(0) 
        for v in G.neighbors(u): 
            if G.nodes[v]['visitado'] == 0: 
                G.nodes[v]['visitado'] = 1 
                G.nodes[v]['predecessor'] = u 
                F.append(v) 
    

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5,6])
G.add_edges_from([(1, 2), (1, 3),(2,3),(2,4),(3,4),(5,6),(6,3)])
        
print(G.node.data())
print("\n ------- \n")
BuscaEmLargura(G,1)
print(G.node.data())

