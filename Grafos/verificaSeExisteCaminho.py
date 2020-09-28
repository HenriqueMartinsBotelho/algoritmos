class Grafo:
    def __init__(self, visinhos = [], visitado = 0, predecessor = None):
        self.visitado = visitado
        self.predecessor = predecessor
        self.visinhos = visinhos
    
v = Grafo()
u = Grafo()
v3 = Grafo()
v4 = Grafo()
v5 = Grafo()
v6 = Grafo()
v7 = Grafo()
v8 = Grafo()
v.visinhos = [u,v3,v4]
u.visinhos = [v5,v6]
v4.visinhos = [v7]


def verificaSeExisteCaminho(G,v,u):
    v.visitado = 1
    v.predecessor = v
    Fila = []
    Fila.append(v)
    while Fila != []:
        h = Fila[0]
        Fila.pop(0)
        for vert in h.visinhos:
            if vert.visitado == 0:
                vert.visitado = 1
                vert.predecessor = h
                Fila.append(vert)
    if u.visitado == 1:
        print("Existe caminho")
    else:
        print("Não existe caminho")

G = [v,u,v3,v4,v5,v6,v7,v8]


#Teste
verificaSeExisteCaminho(G,v,u) #Existe caminho entre u e v
verificaSeExisteCaminho(G,v,v8) #Não existe caminho entre u e v8

