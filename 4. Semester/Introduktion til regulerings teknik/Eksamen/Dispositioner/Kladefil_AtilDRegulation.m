K = 2; 
% 
% clear all
% s = tf('s');
% 
% G = 300/((s+2)*(s+7)*(s+20));
% Kp = 8.9125; 
% Glead = (1.767*s+10)/(s+17.67);
% Glag = (s+0.5)/s;
% Gc = Glag*Kp*Glead;
% margin(Gc*G)
% 
% Gcl = feedback(G*Gc, 1);
% % step(Gcl);
% 
% wc= 10; 
% Ts=2*pi/(15*wc); 
% Gsh = exp(-s*Ts/2)
% 
% bode(Gc*G);
% hold on 
% margin(Gsh*Gc*G);
% hold off 
% 
% % step(Gsh); Duer ikke
% [num, den]= pade(Ts/2, 3); % Pade approksimation
% Gsh = tf(num, den);
% Gcl_sh = feedback(Gsh*Gc*G, 1)
% step(Gcl, 'b'); 
% hold on
% step(Gcl_sh, 'g');
% hold off




%% Opgave 1 & 2
% Design Analog regulator 
clear all 
s = tf('s'); 
G = 300/((s+2)*(s+5)*(s+20));
%margin(G);


% Krav: 
%   Mindst 60° phase margin ( OS% ~10) 
%   Krydsfrekvens på 8rad/s
%   Type 1

% Tilstand: 
%   Phase margin på 109
%   Krydsfrekvens på 1.94 rad/s 

reg = Regulatorer;
reg.wc_oensket = 8; 
Kp1 = proportional(reg, 16);

Glead = lead(reg, 45, 9);
Glag = lag(reg, 30);

% Opgave 2 - Digitaliser
Gdig = sampleAndHold(reg, 20, 3) % Sampling frekvens 20x wc










%% Billinear transformation 
clear all; 
s = tf('s')
z = tf('z')

Gs = 5*(s+4)/s;
Ts = 1;
% Bilinear transformation 

%          //                  \       \     /      1     \
%         ||   2        z - 1   |       |   |  ----------  |
% Gz = 5 *||  ---- *   -------  |  + 4  | * |   / z - 1 \  |
%         ||   Ts       z + 1   |       |   |  | ------- | |
%          \\                  /       /     \  \ z + 1 / /

% Gz  = (15z + 5)/(z - 1) 
% Gz  = (15 + 5*z^-1)/(1 - z^-1) 

% Men kan også findes ved 
Gz1 = c2d(Gs, Ts, 'tustin')

% Herfra kan man finde differensligningen: 
% 
% Y(z)*(1-z^-1) = (15 + 5z^-1)X(z) 
% Y_k - Y_k-1 = 15X_k + 5X_k-1

Gc = (s + 10)/(s + 30); 
Gz_hundredeMilli = c2d(Gc, 0.1, 'tustin')
Gz_tiMilli = c2d(Gc, 0.01, 'tustin')



