import matplotlib.pyplot as plt
import numpy as np
from Formelsamling.Numerisk_Lineær_Algebra import * 

A = np.array([
    [4.,  1.,  2., 1.],
    [1.,  5., -1., 2.],
    [2., -1., -3., 1.],
    [1.,  2.,  1., 1.]])

print(A.T == A)

q, r = householder_qr(A)

a1 = r @ q
print(a1)

print(np.all(a1.T == a1))

print(a1.T - a1)

q1, r1 = householder_qr(a1) 
a2 = r1 @ q1
print(a2)

b = np.copy(A)
for i in range(10): 
    q, r = householder_qr(b)
    b = r @ q 
print(b)

b = np.copy(A)
for i in range(50):  # Udvidet metode af potensmetode, konvergerer mod alle egenværdier.
    q, r = householder_qr(b)
    b = r @ q 
print(b) # Grænser op mod egenværdier for diagonalen. 

lambda_værdier = np.diag(b)
print(lambda_værdier)
print(np.linalg.eig(b)[0])
print(np.allclose(np.linalg.eig(b)[0], lambda_værdier)) # == tæt på sand

rng = np.random.default_rng()
q, r = householder_qr(rng.random((A.shape[0], 3)))
w = q
print(w) 
print(w.T @ w) # Ortonormal

for i in range(10): 
    v = A @ w 
    q, r = householder_qr(v)
    w = q

print(w)

# Rayleigh kvotienter 
lambdaer = np.diag(w.T @ (A @ w))
print(lambdaer)

print(A @ w - w * lambdaer) # Egenvektorer? 


A = np.array([
    [3, 0], 
    [0, 2]])
w = np.eye(A.shape[0])

for i in range(10): 
    v = A @ w
    q, r = householder_qr(v)
    w = q
print(w)

# QR på tridiagonalform 

def heat_map(a): 
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    r = np.max(np.abs(a))
    im = ax.matshow(a, cmap = 'seismic', clim=(-r, r))
    fig.colorbar(im)

n = 200
d = rng.standard_normal(n) 
u = rng.standard_normal(n-1)
t = np.diag(d) + np.diag(u, 1) + np.diag(u, -1) # Tridiagonal matrix

heat_map(t)

q, r  = householder_qr(t) 
heat_map(q)
heat_map(r)
# Begge er øvretriagonale 

t1 = r @ q
heat_map(t1) # Triangulær matrix tilbage
print(np.diag(t1, -2))
print(np.diag(t1, 2))
# Begge er nuller under eller tæt på machine epsilon. 


