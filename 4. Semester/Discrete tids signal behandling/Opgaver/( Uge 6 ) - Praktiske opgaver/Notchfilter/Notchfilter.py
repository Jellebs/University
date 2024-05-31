import numpy as np
import os 
import matplotlib.pyplot as plt 
import scipy.signal as sig
from sympy import * 

def makePath(folders): 
    dir = os.getcwd()
    for folder in folders: 
        dir += f"/{folder}" 
    return dir


def makePlot(x, y): 
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Ecg skanning")
    fig.legend()
    plt.show()

















## Få data
parentFolders = ["Opgaver", "( Uge 6 ) - Praktiske opgaver", "Notchfilter"]
dir = makePath(parentFolders)
path = f"{dir}/ecg.dat"
print(path)

f = 500;            samples = 25000
T = samples/f;      step = 1/f
t = np.arange(0, T, step) # f = 500Hz
data = lambda : np.loadtxt(path)[0: samples]
data_f = lambda : np.fft.fft(data())
omega = lambda : np.fft.fftfreq(len(data()), 1/f)

## Plot data  
plotTids = lambda : makePlot(t, data()) # - Plot af data i tidsdomæne.
plotFrekvens = lambda : makePlot(omega()[: int(len(data_f())/2)], data_f()[: int(len(data())/2)]) # Positive side kun. Spike ses ved omega = 50rad/s

## Lav notch filteret
def notchFilter(theta, z):  # Bryder frekvenser ved theta. Formel 5.125
    #   Formlen for notch filters
    #                   2cos(theta)       1
    # H(z) = b0 * ( 1 - -----------  +   ---- )
    #                        z           z*z
    # Hvor frekvenser til theta bliver filtreret fra. 
    # I frequency domain findes konvolution af to funktioner ved at gange dem med hinanden. 
    # b0 er valgt, så den maksimale magnitude response er 1. 
    def loesForB0(): 
        Notch_sym = lambda b0, theta, z : b0 * (1 - 2*cos(theta)/z + 1/(z**2))
        omega, z, b0, c, k = symbols("omega z b0 c k")
        eq = 1 - sqrt(b0**2 + (b0*c)**2 + (b0*k)**2)
        b0 = solve(eq, b0)
        pprint(eq)
        pprint(b0)
        
        #                _______________
        #      +       ╱       1             
        # b0 =        ╱  ───────────── 
        #      -     ╱      2    2         
        #          ╲╱      c  + k  + 1   
    
    b0 = lambda c, k : np.sqrt(1/(c**2 + k**2 + 1)) # Jeg mener at negativ amplitude spejlvender signalet. Det vil ikke gøre det store, med så mange målinger, men det er ikke det jeg ønsker.
    c = lambda omega, z : -2*np.cos(omega)/z
    k = lambda z : 1/(z**2)
    Notch_num = lambda theta, z : b0(c(theta, z), k(z)) * (1 - 2*np.cos(theta)/z + 1/(z**2))
    return Notch_num(theta, z)

