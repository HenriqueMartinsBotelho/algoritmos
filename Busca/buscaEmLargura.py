G = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D'],
    'D':['B','C']}

visitados = {'A': 0,
              'B': 0,
              'C': 0,
              'D': 0}

fila = []



def BSF(G,s):
    fila.append(s) #adiciona s na fila
    visitados[s] == 1
    while fila != []:
        fila.pop(0) #remove o primeiro nó da fila
        for v in G[s]: #para cada vizinho de s
            if visitados[v] == 0:
                visitados[v] = 1
                fila.append(v)


for v in G:
    if visitados[v] == 0:
        BSF(G,v)


        
#print(listaDeAdjacencia['B'])

#print(visitados)
#BSF(G, 'B')
#print(visitados)
#print(fila)
#print(visitados)
