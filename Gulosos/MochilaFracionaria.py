class Objetos:
  def __init__(self, peso=0, valor=0):
    self.peso = peso
    self.valor = valor
    

o1 = Objetos(10,20)
o2 = Objetos(30,5)
o3 = Objetos(15,50)

def getKey(O):
    return O.valor/O.peso

def ordena(O):
    O = sorted(O, key=getKey, reverse=True)
    return O
                

def mochilaFracionaria(O,c):
    O = ordena(O)
    pesoAtual = 0
    valor = 0
    i = 0
    n = len(O)
    while i < n and pesoAtual + O[i].peso < c:
        pesoAtual = pesoAtual + O[i].peso
        valor = valor + O[i].valor
        i = i + 1
    if i < n:
        valor = valor + (c - pesoAtual)/(O[i].peso) * O[i].valor

    return valor
    

resultado = mochilaFracionaria([o3,o1,o2],40)
print(resultado)
