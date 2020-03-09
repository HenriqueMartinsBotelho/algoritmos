final = ("estavel")
x = int(input("Entre com a linha da primeira coluna: "))
if x==1 or x==4:
  print("Instavel!")
  exit(1)
y = int(input("Entre com a linha da segunda coluna: "))
if (y==2 and y!=4) or (y==3 and y!=1):
  print("Instavel")
  exit(1)
z = int(input("Entre com a linha da terceira coluna: "))
if (y==4 and z!=1) or (y==1 and z!=4):
  print("Instavel")
  exit(1)
w = int(input("Entre com a linha da quarta coluna: "))
if (z==1 and w!=3) or (z==4 and w!=2):
  print("instavel")
  exit(1)
print("ESTAVEL!")


