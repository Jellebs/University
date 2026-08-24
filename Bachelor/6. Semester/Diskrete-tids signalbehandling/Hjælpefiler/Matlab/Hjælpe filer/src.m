function y=src(x,D)
% Sampling rate compressor by a factor D

y=x(1:D:length(x));