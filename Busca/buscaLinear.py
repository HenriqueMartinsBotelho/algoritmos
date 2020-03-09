def buscaLinear(vetor,x):
    for i in range(0,len(vetor)):
        if vetor[i] == x:
            return i
    return None

result = buscaLinear([1,2,3,4,5],3)
print(result)