import math
'''
def math.factorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n-1) 
'''
def f(n,p):
    r = math.factorial(n)//(math.factorial(n-p)*math.factorial(p)) + 1
    return r

def g(n):
    soma = 0
    p = 0
    while(p <= n):
        soma += f(n,p)
        p += 1
    return soma

n = int(input())

for i in range(n+1):
    print(g(i))
