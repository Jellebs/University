from Formelsamling.StudieHjaelp import Opgave
from Formelsamling.SignalerOgSystemer import SignalerOgSystemer as SOS
from sympy import * 
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
# Lyd 
import soundcard as sc
from scipy.io import wavfile
import os
import re 

#?     _______        _______           ___      _____   ____  ____________  ____________    __________  _____   ____
#?    |        \     |        \        /   \       |    __/          |             |        /              |    __/  
#?    |        |     |        |       |     |      | __/             |             |        \              | __/     
#?    |________/     |________/       /-----\      |/\__             |             |         --------      |/\__     
#?    |              |        \      |       |     |   \__           |             |                 \     |   \__   
#?  __|__          __|__       \__  _|_     _|_  __|__  __\__       _|_      ______|_____  __________/   __|__  __\__


# * Nummernavngning 
nummerTilDansk = {0: "nul", 1: "en", 2: "to", 3: "tre", 4: "fire", 5: "fem", 6: "seks", 7: "syv", 8: "otte", 9: "ni",
                  10: "ti", 11: "eleve", 12: "tolv", 13: "tretten", 14: "fjorten", 15: "femten", 16: "seksten", 17: "sytten", 18: "atten", 19: "nitten", 
                  20: "tyve", 21: "enogtyve", 22: "toogtyve", 23: "treogtyve", 24: "fireogtyve", 25: "femogtyve", 26: "seksogtyve", 27: "syvogtyve", 28: "otteogtyve", 29: "niogtyve",
                  30: "tredive", 31: "enogtredive", 32: "toogtredive", 33: "treogtredive", 34: "fireogtredive", 35: "femogtredive", 36: "seksogtredive", 37: "syvogtredive", 38: "otteogtredive", 39: "niogtredive"}

# * Billed- / Tex filshåndtering
Billedsti = os.path.dirname(os.path.abspath(__file__)) + "/Latex/Indhold/Billeder/"
def ændreIndstilling(fil, linje, nyværdi): 
    indstilling, værdi = linje.replace(" ", "").split(":")
    indstilling = re.sub(r'[^A-Za-z0-9 ]+', '', indstilling) # Fjern specielle tegn
    værdi = re.sub(r'[^A-Za-z0-9 ]+', '', værdi) # Fjern specielle tegn
    match indstilling: 
        case "Billednr": 
            nr = int(værdi)
            nr += 1
            taltekst = nummerTilDansk[nr]
            nr = str(nr)
            fil.write(f"% {indstilling}:{nr}\n")
            ekstra = r"\newcommand{\fig" + taltekst +  r"}[1]"
            return ekstra

def ændreTexFil(indstilling, nyværdi = None, tilføjelser = None):
    # Stier
    scriptpath = os.path.dirname(os.path.abspath(__file__)) 
    texFil = Billedsti + "Billeder.tex"
    texFilSikkerhedskopi = Billedsti + "BillederMidlertidig.tex"
    # Skaf indhold  
    f = open(texFil, "r"); lines = f.readlines(); f.close()          
    
    # Omskriv indhold
    erIndstilling = False
    f = open(texFilSikkerhedskopi, "w")        
    ekstra = ""
    for line in lines:
        if erIndstilling:
            if line == "\n": erIndstilling = False
            if indstilling in line:
                ekstra = ændreIndstilling(f, line, nyværdi) + tilføjelser
                continue
        elif "Indstillinger" in line:
            erIndstilling = True            
        f.write(line)
    f.close() 
    
    # Tilføj 
    f = open(texFilSikkerhedskopi, "a")
    if ekstra != "": 
        f.write(ekstra + "\n")
    # if tilføjelser is not None: f.write(tilføjelser)
    f.close()
    
    texFilLager = Billedsti + "Billederkopi.tex"
    print(texFil)
    print(texFilLager)
    print(texFilSikkerhedskopi)
    
    os.rename(texFil, texFilLager)              # Cache fil
    os.rename(texFilSikkerhedskopi, texFil)     # Opdater ny fil
    os.rename(texFilLager, texFilSikkerhedskopi)# Sikkerheds kopier den gamle
    
def gemBillede(navn, fig): 
    scriptpath = os.path.dirname(os.path.abspath(__file__))
    filsti = Billedsti + navn
    print(filsti)
    fig.savefig(filsti)
    ændreTexFil(indstilling="Billednr", tilføjelser = r"{\fig{" + navn + r"}{#1}}")


