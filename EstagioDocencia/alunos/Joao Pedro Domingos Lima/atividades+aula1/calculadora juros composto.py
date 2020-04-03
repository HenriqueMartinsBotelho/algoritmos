print("Juros simples e composto")

C = input("Digite o Capital:")
I = input("Digite a Taxa de Juros: ")
t = input("Digite o Tempo:")

ResC = float(C)*(1+float(I)**float(t))

print("Total de juros é:",ResC,)