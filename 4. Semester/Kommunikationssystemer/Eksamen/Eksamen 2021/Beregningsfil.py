from Uni.Formelsamling.Opgaver import Opgave
from Uni.Formelsamling.Kommunikationssystemer import InformationsTeori
from Uni.Formelsamling.Sandsynlighed_Og_Statistik import Fordelinger as fordelinger
from sympy import * 
import numpy as np


class Opgave1(Opgave):
    inf = InformationsTeori()
    inf.bscErrorProbability = 0.01
    resultat_Channelcapacity = inf.bscCapacity
    resultat_FejlPrSide = fordelinger.binomialFordeling(8, 1, 1e-3) * 3000 # 8 bits pr. side
    resultat_IkkeFundneFejlPrSide = fordelinger.binomialFordeling(8, 2, 1e-3) * 3000
    x00, x01, x10, x11 = symbols("x00 x01 x10 x11")
    p = symbols("p")
    transitionMatrix = Matrix([[x00, x01],
                               [x10, x11]])
    resultat_DobbeltKaskadeKombinationer = transitionMatrix @ transitionMatrix @ transitionMatrix
    resultat_DobbeltKaskade = resultat_DobbeltKaskadeKombinationer.subs([(x00, 1 - p), (x01, p), (x10, p), (x11, 1-p)])
    resultat_dobbeltKaskadeVaerdier = resultat_DobbeltKaskade.subs(p, 0.25)
    
class Opgave2(Opgave): 
    f, omega, t = symbols("x omega t")
    f = Symbol("f", constant = True)
    fc = symbols("fc", konstant=  true)
    RXtau = (1/4) * (exp(1j * t) + exp(-1j * t)) # cos(2*pi*t)/2 
    resultat_RXtau = fourier_transform(RXtau, t, omega, noconds = False) # 
    resultat_SXomega = fourier_transform(RXtau, t, omega, noconds = False)
    


# opg1 = Opgave1()
opg2 = Opgave2()