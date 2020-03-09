v = [5,4,3,2,1]


for i in range(1,len(v)):
    x = v[i]
    j = i - 1
    while(j >= 0 and x < v[j]):
        v[j + 1] = v[j]
        j = j - 1
    v[j + 1] = x

print(v)