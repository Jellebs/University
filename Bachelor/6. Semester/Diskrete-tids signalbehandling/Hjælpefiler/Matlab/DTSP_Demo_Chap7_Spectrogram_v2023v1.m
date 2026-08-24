%Spectrogram
%Hka 2023

clear, close all;

% % %Generate sum of 2 sinoids.
% N = 2048;
% n = 0:N-1;
% w0 = 2*pi/5;
% x = sin(w0*n)+10*sin(2*w0*n);
% 
% figure(1)
% spectrogram(x,'yaxis')


%Generate a quadratic chirp, x, sampled at 1 kHz for 2 seconds. 
%The frequency of the chirp is 100 Hz initially and crosses 200 Hz at t = 1 s.
t = 0:0.001:2;
x1 = chirp(t,100,1,200,'quadratic');

figure(2)
spectrogram(x1,128,120,128,1e3)


