#!/usr/env/bin python

## Júros Simples ##

c = float(input("Digite o Capital: "))
i = float(input("Digite a Taxa: "))
n = float(input("Digite a quantidade de Períodos: "))

m = c * i * n

print("O Montante final é:", str(round(m, 2)) + ".")
