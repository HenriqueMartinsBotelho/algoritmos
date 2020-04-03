#Nome do segundo exemplo
print("Exemplo com areas de retangulo, triangulo, trapezio e circulo")

numero1=input("\nDigite a base(maior):")
numero2=input("Digite a altura:")
numero3=input("Digite a base(menor):")
numero4=input("Digite o raio:")

ret=float(numero1)*float(numero2)
tri=ret/2
tra=tri+float(numero3)*float(numero2)/2
cir=3.1416*float(numero4)*float(numero4)

print("\nAreas: {0}, {1}, {2} e {3}".format(ret,tri,tra,cir))