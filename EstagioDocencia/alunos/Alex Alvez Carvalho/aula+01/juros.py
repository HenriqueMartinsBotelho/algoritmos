print("Juros simples e composto")
c = input("Digite o capital: ")
i = input("Digite a taxa de juros: ")
t = input("Digite o tempo: ")

resS = float(c)*(1+float(i)*float(t))
resC = float(c)*(1+float(i))**float(t)

print("valores finais, simples e composto: {0} e {1}" . format(resS,resC))

