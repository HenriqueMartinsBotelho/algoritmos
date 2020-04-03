import math 
def binom(m,n):
  b=math.factorial(m)/(math.factorial(m-n)*math.factorial(n))
  return b

m=int(input('Valor de m:'))
n=int(input('Valor de n:'))

while n>m: 
  n-=m

print('Exist {0} formas de distribuir'.format(binom(m,n)))

