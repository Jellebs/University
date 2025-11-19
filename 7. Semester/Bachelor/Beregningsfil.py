import os 
import itertools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import EngFormatter
import pandas as pd
from sympy import * 
from scipy import constants
from Formelsamling.StudieHjaelp import Beregning, Opgave
import time 
#?  _____  _____  ___________   ____  ______  ___              _______     __________                __           __  ____  ______     _______       _____   ____  ____________    _______/   ___________    __________     _______     
#?    |      |               |   | \ /         |              |       \   |                            \         /     | \ /          |        \       |    __/          |        /      /\              |  |              |        \   
#?    |      |               |   |  \          |              |        |  |                             \       /      |  \           |        |       | __/             |       |     _/  |             |  |              |        |   
#?    |------|               |   |---\------   |              |_______/   |------                        \     /       |---\------    |________/       |/\__             |       |   _/    |             |  |------        |________/   
#?    |      |    ____       |   |    \        |       ___    |           |                               \   /        |    \         |        \       |   \__           |       |  /      |  ____       |  |              |        \   
#?  __|__  __|__    \_______/   _|_   _\____    \_______/   __|__         |__________                     _\_/_       _|_   _\____  __|__       \__  __|__  __\__       _|_       \/______/     \_______/   |__________  __|__       \__


class Vindue_Kaiser(Beregning):
    def I0(x):                                                      # Bessel funktion der bruges til udregning
        m, M = symbols("m M")
        return 1 + Sum(((x/2)**m)/factorial(m), (m, 1, M))
    
    def w(n):                                                       # Vindue funktion
        a, b, M = symbols("alpha beta M")
        w = Piecewise((Function("I_0")(b * sqrt(1 - ((n - a)/a)**2))/Function("I_0")(b), And(0 <= n, n <= M)), 
                      (0, True))
        return w
    
    def __wnnum__(self, M, beta):
        x = symbols("x")
        I0 = Vindue_Kaiser.I0(x)                                    # Henter Funktion
        I0 = I0.subs({"M" : M})                                     # Sætter grænse
        I0num = lambda x : np.float64(I0.subs({"x" : x}).doit())    # Indsætter numerisk værdi og evaluerer 

        # ? Få symbolsk funktion
        n = symbols("n")
        w = Vindue_Kaiser.w(n)
        # ? Udskift konstanter
        konstanter = {
            "beta" : beta, 
            "M"       : M, 
            "alpha" : M / 2
        }
        w = w.subs(konstanter)
        
        # ? Gør numerisk. Brug I0num som funktion
        w = lambdify(n, w, modules=[{'I_0': I0num}, 'numpy'])
        
        # * Test resultat
        # Jeg tror den er rigtig nok. 
        # Han plotter den lidt anderledes, så det ligner at min w[5] == hans w[4]
        # figsyvoghalvfems viser det. 
        
        wn = np.array([w(n) for n in range(M + 1)])
        return wn
    
    def vindue(self, M, beta): 
        return self.__wnnum__(M, beta)

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

def dftmtx(N):          # Diskrete tids fourier transform matrix
    # W_N_(i, j) = e^{-j * (2*pi/N) * (i * j)} # Normaliseret matrice. 
    return scialg.dft(N)
               
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
    
