def tbloco(lista):
    tamanhoBloco = 1
    ok = False
    if lista[0] > 0:
        for i in range(1, len(lista)):
            if lista[i] > 0:
                tamanhoBloco += 1
            else:
                return tamanhoBloco
    else:
        for i in range(1, len(lista)):
            if lista[i] < 0:
                tamanhoBloco += 1
            else:
                return tamanhoBloco


    return tamanhoBloco
    #return ok



# para cada bloco se todos os elementos tem o mesmo sinal retorne true e false caso contrario

def alternate(lista):
    tamanhoBloco = tbloco(lista)
    t = tamanhoBloco
    x = 1
    ok = False
    if l1[0] > 0:
        for i in range(t*x, t + x*t):
            if x % 2 == 0:
                if l1[i] > 0:
                    ok = True
                else:
                    return False
            else:
                if l1[i] < 0:
                    ok = True
                else:
                    return False                    
        x += 1
    else:
        for i in range(t*x, t + x*t):
            if x % 2 == 0:
                if l1[i] < 0:
                    ok = True
                else:
                    return False
            else:
                if l1[i] > 0:
                    ok = True
                else:
                    return False
        x += 1
    
    
    return ok


l1 = [1,2,3,3-8,-8,-8,1,1,5] 
print(alternate(l1)) ## esperado false


#print(tbloco([1,2,3,-8,-8,-8,1,1,5]))
#print(tbloco([-1,-2,3,4,-1,-2,5,6]))
#print(tbloco([1,2,3,4,5]))
