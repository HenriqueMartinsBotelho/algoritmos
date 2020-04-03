L = []
t = []

for i in range(1,7):
  for j in range(1,7):
    for k in range(1,7):
      for l in range(1,7):
        for m in range(1,7):
          for n in range(1,7):
           if (i-j)*(i-k)*(i-l)*(i-m)*(i-n)*(j-k)*(j-l)*(j-m)*(j-n)*(k-l)*(k-m)*(k-n)*(l-m)*(l-n)*(m-n):
            t.append(i)
            t.append(j)
            t.append(k)
            t.append(l)
            t.append(m)
            t.append(n)
            L.append(t)
            t=[]

for i in range(0,720):
 print(L[i])