def forbedretNotchFilter(theta, z): 
    # Formel 5.126
    #        B(z)      b0 - 2b0*cos(theta) * z^-1 + b0*z^-2
    # G(z) = ----    = ------------------------------------
    #        A(z)      1 - 2*r*cos(theta) * z^-1 + r^2z^-2 
    
    # Vi ønsker at radiusen skal være så tæt på enhedscirklen som muligt, så systemet reagerer hurtigst muligt, men samtidig ikke er ustabilt. 
    # Hvis r sættes som 1 så kan der være en stor sandsynlighed for at støj vil gøre systemet ustabilt. 
    # i bogen sætter de værdien til at være 0.9. Det gør jeg også.
    r = 0.9
    def loesForB0(): 

        # Igen finder vi for |G(z)|max = 1.
        # Filteret står klar på form til partial fraction.
        b0, theta, z, c = symbols("b0 theta z c")
        theta = 50
        Bz = b0 - 2*b0*cos(theta) * (z**(-1)) + b0*(z**(-2))  
        Az =  1 - 2*r*cos(theta) * (z**(-1)) + r**2 * (z**(-2))
        nulpunkter = solve(Bz, z); nulpunkter = [N(nulpunkter[i], 4) for i in range(len(nulpunkter))]
        poler = solve(Az, z); poler = [N(poler[i], 4) for i in range(len(poler))]

        #        B(z)      (z^(-1) - (0.965 - 0.2624i)) * (z^(-1) - (0.965 + 0.2624))                      A                            B
        # G(z) = ----    = ------------------------------------------------------------- = ----------------------------- + -----------------------------
        #        A(z)      (z^(-1) - (0.8685 - 0.2361i)) * (z^(-1) - (0.8685 + 0.2361i))   (z^(-1) - (0.8685 - 0.2361i))   (z^(-1) - (0.8685 + 0.2361i))

        #                                                                              
        # (z^(-1) - (0.965 - 0.2624i)) * (z^(-1) - (0.965 + 0.2624i)) = A*(z^(-1) - (0.8685 + 0.2361i) + B * (z^(-1) - (0.8685 - 0.2361i))
        # z^(-1) = 0.8685 + 0.2361i => A*(0)
        # z^(-1) = 0.8685 - 0.2361i => B*(0)
        A, B = symbols("A B")
        # Det er ikke når z = pol men z^-1 der er pol, at ligningerne findes. Jeg siger at Z = z**(-1)
        eq = lambda Z : Eq((Z - (0.965 - 0.2624j)) * (Z - (0.965 + 0.2624j)), A*(Z - (0.8685 + 0.2361j)) + B *(Z - (0.8685 - 0.2361j)))
        eq1 = eq(poler[1]); B = solve(eq1, B)
        # Værdi for tæt på 0. eq2 = eq(poler[0]);
        eq2 = lambda Z : Eq((Z - (0.965 - 0.2624j)) * (Z - (0.965 + 0.2624j)), A*(Z - (0.8685 + 0.2361j))); eq2 = eq2(poler[0])
        A = solve(eq2, A)
        pprint(eq2)
        pprint(A)
        A = - 0.0965 + 0.0475j
        B = - 0.0965 - 0.0475j

        #                                   A                            B
        # G(z) = ----    =  ----------------------------- + -----------------------------
        #        A(z)       (z^(-1) - (0.8685 - 0.2361i))   (z^(-1) - (0.8685 + 0.2361i))
        Gz = A/(z**(-1) - (0.8685 - 0.2361j)) + B/((z**(-1) - (0.8685 + 0.2361j)))
        
        # Så nu kan jeg beregne for den absolutte værdi ved at sige: 



        #           - 0.0965 + 0.0475j                - 0.0965 - 0.0475j
        # a =  -----------------------------   b = -----------------------------
        #       (z^(-1) - (0.8685 - 0.2361i))      (z^(-1) - (0.8685 + 0.2361i))

        # Og 
        # 
        # 1 = |Gz| = √(a**2 + b**2)

        # Men til min overraskelse, så afhang mine beregninger ikke af b0, så det kan ikke lade sig gøre. 

    # Lad mig bare sige en arbitrær værdi og se om det passer
    b0 = 0.9; r = 0.9 # Ud fra omega, |Gz| graf så ligner det, at med en b0 = 0.9, vil gainet ikke være større end 1.
    Gz_num = lambda b0, theta, r, z : (b0 - 2*b0*np.cos(theta)/z + b0/(z**2)) / (1 - 2*r*np.cos(theta)/z + r**2/(z**2))
    return Gz_num(b0, theta, r, z)

def lavpass(alpha, z): 
    return alpha/((z**-1) - alpha)

data_f_filtreret = lambda Hz: data_f()*Hz
data_t_filtreret = lambda H : np.fft.ifft(data_f_filtreret(H))

z = np.exp(1j*omega())
theta = 50
H1 = notchFilter(theta, z)    
H2 = forbedretNotchFilter(50, z) 
H3 = lavpass(50, z)
data_tf1 = data_t_filtreret(H1)
data_tf2 = data_t_filtreret(H2)

# Plot resultat
plotTidsFiltreret = lambda ft : makePlot(t, ft) # Formel
plotTids()
plotFrekvens()
plotTidsFiltreret(data_tf1)
# plotTidsFiltreret(data_tf2)

