#### Falta fazer rodar nao apenas para uma piramide de tamanho quatro mas para uma qualquer


# recebe uma lista e retorna outra lista cujos elementos
# sao a soma de cada linha da piramidade que a primeira lista definine
def piramide(lista):
    #x = 0
    somai = 0
    somap = 0
    x = 0
    h = 0
    vetor = []
    for i in range(5): #// TODO generalizar
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

lista = [10, 20 , 30, 40, 50, 60, 70, 80, 90, 100]
lista2 = [10, 20 , 31, 40, 50, 60, 70, 81, 90, 100]
#vetor = piramide(lista)

def parPiramidal(lista):
    lista = piramide(lista)
    lista.remove(0)
    print(lista)
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


print(parPiramidal(lista))
print(parPiramidal(lista2))

