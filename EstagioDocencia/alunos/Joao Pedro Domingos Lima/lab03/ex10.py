import math
def norm(A:[float]) -> float:
  u = sum(A)/len(A)
  y = sum((A[i]**2 for i in range (len(A))))
  s = math.sqrt(y/len(A) - u**2)
  B = []
  for j in range (len(A)):
    k = A[j]-u
    l = k/s 
    B.append(l)
    k,l=0.0,0.0
  return u, s, B
