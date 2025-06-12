from Formelsamling.StudieHjaelp import *
from Formelsamling.SignalerOgSystemer import SignalerOgSystemer as SOS
from sympy import * 
import scipy.signal as sig
import scipy.linalg as scialg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Lyd 
import soundcard as sc
import scipy.io.wavfile as wav
import os
import re 
# Hjælpe funktioner
import inspect
import itertools

#?     _______        _______           ___      _____   ____  ____________  ____________    __________  _____   ____
#?    |        \     |        \        /   \       |    __/          |             |        /              |    __/  
#?    |        |     |        |       |     |      | __/             |             |        \              | __/     
#?    |________/     |________/       /-----\      |/\__             |             |         --------      |/\__     
#?    |              |        \      |       |     |   \__           |             |                 \     |   \__   
#?  __|__          __|__       \__  _|_     _|_  __|__  __\__       _|_      ______|_____  __________/   __|__  __\__


# * Nummernavngning 
nummerTilDansk = {  0:                    "nul",   1:                         "en",   2:                         "to",   3:                         "tre",   4:                         "fire",   5:                         "fem",   6:                         "seks",   7:                         "syv",   8:                         "otte",   9:                         "ni",
                   10:                     "ti",  11:                      "eleve",  12:                       "tolv",  13:                     "tretten",  14:                      "fjorten",  15:                      "femten",  16:                      "seksten",  17:                      "sytten",  18:                        "atten",  19:                     "nitten", 
                   20:                   "tyve",  21:                   "enogtyve",  22:                   "toogtyve",  23:                   "treogtyve",  24:                   "fireogtyve",  25:                   "femogtyve",  26:                   "seksogtyve",  27:                   "syvogtyve",  28:                   "otteogtyve",  29:                   "niogtyve",
                   30:                "tredive",  31:                "enogtredive",  32:                "toogtredive",  33:                "treogtredive",  34:                "fireogtredive",  35:                "femogtredive",  36:                "seksogtredive",  37:                "syvogtredive",  38:                "otteogtredive",  39:                "niogtredive",
                   40:                  "fyrre",  41:                  "enogfyrre",  42:                  "toogfyrre",  43:                  "treogfyrre",  44:                  "fireogfyrre",  45:                  "femogfyrre",  46:                  "seksogfyrre",  47:                  "syvogfyrre",  48:                  "otteogfyrre",  49:                  "niogfyrre",
                   50:              "halvtreds",  51:              "enoghalvtreds",  52:              "tooghalvtreds",  53:              "treoghalvtreds",  54:              "fireoghalvtreds",  55:              "femoghalvtreds",  56:              "seksoghalvtreds",  57:              "syvoghalvtreds",  58:              "otteoghalvtreds",  59:              "nioghalvtreds",
                   60:                   "tres",  61:                   "enogtres",  62:                   "toogtres",  63:                   "treogtres",  64:                   "fireogtres",  65:                   "femogtres",  66:                   "seksogtres",  67:                   "syvogtres",  68:                   "otteogtres",  69:                   "niogtres",
                   70:             "halvfjerds",  71:             "enoghalvfjerds",  72:             "tooghalvfjerds",  73:             "treoghalvfjerds",  74:             "fireoghalvfjerds",  75:             "femoghalvfjerds",  76:             "seksoghalvfjerds",  77:             "syvoghalvfjerds",  78:             "otteoghalvfjerds",  79:             "nioghalvfjerds",
                   80:                   "firs",  81:                   "enogfirs",  82:                   "toogfirs",  83:                   "treogfirs",  84:                   "fireogfirs",  85:                   "femogfirs",  86:                   "seksogfirs",  87:                   "syvogfirs",  88:                   "otteogfirs",  89:                   "niogfirs",
                   90:               "halvfems",  91:               "enoghalvfems",  92:               "tooghalvfems",  93:               "treoghalvfems",  94:               "fireoghalvfems",  95:               "femoghalvfems",  96:               "seksoghalvfems",  97:               "syvoghalvfems",  98:               "otteoghalvfems",  99:               "nioghalvfems",
                  100:               "hundrede", 101:             "ethundredeogen", 102:             "ethundredeogto", 103:             "ethundredeogtre", 104:             "ethundredeogfire", 105:             "ethundredeogfem", 106:             "ethundredeogseks", 107:             "ethundredeogsyv", 108:             "ethundredeogotte", 109:             "ethundredeogni",
                  110:         "ethundredeogti", 111:           "ethundredeogelve", 112:           "ethundredeogtolv", 113:         "ethundredeogtretten", 114:          "ethundredeogfjorten", 115:          "ethundredeogfemten", 116:          "ethundredeogseksten", 117:          "ethundredeogsytten", 118:            "ethundredeogatten", 119:         "ethundredeognitten",
                  120:       "ethundredeogtyve", 121:       "ethundredeogenogtyve", 122:       "ethundredeogtoogtyve", 123:       "ethundredeogtreogtyve", 124:       "ethundredeogfireogtyve", 125:       "ethundredeogfemogtyve", 126:       "ethundredeogseksogtyve", 127:       "ethundredeogsyvogtyve", 128:       "ethundredeogotteogtyve", 129:       "ethundredeogniogtyve",
                  130:    "ethundredeogtredive", 131:    "ethundredeogenogtredive", 132:    "ethundredeogtoogtredive", 133:    "ethundredeogtreogtredive", 134:    "ethundredeogfireogtredive", 135:    "ethundredeogfemogtredive", 136:    "ethundredeogseksogtredive", 137:    "ethundredeogsyvogtredive", 138:    "ethundredeogotteogtredive", 139:    "ethundredeogniogtredive",
                  140:      "ethundredeogfyrre", 141:      "ethundredeogenogfyrre", 142:      "ethundredeogtoogfyrre", 143:      "ethundredeogtreogfyrre", 144:      "ethundredeogfireogfyrre", 145:      "ethundredeogfemogfyrre", 146:      "ethundredeogseksogfyrre", 147:      "ethundredeogsyvogfyrre", 148:      "ethundredeogotteogfyrre", 149:      "ethundredeogniogfyrre",
                  150:  "ethundredeoghalvtreds", 151:  "ethundredeogenoghalvtreds", 152:  "ethundredeogtooghalvtreds", 153:  "ethundredeogtreoghalvtreds", 154:  "ethundredeogfireoghalvtreds", 155:  "ethundredeogfemoghalvtreds", 156:  "ethundredeogseksoghalvtreds", 157:  "ethundredeogsyvoghalvtreds", 158:  "ethundredeogotteoghalvtreds", 159:  "ethundredeognioghalvtreds",
                  160:       "ethundredeogtres", 161:       "ethundredeogenogtres", 162:       "ethundredeogtoogtres", 163:       "ethundredeogtreogtres", 164:       "ethundredeogfireogtres", 165:       "ethundredeogfemogtres", 166:       "ethundredeogseksogtres", 167:       "ethundredeogsyvogtres", 168:       "ethundredeogotteogtres", 169:       "ethundredeogniogtres",
                  170: "ethundredeoghalvfjerds", 171: "ethundredeogenoghalvfjerds", 172: "ethundredeogtooghalvfjerds", 173: "ethundredeogtreoghalvfjerds", 174: "ethundredeogfireoghalvfjerds", 175: "ethundredeogfemoghalvfjerds", 176: "ethundredeogseksoghalvfjerds", 177: "ethundredeogsyvoghalvfjerds", 178: "ethundredeogotteoghalvfjerds", 179: "ethundredeognioghalvfjerds", 
                  180:       "ethundredeogfirs", 181:       "ethundredeogenogfirs", 182:       "ethundredeogtoogfirs", 183:       "ethundredeogtreogfirs", 184:       "ethundredeogfireogfirs", 185:       "ethundredeogfemogfirs", 186:       "ethundredeogseksogfirs", 187:       "ethundredeogsyvogfirs", 188:       "ethundredeogotteogfirs", 189:       "ethundredeogniogfirs",
                  190:   "ethundredeoghalvfems", 191:   "ethundredeogenoghalvfems", 192:   "ethundredeogtooghalvfems", 193:   "ethundredeogtreoghalvfems", 194:   "ethundredeogfireoghalvfems", 195:   "ethundredeogfemoghalvfems", 196:   "ethundredeogseksoghalvfems", 197:   "ethundredeogsyvoghalvfems", 198:   "ethundredeogotteoghalvfems", 199:   "ethundredeognioghalvfems"
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


class DualToneMultiFrequencyDTMF(): 
    """
    Alt funktionalitet for at encrypte karakterer som frekvenser \n
    og også til at decrypte karaktererne igen fra deres frekvenser.\n
    
    Variabler
    -----------------
    - lyd:                  Lyd i samples.
    - frekvensFunktioner:   Frekvensspektre af tonerne.
    - toner:                Karaktererne fundet efter decryption
    
    Funktioner
    -----------------
    - genererlyd(sekvens, T_tone): Tager frekvenser, tid per tone og sampling frequency og laver lyd ud af det. 
    - afspilLyd(): Er en hjælpefunktion der tager lydlisten og afspiller den. 
    - dekomponerToner(N_toner): Tager lyd og antallet af toner, inddeller det i hver sin tone og laver frekvenspektrum på det.
    - afkodToner(): Tager frekvensFunktioner lavet af dekomponerToner, analysere tonerne og returnere toner der passer bedst til frekvenserne.                
    
    Kode eksempel: 
    -----------------                 
    fs = 8000 \\                                               
    dtmf = DualToneMultiFrequencyDTMF(fs)\\                 
    sekvens = "112213*#" \\                                  
    T_tone = 0.2  \\                                      
    dtmf.genererLyd(sekvens, T_tone) \\                     
    dtmf.afspilToner() \\                                     
    N_toner = len(sekvens) \\                                 
    dtmf.dekomponerToner(N_toner) \\                           
    dtmf.afkodToner() \\                                      
    print(dtmf.toner)                                           
    """
    
    __konfiguration = {
        "1" : np.array([697, 1209]), 
        "2" : np.array([697, 1336]), 
        "3" : np.array([697, 1477]), 
        "A" : np.array([697, 1633]),
        "4" : np.array([770, 1209]),
        "5" : np.array([770, 1336]),
        "6" : np.array([770, 1477]),
        "B" : np.array([770, 1633]),
        "7" : np.array([852, 1209]),
        "8" : np.array([852, 1336]),
        "9" : np.array([852, 1477]),
        "C" : np.array([852, 1633]),
        "*" : np.array([941, 1209]),
        "0" : np.array([941, 1336]),
        "#" : np.array([941, 1477]),
        "D" : np.array([941, 1633])        
    }
    
    #?  Hjælpe funktioner
    def afspilToner(self):
        default_speaker = sc.default_speaker()
        default_speaker.play(self.lyd, self.fs)
    
    # * Håndtering 
    def genererLyd(self, sekvens, T_tone):                                  # Generer lyd ud fra indtastede værdier.
        """
        DMTF.lyd = list(N_samples)
        """
        fs = self.fs
        def genererToner(frekvenser): 
            Ts = 1/fs
            n = np.arange(0, T_tone, Ts).reshape(-1, 1)                     # Pulse of half a second given the sampling frequency
            signals = np.hstack([np.sin(2*np.pi*frekvenser[0] * n), np.sin(2*np.pi*frekvenser[1] * n)])
            return signals
        
        def samlLyd(signaler):
            lyd = signaler[:, 0] + signaler[:, 1] 
            return lyd
        lyd = np.zeros((0, 1))
        for bogstav in list(sekvens.upper()): 
            frekvenser = self.__konfiguration[bogstav]
            signaler = genererToner(frekvenser)
            samlet = samlLyd(signaler).reshape(-1, 1)
            lyd = np.vstack([lyd, 
                             samlet])
        self.lyd = lyd
    
    def dekomponerToner(self, N_toner):                                     # Splitter lyd i N_toner.
        """
        Dekomponere ud fra længden af lyden og antallet af toner. \\
        Returnere frekvensfunktioner svarende til antallet af toner.\n
        DMTF.frekvensFunktioner = list(SamplesPrTone, N_toner)
        """
        lyd = self.lyd
        def splitListe() -> np.array(["Toner"]): 
            N = lyd.shape[0]
            samplesPrTone =int(N/N_toner)
            symboler = np.split(lyd, np.arange(samplesPrTone, N, samplesPrTone))
            symboler = symboler[:N_toner]                   # Smider uønskede splits ud
            return symboler
        def frekvensTransformation(tone) -> list("1, N"):
            """
            Skal transformere tonen. \\
            Det er meningen at jeg kan vælge hvilken måde jeg skal transformere det på.
            """
            
            def fastFourier(tone):
                """
                Fast fourier metoden er bare en standard fourier transformation. \\ 
                X bliver analyseret til alle frekvenser, og de bidrag er dem som signalet er bygget op af.
                """
                # En vektor med formen (N, 1) laver en helt forkert fourier analyse. 
                # Vektoren skal være (1, N)
                tone = tone.reshape(1, -1)
                lyd_fft = np.fft.fft(tone)                                      #   0; 2pi            
                lyd_fft = np.fft.fftshift(lyd_fft)                              # -pi;  pi
                
                return lyd_fft 
            def GoertzelsFT(tone): 
                """
                GoertzelsFT metoden tager diskrete og valgte frekvenser \\
                og de X'er som er største til disse, må være dem som mit signal er lavet med. 
                De udvalgte frekvenser er de 8 fra en 16 karakters DTMF
                """
                N = len(tone)
                frekvenser = np.array([697, 770, 852, 941, 1209, 1336, 1477, 1633])
                K = len(frekvenser)
                k = frekvenser * N / self.fs
                k = np.int64(k)
                X = GoertzelsFourierTransform(tone, k).reshape(1, -1) # (1, maks(k))                
                k = np.argsort(np.abs(X), axis = 1)
                
                # X ser ud til at tage værdier for mange frekvenser.
                # Jeg kan ikke se et mønster. Måske er min transformation forkert sat op
                # 
                k = k[0, -10:] 
                f = k * self.fs / N # f ≠ frekvenser
                return X
            return fastFourier(tone)
        
        def dataHåndtering(toner) -> list("N, N_toner"):                    # Laver output til liste af frekvensfunktioner
            """
            Frekvens funktion for hver tone, ellers er der mange "spøgelses"
            frekvenser som kompensere for skiftene.
            """
            frekvensFunktioner = np.vstack([frekvensTransformation(tone) for tone in toner])
            frekvensFunktioner = frekvensFunktioner.T
            return frekvensFunktioner

        toner = splitListe()
        frekvensFunktioner = dataHåndtering(toner)
        self.frekvensFunktioner = frekvensFunktioner 
    
    def afkodToner(self) -> "Toner":
        frekvensFunktioner = self.frekvensFunktioner
        samplesPrTone, N_toner = frekvensFunktioner.shape
        w = np.linspace(-1, 1, samplesPrTone)
        w *= self.fs                                            # Tilbage til unormaliserede frekvenser
        w *= 1/2                                                # Jeg ser, at frekvenserne har en faktor på sig.
        
        def findFrekvenser(frekvensFunktion) -> None:           # Hjælpefunktion til fjerne spike i DC 
            # 4 Største værdier -> absolutte værdier -> Kun unikke -> 2 frekvenser.
            i_maks = np.argsort(np.abs(frekvensFunktion)) # min -> max
            frekvenser = np.round(w[i_maks[-4:]], 0)
            frekvenser = np.abs(frekvenser)
            frekvenser = np.unique(frekvenser)
            def adskilUdFraGrænseværdier(grænseværdi, frekvenser):# Funktion til frekvenser tætte på hinanden. 
                """
                Funktion til at fjerne frekvenser
                som er mindre en grænseværdien fra hinanden
                """
                frekvenser = np.sort(frekvenser)
                f = np.array([0])
                for frekvens in frekvenser: 
                    #                               (667 - 660) < 10
                    if frekvens not in f and np.abs(frekvens - f[-1]) > grænseværdi:
                        f = np.append(f, frekvens)
                return f[1:]
            frekvenser = adskilUdFraGrænseværdier(10, frekvenser)
            return frekvenser  
        def fjernDC(frekvensFunktion) -> None:                  # Hjælpefunktion til fjerne spike i DC
            i_maks = np.argsort(frekvensFunktion)
            frekvensFunktion[i_maks[-1]] *= 0                           # Fjern største værdi  
        def bearbejdFrekvenser(frekvensFunktion) -> "Tone, f":  # Funktion som bearbejder data og finder tonen. 
            F = frekvensFunktion 
            fjernDC(F)                                                  # Spike i DC 
            f = findFrekvenser(F)
            # Pythagoras: min(√(førsat frekvens - frekvens)^2) -> Afkodet tone
            tone = min(self.__konfiguration, key=lambda k: np.linalg.norm(self.__konfiguration[k] - f))
            return (tone, f) 
        def analyser() -> list("Toner"):                        # Funktion til at afkode men også til visuelt at analysere det
            toner = []
            for tone in range(0, N_toner, 2): 
                # Analysere 2 toner af gangen.             
                frekvenser1 = frekvensFunktioner[:, tone]
                frekvenser2 = frekvensFunktioner[:, tone + 1]
                tone1, f1s = bearbejdFrekvenser(frekvenser1)
                tone2, f2s = bearbejdFrekvenser(frekvenser2)
                toner += [tone1, tone2]
                
                # Plot
                frekvenser = {
                    f"Tone {tone}": frekvenser1, 
                    f"Tone {tone + 1}" : frekvenser2
                }
                fig, ax = plt.subplots(1, 2, sharex= True)
                # w * 2 pi siden, at min funktion normalisere for 2 * pi.
                fig, ax = frekvensResponseTo(fig, ax, w * 2*np.pi, frekvenser, "Magnitude")     
            return toner
        def afkod() -> list("Toner"):                           # Funktion til at afkode       
            toner = []
            for tone in range(0, N_toner, 2): 
                # Analysere 2 toner af gangen. 
                frekvenser1 = frekvensFunktioner[:, tone]
                frekvenser2 = frekvensFunktioner[:, tone + 1]
                tone1, f1s = bearbejdFrekvenser(frekvenser1)
                tone2, f2s = bearbejdFrekvenser(frekvenser2)
                toner += [tone1, tone2]
            return toner
        toner = analyser()
        self.toner = toner   
         
    def __init__(self, fs, lyd = None):
        self.fs = fs
        if lyd is not None:
            self.lyd = lyd

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
    
def frekvensResponseTo(fig = None, ax = None, w = None, frekvensFunktioner = None, *args, **kwargs) -> Tuple:
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
                vinkel = np.rad2deg(np.angle(H))
                ax.plot(w, vinkel, **kwargs)
            case "Unwrapped": 
                vinkel = np.rad2deg(np.angle(H))
                ax.plot(w, np.unwrap(vinkel), **kwargs)
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
    
#?  _____   ____    _______     _____    _____   __________  ____________    _______     ___      ___     _______           ___      ____________  ____________    _______     _____    _____   __________     _______     
#?    |    __/     /       \     |  \      |    |                  |        /             |        |    |        \        /   \           |             |        /       \     |  \      |    |              |        \   
#?    | __/       |         |    |   \     |    |                  |       |              |        |    |        |       |     |          |             |       |         |    |   \     |    |              |        |   
#?    |/\__       |         |    |    \    |    |------            |       |      ____    |        |    |________/       /-----\          |             |       |         |    |    \    |    |------        |________/   
#?    |   \__     |         |    |     \   |    |                  |       |          |   |        |    |        \      |       |         |             |       |         |    |     \   |    |              |        \   
#?  __|__  __\__   \_______/   __|__    \__|    |            ______|_____   \________/     \______/   __|__       \__  _|_     _|_       _|_      ______|_____   \_______/   __|__    \__|    |__________  __|__       \__

plt.rcParams['figure.subplot.left']   = 0.06
plt.rcParams['figure.subplot.bottom'] = 0.08
plt.rcParams['figure.subplot.right']  = 0.955
plt.rcParams['figure.subplot.top']    = 0.955
plt.rcParams['figure.subplot.wspace'] = 0.10
plt.rcParams['figure.subplot.hspace'] = 0.10




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
            r"$H(e^{j\omega})$" : self.H, 
        }
        fig, ax = plt.subplots(3, 1,sharex= True)
        # frekvensResponse(fig, ax, self.w, frekvensFunktioner)
        
        # Læring. Jeg skal ikke lave en omega som er 2 * pi * f, når f: [-1, 1]
        # Da ville jeg få w = [-2pi; 2*pi]. Og [-2pi; 0] er det samme som [0; 2pi]. 
        # Når jeg så lavede normalisering af mine frekvenser, så manglede mit filter en faktor 2. 
        
        fig, ax = plt.subplots()
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude")
        # gemBillede("Opgave 5.38.b.png", fig)
        fig, ax = plt.subplots(2, 1, sharex= True)
        frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Unwrapped", "Gruppedelay")
        # gemBillede("Opgave 5.38.c.png", fig)