def frekvensResponse(fig = None, ax = None, w = None, frekvensFunktioner = None, *args, **kwargs) -> Tuple:
    """
    Funktion til at plotte magnitudeplottet af et system / systemer.              
    Funktionen kan kaldes på 2 måder              
    frekvensResponse_magnitudePlot(b, a)              
    frekvensResponse_magnitudePlot(fig, ax, w, frekvensFunktioner, ...)\n\n
    
    ---- Parametre ----             
    b beskriver koefficienter i tælleren på et system              
    a beskriver koefficienter i nævneren på et system\n
    
    fig, ax = plt.subplots(M, N, sharex = True): 
    M er antallet af (Magnitude, fase, Unwrapped_fase, Gruppe delay) og N er antallet af plots                   
    w er frekvenserne unormaliseret i intervallet [-pi; pi]              
    frekvensFunktionerne er et bibliotek med funktioner:               
    frekvensFunktioner = {
        'F_1' : F1,
        'F_2' : F2,
        ...       , 
        'F_n' : Fn
    }\n
    ARGS:           
    "Magnitude"     
    "Fase"                  
    "Unwrapped"             
    "Gruppedelay"                     
    Ændre dem, hvis man ønsker dem med. Og sørg for at der er plots nok ned at rækkerne ved opsætning af fig, ax.  
    "Unormaliseret" for at frekvenserne ikke skal normaliseres.
    """
    
    enkeltPlot = np.ndim(ax) <= 1 or frekvensFunktioner is None
    metoder = [funktion for funktion in args if funktion in ["Magnitude", "Fase", "Unwrapped", "Gruppedelay"]] # Samler ønskede funktioner ud af argumentsne
    M = len(metoder)
    metoder = ["Magnitude"] if M == 0 else metoder
    metoder_iter = itertools.cycle(iter(metoder))     # Gør det til et iterativt objekt som gentager sig om og om igen.
    enkeltMetode = M == 1
    colormap = plt.cm.viridis if "colormap" not in kwargs.keys() else args["colormap"]
    N = len(frekvensFunktioner) if frekvensFunktioner is not None else 1
    colors = colormap(np.linspace(0, 1, N)) 
    
    
    def labelOpsætning(ax = "Første række"):
        i = 0 
        if "Magnitude" in metoder: 
            ax[i].set_ylabel(r"$|Forstærkning|_{dB}$" if "dB" in args else r"$|Forstærkning|$") 
            i+=1 
        if "Fase"      in metoder: 
            ax[i].set_ylabel(r"$\angle$ Vinkel")
            i+=1 
        if "Unwrapped" in metoder:                                                    
            ax[i].set_ylabel(r"$\angle$ Vinkel unwrapped")
            i+=1 
        if "Gruppedelay" in metoder: 
            ax[i].set_ylabel(r"$Gruppedelay$")
        fig.text(0.5, 0.02, r"$\omega \quad [\frac{\omega}{\pi}]$" if "Unormaliseret" not in args else r"$\omega$", ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    def plotOpsætning(ax):
        ax.grid()
        
    def plotMetode(ax, w, H, *args, **kwargs): 
        """
        ARGS: 
        "dB"
        
        KWARGS: 
        "color" : blue
        """
        match next(metoder_iter): 
            case "Magnitude": 
                gain = np.abs(H) if "dB" not in args else 20*np.log10(np.abs(H))
                ax.plot(w, gain, **kwargs)
            case "Fase": 
                # vinkel = np.rad2deg(np.angle(H))
                vinkel = np.angle(H)
                ax.plot(w, vinkel, **kwargs)
            case "Unwrapped": 
                vinkel = np.angle(H)
                ax.plot(w, np.unwrap(vinkel), **kwargs)
                # vinkel = np.rad2deg(np.angle(H))
                # ax.plot(w, np.unwrap(vinkel, discont= 180), **kwargs)
            case "Gruppedelay": 
                """
                The derivative in this definition requires that the phase response is a continuous function of frequency.
                Therefore, to compute the group delay, we should use the unwrapped phase response""" # Side 218 i bogen formel 5.59
                unwrapped = np.unwrap(np.rad2deg(np.angle(H)))
                tau_gd = -np.gradient(unwrapped, w)     # Numerisk afledning
                ax.plot(w, tau_gd, **kwargs)
            case default: 
                print("Ski")
            
    if (N and M) != 1: 
        labelOpsætning(ax[:] if enkeltPlot else ax[:, 0])
    w = w / (2 * np.pi) if "Unormaliseret" not in args else w   # Normalisering eller ej.
    ax = ax.flatten(order = "F") if np.ndim(ax) != 0 else ax    # Order "F" -> flattening nedad rækkerne. 
    j = 0               # System
    i = 0               # Metode
    for label, H in frekvensFunktioner.items():                 # For hvert system
        if np.max([N, M]) == 1: 
            ax.set_title(label)
            plotOpsætning(ax)
            plotMetode(ax, w, H, *args, color = colors[i])
            continue
        
        ax[j].set_title(label)
        for _ in range(M):                                      # Beregn for dens metoder.
            plotOpsætning(ax[j])
            plotMetode(ax[j], w, H, *args, color = colors[i])
            j+=1
        i+=1         
    plt.show()
    return (fig, ax)

def GoertzelsFourierTransform(x, ks):
    beskrivelse = r"""
    En algorithme som skulle bedre hvis man kun ønsker bestemte frekvenser.\\
    Forstår det ikke helt endnu, men i stedet for N^2 beregninger laver den NK beregninger, hvor K er antallet af koefficienter man ønsker. 
    
    v_k(z) = v_k[n - 1] + 2\cos(2\pi k /N)v_k[n - 2] + x[n] \\
    X_k(z) = v_k[n] - W_N^k v_k[n - 1] 
    """
    N = len(x)
    shape = max(ks)
    X = np.zeros(shape, dtype=complex)
    v = np.zeros(shape)             
    # print(K)
    for k in ks: 
        # print(k)
        k = k-1 
        b = [1]
        a = [1, -2*np.cos(2*np.pi*k/N), 1]
        v = sig.lfilter(b, a, x)
        X[k] = v[-1] - np.exp(-1j * 2 * np.pi * k/N) * v[-2]
    return X

def højpassFilter(self, M : int, vindue : Function, ws : float, wp: float): 
        """ 
        numpys sinc funktion har den begrænsning, at den ikke er symmetrisk for lige antal M. 
        Det giver fejl i fasen så et lineært fase filter nødvendigvis ikke vil være lineært længere. 
        For at kompensere for det så sætter: 
        1. M = M + 1, for M er lige
        2. Laver sinc funktionen. 
        3. Popper dens midterste element
        4. Fortsætter filter processen. 
        """
        W = wp 
                 
        if M % 2 == 0: M += 1                               # M = M + 1
        n = np.arange(-floor(M/2), ceiling(M/2), dtype= float)       
        
        hd = np.sinc(W * n / np.pi)                         # sin(W n)/(pi n) = W/np.pi * np.sinc(W * n / np.pi) => rect(w/W)
        hd = hd * W / np.pi
        if M % 2 == 1: 
            hd = np.delete(hd, int(floor(M/2)));            # Popper midterste element
            M -= 1                                          # M = M 
            n = np.delete(n, -1)                            
        
        h = hd * np.exp(1j * np.pi * n)                     # Lavpass til højpass 
        h = h * vindue(M)                                   # Dæmper sidetoppende
        
        # Tjek filter
        fig, ax = plt.subplots() 
        ax.set_xlabel(r"$n \pi$")
        ax.set_title("Filter før shift")
        diskretePlotAfFunktioner(fig, ax, n, {r"$h_{lp}[n]$": hd}) 
        return h 

def vindueAnalyse(fig, ax, n, vinduer, *args, **kwargs):
    """
    N x M plot, hvor M er antallet af forskellige plots pr. vindue og N er antallet af vinduer.
    """
    enkeltPlot = np.ndim(ax) <= 1 or vinduer is None
    metoder = [funktion for funktion in args if funktion in ["Impuls", "Magnitude"]] # Samler ønskede funktioner ud af argumenterne
    M = len(metoder)
    metoder = ["Impuls"] if M == 0 else metoder
    metoder_iter = itertools.cycle(iter(metoder))     # Gør det til et iterativt objekt som gentager sig om og om igen.
    enkeltMetode = M == 1
    colormap = plt.cm.viridis if "colormap" not in kwargs.keys() else args["colormap"]
    N = len(vinduer) if vinduer is not None else 1
    colors = colormap(np.linspace(0, 1, N)) 
    
    def labelOpsætning(ax = "Første række"):
        funktioner = ax[:] if enkeltPlot else ax[0, :]
        tidsintervaller = ax[:] if enkeltPlot else ax[N - 1, :]
        i = 0 
        if "Impuls" in metoder: 
            funktioner[i].set_title(r"$x[n]$")
            tidsintervaller[i].set_xlabel(r"$n$")
            i+=1
        if "Magnitude" in metoder: 
            funktioner[i].set_title(r"$|H(e^{j\omega})|_{dB}$")
            tidsintervaller[i].set_xlabel(r"$\omega \quad [\frac{\omega}{\pi}]$" if "Unormaliseret" not in args else r"$\omega$")
            i+=1
    def plotOpsætning(ax):
        ax.grid()
        
    def plotMetode(ax, n, h, *args, **kwargs): 
        """
        ARGS: 
        "dB"
        
        KWARGS: 
        "color" : blue
        """
        match next(metoder_iter): 
            case "Impuls": 
                markerline, stemlines, baseline = ax.stem(n, h, markerfmt='go', label= label)  
                color = kwargs["color"] if "color" in kwargs.keys() else "blue"
                stemlines.set_color(color)
                markerline.set_color(color)
                baseline.set_color(color)
                
                
            case "Magnitude": 
                re = 1024
                H = np.fft.fft(h, re)
                w = np.fft.fftfreq(re)
                
                H = np.fft.fftshift(H)
                w = np.fft.fftshift(w)
                w *= 2 * np.pi
                w = w / (np.pi) if "Unormaliseret" not in args else w       # Normalisering eller ej.
                gain = 20*np.log10(np.abs(H))                               # np.abs(H) if "dB" not in args else 
                ax.plot(w, gain, **kwargs)
            case default: 
                print("Ski")
            
    if (N and M) != 1: 
        labelOpsætning(ax) 
        ax = ax.flatten() if np.ndim(ax) != 0 else ax     # Order "F" -> flattening nedad rækkerne. 
        j = 0               # Metode
        i = 0               # System
        
        for label, h in vinduer.items():                 # For hvert system
            
            if np.max([N, M]) == 1:
                ax.set_ylabel(label)
                plotOpsætning(ax)
                plotMetode(ax, n, h, *args, color = colors[i])
                continue
            
            ax[j].set_ylabel(label)
            for _ in range(M):                                      # Beregn for dens metoder.
                plotOpsætning(ax[j])
                plotMetode(ax[j], n, h, *args, color = colors[i])
                j+=1
            i+=1         
        plt.show()
    return (fig, ax)    

def læsSamples(path, delimiter=','):
    data = open(path, 'r').readlines() # Læst som en string
    data = np.array([line.strip().split(delimiter) for line in data]) # Overflødig tekst -> strip, separeret med kommaer -> split
    headers, data = data[0], data[1:]
    # Nogle data punkter mangler '' -> NaN
    N, _ = data.shape
    for i in range(N):
        line = data[i]; 
        data[i] = [x if x != '' else np.nan for x in line]
    data = np.float64(data)
    return headers, data

def læsCSV(path, delimiter=',', dataType : str = "Samples"):            # Virker ikke optimalt. Pandas har styr på alle de ting det kræver. 
    """
    Jeg har brug for at vide hvilken type data jeg læser, da jeg skal håndtere tomteksterne anderledes.
    type = "Samples" || "Reference"
    path = stien til filen
    delimiter = Hvilket tegn der adskiller værdierne i filen.
    
    Output: 
    headers
    data 
    """
    data = open(path, 'r').readlines() # Læst som en string
    liste = np.ones(len(data[0]))
    for i in range(1, len(data)): 
        linje = data[i].strip().split(delimiter)                                    # Str -> Array ( Overflødig tekst -> strip, separeret med kommaer -> split )
        match dataType: 
            case "Reference":
                N = len(data[i - 1])                                                            # Det må være dataens størrelse på kolonnnerne. 
                liste = np.append(liste, np.array(linje) if linje[0] != '' else np.array([np.nan for _ in range(N)]))   # Tom tekst -> NaN
                    
                # data[i] = linje if linje[0] != '' else [np.nan for _ in range(N)]   # Tom tekst -> NaN
            case "Samples":                                
                liste = np.append(liste, np.array([x if x != '' else np.nan for x in linje]))                           # Tom tekst -> NaN
                # data[i] =                  # Tom tekst -> NaN
                
            case default:
                raise ValueError("dataType skal være enten 'Samples' eller 'Reference'")
    
    headers, data = data[0], data[1:]
    print(data[-5: -1])
    data = np.float64(data)
    return headers, data
    
def læsCSV(path, delimiter=',', dataType : str = "Samples"):
    df = pd.read_csv(path, delimiter=delimiter)
    data = df.values
    data = np.float64(data)
    return "", data
    
def plot(f, P1, n): 
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].plot(f, P1, label=r'$\angle{H_1}$')
    ax[1].plot(f, n, label=r'$n$')
    ax[1].set_xlabel('Frequency [Hz]')
    ax[0].set_ylabel(r'Phase [rad]')
    ax[1].set_ylabel(r'Refractive index $n$')
    ax[0].legend()
    ax[1].legend()
    plt.show()


