#!/usr/env/bin python

## Júros Compostos ##

c = float(input("Digite o Capital: "))
i = float(input("Digite a Taxa: "))
n = float(input("Digite a Quantidade de Períodos: "))

m = c * ( ( 1 + i ) ** n )

print("O Montante final é:", str(round(m, 2)) + ".")