class Opgave5_39(Opgave): 
    def faaWZ(self): 
        f = np.linspace(-1, 1, 500)
        w = np.pi*f
        z = np.exp(1j*w)
        return w, z
        
    def opga(self): 
        w, z = self.faaZ()
        H = (1 - 0.589*(z**(-1)) + 0.9025*(z**(-2)))
        resultal_b0 = 1/np.max(np.abs(H))
        H *= resultal_b0
        fig, ax = plt.subplots()
        frekvensFunktioner = {
            r"$H(e^{j\omega})$": self.H
        }
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude", "dB")
        # gemBillede("Opgave 5.39.a.png", fig)
    
    def opgb(self): 
        w, z = self.faaZ()
        H2 = (1 - 0.62*(z**(-1)) + z**(-2))
        resultat_b02 = 1/np.max(np.abs(H2))
        H2 *= resultat_b02
        frekvensFunktioner = {
            r"$H_2(e^{j\omega})$": self.H2
        }
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude", "dB")
        # gemBillede("Opgave 5.39.b.png", fig)

    def opgc(self):
        w, z = self.faaWZ()
        H3 = np.ones_like(z.shape, dtype=float)
        for k in range(-1, 2): 
            print(k)
            theta_k = (1 + 0.05*k) * 2 * np.pi/5 
            H3 = H3 * 1 - (2*np.cos(theta_k)*(z**(-1)) + z**(-2))
        
        resultat_b03 = 1/np.max(np.abs(H3))
        H3 *= resultat_b03
        frekvensFunktioner = {
            r"$H_3(e^{j\omega})$": H3
        }
        fig, ax = plt.subplots()
        fig, ax = frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Magnitude", "dB")
        # gemBillede("Opgave 5.39.c.png", fig)
    
    def opgd(self):
        w, z = self.faaWZ()
        H4 = np.ones_like(z.shape, dtype=float)
        for k in range(-2, 3): 
            print(k)
            theta_k = (1 + 0.05*k) * 2 * np.pi/5 
            H4 = H4 * 1 - (2*np.cos(theta_k)*(z**(-1)) + z**(-2))
        frekvensFunktioner = {
            r"$H_4(e^{j\omega})$": H4
        }
        fig, ax = plt.subplots()
        fig, ax = frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Magnitude", "dB")
        # gemBillede("Opgave 5.39.d.png", fig)
            
    def __init__(self):
        self.opgd() 
               
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
        
