import math

# Retorna o quadrado da distância (pois não é bom trabalhar com raiz quadrada)
def dist2(X,Y):
    x = (Y[0] - X[0])
    y = (Y[1] - X[1])    
    dist2 = x**2 + y**2
    return dist2

def modulo(X):
    modulo = math.sqrt(X[0]**2 + X[1]**2)
    return modulo

def fourPointsRetangle(A,B,C,D):
    ehParalelogramo = False
    A_C = (C[0] - A[0], C[1] - A[1])
    B_D = (D[0] - B[0], D[1] - B[1])
    if modulo(A_C) == modulo(B_D):
        ehParalelogramo == True
    else:
        return 0
    
    ehRetangulo = False
    AC = dist2(A,C)
    AD = dist2(A,D)
    DC = dist2(D,C)
    if AC == (AD + DC):
        ehRetangulo = True    
    
    if ehRetangulo == True:
        area = AD*DC
        return area
    else:
        return 0

'''
p1 = [1,2]
p2 = [2,3]
p3 = [4,5]
p4 = [5,6]
'''
'''
teste = fourPointsRetangle(p1,p2,p3,p4)
print(teste)

t1 = [0,-3]
t2 = [-4,0]
t3 = [2,8]
t4 = [6,5]

teste2 = fourPointsRetangle(t1,t2,t3,t4)
print(teste2)

'''
'''
points = [p1,p2,p3,p4]
for i1 in range(len(points)):
    for i2 in range(len(points)-1):
        for i3 in range(len(points)-2):
            for i4 in range(len(points)-3):
                fourPointsRetangle(points[i1],points[i2],points[i3],points[i4]) 
'''

t1 = [0,-3]
t2 = [-4,0]
t3 = [2,8]
t4 = [6,5]

areas = []
points = [t1,t2,t3,t4]

for i1 in range(len(points)):
    for i2 in range(len(points)-1):
        for i3 in range(len(points)-2):
            for i4 in range(len(points)-3):
                x = fourPointsRetangle(points[i1],points[i2],points[i3],points[i4])
                areas.append(x) 


y = min(filter(None, areas))
print(y)

'''for elem in areas:
    print(elem)
    if elem == 0:
        areas.remove(elem)
y = min(areas)
print(y)'''