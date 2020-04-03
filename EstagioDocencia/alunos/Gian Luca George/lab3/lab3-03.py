import math

def sen_x (x: float, eps: float) -> float:
  c  = 0.0
  fj = 0.0
  fk = x
  k  = 1
  while abs(fk - fj) >= eps:
    c, fj, k = c+fk, fk, k+1
    fk *= (-x*x/((2*k-1)*(2*k-2)))
  return c

x = float( input("Entre com x: "))
eps = 0.0001
print("O sen de {0} � aproximadamente {1}.".format(x,sen_x(x,eps)))