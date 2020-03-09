main =
    print (fst (1,"oi")) >> -- Imprime o primeiro elemento
    print (snd (1,"oi")) -- Imprime o segund elementos

-- Soma e subtrai dois números
soma_e_sub :: (Int, Int) -> (Int, Int)
soma_e_sub (a,b) = (a + b, a - b)

-- Criação de Tipos

type Peso = Float -- novo tipo chamado Peso 
type Idade = Int
type Pessoa = (String, Idade, Peso, String)

f_francy, f_marcos :: Pessoa
f_francy = ("Francyelle", 20, 75.3, "Basquete")
f_marcos = ("Marcos", 22, 80.1, "Computação")