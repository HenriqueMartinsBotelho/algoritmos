import math

def binom(m,n):
  b = math.factorial(m)/(math.factorial(m-n)*math.factorial(n))
  return b
m = int( input("entre com m: "))
n = int( input("entre com n: ") ) 

while n>m:
  n = n-m

print("existem {0} formas de distribuir".format(binom(m,n)))