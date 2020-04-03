import matplotlib.pyplot as plt
import os
import sys
import graph
import math
import networkx as nx
import pandas as pd
import seaborn as sns
 

lista = []
abscissa = []
ordenada = []
def onclick(event):
    plt.scatter(event.xdata, event.ydata, c="red")
    plt.show()
    global lista
    a = (event.xdata, event.ydata)
    global abscissa
    global ordenada
    abscissa.append(event.xdata)
    ordenada.append(event.ydata)
    lista.append(a)
    







fig,ax = plt.subplots()
plt.axis([0, 100, 0, 100])
print("Aperta 1 para escolher pontos ou 2 para ler de um arquivo")
opcao = input()
if opcao == '1':
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    pontos = lista
    X = abscissa
    Y = ordenada
    #plt.axis([0, 100, 0, 100])
    #plt.scatter(X, Y, c="blue")
    #plt.show()
elif opcao == '2':
    X = []
    Y = []
    lista = []
    print("Digite o nome do arquivo")
    nome = input()
    with open(os.path.join(sys.path[0], nome), "r") as f:
        for linha in f:
            linha=linha.replace("\n","") 
            x, y = linha.split(" ")
            X.append(x)
            Y.append(y)
            a = (x, y)
            lista.append(a)
else:
    print("Opção inválida")


#Código começa aqui

G = nx.Graph()


def prim(V):
    X = [V[0]]
    Y = V[1:]
    A = []
    while len(X) < len(V):
        menor = math.inf
        for x in X:
            for y in Y:
                distance = math.sqrt(((float(x[0])-float(y[0]))**2)+((float(x[1])-float(y[1]))**2))
                if distance < menor:
                    menor = distance
                    e = (x,y)
                    yescolhido = y
        X.append(yescolhido)
        Y.remove(yescolhido)
        A.append(e)
    return A



#Funcao de Plotagem

def plota(aresta):
    abscissa = []
    ordenada = []
    abscissa.append(float(aresta[1][0]))
    abscissa.append(float(aresta[0][0]))
    ordenada.append(float(aresta[0][1]))
    ordenada.append(float(aresta[1][1]))
    #plt.plot(abscissa, ordenada)
    



pontos = lista
#X = abscissa
#Y = ordenada
A = prim(pontos)
print("pontos = ", pontos)

G = graph.Graph()

for e in A:
    G.add_edge(e)
    

#print("Arestas = ", G.edges())

abscissas = []
ordenadas = []
for aresta in A:
    abscissas.append(float(aresta[0][0]))
    abscissas.append(float(aresta[1][0]))
    ordenadas.append(float(aresta[0][1]))
    ordenadas.append(float(aresta[1][1]))


print(abscissas)
print(ordenadas)

#plt.plot(abscissas,ordenadas)
#plt.scatter(abscissas, ordenadas, c="red")

plt.axis([0, 100, 0, 100])
#plt.show()

plt.show()




















print("Type s to save the file")
s = input()
if opcao == '2':
    if s == 's':
        print("Choose file name")
        nome = input()
        with open(os.path.join(sys.path[0], nome), "w") as f:
            for item in lista:
                f.write(' '.join(item))
                f.write('\n')
            print("file saved")
if opcao == '1':
    if s == 's':
        print("Choose file name")
        nome = input()
        with open(os.path.join(sys.path[0], nome), "w") as f:
            for item in lista:
                texto = str(item).replace('(', '').replace(')', '').replace(',', '').replace("'",'')
                f.write(texto + '\n')
            print("file saved")





#pontos = lista
#X = abscissa
#Y = ordenada



#plt.axis([0, 100, 0, 100])
#plt.scatter(X, Y, c="blue")
#plt.show()