from Uni.Formelsamling.Opgaver import *
import numpy as np
from scipy import constants
# Koncentration af acceptorer i NPN mosfet

Na = lambda ni, Nd, Vb, kB, T, qe : ((ni**2)/Nd)*np.exp(qe*Vb/(kB*T))
class Opgave8(Opgave): 
    ni = 2e13
    Nd = 3.3e14
    Vb = 0.31
    kB = constants.Boltzmann
    qe = constants.elementary_charge
    T = 295
    resultat_Na = Na(ni, Nd, Vb, kB, T, qe)

opg8 = Opgave8()