%% Problem 1
A = [12, 17, 3, 4]; 

B = [5, 8, 3; 
     1, 2, 3; 
     2, 4, 6]; 
C = [22, 17, 4];

x1 = A(2); %% = 17 
x2 = B(:, 3); 
x3 = B(3, :); 
x4 = [A(1:3); 
      B(1:3, :)];

%% Problem 2
E = [3, 2; 2, 1];

%% Problem 3
A_2 = [ 1, 2, 3; 
        2, 2, 2; 
       -1, 2, 1];
B_2 = [1, 0, 0; 
       1, 1, 0; 
       1, 1, 1];
C_2 = [1, 1; 
       2, 1; 
       1, 2]; 
eq1 = A_2 + B_2; 
eq2 = A_2*B_2; 
% eq3 = A_2 + C_2; --  Error, Addition of different shape matrice
eq4 = B_2 * A_2;
eq5 = B_2 - A_2; 
eq6 = A_2 * C_2; 
% eq7 = C_2 - B_2; --  Error, Addition of different shape matrice
% eq8 = C_2 * A_2; --  Error, Matrix multiplication of different shape matrice
% eq9 = A/B;       --  Error, Something to do about division, that is not commonly used with matrices. 
eq10 = inv(A_2); 
% eq11 = inv(C_2); --  Error, Matrix not invertibel. 
% eq12 = A_2.B_2;  --  Error, Vector multiplication with matrices = Invalid operation
eq13 = A_2.^B_2;    

% b. What's the difference between A*B and A.B
% the first is Matrix multiplication the second is vector multiplication. 

%% Problem 4
% Define a complex number z = 3 + 4i 
z = 3 + 4i; 
z_real = real(z); 
z_imag = imag(z);
z_mag = abs(z); 
z_angle = angle(z); %% Might be in radian

%% Problem 5
I = eye(3); 
eq14 = sqrt(31);
r = randi(10, 10, 1); %% randi(max, n, min) 
zeroMat = zeros(4, 4)
eq15 = exp(A_2); 
diaMat = diag([1, 3, 6, 8, 9]); 
nonZero = find(B_2); %% Index numbers, counting down rows then coloumns.
A_sum = sum(A); 

%% Problem 6
% min sin(x) + 0,5x**2.   1/2 * x**2 -> 0, the largest value must be found
% around 0. 

x = linspace(-2, 2, 50); 
f = sin(x) + 0.5 * (x.^2); 
f_min = min(f); % - 0.3994
c_area = pi*((2*(10^-2))^2); %% Area of circle = 1.3e-3 m^-4
% Find the roots of the square function 
f_roots = roots([1, -3, 2]); % x = 2, 1 















