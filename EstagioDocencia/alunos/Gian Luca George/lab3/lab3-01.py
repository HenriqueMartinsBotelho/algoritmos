import math

def binom(m,n):
  b = math.factorial(m)/( math.factorial(m-n)*math.factorial(n) )
  return b

m = int( input("Entre com o n�mero m: ") )
n = int( input("Entre com o n�mero n: ") )

while n>m:
  n=n-m

print("Existem {0} formas de distribuir".format(binom(m,n)))