L = []
t = []

for i in range(1,6):
  for j in range (1,6):
    for k in range (1,6):
      for l in range (1,6):
        for m in range (1,6):
         if (i-j)*(i-k)*(i-l)*(i-m)*(j-k)*(j-l)*(j-m)*(k-l)*(k-m)*(l-m):
          t.append(i)
          t.append(j)
          t.append(k)
          t.append(l)
          t.append(m)
          L.append(t)

          # t=[] --> sera a lista para rodar de novo
          t=[]
for i in range (0,120):
  print (L[i])        