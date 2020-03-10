function [custo] = cost (a,w1,b,w2)
  dist =  sqrt((real(a) - real(b))**2 + (imag(a) - imag(b))**2);
  custo = 0.5*(w1 + w2)*dist; 
endfunction