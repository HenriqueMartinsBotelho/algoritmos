def numero_par(x):
  if x%2==0:
    return True
  else:
    return False

# Inserir no () os numeros a serem testados

print(numero_par(23))
print(numero_par(100))

#Como otimizar o comando acima? Excluindo o else, nesse caso, se ele ficar na msm altura do if, traz a msm solução

def numero_par(x):
  if x%2==0:
    return True
  return False
# Inserir no () os numeros a serem testados
print(numero_par(23))
print(numero_par(100))
print(numero_par(123))


#Como otimizar (mais ainda) o comando acima? Excluindo if, nesse caso, ele compara e traz o mesmo resultado

def numero_par(x):
  return x%2==0
    
# Inserir no () os numeros a serem testados
print(numero_par(23))
print(numero_par(100))
print(numero_par(123)) 