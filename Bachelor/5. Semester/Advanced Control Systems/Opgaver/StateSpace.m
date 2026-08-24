classdef StateSpace
    methods 
        function aabenLoekkeSystemTjek(obj, A, B, C, D)
            SSsystem = ss(A, B, C, D);
            overfoerselsFunktion = tf(SSsystem)
            fprintf("\nPasser pengene? Hvis ja, så er polerne her");
            poler = eig(A)
            
        end 
    end 
end 
