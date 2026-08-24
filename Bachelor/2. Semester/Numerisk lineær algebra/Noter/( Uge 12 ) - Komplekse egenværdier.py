import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt
from Formelsamling.Numerisk_Lineær_Algebra import * 

# Eksempel om kredsløb med komplekse egenværdier. 
R1 = 5
R2 = 0.8
L = 0.4 # H 
C = 0.1 # F 

A = np.array([
    [-2.0, -2.5],
    [  10, -2.0]])

eq, (lambda0, lambda1) = findLambda(A)
eq0 = A - lambda0 * np.eye(A.shape[0])
eq1 = A - lambda1 * np.eye(A.shape[0])

# Bare fyr los med rækkeoperationer! 
# Nu med komplekse tal, nej hvor spændende... Ironi kan forekomme

v1 = np.array([1, 0 - 2j]) [:, np.newaxis] 
w1 = np.real(v1) # Reel del
z1 = np.imag(v1) # Imag del

# print(A @ v1 - lambda1 * v1)
# Burde give det samme som 
# print(A @ v1 - (-2.0 + 5j) * v1) 
# Problemer mellem python complex og sympy complex formatter

t = np.linspace(0, 8, 100)

print(lambda1)

# sympy format er et problem.
# u0 = np.exp(lambda1.real * t) * ( np.cos(lambda1.imag * t) * w1 + np.sin(lambda1.imag * t ) * z1) # Den imaginære måde af c*v*e^lambda*t 
u0 = np.exp(-2.0 * t) * ( np.cos(5.0 * t) * w1 + np.sin(5.0 * t ) * z1) # Den imaginære måde af c*v*e^lambda*t 

fig, ax = plt.subplots()
ax.plot(t, u0[0, :], label="iL")
fig.legend()

# Nået til 56 min

