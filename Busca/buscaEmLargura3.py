class Grafo:
    def __init__(self, visinhos = [], visitado = 0, predecessor = None):
        self.visitado = visitado
        self.predecessor = predecessor
        self.visinhos = visinhos
    
v1 = Grafo()
v2 = Grafo()
v3 = Grafo()
v4 = Grafo()
v5 = Grafo()
v6 = Grafo()
v7 = Grafo()
v1.visinhos = [v2,v3,v4]
v2.visinhos = [v5,v6]
v4.visinhos = [v7]


def buscaEmLargura(G,s):
    s.visitado = 1
    s.predecessor = s
    Fila = []
    Fila.append(s)
    while Fila != []:
        u = Fila[0]
        Fila.pop(0)
        for v in u.visinhos:
            if v.visitado == 0:
                v.visitado = 1
                v.predecessor = u
                Fila.append(v)

G = [v1,v2,v3,v4,v5,v6,v7]

for v in G:
    print(v.visitado)

buscaEmLargura(G,v1)

for v in G:
    print(v.visitado)