phase = lambda H: np.unwrap(np.angle(H))
magnitude = lambda H: 20*np.log10(np.abs(H))
nmaerke = lambda m, f, dangle, c, d : 1 + (dangle + 2 * np.pi * m ) * c / (2 * np.pi * f * d) 

# Indlæs data
cwd = os.getcwd() 
mappe = os.path.join(cwd, "Øvelser/Data")
sample_path = os.path.join(mappe, 'Si_500middel.spectr.csv') # 'Ref_500middel.spectr.csv')
reference_path = os.path.join(mappe, 'Si_500middel.pulse.csv') # 'Ref_500middel.pulse.csv')
headers_sam, sample = læsCSV(sample_path)
headers_sam, reference = læsCSV(reference_path)
data = {
    "f_sam" : sample[:, 0] * 1e9,           # GHz
    "A1_sam" : sample[:, 1],
    "A2_sam" : sample[:, 5],
    "P1_sam" : sample[:, 2],
    "P2_sam" : sample[:, 6],
        
    "t_ref" : reference[:, 0] * 1e-12,      # ps -> s
    "sig1_ref" : reference[:, 1] * 1e-9,    # nA -> A
    "sig2_ref" : reference[:, 2] * 1e-9,    # nA -> A,
    
    "t0" : 90e-12                           # Aflæst tidsforsinkelse
}

