function swrite(pts,w)

% swrite Stores the terminal points and their weights in a text-file.
%    swrite is the last subprogram called before we finish running the 
%    main program "stree". The user is prompted to choose between saving 
%    or not the input data into a text-file. 
%    
%    No subprogram invoked.

disp('Save points in file? Yes=1, No=0');

ok=0;
while ~ok
 chc=input(' ');
 if chc==1
  L=length(pts);
  lis=[real(pts), imag(pts), w(1:L)'];%'
  disp('Please give file name');
  fnm=input(' ','s');
  if isempty(fnm) fnm='trash';end;
  fnm=strcat(fnm,'.txt');
  save(fnm,'lis','-ascii');
  ok=1;
  clear lis;
 elseif isempty(chc)|(chc~=0)
  disp('Please answer 1, 0 or interrupt with Ctrl-C.');
 else ok=1; 
 end;
end;
