inicial_n = int(input())
dias_d = int(input())
fixa_x = int(input())

def dobrarDdias(dias_d):
    return inicial_n*(2**(dias_d))

def darQuantiaFixa(x):
    return inicial_n + (dias_d) * x


a = dobrarDdias(dias_d)
b = darQuantiaFixa(fixa_x)

if a > b:
    print(1)
if a < b:
    print(2)
if a == b:
    print(3)

