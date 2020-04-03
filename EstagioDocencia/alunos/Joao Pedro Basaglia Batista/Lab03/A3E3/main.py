import math

def sen_x(x: float, eps:float) -> float:
  c, fj, fk, k = 0.0, 0.0, x, 1
  while abs(fk - fj) >= eps:
    c, fj, k = c + fk, fk, k+1
    fk = fk*(-x*x/((2*k-1)*(2*k-2)))
  return c

x = float(input("Entre com x: "))
eps = 0.00001
print ("O seno de {0} é aproximadamente {1}.".format(x,sen_x(x,eps)))
