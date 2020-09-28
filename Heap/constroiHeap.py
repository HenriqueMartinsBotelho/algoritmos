import math
from corrigeParaBaixo import corrigeHeapParaBaixo

def constroiHeap(A):
	i = math.floor(len(A)/2)
	while i >= 1:
		corrigeHeapParaBaixo(A,i)


vetor = [1,2,3,4,5,6]

constroiHeap(vetor) 

print(2+2)
print(vetor)