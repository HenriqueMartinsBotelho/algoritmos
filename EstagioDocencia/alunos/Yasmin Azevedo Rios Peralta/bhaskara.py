a = int(input("valor de a:\n"))
b = int(input("valor de b:\n"))
c = int(input("valor de c:\n"))

delta = (b**2 - 4*a*c)


if delta<0 : 
	print"nao existe raiz real"

elif delta==0 :
	print"existe apenas uma raiz real"
else: 
	print"existem duas raizes reais"
