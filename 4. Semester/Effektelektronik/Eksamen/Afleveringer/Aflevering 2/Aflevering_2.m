% solution1 = task1() % i1 & i2
% [assumption2, solution2] = task2() % V1 & V2 
% task3()
task4()






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
    
    R1 = 1e3;
    C1 = 1e-6;
    tau = R1*C1; % 1ms
    t = 0: tau/10 : 5*tau; % 0 -> 5x time constant 
    Vin = 10; 
    % I solved vct by doing KVL and then solving for the nonhomogenous
    % differential equation: vc' +1/RC * vc = 10V/RC 
    % vcp = 10V for t -> ∞, as the voltage above it will be equal to the
    % voltage across the resistor = 10V = Vin. 
    % vc(0) = 0

    % vcc = vc' +vc/RC = 0 => 10 * exp(-t/RC)  
    
    % With basic configurations
    vct1 = signal(R1, C1);
    % With slightly changed configurations
    R2 = R1 - 100; R3 = R1 + 100; C2 = C1 - 1e-7; C3 = C1 + 1e-6
    vct2 = signal(R2, C2); % tau = 0,81ms 
    vct3 = signal(R3, C3); % tau = 2,2ms 
    
    plot(t, vct1, t, vct2, t, vct3); 
    legend({"R1 = "+R1 + ", " + "C1 = " + C1, "R2 = "+R2 + ", " + "C2 = " + C2, "R3 = "+R3 + ", " + "C3 = " + C3}, 'location', 'southwest')
    
    function signal = signal(R, C)
        signal = Vin - Vin * exp(-t/(R*C))
    end    
end 
function task4() 
    f = 50;
    t = 0: 0.0004 : 0.020; % Arbitrary time interval 0ms -> 5ms by 0.1ms
    % using KVL i derive the differential equation: 
    % LC *v_c'' + CR * v_c' + v_c = v_g 
    % Deriving the complementary solution to be: 
    % v_CC = c1e^(-1127t) +c2e^(-8873t) 
    % And finding v_CP 
    % LC *B'' + CR * B' + B = V_g
    % B = v_g
    % V_CP = v_g
    
    % v_c = v_CC +V_CP = c1e^(-1127t) +c2e^(-8873t) + v_g
    
    % Using v_c = 0 to find the first constant c1
    %c1 = -v_g + c2
    
    % Using current through capacitor to derive the second constant 
    % I_C = C*dv_c/dt
    
    % For type(v_g) = DC = 10V
    % I find that c2 = 1/2v_g
    % and c1 = -1/2v_g
    % Finding the solutions to be
    % v_c = v_CC + V_CP = -1/2 * v_g * e^(-1127t) +1/2 * v_g * e^(-8873t) + v_g
    vgDC = 10;
    vcDC = -vgDC/2 * exp(-1127*t) + vgDC/2 * exp(-8873*t) + vgDC ;

    
    % Solving for A_c the constants get more complicated: 
    % Using the current through the capacitor equation to solve for c2 again.
    % I find that
     
    omega = 2*pi * f;
    vgAC = 10*sin(omega*t);
    c1 = -vgAC/2 + 500*pi/1127 * cos(100*pi*t).*exp(1127*t);
    c2 = vgAC/2 + 500*pi/1127 * cos(100*pi*t).*exp(1127*t)
    vcAC = c1.*exp(-1127*t) + c2.*exp(-8873*t) + vgAC; 
    plot(t, vcDC); % It doesn't plot the vc to DC, but looking at the values as t -> 20ms it goes towards 10V which was suspected.
    plot(t, vcAC); 
    % Looking at two outputs i see some strange behaviour at t = 0. I
    % choose to ignore this. 
    



    % Trying to find the resonance frequency
    % I know that the fundamental frequency is the lowest resonance
    % frequency, so every n*f0 should give a resonance frequency. 
    
    % The most simplified vcAC i could simplify is: 
    % vcAC = sin⁡(100πt)*(10 - 5e^(-1127t) + 5e^(-8873t)) + cos⁡(100πt) · ((500π )/1127+(500π )/1127 e^(-7746t))
    % Where the fundamental frequency for both signals is 1/(2pi/100pi)
    % which comes to the same frequency as we started with.
    % f0 = 50Hz
    
    % This indicates, that the AC signal currently runs on the resonance
    % frequency.
    % Somethings wrong
    

end 