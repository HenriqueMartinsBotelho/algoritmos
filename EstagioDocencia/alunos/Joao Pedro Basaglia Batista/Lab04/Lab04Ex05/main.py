import numpy
n = int(input("\n Entre com n: "))
A = []        
for i in range(n):
 A.append(i)
#A = [1, 2, 0, 3]
#A = [3, 4, 0, 1, 2]
A = numpy.random.permutation(A)
print(A)
#B = [2, 1, 0, 3]
#B = [1, 2, 3, 4, 0]
B = numpy.random.permutation(A)
print(B)
i = 0
while (A[0]!=B[i]): i += 1
j = n-i
i = 0
while (i<n-1) and (j-i>1):
 if (A[i]==B[n-j+i]): i += 1
 else: break
if (i==n-1): 
 print("\n Permutação cíclica com j = {0}.".format(j))
 exit(1)
elif (j-i!=1): 
 print("\n Permutação não-cíclica, j = {0}.".format(n))
 exit(1)
else:
 i = 0
 while (i<n-j-1):
  if (B[i]==A[j+i]): i += 1 
  else: break
if i==n-j-1: print("\n Permutação cíclica com j = {0}.".format(j))
else: print("\n Permutação não-cíclica, j = {0}.".format(n))

