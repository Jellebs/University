import numpy as np
from sympy import * 
import matplotlib.pyplot as plt
from Uni.Vaerktoejer.Plots import *

def gain(M, N, T):
    k = lambda slut: np.arange(0, slut, 1)
    omega, k, ak, bk = symbols("omega k ak bk")
    taeller = 0
    naevner = 1
    # Udfolder summations regnestykkerne
    for k in range(0, M + 1): 
        taeller += ((-1)**k)*bk*exp(-1j*omega*k)
    for k in range(1, N + 1): 
        naevner += ((-1)**k)*ak*exp(-1j*omega*k)
    Hejw_sym = taeller/naevner

    pprint(f"Filter med kan blive beskrevet som:")
    pprint(Hejw_sym)
    pprint(f"\nved\nM = {M}\nN = {N}\n")

    pprint("Beregner fra symbols til numerisk")
    pprint("."); pprint(".")
    # Fra symbols til numerisk brug lambdify
    f = lambdify([ak, bk, omega], Hejw_sym, "numpy")
    omega = np.linspace(-T, T, 100)

    Hejwlp = f(1, 1, omega)[:, np.newaxis] # Fra nu
    Hejwhp = f(1, 1, omega - np.pi)[:, np.newaxis]
    return (Hejwlp, Hejwhp, omega)

T = 2*np.pi
Hejwlp, Hejwhp, omega = gain(0, 1, T)
filters = np.hstack([np.abs(Hejwlp), np.abs(Hejwhp)])








config = Plots_config(
    ylim = [0, 10], 
    xlim = [-T, T], 
    ylabel= ["|Hejw|", "|Hej(w-pi)|"],
    xlabel= "Omega",
) 

plots = Plots(omega, filters, config = config)
plots.plot()
