#!/usr/env/bin python

print("Áreas de Retângulo, Triângulo, Trapézio e Círculo")

number1 = float(input("Digite a base (maior): "))
number2 = float(input("Digite a altura: "))
number3 = float(input("Digite a base (menor): "))
number4 = float(input("Digite o raio: "))

ret = number1 * number2
tri = ret/2
tra = tri + number3 * number2 / 2
cir = 3.1416 * number4 * number4

print("Áreas: " + str(round(ret, 2)) + ", " +  str(round(tri, 2)) + ", " + str(round(tra, 2)) + ", " +  str(round(cir, 2)))
