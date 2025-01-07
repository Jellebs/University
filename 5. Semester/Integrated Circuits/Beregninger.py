import matplotlib.pyplot as plt
import numpy as np 
from sympy import *
from Formelsamling.StudieHjaelp import Opgave

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


class Opgaver_Uge2(Opgave):
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


class Opgaver_Uge13(Opgave):
    VA, VB, VT, IT, kp, kn, Vthn, Vthp, lamb, Zc1 = symbols('V_A V_B V_T I_T k_p k_n V_THn V_THp lambda Z_c1')
    eq = (VT/Zc1 - IT - VB/Zc1 + 
          kp*(VA**2 + Vthp**2 + 2*VA*Vthp)*(1 - lamb * VB) - 
          kn*(VA**2 + Vthn**2 + 2*VA*Vthn) * (1 + lamb * VB))
    V_A = VT - IT*Zc1
    V_B = VA - IT*Zc1
    res_eq = eq.subs(VB, V_B)
    res_eq = res_eq.subs(VA, V_A)
    res_eq = simplify(res_eq)
    res_eq = factor(res_eq, [IT, VT])
    res_eq = collect(res_eq, [IT, VT]) # IT order max = 3, VT order max = 3
    IT1 = res_eq.coeff(IT, 1); IT2 = res_eq.coeff(IT, 2); IT3 = res_eq.coeff(IT, 3)
    VT1 = res_eq.coeff(VT, 1); VT2 = res_eq.coeff(VT, 2); VT3 = res_eq.coeff(VT, 3)
    ekstra = kn * Vthn**2 + kp * Vthp**2
    lhs = IT*IT1 + IT2*IT**2 + IT3*IT**3 + ekstra
    rhs = VT*VT1 + VT2*VT**2 + VT3*VT**3 
    pprint(lhs)
    res_eq = Eq(lhs, rhs)
    
    
    Eq
    
    

Opgaver_Uge13()
# Opgaver_Uge2().lavPlot() 
