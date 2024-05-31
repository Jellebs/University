import numpy as np
import matplotlib.pyplot as peterlys 

a = np.array(
    [
    [2.0, -1.0, -3.0],
    [5.0, 2.0, -4.0]
    ]
    )

b = np.array(
    [
    [1.0, 2.0, 4.0, 0.0], 
    [1.0, 3.0, 2.0, 2.0],
    [3.0, 2.0, 2.0, -1.0]
    ]
)
a.shape
b.shape
# Matrix multiplikation. a har 3 søjler, b har 3 rækker, det er reglen for matrix multiplikation.
# Matrix multiplikation er @ eller np.matmul
a @ b

c = np.array([
    [3.0, -1.0], 
    [2.0, 1.0]
    ])

a @ c # Ugyldig, rækken for matrix 1 skal være mindre end søjlen på matrix 2.

# Rækkefølgen betyder noget, jo!! 
# a x b ≠ b x a 
x = np.array([
    [1.0, 3.0], 
    [0.0, 2.0]])
y = np.array([
    [2.0, 0.0], 
    [0.0, 3.0]])

x,y

x @ y 
y @ x    

x @ y == y @ x 

np.zeros((3,5))
np.ones((2, 7))
np.eye(3) # Identitets matrix

a.shape

a @ np.eye(3) == a # Kendetegnet ved en identitetsmatrix.

# Ydre produkt 
v = np.array([1.0, 2.0, -1.0, -2.0, 0.0])[:, np.newaxis] # Søjle vektor.
v
# Ikke det samme som række - søjle produkt. I stedet for et tal, får vi her en udvidet matrice. 
wt = np.array([[3.0, 1.0, 3.0, 1.0, 3.0]]) # Række vektor.

v @ wt # resultat

fig, ax = peterlys.subplots()
ax.matshow(v @ wt, cmap='coolwarm', clim=(-7,7))
fig.show()