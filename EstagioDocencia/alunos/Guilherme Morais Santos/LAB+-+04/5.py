import numpy
n = int(input("\n Entre com n: "))
A = []
for i in range (n):
  A.append(i)

#A = [3,4,0,1,2]
A = numpy.random.permutation (A)
print (A)
B = numpy.random.permutation (A)
print (B)

i=0
while (A[0]!=B[i]): i += 1
j = n-1
i = 0
while (i<n-1) and (j-i>1):
 if (A[i]==B[n-j+i]): i += 1
 else: break
if i==n-1:print ("\n Permutação cíclica com j = {0}.".format(j))
else:
  i = 0
  while (i<n-1):
   if (B[i]==A[j+i]): i+= 1
   else: break
if (i==n-1): print ("\n Permutação cíclica com j = {0}.".format(j))
else: print ("\n Permutação não cíclica, j = {0}.".format (n))



