print("Juros simples e composto")

C = input("Digite o Capital em R$: ")
I = input("Digite a Taxa de Juros por Mês: ")
t = input("Digite o Tempo em Meses:")
juros = float(C)*float(I)*float(t)
montante = float(C)+float(juros)
print("\nTotal de juros é R${0}" .format(juros))
print("\nMontante final de R${0}".format(montante))