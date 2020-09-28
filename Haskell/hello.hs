area_retangulo x y = x * y
area_circulo r = pi * r * r
soma x y = x + y

hipotenusa x y = sqrt(soma (x*x) (y*y))

d_AB x1 y1 x2 y2 | x1 == x2 = abs(y2-y1)
                 | y1 == y2 = abs(x2-x1)
                 | otherwise = sqrt((x2-x1)^2 + (y2-y1)^2)

-- retorna quantos dos valores forenecidos sao iguais
quantosIguais a b c | a == b && b == c = 3
                    | a == b = 2
                    | a == c = 2
                    | otherwise = 0

-- Ex 3 recebe x e retorna x^2
potencia_2 x = x*x

-- Ex 4 usar a funcao do ex 3 para construir potencia_4
potencia_4 x = potencia_2 x * potencia_2 x

-- soma de 1 + 2 + 3 + .... + n
somaNaturais 1 = 1
somaNaturais n = somaNaturais(n-1) + n

-- fatorial
fatorial 0 = 1
fatorial n = fatorial(n-1) * n

--fibonacci

fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2) 

-- funcao ou lógico
ou :: Bool-> Bool -> Bool
ou False False = False
ou _ _ = True





