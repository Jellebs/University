from Formelsamling.SignalerOgSystemer import SignalerOgSystemer as SOS 
from Formelsamling.StudieHjaelp import Opgave
import numpy as np
import matplotlib.pyplot as plt

class Opgave1_21(Opgave): 
    """ 
    Et Maerkeligt signal, formegentligt samplet fra en harmonisk boelge.  
    """
    ts = np.linspace(-2, 2, 100)
    
    ys = np.array([t if t <= -1 else 
                   1 if t <=  0 else  
                   2 if t <=  1 else
                   2 - t             for t in ts])
    ts = np.insert(ts, 0, -2) # tsstart = -2, -2, os så andre værdier.
    ys = np.insert(ys, 0, 0) # ys(-2) = 0
    # Saa skal jeg proeve at forudsige det manipulerede signal ved at plotte forskellige manipulationer. 
    SOS = SOS()
    
    # x(t - 1)
    tsa = SOS.time_shift(ts, 1)
    
    # x(2 - t) = x(-t + 2) = x(-(t-2))   
    # Saa I virkeligheden kan den forstaes som en tidsforsinkelse, men den tidsforsinkelse er modsat. 
    tsb = SOS.time_shift(SOS.time_rev(ts), 2)
    
    # x(2t + 1)
    tsc = SOS.time_shift(SOS.time_scale(ts, 2), -1)
    
    tsd = SOS.time_shift(SOS.time_scale(ts, -1/2), 4)
    
        
    
    # Aha, saa mangler jeg saa at lave en function til vaert tidsvektor. Det kan jeg ogsaa, men det vil lige tage lidt tid. Maaske en anden dag. 
    # Som estimation kan jeg godt approximere, at funktionen er en cosinus kurve. Den har period i 4. 
    # 2*pi/w0 = T
    # 1/T * 2pi = w0   
    ys_approximation = lambda ts : 1.5*np.cos(2*np.pi/4*ts)
    """
    ys_estimation = ys_approximation(ts)
    ysa = ys_approximation(tsa)
    ysb = ys_approximation(tsb)
    ysc = ys_approximation(tsc)
    ysd = ys_approximation(tsd)
    
    
    ys_dict = {
        "ys_estimation": ys_estimation,
        "a. x(t-1)": ysa, 
        "b. x(2-t)" : ysb, 
        "c. x(2t + 1)": ysc, 
        "d. x(4-t/2)": ysd
    }
    
    SOS.plot_transforms(ts, ys, ys_dict)
    """
    # Svaert at forudsige ud fra det her. Maaske skulle jeg bare lave en funktion som var delt op i 4 kvarter.
    ys_funktion = lambda ts : np.array([ts[i] if i / len(ts) <= 0.25 else 
                               1     if i / len(ts) <= 0.5  else  
                               2     if i / len(ts) <= 0.75 else
                               2 - ts[i]                         for i in range(len(ts))])
    ysa = ys_funktion(tsa)
    ysb = ys_funktion(tsb)
    ysc = ys_funktion(tsc)
    ysd = ys_funktion(tsd)
    ys_dict = {
        "a. x(t-1)": ysa, 
        "b. x(2-t)" : ysb, 
        "c. x(2t + 1)": ysc, 
        "d. x(4-t/2)": ysd
    }
    
    SOS.plot_transforms(ts, ys, ys_dict)

class Opgave1_9(Opgave): 
    """
    Opgave om periodicity 
    """
    n = np.linspace(20, 20, 41)
    y = np.cos(7*np.pi*n)
    fig, ax = plt.subplots()
    ax.stem(y)
    plt.show()
    # ax.stem(n, y, use_line_collection=True
Opgave1_9()