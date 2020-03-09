function [pts,fid,w]=ler

h=figure;axis([0 100 0 100]);axis square;

hold on;
X = [];
Y = [];
button = 10;
while(~isempty(button))
    [x,y,button]=ginput(1);
    scatter(x,y,'k',"filled");
    X = [X; x];
    Y = [Y; y];
endwhile

pts = [X Y];

endfunction