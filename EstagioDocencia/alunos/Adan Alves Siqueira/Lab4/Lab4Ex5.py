import numpy
n = int(input('\n Entre com n: '))
A = []
for i in range (n):
  A.append(i)
A = [3,4,0,1,2]
#A = numpy.random.permutation(A)
print(A)
B = [1,2,3,4,0]
#B = numpy.random.permutation(A)
print(B)
i = 0
while (A[0]!=B[i]): i += 1
j = n-i 
i = 0
while (i<n-1) and (j-i>1):
  if (A[i]==B[n-j+i]): i+=1
  else: break
if i==n-1: print('\n Permutaçao ciclica com j = {0}'.format(j))
else:
  i = 0
  while (i<n-j-1):
    if(B[i]==A[j+i]): i+= 1
    else: break
if i==n-j-1: print('\n Permutaçao ciclica com j = {0}'.format(j))
else: print('\n Permutaçao nao ciclica, j={0}'.format(n))