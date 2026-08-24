import numpy as np
from sympy import *
from sympy import init_session
init_printing()
theta = lambda m, lamb, d : np.rad2deg(np.arcsin((m*lamb)/(2*d)))



def opgave3(): 
    lamb = 1.175657e-9
    d = lamb/(2*np.sin(np.deg2rad(77.3)))
    vinkel = lambda m : theta(m, lamb, d)
    for m in range(1, 10): 
        pprint(f"m = {m} =>   theta = {vinkel(m)}")
    
    
opgave3()