% Criando a matriz A
A = [ 
        1, 1, 2;
        3, 5, 8;
        13, 21, 34
    ];  

% Deletando uma linha
A(3,:) = []; % Deleta a linha 3

% Deleta a coluna 2
A(:,2) = [];

% Acessando um elemento (i,j)
A(1,2);

% Acessado todos os elementos de uma linha
A(1,:);

% Acessado todos os elementos de uma coluna
A(:,2)


%Como acrescentar linhas ou colunas numa dada Matriz
A = [5 6 7; 5 8 9]; 
B = [A,[15;12]]; % acrescenta a Matriz A, a quarta coluna formada pelos elementos 15 e 12;
C = [B;[16 17 18 19]]; % acrescenta-se a Matriz A, a terceira linha formada pelos elementos 16, 17, 18 e 19.

