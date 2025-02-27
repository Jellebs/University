import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig
from sympy import * 
import lcapy as lc
from lcapy.discretetime import n, z

def opgave5_1(): 
    Y = lambda X, b, z : b * X(z)

    input1 = lambda z: (z**2 - 3*z*np.cos(np.pi/2))/(z**2 - 6*z*np.cos(np.pi/2) + 9)
    input2 = lambda z: (3*z*np.sin(np.pi/4))/(z**2 - 6*z*np.cos(np.pi/4) + 9)

    omega = np.exp(1j*np.arange(0, np.pi, np.pi/8)) # z = e^(j*omega)
    b = 0.8
    Y1 = Y(input1, b, omega)
    Y2 = Y(input2, b, omega)

    fig, ax = plt.subplots()
    ax.plot(omega, Y1.real, label = "1. Input")
    ax.plot(omega, Y2.real, label = "2. Input")
    fig.legend()
    plt.show()
    print(Y1, Y2)


def opgave3_14(): 
    def lavLigning(A, p, C): 
        yz = 0
        for i in range(min(len(A), len(p))): # len(A) = len(p) ellers er der fejl, men det er for en sikkerhedsskyld.
            yz += A[i] / (1 - p[i]*(z**(-1))) 
        for i in range(len(C)): 
            yz += C[i] * (z**(-i))    
        return yz

    b = [1] 
    a = [1, -1/2]
    
    A, p, C = sig.residuez(b, a)
    print(A, p, C)
    yz = lavLigning(A, p, C) # (1/2)^n, n >= 0 
    yn = yz.IZT()
    print(yn)

    
    

opgave3_14()


