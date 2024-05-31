from Formelsamling.Numerisk_Lineær_Algebra import * 
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

A = np.array([[3, 1, 1],
              [2, 0, 1], 
              [1, 2, 0]], dtype = float)

b = np.array([1, 1, -1])[:, np.newaxis]

bE = np.linalg.solve(A, b)
print(bE)

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3")

A = sp.Matrix([[1,  1,  0,  2], 
               [1, -1,  2,  0], 
               [0,  1, -1, -1]])
x = sp.Matrix([[x0], 
               [x1], 
               [x2], 
               [x3]])

Ax = A @ x 
sp.pprint(Ax)

u0 = np.array([1, 1,  1, 1])[:, np.newaxis]
u1 = np.array([1, 0,  1, 0])[:, np.newaxis]
u2 = np.array([1, 1, -1, 1])[:, np.newaxis]

def findVinklen(u, v): # Normal er vi ligeglade med vinklen i grader, men snakker om vinklen i cos(vinklen). 
    return np.vdot(u, v)/(np.linalg.norm(u) * np.linalg.norm(v))

vinklen = findVinklen(u0, u2)
print(vinklen)

w0 = u0 
v0 = 1*w0
print(projektionPå(v0, u1))
w1 = u1 - projektionPå(v0, u1)
print(w1)
# For simpelhedens skyld, så sættes skalaren c1 til at være to. 
v1 = 2*w1

# nu gøres det samme for w2, men denne gang skal den næste vektorsprojektion på u også trækkes fra. 
w2 = u2 - projektionPå(v0, u2) - projektionPå(v1, u2)
print(w2)
# Her ser w2 simpelt ud, c2 kan nøjes med at være 1. 
v2 = 1*w2

u = np.hstack([u0, u1, u2])
v = np.hstack([v0, v1, v2])
v_norm = np.linalg.norm(v, axis = 0)
v[:, 0] /= v_norm[0]
v[:, 1] /= v_norm[1]
v[:, 2] /= v_norm[2]

# print(np.linalg.norm(v, axis = 0)) # Hvis ortonormal, skal disse være 0. 




# ------------------------------------ Opgave 6. ------------------------------------ # 

x = np.array([-0.01, 1.04, 1.31, 1.95, 2.58,  3.28,  3.86])
y = np.array([ 0.13, 2.77, 3.12, 2.93, 1.43, -0.01, -1.76])
cols = 3
A = np.vander(x, cols)
u, s, vt = np.linalg.svd(A, full_matrices= False)
sigmaInvers = np.diag(1/s)
kappaA = s[0]/s[-1]

# sigmainvers = np.diag(1/s)
koeffs_w = vt.T @ (sigmaInvers @ (u.T @ y[:, np.newaxis]))
t = np.linspace(-0.1, 4, 100)
rest_w = y[:, np.newaxis] - A @ koeffs_w
laengde_rest_w = np.linalg.norm(rest_w)
# Længden af rest vektoren.
svar = f"""
koeffs_w = {koeffs_w[:, 0]}
||rest_w||_2 = {laengde_rest_w} 
"""
opgaveBesvarelse("Opgave 6.c", svar= svar)

fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.plot(x, np.vander(x, cols) @ koeffs_w)
# fig.savefig("Sommer 2022. Opgave 6: SVD approksimations.pdf")
# plt.show()  


