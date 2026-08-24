import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0.1, 10, 100)
h = 0.1 * x # 10 % fejl fra x

def rel_rel_ændring(x, h): 
    return (np.exp(x+h) - np.exp(x)) / np.exp(x) / (h / x) # Relativ fejl af funktionen kontra relativ fejl af x.

fig, ax = plt.subplots()
ax.plot(x, rel_rel_ændring(x, h)) 
ax.plot(x, rel_rel_ændring(x, 0.1*x), label="0.1x")
ax.plot(x, rel_rel_ændring(x, 0.01*x), label="0.01x")
ax.plot(x, rel_rel_ændring(x, 0.001*x), label="0.001x")
ax.plot(x, x, label="|x|")
ax.legend()

# h -> 0, vil e**x gå mod kappa(x) = 2

# kappa(x) = 10**4
print(10**4 * (10**(-3)) )


v = np.array([1, 2, -1], dtype=float)[:, np.newaxis]

print(np.linalg.norm(v), np.sqrt(6)) # == hinanden 
print(np.linalg.norm(v, 2)) # Standard norm er 2 normen
print(np.linalg.norm(v, 1)) # Lægger alle værdier sammen
print(np.linalg.norm(v, np.inf)) # Uendelig norm giver største værdi 

t = np.linspace(0, 2*np.pi, 100)
v = np.vstack([np.cos(t), np.sin(t)])
print(v.shape)
fig, ax = plt.subplots()
ax.plot(*v)

vn2 = np.linalg.norm(v, 2, axis = 0) # Norm af hver søjle. √(sin**2 + cos**2) = 1, 100 søjler med værdien 1.

vs2 = v / vn2 # / 1 = v 
vs1 = v / np.linalg.norm(v, 1, axis = 0)
vsInf = v / np.linalg.norm(v, np.inf, axis = 0)

fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.plot(*vs1, label = "Første norm")
ax.plot(*vs2, label = "Anden norm")
ax.plot(*vsInf, label = "Uendelig norm")
ax.legend()



A = np.diag(np.array([7, 8, 3, 4, 2]))
print(np.linalg.norm(A, 2))

