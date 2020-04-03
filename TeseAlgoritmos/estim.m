function estim(pts,w)

%    estim Draws the weighted tree of Prim and computes its total 
%    weighted length. estim is invoked by stree and performs the 
%    sum of all edge lengths of the tree of Prim, weighted according 
%    to the input from "sread". 
%
%    It gives an upper estimate of the weighted length of the sought 
%    after Steiner tree. This one must attain the least weighted length 
%    possible.
%    
%    Invoked subprograms: sread, nocross. For more details type 
%    "help stree" and "help sread".

clc
clear
close all
A = []
[pts,fid,w]=sread;
k=2;Lprim=0;vec=[];
edge=zeros(length(pts)-1,2);
while k<=length(pts)
 rest=pts(k:end);
 for K=1:k-1 
  [prox(K),h(K)]=min(abs((w(k:end)+w(K))'.*(rest-pts(K))));%'
 end;
 [Prox,H]=min(prox);
 temp=pts(h(H)+k-1);
 pts(h(H)+k-1)=pts(k);
 pts(k)=temp;
 temp=w(h(H)+k-1);
 w(h(H)+k-1)=w(k); 
 w(k)=temp;
 if k>3
  if nocross(pts,H,k,edge(1:k-2,:)) disp('ok');
  else disp('blaaa...');			 
  end;
 end;
teste = [pts(H); pts(k)]
A = [A; teste]
plot([pts(H);pts(k)])
edge(k-1,1:2)=[H k];
Lprim=Lprim+abs((w(H)+w(k))*(pts(H)-pts(k)));
k=k+1;
end;
disp('The length of a weighted Prim is')
Lprim/2

if fid==-1 swrite(pts,w);end;

fnm = 'st2.fe';
fid = fopen(fnm,'wt');
fprintf(fid,'%6s\n','STRING');
fprintf(fid,'%17s\n\n','SPACE_DIMENSION 2');
fprintf(fid,'%45s\n\n','quantity len energy method edge_length global');
fprintf(fid,'%8s\n','VERTICES');
for k=1:length(pts)
 fprintf(fid,'%d %3.3f %3.3f %s\n',k,real(pts(k)),imag(pts(k)),'fixed');
end
fprintf(fid,'\n');

fprintf(fid,'%5s\n','EDGES');
for k=1:length(pts)-1
 fprintf(fid,'%d %d %d\n',k,edge(k,1),edge(k,2));
end

fclose(fid);
keyboard
