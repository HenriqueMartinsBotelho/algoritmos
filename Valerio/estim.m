function estim(pts,w)

% estim Draws the weighted tree of Prim and computes its total weighted length
%    estim is invoked by stree and performs the sum of all edge lengths 
%    of the tree of Prim, weighted according to the input from "sread". 
%
%    It gives an upper estimate of the weighted length of the sought 
%    after Steiner tree. This one must attain the least weighted length 
%    possible.
%    
%    No subprogram invoked. For more details type "help stree" and 
%    "help sread".

[pts,fid,w]=sread;
k=2;Lprim=0;
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
 plot([pts(H);pts(k)]);
 Lprim=Lprim+abs((w(H)+w(k))*(pts(H)-pts(k)));
 k=k+1; 
end;
disp('The length of a weighted Prim is')
Lprim/2
