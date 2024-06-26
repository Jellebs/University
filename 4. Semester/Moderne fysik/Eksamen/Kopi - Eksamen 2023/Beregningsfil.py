from Uni.Formelsamling.Opgaver import * 
from Uni.Formelsamling.Elektriske_Kredsløb import Halvledere
from sympy import * 
import scipy.integrate as integrate
import numpy as np
class EksamensOpgave7(Opgave): 
    eV = 1.602176565e-19
    # Funktion til at evaluere integrallet 
    fermi = 1.9
    T = 300 # Kelvin
    resultat_PxCupLedningsbaand, err = integrate.quad(Halvledere.fermi_dirac, 3.44, np.inf, args=(fermi, T))
    

    

opg7 = EksamensOpgave7()
