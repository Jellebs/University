classdef Noter 
    %% --------- Noter ---------
        % Funktioner at kalde
        % Teori funktioner
        % Praksis funktioner

    %% Funktioner at kalde
    properties
         

    end 
    methods 

        %% Teori 
        % State Space
        function beskrivelse = teori_ssKontinuert(obj)
            nl = newline
            beskrivelse = "Analog state space, hvor representationen foelger" + nl + ...
                "x' = Ax + Bu,  y = Cx + Du";
        end 
        function beskrivelse = teori_ssDiskrete(obj)
            nl = newline
            beskrivelse = "Den diskrete teori bygger videre paa den kontinuerte:" + nl + ...
                            "Nu er Ts en fakter." + nl + ...
                            "Matlabs c2d bruges til nemt at finde ss for diskrete systemer. 'zoh' metoden bruges til at diskretisere en process. " + nl + ...
                            "Herefter ændres A & B i systemet, og vi kalder dem nu Phi & Gamma" + nl + ...
                            "Foer blev systemet set som en differentialligning, nu ses systemet som en naeste sequense ligning." + nl + ...
                            "Gd = c2d(G, Ts, 'zoh'" + nl + ...
                            "ps -> pz: z = e^(Ts*ps)" + nl + ...
                            "x(k + 1) = Phi*x(k) + Gamma*u" + nl + ...
                            "K_d = place(Phi, Gamma, pz)" + nl + ...
                            "N er dog mere besværlig en gain i kontinuert tid. Se eks 8.73 i bogen.";
        end 
        function beskrivelse = teori_ssObserver(obj)
            nl = newline;
            beskrivelse = "Grundet at vi med observer observere outputtet, og har et parallelt system, som vi antager er ens som processen" + nl + ...
                "saa kigger vi anderledes paa tilstandene. Jeg har ikke selv bevist det, men vi transponere vores statespace matricer. " + nl + ...
                "som chatten saa fint siger: " + nl + ...
                "In control theory, there's a concept called duality," + nl + ...
                "where observer design can be thought of as analogous to the state feedback design but with the roles of A, B and C transposed" + nl + ...
                "L = place(A', B', p)'";
        end 
        function beskrivelse = teori_ssKontinuertIntegrator(obj)
            nl = newline;
            beskrivelse = "Vi oensker at loese for K reguleringen og gain faktoren Ke" + nl + ...
                "For integrator delen, er det bare opsaetningen af nye matricer der er anderledes" + nl + ... 
                "Ai = [A zeros(n,1); -C 0]; " + nl +...
                "Bi = [B; 0]" + nl + ...
                "Ci = [C 0]" + nl + ... 
                "Og så noget med D som jeg ikke kan huske. D = 0 for ingen feedforward." + nl + ...
                "Saa eig(Ai -BiK) til at vaere oenskede poler. ";
        end 
        function beskrivelse = teori_ssDiskreteIntegrator(obj)
            nl = newline;
            beskrivelse = "Meget lig den kontinuerte version, men med nogle aendringer i opstillingen af matricerne." + nl + ...
                "Maeske fordi integration i diskrete tid ikke er 1/z men 1/(z+1) -\_(^.^)_/-" + nl + ...
                "Phii = [Phi zeros(n, 1); -H 1]; " + nl + ...
                "Gammai = [Gamma; 0];" + nl + ...
                "Hi = [H 0]" + nl + ...
                "Plus en Ji del, hvis feedforward eksistere." + nl + ...
                "Loes for eig(Phii - GammaK) = polerD";
        end 
       

        %% Praksis
        % Digital state space representation c -> d -> regulering
        function [Phi, Gamma, H, J, N, Nbar] = praksis_ssDigitalt_PhiMinusGammaK_regulering(obj, A, B, C, D, Ts, poler)
            G = ss(A, B, C, D); % Analog state space  
            Gd = c2d(G, Ts, "zoh"); % Diskrete state space - Z over hold metoden 
            [Phi, Gamma, H, J] = ssdata(Gd); 
            poler = [0.8+0.5j 0.8-0.5j 1]; 
            z = exp(Ts*poler) 
            
            N = place(Phi, Gamma, z) % (A -BK) kontinuert, nu (Phi - Gamma*N) 
            
            % Gain 
            XX =[Phi-eye(length(Phi(:, 1))) Gamma;
                 H                              0]^-1 * [zeros(3, 1); 1]; 
            Nx = XX(1:3, 1); 
            Nu = XX(end, 1); 
            Nbar = Nu+N*Nx; % Gain værdi. 
        end 
    end 
end 
 














