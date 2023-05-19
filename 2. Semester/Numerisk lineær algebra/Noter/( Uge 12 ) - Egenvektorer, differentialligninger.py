import numpy as np 
import sympy as sp 
from Formelsamling.Numerisk_Lineær_Algebra import * 
import matplotlib.pyplot as plt
# Eksempel fra forelæsning 

A = sp.Matrix([
    [-3, 4, 2], 
    [1, 0, -1], 
    [-6, 6, 5]])

# p(lambda) = det(A - lambda*i_n )
def findLambda(Matrice): # Finder egenværdier fra vektorer
    lambdaA = sp.symbols("Lambda")
    eq = sp.det(A - lambdaA*sp.eye(A.shape[0]))
    sol = sp.solve(eq, lambdaA)  
    return eq, sol

eq, (lambda0, lambda1, lambda2) = findLambda(A)
print(lambda0)

A = np.array([
    [-3, 4, 2], 
    [1, 0, -1], 
    [-6, 6, 5]], dtype= float)

eq1 = A - float(lambda0)*np.eye(A.shape[0])

# Løs med rref 
""" 
A = np.array([[1, 1, -1],
              [0, 1,  0], 
              [0, 0,  0]])
"""
# 1x + 1y + -1z = 0
# 1 y = -1x + 1z
# 1y = 0 
# Løsning y = 0 & x = 1, z = 1
v0 = np.array([1, 0, 1], dtype=float)[:, np.newaxis]



eq2 = A - float(lambda1) * np.eye(A.shape[0])

# Løs med rref 
""" 
A = np.array([[1, -1, -1],
              [0,  0,  0], 
              [0,  0, -1]])
"""
# z = 0, 
# x = y
v1 = np.array([1, 1, 0], dtype= float) [:, np.newaxis]



eq3 = A - float(lambda2) * np.eye(A.shape[0])

# Løs med rref 
""" 
A = np.array([[1,  0,  0],
              [0,  2,  1], 
              [0,  0,  0]])
"""
# x = 0, 
# 2y + 1z = 0 
# z = -2y
# y = 1, z = -2
v2 = np.array([0, 1, -2], dtype= float) [:, np.newaxis]

v = np.hstack([v0, v1, v2])
lambda_mat = np.diag([lambda0, lambda1, lambda2])

# print(v @ lambda_mat @ np.linalg.inv(v)) # = A




# Eksperiment med salt i beholdere 
# To tanke, A & B
# A = 200L vand & 60 g salt
# B = 200L vand

# a, b, c, d er vandrør 
# a = 15L rent vand i minuttet, b = 5L, c = 20L / min, d = 15L / min 
"""
y0 = -20/200y0t + 5/200y1t + 
y1 = + 20/200y0t - (5+15)/200y1t 

y' = Ay
y(0) = 60
"""
A = np.array([
    [-1/10, 1/40], 
    [1/10, -1/10]])

eq, (lambda0, lambda1) = findLambda(A)
print(eq)
print(lambda0)
print(lambda1)
eq0 = A - float(lambda0)*np.eye(A.shape[0])
eq1 = A - float(lambda1)*np.eye(A.shape[0])

# => 
v0 = np.array([-0.5, 1.0]) [:, np.newaxis]
v1 = np.array([0.5, 1.0])[:, np.newaxis]

# Startbetingelser medfører
koeffs = np.hstack([v1, v0])
startværdi = np.array([60, 0])[:, np.newaxis]
koeff_udvidet = np.hstack([koeffs, startværdi])
print(koeff_udvidet)
# rref => 
"""
np.array([[1, 1,   0], 
          [0, 1, -60]])

1x + 1y = 0
y = -x
1y -60z = 0
"""

c0 = 60; c1 = -60.
t = np.linspace(0, 100, 100)
løsning = c0 * v0 * np.exp(float(lambda0)*t) + c1 * v1 * np.exp(float(lambda1)*t ) #SKAL LAVES TIL FLOAT, sympy format problem. # Generelle løsning c*v*e^lambda*t
fig, ax = plt.subplots()
ax.plot(t, løsning[0, :], label = "y0")

ax.plot(*løsning, label = "y0 mod y1", marker='o', markevery=10, markersize=4)

print(løsning)
ax.legend()
