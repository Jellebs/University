from Formelsamling.StudieHjaelp import *
from Formelsamling.SignalerOgSystemer import SignalerOgSystemer as SOS
from sympy import * 
import scipy.signal as sig

import numpy as np
import matplotlib.pyplot as plt
# Lyd 
import soundcard as sc
import scipy.io.wavfile as wav
import os
import re 
# Hjælpe funktioner
import inspect

#?     _______        _______           ___      _____   ____  ____________  ____________    __________  _____   ____
#?    |        \     |        \        /   \       |    __/          |             |        /              |    __/  
#?    |        |     |        |       |     |      | __/             |             |        \              | __/     
#?    |________/     |________/       /-----\      |/\__             |             |         --------      |/\__     
#?    |              |        \      |       |     |   \__           |             |                 \     |   \__   
#?  __|__          __|__       \__  _|_     _|_  __|__  __\__       _|_      ______|_____  __________/   __|__  __\__


# * Nummernavngning 
nummerTilDansk = {0:             "nul",  1:              "en",  2:               "to",  3:              "tre",  4:               "fire",  5:              "fem",  6:               "seks",  7:              "syv",  8:              "otte",  9:              "ni",
                  10:             "ti", 11:           "eleve", 12:             "tolv", 13:          "tretten", 14:            "fjorten", 15:           "femten", 16:            "seksten", 17:           "sytten", 18:             "atten", 19:          "nitten", 
                  20:           "tyve", 21:        "enogtyve", 22:         "toogtyve", 23:        "treogtyve", 24:         "fireogtyve", 25:        "femogtyve", 26:         "seksogtyve", 27:        "syvogtyve", 28:        "otteogtyve", 29:        "niogtyve",
                  30:        "tredive", 31:     "enogtredive", 32:      "toogtredive", 33:     "treogtredive", 34:      "fireogtredive", 35:     "femogtredive", 36:      "seksogtredive", 37:     "syvogtredive", 38:     "otteogtredive", 39:     "niogtredive",
                  40:          "fyrre", 41:       "enogfyrre", 42:        "toogfyrre", 43:       "treogfyrre", 44:        "fireogfyrre", 45:       "femogfyrre", 46:        "seksogfyrre", 47:       "syvogfyrre", 48:       "otteogfyrre", 49:       "niogfyrre",
                  50:      "halvtreds", 51:   "enoghalvtreds", 52:    "tooghalvtreds", 53:   "treoghalvtreds", 54:    "fireoghalvtreds", 55:   "femoghalvtreds", 56:    "seksoghalvtreds", 57:   "syvoghalvtreds", 58:   "otteoghalvtreds", 59:   "nioghalvtreds",
                  60:           "tres", 61:        "enogtres", 62:         "toogtres", 63:        "treogtres", 64:         "fireogtres", 65:        "femogtres", 66:         "seksogtres", 67:        "syvogtres", 68:        "otteogtres", 69:        "niogtres",
                  70:     "halvfjerds", 71:  "enoghalvfjerds", 72:   "tooghalvfjerds", 73:  "treoghalvfjerds", 74:   "fireoghalvfjerds", 75:  "femoghalvfjerds", 76:   "seksoghalvfjerds", 77:  "syvoghalvfjerds", 78:  "otteoghalvfjerds", 79:  "nioghalvfjerds",
                  80:           "firs", 81:        "enogfirs", 82:         "toogfirs", 83:        "treogfirs", 84:         "fireogfirs", 85:        "femogfirs", 86:         "seksogfirs", 87:        "syvogfirs", 88:        "otteogfirs", 89:        "niogfirs",
                  90:       "halvfems", 91:    "enoghalvfems", 92:     "tooghalvfems", 93:    "treoghalvfems", 94:     "fireoghalvfems", 95:    "femoghalvfems", 96:     "seksoghalvfems", 97:    "syvoghalvfems", 98:    "otteoghalvfems", 99:    "nioghalvfems"
}
# * Billed- / Tex filshåndtering
Billedsti = os.path.dirname(os.path.abspath(__file__)) + "/../Latex/Indhold/Billeder/" # Gammel metode før jeg flyttede beregningsfilerne "/Latex/Indhold/Billeder/"
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
    filsti = Billedsti + navn                       # Billedsti + navn 
    print(filsti)
    fig.savefig(filsti)
    ændreTexFil(indstilling="Billednr", tilføjelser = r"{\fig{" + navn + r"}{#1}}")

def latexPrint(udtryk):
    latex_str = latex(udtryk)
    # Replace 'i' with 'j'
    # latex_str = latex_str.replace([('\left', ''), ('right', ''), ('i', 'j')])
    latex_str = latex_str.replace('\left', '')
    latex_str = latex_str.replace(r'\right', '')
    latex_str = latex_str.replace(' i', 'j')
    return latex_str
 
    

#?  _____  _____  ___________   ____  ______  ___              _______     __________                __           __  ____  ______     _______       _____   ____  ____________    _______/   ___________    __________     _______     
#?    |      |               |   | \ /         |              |       \   |                            \         /     | \ /          |        \       |    __/          |        /      /\              |  |              |        \   
#?    |      |               |   |  \          |              |        |  |                             \       /      |  \           |        |       | __/             |       |     _/  |             |  |              |        |   
#?    |------|               |   |---\------   |              |_______/   |------                        \     /       |---\------    |________/       |/\__             |       |   _/    |             |  |------        |________/   
#?    |      |    ____       |   |    \        |       ___    |           |                               \   /        |    \         |        \       |   \__           |       |  /      |  ____       |  |              |        \   
#?  __|__  __|__    \_______/   _|_   _\____    \_______/   __|__         |__________                     _\_/_       _|_   _\____  __|__       \__  __|__  __\__       _|_       \/______/     \_______/   |__________  __|__       \__

def diskretePlotAfFunktioner(fig, ax, n, plots, colormap = plt.cm.viridis): 
    """ 
    plots = {
        "label1": x1, 
        "label2": x2, 
        ....
    }
    """
    colors = colormap(np.linspace(0, 1, len(plots)))    if colormap is not None     else np.array(["blue" for _ in range(len(plots))])
    erListe = True                                      if type(ax) is np.ndarray   else False 
    ax = ax.flatten() if erListe else ax 
    for i, (label, x) in enumerate(plots.items()):
        markerline, stemlines, baseline = ax[i].stem(n, x, markerfmt='go', label= label)        if erListe      else ax.stem(n, x, markerfmt='go', label= label)
        stemlines.set_color(colors[i])
        markerline.set_color(colors[i])
        baseline.set_color(colors[i])
        ax[i].legend(loc = "upper right", labelcolor = colors[i])                               if erListe      else ax.legend(loc = "upper right", labelcolor = colors[i])
        # Sidste måde at løse farverne på. 
        # plt.setp(stemlines, 'color', colors[i])
        # plt.setp(markerline, 'color', colors[i])
        # plt.setp(baseline, 'color', colors[i])
    plt.show()

