x = int( input("Entre com a linha da Primeira coluna:"))
if (x==1) or(x==4):
  print ("Instável!")
  exit(1)
z = int( input("Entre com a linha da Segunda coluna:"))
if (x==2 and z!=4) or (x==3 and z!=1):
    print("instavel")
    exit(1)
u = int( input("Entre com a linha da Terceira coluna"))
if (z==4 and u!=1) or (z==1 and u!=4):
  print("Instável")
  exit(1)
p = int(input("Entr com a linha da quarta coluna: "))
if (u==1 and p!=3) or (u==4 and p!=2):
    print ("instavel")
    exit(1)
else:
  print("Estável")