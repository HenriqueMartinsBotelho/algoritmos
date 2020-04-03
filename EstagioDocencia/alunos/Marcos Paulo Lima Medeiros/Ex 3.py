import numpy
n = int(input("\n Entre com n:"))
A = []
for i in range(1,n+1):
  A.append(i)

A = numpy.random.permutation(A)
print(A)

for i in range(n):
 if A[i]==i+1: print(i+1)