Tfs = {                                                                                             # Samme frekvens resolution ( 10001 Res )
    "H_sam" : data["A1_sam"] * np.exp(1j*data["P1_sam"]),          
    "H_ref" : np.conj(np.fft.rfft(data["sig1_ref"], 2 * len(data["f_sam"]) - 1))                    # Samplingen er foretaget til de negative frekvenser, for et reelt signal er de positive frekvensers fase den konjugerede af de negatives.
}
dangle = phase(Tfs["H_ref"]) - phase(data["P1_sam"])
w = 2*np.pi*data["f_sam"]

def tidsplot(data): # f {ifft}-> t 
    fig, ax = plt.subplots(2, 1)
    plots = {                                                       # Samme resolution ( 2000 )
        "sig_ref" : data["sig1_ref"],
        "sig_sam" : np.fft.ifft(data["A1_sam"] * np.exp(1j*data["P1_sam"]), len(data["t_ref"]))
    }
    diskretePlotAfFunktioner(fig, ax, data["t_ref"], plots)

def frekvensplot(data): # t {fft} -> f
    Tfs = {                                                                                             # Samme frekvens resolution ( 10001 Res )
        "H_sam" : data["A1_sam"] * np.exp(1j*data["P1_sam"]),          
        "H_ref" : np.conj(np.fft.rfft(data["sig1_ref"], 2 * len(data["f_sam"]) - 1))                    # Samplingen er foretaget til de negative frekvenser, for et reelt signal er de positive frekvensers fase den konjugerede af de negatives.
    }
    fig, ax = plt.subplots(2, 2, sharex=True)
    
    frekvensResponse(fig, ax, data["f_sam"], Tfs, "Magnitude", "Unwrapped", "dB", "Unormaliseret")

