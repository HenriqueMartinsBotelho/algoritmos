function logic=nocross(p,H,K,ed)

logic=0;

v1=p(K)-p(H);             % v1=p(end)-p(end-1);
v0=p(ed(1:end-1,1))-p(H); % v0=p(1:end-3)-p(end-1);
v2=p(ed(1:end-1,2))-p(H); % v2=p(2:end-2)-p(end-1);
at1=imag(v1*conj(v0)).*imag(v1*conj(v2))>=0;

for k=1:length(v0)
 ncl(k)=abs(det([real(v0(k)) imag(v0(k));real(v1) imag(v1)]))+...
        abs(det([real(v2(k)) imag(v2(k));real(v1) imag(v1)]));
end;
fnd=find(ncl==0);

for k=1:length(fnd)
 if real((v0(fnd(k))-v1)*conj(v2(fnd(k))-v1))>=0 at1(fnd(k))=1;end; 
end;

v1=p(ed(1:end-1,2))-p(ed(1:end-1,1)); %v1=p(2:end-2)-p(1:end-3);
v0=p(H)-p(ed(1:end-1,1));             %v0=p(end-1)-p(1:end-3);
v2=p(K)-p(ed(1:end-1,1));             %v2=p(end)-p(1:end-3);
at2=imag(v1.*conj(v0)).*imag(v1.*conj(v2))>=0;
at=at1|at2;

if prod(double(at)) logic=1;end;

