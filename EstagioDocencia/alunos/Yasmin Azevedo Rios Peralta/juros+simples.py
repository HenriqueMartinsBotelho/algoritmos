valor = float(input("digite o capital:\n"))

taxa = float(input("valor da taxa de juros mensal (em %): \n"))/100

mes = int(input("meses rodando: \n"))

juros = valor*taxa*mes

print"\nO juros final para uma taxa de ", taxa*100, "% ao mes por ", mes, " meses para um capital de entrada de ", valor, " reais, seria igual a: ", juros


print"\nO valor final a ser pago(capital + juros) seria de", juros+valor

