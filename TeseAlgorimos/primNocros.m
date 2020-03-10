function [V, indices, adj, costPrim] = primNocros()

pkg load geometry

[V, fid, w] = sread;

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
      cost = custo(V(X(i)),w(X(i)),V(Y(j)),w(Y(j)));
      costPrim = costPrim + cost; 
      if (cost < menor)
        menor = cost;
        e = [V(X(i)); V(Y(j))];
	      eidx = [X(i) Y(j)];
      endif
     endfor
  endfor
  X = [X eidx(2)];
  Y = Y(Y~= eidx(2));
  E = [E e];
  #plot(e);
  #pause (5);
  indices = [indices; eidx];
endwhile
plot(E,'b');

%%% ---- %%%


%%% Cria a lista de adjacencias %%%
adj{length(indices)+1} = [];
for(i=1:length(indices))
	u = indices(i,1); 
	v = indices(i,2);
	adj{u} = [adj{u} v];
	adj{v} = [adj{v} u];
endfor
%%% --- %%%


%% Remove Cruzamentos %%
for (i = 1: length(E))
disp('hello')
  for(j = 2: length(E))
    p1 = E(1,i)
    p2 = E(2,i)
    plot([p1,p2],'r')
    pause(1)
    p3 = E(1,j)
    p4 = E(2,j)
    plot([p3,p4], 'o')
    teste = intersectEdges([real(p1),imag(p1), real(p2), imag(p2)], [real(p3),imag(p3), real(p4), imag(p4)])
    #teste = nocros(p1,p2,p3,p4)
    #if (teste == 10)
    #  disp("remover cruzamentos")
    #  plot([p1,p2], 'r')
    #endif
  endfor
endfor
%% --- %%

endfunction
