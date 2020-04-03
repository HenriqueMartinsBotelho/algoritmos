[V,indices, adj, costPrim, E] = prim();

for v = 1:length(adj)
    #E = adj;
    MaxCos = -1/2; 
    escolhido1 = []; escolhido2 = []; indEsc1 = []; indEsc2 = [];
    p1 = V(v);
    for i = 1:length(adj{v})
        p2 = V(adj{v}(i)); 
        for (j = (i + 1): length(adj{v}))
            p3 = V(adj{v}(j));
            CosA = angulo(p1,p2,p3);
            if CosA > MaxCos
                MaxCos = CosA;
                escolhido1 = p2;
                indEsc1 = i;
                escolhido2 = p3;
                indEsc2 = j;
            endif
        endfor
    endfor
    coloreAngulo(p1, escolhido1, escolhido2, MaxCos);

    c = norm([real(escolhido1 - p1), imag(escolhido1 - p1)]);
    b = norm([real(escolhido2 - p1), imag(escolhido2 - p1)]);
    a = sqrt(b^2 + c^2 - 2*CosA*b*c);
    if (c^2>=a^2+b^2+a*b)|(b^2>=a^2+c^2+a*c)
        if (c > b)
            E(indEsc1) = [];
            2#E{v}(indEsc1) = [];
        else
            E(indEsc2) = [];
            3#E{v}(indEsc2) = [];
        endif
    endif
endfor

#preciso transforma a lista de adjacencia E num formato plotavel

plot(E,'g');

disp("Custo da arvore de Prim:")
costPrim
disp("Custo da arvore de Steiner")















#### --- Acha os menores �ngulos e colore eles de vermelhos ###
#for (x = 1:length(adj))
#  menor = 10000
#  ii = -1;
#  jj = 1;
#  for (i = 1:length(adj{x}))
#    for (j = (i + 1): length(adj{x}))
#      V0=V(x);
#      P0 = [real(V0), imag(V0)];
#      V1 = V(adj{x}(i));
#      P1=[real(V1), imag(V1)];
#      V2 = V(adj{x}(j));
#      P2 = [real(V2), imag(V2)];
#      ang = atan2(abs(det([P2-P0;P1-P0])),dot(P2-P0,P1-P0))*180/pi
#      if (ang < menor)
#        menor = ang
#        ii = i;
#        jj = j; 
#      endif
#     endfor
#  endfor
#  if (ii > -1)
#  plot([V(x) V(adj{x}(ii))],'r');
#  plot([V(x) V(adj{x}(jj))],'r');
#  endif
#endfor
### ----- ####











