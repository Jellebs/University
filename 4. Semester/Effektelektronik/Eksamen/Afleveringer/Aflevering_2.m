
solution1 = task1() % i1 & i2
[assumption2, solution2] = task2() % V1 & V2 
task3()






function x = task1()
    V1 = 32;
    V2 = 20; 
    R1 = 2; 
    R2 = 4;
    R3 = 8; 
    % MaskeA = 32 + i1 * R1 + (i1 - i2)* R3; % = 0
    %        = i1(R1 + R3) + i2(-R3) = -32
    % MaskeB = (i2 - i1) * R3 + i2 * R2 - 20; % = 0 
    %        = i1*(-R3) + i2(R2 + R3) = 20
    Masker = [R1 + R3, -R3     ; 
              -R3    ,  R2 + R3]; 
    b = [V1; -V2]; 
    
    % Ax = b, A^-1b = x
    % x = linsolve(Masker, b)
    x = inv(Masker) * b; % i1 = 4, i2 = 1 
end
function [assumption, x] = task2()
    ZR = 10; 
    ZC = -5j; 
    ZL = 10j;
    % Matrix of 1/Impendance * V = I 
    % Assuming V1 > V2
    Impedance1 = [1/(ZR + ZC),     1/(-ZC); 
                 1/(ZC     ), 1/(ZL - ZC)] % => Negativ reel part but positive imaginary part. ground < nodevoltages. 
    % Assuming V2 > V1
    Impedance2 = [1/(ZR - ZC),     1/(ZC); 
                 1/(-ZC     ), 1/(ZL + ZC)] % => Pure negativ meaning ground > nodevoltages.
   
    phaseCurrent = -90;
    current = [-2 * exp(1j*phaseCurrent * pi/180); -1.5]  % Phase = 0 => I = I_amplitude 
    assumption = "V1 > V2"
    x = inv(Impedance1) * current
end 
function task3() 
    R = 1000; 
    C = 1e-6;
    s = linspace(0, 001, 100)
    % s = 0: 0.0001: 0.01;
    Vin = 10; 
    Vc = Vin * 1/(1 + R*C.*s); % This usually works in python. It should just make a new array with same size with this formular for every s
    % This is easier in python, i will plot it there. 

 

end 

