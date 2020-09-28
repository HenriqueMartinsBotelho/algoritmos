
n = int(input())
A = list(map(int, input().split())) 

i = 0
soma = 0
while i < n:
    soma = soma + A[i]
    i += 1

print(soma)
