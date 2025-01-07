%Vores egen kode til bilen

%Systemet er (Output er vinkel i radianer)
A = [0 1 ; 0 -7.8125];
B = [0 ; 1];
C = [1 0];
D = [0];


%Vi tjekker om der er styrbarhed
C_M = [B A*B];
rank(C_M) %Ser fint ud


%Så vil vi sætte vores poler, som er sat ud fra at vi ikke vil have noget
%oversving (dermed kun reelle), og at vi gerne vil have en tidskonstant på
%ca. 2 sekunder. En hurtigere pol kan godt bruges
P = [-1 -1/2];
%K = place(A, B, P)

%Vi prøver så nu at optimerer pol-placeringen ved brug af LQR:
Actuator = 70;
vinkel_rad = 50/3;
vinkelhastighed_step = (1/7.8125)*Actuator;
%Man tager den ønskede afstand (50cm) og deler den med hjulets radius (3cm) for at få rad/s%

Q = [1/((vinkel_rad)^2) 0 ; 0 1/(vinkelhastighed_step^2)];
R = 1/(Actuator^2);
[K, z, p] = lqr(A, B, Q, R)
Gcl = ss(A-B*K, B, C, D)
p = [p(1) p(2)]

K0 = 1/dcgain(Gcl)
Gcl0 = ss(A-B*K, B*K0, C, D)


%Vi printer lige en step respons, og det ser fint ud
figure(1)
G = tf(Gcl);
step(G, 30)


%Herpå introduceres L, først ses det om vi kan bruge den
O_M = [C ; C*A];
rank(O_M) %Den er 2, så okay


%Vi finder L ud fra dobbelte poler
L = place(A', C', P)'
%Tjekker om de er rigtige
figure(2)
hold on
pzmap(Gcl, 'r')
pzmap(zpk([], eig(A-L*C), 1), 'm')
hold off

%Integral controler:
Q = [1/((vinkel_rad)^2 - 270) 0 0; 0 1/(vinkelhastighed_step^2) 0; 0 0 1];
R = 1/(Actuator^2);
Ai = [A zeros(2,1) ; -C 0];
Bi = [B ; 0];
Ci = [C 0];
[K, s, p] = lqr(Ai, Bi, Q, R);
Kp = K(1:2);
Ke = -K(end); 
%Sidst sættes back calculator anti windup
Ti = 1/8;



% %% Martins ord
% % Man må ikke blande pol placering med LQR, entet gør man den ene ellers så
% % gør man den anden. 
% % Hvis vi husker på, så er Ki vores pol placerings metode for integral
% % systemet. 
% 
% % Så 
% 
% % - 
% Ki = place(Ai, Bi, [-10 p]) 
% 
% % + 
% Q = [1/((vinkel_rad)^2) 0 0; 0 1/(vinkelhastighed_step^2) 0; 0 0 1];
% R = 1/(Actuator^2);
% [K, s, p] = lqr(Ai, Bi, Q, R);
% 
% Kp = K(1:2);
% 
% Ke = -K(end); 
% 
% %Sidst sættes back calculator anti windup
% Ti = 1/8;
% 






