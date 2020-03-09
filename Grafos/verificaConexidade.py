class Vertice:
    def __init__(self, vizinhos = [], visitado = 0, predecessor = None):
        self.visitado = visitado
        self.predecessor = predecessor
        self.vizinhos = vizinhos
    
v = Vertice()
u = Vertice()
v3 = Vertice()
v4 = Vertice()
v5 = Vertice()
v6 = Vertice()
v7 = Vertice()
v8 = Vertice()
v.vizinhos = [u,v3,v4]
u.vizinhos = [v5,v6]
v3.vizinhos = [v]
v4.vizinhos = [v7]
v5.vizinhos = [u]
v6.vizinhos = [u]
v7.vizinhos = [v4]


def verificaSeExisteCaminho(G,v,u):
    v.visitado = 1
    v.predecessor = v
    Fila = []
    Fila.append(v)
    while Fila != []:
        h = Fila[0]
        Fila.pop(0)
        for vert in h.vizinhos:
            if vert.visitado == 0:
                vert.visitado = 1
                vert.predecessor = h
                Fila.append(vert)
    if u.visitado == 1:
        print("Existe caminho")
        return True
    else:
        print("Não existe caminho")
        return False

G = [v,u,v3,v4,v5,v6,v7,v8]

for vert in G:
    x = verificaSeExisteCaminho(G,u,vert)
    if x == True:
        pass
    else:
         print(x)
         break
print(x)

#Teste
#verificaSeExisteCaminho(G,v,u) #Existe caminho entre u e v
#z = verificaSeExisteCaminho(G,v,v8) #Não existe caminho entre u e v8

#print(z)