class Opgave5_55(Opgave): 
    
    
    def systemer(self, system, z):
        match system:
            case "a": 
                b = [1, 0, -1]
                a = [1, 0, -0.81]
                H = (1 - z**(-2))/(1 - 0.81*(z**(-2)))
                return (b, a, H)
            case "b": 
                b = [1, 0, 0, 0, -1]
                a = [1, 0, 0, 0, -0.6561]
                H = (1 - z**(-4))/(1 - 0.6561*(z**(-4)))
                return (b, a, H) 
            case "c": 
                b = [1, 0, 0, 0, -1]
                a = [1, 0, 0, 0, 0.6561]
                H = (1 - z**(-4))/(1 + 0.6561*(z**(-4)))
                return (b, a, H) 
            case "d": 
                b = [1, -1]
                a = [1, -0.99, 0.9801]
                H = (1 - z**(-1))/(1 -0.99*(z**(-1)) + 0.9801*(z**(-2)))
                return (b, a, H)
            case default: 
                ""  
    
    def analyser(self, system): 
        f = np.linspace(-1, 1, 500)
        w = np.pi*f
        z = np.exp(1j*w)
        b, a, H = self.systemer(system, z)
        fig, ax = plt.subplots(2, 1, sharex=True)
        ax = ax.reshape(-1, 1)
        print(ax.shape)
        frekvensFunktioner = {
            r"$H(e^{j\omega})$" : H 
        }
        print(frekvensFunktioner)
        frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Magnitude", "Fase")
        SOS.pzplotZ(b, a, "ydre")

    def __init__(self):
        self.analyser("a")
        self.analyser("b")
        self.analyser("c")
        self.analyser("d")
        
class Opgave6_2(Opgave): 
    # Plot af samplet spektrum. 
    N = 300
    Fs = 100
    F = np.linspace(-150, 150, N)
    w = 2 * np.pi * F 
    
    
    def shift(self, X, w, w_0): 
        """
        Positiv w0 betyder venstre shift
        Negativ w0 betyder højre shift.
        """
        wRange = np.max(w) - np.min(w)
        wLen = w.shape[0]
        wIncrease = wRange/wLen
        padLen = np.abs(round(w_0/wIncrease))
        origo = np.argmin(np.abs(w))
        nyW = w
        if w_0 >= 0: 
            nyW = np.pad(w[padLen: ], (0, padLen))
            nyX = np.pad(X[padLen: ], (0, padLen))
            return (nyW, nyX)
        else: 
            nyW = np.pad(w[: wLen - padLen], (padLen, 0))
            nyX = np.pad(X[: wLen - padLen], (padLen, 0))
            return (nyW, nyX)
            
            
    z = np.exp(1j*w)
    X = 100/(100 + w**2)
    def opga(self): 
        # For Fs = 100Hz
        _, X1 = self.shift(self.X, self.w, -100*2*np.pi)
        _, X2 = self.shift(self.X, self.w, 100*2*np.pi)
        Xejw = self.X + X1 + X2 
        fig, ax = plt.subplots(2, 2, sharex = True) 
    
        frekvensFunktioner = {
            r"$X(j\omega)$" : self.X, 
            r"$X(e^{j\omega})$" : Xejw
        }
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude", "Fase") 
        gemBillede("Opgave 6.2.a.png", fig)
    
    def opgb(self): 
        # For Fs = 50Hz  
        _, X1 = self.shift(self.X, self.w, -150*2*np.pi)
        _, X2 = self.shift(self.X, self.w, -100*2*np.pi)
        _, X3 = self.shift(self.X, self.w, -50*2*np.pi)
        _, X4 = self.shift(self.X, self.w, 50*2*np.pi)    
        _, X5 = self.shift(self.X, self.w, 100*2*np.pi)    
        _, X6 = self.shift(self.X, self.w, 150*2*np.pi)    
        Xejw = self.X + X1 + X2 + X3 + X4 + X5 + X6
        fig, ax = plt.subplots(2, sharex = True) 
        ax = ax.reshape(1, -1)
        frekvensFunktioner = {
            r"$X(j\omega)$" : self.X, 
            r"$X(e^{j\omega})$" : Xejw
        }
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude") 
        gemBillede("Opgave 6.2.b.png", fig)
        
    def opgc(self): 
        # For Fs = 25Hz
        Xejw = self.X
        for i in range(-150, 151, 25): 
            if i == 0: continue
            _, Xejw = Xejw + self.shift(self.X, self.w, i*2*np.pi)
        fig, ax = plt.subplots(2, sharex = True) 
        ax = ax.reshape(1, -1)
        # print(ax.shape)
        frekvensFunktioner = {
            r"$X(j\omega)$" : self.X, 
            r"$X(e^{j\omega})$" : Xejw
        }
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude") 
        gemBillede("Opgave 6.2.c.png", fig)
        
    def __init__(self): 
        self.opgc()

