import sympy as sp 

sp.init_printing(pretty_print=True, precision = 3)

s, C1, C2, rPi, r0, R2, R3, RL, V1, iB = sp.symbols("s C1 C2 rPi r0 R2 R3 RL V1 iB")

C1 = 100e-6
C2 = 100e-6
R2 = 448
R3 = 118900
RL = 100
rPi = 1040

# sp.pprint(sp.N(sp.Inverse(A) @ b, 1)) # Pretty print med hvert værdi med 1 decimal efter kommaet 


A = sp.Matrix([
    [ rPi,   -rPi,  0,     0], 
    [-rPi, R3+rPi,  0,     0], 
    [   0,      0, r0,    r0], 
    [   0,      0, r0, r0+RL]
    ])
b = sp.Matrix([[V1], 
               [ 0], 
               [ 0],
               [ 0]])


sp.pprint(sp.N(sp.Inverse(A) @  b, 2))

 