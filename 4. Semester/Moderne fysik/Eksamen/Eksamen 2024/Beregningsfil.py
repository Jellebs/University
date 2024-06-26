from Uni.Formelsamling.Opgaver import *
from scipy import constants
import numpy as np

class Opgave5(Opgave): 
    boelgelaengde = np.array([200, 250, 300, 325, 375, 450])
    Vstop = np.array([3.9, 2.66, 1.84, 1.52, 1.01, 0.46])
    plots = Plots()
    plots.config.ylabel = "Stop potentiale"
    plots.config.xlabel = "Frekvens"
    frekvens = constants.c/(boelgelaengde)
    print(frekvens)
    plots.xy = (frekvens, Vstop)

opg5 = Opgave5()