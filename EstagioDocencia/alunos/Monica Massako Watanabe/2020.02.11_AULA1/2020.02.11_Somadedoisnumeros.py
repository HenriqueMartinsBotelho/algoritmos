#Como colocar um título
print("Primeira aula")

#Como pedir ao usuário para digitar dois numeros; o \n faz pular uma linha
numero1 = input("\nDigite o primeiro numero: ")
numero2 = input("\nDigite o segundo numero: ")

#Fazer uma operacao, mas antes precisamos converter o input em numero
soma=float(numero1)+float(numero2)

#Para exibir a operação
print("\nA soma dos numeros ",numero1," e ",numero2,"eh ",soma)