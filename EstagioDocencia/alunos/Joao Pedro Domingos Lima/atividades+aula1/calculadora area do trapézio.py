print("Calculando área do trapézio")
bmaior = input("\nDigite a base maior em cm:")
bmenor = input("Digite a base menor em cm:")
altura = input("Digite a altura em c²:")

btotal = float(bmaior)+float(bmenor)
areacima = float(btotal)*float(altura)
area = float(areacima)/2
print ("A área do trapézio é: {0}cm²" .format (area))