def f(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

lista = list(map(int, input("Digite a lista: ").split()))
print(f(lista))



### TESTES ###

assert f([1,2,3,4,5]) == False
assert f([1,2,3,3,4,5]) == True
assert f([1,2,3,1]) == True
