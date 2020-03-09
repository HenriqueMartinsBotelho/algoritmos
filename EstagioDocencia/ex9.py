def f(seq, x):
    for i in range(len(seq)):
        for j in range(len(seq)):
            soma = seq[i] + seq[j]
            if soma == x:
                return [i,j]
    return [len(seq),len(seq)]


seq = list(map(int, input("Digite uma sequência de números naturais: ").split()))
x = int(input("Digite o valor de x: "))
s = f(seq, x)
print(s)


### Testes ####
def test_f():
    assert f([10,21,32,40], 53) == [1,2], "Errado"

test_f() 
