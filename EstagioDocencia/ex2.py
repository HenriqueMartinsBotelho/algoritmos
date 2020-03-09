# Entrada no formato (a,b) (c,d) (e,f) (g,h)
posicoes = set(input().split(' '))
validas = {'(2,1)','(4,2)','(1,3)','(3,4)'}
ok = posicoes.intersection(validas) == validas
print(ok)
