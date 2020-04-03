x = int(input("Entre com alinha da 1a. coluna: "))
if (x==1)or(x==4):
    print ("Instável ! ")
z = int(input("Entre com a 2a. coluna: "))
if (x==2 and z!=4) or(x==3 and z!=1):
    print ("Instável ! ")
    exit(1)
u = int(input("Entre com a 3a. coluna: "))
if (x==2 and u!=1) or(x==3 and u!=4):
    print ("Instável ! ")
    exit(1)
p = int(input("Entre com alinha da 4a. coluna: "))
if (x==2 and p!=3) or(x==3 and u!=2):
    print ("Instável ! ")
    exit(1)

print("ESTÁVEL!")

