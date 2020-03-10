posicoes = set(input("Entre as posições (a,b) (c,d) (e,f) (g,h): \n").split(' '))
validas = {'(2,1)','(4,2)','(1,3)','(3,4)'}
ok = posicoes.intersection(validas) == validas
print(ok)
