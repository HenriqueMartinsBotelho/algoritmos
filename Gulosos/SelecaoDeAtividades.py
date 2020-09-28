S = [[1,2],[4,5],[3,6],[7,8],[8,9],[10,11]] #ordem crescente de termino

class Atividades:
    def __init__(self, inicio=0, fim=0):
        self.inicio = inicio
        self.fim = fim

a1 = Atividades(1,2)
a2 = Atividades(4,5)

def SelecaoDeAtividades(S):
	t = 0
	A = []
	for i in range(len(S)):
		if S[i][0] >= t:
			A.append(S[i])
			t = S[i][1]
	return A

atividades = SelecaoDeAtividades(S)
print(atividades)