#?    _______       _______      _______         ___      __           __   __________  _____  _____  ___________   ____  ______  ___              _______  
#?   /       \     |       \    /               /   \       \         /    |              |      |               |   | \ /         |              |       \ 
#?  |         |    |        |  |               |     |       \       /     |              |      |               |   |  \          |              |        |
#?  |         |    |_______/   |      ____     /-----\        \     /      |------        |------|               |   |---\------   |              |_______/ 
#?  |         |    |           |          |   |       |        \   /       |              |      |    ____       |   |    \        |       ___    |         
#?   \_______/   __|__          \________/   _|_     _|_       _\_/_       |__________  __|__  __|__    \_______/   _|_   _\____    \_______/   __|__       
def diskretePlotAfFunktioner(fig, ax, n, plots, colormap = plt.cm.viridis): 
    """ 
    plots = {
        "label1": x1, 
        "label2": x2, 
        ....
    }
    """
    colors = colormap(np.linspace(0, 1, len(plots))) if colormap is not None else np.array(["blue" for _ in range(len(plots))])

    ax = ax.flatten()
    for i, (label, x) in enumerate(plots.items()):
        markerline, stemlines, baseline = ax[i].stem(n, x, markerfmt='go', label= label)
        plt.setp(stemlines, 'color', colors[i])
        plt.setp(markerline, 'color', colors[i])
        plt.setp(baseline, 'color', colors[i])
    fig.legend()
    plt.show()

def dTM(x, n):     # Diskrete Tidsmodsætter 
    x.reverse()
    n *= -1 
    return np.flipud(n)
    
def dTF(xn, n,  n0):    # Diskrete Tidsforsinkelse
    for i in range(abs(n0)): 
        if n0 < 0 :     # Tidsforsinkelse 
            xn.insert(0, 0)
            n = np.insert(n, 0, n[0] - 1)
        else:           # Tidsforudsigelse
            xn.append(0)
            n = np.append(n, n[-1] + 1)
    return n

    








class opg_kapitel2(Opgave): 
    n = np.arange(-3, 6)
    x =         np.array([0, 0, 0, 1, 2, -1, 3, 0, 0])
    h =         np.array([0, 0, 0, 4, 5,  6, 0, 0, 0])
    hflipped =  np.array([0, 6, 5, 4, 0,  0, 0, 0, 0])
    forskyd = lambda h, h0 : np.insert(h[:-1], 0, 0)
    
    hn1 = forskyd(hflipped, 1)
    hn2 = forskyd(hn1, 1)
    hn3 = forskyd(hn2, 1)
    hn4 = forskyd(hn3, 1)
    hn5 = forskyd(hn4, 1)
    xH = np.array([x * hflipped,
                   x * hn1,
                   x * hn2, 
                   x * hn3,
                   x * hn4, 
                   x * hn5]) # Skulle være piecewise operationer. 
    y = np.sum(xH, axis=1)
    y = np.hstack([[0, 0, 0], y])
    plots = {
        "x": x, 
        "h[n]": hflipped,
        "h_1[n]": hn1,
        "h_2[n]": hn2,
        "h_3[n]": hn3,
        "h_4[n]": hn4,
        "h_5[n]": hn5,
        "y[n]"  : y
    }
    def __init__(self):
        fig, ax = plt.subplots(8, sharex= True)
        diskretePlotAfFunktioner(fig, ax, self.n, self.plots)
        # gemBillede("Opgave til kapitel 2", fig)

class opg2_1(Opgave):  
    n = np.linspace(-20, 40, 61)
    x4 = (0.9 * np.exp(1j*np.pi/10))**n

    plots = {
        "x1": [1 if ni == 0 else 0 for ni in n],
        "x2": [1 if ni >= 0 else 0 for ni in n],
        "x3": 0.8 ** n,
        "x5": 2 * np.cos(2*np.pi*0.3*n + np.pi/3),
        "R{x4}": x4.real,
        "I{x4}": x4.imag,
        "|x4|": np.abs(x4),
        "<x4>": np.angle(x4)  
    }
    def __init__(self):
        fig, ax = plt.subplots(2, 4, sharex = True, figsize = (16, 9))
        diskretePlotAfFunktioner(fig, ax, self.n,  self.plots)
        # gemBillede("Opgave 2.1.png", fig) 