def diskreteSystemPaavirkning(fig, ax, n, xn, systemer, *args, **kwargs): 
    ax = ax.flatten()
    colormap = plt.cm.viridis if "colormap" not in kwargs.keys() else kwargs["colormap"]
    N = len(systemer)
    colors = colormap(np.linspace(0, 1, N)) if colormap is not None else np.array(["blue" for _ in range(N)])
    for i, (label, hn) in enumerate(systemer.items()):
        label = fr"$y_{i}" if len(label.split('_')) <= 1 else fr"$y_{label.split('_')[1]}"  # regner med h_a -> y_a
        
        # x[n]
        ax[i].plot(n, xn, '.-', color = "blue", label = r'x[n]')
        yn = np.convolve(xn, hn)[: n.shape[0]]
        # y[n]
        markerline, stemlines, baseline = ax[i].stem(n, yn, markerfmt='go', label= label)
        stemlines.set_color(colors[i])
        markerline.set_color(colors[i])
        baseline.set_color(colors[i])
        ax[i].legend(loc = "upper right", labelcolor = colors[i])
    fig.text(0.5, 0.02, r"$n$")
    plt.show()
    return (fig, ax)

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

def filterRepræsentation(r, p, k): 
    N = max(r.shape[0], p.shape[0])
    expression = 0
    z = symbols('z')
    for n in range(N): 
        vaerdi = r[n] # np.complex64(r[n])
        pol = p[n]# np.complex64(])
        expression += vaerdi/(1 - pol * z**(-1))
    for dc in k: 
        expression += dc
    return expression 

def filterRepræsentation(b, a, function): 
    r, p, k = sig.residuez(b, a)
    K = max(r.shape[0], p.shape[0])
    expression = 0
    z = symbols('z')
    variabel = function.args[0]
    func = function.func.__name__
    scipy = Function(f'scipy: {func}')(variabel)
    sympy = Function(f'sympy: {func}')(variabel)
    for n in range(K): 
        vaerdi = r[n] # np.complex64(r[n])
        pol = p[n]# np.complex64(])
        expression += vaerdi/(1 - pol * z**(-1))
    for dc in k: 
        expression += dc
    
    scipy = Eq(scipy, N(expression, 3))
    sympy = Eq(sympy, N(partialFraction(b, a, "DT"), 3))
    return (scipy, sympy)

def stepResponse(b, a, N): 
    n = np.ones(N)
    return sig.lfilter(b, a, n)
    
def impulsResponse(b = None, a = None, N = None):
    """
    b = Koefficienter i tælleren\n
    a = Koefficienter i nævneren\n
    N = Antal i output array. \n
    \n\n
    Hvis a = None så antager jeg, b = input array. \n
    Da en impuls i filtrering bare er en identitets operation, så returnere jeg bare inputtet.\n\n
    y[n] = x[n] * delta[n] = x[n]    
    """
    if a == None: 
        # x input liste er givet. 
        x = b 
        return x 
    n = np.array([1] + [0]*(N-1))
    return sig.lfilter(b, a, n)
    
def frekvensResponse(b, a):
    """ 
    Funktion brugt til at karakterisere systemer.  
    Tager udgangspunkt i scipys sig.freqz til beregning og plotter indenfor [-pi, pi]    
    """
    w, H = sig.freqz(b, a, whole=True)  # [0, 2*pi]
    w = np.fft.fftshift(w - np.pi)      # [0, pi, -pi, 0] 
    H = np.fft.fftshift(H)
    fig, ax = plt.subplots(3, 1, sharex = True, figsize = (16, 7.75))
    w_norm = w / np.pi                              # Normaliseret
    colors = iter(plt.rcParams["axes.prop_cycle"].by_key()["color"])
    
    ax[0].plot(w_norm,               np.abs(H), color = next(colors), label=r"$|H(e^{j\omega})|$")
    ax[1].plot(w_norm, np.rad2deg(np.angle(H)), color = next(colors), label=r"$\angle H(e^{j\omega})$")
    ax[2].plot(w_norm, np.rad2deg(np.angle(H)), color = next(colors), label=r"$\angle H(e^{j\omega})$ unwrapped")
    
    plt.text(0.5, 0.95, 'Forstærknings og fase plot', transform=fig.transFigure, horizontalalignment='center', weight="bold", fontsize = 20)
    ax[0].grid()
    ax[1].grid()
    ax[2].set_xlabel(r"$\omega_{norm} ( \frac{\omega}{\pi} )$")
    ax[2].grid(); ax[2].grid() # Den gider åbentbart ikke første gang ^^
    fig.legend()
    plt.grid()
    plt.show()
    return (fig, ax)

