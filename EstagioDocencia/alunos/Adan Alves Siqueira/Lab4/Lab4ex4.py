import numpy
n = int(input("\n Entre com n: "))
A = []
for i in range (n):
  A.append(i)
A = numpy.random.permutation(A)
print (A)

i=0
ok=1
while (i<n-1)and ok: 
  if A[i+1]!=A[i]+1: ok=0
  i+= 1

if (i==n-1):
  if ok:
    print('\n Permutação ciclica com j = {0}'.format(j))
    exit(1)
else:
  if A[i]==0:
    i +=1
    j = i
    while (i<n-1):
      if A[i+1]!=A[i]+1: ok=0
      i +=1

if ok==1: print('\n Permutação ciclica com j = {0}'.format(j))
else: print ('\n Permutaçao nao-ciclica, j={0}'.format(n))