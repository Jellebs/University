import scipy.signal as sig 
import numpy as np
from sympy import *
from Uni.Formelsamling.SignalerOgSystemer import diskretTid
import Uni.Vaerktoejer.Plots as eplt
class opgave(): 
    __beskrivelse = ""  
    @property 
    def beskrivelse(self): return self.__beskrivelse
    
    @beskrivelse.setter 
    def beskrivelse(self, ekstraBeskrivelse):
        self.__beskrivelse += "\n" + ekstraBeskrivelse; print(ekstraBeskrivelse)

    step = lambda self, tval, k : [(t >= k).astype(float) for t in tval]
    plots = eplt.Plots()
    def updatePlotVariables(self, x, y):
        self.plots.x = x; self.plots.y = y


class opgave1(opgave):
    def opga(self, beskrivelse = ""):
        self.beskrivelse = beskrivelse  
        t = np.linspace(-10, 10, 100)
        ut = self.step(t, 0) 
        self.xct = 5*np.exp(-10*t)*np.sin(20*np.pi*t) * ut 
        self.Xc = diskretTid.dftdirect(self.xct)[:, np.newaxis] 
        
    def opgb(self, beskrivelse = ""):
        self.beskrivelse = beskrivelse  
        self.F = (np.linspace(-50, 50, 100)*2*np.pi)[:, np.newaxis]
        self.updatePlotVariables(self.F, np.hstack([np.abs(self.Xc), np.angle(self.Xc)]))
        # self.plots.plot()
    
    def opgc(self, beskrivelse = ""): 
        self.beskrivelse = beskrivelse
        W = 50
        Xc = np.fft.fft(self.xct, 2*W)[:, np.newaxis]
        self.updatePlotVariables(self.F, np.hstack([np.abs(self.Xc), np.abs(Xc)]))
        self.plots.plot()

opg1 = opgave1()
opg1.opga()
opg1.opgb("b. Plot magnitude and phase plot of Xc from -50Hz < F < 50Hz")
opg1.opgc("c. Use the fft function to approximate the CTFT computation. Chose a sampling rate to minimize aliasing and the number of samples capture the signal waveform. Plot magnitude and phase of your approximation and compare it with the plot in (a) above. ")

