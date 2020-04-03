t = input("Texto: ")
p = input("Padrão: ")
count = 0
for i in range(len(t)):
    if t[i : i + len(p)] == p:
        count += 1
print(count)
