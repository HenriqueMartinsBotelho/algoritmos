a = input("Digite a: ")
b = input("Digite b: ")
c = input("Digite c: ")

d = float(b)**2 - 4*float(a)*float(c)

if float(d) < 0:
  print("N�o da pra encontrar os valores das raizes")
elif float(d) == 0:
  x1 = (-float(b) + d**0.5) / 2*float(a)
  print("As duas raizes s�o igual a " + float(x1))
else:
  x1 = (-float(b) + d**0.5) / 2*float(a) 
  x2 = (-float(b) - d**0.5) / 2*float(a)
  print("A raiz x1 � " + str(x1) + " e a raiz x2 � " + str(x2))