def sub_lists(list1): 
    sublist = [[]] 
    for i in range(len(list1) + 1): 
        for j in range(i + 1, len(list1) + 1): 
            sub = list1[i:j] 
            sublist.append(sub)             
    return sublist 


def ispar(v):
    soma = 0
    for i in v:
        soma += i
    if soma % 2 == 0:
        return len(v)
    else:
        return -1 

def verifica(a):
    for i in a:
        b = ispar(i)
        if b > -1:
            print(b)
            for j in i:
                print(j, end=" ")
            break 
    print(-1)

t = int(input())
elements = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sub_lists(a)
    for i in a:
        b = ispar(i)
        if b > -1:
            print(b)
            for j in i:
                print(j, end=" ")
            break 
    print(-1)
    



