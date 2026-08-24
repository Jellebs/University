function y=filterdf2t(b,a,x,v)
% Implementation of Direct Form II structure (Transposed)
%  with arbitrary initial conditions
% [y] = filterdf2t(b,a,x,v)

N=length(a)-1; M=length(b)-1; K=max(N,M); 
L=length(x); y=zeros(L,1);

if nargin < 4, v=zeros(K,1); end
if N>M, b=[b' zeros(1,N-M)]'; else
a=[a' zeros(1,M-N)]'; end

for n=1:L
  y(n)=v(1)+b(1)*x(n);
  for k=1:K-1
    v(k)=v(k+1)-a(k+1)*y(n)+b(k+1)*x(n);
  end
  v(K)=b(K+1)*x(n)-a(K+1)*y(n);
end