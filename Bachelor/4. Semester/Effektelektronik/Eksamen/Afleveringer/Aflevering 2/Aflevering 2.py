import numpy as np
import matplotlib.pyplot as plt
from sympy import *
s = np.linspace(0, 5000, 100)
R = 1e3 
C = 1e-6
print(1/R*C)
Vc = 1/(1 + R*C*s)
fig, ax = plt.subplots()
# ax.plot(s, Vc)

t, s = symbols("t s")
Vcs = 1/(1 + R*C*s)
Vct = inverse_laplace_transform(Vcs, s, t)
print(Vct)
t = np.logspace(-8, -2, 100)
ut = (t>= 0).astype(float)
Vct = 1000*np.exp(-1000 * t) * ut
print(t, Vct)
ax.plot(t, Vct)

plt.show()


