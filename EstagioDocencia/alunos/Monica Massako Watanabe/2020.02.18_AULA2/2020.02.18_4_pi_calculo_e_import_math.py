#Incluir biblioteca que permite extrair raiz de um numero
import math

#Inserir um comando para calculo de pi
def pi1():
  return math.sqrt((7+math.sqrt(6+math.sqrt(5))))


#Função desenvolvida por S. Irvine
def pi2():
  return math.sqrt(math.sqrt((3**4)+((19**2)/(78-56))))

print(pi1()) 
print(pi2())
print(math.pi)
print(math.pi - pi1())