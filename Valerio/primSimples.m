#Algoritmo de Prim V^3 baseado no pseudocódigo da dissertação

function [A] = prim()
    
[V, fid, w] = sread;
v = V(1); 
X = v; 
Y =  V(2:end);
A = []; 
menor = 100000

while (length(X) ~= length(V))
  menor = 100000
  for i = 1:length(Y)
    for j = 1:length(X)
      if (cost(X(j),Y(i)) < menor)
        menor = cost(X(j),Y(i))
        x = X(j);
        y = Y(i);
        e = [x y]
      endif
     endfor
  endfor
  X = [X y]
  Y = Y(Y~= y)
  A = [A; e]  
endwhile
#plot(A)      
endfunction      

