import math

#Rainha 1 - (x,y) 
#Rainha 2 - (z,w)
#Rainha 3 - (u,v)
#Rainha 4 - (p,q)

x = int( input("Entre com a linha da 1a coluna: "))
if (x==1) or (x==4) or (x<1) or (x>4):
  print ("Instável");
  exit(1)
z = int( input("Entre com a linha da 2a coluna: "))
if (x==2 and z!=4) or (x==3 and z!=1) or (z<1) or (z>4):
  print("Instável")
  exit(1)
u = int( input("Entre com a linha da 3a coluna: "))
if (x==2 and u!=1) or (x==3 and u!=4) or (u<1) or (u>4):
  print("Instavel")
  exit(1)
p = int( input("Entre com a linha da 4a coluna: "))
if (x==2 and a!=3) or (x==3 and a!=2) or (p<1) or (p>4):
  print("Instável")
  exit(1)
else:
  print("Parabéns")