class Vertice:
	def __init__(self, peso = 0, nome = ''):
		self.peso = peso
		self.nome = nome

v1 = Vertice(2,'v1')
v2 = Vertice(30,'v2')
v3 = Vertice(100,'v3')
v4 = Vertice(200,'v4')
v5 = Vertice(50,'v5')
v6 = Vertice(4,'v6') 

vertices = [v1,v2,v3,v4,v5,v6]

def MaxSetCover(vertices,n):
    f = [0]*n
    solucao = []
    f[0] = v1.peso
    f[1] = v2.peso
    for i in range(6):
        if i > 1:
            f[i] = max(vertices[i].peso + f[i-2], f[i-1])
    return f[i] 

print(MaxSetCover(vertices,6))