class Opgave6_12(Opgave): 
    w0 = 25 * np.pi/(2**8)
    w1 = 125 * np.pi/(2**9)
    N = 200                         # Resolution i spektret
    w, h = np.linspace(0, 2*np.pi, N, retstep = True)
    
    F_s = 2**11
    T_s = 1/(F_s)
    
    
    # --- Kreer diskrete spektrum.
    def findIndices(w, w0, w1): 
        # Suppose w is your frequency array
        I = []
        I += [np.where(w <= w0)[0].max()]
        I += [np.where(w <= w1)[0].max()]
        I += [np.where(w <= 2*np.pi - w1)[0].max()]
        I += [np.where(w <= 2*np.pi - w0)[0].max()]
        return I
    
    # En periode
    I = findIndices(w, w0, w1)
    X = np.zeros_like(w, dtype = complex)
    X[I[0]] += 2 * np.pi 
    X[I[1]] += 3 * np.pi/(1j)
    X[I[2]] += -3 * np.pi/(1j)
    X[I[3]] += 2 * np.pi
    
    def diskreteSpektrum(self, X): 
        N = self.N
        N_perioder = 2
        X_gentaget = np.tile(X, N_perioder)
        X_gentaget = np.hstack([X_gentaget, X_gentaget])
        w_gentaget = np.linspace(- N_perioder * 2 * np.pi, N_perioder * 2 * np.pi, N*N_perioder * 2)
        self.N = N * 6 
        return (X_gentaget, w_gentaget)
    
    # --- Sample and Hold    
    def sampleAndHold(self, Xejw, w_gentaget):
        F_s = self.F_s
        T_s = self.T_s
        w_kontinuert = w_gentaget * F_s         # Tilbage til kontinuert frekvenser
        G_sh = (2 * np.sin(w_kontinuert * T_s/2)/w_kontinuert) * np.exp(-1j*w_kontinuert*T_s/2)
        X_sh = Xejw * G_sh
        return X_sh, G_sh, w_kontinuert
    
    # --- Lavpass filtrering    
    def lavPassFiltrering(self, X, w_gentaget):
        F_s = self.F_s
        T_s = self.T_s
        H_LP = (w_gentaget * T_s/2)/(np.sin(w_gentaget * T_s/2)) * np.exp(1j*w_gentaget*T_s/2)
        I = np.where(np.abs(w_gentaget) >= np.pi*F_s) 
        H_LP[I] *= 0                            # 0 otherwise    
        X_r = X * H_LP
        return X_r, H_LP
    def rekonstruktion(self, w, X):
        I = np.nonzero(X)
        I = I[0]
        
        pprint(
        f""" 
        Frequenc komponenter: 
        =============================== 
        
        X_0 = {N(X[I[0]], 2)} ved w = {w[I[0]]},
        X_1 = {N(X[I[1]], 2)} ved w = {w[I[1]]}
        X_2 = {N(X[I[2]], 2)} ved w = {w[I[2]]}
        X_3 = {N(X[I[3]], 2)} ved w = {w[I[3]]}
        
        ===============================
        """
        )
        t = np.linspace(0, 0.10, 205)
        x_ind = 2 * np.cos(200*np.pi * t) + 3 * np.sin(500 * np.pi * t)
        x_ud = (0.0031/np.pi) * np.cos(644 * t) - (0.0046/np.pi) * np.sin(1610 * t)
        fig, ax = plt.subplots(2)
        ax[0].plot(t, x_ind, label= "Input")
        ax[0].plot(t, x_ud, label= "Output")
        ax[1].plot(t, x_ud, color = "orange")
        ax[0].grid()
        ax[1].grid()
        fig.legend()
        plt.show()
        return (fig, ax)
         
        
    
    def __init__(self): 
        Xejw, w_gentaget = self.diskreteSpektrum(self.X)
        X_sh, G_sh, w_kont = self.sampleAndHold(Xejw, w_gentaget)
        X_r, H_LP = self.lavPassFiltrering(X_sh, w_kont) 
        
        fig, ax = plt.subplots(2, 5, sharex= True)
        frekvensFunktioner = {
            r"$X(e^{j\omega})$" : Xejw, 
            r"$G_{sh}(j\omega)$" : G_sh,
            r"$X_{sh}(e^{j\omega})$" : X_sh, 
            r"$H_{lp}(j\omega)$" : H_LP, 
            r"$X_r(j\omega)$" : X_r
        }
        # fig, ax = frekvensResponseTo(fig, ax, w_kont, frekvensFunktioner, "Magnitude", "Fase", "Unormaliseret")
        # gemBillede("Opgave 6.12.png", fig)
        fig, ax = self.rekonstruktion(w_kont, X_r)
        # gemBillede("Opgave 6.12.Rekonstruering.png", fig)
        
class Opgave7_1(Opgave): 
    N = 100
    F = np.linspace(-50, 50, N)
    w = 2*np.pi*F
    Xc = (5/(4*np.pi*1j)) * (1/(10 + 1j*(w - 20*np.pi)) - 1/(10 + 1j*(w + 20*np.pi)))
    
    def opgb(self): # Plot
        frekvensFunktioner = {
            r"$X_c(j\omega)$" : self.Xc
        }
        fig, ax = plt.subplots(2, 1)
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude", "Fase", "Unormaliseret")
        gemBillede("Opgave 7.1.png", fig)
    
    def opgc(self): 
        Fs = 100
        Ts = 1/Fs 
        T = 0.5
        t = np.arange(0, 2*T, Ts)
        xc = 5 * np.exp(-10*t)*np.sin(20 * np.pi * t)
        I = np.where(t < 0)
        xc[I] *= 0
        
        # Tjek - Er funktionen som den skal være? 
        def tjek(): 
            plots = {
                r"$x_c(t)$" : xc
            }
            fig, ax = plt.subplots()
            diskretePlotAfFunktioner(fig, ax, t, plots)
        # tjek()
        
        # FFT 
        Xc = np.fft.fft(xc)
        Xc = np.fft.fftshift(Xc)
        # Jeg ganger med Fs for at komme tilbage til kontinuert tid og jeg ganger med 2 da
        # numpy normalisere altid diskrete frekvenser fra 0 -> 1, men jeg plejer at normalisere det til antal pi.
        
        frekvensFunktioner = {
            r"$X_c(j\omega)_{beregnet}$"  : self.Xc,
            r"$X_c(j\omega)_{fft}$"       : Xc
        }
        fig, ax = plt.subplots(2, 2, sharex = True)
        fig, ax = frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude", "Fase", "Unormaliseret")        
        gemBillede("Opgave 7.1.c.png", fig)
        
    def __init__(self):
        # self.opgb()
        self.opgc()

class Opgave7_3(Opgave): 
    
    plotnavne = np.array(["Opgave 7.3.b.png", "Opgave 7.3.c.png", "Opgave 7.3.d.png"])
    N_resolution = np.array([20, 50, 100])
    
    def plots(self): 
        # opgave b, c og d har samme process men resolutionen forbedres for hver opgave.
        for navn, N in zip(self.plotnavne, self.N_resolution): 
            n = np.arange(N)
            xn = n * ((0.9)**n)
            X_N = np.fft.fft(xn)
            X_N = np.fft.fftshift(X_N)
            w = np.linspace(-np.pi, np.pi, N)
            Xejw = (0.9 * np.exp(-1j*w))/((1 - 0.9*np.exp(-1j*w)) ** 2)
            w *= 2 # 2 så det passer med min måde at normalisere det på. 
            frekvensFunktioner = {
                r"$X_{beregnet}(e^{j\omega})$"    : Xejw,
                r"$X_{FFT}(e^{j\omega})$"         : X_N
            }
            fig, ax = plt.subplots(2, 2, sharex= True, figsize = (16, 7.75))
            fig, ax = frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Magnitude", "Fase")
            # gemBillede(navn, fig)
            
    
    def __init__(self): 
        self.plots()
        
class Opgave7_4(Opgave): 
    def opgc(self): 
        
        for N_antal in range(4, 11): 
            W_N = dftmtx(N_antal)
            egenværdier = np.linalg.eigvals(W_N * 1/(np.sqrt(N_antal)))
            egenværdier = np.round(egenværdier, 3)
            pprint(egenværdier) 

    def __init__(self): 
        self.opgc()

class Opgave7_5(Opgave): 
    funktioner = {
        "a" : lambda n : 4 - n, 
        "b" : lambda n : 4 * np.sin(0.2 * np.pi * n), 
        "c" : lambda n : 6 * (np.cos(0.2 * np.pi * n)**2), 
        "d" : lambda n : 5 * ((0.8)**n), 
        "e" : lambda n : np.array([3 if i % 2 == 0 else -2 for i in range(len(n))])
    }
    
    DFT_transformation = lambda x, N : dftmtx(N) @ x 
    
    def DFT_transformationer(self): 
        n = lambda N :np.arange(N)
        N = [8, 10, 10, 16, 20]
        X = {}
        
        for i, (opgave, funktion) in enumerate(self.funktioner.items()):
            X[fr"$X_{opgave}(e^{{j\omega}})$"] = np.pad(dftmtx(N[i]) @ funktion(n(N[i])), (0, 20 - N[i]))
        
        w = np.linspace(-np.pi, np.pi, 20)
        fig, ax = plt.subplots(2, 5, sharex=True)
        frekvensResponseTo(fig, ax, w, X, "Magnitude", "Fase")
        # gemBillede("Opgave 7.5.png", fig)
        
    def __init__(self): 
        self.DFT_transformationer()
        ""

