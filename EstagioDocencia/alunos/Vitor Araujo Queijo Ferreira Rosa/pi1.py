import math


def raiz(x,y,z):
	return math.sqrt(y + math.sqrt(x + math.sqrt(z)))

def distance_btw_pi(number):
	distance = abs(math.pi - number)
	if distance < 0.1:
		return (True,distance)
	else:
		return (False,distance)
def pi2():
	return math.sqrt(math.sqrt(3**4+(19**2/78-56)))

def pi1():
	lista_primos = [2,3,5,7,11]
	for k in range(10):
		if k%2==0:
			for i in lista_primos:
				for j in lista_primos:
					checker = distance_btw_pi(raiz(k,i,j))
					if checker[0]:
						print("x=" + str(k) 
							+ " y="+ str(i) 
							+ " z="+ str(j))
						print(raiz(k,i,j))
						print("distance=", checker)
def fibonacci(i: int) -> int:
	r_5 = math.sqrt(5)
	construtor_pos = pow(((1 + r_5)/2), i)
	construtor_neg = pow(((1 - r_5)/2), i)
	return math.floor((construtor_pos - construtor_neg)/r_5)

def golden_ratio(i: int) -> float:
	if i > 1:
		return fibonacci(i)/fibonacci(i-1)
	
print(pi1())
print(pi2())
print(distance_btw_pi(pi2()))
print(100*'*')
print("Fibonacci for 20")
for i in range(20):
	print(fibonacci(i))
	print("Golden Ratio: ", golden_ratio(i))

def somaQ(n):
    soma = 0
    for i in range(1, n+1):
        soma = soma + i*((-1)**(i+1))
    return soma

print(somaQ(22))
