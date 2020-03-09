import math

def imprime_apresentacao(x):
    print("Bem vindo a disciplina")
    print("Processamento da informação")
    print("x")
#mensagem de apresentacao
def numero_par(x):
  if x%2==0:
    return True
#entrega numero par
def numero_impar(x):
  if x%2!=0:
    return True
#entrega numero impar
def pp(x: int)->int:
  return qq(x) + qq(x+1)

def qq(y: int)->int:
  return y*2
#relacionando duas funcoes em um resultado
def funcaopi():
  return math.sqrt((7+math.sqrt(6+math.sqrt(5))))
#aproximacao de pi
def funcaopi2():
  return (math.sqrt(math.sqrt(3**4+((19**2)//78-56))))
#aproximacao de pi - teste 2
def fi(i):
  return ((((1+math.sqrt(5))/2)**i)-((((1-math.sqrt(5))/2))**i))/math.sqrt(5)
#funcao de fibonacci
def somaQ(n):
  soma=0
  for i in range(1,n+1):
    soma = soma + i
  return soma
#sequencia padronizada
def somaP(n):
  soma=0
  for i in range(1,n+1):
    soma = soma + i*((-1)**(i+1))
  return soma
#sequencia padronizada 2
print(somaP(6))