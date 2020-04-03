### Código ainda não testado

'''
Verifica se é possíveo construir uma com a lista
piramede i.e se o tamno dela pertence a lista da soma dos
n primeiros naturais: 1 ou 3 ou 6 ou 10 ou 15 etc...
Retorna a altura da piramida caso seja possível e False caso contrário '''
def tamanho(x):
    soma = 0
    i = 0
    while soma <= x:
        soma += i
        i += 1
        if soma == x:
            return i
    return False


''' recebe uma lista e retorna outra lista cujos elementos
são a soma de cada linha da piramidade que a primeira lista definine '''
def somaLinhas(lista):
    somai = 0
    somap = 0
    x = 0
    h = 0
    vetor = []
    for i in range(tamanho(len(lista))): 
        for j in range(i):
            if h % 2 == 0:
                somai = somai + lista[x]
            if h % 2 == 1:
                somap = somap + lista[x]
            x = x + 1
        if h % 2 == 0:
            vetor.append(somai)
        else:
            vetor.append(somap)
        h += 1
        somai = 0
        somap = 0
    return vetor


# Função principal. Retorna True se eh parPiramidal e False caso contrário
def parPiramidal(lista):
    lista = somaLinhas(lista)
    lista.remove(0)
    ok = False
    for i in range(len(lista)):
        if i % 2 == 0:
            if lista[i] % 2 == 0:
                ok = True
            else:
                return False
        if i % 2 == 1:
            if lista[i] % 2 == 1:
                ok = True
            else:
                return False
    return ok


lista = [10, 20 , 30, 40, 50, 60, 70, 80, 90, 100] #Esperado True
lista2 = [10, 20 , 31, 40, 50, 60, 70, 81, 90, 100] #Esperado False
print(parPiramidal(lista))
print(parPiramidal(lista2))