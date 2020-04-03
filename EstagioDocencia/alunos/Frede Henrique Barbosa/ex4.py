import numpy
n= int(input('Digite o valor n: '))
A=[]
for i in range(n):
    A.append(i)
A=[3,4,5,0,1,2]   
#A= numpy.random.permutation(A)
#print(A)
i=0
ok=1
while(i<n-1) and ok:
    if A[i+1]!=A[i]+1: ok=0
    i+=1
if (i==n-1):
    if ok:
        print('Permutação ciclica com j={0}.'.format(0))
        exit(1)
else: 
    if A[i]==0:
      i+=1
      j=i
      while(i<n-1):
          if A[i+1]!=A[i]+1: ok=0
          i+=1
if (i==n-1): print('Permutação ciclica com j={0}.'.format(j))
else: print('Permutação não ciclica, j={0}'.format(n))