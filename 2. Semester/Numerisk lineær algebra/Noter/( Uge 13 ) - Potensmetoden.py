import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt 
import Formelsamling.Numerisk_Lineær_Algebra as formel 

rng = np.random.default_rng()

a = rng.normal(0, 5,(5, 5))
a += a.T # Gør a symmetrisk

print(a)
print(np.allclose(a, a.T))

def potens_skridt(a, w): 
    v = a @ w
    return v / np.linalg.norm(v)

w = rng.normal(0, 5,(5, 1))
w /= np.linalg.norm(w)

v = potens_skridt(a, w)
print(v)
v = potens_skridt(a, w)
print(v)

for i in range(20): 
    v = potens_skridt(a, w)

print(v)
v = w
vs = np.empty((5, 20))
for i in range(20): 
    v = potens_skridt(a, v)
    vs[:, [i]] = v

print(vs[0, :])
j = range(20)
fig, ax = plt.subplots()
ax.plot(j, np.abs(vs[0, j]), "-o")

fig, ax = plt.subplots()
for i in range(5): 
    ax.plot(j, np.abs(vs[i, j]), "-o")


lambda_out = np.empty(20)
v = w

for k in range(20): 
    lambda_out[k], v = formel.potens_skridt(a, v)

print(lambda_out)

fig, ax = plt.subplots() 
ax.plot(lambda_out, "-o")


# Page rank 

m = np.array([
    [   0, 1./4,  0, 1./2,    0, 1./6], 
    [1./3,    0,  0,    0, 1./2, 1./6], 
    [   0, 1./4,  0,    0,    0, 1./6], 
    [1./3,    0,  0,    0, 1./2, 1./6], 
    [1./3, 1./4,  0, 1./2,    0, 1./6], 
    [   0, 1./4, 1.,    0,    0, 1./6]])

p = 0.85 # Sandsynlighed
n, _ = m.shape
a = p*m + (1-p)/n * np.ones_like(m) # mij + (1-p)
print(np.array_str(a, precision=2))
v = rng.random((n, 1))
v /= np.linalg.norm(v)
nøjagtighed = 1e-9

while True: 
    v_ny = a @ v
    v_ny /= np.linalg.norm(v_ny)
    if np.vdot(v_ny, v) > 1.0 - nøjagtighed: 
        rang_v = v_ny
        break
    else: 
        v = v_ny
    
print(rang_v)
