L = []
t = []

for i in range(1,5):
  for j in range (1,5):
    for k in range (1,5):
      for l in range (1,5):
        if (i-j)*(i-k)*(i-l)*(j-k)*(j-l)*(k-l):
          t.append(i)
          t.append(j)
          t.append(k)
          t.append(l)
          L.append(t)

          # t=[] --> sera a lista para rodar de novo
          t=[]
for i in range (0,24):
  print (L[i])        