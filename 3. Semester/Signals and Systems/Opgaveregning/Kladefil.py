from sympy import * 
import numpy as np


def opgave4_1(): 
    w, t = symbols("t omega")
    eqt = exp(-2*(t-1))
    eqjW = integrate(eqt*exp(-1j*w*t),(t, 0, oo)) 
    pprint(eqjW)
    sol = fourier_transform(eqt, t, w)
    pprint(sol)
    
    # b.
    eqt = exp(-2*(t-1))
    sol = fourier_transform(eqt, t, w)
    pprint(sol)

# opgave4_1()


# Opgaver fra en video om Continuous Time Fourier Series
def CTFS_video(): 
    k = np.array([-4, -3, -2, -1, 1, 2, 3, 4])
    A_k =(np.exp(-1)-1)/(-1-1j*k*2*np.pi)
    for vinkel in np.angle(A_k): 
        pprint(vinkel)

CTFS_video()
    