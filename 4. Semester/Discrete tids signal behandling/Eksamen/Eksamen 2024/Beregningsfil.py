from Uni.Formelsamling.Opgaver import Opgave
import numpy as np
from sympy import * 
from scipy import signal as sig
import matplotlib.pyplot as plt

class Opgave1(Opgave):
    a = symbols("a")
    xn = Matrix([[a],
                 [4],
                 [5],
                 [-6]])
    hn = Matrix([3, 2, -1, 0])
    # resultat_xnhn = xn * hn

class Opgave4(Opgave): 
    """
    b = [-1/2, 1]
    a = [1, -1/2]
    z = symbols("z")
    A, p, k = sig.residuez(b, a)
    resultat_partial = (A, p, k)
    resultat_Hz = 1.5/(1-(z**(-1))) -2
    """
    
    f = np.linspace(0, 100, 1000)
    omega = 2*np.pi * f
    z = np.exp(1j*omega)
    H = -2 + 1.5/(1 - 1/z)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(omega, abs(H))
    ax.set_ylim(-1e2, 1e2)
    plt.show()
    

opg1 = Opgave1()
opg4 = Opgave4()
