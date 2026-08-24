import numpy as np
import matplotlib.pyplot as plt
import os 
os.system("clear")


# Check for ortogonal- ortonormalitet 
def check(v1, v2): 
    # Ortogonalitet a @ b == 0
    # Ortonormalitet a @ b == 0, ||a||_2 == 1, ||b||_2 == 1 
    x = np.vdot(v1, v2)
    y = np.linalg.norm(v1), np.linalg.norm(v2)
    
    if x == 0 and y == (1.0, 1.0):#y == (1.0, 1.0): 
        print("Ortonormale matricer")
    elif x == 0: 
        print("Ortogonale matricer")

v0 = np.array([1./2., 1./2., -1./2., -1./2.])[:, np.newaxis]
v1 = np.array([1./2, 1./2., 1./2., 1./2.])[:, np.newaxis]

check(v0, v1)    

# Approksimer funktion
n = 500 
x = np.linspace(-1, 1, n)
# funktion 0 er konstant 1
v0 = np.ones(n)[:, np.newaxis]
# funktion 1 er x
v1 = x[:, np.newaxis]
# funktion 2 er x**2 
v2 = (x**2)[:, np.newaxis]

fig, ax = plt.subplots()
ax.plot(x, v0[:, 0])
ax.plot(x, v1[:, 0])
ax.plot(x, v2[:, 0])
fig.show()

check(v0, v1)
check(v1, v2)
check(v0, v2)

def projektionsSkalar(u, v): 
    # Korteste afstand fra vektoren u til punkt på linjestykket i retningen af vektoren v. 
    # <u, v>/||v||_2**2 * v
    # u.T*v / ||v||_2**2 * v
    # P = u.T*v / ||v||_2**2
    # Bunden bliver kvadreret i to og ganget i to, hvilket udligner hinanden. 

    # Ved vektorer giver projektionen blot en skalar
    # Ved matricer giver projektionen en ny matrice.

    P = np.vdot(u,v) / np.vdot(v, v) # Eller np.linalg.norm(v)**2, men den funktion laver en ekstra kvadratrod så, mener jeg, at Swann fik sagt.
    print(f"Projektions skalar, P: <u, v> / ||v||_2 = {P}")
    return P 

w2 = v2 - projektionsSkalar(v2, v0) * v0

# print(np.vdot(v0, w2)) # Meget tæt på 0.
# print(np.vdot(v1, w2)) # Meget tæt på 0.

# Så v0, v1, w2 er en ortogonal samling.
f = np.exp(x)[:, np.newaxis]
proj_f_v0 = projektionsSkalar(f, v0) * v0
proj_f_v1 = projektionsSkalar(f, v1) * v1
proj_f_w2 = projektionsSkalar(f, w2) * w2

proj_f_samling = proj_f_v0 + proj_f_v1 + proj_f_w2 # v0 = 1, v1 = x, w2 = x**2, taylor approksimation projekteret på den eksponentielle funktion.
fig, ax = plt.subplots()
ax.plot(x, f[:, 0], label="Exp")
ax.plot(x, proj_f_samling, label="Projektion")
ax.plot(x, np.ones(n) + x + x**2, label="Taylor")
fig.legend() # Placerer tekstboks.

# Grammatrix, så vidt jeg ser, så er det et ydre produkt med samme antal rækker som søjler.
v0 = np.array([1.,0., 0.])[:, np.newaxis]
v1 = np.array([0.0,1.0/np.sqrt(2.), -1./np.sqrt(2.)])[:, np.newaxis]
v2 = np.array([0.0, 1.0/np.sqrt(2.), 1./np.sqrt(2.0)])[:, np.newaxis]

v0, v1, v2

v = np.hstack([v0, v1, v2])
print(v)

gram = v.T @ v
print(gram)

# Da resultatet af grammatricen er en diagonal, er denne ortogonal.
# Da den yderligere er dens identitets matrix er den ortonormal.

print(np.vdot(v1, v2))

