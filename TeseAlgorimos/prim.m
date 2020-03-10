%   Este algoritmo calcula a árvore de Prim, usando como função de peso 
%   a função do artigo: An interactive programme for weighted Steiner trees
%   O algoritmo retorna o conjunto de vértices, os índices dos vértices escolhidos e a lista 
%   de adjacências.
%   A função de custo se encontra no arquivo "custo.m" 0.5*(w1 + w2)*dist 

function [V, indices, adj, costPrim, E] = prim()

[V, fid, w] = sread;

% Algoritmo de Prim implementado conforme pseudocódigo da dissetação 

X = [1];
Y = (2:length(V)); 
E = [];
indices = [];
costPrim = 0;

while (length(X) < length(V))
  menor = inf;
  e = [];
  eidx = [];
  for i = 1:length(X)
    for j = 1:length(Y)
      cost = custo(V(X(i)),w(X(i)),V(Y(j)),w(Y(j))); %Função de custo
      costPrim = costPrim + cost; #Calcula o custo total da árvore
      if (cost < menor)
        menor = cost;
        e = [V(X(i)); V(Y(j))];
	    eidx = [X(i) Y(j)];
      endif
     endfor
  endfor
  X = [X eidx(2)];
  Y = Y(Y~= eidx(2));
  E = [E e]; % Contém as arestas da árvore de Prim 
  % plot(e);
  % pause (5);
  indices = [indices; eidx];
endwhile
plot(E,'b');

### ---- ####


### Cria a lista de adjacencias ###
adj{length(indices)+1} = [];
for(i=1:length(indices))
	u = indices(i,1); 
	v = indices(i,2);
	adj{u} = [adj{u} v];
	adj{v} = [adj{v} u];
endfor
### --- ###


### Remove Cortes na árvore (implementando)

%for (i = 1:length(E))
%    E
%endfor


###




endfunction
