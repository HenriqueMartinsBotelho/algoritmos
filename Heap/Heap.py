import math

def minHeapify(A,i):
	menor = i
	if (2*i + 1) < len(A):
		if A[2*i + 1] < A[menor]:
			menor = 2*i + 1
	if (2*i + 2) < len(A):
		if A[2*i + 2] < A[menor]:
			menor = 2*i + 2
	if menor != i:
		temp = A[i]
		A[i] = A[menor]
		A[menor] = temp
		minHeapify(A,menor)
		

def BuildHeap(A):
	i = math.floor(len(A)/2)
	while i >= 0:
		minHeapify(A,i)
		i-=1

#Remove o menor elemento de um Heap mínimo em O(log n) 
def getMin():
	print("Implementar")

vetor = [9,1,2,3,4,5,6]
BuildHeap(vetor)
print(vetor)

