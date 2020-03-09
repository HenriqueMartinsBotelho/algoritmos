def collatz(n):
    i = 0
    while n != 1:
        if n % 2 == 0:
            i += 1
            n = n / 2
        else:
            n = 3*n + 1
            i += 1
    return i

n = int(input("Digite o número"))
print(collatz(n))
