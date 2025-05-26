from Formelsamling.StudieHjaelp import Opgave
from sympy import *
from scipy.stats import * 
from matplotlib import pyplot as plt
import numpy as np
from scipy import constants
from decimal import Decimal # Videnskabelig notation

def vidskabNotation(tal):       # Videnskabelig notation 
    return '%.2E' % Decimal(tal)

class OpgaveOmOptiskesensorer1(Opgave):
    beskrivelse = "Sagnac interferometry"
    c = constants.c 
    n = 1.46
    cn = c/n 
    P0 = 1
    lamb = 1550e-9
    D = 0.25
    L = 1000
    k = 2*np.pi/lamb
    Omega = np.linspace(0, 4*np.pi, 1000)
    Pud = 2 * (np.cos(k * D * L/(2*cn) * Omega)**2) * P0 
    
    def __init__(self): 
        fig, ax = plt.subplots(figsize=(16, 7.75))
        ax.plot(self.Omega / np.pi, self.Pud)
        ax.grid()
        ax.set_xlabel(r'$\Omega\quad[\frac{\pi}{s}]$')
        ax.set_ylabel(r'$P_{ud}$')
        plt.show()

class OpgaveOmOptiskeSenorer2(Opgave): 
    beskrivelse = "Fabric- perot interferometry"
    r1, r2, E00, k, x, d, w, t = symbols("r1 r2 E00 k x d w t")
    E0 = sqrt(r1)*E00*exp(1j*k*x + w*t)
    E1 = sqrt(1 - r1) * (-sqrt(r2)) * sqrt(1 - r1) * E00*exp(1j*k*x + w*t)
    Er = E0 + E1
    resultat_Ir = np.abs(Er**2)
    resultat_Ir = simplify(resultat_Ir)
    resultat_Ir = expand(resultat_Ir)
    resultat_Ir = factor(resultat_Ir)
    r1 = 0.01; r2 = 0.1; lamb = 1550e-9; P0 = 1
    d = np.linspace(0, 2 * lamb, 5000)
    P = (r1 + ((1 - r2)**2)*r2 - 2*np.sqrt(r1*r2) * (1 - r1)*np.cos(2*( 2 * d * np.pi)/lamb)) * P0 
    # P = Pr(0.01, 0.2, 1, 1550e-9, d)
    def __init__(self): 
        fig, ax = plt.subplots()
        ax.set_xlabel(r"$d$")
        ax.set_ylabel(r"$P$")
        ax.plot(self.d, self.P, label = r"$P_r$")
        ax.plot((0, 2*self.lamb), (0.09, 0.09))
        
        
        plt.show()
         
class opg3_66(Opgave): 
    beskrivelse = "Data fittingsopgave $n(\lambda) = b + \frac{c}{\lambda}$"
    lamb = np.array([425, 475, 525, 575, 625, 675])*1e-9
    n0 = np.array([1.534, 1.528, 1.523, 1.521, 1.518, 1.517])
    x = 1/(lamb**2)
    # pprint(x)
    res_reg = linregress(x, n0)
    b, c =(res_reg.intercept, res_reg.slope)
    y = b + c * x 
    def __init__(self): 
        fig, ax = plt.subplots()
        ax.plot(self.x, self.n0, "o", label = "Data")
        ax.plot(self.x, self.y, label="Lineær regression", color='red')
        ax.set_xlabel(r'$x = \frac{1}{\lambda^2}$')
        ax.set_ylabel(r'$n(x)$')
        fig.legend()
        plt.show()
    
