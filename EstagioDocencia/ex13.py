lista = list(map(int, input().split()))

#Verifica se a lista tem um tamanho possível de ser fazer uma
# piramede i.e se o tamno dela pertence a lista da soma dos
# n primeiros naturais: 1 ou 3 ou 6 ou 10 ou 15 etc...
def verifica(x):
    soma = 0
    i = 0
    while soma <= x:
        soma += i
        i += 1
        if soma == x:
            return True
    return False

passo_i = 0
passo_j = 1

for i in range(passo_i):
    if i % 2 == 0:
        pass
    else:
        return False
return True
passo_i = 2*passo_i - 1


assert verifica(1) == True
assert verifica(3) == True
assert verifica(6) == True
assert verifica(10) == True
assert verifica(15) == True
assert verifica(2) == False
assert verifica(4) == False
assert verifica(11) == False



