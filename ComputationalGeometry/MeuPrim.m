# Retorna uma árvore de Prim e a matriz de adjacência
function [A] = MeuPrim()
    
[V, fid, w] = sread;
v = V(1); 
X = v; 
Y =  V(2:end);
A = [];
indices = []; 
menor = 100000;

while (length(X) ~= length(V))
  menor = 100000;
  for i = 1:length(Y)
    for j = 1:length(X)
      if (cost(X(j),Y(i)) < menor)
        menor = cost(X(j),Y(i));
        x = X(j);
        y = Y(i);
        e = [x y];
        posicoes = [i, j]; 
      endif
     endfor
  endfor
  X = [X y];
  Y = Y(Y~= y);
  A = [A; e]; 
  indices = [indices; posicoes]; #Criando um vetor com os posicoes para facilar na criação da lista de adjacência
endwhile

### Cria a lista de adjacencias ###
adj = {};
adj{length(indices)+1} = [];
for(i=1:length(indices))
	u = indices(i,1); 
	v = indices(i,2);
	adj{u} = [adj{u} v];
	adj{v} = [adj{v} u];
endfor
### --- ###

adj

#Plota os pontos
for i = 1: length(A)
  plot(A(i,:),'b')
endfor

endfunction
