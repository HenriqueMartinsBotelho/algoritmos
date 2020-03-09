function [pts,fid,w]=sread

% sread Reads terminal points graphically or from datafile.
%    sread is invoked by stree and prompts a message for you to either 
%    load an existing datafile or to create one. In this 2nd case you 
%    will mark terminal points with the mouse and the numerical keys 1-9.
%    
%    In either case two graphic windows will open. The 1st one shows a 
%    weighted tree of Prim and the 2nd is for you to draw a Steiner tree
%    aiming at the minimum weight.
%
%    No subprogram invoked. For more details type "help stree".

disp('Please adjust terminal window to show full picture.');
disp('Give a filename to open or press Enter to choose points.');
fnm=input(' ','s');
fid=-1;

%h=figure;set(h,'Position',[600 0 840 800]);axis([0 100 0 100]);axis square;
h=figure;axis([0 100 0 100]);axis square;

hold on;

if ~isempty(fnm) 
 arq=strcat(fnm,'.txt');
 fid=fopen(arq,'rt');
 if fid~=-1 
  lis=textread(strcat(arq));
  fclose(fid);
%  lis=lis(:);
%  pts=lis(1:end/3)+i*lis(end/3+1:2*end/3);
%  w=lis(2*end/3+1:end)';%'
  pts=lis(1:3:end)+i*lis(2:3:end);
  w=lis(3:3:end)';%'
  for k=1:length(lis)/3
   plot(pts(k),'rs');
   if w(k)>1 text(real(pts(k))+1,imag(pts(k))+1,int2str(w(k)));end;
  end;
  clear lis;
 end;
end;

if ~isempty(fnm)&(fid==-1) disp('File not found');end;

if isempty(fnm)|(fid==-1)
 disp('Choose three or more points and press Enter to conclude.'); 
 arq=strcat(fnm,'.txt');
 fid=fopen(arq,'rt');
 if fid==-1
  k=1;prox=3;
  button=10;
  while ~isempty(button)
   [aa,bb,button]=ginput(1);
   if ~isempty(button)
    pts(k)=aa+i*bb;
    plot(aa,bb,'r.',"markersize", 20);
    w(k)=max(button-48,1);
    if k>1 [prox,ii]=min(abs(pts(1:k-1)-pts(k)));end;
    if prox>=3 
     if w(k)>1 obw(k)=text(aa+1,bb+1,int2str(w(k)));
     else obw(k)=text(aa+1,bb+1,' ');
     end;
     k=k+1;
    else 
     if ii<k delete(obw(ii));end;     
     obw(ii)=text(aa+1,bb+1,int2str(w(k)));
     w(ii)=w(k);
     w=w(1:k-1);
     obw=obw(1:k-1);
     plot(aa,bb,'ws');
     plot(pts(ii),'rs');
     pts=pts(1:k-1);
    end;
   end;
  end;
  if length(pts)<3 disp('You chose less than three points!');return;end;   
  pts=pts.';%'
 end;
end;

pts=round(100*pts)/100;