class opg3_80(Opgave): 
    s = np.array([10.1, 29.2, 51.6, 78.3, 98.9])
    M = np.array([1.31, 4.77, -4.38, -1.27, -0.724])
    #x = -1/(s - f)
    #res_reg = linregress(x, M)
    #b, a = (res_reg.intercept, res_reg.slope)
    
    
    def __init__(self): 
        fig, ax = plt.subplots(3,1)
        #ax[0].plot(self.s, self.M, "o", label = "Data")
        #ax[0].set_ylabel(r'$M$')
        #ax[0].set_xlabel(r'$s$')
        
        ax[0].plot(self.M, self.s, "o", label = "Data")
        ax[0].set_ylabel(r'$s$')
        ax[0].set_xlabel(r'$M$')
        
        res_f = self.s/(1/self.M - 1)
        # print(res_f)
        n = np.arange(1, res_f.shape[0] + 1)
        res_f_mean = np.ones(res_f.shape[0]) * np.mean(res_f)
        ax[1].plot(n, res_f, "o", markersize = 8, color = "orange", label = "F beregning i hvert datapunkt")
        ax[1].plot(n, res_f_mean, color = "orange")
        ax[1].set_ylabel(r'$f$')
        ax[1].set_xlabel(r'$n$')
        
        x = (1/self.M - 1)
        a = res_f_mean
        y = a * x 
        ax[2].plot(self.M, self.s)
        ax[2].plot(self.M, y)
        ax[2].set_xlabel(r'$s$')
        ax[2].set_ylabel(r'$M$')
        
        fig, ax = plt.subplots(2)
        res_f = self.s/(1/self.M - 1)
        n = np.arange(1, res_f.shape[0] + 1)
        res_f_mean = np.ones(res_f.shape[0]) * np.mean(res_f)
        ax[0].plot(n, res_f, 'o', label = "F beregnet i hvert punkt")
        ax[0].plot(n, res_f_mean, color = "blue")
        ax[0].set_xlabel(r'$n$')
        ax[0].set_ylabel(r'$f$')        
        
        
        x = (1/self.M - 1)
        a = res_f_mean
        s = a * x 
        ax[1].plot(x, self.s, "o", color= "orange")
        ax[1].plot(x, s, color= "orange", label = "Regression" )
        ax[1].set_xlabel(r'$\frac{1}{M - 1}$')
        ax[1].set_ylabel(r'$s$')        
        fig.legend()

        plt.show()
        
class opg32_52(Opgave): # Data opgave. 
    m = np.array([0, 1, 2, 3, 4, 5])
    theta = np.array([0, 9.2, 22, 30, 48, 64])
    x = np.sin(np.deg2rad(theta)) # Chronologisk? Ellers så sorter 

    
    reg = linregress(x, m)
    b, a = (reg.intercept, reg.slope) 
    # print(a, b)
    y = a*x + b
    resultat_y = f"m = {N(a, 2)}*x + {N(b, 2)}"
    def __init__(self): 
        fig, ax = plt.subplots()
        ax.plot(self.x, m, 'o', label = "Data")
        ax.plot(self.x, self.y, label = self.resultat_y)
        ax.set_xlabel(r'$\sin{\theta_a}$')
        ax.set_ylabel(r'$m$')
        fig.legend()
        
        plt.show()
    
class Opgave33_34(Opgave): 
    beskrivelse = "Opgave som viser hvorfor der ikke er en æter vind"
    L, c, v = symbols("L c v")
    Tv = 2 * L/c * (1/(sqrt(1 + (v**2)/(c**2)))) 
    Th = 2 * L/c * (1/(1 - (v**2)/(c**2)))
    #Th er den langsomste, da den skal mod æter vinden til sidst. 
    Tvnum = Tv.subs({c: constants.c, v: 100})
    Thnum = Th.subs({c: constants.c, v: 100})
    deltaT = Thnum - Tvnum 
    
    print(Tvnum, Thnum)
    print(deltaT)
    # constants.c

