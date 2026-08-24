import numpy as np 
from sympy import * 
import matplotlib.pyplot as plt
from Formelsamling import KontrolSystemer 
def opgave1(): 
    alpha = 1/2 
    H = lambda z, alpha: 1/(1 - alpha*(z**(-1)))
    
    omega = np.linspace(-3*np.pi, 3*np.pi, 200) 
    Hejw = H(np.exp(1j*omega), alpha)
    HejwdB = 20*np.log10(Hejw)
    HejwPhase = np.angle(Hejw)
    fig, ax = plt.subplots()
    ax.plot(omega, Hejw)
    KontrolSystemer.Plots().bodePlot(omega, HejwdB, HejwPhase)
    plt.show()

def opgave2(): 
    xn = np.array([0, 0, -174, -43, -106, -46, -188, -49, -99, -168, 89, -169, 154, -135, 171, -3, 98, 89, 0, 0], dtype = float)
    x = lambda n : xn[n+2]
    y = lambda n : (1/35) * ( -3*x(n + 2) + 12*x(n + 1) + 17*x(n) * 12*x(n - 1) - 3*x(n - 2))
    yn = np.array([y(n) for n in range(0, 16)], dtype= float)

    # Plot
    fig, ax = plt.subplots()
    xn = xn[2:18]
    n = range(0, 16)
    ax.plot(n, xn)
    # ax.plot(n, yn)
    plt.show()
def opgave3(): 
    H = lambda alpha, z : 1/(1 + alpha * (z**(-1)))
    omega = np.linspace(-3*np.pi, 3*np.pi, 200)
    Hejw1 = H(0.9, np.exp(1j*omega))
    Hejw2 = H(-0.9, np.exp(1j*omega))
    
    Hejw1dB = 20*np.log10(Hejw1)
    Hejw1Phase = np.angle(Hejw1)
    
    Hejw2dB = 20*np.log10(Hejw2)
    Hejw2Phase = np.angle(Hejw2)
    
    KontrolSystemer.Plots().bodePlot(omega, Hejw1dB, Hejw1Phase)
    KontrolSystemer.Plots().bodePlot(omega, Hejw2dB, Hejw2Phase)
    
    
    
    
def opgave5(): 
    N = 2 
    n = np.arange(N)
    k = np.reshape(n, (N, 1))
    kn = k * n
    WNkn = np.exp(((-2*np.pi*1j/N)* kn))
    
    xn = np.array([1, 2])
    xk = xn.dot(WNkn)
    xk2 = np.fft.fft(xn, len(n))
    pprint(xk)
    pprint(xk2)
    
    

opgave3()


