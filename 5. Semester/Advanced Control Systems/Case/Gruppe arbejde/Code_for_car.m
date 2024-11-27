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
K = place(A, B, P)

%Vi prøver så nu at optimerer pol-placeringen ved brug af LQR:
vinkel_rad = 50/3;
vinkelhastighed_step = (1/7.8125)*70;
%Man tager den ønskede afstand (50cm) og deler den med hjulets radius (3cm) for at få rad/s
%

Q = [1/((vinkel_rad)^2) 0 ; 0 1/(vinkelhastighed_step^2)];
R = 1/70^2;
K = lqr(A, B, Q, R)
Gcl = ss(A-B*K, B, C, D)

K0 = 1/dcgain(Gcl)
Gcl = ss(A-B*K, B*K0, C, D)


%Vi printer lige en step respons, og det ser fint ud
figure(1)
G = tf(Gcl);
step(G, 30)


%Herpå introduceres L, først ses det om vi kan bruge den
O_M = [C ; C*A];
rank(O_M) %Den er 2, så okay


%Vi finder L ud fra dobbelte poler
L = place(A', C', [-10 -5])'
%Tjekker om de er rigtige
figure(2)
hold on
pzmap(Gcl, 'r')
pzmap(zpk([], eig(A-L*C), 1), 'm')
hold off


%Tilføjer Ki, polen her sættes når den svageste pol eller langt væk
Ai = [A zeros(2,1) ; -C 0];
Bi = [B ; 0];
Ci = [C 0];
Ki = place(Ai, Bi, [-10 P]) %Vi har sat den langt væk 
%Teknisk set er den bare samme sted som den svageste observator pol

Kp = Ki(1:2);
Ke = -Ki(end);


%Sidst sættes back calculator anti windup
Ti = 1/8;

