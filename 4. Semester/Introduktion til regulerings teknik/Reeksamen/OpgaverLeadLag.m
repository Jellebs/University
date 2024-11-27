classdef OpgaverLeadLag
    properties
    end 
    methods 
        function [Gcl, egenskaber] = opgave8_1(obj)
            s = tf('s');
            G_p = 1/(s*(s+50)*(s+120));
            K_p = 177830; 
            omegac = 26;
            beta = 10.12203;
            Glag = (s + omegac/20)/(s + omegac/20 * 1/beta);
            regulatorerOgProcess = K_p * Glag * G_p;
            Gcl = feedback(regulatorerOgProcess, 1);
            egenskaber = dictionary(["Omega_c", "beta"], [omegac, beta]);
        end 
        function [Gcl, egenskaber] = opgave8_2(obj)
            s = tf('s')
            G_p = 1942000/(s*(s + 50)*(s+120)); 
            Kc = 0.12;
            alpha = Kc^2;
            omegac = 105; 
            T = 1/(omegac * Kc);
            Glead = (Kc/alpha) * (s + 1/T)/(s + 1/(alpha*T));
            regulatorerOgProcess = Glead*G_p; 
            Gcl = feedback(Glead*G_p, 1); 
            step(Gcl)
            egenskaber = dictionary(["Kc", "Alpha","omegac", "T"], [Kc, alpha, omegac, T]);
        end 
        function ekstraEkstraOpgave6(obj)
            s = tf('s'); 
            G_p = 3000/((s+5)*(s+10)*(s+50)); 
            omegac = 2.86; 
            
            beta = 100; % Stationær løft på 40dB
            T_lag = 20/omegac;  % 20 gange mindre frekvens end kryds frekvensen.
            G_lag = (s + 1/T_lag)/(s + 1/(beta * T_lag)); 
            
            Kc = 0.85; 
            alpha = sqrt(Kc);
            T_lead = 1/(omegac*Kc); 
            G_lead = (Kc/alpha) * (s + 1/T_lead)/(s + 1/(alpha*T_lead)); 
            
            reguleringOgProcess = G_lead*G_lag*G_p; 
            Gcl = feedback(G_lead*G_lag*G_p, 1); 
            step(Gcl);
            % margin(reguleringOgProcess);
        end 
        function [Gcl, egenskaber] = ekstraOpgave6(obj)
            s = tf('s');
            G_p = 3000/((s + 5)*(s + 10)*(s+50));
            K_p = 10^(18/20); 
            omegac = 19.4;

            alpha = (1 - sind(40))/(1 + sind(40)); 
            Kc = sqrt(alpha);
            T_lead = 1/(omegac*Kc);
            G_lead = (Kc/alpha)*(s + 1/T_lead)/(s + 1/(alpha*T_lead));
            
            beta = 900; % Beregnet ud fra ingen stationær fejl
            T_lag = 20/omegac
            G_lag = (s + 1/T_lag)/(s + 1/(beta*T_lag))

            reguleringOgProcess = G_lag*G_lead*K_p*G_p; 
            Gcl = feedback(reguleringOgProcess, 1);
            % margin(reguleringOgProcess);
            step(Gcl)
            egenskaber = dictionary(["Kp", "Omegac", "Alpha", "Kc"], [K_p, omegac, alpha, Kc])
        end 
        function [G, p] = gaetEnOverfoeringsfunktion(obj);
            clear;
            s = tf('s');
            % rng(0,'twister');
            A = randi(5000); 
            p = [5, 50]% randi([0, 50], 1, 2);
            G = A/((s+p(1))*(s+p(2)))
            margin(G); grid on
        end 
    end
end 
