def f(n,p):
    r = 1
    for i in range(1,p):
        r = (n + 1 - i)/i * r
        print(r)
    return r

r = int(f(10,4))

print(r)