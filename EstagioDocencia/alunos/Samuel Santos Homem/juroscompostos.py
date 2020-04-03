print("Juros simples e composto")

C = input("Digite o Capital: ")
I = input("Digite a Taxa de Juros: ")
t = input("Digite o tempo: ")


resS = float(C)*float(I)*float(t)

resC = float(C)*float(1+float(I))**float(t)



print("Valores Finais, Simples e Composto: {0} e {1}".format(resS,resC))