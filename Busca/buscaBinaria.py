
def buscaBinaria(vetor,procurado):
    esquerda = 0
    direita = len(vetor) - 1
    while esquerda <= direita:
        meio = (esquerda + direita)//2
        if procurado == vetor[meio]:
            return meio
        if procurado < vetor[meio]:
            direita = meio - 1
        else:
            esquerda = meio + 1 
    
    return None


print(buscaBinaria([2,3,5,7,11,13,17],5))
print(buscaBinaria([2,3,5,7,11,13,17],17))
print(buscaBinaria([2,3,5,7,11,13,17],19))
