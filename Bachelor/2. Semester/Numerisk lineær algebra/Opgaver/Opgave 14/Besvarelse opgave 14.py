import numpy as np 
import sympy as sp
from Formelsamling.Numerisk_Lineær_Algebra import * 
np.set_printoptions(precision=2)

# Opgave 14.2
A = np.array([
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], 
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 1], 
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1], 
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1], 
    [0, 0, 0, 0, 1, 1, 0, 0, 1, 0]])
rng = np.random.default_rng()
m, _ = A.shape 
w = rng.standard_normal((m, 1))
n = 20
lambda_out = np.zeros(n)

for k in range(n): 
    lambda_out[k], w = potens_skridt(A, w)

lambda0 = lambda_out[-1]
print(lambda0)

v0 = w

svar = f"Den største egenværdi af A fundet vha. potensmetoden. \nLambda0 = {lambda0}, \nEgenvektoren = \n{v0} "

opgaveBesvarelse("Opgave 14.2.a", svar)

# b. Indgangene i v målre hvor meget påvirkning den tilsvarene computer har i netværket. 
#    Brug v til at bestemme hvilke computer er vigtigst i dette netværk

svar = f"Der ses i vektoren at c5 har den største indflydelse med: \nc5 = {v0[5][0]}"
opgaveBesvarelse("Opgave 14.2.b", svar)


egenVærdier, egenVektorer = np.linalg.eig(A)

sp.pprint(egenVærdier)
sp.pprint(egenVektorer)



print(np.finfo(float).eps)


# Opgave 14.3. For en kvadratisk n x n matrix A defineres e^A til at være
#   e^A = I_n + A + 1/2 A^2 +1/3!A^3 + 1/4!A^4 + ... 

# a. For 

A = np.array([
    [1, 0, -1,  0], 
    [0, 1,  0, -1], 
    [1, 0,  1, -2], 
    [0, 1,  2, -3]])

# tjek at A^4 = 0 og beregn e^A
# print(A @ A @ A @ A) # === 0

