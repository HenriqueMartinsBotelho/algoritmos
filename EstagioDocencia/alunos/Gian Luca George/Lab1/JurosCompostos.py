x = input("Digite a o valor a ser aplicado: ")
y = input("Digite a taxa de juros (sem o %): ")
t = input("Digite o tempo da aplica��o em meses: ")

j = float(y)/100

f = float(x) * (1 + float(j)) ** float(t)

print("\nO valor final recebido � {0}".format(f))