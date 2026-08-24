%% --------- Variabler til legobilen ---------

% I opgaver har jeg lavet mange af mine beregninger: 

% State space repræsentation ( Ureguleret ) 
alpha = 1; 
k2 = 1; 
K0 =1.2;

A = [0 1; 0 -alpha];
B = [0;1];
C = [k2 0];
D = [0];
K = [2482 17];
Acl = A - (B*K);
K0 = 2482
Bcl = K0*B

