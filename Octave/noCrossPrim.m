%[V, fid, w] = open;

[x, y, buttons] = ginput ()
V = [x,y]  

v = V(1,:); % Escolhendo um vértice v qualquer de x
X = [v]
Y = V(  
A = []
costPrim = 0;

while (length(X) < length(V))
    menor = inf;
    for i = 1:length(X)
        for j = 1:length(Y)
            cost = distancePoints(X(i),Y(j))%custo(X(i),w(X(i)),Y(j),w(Y(j))); %Função de custo
            costPrim = costPrim + cost; #Calcula o custo total da árvore
            if (cost < menor)
                menor = cost;
                e = [X(i); Y(j)]
            endif
        endfor
    endfor
    X = [X; e]
    Y = Y(Y~= e)
endwhile