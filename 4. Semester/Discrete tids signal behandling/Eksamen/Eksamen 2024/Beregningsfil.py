import numpy as np
from sympy import *
import scipy.signal as sig
import matplotlib.pyplot as plt
from Formelsamling import KontrolSystemer
xn = np.array([0, 4,  5, -6])
hn = np.array([3, 2, -1,  0])
xnhn = xn[:, np.newaxis] * hn
pprint(xnhn)

# alpha = np.linspace(0, 20, 100)
# magnitude = (1 + alpha/sqrt(2)) +(alpha/sqrt(2))
alpha, z = symbols('alpha z')
eq = alpha**2 + (2/sqrt(2)) * alpha + 0.75
pprint(solve(eq))

b = [-1/2, 1]
a = [1, -1/2]
A, p, k = sig.residuez(b, a)
Hz = sum([A[i]/(1 - p[i]*z**(-1)) for i in range(max(len(A), len(p)))])
Hz += k[0]

w = np.linspace(-3*np.pi, 3*np.pi, 1000)
Hz = lambdify(z, Hz); Hz = Hz(np.exp(1j*w))
Hejw = np.abs(Hz)
HejwdB = np.log10(Hejw)
HejwPhase = np.angle(Hz)


# plots = KontrolSystemer.Plots()
# plots.bodePlot(w, HejwdB, HejwPhase)

H = lambda alpha : (-1/2 + (1-alpha/2)*(z**(-1)) + alpha*(z**(-2)))/(1 - (1/2)*(z**(-1)))
pprint(simplify(H(-1/2)))

# pprint(expand_power_exp(eq))




