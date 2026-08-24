import numpy as np
import matplotlib.pyplot as plt
# Ortogonale samlinger kan fås ved: 
# u - pr_v0...vk-1 giver en samling af vinkelrette vektorer på alle af vektorerne i v. 

u0 = np.array([1, 1, 0, 0], dtype= float)[:, np.newaxis]
u1 = np.array([2, 1, 1, 1], dtype = float)[:, np.newaxis]
u2 = np.array([-1, 3, 1, -1], dtype = float)[:, np.newaxis]

def projektion(v, u): 
    return np.vdot(v, u) / np.vdot(v, v) * v 

w0 = u0 
v0 = w0

w1 = u1 - projektion(v0, u1)

v1  = 2 * w1

w2 = u2 - projektion(v0, u2) - projektion(v1, u2)

v2 = 5 * w2

# Tjek ortogonal 
v = np.hstack([v0, v1, v2])


# Grammatrice
gram = v.T @ v
print(gram) # Skulle give en diagonal matrice, så de er ortogonale på hinanden.




# Ortogonale polynomier

# Legendre polynomier, klasse navn! 

x, h = np.linspace(-1, 1, 5000, retstep=True)

u0 = np.ones_like(x)
u1 = x
u2 = x**2
u3 = x**3

def indre_produkt(f, g, h): # Indre produkt af funktionerne er integralet
    return np.trapz(f*g, dx=h)

def projektion(f, g, h): 
    return indre_produkt(f, g, h) / indre_produkt(f, f, h) * f

v0 = u0 
w1 = u1 - projektion(v0, u1, h) 
print(w1 - x) # Masse 0'er, de er vinkelrette på hinanden.

#w2 = u2 - projektion(v0, u2, h) - projektion(v1, u2, h)

#print(w2 - u2)

from numpy.polynomial import Polynomial as P
from numpy.polynomial import Legendre as L

fig ,ax = plt.subplots()
for i in range(8): 
    ax.plot(x, L.basis(i)(x))