class Opgave33_71(Opgave): # Data opgave
    beskrivelse = "Givet data på en partikels totale energi og dens samtidige momentum, så skal jeg vælge en model, finde værdien for c,"
    beskrivelse += "\nværdien for partiklens masse og beskrive hvilken partikel det er."
    beskrivelse += "\nJeg forstår ikke helt at de også vil have c fundet. Jeg har en ligning med to ubekendte. For nu ignorerer jeg det"
    beskrivelse += "\nVha. formel 33.10 har jeg udledt et lineært udtryk for momentummet."
    beskrivelse += "\np^2 = E^2/c^2 - m^2"
    p = np.array([0, 0.872, 1.41, 2.46, 3.45, 4.61, 5.49])
    E = np.array([0.511, 1.01, 1.51, 2.51, 3.51, 4.51, 5.51])
    
    c = constants.c
    # Convertering til SI enhed 
    # MeV til Joules
    E *= 1.602e-13  # J 
    p *= 1.602e-13/(c)  # J/c 
    
    y = p**2
    reg = linregress(E**2, p**2)
    resultat_b, resultat_a = (reg.intercept, reg.slope) 
    
    resultat_p2 = resultat_a*(E**2) + resultat_b
    def __init__(self): 
        fig, ax = plt.subplots()
        ax.plot(self.E**2, self.p**2, "o", label = "Punkter")
        ax.plot(self.E**2, self.resultat_p2, label = "Regression")
        fig.legend()
        plt.show()

class Opgave34_34(Opgave): 
    c = constants.c
    h = constants.h
    k = constants.k
    R = lambda lamb, T, h, k, c: (2*np.pi * h * (c**2))/((lamb**5) * (np.exp(h*c/(lamb * k * T))))
    resultat_R200nm = vidskabNotation(R(200e-9, 5800, h, k, c))
    resultat_R500nm = vidskabNotation(R(500e-9, 5800, h, k, c))

class Opgave34_81(Opgave): # Data fittings opgave
    beskrivelse = "Givet data fra bølgelængder i forhold til stop potentialet, så skal jeg" 
    beskrivelse += "\nbeskrive en eksperimentiel udgave af plancks konstant."
    beskrivelse += "\nOg så finde arbejdsfunktionen"
    beskrivelse += "\nVha. formel 34.7 har jeg udledt et lineært udtryk for stop potentialet.\n"
    beskrivelse += r"$V_s = \frac{hc}{e_l} * \frac{1}{\lambda} - \frac{\phi}{e_l}$"
    def __init__(self): 
        lamb = np.array([225, 275, 325, 375, 425, 475, 525]) * (10**(-9))
        V_s = np.array([3.25, 2.17, 1.52, 0.962, 0.646, 0.312, 0.065])
        x = 1/lamb
        reg = linregress(x, V_s)
        resultat_a, resultat_b = (reg.slope, reg.intercept) 
        y = resultat_a*x + resultat_b
        fig, ax = plt.subplots()
        ax.plot(x, V_s, 'o')
        ax.plot(x, y)
        ax.set_xlabel(r"$\frac{1}{\lambda}$")
        ax.set_ylabel(r"$V_s$")
        plt.show()
    
class Opgave35_61(Opgave): 
    def __init__(self): 
        n = np.array([4, 5, 7, 8, 10])
        lamb = np.array([1110, 674, 354, 281, 169]) * (10**(-9))
        x = n**2
        reg = linregress(x, 1/lamb)
        a, b = (reg.slope, reg.intercept)
        
        y = a*x + b
        fig, ax = plt.subplots()
        ax.grid()
        ax.plot(x, 1/lamb, 'o')
        ax.plot(x, y, label= fr"a = {N(a, 3)}, b = {N(b, 3)}")
        fig.legend()
        plt.show()
    
   
    
class Opgave36_40(Opgave): 
    h = constants.h 
    J = symbols("J")
    res_J = Eq(J, N(np.sqrt(
        ((30 * np.sqrt(11))**2 ) * ((h**3) / (8 * (np.pi**3))) + 30 * np.sqrt(11) * ((h**2) / (4 * (np.pi**2)))
    ), 6))
    def __init__(self): 
        ""
Opgave36_40()    
