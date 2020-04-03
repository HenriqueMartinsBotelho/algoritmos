print("Juros simples e composto")

C = input("Digite o capital: ")
I = input("Digite a taxa de juros: ")
t = input("Digite o Tempo: ")


ResS=float(C)*(1+float(I)*float(t))
ResC=float(C)*(1+float(I))**float(t)

print("Valores Finais, Simples e Composto: {0} e {1}".format(ResS,ResC))