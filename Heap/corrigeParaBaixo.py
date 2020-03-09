def corrigeHeapParaBaixo(A,i):
	maior = i
	if (2*i + 1) < len(A):
		if A[2*i + 1] > A[maior]:
			maior = 2*i + 1
	if (2*i + 2) < len(A):
		if A[2*i + 2] > A[maior]:
			maior = 2*i + 2
	if maior != i:
		temp = A[i]
		A[i] = A[maior]
		A[maior] = temp
		corrigeHeapParaBaixo(A,maior)


vetor = [7,8,9,4,3,2]
corrigeHeapParaBaixo(vetor,0)
print(vetor)