import os

class Ponto:
    def __init__(self, x,y,w):
        self.x = x
        self.y = y
        self.w = w

def printPonto(p):
    print(p.x, p.y, p.w)



#raiz = os.getcwd()
#os.chdir(raiz + "/Tese")
#print(os.getcwd())
#print(os.listdir())


def pontosFromFile():
    raiz = os.getcwd()
    os.chdir(raiz + "/Tese")
    pontos = []
    with open("cruzamentoTeste.txt", "r") as f:
        for l in f:
            row = l.split()
            p = Ponto(row[0],row[1], row[2])
            pontos.append(p)
    return pontos

pontos = pontosFromFile()

for p in pontos:
    printPonto(p)