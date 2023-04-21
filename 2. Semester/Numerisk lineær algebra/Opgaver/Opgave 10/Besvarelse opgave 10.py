import numpy as np
from Formelsamling.Numerisk_Lineær_Algebra import *

# Opgave 10.2. Hvilken af de følgende funktioner L: V -> W er lineær? 
# a. L: R^2 -> R^3, L(x, y) = (2x, 3y, x-y). 

# x: R^1 
# y: R^1 
# L(x, y): R^3 
# L(x, y): [ ix
#            jy 
#            kz ]

# L((x,y)) = Ax

A = np.array([[2,  0],
              [0,  3],
              [1, -1]], dtype = float)

x = [1, 1]
# Ax = b 
L = A @ x  # [2, 3, 0]






# Opgave 10.5: Gram Schmidt eksperiment, nu med householder matricen. 

s = 1e-8
a = np.array([[1.0, 1.0, 1.0], 
              [  s, 0.0, 0.0], 
              [0.0,   s, 0.0], 
              [0.0, 0.0,   s]])

# Testen går ud på, at vi ser langt q @ r er fra a, og om q.T @ q = identitetsmatricen

def lavForsøg(q, r, a = False): 
    if type(a) == bool: 
        print(q.T @ q) # Hvor tæt er matricen på en identitets matrice? 
        return 
    print(a - q @ r) # Hvor tæt er matricen på en 0 matrice? 
    return 
    
print("""
------------------------------------------- Klassisk Gram Schmidt -------------------------------------------
""")
q, r = gramSchmidt(forbedretGramSchmidt=False, a=a)
lavForsøg(q, r, a)
lavForsøg(q, r)

print("""
------------------------------------------ Forbedret Gram Schmidt -------------------------------------------
""")
q, r = gramSchmidt(forbedretGramSchmidt=True, a= a)
lavForsøg(q, r, a)
lavForsøg(q, r)

print("""
-------------------------------------------- Householder matrice --------------------------------------------
""")

q, r = householder_qr(a)
lavForsøg(q, r, a)
lavForsøg(q, r)

# House holder qr værdidekomponeringen viser de bedste resultater 


