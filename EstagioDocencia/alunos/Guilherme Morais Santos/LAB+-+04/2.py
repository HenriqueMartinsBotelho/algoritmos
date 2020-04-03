L = []
t = []

for i in range (1,6):
  for j in range (1,6):
    for k in range (1,6):
      for l in range (1,6):
        for m in range (1,6):
          if (i-j)*(i-k)*(i-l)*(j-k)*(j-l)*(k-l)*(m-i)*(m-j)*(m-k)*(m-l):
            t.append(i)
            t.append(j)
            t.append(k)
            t.append(l)
            t.append(m)
            L.append(t)
            t=[]

for i in range(0,120):
 print(L[i])