def frekvensResponse(fig = None, ax = None, w = None, frekvensFunktioner = None, *args, **kwargs) -> Tuple:
    """ 
    Funktion brugt til at karakterisere systemer.  
    Tager udgangspunkt i numeriske transformationer lavet vha Fast Fourier Transforms.
    Plotter forstærkning og fase for hver frekvensfunktion givet. 
    
    Hvis system beskrivelse læg 
    b = Koefficienter i tælleren 
    a = Koefficienter i nævneren 
    som parametre 
    
    Hvis frekvens funktioner så giv frekvensfunktionerne som: 
    frekvensFunktioner = {
        'F_1' : F1,
        'F_2' : F2,
        ...       , 
        'F_n' : Fn
    }
    """

    if w is None: # [b, a] er givet
        b = fig
        a = ax
        w, H = sig.freqz(b, a, whole=True)  # [0, 2*pi]
        w = np.fft.fftshift(w - np.pi)      # [0, pi, -pi, 0] 
        H = np.fft.fftshift(H)
        fig, ax = plt.subplots(3, 1, sharex = True, figsize = (16, 7.75))
        w_norm = w / np.pi                              # Normaliseret
        colors = iter(plt.rcParams["axes.prop_cycle"].by_key()["color"])
        
        ax[0].plot(w_norm,               np.abs(H), color = next(colors), label=r"$|H(e^{j\omega})|$")
        ax[1].plot(w_norm, np.rad2deg(np.angle(H)), color = next(colors), label=r"$\angle H(e^{j\omega})$")
        ax[2].plot(w_norm, np.rad2deg(np.angle(H)), color = next(colors), label=r"$\angle H(e^{j\omega})$ unwrapped")
        
        plt.text(0.5, 0.95, 'Forstærknings og fase plot', transform=fig.transFigure, horizontalalignment='center', weight="bold", fontsize = 20)
        ax[0].grid()
        ax[1].grid()
        ax[2].set_xlabel(r"$\omega_{norm} ( \frac{\omega}{\pi} )$")
        ax[2].grid(); ax[2].grid() # Den gider åbentbart ikke første gang ^^
        fig.legend()
        plt.grid()
        plt.show()
        return (fig, ax)
    
    colormap = plt.cm.viridis if "colormap" not in kwargs.keys() else args["colormap"]
    enkeltPlot = np.ndim(ax) == 1 or frekvensFunktioner is None
    N = len(frekvensFunktioner) if frekvensFunktioner is not None else 1
    colors = colormap(np.linspace(0, 1, N)) 
    
    def labelOpsætning(ax = "Første række"):
        ax[0].set_ylabel(r"$|Forstærkning|_{dB}$" if "dB" in args else r"$|Forstærkning|$")   
        ax[1].set_ylabel(r"$\angle$ Vinkel")
        ax[2].set_ylabel(r"$\angle$ Vinkel unwrapped")
        fig.text(0.5, 0.02, r"$\omega \quad [\frac{\omega}{\pi}]$", ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    def raekkeOpsætning(ax, kolonne, række):
        if enkeltPlot: 
            ax[række].sharey(ax[række]) if "delty" in args else ""
            ax[række].grid()
        
        else :  
            ax[række, kolonne].sharey(ax[række, 0]) if "delty" in args else ""
            ax[række, kolonne].grid()
            
    labelOpsætning(ax[:] if enkeltPlot else ax[:, 0])
    
    w = w / np.pi                     # Normaliseret
    for i, (label, H) in enumerate(frekvensFunktioner.items()): 
        mag = 20*np.log10(np.abs(H)) if "dB" in args else np.abs(H)
        ang = np.angle(H)
        ang = np.rad2deg(ang)
        if enkeltPlot: 
            ax[0].plot(w, mag, color = colors[i])
            ax[1].plot(w, ang, color = colors[i])
            ax[2].plot(w, np.unwrap(ang), color = colors[i])
            ax[0].set_title(label)
            raekkeOpsætning(ax, i, 0)
            raekkeOpsætning(ax, i, 1)
            # raekkesetup(ax, i, 2)         # Meget stor variation af hvordan fase diskontinuiteten er. 
            ax[2].grid()
        else: 
            ax[0, i].plot(w, mag, color = colors[i])
            ax[1, i].plot(w, ang, color = colors[i])
            ax[2, i].plot(w, np.unwrap(ang), color = colors[i])
            ax[0, i].set_title(label + r"$(e^{j\omega})$")
            raekkeOpsætning(ax, i, 0)
            raekkeOpsætning(ax, i, 1)
            # raekkesetup(ax, i, 2)         # Meget stor variation af hvordan fase diskontinuiteten er. 
            ax[2, i].grid()
    plt.show()
    return (fig, ax)
    
def frekvensResponse_magnitudePlot(fig = None, ax = None, w = None, frekvensFunktioner = None, *args, **kwargs) -> Tuple:
    """
    Funktion til at plotte magnitudeplottet af et system / systemer.              
    Funktionen kan kaldes på 2 måder              
    frekvensResponse_magnitudePlot(b, a)              
    frekvensResponse_magnitudePlot(fig, ax, w, frekvensFunktioner, ...)\n\n
    
    ---- Parametre ----             
    b beskriver koefficienter i tælleren på et system              
    a beskriver koefficienter i nævneren på et system\n
    
    fig, ax = plt.subplots(N, 1, sharex = True) # Plotter på rækkerne.     
    w er frekvenserne unormaliseret i intervallet [-pi; pi]              
    frekvensFunktionerne er et bibliotek med funktioner:               
    F = {\n
        "F1" : F1, \n
        "F2" : F2, \n
        "...": ... \n
        "FN" : FN \n
    }
    """
    enkeltPlot = np.ndim(ax) == 0 or frekvensFunktioner is None
    colormap = plt.cm.viridis if "colormap" not in kwargs.keys() else args["colormap"]
    N = len(frekvensFunktioner) if frekvensFunktioner is not None else 1
    colors = colormap(np.linspace(0, 1, N)) 
    
    def rækkeOpsætning(ax = "Række i", legend = None):
        ax.set_ylabel(legend)
        ax.grid()
    print(f"{enkeltPlot=}")
    if enkeltPlot:
        # Bliver brugt hvis system er givet.
        b = fig
        a = ax
        if w is None: 
            # System givet
            w, H = sig.freqz(b, a, whole=True)  # [0, 2*pi]
            w = np.fft.fftshift(w - np.pi)      # [0, pi, -pi, 0] 
            H = np.fft.fftshift(H)
            fig, ax = plt.subplots()
        else : 
            label, H = next(iter(frekvensFunktioner.items()))
        mag = 20*np.log10(np.abs(H)) if "dB" in args else np.abs(H)  
        w_norm = w / np.pi 
        
        # Setup
        rækkeOpsætning(ax)
        ax.set_xlabel(r"$\omega \quad [\frac{\omega}{\pi}]$")
        ax.set_title(r"$|H(e^{j\omega})|$")
        
        #Plot
        ax.plot(w_norm, mag, color =colors[0])
        plt.show()
        return (fig, ax)
    
    
    #Flere plots
    for i, (label, H) in enumerate(frekvensFunktioner.items()): 
        mag = 20*np.log10(np.abs(H)) if "dB" in args else np.abs(H)
        w_norm = w / np.pi
        
        ax[0].set_title(label + r"$(e^{j\omega})$")
        
        rækkeOpsætning(ax[i], legend = label)
        ax[i].plot(w_norm, mag, color = colors[i])
    plt.show()
    return (fig, ax)
    
    
    

#?    _______       _______      _______         ___      __           __   __________     _______     
#?   /       \     |       \    /               /   \       \         /    |              |        \   
#?  |         |    |        |  |               |     |       \       /     |              |        |   
#?  |         |    |_______/   |      ____     /-----\        \     /      |------        |________/   
#?  |         |    |           |          |   |       |        \   /       |              |        \   
#?   \_______/   __|__          \________/   _|_     _|_       _\_/_       |__________  __|__       \__

class Opgave_HjerteImpulser(Opgave): 
    cwd = os.getcwd()
    dataMappe = cwd + "/Hjælpefiler/Data/"
    navn = "ecg.dat"
    fil = dataMappe + navn
    data = np.loadtxt(fil, delimiter = ",")
    fs = 500 # Hz
    
    # Data
    T_0 = data.shape[0] / fs                # Samples / (Samples / sekund ) -> Sekunder
    t = np.linspace(0, T_0, data.shape[0])
    def visData(self):
        print(self.data.shape[0])
        fig, ax = plt.subplots(figsize = (16, 7.75))
        ax.plot(self.t, self.data)
        gemBillede("EKG_data.png", fig)
        plt.show()
    
    # Frekvens analyse
    data_fft = np.fft.fft(data)
    Ts = 1/fs                               # Tid før hver sample. 
    f = np.fft.fftfreq(data.shape[0], Ts)   # Dataset som længde, Ts som sampling spacing. 
    
    def visFrekvensSpektrum(self): 
        fig, ax = plt.subplots(figsize = (16, 7.75))
        ax.plot(self.f, self.data_fft)
        ax.set_xlabel(r"$Frequency f \in [Hz]$")
        gemBillede("EKG_frekvenspektrum.png", fig)
        plt.show()                              # 49:50 Hz støj. 
    
    # Filtrering 
    # Jeg skulle ved hjælp af formel 5.125 designe et notch filter. 
    # Formel 5.125 adskiller sig fra 5.124 ved at i stedet for valget om at sætte nullerne på enhedscirklen, så er de blevet sat på enhedscirklen i 5.125
    # H(z) = b0 * [1 - 2cos(theta)*z^{-1} + z^{-2}], b0 forstærkning. 
    f0 = 49.75                              # Fjern støj omkring 49.75 Hz
    theta = 2 * np.pi * (f0/fs)             # Fjern støj i form af vinkelfrekvens.                     
    # Top i . e^0 = 1. b0 * [1 - 2 * cos(0.2*pi) + 1].
    # b0 => dc = 1:         
    b0 = 1 / (2 - 2*np.cos(theta))
    b = [b0, -2*b0*np.cos(theta), b0]
    a = [1]
    
    def filterAnalyse(self):
        w = 2*np.pi*self.f
        z = np.exp(1j*w)
        Hz = self.b0 - 2*self.b0*np.cos(self.theta)*(z**(-1))+ self.b0*(z**(-2))        # Theta ret tæt på DC, derfor kompensere filteret i de yderste frekvenser med højere gain.   
        frekvensFunktioner = {
            r"$H(z)$" : Hz[:1000]
        }
        fig, ax = plt.subplots(3, 1)
        frekvensResponse(fig, ax, w[:1000], frekvensFunktioner) 
        gemBillede("EKG_notchfilterAnalyse.png", fig)
        
        fig, ax = SOS.pzplotZ(self.b, np.array(self.a))
        gemBillede("EKG_notchfilterPZmap.png", fig)
    
    y_fft = sig.lfilter(b, a, data)
    y = np.fft.ifft(y_fft)
    def filtretet(self): 
        fig, ax = plt.subplots(2, 1, sharex=True)
        ax[0].plot(self.t, self.data, label = "Signal")
        ax[0].legend(loc="upper right")
        ax[1].plot(self.t, self.y, label = "Signal filtreret")
        ax[1].legend(loc="upper right")
        gemBillede("EKG_signalfiltreret.png", fig)
        plt.show()
    
    # Forbedret Notch filter. Formel 5.126
    # 2 poler er tilføjet med samme vinkel som nulpunkterne, men inden for enhedscirklen. 
    # Det skulle skabe skabere kanter
    b_forbedret = b0 * np.array([1, -2*np.cos(theta), 1])
    a_forbedret = [1, -1.6*np.cos(theta), 0.64]
    # r = 0.8 for at trække 20% af 1.
    r = 0.8
    theta = theta 
    b0_forbedret = 1 / ( (2 -  2 * np.cos(theta)) / (1.64 - 1.6*np.cos(theta))) # DC = 1 af den nye formel. 
    def forbedretFilterAnalyse(self):
        w = 2*np.pi*self.f
        z = np.exp(1j*w)
        Gz = self.b0_forbedret * ( 1 - 2*np.cos(self.theta)*(z**(-1)) + z**(-2) ) / ( 1 - 1.6*np.cos(self.theta) * (z**(-1)) + 2.56*(z**(-2)))
        
        frekvensFunktioner = {
            r"$H(z)$" : Gz[:100]
        }
        fig, ax = plt.subplots(3, 1)
        frekvensResponse(fig, ax, w[:100], frekvensFunktioner) 
        gemBillede("EKGforbedretNotchfilterAnalyse.png", fig)
        
        fig, ax = SOS.pzplotZ(self.b_forbedret, self.a_forbedret)
        gemBillede("EKGforbedretNotchfilterPZmap.png", fig)

    y_fft_forbedret = sig.lfilter(b_forbedret, a_forbedret, data)
    y_forbedret = np.fft.ifft(y_fft_forbedret)
    
    def filtretetForbedret(self): 
        fig, ax = plt.subplots(2, 1, sharex=True)
        ax[0].plot(self.t, self.data, label = "Signal")
        ax[0].legend(loc="upper right")
        ax[1].plot(self.t, self.y_forbedret, label = "Signal filtreret")
        ax[1].legend(loc="upper right")
        gemBillede("EKGforbedretSignalFiltrering.png", fig)
        plt.show()
        
    
    
    
    def __init__(self): 
        #self.visData()
        #self.visFrekvensSpektrum()
        #self.filterAnalyse()
        # self.filtretet()
        # self.forbedretFilterAnalyse()
        self.filtretetForbedret()
    
class Opgave_Temperaturer(Opgave): 
    beskrivelse = "En opgave om data samplet fra et elektrisk kredsløb som opfattede temperaturerne"
    cwd = os.getcwd()
    dataMappe = cwd + "/Hjælpefiler/Data/"
    navn = "temperatures.dat"
    fil = dataMappe + navn
    data = np.loadtxt(fil, delimiter = ",")
    fs = 0.1
    Ts = 1/fs
    N = data.shape[0]
    t = np.arange(0, N*Ts, Ts)
    def visData(self): 
        fig, ax = plt.subplots(figsize=(16, 7.75))
        ax.plot(self.t, self.data)
        ax.set_xlabel(r"$t$")
        ax.set_ylabel(r"$Celsium\degree$")
        # gemBillede("SignalbehandlingTemperaturdata.png", fig)
        plt.show()
    
    def fjernStøj(self, x, N): # Fjerner støj ud fra antal N vægte.
        b = np.array([1/N for _ in range(N)])
        a = np.array([1])
        return sig.lfilter(b, a, x) 
    N = np.array([10, 20, 40])
    def filtreretPlot(self): 
        fig, ax = plt.subplots(3,1, figsize= (16, 7.75), sharex=True)
        
        for i in range(len(self.N)): 
            ax[i].plot(self.t, self.data)
            y = self.fjernStøj(self.data, self.N[i])
            ax[i].plot(self.t, y, label = f"N = {self.N[i]}")
            ax[i].legend(loc="upper right")
        ax[2].set_xlabel(r"$t$")
        ax[1].set_ylabel(r"$Celsius\degree$")
        gemBillede("SignalbehandlingTemperaturdataFiltreret.png", fig)
        plt.show()
    
    def filterAnalyse(self):
        f = np.linspace(-1, 1, 100) 
        w = 2 * np.pi * f
        z = np.exp(1j*w)
        Hz = lambda N, z : np.sum(np.array([1/N * (z ** (-i)) for i in range(N)]), axis = 0)
        
        frekvensFunktioner = {
            r"H_1(z)" : Hz(self.N[0], z), 
            r"H_2(z)" : Hz(self.N[1], z), 
            r"H_3(z)" : Hz(self.N[2], z)
        }
        fig, ax = plt.subplots(3, 3, sharex=True)
        frekvensResponse(fig, ax, w, frekvensFunktioner)
        # gemBillede("SignalbehandlingTemperaturdataFilteranalyse.png", fig)
        
        
    
    
    
    def __init__(self):
        # self.visData()
        # self.filtreretPlot()
        self.filterAnalyse()
    
class Opgave_3DAudio(Opgave): 
    beskrivelse = "En opgave om at styre retningerne fra hvor lyden kommer, ved hjælp af signalbehandling."
    cwd = os.getcwd()
    dataMappe = cwd + "/Hjælpefiler/Data/signals/"
    navn = "speech_fem_4.wav"
    fil = dataMappe + navn
    datasamplerate, lyd = wav.read(fil)
    
    def skafLyd(navn): 
        cwd = os.getcwd()
        dataMappe = cwd + "/Hjælpefiler/Data/signals/"
        fil = dataMappe + navn
        datasamplerate, lyd = wav.read(fil)  
        lyd = lyd / (2**15) # 16 bits medføre 1 sign bit og så 15 bits værdier. 
        # 2^15 = 32768 så så høje kan de værdier være. 
        # Ved at dele med 2^15 sørger jeg så for, at lyden er normaliseret mellem -1;1
        # Uden det var lyden irreterende at lytte til. Måske for høj i det. 
        return datasamplerate, lyd
    
    def afspilLyd(self, lyd, sampleRate): 
        default_speaker = sc.default_speaker()
        default_speaker.play(lyd, sampleRate)
    
    # fs1, lyd1 = skafLyd("speech_fem_4.wav")
    fs = 44100                                  # Alle med samme samplerate
    lyd = {
        "1" : skafLyd("speech_fem_4.wav")[1], 
        "2" : skafLyd("speech_fem_5.wav")[1], 
        "3" : skafLyd("speech_mal_1.wav")[1], 
        "4" : skafLyd("speech_mal_5.wav")[1], 
    }
    # Lave dem af samme længde. 
    def gruppesnak(self):
        N = np.max([lyd.shape[0] for _, lyd in self.lyd.items()])
        padToMatch = lambda lyd, maks : np.pad(lyd, (0, maks - lyd.shape[0]))
        gruppesnak = np.sum([padToMatch(lyd, N) for _, lyd in self.lyd.items()], axis = 0)
        return gruppesnak
    
    def manipulerLyd(self, lyd ): 
        cwd = os.getcwd()
        dataMappe = cwd + "/Hjælpefiler/Data/compact/"
        elevation = "elev-20/"
        # Hvad jeg så har hørt er, at man vælger den vinkel som svare til den modsatte sides vinkel. 
        # Vinklerne variere med 180 grader, så 20 grader er det samme som 160 grader, da de begge er 20 grader fra ens lodrette synspunkt.
        H = 20
        H1 = "H-20e020a.wav"
        H2 = "H-20e160a.wav" # Og her skal man ikke blive snydt af H som horizontal (Azimuth) og e (elevation),
                             # det vil have været mega oplagt, men self skulle det da ikke være sådan. 
        H1 = wav.read(dataMappe + elevation + H1)[1]
        H2 = wav.read(dataMappe + elevation + H2)[1]
        
        # Glem hvad jeg sagde, wav filen er gemt som 2 channels, og det er på den måde, at det skal forstås. 
        h1 = H1[:, 0]
        h2 = H1[:, 1]
        
        def vinkelLyd(lyd, elevation, azimuth) -> np.array:
            cwd = os.getcwd()
            dataMappe = cwd + "/Hjælpefiler/Data/compact/"
            
            H = wav.read(dataMappe + elevation + azimuth)[1]
            h1 = H[:, 0]
            h2 = H[:, 1]
            venstre = np.convolve(lyd, h1)[: lyd.shape[0]]
            højre = np.convolve(lyd, h2)[: lyd.shape[0]]        # Jeg er kun intereseret i filtrering "steady state" og ikke slutningen. 
            lydud = np.vstack([venstre, højre])
            lydud /= np.max(lydud)
            lydud = lydud.T                                     # 437628, 2 
            lydud = np.int16(lydud * (2 ** 15))                 # Alt efter datatype bliver lyden lavet ud fra det. Originalen var 16 bit.
            # Int værdier af 32765 er ikke ballade, men float værdier på 32765 er meget ballade. 
            # Mistede næsten min trommehinde :D 
            return lydud
        
        def gemLyd(lyd, elevation, azimuth, filnavn): 
            lydud = vinkelLyd(lyd, elevation, azimuth)
            wav.write(cwd + f"/Hjælpefiler/Data/signals/{filnavn}", 44100, lydud)

        # Placering af 3 stemmer forskellige steder. 
        lyd1 = vinkelLyd(self.lyd["1"], "elev-20/", "H-20e020a.wav")
        lyd2 = vinkelLyd(self.lyd["2"], "elev70/", "H70e000a.wav")
        lyd3 = vinkelLyd(self.lyd["3"], "elev30/", "H30e180a.wav")
        N = np.max([lyd.shape[0] for _, lyd in self.lyd.items()])
        
        
        padToMatch = lambda lyd, maks : np.pad(lyd, ((0, maks - lyd.shape[0]), (0, 0)))
        lyd1 = padToMatch(lyd1, N); lyd2 = padToMatch(lyd2, N); lyd3 = padToMatch(lyd3, N)  # Zero padding
        
        lydud = lyd1 + lyd2 + lyd3
        # wav.write(cwd + f"/Hjælpefiler/Data/signals/lydud.wav", 44100, lydud)  
        
        # print(np.max(lydud))
        
        #gemLyd(lyd, "elev-20/", "H-20e020a.wav", "e-20H20.wav")     
        #gemLyd(lyd, "elev-20/", "H-20e090a.wav", "e-20H90.wav")
        #gemLyd(lyd, "elev-20/", "H-20e160a.wav", "e-20H160.wav")
        #gemLyd(lyd, "elev70/", "H70e000a.wav", "e70H00.wav")
        #gemLyd(lyd, "elev70/", "H70e090a.wav", "e70H90.wav")
        #gemLyd(lyd, "elev70/", "H70e180a.wav", "e70H180.wav")

    # Undersøge filtrerene på baggrund af den orientering jeg vælger.
    def filterAnalyse(self, elevation, azimuth): 
        cwd = os.getcwd()
        dataMappe = cwd + "/Hjælpefiler/Data/compact/"
        H = wav.read(dataMappe + elevation + azimuth)[1]
        print(np.allclose(H[:, 0], H[:, 1]))                            # True
        h1, h2 = (H[:, 0], H[:, 1])
        n = np.arange(0, np.max([len(h1), len(h2)])) 
        fig, ax = plt.subplots(3, 1, figsize = (16, 7.75), sharex=True)
        plots = {
            "Channel1" : h1, 
            "Channel2" : h2, 
            "Forskel"  : h1 - h2
        }
        diskretePlotAfFunktioner(fig, ax, n, plots)
        gemBillede(f"Signalbehandling3DAudio{elevation.replace("/", "") + azimuth.split(".")[0]}.png", fig)
            
        
        
        
    def __init__(self): 
        # self.afspilLyd(self.lyd, self.datasamplerate)
        # self.afspilLyd(self.lyd, self.fs)
        # self.afspilLyd(self.gruppesnak(), self.fs)
        # self.manipulerLyd(self.lyd["1"])
        # self.filterAnalyse("elev70/", "H70e180a.wav")
        # self.filterAnalyse("elev40/", "H40e122a.wav")
        self.filterAnalyse("elev50/", "H50e096a.wav")
        # self.filterAnalyse("elev-20/", "H-20e180a.wav")
        
class Opgave_kapitel2(Opgave): 
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

class Opgave2_1(Opgave):  
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

class Opgave2_2(Opgave): 
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

class Opgave2_5(Opgave): 
    n1 = np.linspace(-20, 20, 41)
    Opgaveb = np.cos(0.1*n1 - np.pi/5)
    n2 = np.linspace(-10, 20, 31)
    Opgavec = np.cos(0.1*np.pi*n2 - np.pi/5)
    def __init__(self):
        fig, ax = plt.subplots(2, 1) 
        ax[0].stem(self.n1, self.Opgaveb, label = "cos(n/10 - π/5)")
        ax[1].stem(self.n2, self.Opgavec, label = "cos(πn/10 - π/5)")
        fig.legend()
        plt.show()
    
class Opgave2_11(Opgave):  
    h1 = np.ones(5)
    h2 = np.array([1, -1, -1, -1, 1])
    h = sig.convolve(h1, h2) 
    h3 = sig.convolve(h, np.ones(3))
    
class Opgave2_17(Opgave): 
    b = [0.18, 0.1, 0.3, 0.1, 0.18]
    a = [1, -1.15, 1.5, -0.7, 0.25]
    N = 100
    n, h = sig.dimpulse((b, a, 1), n = N)
    
    def Opgavea(self):
        fig, ax = plt.subplots()
        ax.stem(self.n, self.h[0])
        plt.show()
    def Opgavebc(self): 
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
        self.Opgavebc() 
           
class Opgave2_19(): 
    b = [1]
    D = 410
    a = [1] + [0]*(D -2) + [0.7]
    a = np.array(a)
    default_speaker = sc.default_speaker()
    datasamplerate, lyd = wav.read('Hjælpefiler/Python/handel_audio.wav')
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

class Opgave2_33(Opgave):
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
    
class Opgave2_50(Opgave): 
    D = 400 
    reverb = lambda self, a, DFB, DFF: ([0] * (DFF-1) + [1], [1] + [0] * (DFB-2) + [a])
    # b, a = reverb(0.7, D, D)
    # n, h = sig.dimpulse((b, a, 1), n = 4000)
    default_speaker = sc.default_speaker()
    datasamplerate, lyd = wav.read('Hjælpefiler/Python/handel_audio.wav')
    lyd = lyd / (2**15) # 16 bits medføre 1 sign bit og så 15 bits værdier. 
    
    def Opgaved(self): 
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
        self.Opgaved()

class Opgave_kapitel3(Opgave): # Sløring og afsløring af billedde
    b = [1, -2, 1]
    a = [1, -1] + [0]*7 + [1, -1] 
    b = np.array(b)
    a = np.array(a)

    r, p, k = sig.residuez(b, a)
    G = Function("G")(symbols("z"))
    resultat_gn = filterRepræsentation(b, a, G)
    
class Opgave3_1(Opgave): 
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

class Opgave3_4(Opgave): 
    z = symbols("z") 
    X = Function("X")(z)
    b1 = [1, -1/3]
    a1 = [1, 1, -2]
    r, p, k = sig.residuez(b1, a1)
    res_partialFraction1 = Eq(X, r[0]/(1 - p[0] * z**(-1)) + r[1]/(1 - p[1] * z**(-1)))
    
    b2 = [1, -1]
    a2 = [1, -1/4]
    r, p, k = sig.residuez(b2, a2)
    res_partialFraction2 = Eq(X, r[0]/(1 - p[0] * z**(-1)) + k[0])
    
    b3 = [1]
    a3 = [1, 3/4, 1/8]
    r, p, k = sig.residuez(b3, a3)
    res_partialFraction3 = Eq(X, r[0]/(1 - p[0] * z**(-1)) + r[1]/(1 - p[1] * z**(-1)))
    
class Opgave3_14(Opgave): 
    b = [1]
    a = [1, np.sqrt(2)/2 * (1 + 1j) + 0.5, np.sqrt(2)/4 * (1 + 1j)]
    r, p, k = sig.residuez(b, a)
    Y = Function("Y")(symbols("z"))
    Y = filterRepræsentation(b, a, Y)
    resultat_Yz = Y
    
class Opgave3_15(Opgave): 
    b = [1]
    a = [1, -3/4, 1/8]
    r, p, k = sig.residuez(b, a)
    Y = Function("H")(symbols("z"))
    resultat_Yz = filterRepræsentation(b, a, Y)
    N = 11
    step = np.ones(11)
    b = [1]
    a = [1, -0.75, 0.125]
    s = Function("s")(symbols("n"))
    resultat_sn = sig.lfilter(b, a, step)
    
class Opgave3_16(Opgave): 
    b = [2, -2]
    a = [1, -1/3]
    r, p, k = sig.residuez(b, a)
    H = Function("H")(symbols("z"))
    resultat_Hz = filterRepræsentation(b, a, H)
    xn = np.array([(1/2)**n for n in range(11)])
    y = Function("y")(symbols("n"))
    resultat_yn = sig.lfilter(b, a, xn)
    
    b = [2, -2]
    a = [1, -5/6, 1/6]
    r, p, k = sig.residuez(b,a) 
    Y = Function("Y")(symbols("z"))
    resultat_Yz = filterRepræsentation(b, a, Y)    
    
class Opgave3_19(Opgave): 
    b = [1] + [0]*9 + [-1/1024]
    a = [1, -0.5]
    
    N = 20
    
    resultat_y1 = impulsResponse(b, a, N)
    resultat_y2 = stepResponse(b, a, N)
    
    H = Function("H")(symbols("z"))
    resultat_Hz = filterRepræsentation(b, a, H)
    
    
    def __init__(self): 
        fig1, ax1 = SOS.pzplotZ(self.b, self.a, roc = "ydre")
        # gemBillede("Opgave 3.19 - pzmap.png", fig)
        
        fig, ax = plt.subplots(2, 1, sharex=True)
        n = np.arange(self.N)
        plots = {
        "Impuls response" : self.resultat_y1,
        "Step response" : self.resultat_y2 
        }
        plt.xlabel("n") 
        diskretePlotAfFunktioner(fig, ax, n, plots)
        # gemBillede("Opgave 3.19 - Respons.png", fig)
        
class Opgave3_20(Opgave): 
    b = [-3, 0, -3]
    a = [1, -4]
    H = Function("H")(symbols("z")) 
    resultat_Hz = filterRepræsentation(b, a, H)

class Opgave5_2(Opgave): 
    omega = np.linspace(-np.pi, np.pi, 200)
    z = np.exp(1j*omega)
    Hz = 0.19/(1 + 0.81 * (1/z))
    
    b = [0.19]  # Numerator coefficients
    a = [1, 0.81]     # Denominator coefficients
    # Compute frequency response
    w, H = sig.freqz(b, a, whole= True)             # [0, 0.2, ..., 2*pi]
    w = np.fft.fftshift(w - pi)                     # [pi, pi + 0.2, ..., 2 * pi, 0, 0.2, ..., pi]
    H = np.fft.fftshift(H)                          # == De negative frekvenser kommer igen efter pi, og derfor har scipy sat det sådan op. 
                                                    # For at plotte det har jeg dog brug for, at det er fra -pi -> pi.                                              
    principal_phase = np.angle(H)  # Principal phase (wrapped within [-pi, pi])
    cumulative_phase = np.unwrap(principal_phase)  # Cumulative phase (unwrapped)

    def __init__(self): 
        fig, ax = plt.subplots(2, 1, sharex = True)
    
        ax[0].plot(self.omega, np.abs(self.Hz), label=r"$|H(e^{j\omega})|$")
        ax[1].plot(self.omega, np.rad2deg(np.angle(self.Hz)), color = "orange", label= r"$\angle H(e^{j\omega}$")
        plt.xlabel(r"$\omega$")
        fig.legend()
        plt.show()
        fig, ax = plt.subplots(figsize = (16, 7.75))    
        ax.plot(self.w / np.pi, self.principal_phase, label="Principal Phase (Wrapped)", linestyle='--')
        ax.plot(self.w / np.pi, self.cumulative_phase, label="Cumulative Phase (Unwrapped)", linestyle='-.')

        ax.set_xlabel("Normalized Frequency (×π rad/sample)")
        ax.set_ylabel("Phase (radians)")
        ax.set_title("Phase Response and Cumulative Phase")
        fig.legend()
        ax.grid()
        plt.show()
    
class Opgave5_2ny(Opgave): 
    b = [0.19]          # Numerator coefficients
    a = [1, 0, 0.81]       # Denominator coefficients
    # 
    # 
    
    eigenfunction = lambda H, z0, fase : exp(fase*1j) * H(z0) * (z0)**symbols("n")
    H = lambda z : 0.19/(1 + 0.81*(z**(-2)))
    y = Function("y")(symbols("n"))
    resultat_yn = Eq(y, 
                     N(eigenfunction(H, exp(0.52*pi*1j), pi/3) + eigenfunction(H, exp(-0.52*pi*1j), -pi/3), 4))
    resultat_latex = latexPrint(resultat_yn)
    r = np.abs(0.7235 + 0.4638j)
    theta = np.angle(0.7235 + 0.4638j)
    udtryk = lambda r, faseskift, fase : r * exp(faseskift*1j) * exp(fase*1j)
    
    resultat_yn = udtryk(r, theta, 0.52*pi*symbols("n")) + udtryk(r, -theta, -0.52*pi*symbols("n")) 
    # Sammenlign med filter
    n = np.arange(0, 60)
    # h = 0.19 * ((0.81)**n)
    x = 2 * np.cos(0.5*np.pi * n + np.pi/3)
    resultat_yn_calculeret = sig.lfilter([0.19], [1, 0, 0.81], x)
    resultat_yn_udledt = 1.76 * np.cos(0.5*np.pi*n + np.pi/6)
    resultat_yn_udledt2 = 2 * np.cos(0.5*np.pi*n + np.pi/3)
    fig, ax = plt.subplots(3) 
    plots = {
        "Beregnet"  : resultat_yn_calculeret, 
        "Udledt"    : resultat_yn_udledt,
        "Udledt2"   : resultat_yn_udledt2
    }
    def __init__(self):
        fig, ax = frekvensResponse(self.b, self.a)
        # gemBillede("Opgave 5.2.png", fig)
        diskretePlotAfFunktioner(self.fig, self.ax, self.n, self.plots)
        # gemBillede("Opgave 5.2.e.png", fig)
    
class Opgave5_4(Opgave):
    b = [1, -0.5]
    a = [1, -1/3]
    
    # res_H = partialFraction(b, a, "DT")
    res_H = filterRepræsentation(b, a , Function("H")(symbols("z")))
    res_latex = latexPrint(res_H[0])

class Opgave5_16(Opgave): 
    f = np.linspace(-1, 1, 100, dtype= float)
    w = 2 * np.pi * f 
    z = np.exp(-1j*w) # Normalt e^jw, men med vander matricen, så burde det passe med e^{-mj\omega}
    M = 20 
    
    z_wander = np.vander(z, M, increasing = True) 
    Hz = 1/M * np.sum(z_wander, axis = 1)
    Hz1 = lambda N, z : np.sum(np.array([1/N * (z ** (-i)) for i in range(N)]), axis = 0)
    frekvensFunktioner = {
        "Moving average" : Hz, 
        "Moving average med lambda" : Hz1(M, z) 
    }
    # fig, ax = plt.subplots(3, 2, figsize = (16, 7.75))
    # frekvensResponse(fig, ax, w, frekvensFunktioner)
    # Resultaterne vidste at vander metoden giver samme gain som hvis jeg havde brugt lambda funktionen. Dens fase er dog stik modsat. Ved ikke lige hvorfor. 
    
    # Men nu skal jeg egentlig også vise en ændring i tids domænet kan danne baggrund for lowpass til højpass. 
    n = np.arange(0, 100)
    h1 = np.pad(1/M * np.ones(M), (0, 100-M)) 
    h2 = np.cos(np.pi * n) * np.pad(1/M * np.ones(M), (0, 100-M)) 
    H1 = np.fft.fft(h1)
    H2 = np.fft.fft(h2)
    ws = 100/(2*np.pi)
    fs = ws/(2 * np.pi) 
    w_fft = np.fft.fftfreq(100, 1/fs)
    H1 = np.fft.fftshift(H1)
    H2 = np.fft.fftshift(H2)
    w_fft = np.fft.fftshift(w_fft)
    # Næste filter, et lavpas filter. 
    
    H = lambda z : (1 + 1.655*(z**(-1)) + 1.655*(z**(-2)) + z**(-3))/(1 - 1.57*(z**(-1)) + 1.264*(z**(-2)) - 0.4*(z**(-3))) 
    z = np.exp(1j*w)
    H3 = H(z)
    # Frekvens versionen af den her relation, bare et frekvensskifte.
    H4 = H(np.exp(1j*(w - np.pi))) 
    
    
   
    def __init__(self): 
        frekvensFunktioner = {
            "Moving average"            : self.H1, 
            "Moving average moduleret"  : self.H2, 
            "Lavpass"                   : self.H3, 
            "Lavpass moduleret"         : self.H4
        }
        fig, ax = plt.subplots(3, 4, figsize = (16, 7.75))
        frekvensResponse(fig, ax, self.w_fft, frekvensFunktioner)
        gemBillede("Opgave 5.16.png", fig)
        
class Opgave5_30(Opgave): 
    
    n = np.arange(60)
    xn = np.sin(0.1*np.pi * n) + 1/3 * np.sin(0.3*np.pi * n) + 1/5 * np.sin(0.5*np.pi * n) 
    hn = [1, -2, 3, -4, 0, 4, -3, 2, -1]
    y_a = np.convolve(xn, hn)
    y_b = 10 * np.fft.fftshift(xn)
    y_b[:10] *= 0
    h_c = 1/9 * np.array([1, 2, 3, 2, 1])
    y_c = np.convolve(xn, h_c)
    h_d = np.array([1, -1.1756, 1])
    y_d = np.convolve(xn, h_d)
    H_e = filterRepræsentation([1, 0, 1.778, 0, 3.1605], [1, 0, 0.5625, 0, 0.3164], Function("H")(symbols("z")))
    
    h_e = -6.75327 * np.array([1, 0.5, -0.5, -1, -0.5, 0.5]) # ... osv. 6.75327 * cos(pi/3 * n) 
    # Den er gentagende i n = 6. For at den skal køre stationær i alle n = 0 < 60, så må jeg gentage mindst 10 gange.
    K = 13
    h_e = np.tile(h_e, K)
    y_e = np.convolve(xn, h_e)
    plots = {
        r"$x[n]$" : xn,
        r"$y_a$" : y_a[:60],
        r"$y_b$" : y_b, 
        r"$y_c$" : y_c[:60], 
        r"$y_d$" : y_d[:60],
        r"$y_e$" : y_e[:60]
    }
    
    def __init__(self): 
        fig, ax = plt.subplots(3, 2, sharex=True, sharey=True)    
        diskretePlotAfFunktioner(fig, ax, self.n, self.plots)

class Opgave5_31(Opgave): 
    # Impulse response
    n = np.arange(-100, 100, 1)
    # nd = 0
    h = 1/(np.pi * n) * (np.sin(n * np.pi/8) - np.sin(n * np.pi / 4) + 0.5*np.sin(n*np.pi * 7 / 8) - 0.5*np.sin(n * np.pi * 5 / 8))
    y = impulsResponse(h)
    plots = {
        r"$y[n]$" : y, 
    }
    
    # Frekvens response
    H = np.fft.fft(h, h.shape[0])
    w = np.fft.fftfreq(h.shape[0])
    frekvensFunktioner = {
        r"$H(e^{j\omega})$" : H
    }
    ##          naNs i h             ##
    print("Any NaNs in h?", np.isnan(h).any())
    print("Any Infs in h?", np.isinf(h).any())
    print("Max amplitude:", np.max(np.abs(h)))
    # Vigtig læring. Fordi nogle af mine værdier i listen har været umulige at beregne,
    # så har h nogle naNs.
    h = np.nan_to_num(h)
    
    
    H = np.fft.fft(h, h.shape[0])
    w = np.fft.fftfreq(h.shape[0])  # (-pi/20 ; pi / 20)
    w = w * (20/pi)                 # (-1     ;       1)
    
    def __init__(self): 
        # Impuls response
        plots = {
            r"$y[n]$" : self.y, 
        }
        fig1, ax1 = plt.subplots()
        diskretePlotAfFunktioner(fig1, ax1, self.n, plots)
        # gemBillede("Opgave 5.31b.png", fig1)
        
        # Frekvens response
        frekvensFunktioner = {
            r"$H(e^{j\omega})$" : self.H
        }
        fig2, ax2 = plt.subplots(3)
        frekvensResponse(fig2, ax2, self.w, frekvensFunktioner)
        # gemBillede("Opgave 5.31c.png", fig2)
        
class Opgave5_38(Opgave): 
    z1 = 1 
    z2 = -1
    p1 = (1 + 1j)/sqrt(2)
    p2 = conjugate(p1)
    
    a = 1/z1
    b = 1/z2
    c = 1/p1 
    d = 1/p2

    z = symbols("z")
    resultat_H = simplify((a - z**(-1))*(b - z**(-1))/((c - z**(-1))*(d - z**(-1))))
    f = np.linspace(-1, 1, 250)
    w = np.pi * f 
    z = np.exp(1j*w)    
    H = lambdify([symbols("z")], resultat_H, modules = "numpy")
    H = H(z)
    resultat_b0 = np.max(np.abs(H))
    H /= resultat_b0
    def __init__(self): 
        frekvensFunktioner = {
            r"$H(e^{j\omega})$" : self.H
        }
        fig, ax = plt.subplots(3, 1,sharex= True)
        frekvensResponse(fig, ax, self.w, frekvensFunktioner)
        
        # Læring. Jeg skal ikke lave en omega som er 2 * pi * f, når f: [-1, 1]
        # Da ville jeg få w = [-2pi; 2*pi]. Og [-2pi; 0] er det samme som [0; 2pi]. 
        # Når jeg så lavede normalisering af mine frekvenser, så manglede mit filter en faktor 2. 
        fig, ax = plt.subplots()
        frekvensResponse_magnitudePlot(fig, ax, self.w, frekvensFunktioner)
    
    
class Opgave5_48(Opgave): 
    N = 8
    K = np.int64(np.ceil(60 / N))
    oploesning = 512
    # w = np.fft.fftfreq(oploesning); w = np.fft.fftshift(w)
    w = np.linspace(-np.pi, np.pi, oploesning)
    xn = np.array([1, 2, 3, 4, 3, 2, 1, 0]); xn = np.tile(xn, K)  
    X = np.fft.fft(xn, oploesning); X = np.fft.fftshift(X)
    z = np.exp(1j*w)

    h_a  = np.array([2, -1, 1, 3, 6, 3, 1, -1, 2])
    h_d = np.array([1, 0.5, 0.25, 0.125, 0.0625])
    
    
    H_a = np.fft.fft(h_a, oploesning); H_a = np.fft.fftshift(H_a)
    H_b = 1/9 * (1 - 0.5*(z**(-1)) + 2*(z**(-2)) + 0.5*(z**(-3)) - (z**(-4)))
    H_c = 5 * np.exp(1j*np.pi * 1/4) * np.ones(H_b.shape[0])
    H_d = np.fft.fft(h_d, oploesning); H_d = np.fft.fftshift(H_d)
    H_e = (1 + 1.7928 * (z**(-2)) + 1.2277*(z**(-4))) / (1 + 1.4603*(z**(-2)) + 0.8145*(z**(-4)))

    w = w / np.pi   # Normalisering. 
    
    
    n = np.arange(0, N * K)
    h_a = np.fft.ifft(H_a, 9)           # Kendt længde fra start af.
    h_b = np.fft.ifft(H_b, 5)           # Feedforward har impulser til hver z^{-i}. 
    h_c = np.fft.ifft(H_c, 1)
    h_d = np.fft.ifft(H_d, 5)
    h_e = np.fft.ifft(H_e, 6)  # Feedforward og feedback. For 5 aftagende funktioner siger jeg, at de approksimativt er 0 efter 6
    systemer = {
        r"$h_a$" : h_a, 
        r"$h_b$" : h_b, 
        r"$h_c$" : h_c,
        r"$h_d$" : h_d, 
        r"$h_e$" : h_e
    }
    
    def __init__(self):
        fig, ax = plt.subplots(3,6, sharex=True)
        frekvensFunktioner = {
            "X" : self.X, 
            r"$H_a$" : self.H_a, 
            r"$H_b$" : self.H_b, 
            r"$H_c$" : self.H_c,  
            r"$H_d$" : self.H_d, 
            r"$H_e$" : self.H_e
        }
        fig, ax = frekvensResponse(fig, ax, self.w, frekvensFunktioner)
        
        fig, ax = plt.subplots(2,3, sharex=True)
        # gemBillede("Opgave 5.48.png", fig)
        fig, ax = diskreteSystemPaavirkning(fig, ax, self.n, self.xn, self.systemer)
        # gemBillede("Opgave 5.48.2.png", fig)
        

Opgave5_38()