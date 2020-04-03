lista_posicoes = list()

def n_queens_simples(lista_posicoes: list)->None:
	contador = 0
	# inicializando o tabuleiro
	tabuleiro = [[0 for i in range(4)] for j in range(4)]
	# populando o tabuleiro, sendo 1 para as posicoes das rainhas
	try:	
		for elem in lista_posicoes:
			tabuleiro[elem[0]][elem[1]] = 1
	except IndexError:
		print(tabuleiro)
		return print("Entradas invalidas!")
	for linha in tabuleiro:
		if sum(linha)>1:
			return print("Instavel!")
	for i in range(4):
		contador += tabuleiro[i][i]
		if contador>1:
			return print("Instavel!")
	# using this method: https://stackoverflow.com/questions/6473679/transpose-list-of-lists
	tabuleiro_transposto = list(map(list, zip(*tabuleiro)))
	for linha in tabuleiro:
		if sum(linha)>1:
			return print("Instavel!")
	return print("Estável!")

def popula_lista():
	for k in range(4):
		x = int(input("Entre com o valor da linha da {}th rainha: ".format(k+1)))
		y = int(input("Entre com o valor da coluna da {}th rainha: ".format(k+1)))
		lista_posicoes.append((x,y))
	return lista_posicoes

n_queens_simples(popula_lista())
