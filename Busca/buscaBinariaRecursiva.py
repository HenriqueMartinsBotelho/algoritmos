# Recebe um vetor ordenado (ordem não-decrescente) A com n elementos, i.e.,
# A [i] ≤ A [ i + 1] para todo 1 ≤ i ≤ n − 1.

def buscaBinariaRecursiva(A, x, inicio=0, fim=None):
    if fim is None:
        fim = len(A) - 1
    if inicio > fim:
        return False
    meio = (inicio + fim) // 2
    if x == A[meio]:
        return meio
    else:
        if x < A[meio]:
            return buscaBinariaRecursiva(A, x, inicio, meio-1)
        else:
            return buscaBinariaRecursiva(A, x, meio+1, fim)
    

result = buscaBinariaRecursiva([5,10,15,20,25,30,35,40],20)
print(result)