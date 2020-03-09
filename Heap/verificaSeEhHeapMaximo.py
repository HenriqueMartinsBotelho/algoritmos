import math

count = 0

def corrigeHeapParaBaixo(A,i):
    global count
    maior = i
    if (2*i + 1) < len(A):
        if A[2*i + 1] > A[maior]:
            maior = 2*i + 1
    if (2*i + 2) < len(A):
        if A[2*i + 2] > A[maior]:
            maior = 2*i + 2
    if maior != i:
        count = count + 1
        temp = A[i]
        A[i] = A[maior]
        A[maior] = temp
        corrigeHeapParaBaixo(A,maior)
    return count


def constroiHeap(A):
    i = math.floor(len(A)/2)
    while i >= 0:
        corrigeHeapParaBaixo(A,i)
        i = i - 1

#vetor = [1,2,3,4,5,6,7,8]
vetor = [8,7,6,5,4,3,2,1]
constroiHeap(vetor)
print(vetor)
print(count)