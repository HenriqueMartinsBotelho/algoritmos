x= int(input("Entre com a linha da 1a. coluna: "))
if (x==1) or (x==4):
  print ("Instável!")
  exit(1)
y= int(input("Entre com a linha da 2a. coluna: "))
if (x==2 and y!=4) or (x==3 and y!=1):
  print ("Instável!")
  exit(1)
z= int(input("Entre com a linha da 3a. coluna: "))
if (x==2 and z!=1) or (x==3 and z!=4):
  print ("Instável!")
  exit(1)
k= int(input("Entre com a linha da 4a. coluna: "))
if (x==2 and k!=3) or (x==3 and k!=2):
  print ("Instável!")
  exit(1)

print ("Estável!")