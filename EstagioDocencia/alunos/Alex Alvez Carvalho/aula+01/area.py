print("areas de retangulo, triangulo, trapezio e circulo")

number1 = input("Digite a base(maior): ")
number2 = input("Digite a altura: ")
number3 = input("Digite a base(menor): ")
number4 = input("Digite o raio: ")

ret=float(number1)*float(number2)
tri=ret/2
tra=tri+float(number3)*float(number2)/2
cir=3.1416*float(number4)*float(number4)

print("Áreas: {0}, {1}, {2} e {3}" .format(ret,tri,tra,cir))


