clear all; 
s = tf('s')
Gp = 100/((s+1)*(s+100)*(s+36))
bode(Gp); grid on



%% Oensker
% K0 = 40dB 
% Gamma_M = 60° findes som phasen ved wc - (-180) 
omega_C = 30 % rad/s


%% Lead soerger for phaseloeft (Hurtigere stigtider / Mindre oversving) 
phaseloeft = deg2rad(24); 
alpha = (1 - sin(phaseloeft))/(1 + sin(phaseloeft)) % Størrelsen af phaseloeftet
T = 1/(omega_C * sqrt(alpha))
K_C = sqrt(alpha)
GLead = (1/alpha) * ((s + 1/T) / (s + 1/(alpha*T)))


%% Lag soerger for forstaerkning (Mindre stationaer fejl) 

% gain -> db = 20log_10(K)
beta = 40 - 28 % Hoejeste uden lag er 28db, 40 oensket. => 12db
beta = beta/20
beta = 10^(beta) % K = 3.98 


% For at nulpunktet ikke pavirker systemet, saa sættes den noget mindre
% end knaekfrekvensen. Professoren sagde fingreregel 10-20 x mindre, men i
% videoen jeg saa paa det, fik jeg at vide, at tommelfingerreglen var 50
% gange mindre. 
% Jeg foelger eksemplet dog 

faktor = 10
T = 1 / (omega_C) * faktor % = 0.33
GLag = (s + 1/T)/(s + 1/(beta*T))

% Proportional gain 
Kp = 10^(63.5/20)

sys = GLag*GLead*Kp*Gp
feedback(sys, 1)
step(sys)
bode(sys); grid on 
% K0 > 40db √
% GammaM < 60db % 
% Wc ≠ 30 rad/s % 


