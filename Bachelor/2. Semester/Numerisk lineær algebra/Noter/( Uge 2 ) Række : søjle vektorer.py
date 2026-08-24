import numpy as np 
import matplotlib.pyplot as plt
a = np.array([
    [-1.0, 2.0, 3.5, -1.5],
    [4.0, -3.0, 4.1, 2.4], 
    [1.2, -1.2, 3.8, 2.7]])
print(a)
a[2,2]
a.ndim # Hvilken dimension af vektorer vi bruger, 2 dimensioner

x = np.array([1.0, -1.1, 2.0, 3.0, -5.0])
x.ndim # 1 dimension

b = a[0, :] # Udsnit af række 
b.ndim # 1 dimension

c = a[:, 2] # udsnit af søjle.

fig, ax = plt.subplots()
im = ax.matshow(a, cmap = 'coolwarm_r', clim = (-4.5, 4.5)) # cmap eksempler coolwarm_r, coolwarm og Reds
fig.colorbar(im, shrink = 0.65)

6 * a # Skalerer med 6
c.shape 
b = np.array([
    [1.0, 2.0, 3.0, 4.0],
    [1.0, 2.0, 3.0, 4.0], 
    [1.0, 2.0, 3.0, 4.0]]) # For at lægge tal sammen, så lægger man tal sammen. 

print(a + b)
a.T # Transponer Række, søjle til søjle, række og omvendt

v = np.array([
    [1.0],
    [2.0], 
    [3.0],
    [4.0]]
) # Søjlevektor
v
v = np.array([1.0,2.0,3.0,4.0])[:, np.newaxis] # Mindre bøvlet måde at lave søjle vektor.
v

np.vander([3.0, 5])
