w = logspace(-1, 3, 1000)
alpha = (-1/sqrt(2) + 1j/2);
z = exp(j*w); 
H = 1 + alpha * z.^-1;
gaindB = 20*log10(abs(H));
phase = rad2deg(angle(H))
figure(1); plot(w, gaindB, 'm'); hold on
figure(2); plot(w, phase); hold off