lista = list(map(int, input("Digite 3 ou mais inteiros ").split()))

def achaTerceiro(lista):
    # Ordenando a lista
    for i in range(len(lista)):   
        indiceMenor = i 
        for j in range(i+1, len(lista)): 
            if lista[indiceMenor] > lista[j]: 
                indiceMenor = j 
        lista[i], lista[indiceMenor] = lista[indiceMenor], lista[i] 
    # Achando o terceiro menor levando em conta repetições
    j = 0
    for i in range(len(lista)):
        if lista[i] == lista[i+1]:
            pass
        else:
            j +=1
            if j == 3:
                return lista[i]


ter = achaTerceiro(lista)

print(ter)