class opg2_2(Opgave): 
    n = np.linspace(0, 4, 5)
    n1 = n.copy()
    xn = [5, 4, 3, 2, 1]
    xn1 = xn.copy()
    n1 = dTM(xn1, n1)
    n1 = dTF(xn1, n1, -2)
    xn1 = np.array(xn1)
    n1 = np.array(n1)
    
    xn2 = xn.copy() 
    n2 = n.copy()
    n2 = dTF(xn2, n2, 2)
    n2 = dTM(xn2, n2)
    def __init__(self):
        fig, ax = plt.subplots()
        ax.stem(self.n, self.xn)
        ax.stem(self.n1, self.xn1)
        ax.stem(self.n2, self.xn2)
        plt.show()

class opg2_5(Opgave): 
    n1 = np.linspace(-20, 20, 41)
    opgb = np.cos(0.1*n1 - np.pi/5)
    n2 = np.linspace(-10, 20, 31)
    opgc = np.cos(0.1*np.pi*n2 - np.pi/5)
    def __init__(self):
        fig, ax = plt.subplots(2, 1) 
        ax[0].stem(self.n1, self.opgb, label = "cos(n/10 - π/5)")
        ax[1].stem(self.n2, self.opgc, label = "cos(πn/10 - π/5)")
        fig.legend()
        plt.show()
    
class opg2_11(Opgave):  
    h1 = np.ones(5)
    h2 = np.array([1, -1, -1, -1, 1])
    h = sig.convolve(h1, h2) 
    h3 = sig.convolve(h, np.ones(3))
    
class opg2_17(Opgave): 
    b = [0.18, 0.1, 0.3, 0.1, 0.18]
    a = [1, -1.15, 1.5, -0.7, 0.25]
    N = 100
    n, h = sig.dimpulse((b, a, 1), n = N)
    
    def opga(self):
        fig, ax = plt.subplots()
        ax.stem(self.n, self.h[0])
        plt.show()
    def opgbc(self): 
        x = np.array([1 if i >= 0 else 0 for i in self.n])
        y_1 = sig.lfilter(self.b, self.a, x)
        h = self.h[0].flatten()
        print(h.shape, x.shape)
        y_2 = np.convolve(x, h)
        print(y_2)
        fig, ax = plt.subplots(2, sharex= True)
        ax[0].stem(self.n, y_1, "blue", label="Filter fundet")
        n_1 = np.arange(0, 199)
        ax[1].stem(n_1, y_2, "orange", label="Convolution fundet")
        fig.legend()
        plt.show()
        gemBillede("Opgave 2.17.c.png", fig)
    
    
    def __init__(self):
        self.opgbc() 
           
class opg2_19(): 
    b = [1]
    D = 410
    a = [1] + [0]*(D -2) + [0.7]
    a = np.array(a)
    default_speaker = sc.default_speaker()
    datasamplerate, lyd = wavfile.read('Hjælpefiler/Python/handel_audio.wav')
    lyd = lyd / (2**15) # 16 bits medføre 1 sign bit og så 15 bits værdier. 
    # 2^15 = 32768 så så høje kan de værdier være. 
    # Ved at dele med 2^15 sørger jeg så for, at lyden er normaliseret mellem -1;1
    # Uden det var lyden irreterende at lytte til. Måske for høj i det. 
    
    def __init__(self): 
        self.default_speaker.play(self.lyd, self.datasamplerate)
        filtreretLyd = sig.lfilter(self.b, self.a, self.lyd)
        self.default_speaker.play(filtreretLyd, self.datasamplerate) 
        # Sjovt at høre, det skaber meget rumklang, men det giver vel også mening, da filteret reagere pr. 50ms
        # Og derfor hører vi den som om, at lyden kommer tilbage til os. 
        
        
        # Igen med tau = 100ms 
        D = round(8192 * 0.1)
        a = [1] + [0]*(D -2) + [0.7]
        filtreretLyd = sig.lfilter(self.b, a, self.lyd)
        self.default_speaker.play(filtreretLyd, self.datasamplerate) 
        
        # Igen med tau = 500ms
        D = round(8192 * 0.5)
        a = [1] + [0]*(D -2) + [0.7]
        filtreretLyd = sig.lfilter(self.b, a, self.lyd)
        self.default_speaker.play(filtreretLyd, self.datasamplerate) 
        
        D = round(8192 * 1)
        a = [1] + [0]*(D -2) + [0.7]
        filtreretLyd = sig.lfilter(self.b, a, self.lyd)
        self.default_speaker.play(filtreretLyd, self.datasamplerate)

