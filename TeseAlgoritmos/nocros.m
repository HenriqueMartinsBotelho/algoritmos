function valor=nocros(p0,p1,p2,p3)

valor = 0;

s1_x = real(p1) - real(p0);
s1_y = imag(p1) - imag(p0);
s2_x = real(p3) - real(p2);
s2_y = imag(p3) - imag(p2);

    
s = (-s1_y * (real(p0) - real(p2)) + s1_x * (imag(p0) - imag(p2))) / (-s2_x * s1_y + s1_x * s2_y);
t = (-s2_x * (imag(p0) - imag(p2)) - s2_y * (real(p0) - real(p2))) / (-s2_x * s1_y + s1_x * s2_y);

if (s >= 0 && s <= 1 && t >= 0 && t <= 1)
        valor = 1;
endif







%d1 = (p1 - p3) * (p4 - p3) 
%d2 = (p2 - p3) * (p4 - p3)
%d3 = (p3 - p1) * (p2 - p1)
%d4 = (p4 - p1) * (p2 - p1)


%if (((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) && ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0)))
%    valor = 1
%endif

%valor

endfunction