class Opgave8_48(Opgave):          
    # ? Opgaver
    def opga_c(self):    
        fs = self.fs    
        # Sekvens: 
        sekvens = "13268*#A"
        self.dtmf.genererLyd(sekvens, 0.5)
        
        # Afspil
        self.dtmf.afspilToner()        
        
        # Frekvensanalyse
        N = len(sekvens)
        SamplesPrTone = int(self.dtmf.lyd.shape[0] / N)
        self.dtmf.dekomponerToner(N)
        plots = {}
        for i in range(self.dtmf.frekvensFunktioner.shape[1]):
            plots[f"Tone {i + 1}"] = self.dtmf.frekvensFunktioner[:, i]
        fig, ax = plt.subplots(1, N, sharex= True)
        w = np.linspace(-np.pi, np.pi, SamplesPrTone)
        w *= fs                                             # Tilbage til unormaliserede frekvenser
        fig, ax = frekvensResponseTo(fig, ax, w, plots, "Magnitude")
        # gemBillede("Opgave 8.48.png", fig)
          
    def opge(self):
        """
        Afkod egen fil og ellers test på wav fil fra internettet
        """ 
        # Test af lyd jeg selv skaber
        # Sekvens: 
        fs = self.fs
        sekvens = "13268*#A"
        self.dtmf.genererLyd(sekvens, 0.2)
        
        # Afspil
        self.dtmf.afspilToner()        
        
        # Frekvensanalyse
        N = len(sekvens)
        SamplesPrTone = int(self.dtmf.lyd.shape[0] / N)
        frekvensFunktioner = self.dtmf.dekomponerToner(N)
        self.dtmf.afkodToner()
        toner = ''.join(self.dtmf.toner)
        
        # Test af lydfil fundet på nettet: 
        cwd = os.getcwd()
        dataMappe = cwd + "/Hjælpefiler/Data/"
        navn = "DTMF.wav"
        fil = dataMappe + navn
        fs, lyd = wav.read(fil)
        N = 16
        SamplesPrTone = floor(lyd.shape[0] / N)
        self.dtmf.lyd = lyd
        self.dtmf.dekomponerToner(N)
        self.dtmf.afkodToner()

    def testGoertzelsFT(self): 
        # Test af GoertzelsFT
        N = 10
        K = 6
        xn = np.ones(N)
        xn[:3] *= 0 
        xn[-3:] *= 0        

        # Set up the figure
        fig, ax = plt.subplots()
        line, = ax.plot([], [], 'bo-')
        ax.set_xlim(0, N)
        ax.set_ylim(-10, 40)
        ax.set_title("Goertzel Output for each DFT bin")
        ax.set_xlabel("Frequency bin (k)")
        ax.set_ylabel("|X[k]| [dB]")

        # Update function
        def update(frame):
            K = frame
            X = GoertzelsFourierTransform(xn, N, K)
            mag = 20 * np.log10(np.abs(X) + 1e-12)  # Avoid log(0)
            line.set_data(np.arange(K), mag)
            return line,

        # Animate over frames from K = 1 to N
        ani = FuncAnimation(fig, update, frames=N + 1, interval=500, blit=True)
        plt.show()    
    def __init__(self):
        self.fs = 8000
        self.dtmf = DualToneMultiFrequencyDTMF(self.fs)
        # self.opga_c()
        # self.testGoertzelsFT()
        # self.opge()
        
        # Steps for at komme frem og tilbage: 
        fs = 8000
        dtmf = DualToneMultiFrequencyDTMF(fs)
        sekvens = "1234122*"
        dtmf.genererLyd(sekvens, 0.2)
        dtmf.afspilToner()
        N_toner = len(sekvens)
        dtmf.dekomponerToner(N_toner)
        dtmf.afkodToner()
        print(dtmf.toner)

class Opgave_Kapitel9(Opgave): 
    N = 13              # Ordnen af filteret
    # Forskel på stabilitet i direkt filter form og transposed filter for. Eksempel fra slides.
    
    ripple = 0.009 # 1 for y > 0.991, 0 for y < 0.009
    attenuation = 80 # dB. Afstanden mellem stopband og passband. 
    b, a = sig.ellip(N, ripple, attenuation, 0.05 , output='ba')
    sos = sig.ellip(N, ripple, attenuation, 0.05, output='sos')
    x = sig.unit_impulse(700)

    def __init__(self): 
        b, a = (self.b, self.a)
        x = self.x
        sos = self.sos
        y_tf = sig.lfilter(b, a, x)

        y_sos = sig.sosfilt(sos, x)

        plots = {
            "SOS" : y_sos,
            "TF"  : y_tf
        }
        
        N = len(plots)      # Antallet af plots
        fig, ax = plt.subplots(N, 1, sharex = True)
        
        n = np.arange(700)
        
        diskretePlotAfFunktioner(fig, ax, n, plots)
        # Systemet skulle vise, at det normale filter vil have polerne uden for enhedscirklen på grund af numerisk fejl 
        # når filterorden bliver så stor som den er blevet. 
        
        SOS.pzplotZ(b, a) # 4 poler udenfor enhedscirklen

class Opgave9_1(Opgave): 
    b = [0, 7, 1]
    a = [1, -9]
    res_Hz = filterRepræsentation(b, a, Function("H")(symbols("z")))

class Opgave9_3(Opgave): 
    b, a = ([1, -2.55, 4.4, -5.09, 2.41], [1, 0.26, -0.38, 0.45, 0.23])
    resultat_sos = sig.tf2sos(b, a) 
    resultat_tf = sig.sos2tf(resultat_sos)

class Opgave9_4(Opgave): 
    b, a = ([1, 1], [1, -3/2, -9/8])
    # resultat_sos = sig.tf2sos(b, a) 
    resultat_filter = filterRepræsentation(b, a, Function("H")(symbols("z")))

class Opgave9_29(Beregning): 
    sos = np.array([[1, 0.5, 2, 1, -1/4, -3/8],
                    [1,  -2, 1, 1,  1/3, -2/9]])
    resultat_tf = sig.sos2tf(sos)
    
    # Gammel metode, 
    """
    z, n = symbols("z n")
    x = Function("x")(n)
    y = Function("y")(n)
    pprint(x)
    y1 = Matrix([[1, -1, 0.5]]).dot(Matrix([[1, z**(-1), z**(-2)]])) * x
    y2 = Matrix([[1, z**(-1), 4*z**(-2)]]).dot(Matrix([[1, -1/3 * z**(-1), 2/9 * z**(-2)]])) * y1
    y3 = Matrix([[1, -1/4, 3/8]]).dot(Matrix([[1, z**(-1), z**(-2)]])) * y2
    resultat_y3 = Eq(y, N(expand(y3), 3))
    """
    # Nu kun i z domæne.
    z = symbols("z")
    H1 = lambda z : 1 - z**(-1) + 0.5*(z**(-2))
    H2 = lambda z : (1 + z**(-1) + 4*(z**(-2))) / (1 + 2/9*(z**(-1)) - 1/3*(z**(-2)))
    H3 = lambda z : (1) / (1 - 1/4*(z**(-1)) - 3/8*(z**(-2)))
    
    X = Function("X")(z)
    
    Y = H1(z) * H2(z) * H3(z) * X

    resultat_Y = Eq(Function("Y")(z), cancel(Y))

class Opgave_kapitel10_1(Beregning):
    beskrivelse = "Eksempel 10.4 om design af vinduer ud fra den generelle metode, kaiser vinduet"
    def metodeFinding(self): 
        # ? Først test af metoden 
        M = 20
        beta = 8
        kaiser = Vindue_Kaiser()
        wn = kaiser.vindue(M, beta)
        n = np.arange(M + 1)
        fig, ax = plt.subplots()
        wn2 = np.append(sig.windows.kaiser(20, beta, False), 0)
        # diskretePlotAfFunktioner(fig, ax , n, {"w[n]" : wn, "w_2[n]" : wn2})
        # * Sjovt nok så kan man se, at der er forskel. 
        # * Måske er det noget med nogle afrundings fejl. 
        # diskretePlotAfFunktioner(fig, ax , n, {"w_2[n]" : wn2})
        #fig, ax = plt.subplots(2, 2)
        #vinduer = {
        #    r"$w[n]$" : wn, 
        #    r"$w_2[n]$" : wn2
        #}
        # vindueAnalyse(fig, ax, n, vinduer, "Impuls", "Magnitude") 
        # gemBillede("Øvelse 10.4.3.png", fig)
    
    def kaiserVindue(self): 
        M = 74 
        beta = 4.5335
        wn = np.append(sig.windows.kaiser(74, beta, False), 0)
        # vindueAnalyse(fig, ax, n, {r"$w[n]$" : wn}, "Impuls", "Magnitude")
        # gemBillede("Øvelse 10.4.4.png", fig)  
        return wn
    
    def __init__(self): 
        # kaiser vindue: 
        wn = self.kaiserVindue()
        
        # Ideel bandpass:      
        B = 0.49 * np.pi
        W = B/2
        M = 74
        n = np.arange(-floor(M/2), ceiling(M/2) + 1, dtype = float)
        pprint(n.shape)
        h_1 = W/np.pi * np.sinc(W*n/np.pi)
        
        
        omega_0 = 0.495 * np.pi
        # * Forkert opsætning 
        # h_2 = np.exp(-1j*omega_0*n) * h_1
        # fig, ax = plt.subplots()
        # diskretePlotAfFunktioner(fig, ax, n, {r"$h_1[n]$" : h_1, r"$h_2[n]$" : h_2})
        # gemBillede("Øvelse 10.4.5.png", fig)
        # re = 1024
        # H_1 = np.fft.fft(h_1, re)
        # H_1 = np.fft.fftshift(H_1)
        # H_2 = np.fft.fft(h_2, re)
        # H_2 = np.fft.fftshift(H_2)
        # fig, ax = plt.subplots(3, 2, sharex = True)
        # frekvensFunktioner = {
        #     r"$H_1(e^{j\omega})$" : H_1, 
        #     r"$H_2(e^{j\omega})$" : H_2
        # }
        # w = np.linspace(-1, 1,re)
        # frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Unormaliseret", "Magnitude", "Fase", "Unwrapped")
        # gemBillede("Øvelse 10.4.6.png", fig)
        
        # * Indså, at det eneste jeg rent faktisk havde brug for var en cos modulering.
        omega_0 = 0.495 * np.pi
        n = np.arange(-floor(M/2), ceiling(M/2) + 1, dtype = float)
        h_2 = 2 * np.cos( omega_0*n)*h_1
        
        fig, ax = plt.subplots()
        diskretePlotAfFunktioner(fig, ax, n, {r"$h_1[n]$" : h_1, r"$h_2[n]$" : h_2})
        # gemBillede("Øvelse 10.4.7.png", fig)
        re = 1024
        H_1 = np.fft.fft(h_1, re)
        H_1 = np.fft.fftshift(H_1)
        H_2 = np.fft.fft(h_2, re)
        H_2 = np.fft.fftshift(H_2)
        
        frekvensFunktioner = {
            r"$H_1(e^{j\omega})$" : H_1, 
            r"$H_2(e^{j\omega})$" : H_2
        }
        fig, ax = plt.subplots(3, 2, sharex = True)
        w = np.fft.fftfreq(re)  # [-pi/2 : pi/2] (Normaliseret)
        w = np.fft.fftshift(w)
        w = w * 2               # [-pi : pi]     (Normaliseret)
        frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Unormaliseret", "Magnitude", "Fase", "Unwrapped")
        # gemBillede("Øvelse 10.4.8.png", fig)
        
        
        h_3 = wn * h_2 
        H_3 = np.fft.fft(h_3, re)
        H_3 = np.fft.fftshift(H_3)
        
        # Bandpass design using firwin + Kaiser
        M = 74 
        beta = 4.5335
        h_4 = sig.firwin(M + 1, [0.25, 0.74], pass_zero=False, window=('kaiser', beta))# , 0) 
        H_4 = np.fft.fft(h_4, re)
        H_4 = np.fft.fftshift(H_4)
        w = np.fft.fftfreq(re)  # [-pi/2 : pi/2] (Normaliseret)
        w = np.fft.fftshift(w)
        w = w * 2               # [-pi : pi]     (Normaliseret)
        
        frekvensFunktioner = {
            r"$H_3(e^{j\omega})$" : H_3, 
            r"$H_4(e^{j\omega})$" : H_4
        }
        fig, ax = plt.subplots(3, 2, sharex = True)
        frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Unormaliseret", "Magnitude", "Fase", "Unwrapped", "dB")
        # gemBillede("Øvelse 10.4.9.png", fig)
        