class opg2_33(Opgave):
    n = np.arange(-15, 25)
    b = np.array([1, -1], dtype=float)
    a = np.array([1], dtype=float)
    
    x1 = np.array([10 if i >= -10 and i < 20 else 0 for i in n])
    y = sig.lfilter(b, a, x1)
    
    x2 = np.array([i if i >= 0 and i < 10 else (20 - i) if i >= 10 and i < 20 else 0 for i in n])
    y2 = sig.lfilter(b, a, x2)
    
    x3 = np.array([np.cos(np.pi*i/5 - np.pi/2) if i >= 0 and i < 40 else 0 for i in n])
    y3 = sig.lfilter(b, a, x3)
    
    plots = {
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "y1": y,
        "y2": y2,
        "y3": y3,
    }
    def __init__(self): 
        fig, ax = plt.subplots(2, 3)
        diskretePlotAfFunktioner(self.fig, self.ax, self.n, self.plots)
        gemBillede("Opgave 2.33.png", self.fig)
    
class opg2_50(Opgave): 
    D = 400 
    reverb = lambda self, a, DFB, DFF: ([0] * (DFF-1) + [1], [1] + [0] * (DFB-2) + [a])
    # b, a = reverb(0.7, D, D)
    # n, h = sig.dimpulse((b, a, 1), n = 4000)
    default_speaker = sc.default_speaker()
    datasamplerate, lyd = wavfile.read('Hjælpefiler/Python/handel_audio.wav')
    lyd = lyd / (2**15) # 16 bits medføre 1 sign bit og så 15 bits værdier. 
    
    def opgd(self): 
        D = lambda tau: round(tau * 8192)  # Tau i sekunders
        n = np.arange(self.lyd.shape[0])
        tau = [0.05, 0.1, 0.5]
        for forsinkelse in tau: 
            D_nu = D(forsinkelse)
            b, a = self.reverb(0.7, D_nu, D_nu)
            filtreretLyd = sig.lfilter(b, a, self.lyd)
            self.default_speaker.play(filtreretLyd, self.datasamplerate) 
    
    def __init__(self):
        fig, ax = plt.subplots()
        # ax.stem(self.n, self.h[0].flatten())
        # fig.legend()
        # plt.show()
        # gemBillede("Opgave 2.50.png", fig)
        self.opgd()

class opg3_1(Opgave): 
    b1 = [1] + [0]* 9 + [-1/(2**10)]
    a1 = [1, - 1/2]
    
    b2 = [-3]
    a2 = [2, -5, 2]
    
    b3 = [1]
    a3 = [2, -1]
    def __init__(self): 
        fig, ax = SOS.pzplotZ(self.b1, self.a1, roc="ydre")
        # gemBillede("Opgave 3.1.a.png", fig)
        fig, ax = SOS.pzplotZ(self.b2, self.a2, roc_interval=(1/2, 2))
        # gemBillede("Opgave 3.1.b.png", fig)
        fig, ax = SOS.pzplotZ(self.b3, self.a3, roc = "ydre")
        # gemBillede("Opgave 3.1.d.png", fig)

class opg3_4(Opgave): 
    z = symbols("z")
    b1 = [1, -1/3]
    # print(expand((1 - z**(-1)) * (1 + 2*z**(-1))))
    a1 = [1, 1, -2]
    r, p, k = sig.residuez(b1, a1)
    res_partialFraction1 = r[0]/(1 - p[0] * z**(-1)) + r[1]/(1 - p[1] * z**(-1))
    
    b2 = [1, -1]
    a2 = [1, -1/4]
    r, p, k = sig.residuez(b2, a2)
    res_partialFraction2 = r[0]/(1 - p[0] * z**(-1)) + k[0]
    
    b3 = [1]
    a3 = [1, 3/4, 1/8]
    r, p, k = sig.residuez(b3, a3)
    # print(r, p, k)
    res_partialFraction3 = r[0]/(1 - p[0] * z**(-1)) + r[1]/(1 - p[1] * z**(-1))
    
opg3_4()