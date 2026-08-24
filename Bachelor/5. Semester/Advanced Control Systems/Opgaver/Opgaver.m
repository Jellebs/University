addpath('../Noter/'); 
% data = load('somefile.mat');


%% --------- Opgaver ---------
    % Konstanter og klasser
    % Opgavevisning
    % Lego bilen 
    % Opgaveregning
    % Hjaelpefunktioner



%% Konstanter og klasser
stateSpace = StateSpace()
noter = Noter()


%% Opgavevisning
% Opgave3_1()
[Acl, Bcl, K, Ao, Bo, Co, L, K0] = legoBilen()

% [A, B, C, Ac, Bc, Cc] = Opgave5_6()
% [A, B, C, D, N, Ne, Lds] = Opgave9_1()
% [A, B, C, D, L, K, Ke] = Opgave11_1()



%% Lego bilen
% Find state space af bilen. 
% I word har jeg omskrevet systemet til et system med x og y
% med A, B, C, D som konstanter og U som input. 
function [Acl, Bcl, K, Ao, Bo, Co, L, K0] = legoBilen() % Kompenseret system.
    alpha = 1/1.1; k2 = 1/2; 
    A = [0 1; 0 -alpha];
    B = [0; 1];
    C = [k2 0];
    D = [0];
    aabenLoekkeSystemTjek(StateSpace, A, B, C, D); 

    % Tilbagekobling medfører
    w0 = 50                         % Medføre måske fejl senere hen. Martin sætter frekvenser omkring 10.
    z = 0.184
    P = roots([1 2*z*w0 w0^2])
    K = place(A, B, P)
    Acl = A - (B*K)
    Gcl = ss(Acl, B, C, D); % Dc gain = 0.0004 

    K0 = 1/dcgain(Gcl)
    Bcl = K0*B
    Gcl = ss(Acl, Bcl, C, D); 

    % Observer 
    w0_o = w0*10; 
    z_o = 0.8; 
    P12_o = roots([1 2*z_o*w0_o w0_o^2]);
    P_o = [P12_o];
    L = place(A', C', P_o)';  % A' == A.T 
    Ao = [A - L*C]; 
    Bo = [1 ;0]; 
    Co = [C]; 
    Do = [D]; 
    Go = ss(Ao, Bo, Co, Do); 
    Go_pzmap = zpk([],eig(Ao),1); 
    figure(1)
    hold on
    pzmap(Go_pzmap,'m')
    hold off

    


    


    % step(Gcl) % Tilfredsstillende resultat.
end 

%% Opgaveregning
% Opgave 2.1 
% Givet 4 transfer funktioner, lav et pole zero plot. Step den så og plot
% den. 
function Opgave2_1()
    s = tf('s');
    
    G1 = 1/(s^2 + s + 5);
    G2 = (s + 0.2)/(s^2 + 10*s + 5);
    G3 = 10/(s^2 + 2);
    G4 = 1/(s^3 + 1.1*s^2 + 5.1*s + 0.5);
    transferFunktioner = [G1, G2, G3, G4]; 
    
    % plotListe(@pzmap, transferFunktioner)
    % plotListe(@step, transferFunktioner)
end 

% Opgave 3.1 State space opgave.
function Opgave3_1()
    stateSpace = StateSpace()
    % System 1: 
    A = [0 1; -7 -1];
    B = [0; 1];
    C = [3 2];
    D = [0];
    aabenLoekkeSystemTjek(stateSpace, A, B, C, D); 
    
    % System 2: 
    A = [0 1; 0 -1]; 
    B = [0; 1];
    C = [3 0];
    D = 0;
    aabenLoekkeSystemTjek(stateSpace, A, B, C, D); 
    
    % System 3: 
    A = [0 1; 0 -1];
    B = [0; 1]; 
    C = [3.55 1.1];
    D = [0];
    aabenLoekkeSystemTjek(stateSpace, A, B, C, D); 

    % System 4: 
    A = [0 1 0; 0 0 1; -30 -53 -15]; 
    B = [0; 0; 1]; 
    C = [10 0 0]; 
    D = [0];
    aabenLoekkeSystemTjek(stateSpace, A, B, C, D); 

end 

% Opgave 5.6 Integrator regulator opgave
function [A, B, C, Ac, Bc, Cc] = Opgave5_6()
    A = [-19 -14 -6;
           8   0  0;
           0   4  0] 
    B = [16;
          0; 
          0]
    C = [0 5 7];
    D = [0];
    
    % Løs for observer regulator L. 
    poler = [10 9+4.36j 9-4.36j]; 
    L = place(A, transpose(C), poler)
    
    % Løs for closed loop system
    Ai = [A  zeros(3, 1);
          -C 0]
    Bi = [B;
          0]
    Ci = [C 0]

    poleri = [3.5 + 0.36j;
              3.5 - 0.36j; 
                4 +  0.3j; 
                4 -  0.3j] 
    Ki = place(Ai, Bi, poleri)
    K = Ki(1:3)
    Ke = Ki(end)
    
    %Beskrivelse a closed loop systemet

    Ac = [A-K.*B-C.*L         Ke*B; 
             zeros(1, 3)        0  ];
    
    Bc = [zeros(2, 2);
             1   -1   ]
    Bc = [Bc transpose(L)]
    Cc = [-K Ke]
