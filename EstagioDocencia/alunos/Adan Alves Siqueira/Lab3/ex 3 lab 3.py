def sen_x (x: float, eps: float)->float:
  c, fj, fk, k = 0.0, 0.0, x, 1
  while abs(fk-fj) >= eps:
    c = c+fk
    fj = fk
    k = k + 1
    fk = fk*(-x*x/((2*k-1)*(2*k-2)))
  return c

x = float( input("entre com x: "))
eps = 0.0001;
print ("O sen de {0} eh aproximadamente {1}".format(x,sen_x(x,eps)))
