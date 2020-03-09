function [custo] = cost (a,w1,b,w2)
  dist =  sqrt(a[1] - b[1])**2 + (a[2] - b[2])**2);
  custo = 0.5*(w1 + w2)*dist; 
endfunction