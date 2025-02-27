from Formelsamling.StudieHjaelp import Opgave
from Formelsamling.SignalerOgSystemer import SignalerOgSystemer as SOS 
from sympy import * 
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


class Opgave1(Opgave):
    t = np.linspace(-10*np.pi, 10*np.pi, 1440)
    
    funktioner = [3*np.cos(3*t + np.pi/3),
                 3*((np.cos(3*t + np.pi/3))**2),
                 np.cos(np.pi/2*t) + np.cos(0.5 * t),
                 np.exp(np.pi*t*1j)]
    # SOS.periodePlot(t, funktioner)  
class Opgave2(Opgave): 
    """
    a = lambda self, k, c, b : (0.5*np.pi*1j*k*c-1+c)/((np.pi**2)*k**2)+(1j*(b-c))/(2*k*np.pi)
    def koefficienter(self, dc, n): 
        ak = np.array([dc                 if k == 0 else
                       self.a(k, -1j, -1) if k % 4 == 1 else 
                       self.a(k,  -1,  1) if k % 4 == 2 else 
                       self.a(k, -1j, -1) if k % 4 == 3 else
                       self.a(k,   1,  1) for k in range(-n, n)], dtype= complex)
        return ak
        
    def plot(self): 
        t = np.linspace(0, 8, 400)
        n = 400 # Koefficienter
        T = 4
        w0 = 2*np.pi/T
        dc = 3/8                    # Calculated the dc value of the signal to be 3/8
        
        a = self.koefficienter(dc, n)
        xt = np.zeros(t.shape)
        for k in range(n - 1): 
            xt += np.real(a[k] * np.exp(-1j*k*w0 * t))
        
        fig, ax = plt.subplots()
        ax.plot(t, xt)
        plt.show()
    """           
class Opgave3(Opgave):
    # Bodeplot
    def plot(): 
        omega = np.logspace(0, 4, 100)
        s = 1j*omega
        H = 1/(s + 3)
        Hjw = 20*np.log10(np.abs(H))
        
        fig, ax = plt.subplots()
        ax.plot(omega, Hjw)
        ax.set_xlabel("$\omega$")
        ax.set_ylabel("$H_{j\omega dB}$")
        plt.show()
    
    t, s = symbols("t s")
    xt = Heaviside(t) * exp(-t)
    Xs = laplace_transform(xt, t, s)[0]
    Hs = 1/(s + 3)
    Ys = Xs*Hs
    # Ys = Ys.apart()           - Enkelt tilfælde hvor det giver det samme bare ikke med normalizeret største nævner. 
    
    
    b = [1]
    a = [1, 4, 3]
    r, p, k = sig.residue(b, a)
    Ys = r[0]/(s - p[0]) + r[1]/(s - p[1])
    pprint(Ys)  
class Opgave4(): 
    xn = np.array([1, 1, 1, 0, 0])
    hn = np.array([2, 2, 2, 2, 2]) 
    yn = np.convolve(xn, hn)
    print(yn)
    
    xnThn = np.outer(xn, hn)
    pprint(xnThn)
    
    def plot(): 
        tt = np.linspace(-2, 10, 100)
        xt = np.array([        1/2 * t**2 if t >= 0 and t < 3 else
                       3 * t              if t >= 3 and t < 5 else
                       8 * t - 1/2 * t**2 if t >= 5 and t < 8 else 
                       0                                            for t in tt  
        ])
        fig, ax = plt.subplots()
        ax.plot(tt, xt)
        plt.show()
    plot()
    convolution()
# Opgave1()
# Opgave2().plot()
# Opgave3()
Opgave4()



