import math 

def binom(m,n):
  b = math.factorial(m)/(math.factorial(m-n)*math.factorial(n))
  return b

m = int(input("Entre com m: "))
n = int(input("Entre com n: "))

print ("O binom(m,n) é: {0}".format(binom(m,n)))
