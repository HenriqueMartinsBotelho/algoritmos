x = int( input("Entre com a linha da 1a. coluna: ") )
if (x==1)or(x==4):
  print ("Inst�vel!")
  exit(1)
z = int( input("Entre com a linha da 2a. coluna: ") )
if (x==2 and z!=4)or(x==3 and z!=1):
  print ("Inst�vel!")
  exit(1)
u = int( input("Entre com a linha da 3a. coluna: ") )
if (x==2 and u!=1)or(x==3 and u!=4):
  print ("Inst�vel!")
  exit(1)
p = int( input("Entre com a linha da 4a. coluna : ") )
if (x==2 and p!=3)or(x==3 and p!=2):
  print ("Inst�vel!")
  exit(1)