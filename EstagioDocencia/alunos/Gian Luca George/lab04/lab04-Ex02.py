L = []
t = []

for i in range(1,6):
  for j in range(1,6):
    for k in range(1,6):
      for l in range(1,6):
        for n in range(1,6):
          if(i-j)*(i-k)*(i-l)*(i-n)*(j-k)*(j-l)*(j-n)*(k-l)*(k-n)*(l-n):
            t.append(i)
            t.append(j)
            t.append(k)
            t.append(l)
            t.append(n)
            L.append(t)
            t=[]

for i in range(0,120):
  print(L[i])