def dfrekvensPhaseplot(data): # ∆|H|*e^{j*(∆p)}
    Tfs = {                                                                                             # Samme frekvens resolution ( 10001 Res )
        "H_sam" : data["A1_sam"] * np.exp(1j*data["P1_sam"]),          
        "H_ref" : np.conj(np.fft.rfft(data["sig1_ref"], 2 * len(data["f_sam"]) - 1) * np.exp(-1j*2*np.pi*data["f_sam"] * data["t0"])) # np.fft.fft(data["sig1_ref"], len(data["f_sam"])) * np.exp(-1j * data["f_sam"] * data["t0"])                    # Samplingen er foretaget til de negative frekvenser, for et reelt signal er de positive frekvensers fase den konjugerede af de negatives.
    }
    # * Jeg har fundet ud af, at den passer godt indtil 4,450 THz, hvor at dæmpningen er på 60dB. 
    P3 = np.angle(Tfs["H_ref"])
    dP = P3 - data["P1_sam"] 
    dM = np.abs(Tfs["H_ref"]) - np.abs(Tfs["H_sam"])
    dH = dM * np.exp(1j * dP)

    # Forskels plot
    fig, ax = plt.subplots(2, 3, sharex= True)
    Tfs[r"$\Delta H$"] = dH
    frekvensResponse(fig, ax, data["f_sam"], Tfs, "Magnitude", "Unwrapped", "dB", "Unormaliseret")

