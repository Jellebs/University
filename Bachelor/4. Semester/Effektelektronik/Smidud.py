import sympy as sp
import numpy as np
from Uni.Formelsamling.Elektriske_Kredsløb import Spole, Kondensator

eq = ((3400 - 816*np.pi)/(400 - 23.04*(np.pi**2)))**2
print(eq)
spole = Spole()
kondensator = Kondensator()
