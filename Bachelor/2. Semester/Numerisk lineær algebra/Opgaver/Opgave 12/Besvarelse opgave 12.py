import numpy as np 
from sympy import * 
from Formelsamling.Numerisk_Lineær_Algebra import *

# Opgave 12.2. Bestem standardmatrixrepræsentationen(SMR) for de følgende lineære afbildninger L. Brug dette til at angive en basis for ker L og en basis for im L 

# a. L(x, y) = (2x, 3y, x-y)
x = np.array([2, 0,  1]) [:, np.newaxis]
y = np.array([0, 3, -1])

A = np.array([
    [2,  0], 
    [0,  3], 
    [1, -1]
    ])

# Reducer til echelonform, så fås pivot søjlerne til 0 & 1, da er 
# im(L) = (2, 0, 1) & (0, 3, -1)
# ker(L), den værdi der skal ganges på begge af disse for at få nulvektoren
# ker(L) 0*(2, 0, 1), 0*(0, 3, -1)
# ker(L) = span(0,0)



# Opgave 12.3. Betragt den lineære afbildning L, hvor p_2 er vektorrummet som består af polynomier af grad højst 2 givet ved
a, b, c, d, e, f, g, h, i, r, s, t = symbols("a b c d e f g h i r s t")
p = Matrix([
    [a, d, g], 
    [b, e, h], 
    [c, f, i]])


F = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
    ])

S = Matrix([
    [1, 0, 0],
    [0, 1, 0], 
    [0, 0, 1]])

"""S * Matrix[[
    [r], 
    [s],
    [t]]]
"""

# Så er S koordinatskiftsmatricen for E fra F 
# S^-1 er da koordinatskiftsmatricen for F fra E.

# Opgave 12.4. Betragt den øvre triangulære matrix 
A = np.array([
    [6, -3,  2],
    [0,  2,  7], 
    [0,  0, -1]])

# Vis at 6, 2, -1 er egenværdier for A og bestem egenvektorer.

# For at dette skal være gældende, så må A - \lambda*eye ikke være invertibel
lambdaA = np.array([6, 2, -1]) [:, np.newaxis]
print(np.linalg.det(A - lambdaA*np.eye(3, 3)) == 0) # True og det er derfor egenværdierne. 

# Egenvektorerne findes da. #bx = c, men c indeholder 0'er så disse behøves ikke i rækkeoperationen.
B = A - np.array(np.eye(3,3)*6)

np.set_printoptions(precision=3)

lægTil(B, 1, -4/3, 0)
lægTil(B, 2, 7/4.333333333333, 1)
print(B)

# v_0 = (2, -3, 0)

B = A - np.array(np.eye(3,3)*2)
lægTil(B, 1, 7/3, 2)
lægTil(B, 2, -1, 2)


# v_1 = (4, -3, 2)

B = A - np.array(np.eye(3,3)*(-1))


# Jeg går videre uden den sidste.

print((A - 6*np.eye(3)) @ ( A - 2*np.eye(3)) @ ( A + 1*np.eye(3)) ) # Skulle give en nulvektor med 3 0'er. 

# Gøre rede at for en generel øvre triangulær matrix er indgangene på diago- nalen netop matricens egenværdier. Er sådan en matrix nødvendigvis diagona- liserbar? Opfylder den en ligning af typen (12.1)?

# Jeg ved ikke helt hvordan det fungerer, men determinanten har da noget med diagonlaen at gøre.
# For at finde egenværdierne finder man så løsningen til det(A - \lambda*in)



# Opgave 12.5. Lad u = (1, 2, 4), v = (-1, 2, 1) og sæt A = u*v.T.
# Bestem en basis for N(A)
u = np.array([1, 2, 4], dtype = float) [:, np.newaxis]
vt = np.array([-1, 2, 1], dtype = float)
A = u*vt
lægTil(A, 1, -2, 0)
lægTil(A, 2, -4, 0)
skaler(A, -1, 0)

NA = np.array([
    [-2, -1], 
    [ 0,  0],
    [ 0,  0]
    ]) # Søjle 1 & 2 er nulrum for den reducerede echelonform matrice. 
