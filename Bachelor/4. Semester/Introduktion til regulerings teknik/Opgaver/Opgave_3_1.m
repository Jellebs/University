sampleTime = 1000; 
s = tf('s');
Gs = 500 * ( ((s + 8 ) * (s + 10) * (s + 15))  / ((s) * (s + 38) * ( s^2 + 2*s +25)))

t = linspace(-50, 50, 200);
ut = zeros(size(t)); 
ut(t>= 0) = 25;
%%r = 37*ramp()
subplot(2, 1, 1);
plot(t, ut);
lsim(Gs, ut, t)

%%plot(Gs)
