import math
def norm(A:[float]) -> float:
  u = sum(A)/len(A) #ok
  y = sum((A[i]**2 for i in range (len(A)))) #ok
  s = math.sqrt(y/len(A) - u**2)
  B = []
  for j in range (len(A)):
    k = A[j]-u
    l = k/s 
    B.append(l)
    k,l=0.0,0.0
  return (u, s, B)

def conceito(s:float, B:[float]) -> str:
  C = []
  for j in range (len(B)):
    if B[j] < 0:
      C.append("F")
    elif 0 <= B[j] < s/2:
      C.append("D")
    elif s/2 <= B[j] < s:
      C.append("C")
    elif s <= B[j] < 3*s/2:
      C.append("B")
    else:
      C.append("A")
  return (C) 

