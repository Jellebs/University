









function Uge12()
    
    
    
    function opgave7_1()
        % Ud fra en transferfunction Gp(s) find propertionalregulator
        % værdien så at lukketsløjfesystemet højst har et overshoot på 20%
        % og ellers har en lav rise tid
    
        % Jeg starter simulink
        s = tf('s')
        Gp = 1/(s*(s + 50)*(s + 120)
        % (s^2 + 50s)*(s + 120) = s^3 + 120s^2 + 50s^2 + 6000s = s^3 + 170s^2 + 6000s 
    end 
end 