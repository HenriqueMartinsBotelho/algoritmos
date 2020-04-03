capital = float(input("valor do capital: \n"))

taxa = float(input("valor da taxa de juros mensal(em %): \n"))/100

tempo = int(input("duracao em meses: \n"))

montante = capital*(1+taxa)**tempo

print"o valor do montante sera de %.2f" %montante

#o %.2f % vai limitar a quantidade de casas decimais



