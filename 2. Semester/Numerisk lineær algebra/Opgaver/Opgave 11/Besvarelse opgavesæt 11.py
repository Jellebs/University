import numpy as np
from sympy import * 

# Opgave 11.2. Lad P3 være vektorrummet af polynomier af grad højst 3. Bestem koordinatvektorerne af polynomiet p(x) = (x - 1)**3
# mht. basen E: x**3, x**2, x, 1

x = symbols('x')
eq = (x - 1)**3
eq_simplified = expand(eq, power_base=True) # Fra eksponent opløftet til udtryk
# Koordinatvektorerne må da være: 
k = np.array([1, -3, 3, -1])

# Opgave 11.3. Bestem koordinatvektorerne af punktet p = (1, -1, 2, 4) indeholder reel**4
# mht. til hver af følgende baser.
E = np.array([
    
    ])


E = Matrix([
    [1, 1, 1, 1],
    [0, 1, 1, 1], 
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])
x0, x1, x2, x3 = symbols('x0 x1 x2 x3')

koor_eq = x0 * E[:, 0] + x1 * E[:, 1] + x2 * E[:, 2] + x3 * E[:, 3] 

# Lad os løse den med numpy.
E = np.array([
    [1, 1, 1, 1],
    [0, 1, 1, 1], 
    [0, 0, 1, 1],
    [0, 0, 0, 1]
])

b = np.array([1, -1, 2, 4])
x1 = np.linalg.solve(E, b)

# Det samme gøres med anden base 
F = np.array([
    [ 1/2, 1/np.sqrt(2),            0,  1/2], 
    [-1/2, 1/np.sqrt(2),            0, -1/2], 
    [ 1/2,            0, 1/np.sqrt(2), -1/2], 
    [-1/2,            0, 1/np.sqrt(2),  1/2]
    ])
x2 = np.linalg.solve(F, b)
np.set_printoptions(precision=3)
print(f"""
----------------------------------- Resultater af opgave 11.3 -----------------------------------
===============================
b_E = {x1}
b_F = {x2}
===============================
""")
# Opgave 11.4. Lad cols = 5 og lad a være Vandermondematricen for tallene 
# -1.0, 0.1, 0.5, 0.7, 1.0
# Afgør i python om søjlerne af a udgør en basis for R ** 5 eller ej. Gør det samme for den transponerede a.T   

cols = 5 
a = np.vander([-1.0, 0.1, 0.5, 0.7, 1.0], cols)
# Her vides der, at hvis a's determinant er forskellig fra 0, så er det en base. 
print(f"""
----------------------------------- Resultater af opgave 11.4 -----------------------------------
=====================================================================
{np.linalg.det(a)} = En smule anderledes end 0, dermed er dette en base.
{np.linalg.det(a.T)} = En smule anderledes end 0, dermed er dette en base.
=====================================================================
""") 

# Opgave 11.5. Bestem for hver af de følgende lineære transformationer L dens standard matrixrepræsentation (SMR).
# a. Reel**2 -> R**3, L(x, y) = (2x, 3y, x-y). 
    # L([1, 0]) = [2, 0,  1]
    # L([0, 1]) = [0, 3, -1]
A_a = np.array([[2,  0], 
                [0,  3], 
                [1, -1]])

# b. Reel**3 -> R**2, L(x, y, z) = (x + y + z, x - 2y + 3z).
    # L([1, 0, 0]) = [1,  1]
    # L([0, 1, 0]) = [1, -2]
    # L([0, 0, 1]) = [1,  3]
A_b = np.array([[1,  1, 1], 
                [1, -2, 3]])

print(f"""
----------------------------------- Resultater af opgave 11.5 -----------------------------------
# a. Reel**2 -> R**3, L(x, y) = (2x, 3y, x-y). 
    # L([1, 0]) = [2, 0,  1]
    # L([0, 1]) = [0, 3, -1]
===================
{A_a}
===================

# b. Reel**3 -> R**2, L(x, y, z) = (x + y + z, x - 2y + 3z).
    # L([1, 0, 0]) = [1,  1]
    # L([0, 1, 0]) = [1, -2]
    # L([0, 0, 1]) = [1,  3]
===================
{A_b}
===================
""") 





