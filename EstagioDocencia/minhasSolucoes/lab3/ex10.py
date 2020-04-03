lista = list(map(int, input("Digite a lista ").split()))

def plato(lista):
    if len(lista) == 0:
        return 0
    soma = 1
    maior = 1
    for i in range(len(lista) - 1):
        if lista[i] == lista[i+1]:
            soma += 1
        else:
            if soma >= maior:
                maior = soma
                im = i - soma
            soma = 1
    return [im + 1, im + maior]        


p = plato(lista)
print(p)


### Testes ####
assert plato([1,1,1,2,2,2,2,3,3]) == [3,6], "1 - aqui"
assert plato([1,1,1,1,1,2,2,2,2,3,3]) == [0,4], "2 - aqui"
assert plato([]) == 0, "3 - aqui"

