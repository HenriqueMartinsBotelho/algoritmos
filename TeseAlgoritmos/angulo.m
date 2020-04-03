# retorna o cosseno do ângulo p1p2p2

function [CosA] = menorAngulo(p1,p2,p3);
MaxCos = -1/2; 
vec1 = [real(p2-p1), imag(p2-p1)];
vec2 = [real(p3-p1), imag(p3-p1)];
prodEscalar = dot(vec1,vec2);
mod1 = norm(vec1);
mod2 = norm(vec2);
CosA = prodEscalar /(mod1*mod2);

endfunction