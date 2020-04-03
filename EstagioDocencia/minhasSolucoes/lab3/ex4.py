def collatz(n):
    if n == 1: return 0
    i = 0
    while n != 1:
        if n % 2 == 0:
            i += 1
            n = n / 2
        else:
            n = 3*n + 1
            i += 1
    return i

n = int(input("Digite o número: "))
print(collatz(n))







### TESTES #### (usando a sequência https://oeis.org/A006577)
vetor = []
for j in range(1, 18):
    v = collatz(j)
    vetor.append(v)
seq = [0, 1, 7, 2, 5, 8, 16, 3, 19, 6, 14, 9, 9, 17, 17, 4, 12]
assert vetor == seq, "Aqui"