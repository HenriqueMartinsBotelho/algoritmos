def verificaHeap(A):
	for e in range(len(A)):
		if (2*e + 1) < len(A):
			if A[e] < A[e+1]:
				return False
		if (2*e + 2) < len(A):
			if A[e] < A[e+2]:
				return False
	return True

heapNaoMaximo = [7,8,9,4,3,2]
heapMaximo = [9,8,7,6,5,4,3]
x = verificaHeap(heapNaoMaximo)
y = verificaHeap(heapMaximo)
print(x)
print(y)