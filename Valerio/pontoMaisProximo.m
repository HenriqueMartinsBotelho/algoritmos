[pts,w]=sread;

#oi = pts
#pts = sortrows(pts)

X = real(pts);
Y = imag(pts);

pontos = [X Y] #cria matriz de colunas X e Y
pontos = sortrows(pontos) #ordena os pontos segundo a coluba dos x


X = pontos(:,1)
Y = pontos(:,2)


Xvermelhos = X(1:length(pts)/2);
Yvermelhos = Y(1:length(pts)/2);
Xazuis =  X(length(pts)/2+1:length(pts));
Yazuis =  Y(length(pts)/2+1:length(pts));

scatter(Xvermelhos, Yvermelhos, 'r', 'filled');
scatter(Xazuis, Yazuis, 'b', 'filled');

#scatter(X,Y,'b');





#save pontos.txt pts;
