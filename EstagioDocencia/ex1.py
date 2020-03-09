import math

n = int(input("Criancas "))
m = int(input("Doces "))

def f(n,m):
    return math.factorial(n)/(math.factorial(m)*math.factorial(n-m))

print(f(n,m))










