function [dist] = cost (a,b)
  dist =  sqrt((real(a) - real(b))**2 + (imag(a) - imag(b))**2);
endfunction