end 

% Opgave 9.1 Design process G i diskrete domæne.
function [A, B, C, D, N, Ne, Ld] = Opgave9_1()
    % Jeg skal designe både for observer og integral effekt. 
    % OS = 0 & tr_max = 2.5
    s = tf('s'); 
    G = 20*(s + 5)/(s*(s+1)*(s+4)); 
    [A, B, C, D] = ssdata(G); 
    eig(A); % Poler for process,  [0, -1, -4] 
    
    % Jeg sætter polerne til at være 2-10 gange hurtigere end de diskrete
    % poler. Den hurtigste pol er -4
    % Daempningen vil jeg have på 0.8. 
    w0_o = -4*10; 
    zeta = 0.8;
    angle = acos(zeta);
    poler_c = [w0_o*cos(angle)+w0_o*i*sin(angle)
               w0_o*cos(angle)-w0_o*i*sin(angle) 
               w0_o]
    Ts = 0.1 % Sampling tiden er ikke givet, så jeg vælger 0.1 sekunder
    poler_d = exp(Ts*poler_c)
    % Saa skal jeg soerge for at A-CL = egenvaerdierne til mine poler.
    noter = Noter(); teori_ssObserver(noter);
    % Inden, at jeg begynder at bruge systemet mere, saa laver jeg det
    % digitalt. 
    Gd = c2d(G, Ts, 'zoh'); 
    pzmap(Gd)
    [Phi, Gamma, H, J] = ssdata(Gd); 
    Ld = place(Phi', H', poler_d)';
    
    % Så nu har jeg observer aekvivalenten. 
    Ao = [Phi - H*Ld]; 
    K0 = 1;
    Bo = [K0*Gamma];
    Co = [C];
    Do = [D];
   
    n = length(Ao(:, 1));
    % teori_ssDiskreteIntegrator(noter); 
    Phii = [Ao zeros(n, 1); -H 1]; 
    Gammai = [Bo; 0]; 
    Hi = [C 0];
    
    % Saa kan jeg endelig loese for process reguleringens Ki og gain
    % parametren Kei. 
    % 
    % Men hvad skal jeg vaelge som poler? Jeg satte observer polerne ved
    % 10x process polerne. 
    % Jeg saetter dem ved 2 & 4 gange polerne. 
    % Jeg forventer nu en 4 orden, saa jeg skal have 4 poler
    w0i_1 = -4*2; w0i_2 = -4*4;
    poler_c = [w0i_1*cos(angle)+w0i_1*i*sin(angle)
               w0i_1*cos(angle)-w0i_1*i*sin(angle)
               w0i_2*cos(angle)+w0i_2*i*sin(angle)
               w0i_2*cos(angle)-w0i_2*i*sin(angle)];
    poler_d = exp(Ts*poler_c);
    Ki_d = place(Phii, Gammai, poler_d)
    N = Ki_d(1:n);
    Ne = -Ki_d(end)

    A = Phii; 
    B = Gammai; 
    C = Hi; 
    D = [0]
    

    % Lad mig lade som om, at jeg bare kan tage gain paa samme maede som
    % ved kontinuert tid. Det samme har Martin gjort, men jeg tror det er
    % en fejl... Jeg kunne i hvert fald ikke få dimensionerne til at gå op,
    % så det må jeg forsøge en anden gang. 
    % Phii
    % eye(length(Phii(:, 1)))
    % Hi
    % [Phii - eye(length(Phii(:, 1))); Hi]^-1 
    % Saa til fejlen
    % XX =[Phii-eye(length(Phii(:, 1))) Gammai;Hi 0]^-1 * [zeros(4, 1); 1]
    % Nx = XX(1:3, 1)
    % Nu = XX(end, 1); 
    % Nbar = Nu+Ki_d*Nx; % Gain værdi. 
    % teori_ssDiskrete()
end 

function [A, B, C, D, L, K, Ke] = Opgave11_1()
    s = tf("s"); 
    G = 100*(s + 5)/((s + 10)*(s + 1)*(s + 4))
    A = [-15 -6.75 -2.5; 
           8     0   0; 
           0     2   0]; 
    B = [8; 
         0; 
         0]; 
    C = [0 1.5625 3.9063]; 
    D = [0]
    L = [4.88; 
        -3.84; 
         1.28]; 
    K = [-0.9 -0.5813 -0.2031]; 
    Ke = 0.01; 
end 




%% Hjalpefunktioner
function plotListe(plotfunktion, liste)
    for i = 1:length(liste)
        plotfunktion(liste(i)); 
        waitforbuttonpress();
    end 
end 
    
    
