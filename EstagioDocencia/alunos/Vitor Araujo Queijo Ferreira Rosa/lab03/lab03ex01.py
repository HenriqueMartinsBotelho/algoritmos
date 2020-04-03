import math


def binomio(m,n):
	# checar entradas para evitar erros na função de binomio
	try:
		binomio = (math.factorial(m))/(math.factorial(m-n)*math.factorial(n))
		return int(binomio)
	except Exception as e:
		return print("Entrada(s) invalida(s): {}, {}".format(m,n))

m = int(input("Numero de criancas (m): "))
n = int(input("Numero de doces (n): "))

if (m<0 or n<0):
	print("Alguma entrada nula!")
elif n>m:
	n = n - m

resultado = binomio(m,n)

if resultado:
	print("A combinacoes possiveis sao: {}".format(resultado))
