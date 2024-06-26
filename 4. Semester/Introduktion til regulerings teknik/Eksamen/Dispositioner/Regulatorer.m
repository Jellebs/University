classdef Regulatorer
    properties
        wc_oensket = 0; 
    end 
    methods
        function Kp = proportional(obj, loeftIdB) % Proportionals regulatoren er med til at loefte cutoff frekvensen.
            Kp = 10^(loeftIdB/20);
        end 
        function Glead = lead(obj, faseLoeft, wmax) % Lead regulatoreren er med til at loefte fasen.
            s = tf('s');
            alfa = (1 - sind(faseLoeft))/(1 + sind(faseLoeft));
            T = 1/(wmax * sqrt(alfa));
            Kc = sqrt(alfa);
            Glead = (Kc/alfa) * ((s + 1/T)/(s + 1/(alfa * T)));
        end 
        function Glag = lag(obj, stationaertLoftIdB) % Lag regulatoren er med til at loefte den stationære tilstand.
            s = tf('s');
            beta = 10^(stationaertLoftIdB/20); 
            T = 10/obj.wc_oensket;
            Glag = (s + 1/T) / (s + 1/(beta*T)); 
        end 
        function Gdig = sampleAndHold(obj, nXsamplingfrekvens, padeApproksOrden) % Regulering ved digitalisering. God til fjern styring, men kan koste i fasen med (wc*Ts)/2
            Ts = 1/obj.wc_oensket;
            [num, den] = pade(Ts/(2*nXsamplingfrekvens) , padeApproksOrden);
            Gdig = tf(num, den); 
        end 
    end
end 