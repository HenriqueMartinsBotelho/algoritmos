def f(n,p):
    r = 1
    b = 1
    for i in range(1,p):
        r = (n + 1 - i) * r
        b = b * i
    r = r/b
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
