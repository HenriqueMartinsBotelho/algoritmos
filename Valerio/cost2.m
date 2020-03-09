function [peso] = cost (a,w1,b,w2)
  dist =  sqrt((real(a) - real(b))**2 + (imag(a) - imag(b))**2);
  peso = (w1 + w2)*dist;
endfunction
