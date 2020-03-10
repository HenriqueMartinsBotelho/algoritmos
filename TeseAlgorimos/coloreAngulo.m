function coloreAngulo(p1, escolhido1, escolhido2, CosA)

    ce = norm([real(escolhido1 - p1), imag(escolhido1 - p1)]);
    be = norm([real(escolhido2 - p1), imag(escolhido2 - p1)]);
    ae = sqrt(be^2 + ce^2 - 2*CosA*be*ce);
    if (ce^2>=ae^2+be^2+ae*be)|(be^2>=ae^2+ce^2+ae*ce)
        if (ce > be)
            plot([p1 escolhido1],'r');
            plot([p1 escolhido2],'m');
        else
            plot([p1 escolhido1],'m');
            plot([p1 escolhido2],'r');
        endif
    endif

endfunction
