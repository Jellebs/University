from Formelsamling.StudieHjaelp import Opgave
from sympy import *
from scipy.stats import * 
from matplotlib import pyplot as plt
import numpy as np
from scipy import constants

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
    
    
    
Opgave33_34()    