def phaseExtrapolation(data): 
    dangle = phase(Tfs["H_ref"]) - data["P1_sam"] 

    c = constants.speed_of_light
    d = 300e-6
    
    # Setup figure
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(0, 0.1e12)
    ax.set_ylim(-1300, 2500)

    M = 5                       # Antal plots
    
    # Initialization
    def init():
        line.set_data([], [])
        line.set_label("")
        return line,

    # Update
    def update(frame):
        idx = frame // 50       # switch function every 50 frames
        if idx < M:
            m = idx - 2 
            n =  nmaerke(m, data["f_sam"], dangle, c, d)
            line.set_data(data["f_sam"], n)
            line.set_label(rf"$n({m})$")
            ax.legend()    
        return line,

    ani = FuncAnimation(fig, update, frames=50*M, 
                        init_func=init, blit=False, interval=50)
    plt.show()

def phaseExtrapolationBedst(data):
    fig, ax = plt.subplots()
    ax.plot(data["f_sam"], nmaerke(-1, data["f_sam"], dangle, constants.speed_of_light, 300e-6 ))
    plt.show()

def genskabelseAfSpektre(data): 
    w = 2 * np.pi * data["f_sam"]
    w_norm = w * 1e-9   # GHz -> Hz 
    W1 = 0.785 * 1e3 * 2 * np.pi    # THz -> GHz -> Grad/s
    W2 = 1.015 * 1e3 * 2 * np.pi    # THz -> GHz -> Grad/s
    print(min(w_norm), max(w_norm))
    Hjw = np.array([-2.8e-18*np.exp(-1j*i * 1.6185) if i < W1 else 0 for i in w_norm]) + np.array([1.55e-18*np.exp(-1j*i * 1.6189) if i < W2 else 0 for i in w_norm])
    Hjw += 0.001 # Divide by zero fejl
    plots = {
        r"$H(j\omega)$" : Hjw
    }
    fig, ax = plt.subplots(3, 1)
    frekvensResponse(fig, ax, w_norm, plots, "Magnitude", "Fase", "Unwrapped", "Unormaliseret", "dB")    
    
def teoretiskFase(data): 
    fig, ax = plt.subplots()
    w_norm = w * 1e-9 # GHz -> Hz
    dangle = -1j*w_norm * 3.328 
    ax.plot(data["f_sam"], nmaerke(0, data["f_sam"], dangle, constants.speed_of_light, 300e-6 ))
    plt.show()

def tidsplot(data): # f {ifft}-> t 
    # Plot hvor der kompenseres for ifft(x, n) resampler som gør en time scaling på 1/5. 
    n_time = 2*len(data["A1_sam"])
    sig_sam_full = np.fft.irfft(data["A1_sam"] * np.exp(1j*data["P1_sam"]), n_time)
    sig_sam = sig_sam_full[-len(data["t_ref"]):]    # Fjerner 0 paddingsne.
    sig_sam = sig_sam[::-1]                         # Tidsmodsætter den
    
    fig, ax = plt.subplots()
    reference = data["sig1_ref"] * max(sig_sam) / max(data["sig1_ref"])     # Normalisering
    ax.plot(data["t_ref"], reference, label = "Reference") 
    ax.plot(data["t_ref"], sig_sam, label = "Sample") 
    ax.set_title("Normaliserede amplituder")
    fig.legend()
    plt.show()
    
    # Find indeks hvor deres minimummer er. 
    I_ref = np.argmin(reference)
    I_sam = np.argmin(sig_sam)
    h = (data["t_ref"][-1] - data["t_ref"][0])/(len(data["t_ref"])) # t_range / T_samples
    t0_ref = I_ref * h + 1610e-12
    t0_sam = I_sam * h + 1610e-12
    print(t0_sam, t0_ref, t0_sam - t0_ref)

