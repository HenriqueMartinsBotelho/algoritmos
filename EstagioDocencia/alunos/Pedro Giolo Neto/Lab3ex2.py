x = int(input("Entre com a linha da primeira coluna: "))
if (x == 1) or (x == 4):
	print("Instável")
	exit(1)
z = int(input("Entre com a linha da segunda coluna: "))
if (x == 2 and z != 4) or (x == 3 and u !=4):
	print("Instável")
	exit(1)
u=int(input("Entre com a terceira coluna: "))
if (x == 2 and u !=1) or (x == 3 and u !=4):
	print("Instável")
	exit(1)
p=int(input("Entre com a linha da quarta colna: "))
if (x == 2 and p != 3) or (x == 3 and p != 2):
	print("Instável")
	exit(1)
print("Estável")