class Opgave_kapitel10_2(Beregning): 
    beskrivelse = """Design af lavpass filter 
    Eksempel 10.5 i bogen
    Design krav: 
    wp = 0.25pi
    ws = 0.35pi
    Ap = 0.1dB 
    As = 40dB
    Designes ud fra frekvens sampling 
    """
    wp = 0.25*np.pi
    ws = 0.35*np.pi
    Ap = 0.1
    As = 40
        
    M = 44          # n samples 
    # L = M + 1       # Længde 
    # alpha = M/2; Q = np.floor (alpha)      # Fase forsinkelses parametre 
    def L(M): return M + 1; 
    def alpha(L): return (L - 1)/2
    def phaseArrayOpsætning(Q): 
        """
        Laver liste elementer til phase til frekvenserne.
        [0, 1, 2, ... alpha, -alpha, ..., -1]
        """
        return np.hstack([np.arange(Q + 1), -np.arange(Q, 0, -1)])
    def psid(alpha, L, phaseArray, M, Q): return - alpha(L(M)) * 2 * np.pi/L(M) * phaseArray(Q) # Psi_d[k]
    
    
    # Cosine transition approach til frekvenssampling
    Q = M/2
    w = np.linspace(0, 2*np.pi, 1001)       # Frekvens liste
    dw = 2 * np.pi / L(M)                   # Afstand mellem hver sample.
    k = np.arange(M)                        # Samplet frekvens index
    k1  = np.int64(np.floor(wp/dw))         # Indeks tættest på pass bånd kanten
    k2 = np.int64(np.ceil(ws/dw))           # Indeks tættest på stop bånd kanten
    w_trans = np.arange((k2 - 1), (k1+1))   # Er hvordan forfatteren beskriver frekvenserne i transitions båndet. 
    #                                         Jeg forstår ikke den omvendt. Det er noget med symmetrien i spektret så man får for 2*pi - w. 
    #                                         Men havde det kun været for det, så kunne man også lave den på den normale måde og flippe.
    w_trans = np.arange(k1 + 1, k2 - 1 + 1)
    A = 0.5 +0.5*np.cos(np.pi*(ws - w_trans)/(ws - wp))     # Transitions bånds samplesne
    B = A[::-1]     # stop, start, step   <- step < 0       # Transitions bånds samplesne for omega > pi. 
    
    # Ønsket frekvensspektrum
    Ad = np.hstack([np.ones(k1 + 1), A, np.zeros(L(M) - 2 * k2 + 1), B, np.ones(k1)])
    Hd = Ad*np.exp(1j*psid(alpha, L, phaseArrayOpsætning, M, Q))    # Frekvens spektrum, lav resolution
    hd = np.real(np.fft.ifft(Hd))                                   # Impuls response
    h = hd * np.ones(L(M))                                          # Her bruges eterne bare som en vindue funktion. 
    H = np.fft.fft(h, w.shape[0])                                   # [0: pi, -pi: 0]
    # Asd ≈ 50dB, men matlab beregner det til omkring 34, men deres beregning er lidt tvivlsom. 
    # Motivationen er, at den ikke er skud sikker, så derfor prøves en ny metode.
    
    
    
    
    # Window approach til frekvenssampling
    wc = (wp + ws)/2 # Cutoff frekvens
    k1 = np.int64(np.floor(wc/dw))            # Index venstre for cutoff frekvens 
    k2 = np.int64(np.ceil(wc/dw))             # Index højre for cutoff frekvens
    
    Ad = np.hstack([np.ones(k1 + 1), np.zeros(L(M) - 2 * k2 + 1), np.ones(k1)])    # Ønskede amplituder 
    
    Hd2 = Ad*np.exp(1j*psid(alpha, L, phaseArrayOpsætning, M, Q))                # Ønskede frekvens respons samples.
    hd2 = np.real(np.fft.ifft(Hd2))                                               # Ønsked impuls response 
    h2 = hd2 * sig.windows.hamming(L(M))                                             # Filtreret respons.
    H2 = np.fft.fft(h2, w.shape[0])
    
    
    
    # ? Konklusion 
    # Vindue funktionen medføre et mere konstant stopbånd,
    # hvor den lavet med cos transitionen falder lidt med frekvenserne
    # Jeg har også fundet ud af, at forfatteren måske gik efter den højeste sidetop. Så at faldet var fra pass bånd til maks sidetop. 
     
    # * Hvad jeg har gjort 
    # Ønskede amplituder
    #    |
    #    v
    # Oversæt til svarende frekvenser.
    # Samplet frekvenser for [0, 2 * np.pi]     <- Lav resolution
    #    |
    #    v
    # Inverse fourier transform                 
    #    |
    #    v 
    # Fourier transform()                       <- Bedre resolution 
    #    |
    #    v 
    # FFTshift [0, 2*np.pi] -> [-pi, pi]

    # Filtrer følger [-pi, pi], men til beregning laver vi for [0, 2*np.pi]
    # Derfor ligner filteret et højpass ved kreering, men det er for at tilpasse det. 
    
    
    
    def frekvensResponseAfProcess(self): 
        self.H = np.fft.fftshift(self.H)                                    # [-pi: pi]
        self.H2 = np.fft.fftshift(self.H2)                                  # [-pi: pi]
        frekvensFunktioner2 = {
            "Hd1" : self.Hd,
            "Hd2" : self.Hd2
        }
        frekvensFunktioner = {
            r"$H_{cos trans}$" : self.H,
            r"$H_{vindue}$" : self.H2
        }
        w2 = np.linspace(0, 2*np.pi, 45)
        self.w -= np.pi                                                     # Shifter 
        self.w *= 2                                                         # Tilpasser min normalisering            
        
        
        fig, ax = plt.subplots(2, 2)
        frekvensResponseTo(fig, ax, w2, frekvensFunktioner2, "Magnitude", "Unwrapped")
        # gemBillede("Eksempel 10.5.a.png", fig)
        fig, ax = plt.subplots(2, 2)
        frekvensResponseTo(fig, ax, self.w, frekvensFunktioner, "Magnitude", "Unwrapped", "dB")
        # gemBillede("Eksempel 10.5.b.png", fig)
        
    def __init__(self): 
        self.frekvensResponseAfProcess()

class Opgave10_4(Opgave): 
    N = 1001
    w = np.linspace(-np.pi, np.pi, N)
    h = np.hstack([[1, 1, 1, 1], np.zeros(N - 4)])
    H = np.fft.fft(h)                               # [0: pi, -pi:0]
    H = np.fft.fftshift(H)
    
    #Ideele værdier. 
    A = (np.sin(w * 5/2)/(np.sin(w/2))) * np.exp(-2j*w)
    
    def sammenlign(self):
        A = self.A; H = self.H; w = self.w
        fig, ax = plt.subplots(2, sharex = True)
        ax[0].grid()
        ax[0].set_ylabel("Forstærkning") 
        ax[1].grid()
        ax[1].set_ylabel(r"$\angle$ fase")
        ax[1].set_xlabel(r"$\omega$")
        ax[0].plot(w, np.abs(H), label=r"$|H(e^{j\omega})|$")
        ax[0].plot(w, np.abs(A), "-.", label=r"$A(e^{j\omega})$")
        ax[1].plot(w, np.angle(H), label=r"$\angle H(e^{j\omega})$")
        ax[1].plot(w, np.angle(A), "-.", label=r"$\psi(e^{j\omega})$")
        fig.legend()
        plt.show()
        # gemBillede("Opgave 10.4.png", fig)
    
    def __init__(self):
        self.sammenlign()

