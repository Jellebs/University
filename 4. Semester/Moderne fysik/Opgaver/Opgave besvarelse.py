from Uni.Formelsamling.Fysik import opgaver
from sympy import *
class kapitel34(opgaver):
    def __init__(self) -> None:
        print("Initialiseret")

    def opgave43(self): 
        h, c, k = self.fysiskeKonstanter("h c k")
        
        radians = lambda Lambda, T: (2*h*(c**2)/(Lambda**5)) * 1 /(exp(h*c/(Lambda * k * T ))) 
        R1 = radians(200e-9, 5800)
        R2 = radians(500e-9, 5800)
        
        print(f"R1 = {N(R1, 5)}")
        print(f"R2 = {N(R2, 5)}")
    def opgave50(self): 
        # a. 
        h, c, e = self.fysiskeKonstanter("h c qe")
        arbejde = lambda Lambda, kinmax: h * c/Lambda - kinmax
        arbejdeGjort = arbejde(365e-9, 1.8*e)* (1/e) # 365nm, 1.8 eV => 1.5968eV
        print(arbejdeGjort) # 1.5968 eV 

        # b. Kin_max * q_e = V_stop
        # V_stop [V] = (h * c/lambda - phi) * q_e [J] eller (h * c/lambda - phi) [eV]
        vStop = lambda Lambda: ((h * c/Lambda)*1/e - arbejdeGjort) # arbejdeGjort i eV
        stopPotentialet = vStop(280e-9)
        print(stopPotentialet)









kapitel = kapitel34()
kapitel.opgave50()


