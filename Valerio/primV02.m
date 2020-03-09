% Nessa versão do algoritmo é acrescentada a função de custo

[pts, fid, w] = sread; % le os pontos, o id do arquivo e os pesos
menor = inf; % menor = infinito
escolhidos = pts(1); %escolhidos = primeiro ponto
pts(1) = []; %deletar o ponto que foi escolhido
n = 0;
final = length(pts);

while(n < final)
        menor = inf;
        for i = 1:length(pts)
            for j = 1:length(escolhidos)
                if (cost2(pts(i),w(i),escolhidos(j),w(i+1)) < menor)
                    menor = cost2(pts(i),w(i),escolhidos(j),w(i+1));
                    edge = [escolhidos(j),pts(i)];
                    rponto = pts(i);
                endif;
            endfor;
        endfor;
        escolhidos(end+1) = rponto; %adiciona ponto escolhido ao final de escolhidos
        pts(pts==rponto) = []; %remove rponto do array
        plot(edge);
        n = n + 1;
 endwhile;

 