class Opgave10_10(Opgave): 
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
        # gemBillede("Opgave 10.10.setup.png", fig)
        return h 
    
    def filterPræstation(self, M, ws, wp, analyseNavn, Hfundet = None): 
        re = 27                           # Analytisk resolution i frekvensdomænet
        # Praktisk filter
        h = self.højpassFilter(M, sig.windows.hamming, ws, wp)
        H = np.fft.fft(h, re)               # [0:pi, -pi, 0]
        H = np.fft.fftshift(H)              # [-pi: pi]
        if Hfundet is not None:             # Til sidste del, hvor jeg skal sammenligne med scipy function. 
            H = Hfundet 
        
        # Ideel filter. 
        w = np.linspace(-np.pi, np.pi, re) 
        A = np.zeros(re, dtype=complex)
        wc = (0.3 - 0.05)*np.pi
        As = 10**(-50/20)                   # Forstærkning ikke i dB
        Ap = 10**(0.01/20)                  # Forstærkning ikke i dB
        A[np.abs(w) <= wc] = Ap
        A[np.abs(w) > wc] = As
        A = np.fft.fftshift(A)
        fig, ax = plt.subplots(3, 3)
        funktioner = {
            r"$H(e^{j\omega})$" : H,
            r"$A(e^{j\omega})$" : A,
            r"$E(e^{j\omega})$" : np.abs(A) - np.abs(H)
        }
        w /= np.pi                          # Normalisere
        frekvensResponseTo(fig, ax, w, funktioner, "Magnitude", "Fase", "Unwrapped", "Unormaliseret")
        gemBillede(analyseNavn, fig)
    
    def foersteDesign(self): 
        M = 26                              # Antal samples
        wp = 0.05 * np.pi           
        ws = 0.30 * np.pi
        self.filterPræstation(M, ws, wp, "Opgave 10.10.resultat.png")
    
    def andenDesign(self): 
        M = 26                              # Antal samples
        wp = 0.15 * np.pi           
        ws = 0.30 * np.pi
        self.filterPræstation(M, ws, wp, "Opgave 10.10.praktisk.png")
        
    def __init__(self):
        # self.foersteDesign()
        # self.andenDesign()
        H = sig.firwin(27, 0.175 * np.pi , window="hamming")
        fig, ax = plt.subplots()
        H = np.fft.fftshift(H) 
        self.filterPræstation(26, 0.05*np.pi, 0.3*np.pi, "Opgave 10.10.Scipy.png", H)
        ax.plot(np.linspace(-np.pi, np.pi, 27), np.abs(H))
        plt.show()

class Opgave10_11(Opgave):
    def Adk(self, L, wc): 
        # Ideelt lowpass
        alpha = np.int64(L/2)
        w_k = np.linspace(0, np.pi, alpha)
        Ad = np.zeros(alpha)                    # Frequency values
        idxlp = np.where(w_k <= wc)             # Lp indices 
        Ad[idxlp] = 1
        Ad = np.hstack([Ad, 0, Ad[::-1][:alpha - 1]])    # -pi : 0 er det samme som pi : 2pi, derfor vender jeg A om og lægger den ind i sidste halvdel
        return Ad
    def psidk(self, L): 
        Q = np.int64(floor((L - 1)/2))
        C = 2*np.pi/L 
        kid = np.hstack([np.arange(Q + 1), np.arange(-(Q + 1), 0, 1)])              # Index manipulation for k
        # k = 0, ...Q; -(L - k) = -20 + 10, ... -20 + 19 
        psidk = - Q * C * kid                                                       # q = 0 for type I og type II.
        return psidk
    
    def __init__(self):
        L = 20
        wc = pi/2
        
        # * Tjek
        fig, ax = plt.subplots()
        n = np.arange(L)
        Ad = Adk(L, wc)
        diskretePlotAfFunktioner(fig, ax, n , {"Ad": Ad})
        
        # *Frekvens udtræk samplings parametre 
        H_oensket = Ad * np.exp(1j*psidk(L)) 
        
        # * Impuls responser 
        h_oensket = np.real(np.fft.ifft(H_oensket))
        h_rigtig = h_oensket * np.ones(L)                                           # rektangulært vindue.
        # * Tjek
        fig, ax = plt.subplots()
        n = np.arange(L)
        diskretePlotAfFunktioner(fig, ax, n, {r"$h_{plukket}[n]$": h_oensket, r"$h_{praktisk}$" : h_rigtig})
        
        # * Filtre analyse
        re = 1024
        H_oensket = np.fft.fft(h_oensket, re)                   # [0, 2pi]
        H_rigtig = np.fft.fft(h_rigtig, re)                     # [0, 2pi]
        w = np.linspace(-1, 1, re)                              # [-pi: pi]
        w += 1                                                  # [0, 2pi]
        w *= 2 * np.pi                                          # Får min normalisering til at gå op
        # * Tjek 
        # frekvensFunktioner = {
        #     r"$H_{oensket}(e^{j\omega})$" : H_oensket, 
        #     r"$H_{rigtig}(e^{j\omega})$" : H_rigtig
        # }
        # fig, ax = plt.subplots(3, 2, sharex = True)
        # frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Magnitude", "Fase", "Unwrapped")
        
        # ? Svar 
        fig, ax = plt.subplots()
        w_k = np.linspace(0, 2 * np.pi, L)
        fig, ax = plt.subplots()
        ax.plot(w_k, Ad, 'o')
        # H_rigtig = np.fft.fft(h_rigtig)
        w /= 2 
        ax.plot(w, np.abs(H_rigtig))
        plt.show()
        # gemBillede("Opgave 10.11.png", fig)
        
        
        # * Nu for L = 400
        # 1. Frekvens pluk 
        L = 400
        A = Adk(L, np.pi/2)
        print(A.shape)
        H = A * np.exp(1j*psidk(L))          # [0: 2pi]
        
        # 2. Til tidsdomæne
        h = np.fft.ifft(H)
        
        # 3. Vindue inputtet
        h_reel = h * np.ones(L)
        
        # 4. Transformer
        re = 1024
        H_reel = np.fft.fft(h_reel, re)
        
        # * Sammenlign
        fig, ax = plt.subplots(2, sharex = True)
        w_k2 = np.linspace(0, 2* np.pi, L)
        ax[0].plot(w_k, Ad, 'o')
        ax[0].plot(w, np.abs(H_rigtig))
        ax[1].plot(w_k2, A, 'o')
        ax[1].plot(w, np.abs(H_reel))
        plt.show()
        # gemBillede("Opgave 10.11.1.png", fig)
        
        
        
        # * Nu med hamming vinduet. 
        h_ham = h * sig.windows.hamming(L)
        H_ham = np.fft.fft(h_ham, re)
        # * Sammenlign
        fig, ax = plt.subplots(3, sharex = True)
        w_k2 = np.linspace(0, 2* np.pi, L)
        ax[0].plot(w_k, Ad, 'o')
        ax[0].plot(w, np.abs(H_rigtig))
        ax[1].plot(w_k2, A, 'o')
        ax[1].plot(w, np.abs(H_reel))
        ax[2].plot(w_k2, A, 'o')
        ax[2].plot(w, np.abs(H_ham))
        plt.show()
        # gemBillede("Opgave 10.11.2.png", fig)
    
class Opgave10_13(Beregning): 
    
    def chebyshev(self, n, w, Tn): 
        if n == 0 : return 1                # T_0 = 1
        elif n == 1 : return cos(w)         # T_1 = cos(w)
        poly = 2 * cos(w) * self.chebyshev(n - 1, w, Tn) - self.chebyshev(n - 2, w, Tn)
        if n > len(Tn): 
            Tn += [poly]
        return poly
        
    def __init__(self):
        w = symbols("omega")
        Tn = []
        self.chebyshev(10, w, Tn)
        for i, T in enumerate(Tn) :
            T = simplify(T)
            eq = Eq(Function(f"T_{i + 2}")("x"), T)
            pprint(latex(eq))

class Opgave10_14(Opgave):
    def solveForCoeffs(x): 
        A = x
        A = np.vander(A, 3, increasing= True)
        A = np.hstack([A, np.array([1, -1, 1, -1])[:, np.newaxis]])
        
        b = np.array([1 - 2*x_k + 4*(x_k**(2)) - 2*(x_k**3) for x_k in x])[:, np.newaxis]
        
        return np.linalg.solve(A, b)
    
    a0, a1, a2, delt = solveForCoeffs([0, 1/3, 2/3, 1])
    
    # * Graf 
    def plot(coeffs): 
        a0, a1, a2, delt = coeffs
        x = np.linspace(0, 1, 100) 
    
        f = 1 - 2*x + 4 * (x**2) - 2*(x**(3))
        P2 = a0 + a1*x + a2*(x**2)
        e = f - P2
        fig, ax = plt.subplots()
        ax.grid()
        ax.axhline(0, color='black', linewidth=1) 
        ax.plot(x, f, label = r"$f(x)$")
        ax.plot(x, P2, '--.', label = r"$P_2(x)$")
        ax.plot(x, e, '--', label = r"$e(x)$")
        fig.legend()
        plt.show()
        # gemBillede("Opgave 10.14.png", fig)
    
    plot([a0, a1, a2, delt])
    
    
    # * Forsæt indtil equiripple.
    # Se på extremerne, så at [del+, del-, del+, del-]
    coeffs = solveForCoeffs([0, 0.236, 0.736, 1])        # +-0.07
    plot(coeffs)
    res_coeffs = coeffs
    
    
    # Chatten fandt de endelige værdier. 
    coeffs = solveForCoeffs([0, 0.2632, 0.7368, 1])
    coeffs[:3] = np.array([0.938, -0.875, 1])[:, np.newaxis]
    plot(coeffs)
    
    
    
    
    
Opgave10_14()

class eksamensOpgave2021_1(Opgave): 
    N = 1000
    w = np.linspace(-np.pi, np.pi, N)
    z = np.exp(1j*w)
    H = (3 + z**(-1)) / (1 + 0.5*(z**(-1)))
    def __init__(self): 
        frekvensFunktioner = {
            r"$H(e^{j\omega})$" : self.H
        }
        fig, ax = plt.subplots(2, 1)
        w /= np.pi
        frekvensResponseTo(fig, ax, w, frekvensFunktioner, "Magnitude", "Fase", "Unormaliseret")
        gemBillede("Eksamenssæt2021.1.3.png", fig)
    
