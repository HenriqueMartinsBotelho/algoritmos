clc
clear
close all

# Passo 1 colorir o ponto mais a esquerda e o mais a direita

[pts] = ler;
pts = sortrows(pts); #ordena os pts segundo a coluna dos x

X = pts(:,1);
Y = pts(:,2);


scatter(X(1),Y(1),'b','filled') #Colore o ponto mais a esquerda
scatter(X(end),Y(end),'r','filled') #Colore o ponto mais a direita
plot( [X(1),X(end)],[Y(1),Y(end)]) #traça linha entre eles


# Passo 2 o ponto P mais distante da reta r = P1 + t*v 

P1 = [X(1), Y(1)]
v = [X(end) - X(1), Y(end) - Y(1)]

P = [4,5]
PP1 = [X(1) - P(1), Y(1) - P(2)]
distPr = sqrt(modulo(PP1)^2 * modulo(v)^2 - dot(PP1, v)^2)/modulo(v)

#lis=[real(pts), imag(pts)];%'
#save('teste.txt','lis','-ascii');

#if fid==-1 
#    swrite(pts,w)
#endif