def fase(data): 
    fig, ax = plt.subplots(1, 2, sharex=True)
    P2 = np.unwrap(np.angle(Tfs["H_ref"]))
    
    dangle = P2 - data["P1_sam"]
    wl = 1550e-9    # nm
    nluft = 1
    d = 300e-6      # um
    nmedium = dangle * (wl/(2*np.pi * d)) + nluft
    ax[0].plot(data["f_sam"], data["P1_sam"], label = r"$\phi_{sam}$")
    ax[0].plot(data["f_sam"], P2, label = r"$\phi_{ref}$")
    ax[1].plot(data["f_sam"], nmedium, color = "green", label = rf"$n_{{medium}}, \quad \Delta\phi_{{max}} = {N(max(dangle[:4450]), 4)}$")
    fig.legend()
    plt.show()

# fase(data)

# tidsplot(data)


# Indlæs data
cwd = os.getcwd() 
mappe = os.path.join(cwd, "Øvelser/Data")
sample_path = os.path.join(mappe, 'Si_500middel.pulse.csv')
reference_path = os.path.join(mappe, 'Ref_500middel.pulse.csv') 
headers_sam, sample = læsCSV(sample_path)
headers_sam, reference = læsCSV(reference_path)
data = {
    "t_ref" : reference[:, 0] * 1e-12,      # ps -> s
    "sig1_ref" : reference[:, 1] * 1e-9,    # nA -> A
    "sig2_ref" : reference[:, 2] * 1e-9,    # nA -> A,
    "t_sam" : sample[:, 0] * 1e-12,      # ps -> s
    "sig1_sam" : sample[:, 1] * 1e-9,    # nA -> A
    "sig2_sam" : sample[:, 2] * 1e-9,    # nA -> A,
}
Tfs = {
    "$H(j\omega)_{ref}$" : np.fft.fft(data["sig1_ref"]),
    "$H(j\omega)_{sam}$" : np.fft.fft(data["sig1_sam"])
}

Tfs["$\Delta H(j\omega)$"] = (magnitude(Tfs["$H(j\omega)_{ref}$"]) - magnitude(Tfs["$H(j\omega)_{sam}$"])) * np.exp(phase(Tfs["$H(j\omega)_{ref}$"]) - phase(Tfs["$H(j\omega)_{sam}$"]))
def dFrekvensResponse(Tfs):
    N = len(Tfs["$H(j\omega)_{ref}$"])
    M = int(N/2)
    fig, ax = plt.subplots(3, len(Tfs), sharex=True)
    
    # Kun positive frekvenser. 
    f = np.fft.fftfreq(N)                                   # [-0.5; 0.5]
    # Numpy har negative frekvenser til de største frekvenser men forrest i listen.
    f = f[:M + 1]                                           # [0; 0.5]
    f *= 2 * 10.001                                         # [0; 10.001] [THz]  
    print(len(f))  
    Tfs = {
        "$H(j\omega)_{ref}$" : Tfs["$H(j\omega)_{ref}$"][M:] + 0.0000000000000001,
        "$H(j\omega)_{sam}$" : Tfs["$H(j\omega)_{sam}$"][M:] + 0.0000000000000001,
        "$\Delta H(j\omega)$": Tfs["$\Delta H(j\omega)$"][M:] + 0.0000000000000001
    }
    
    
    for k, v in Tfs.items(): 
        print(len(v))
    frekvensResponse(fig, ax, f, Tfs, "Magnitude", "Fase", "Unwrapped", "dB", "Unormaliseret")
    fig, ax = plt.subplots()
    formatter = EngFormatter(unit='THz', places=0)  # or places=1 for decimals
    ax.xaxis.set_major_formatter(formatter)

dFrekvensResponse(Tfs)