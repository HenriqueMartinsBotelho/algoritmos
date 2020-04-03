t = input("Texto ")
p = input("String ")
q = input("Input ")
s = input("Sem super posição digite 0. Com superposição digite um número diferente de 0 ")

if s == 0:
    t = t.replace(p,q)
else:
    t_len = len(t)
    for i in range(1000):
        t_len = len(t)
        testando = t[i : i + len(p)]
        if testando == p:
            final = t[i-1 + len(p) + 1:]
            if i == 0:
                primeira = ""
            else:
                primeira = t[0: i]
            t = primeira + q + final    
print(t)