class eksamensOpgave2021_2(Opgave): 
    def beregningsMatrice(N): 
        n = np.arange(0, N)
        W_Nn = np.ones(N) * np.exp(-1j * 2 * ( np.pi/N ) * n )
        W = np.vander(W_Nn, N, increasing = True)
        return W
    xn = np.array([1, -1, 4, 7])
    W = beregningsMatrice(4)
    res_Xk = np.round(np.inner(xn, W), 3)
    
    re = 1024 
    X = np.fft.fft(xn, re)
    X = np.fft.fftshift(X)
    def __init__(self):
        funktioner = {
            r"$X(e^{j\omega})$" : self.X 
        }
        w = np.linspace(-1, 1, self.re)
        fig, ax = plt.subplots(2, 1)
        
        frekvensResponseTo(fig, ax, w, funktioner, "Magnitude", "Fase", "Unormaliseret")
        # gemBillede("Eksamenssæt2021.4.2.png", fig)
    
class eksamensOpgave2021_2ny(Opgave): 
    w = np.linspace(-np.pi, np.pi, 1024)
    z = np.exp(1j*w)
    X = 1 - z**(-1) + 4*z**(-2) + 7*z**(-3)
    def __init__(self):
        fig, ax = plt.subplots(2, 1, sharex= True)
        funktioner = {
            r"$X(e^{j\omega})$" : self.X 
        }
        frekvensResponseTo(fig, ax, self.w, funktioner, "Magnitude", "Fase", "Unormaliseret")
    
class EksamensOpgave2022_2(Opgave): 
    w = np.linspace(-np.pi, np.pi, 1000)
    z = np.exp(1j*w)
    H = (1 - 2*(z**(-1)))/(1 + 0.5*(z**(-1)))
    z0 = np.exp(1j*np.pi/4)
    H0 = (1 - 2*(z0**(-1)))/(1 + 0.5*(z0**(-1)))
    def __init__(self):
        fig, ax = plt.subplots(1)
        w = self.w / np.pi
        frekvensResponseTo(fig, ax, w, {r"$H(e^{j\omega})$" : self.H}, "Magnitude", "Unormaliseret")
        gemBillede("Eksamensopgavesæt2022.2.png", fig)

class EksamensOpgave2022_5(Opgave): 
    def beregningsMatrice(self, N): 
        n = np.arange(0, N)
        W_Nn = np.ones(N) * np.exp(-1j * 2 * ( np.pi/N ) * n )
        W = np.vander(W_Nn, N, increasing = True)
        return W

    def __init__(self):
        x = np.array([3, 2, 1, 0])
        W = self.beregningsMatrice(4)
        X = np.inner(W, x)
        Y = np.array([1, 1, 1, 1])
        pprint(np.round(W))
        pprint(np.round(X, 2))
        pprint(np.fft.fft(x))
        pprint(np.round(np.inner(np.linalg.inv(W), Y), 2))
        pprint(np.fft.ifft(Y))

class EksamensOpgave2024_ord_1(Opgave): 
    w = np.linspace(-np.pi, np.pi, 3)
    z = np.exp(1j*w)
    H = (3 * z + 2 - z**(-1))
    x = [4, 5, -6]
    X = np.fft.fft(x)
    Y = X*H
    res_y = np.fft.ifft(Y)
    res_y2 = np.round( H * (z**1) ) 

class EksamensOpgave2024_ord_2(Opgave):
    alpha = -1/(np.sqrt(2)) + 0.5j
    res_størrelse = np.abs(alpha)
    res_vinkel = np.angle(alpha)

class EksamensOpgave2024_ord_3(Opgave): 
    # DF II system 
    b = [2] 
    a1, a2 = symbols("alpha_1 alpha_2")
    a = [1, a1 + a2]
    # res_sos = sig.residuez(b, a) Kan jeg ikke 

class EksamensOpgave2024_ord_4(Opgave): 
    b = [-0.5, 1]
    a = [1, 0.5]
    res_rpk = sig.residuez(b, a)
    h = lambda z : (-2.5)/(1 + 0.5*(z**(-1)) + 2)
    res_h1 = np.abs(h(np.exp(1j*np.pi)))
    res_h2 = np.abs(h(np.exp(0)))
    res_h3 = np.abs(h(np.exp(1j*np.pi/2)))
    
    def __init__(self):
        w = np.linspace(-np.pi, np.pi, 1024)
        z = np.exp(1j*w)
        
        H2 = (-2.5)/(1 + 0.5*(z**(-1)) + 2)
        
        funktioner = {
            r"$H(e^{j\omega})$" : H2,
        }
        
        fig, ax = plt.subplots(1, 1, sharex=True)
        w /= np.pi
        frekvensResponseTo(fig, ax, w, funktioner, "Unormaliseret", "Magnitude")# , "Fase")
        gemBillede("Eksamenssæt2024.ord.4.png", fig)
        
class EksamensOpgave2024_ord_2_2(Opgave): 
    a = symbols("alpha", complex = True)
    H = lambda alpha, z : 1 + alpha*(z**(-1))
    # z0 = trigsimp(np.exp(-1j*np.pi/4))
    # eq = Eq(0.5, Abs(H(a, z0)))
    # res_a = solve(eq, a)
    a = -0.5 + 0.353j
    a *= np.sqrt(2)/2
    
    r = np.abs(a)
    theta = np.angle(a)     # +- theta
    res_rTheta = (r, theta)
    
    alpha = r * np.exp(1j*theta) # Evaluering for + theta
    
    
    def __init__(self):
        
        w = np.linspace(-np.pi, np.pi, 100)
        z = np.exp(-1j*w) 
        h = np.array([1, self.alpha])
        res_h = np.round(h, 2)
        fig, ax = plt.subplots(2, sharex = True)
        w += np.pi
        w /= np.pi
   
         # frekvensResponseTo(fig, ax, w, {r"$H(e^{j\omega})$" : H}, "Unormaliseret", "Magnitude", "Fase")
    
        n = np.arange(100)
        xn = np.cos(np.pi/4 * n)
        y = np.convolve(xn, h)[:100]
        fig, ax = plt.subplots(1)
        diskretePlotAfFunktioner(fig, ax, n, {r"$y[n]$" : y})

class EksamensOpgave2024_ord_3_2(Opgave): 
    a1, a2, z = symbols("alpha_1 alpha_2 z")
    H = 1/(1 + a1*z) + 1/(1 + a2 * z)
    res_H = H
    res_H = cancel(H)

class EksamensOpgave2024_ord_4_2(Opgave): 
    res_H = partialFraction([0.5, 1], [1, -0.5], "DT")
    res_rpk = sig.residuez([-0.5, 1], [1, -0.5])
    
    w = np.linspace(-np.pi, np.pi, 100)
    z = np.exp(1j*w)
    H = (-0.5 + z**(-1))/(1 - 0.5*(z**(-1)))
    H2 = 1.5/(1 - 0.5*(z**(-1))) - 2
    def __init__(self):
        funktioner = {
            r"$H(e^{j\omega})$" : self.H, 
            #r"$H_2(e^{j\omega})$" : H2
        }
        fig, ax = plt.subplots(2, 1, sharex=True)
        w = self.w / np.pi
        frekvensResponseTo(fig, ax, w, funktioner, "Unormaliseret", "Magnitude", "Fase")
        gemBillede("Eksamenssæt2024.ord.4.4.2.png", fig)

class EksamensOpgave2024_re_2(Opgave): 
    w = np.linspace(-np.pi, np.pi, 150)
    z = np.exp(1j*w)
    H = 1/(35) * (-3*(z**(2)) + 12*z + 17 + 12*(z**(-1)) - 3*(z**(-2)))
    x = np.array([-174, -43, -106, -46, -188, -49, -99, -168, 89, -169, 154, -135, 171, -3, 98, 89])
    h = 1/(35) * np.array([-3, 12, 17, 12, -3])
    y = np.convolve(x, h)[:len(x)]
    def __init__(self):
        funktioner = {
            r"$H(e^{j\omega})$" : self.H
        }
        fig, ax = plt.subplots(2, sharex=True)
        w = self.w / np.pi
        frekvensResponseTo(fig, ax, w, funktioner, "Unormaliseret", "Magnitude", "Fase")
        
        funktioner = {
            r"$x[n]$" : self.x, 
            r"$y[n]$" : self.y
        }
        fig, ax = plt.subplots()
        n = np.arange(len(self.x))
        ax.grid()
        samples = {
            r"$x[n]$" : self.x,
            r"$y[n]$" : self.y 
        }
        ax.plot(n, self.x, '-.', label= "Støjsignal")
        ax.plot(n, self.y, label = "Output")
        fig.legend()
        fig, ax = plt.subplots(1, 2, sharey=True)
        diskretePlotAfFunktioner(fig, ax, n, samples)

class EksamensOpgave2024_re_3(Opgave): 
    M = 110
    h = sig.windows.blackman(M)
    re = 1024
    H = np.fft.fft(h, re)
    H = np.fft.fftshift(H)
    w = np.linspace(-np.pi, np.pi, re)
    
    def __init__(self):
        fig, ax = plt.subplots()
        n = np.arange(self.M)
        diskretePlotAfFunktioner(fig, ax, n, {"w_b[n]" : self.h})
        funktioner = {
            r"$W_b(e^{j\omega})$" : self.H
        }
        fig, ax = plt.subplots(3, sharex = True)
        # w = self.w / np.pi
        frekvensResponseTo(fig, ax, self.w, funktioner, "Unormaliseret", "Magnitude", "Fase", "Unwrapped", "dB")
     
class EksamensOpgave2024_re_4(Opgave): 
    w = np.linspace(-np.pi, np.pi, 100)
    z = np.exp(1j*w)
    H = 1/(1 - 0.5 * (z**(-1)))
    def __init__(self):
        w = self.w / np.pi
        fig, ax = plt.subplots(2, sharex = True)
        frekvensResponseTo(fig, ax, w, {r"$H(e^{j\omega})$" : self.H}, "Unormaliseret", "Magnitude", "Fase")
    
class EksamensOpgave2024_re_5(Opgave): 
    Wn = np.array([[1,  1], 
                   [1, -1]])
    x = np.array([1, 2])
    res_y = np.inner(Wn, x)

