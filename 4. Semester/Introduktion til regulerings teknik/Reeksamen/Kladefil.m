opg = OpgaverLeadLag()
% [Gcllag, vaerdierlag] = opgave8_1(opg) % Lag reguleret system.
% [Gcllead, vaerdierlead] = opgave8_2(opg) % Lead reguleret system
% [Gcl, vaerdier] = ekstraOpgave6(opg)
% [G, p] = gaetEnOverfoeringsfunktion(opg); 

clear all 
s = tf('s');
G = 300/((s+2)*(s+5)*(s+20));
Gc = (14*s + 44)/(s + 20);

Gcl = feedback(G*Gc, 1); 
figure(1); step(Gcl, 'k');

Ts = 0.04; 
Gc_d = c2d(Gc, Ts, 'tustin'); 
G_d = c2d(G, Ts, 'zoh'); 

Gcl_d = feedback(Gc_d*G_d, 1);
figure(1); hold on 
step(Gcl_d, 'r.');
step(Gcl_d, 'm');
hold on

[NumSH, DenSH] = pade(Ts/2, 3);
Gsh = tf(NumSH, DenSH); 
Gcl_sh = feedback(G*Gc*Gsh, 1);
step(Gcl_sh);
hold off