import numpy as np
import matplotlib.pyplot as plt
from Formelsamling.Numerisk_Lineær_Algebra import * 


# QR transponering

# For A = QR, vil det lineære ligningssystem være:  
# QRx = b 
# Med Q.TQ= In: 
# InRx = Rx = Q.Tb

# Gram schmidt

A = np.array([[1, 1],
              [1, 2], 
              [0, 1]], dtype= float)
b = np.array([1, 2, 0], dtype= float) [:, np.newaxis]
q,r = gramSchmidt(True, A)
print(f'{q} \n {r}')
print(np.allclose(q@r, A)) # ... == ... 

c = q.T @ b 
c *= np.sqrt(2) 

print(c)

ruc = np.hstack([r,c])

skaler(ruc, 1/np.sqrt(2), 0)
skaler(ruc, 1/np.sqrt(1.5), 1)
lægTil(ruc, 0, -3/2, 1)

print(ruc)

x = np.array([1, 4, 5.2], dtype= float)
y = np.array([3.2, 2.1, 3.5])

fig, ax = plt.subplots()

ax.plot(x, y, 'o')

cols = len(x)

a = np.vander(x, cols)

koeffs = np.linalg.solve(a, y[:, np.newaxis])
print(koeffs)

t = np.linspace(0, 6, 100)

ax.plot(t, np.vander(t, cols) @ koeffs)

x = np.array([-1.0, -0.5, -0.1, 0.2, 0.7, 0.9, 1.1, 1.4, 1.7])
y = np.array([ 4.0, -1.0,  0.2, 0.6, 1.4, 0.3, -2.1, -1.5, 0.1])

cols = len(x)

a = np.vander(x, cols)

koeffs = np.linalg.solve(a, y[:, np.newaxis])
print(koeffs)

t = np.linspace(x.min()-0.1, x.max() + 0.1, 100)

fig, ax = plt.subplots()
ax.plot(x, y, 'o')
ax.plot(t, np.vander(t, cols) @ koeffs)

#----------------------------------- Eksempel på fejl ------------------------------------------# 
# Der er overflow i følgende eksempel. 5 ubekendte, 9 ligninger = overflow. Linalg.solve kan kun løse kvadratiske matricer.
'''
cols = 5
a = np.vander(x, cols)
koeffs = np.linalg.solve(a, y[:, np.newaxis]) # Går galt, for mange ligninger i forhold til variabler.
'''

#--------------------------Eksempel på hvordan man løser alligevel -----------------------------# 

q, r = gramSchmidt(True, a)

q @ r - a 

c = q.T @ y[:, np.newaxis] 

def back_substitution(r, c):  # Virker ikke.
    _, n = r.shape
    x = np.empty((n, 1))
    for i in reversed(range(n)): 
        x[i] = (c[i] - r[[i], i+1:] @ x[i+1:]) / r[i,i]
    return x

#                                    Test af funktionen                                          #

fig, ax = plt.subplots()
ax.plot(x, y, 'o')
koeffs = back_substitution(r, c)
print(f"Koeffs: \n {koeffs} \n")

ax.plot(t, np.vander(t, cols) @ koeffs, label= "Approksimeret funktion")

# Skulle give en approksimation ud fra mindste kvadraters metode.

# SVD metoden 
u, s, vt = np.linalg.svd(a, full_matrices=False)
print(s[-1]) # Er den forskellig fra 0? 
koeffs_svd = vt.T @ (np.diag(1/s) @ (u.T @ y[:, np.newaxis])) # v.t @ y @ c
print(koeffs_svd) 
rest_svd = y[:, np.newaxis] - np.vander(x, cols) @ koeffs_svd
print(rest_svd) # Hvor langt fra punkterne? 

print(np.linalg.norm(rest_svd)) # Hvor god er løsningen? 

ax.legend()