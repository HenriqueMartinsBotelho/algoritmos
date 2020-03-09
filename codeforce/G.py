def f(x,y,n):
    if n == 1:
        return x
    if n == 2:
        return y
    return f(x,y,n-1) - f(x,y,n-2)

a = [int(x) for x in input().split()]
n = int(input())

r = f(a[0],a[1],n) % 1000000007

print(r)