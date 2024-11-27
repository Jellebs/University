import matplotlib.pyplot as plt
import numpy as np 
from sympy import *
from Formelsamling.StudieHjaelp import Opgaver

class Ekstra(): 
    fig, ax = plt.subplots()
    geq = 1.1 
    Vx = np.linspace(0, 3, 100)
    Ix = Vx * geq
    ax.plot(Vx, Ix, label= "Diode konfiguration af MOSFET")
    ax.set_ylabel("Ix[mA]")
    ax.set_xlabel("Vx")
    fig.legend()
    # plt.show()
    
    # Løst for på tavlen en torsdag.
    A = np.array([[1/10 + 1/3.3, -1/10],
                [-1/10, 1/10 + 1/20]])
    b = np.array([[4],
                [4]])
    x = np.linalg.inv(A).dot(b)


Vout1 = lambda Vin, VDD, kn, RD, RF, Ron, Vth : [(Vi**2) * (kn*RD*RF) + Vi*(RD - 2*kn*Vth*RD*RF) + (kn*(Vth**2)*RF*RD + VDD*RF) if Vi > Vth and Vi < 3 else VDD if Vi < Vth else VDD * (1/(1 + RD/Ron)) for Vi in Vin]


class Opgaver_Uge2(Opgaver):
    res_opgave1 = "Svar"
    # Estimeret plot

    def plotFigure(Vin, Vout): 
        # Plot the result
        plt.figure(figsize=(8, 6))
        plt.plot(Vin, Vout, label="Vout(Vin)", color="b")
        # plt.axvline(Vth, linestyle='--', color='r', label=f"Vth = {Vth}V")
        # plt.axhline(VDD, linestyle='--', color='g', label=f"VDD = {VDD}V")

        # Labels and title
        plt.title("Vout as a Function of Vin with Feedback", fontsize=14)
        plt.xlabel("Vin (V)", fontsize=12)
        plt.ylabel("Vout (V)", fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.show()
    
    def lavPlot(self): 
        VDD = 5.0   # Supply voltage (V)
        Vth = 1.0   # Threshold voltage of NMOS (V)
        kn = 1e-3   # Process transconductance parameter (A/V^2)
        RF = 10e3   # Feedback resistor (ohms)
        RD = 5e3    # Drain resistor (ohms)
        Ron = 100e-3 
        Vin = np.linspace(0, VDD, 100)
        self.plotFigure(Vin, Vout1(Vin, VDD, kn, RD, RF, Ron, Vth))




Opgaver_Uge2().lavPlot()