import numpy as np
import scipy.signal as sig
from Uni.Vaerktoejer.Plots import * 
# Opgave 6.1 
k = np.linspace(-2, 2, 5)
omega = np.arange(0, 100, 1) * np.pi
ohm1 = np.pi/5 - 2*np.pi*k
ohm2 = np.pi * 0.3 -2*np.pi*k 
delta = lambda ohm, ohm0: [[(ohm[i] == ohm0[k]).astype(float) for i in range(len(ohm))] for k in range(len(ohm0))]

a = delta(omega, ohm1) 

print(a)
print(omega)
print(ohm1)
print(k)

Xejw = sig.unit_impulse()

Xejw = (5*np.cos(np.pi/6) * (np.pi * (delta(omega, -ohm1) + delta(omega, ohm1))) 
        - np.sin(np.pi/6) * ((np.pi/1j)*(delta(omega, -ohm1)) + delta(omega, ohm1))
        + 4*(np.pi/1j) * (delta(omega, -ohm2) + delta(omega, ohm2))) 

config = Plots_config(
    ylim=[min(Xejw), max(Xejw)], 
    xlim=[min(omega), max(omega)], 
    ylabel = "Xejw",
    xlabel = "Omega"
)
plots = Plots(omega, Xejw, config)
plots.plot()