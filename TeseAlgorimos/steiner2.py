import numpy as np

class Vertice():
    def __init__(self, num, position, peso):
        self.num = num
        self.peso = peso
        self.position = position

class Graph():
    def __init__(self):
        self.vertices = []
        self.arestas =  []
        self.adjList = {}

    def addVertice(self, num, position, peso):
        nv = Vertice(num, position, peso)
        self.vertices.append(nv)

    def getVertices(self):
        return self.vertices

    def addAresta(self, v1, v2):
        self.arestas.append([v1, v2])

    def getArestas(self):
        return self.arestas

    def addAdjList(self, arestas):
        for a in arestas:
            v1 = a[0]
            self.adjList.setdefault(v1, [])
            v2 = a[1]
            self.adjList.setdefault(v2, [])

            self.adjList[v1].append(v2)
            self.adjList[v2].append(v1)

    def getAdjList(self):
        return self.adjList



# Criando a árvore de Prim conforme modelo
tree = Graph()
tree.addVertice(0, [3,3], 1)
tree.addVertice(1, [4,7], 1)
tree.addVertice(2, [6,2], 1)
tree.addVertice(3, [11,4], 1)
tree.addVertice(4, [3,1], 1)
tree.addVertice(5, [10,3], 1)
tree.addVertice(6, [13,5], 1)
tree.addVertice(7, [13,2], 1)
tree.addVertice(8, [10,6], 1)
tree.addVertice(9, [1,4], 1)
tree.addAresta(0, 1)
tree.addAresta(0,4)
tree.addAresta(0,4)
tree.addAresta(0,2)
tree.addAresta(2,5)
tree.addAresta(3,5)
tree.addAresta(3,8)
tree.addAresta(3,6)
tree.addAresta(3,7)

vertices = tree.getVertices()
arestas = tree.getArestas()
tree.addAdjList(arestas)
Adj = tree.getAdjList()
#print(Adj)

def angulo(a,b,c):
    xa = b[0] - a[0]
    ya = b[1] - a[1]
    xb = c[0] - a[0]
    yb = c[1] - a[1]
    v1 = [xa, ya] 
    v2 = [xb, yb]
    v1 = np.array(v1)
    v2 = np.array(v2)
    prodEscalar = np.dot(v1,v2)
    mod1 = np.linalg.norm(v1)
    mod2 = np.linalg.norm(v2)
    return prodEscalar/(mod1 * mod2)

for v in Adj:
    grauV = len(Adj[v])
    if grauV > 1: #se o grau de v > 1
        for i in range(grauV):
            for j in range(i+1, grauV):
                x = Adj[v]
                a = angulo(vertices[v].position, vertices[x[i]].position, vertices[x[j]].position)
                print(a)
                #print(vertices[].position)
                #print(vertices[x[j]].position)
                #print(v, x[i], x[j]) #Calcula ângulo
                #print(vertices[v].position)

    