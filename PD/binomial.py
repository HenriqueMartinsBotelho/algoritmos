def binomial(n,k):
    c = [[0 for x in range(100)] for y in range(100)]
    K = k + 1
    N = n + 1
    for i in range(K):
        c[0][i] = 0
    for i in range(N):
        c[i][0] = 1
    for i in range(1,N):
        for j in range(K):
            c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c[i][j]

print(binomial(1,1)) # 1
print(binomial(9,3)) #84
print(binomial(10,3)) #120
print(binomial(10,4)) #240