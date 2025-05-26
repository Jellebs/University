function X = gafft(x,N,k)
% Goertzel's algorithm
% X = gafft(x,N,k)
% Computes k-th sample of an N-point DFT X[k] of x[n]
% using Goertzel Algorithm
L = length(x); x = [reshape(x,1,L),zeros(1,N-L+1)];
K = length(k); X = zeros(1,K);
for i = 1:K
   v = filter(1,[1,-2*cos(2*pi*k(i)/N),1],x);
   X(i) = v(N+1)-exp(-1j*2*pi*k(i)/N)*v(N);
end