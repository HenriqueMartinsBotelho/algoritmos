def sen_x (x: float, eps: float) -> float:
  c = 0.0
  fj = 0.0
  fk = x
  k = 1
  while abs(fk - fj) >= eps:
    c = c+fk
    fj = fk
    k = k+1
    fk = fk*( -x*x/((2*k-1)*(2*k-2)))
  return c

x = float( input("Entre com x:"))
eps = 0.001
print("O sen de {0} é aproximadamente {1}.".format(x,sen_x(x,eps)))
