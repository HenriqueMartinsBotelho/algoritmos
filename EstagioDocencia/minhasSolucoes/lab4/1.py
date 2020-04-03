


#https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
def lex(lista):

    #Passo 1
    maiorI = -1
    for i in range(len(lista) -1):
        if lista[i] < lista[i+1]:
            maiorI = i
    if maiorI == -1:
        return 0

    #Passo 2
    maiorJ = -1
    for j in range(len(lista)):
        if lista[j] < lista[maiorJ]:
            maiorJ = j

    #Passo 3
    lista[i], lista[j] = lista[j], lista[i]

    #Passo 4
    lista[maiorI+1:len(lista)].reverse()


    return lista

lista = [4,3,1,0,10,11,2]
print(lex(lista))