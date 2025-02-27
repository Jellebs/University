%DFT
%HKa april 2023

clear; close all;

for N=2:4
N=2^N;

W=fft(eye(N))

x=[0, 1, 2, 3]'
x(N)=0;

X=W*x

stem(abs(X))
pause(2);
end