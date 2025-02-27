from Formelsamling.StudieHjaelp import Opgave
from sympy import *
from scipy.stats import * 
from matplotlib import pyplot as plt
import numpy as np
class opg3_66(Opgave): 
    beskrivelse = "Data fittingsopgave $n(\lambda) = b + \frac{c}{\lambda}$"
    lamb = np.array([425, 475, 525, 575, 625, 675])*1e-9
    n0 = np.array([1.534, 1.528, 1.523, 1.521, 1.518, 1.517])
    x = 1/(lamb**2)
    pprint(x)
    res_reg = linregress(x, n0)
    b, c =(res_reg.intercept, res_reg.slope)
    y = b + c * x 

    fig, ax = plt.subplots()
    ax.plot(x, n0, "o", label = "Data")
    ax.plot(x, y, label="Lineær regression", color='red')
    ax.set_xlabel(r'$x = \frac{1}{\lambda^2}$')
    ax.set_ylabel(r'$n(x)$')
    fig.legend()
    plt.show()
    
opg3_66()
    


    