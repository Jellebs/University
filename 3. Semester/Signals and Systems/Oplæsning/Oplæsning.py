from Formelsamling.SignalerOgSystemer import SignalerOgSystemer as SOS 
from Formelsamling.StudieHjaelp import Opgave, Ligning
from sympy import * 
import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

def bodeplot(Xejws, dB = False, wrange = None, *args, **kwargs): 
    wrange = (-1, 1, 100) if wrange == None else wrange
    f = np.linspace(wrange[0], wrange[1], wrange[2]) if dB == False else np.logspace(wrange[0], wrange[1], wrange[2])
    
    w = 2*np.pi*f
    
    if type(Xejws) != list: 
        fig, ax = plt.subplots(2, 1, sharex= True)
        Xejw = lambdify(symbols("w"), Xejws)        # Lav numerisk funktion 
        Xejw = Xejw(w)                              # Lav punkter ud fra w.
        magnitude = np.abs(Xejw) if dB == False else 20*np.log10(np.abs(Xejw))
        phase = np.rad2deg(np.angle(Xejw))
        ax[0].set_ylabel("$|X(e^{jw})|$" if dB == False else "$|X(e^{jw})|_dB$"); ax[1].set_ylabel("$\\angle X(e^{jw})$")
        ax[0].grid(True); ax[1].grid(True)
        if dB == True: ax[0].set_xscale("log"); ax[1].set_xscale("log")
        ax[0].plot(w, magnitude, label = "$X(e^{jw})$", *args, **kwargs) 
        ax[1].plot(w, phase) 
        fig.text(0.5, 0.04, '$\omega$', ha='center')
        fig.legend()
        plt.show()
        return
    
    # Setup
    fig, ax = plt.subplots(2, len(Xejws))
    colors = iter(plt.cm.rainbow(np.linspace(0, 1, len(Xejws) + 1)))
    fig.text(0.5, 0.04, '$\omega$', ha='center')
    ax[0, 0].set_ylabel("$|X(e^{jw})|$" if dB == False else "$|X(e^{jw})|_dB$"); ax[1, 0].set_ylabel("$\\angle X(e^{jw})$")
    # ax[0, 0].set_ylabel("$|X(e^jw)|$" if dB == False else "$|X(e^jw)|_dB$"); ax[1, 0].set_ylabel("$\\angle X(e^jw)$")
    for i in range(len(Xejws)): 
        Xejw = lambdify(symbols("w"), Xejws[i])        # Lav numerisk funktion 
        Xejw = Xejw(w)            
        magnitude = np.abs(Xejw) if dB == False else 20*np.log10(np.abs(Xejw))
        phase = np.angle(Xejw)
        
        color = next(colors)
        
        if dB == True: ax[0, i].set_xscale("log"); ax[1, i].set_xscale("log")
        ax[0, i].plot(w, magnitude, label = f"$X(e^jw))_{i + 1}$", color = color)
        ax[1, i].plot(w, phase, color = color)
    fig.legend()
    plt.show()


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
    
    # SOS.plot_transforms(ts, ys, ys_dict)

class Opgave1_9(Opgave): 
    """
    Opgave om periodicity 
    """
    n = np.linspace(20, 20, 41)
    y = np.cos(7*np.pi*n)
    fig, ax = plt.subplots()
    ax.stem(y)
    # plt.show()
    
class Eksempel3_4(Opgave): 
    x, w0, t= symbols("x omega0 t")
    eq = 1 + sin(w0*t) + 2*cos(w0*t) + cos(2*w0*t + pi/4)
    eq_exp = SOS.harmoniskTilEksponentiel(eq)
    for eks in eq_exp: 
        pprint(eks)
        print("\n")

    print(np.angle(1 - 1j/2, deg= True))
    print(np.angle(1 + 1j/2, deg= True))
    print(np.angle(np.sqrt(2)/2 + 1j * np.sqrt(2)/2, deg=True))

class Eksempelkapitel3(Opgave): 
    """
    Mit forsøg på at reducere en udtryk ved at bruge python notebook. 
    Det er sat op, så at ak er en variabel jeg kommer til at skifte en ad gangen,
    så jeg ikke skal lave alle transformationer, hver gang jeg køre scriptet.
    """
    def __init__(self):
        super().__init__()
        w0, k, N1 = symbols("omega0 k N1", constant = True)
        N = symbols("N", integer = True, variable = True)
        self.w0 = w0; self.k = k; N1 = N1; self.N= N
        self.__ak =  (1/N)*exp(1j*k*w0*N1) * (1 - exp(-1j*k*w0*(2*N1 + 1))) * 1/(1- exp(-1j*k*w0))
    
    def ak(self, funktion = None, faaAk = False, Ak = None, *args): 
        if faaAk == True: 
            return self.__ak  
        if Ak != None: 
            self.__ak = Ak
            return
        if funktion == None: 
            pprint(self.__ak)
            return
        
        self.__ak = funktion(self.__ak, args)
        pprint(self.__ak)
    
class Opgave3_3(Opgave): 
    t = symbols("t")
    w1 = 2*pi/3 
    w2 = 5*pi/3
    xt = 2 + cos(w1*t) + 4 * sin(w2 * t)
    xt_exp = SOS.harmoniskTilEksponentiel(xt)
    pprint(xt_exp)
    
class Opgave3_22(Opgave): 
    t, k, omega0, T = symbols("t k omega0 T")
    # Jeg har lavet en script som sætter ligningerne for ak op for en.
    # Hvad jeg skal have klar er: 
    # T, grænser, xt for hver funktion. 
    funktioner = zip([(2, [(-1, 1)], [t]), 
                  (6, [(-3, -2), (-2, -1), (-1, 1), (1, 2), (2, 3)], [0, t+2, 1, 2-t, 0]), 
                  (3, [(-2, 0), (0, 1)], [t + 2, 2 - 2*t])])
    
    a1k, a2k, a3k = SOS.fourierSerieRepræsentation(funktioner) 
    a_1k, a_2k, a_3k = symbols("a_1k a_2k a_3k")
    # pprint(Eq(a_1k, expand(a1k.doit())))                        # doit tager uevaluerede udtryk og evaluere dem.     
    a3k = a3k.doit()
    func1, func2 = a3k.args
    # term1, cond1 = func1.args[1].args[0]
    # pprint(func1.args[1].args[0][0])
    # pprint(func2.args[1].args[0][0])
    terms = (1/3 * func1.args[1].args[0][0] + 1/3 * func2.args[1].args[0][0])
    C1, w1, w2, C2 = terms.args
    pprint(nsimplify(C1))
    pprint(nsimplify(C2))
    
class Opgave3_22_2forsoeg(Opgave): 
    t, k, omega0, T = symbols("t k omega0 T")
    a_1k, a_2k, a_3k = symbols("a_1k a_2k a_3k")
    funktioner = zip([(2, [(-1, 1)], [t]),
                      (6, [(-3, -2), (-2, -1), (-1, 1), (1, 2), (2, 3)], [0, t + 2, 1, 2 - t, 0]), 
                      (3, [(-2, 0), (0, 1)], [t + 2, 2 - 2*t])]) # Test, samme funktion ud fra andre grænser: (6, [(0, 1), (1, 2), (2, 4), (4, 5), (5, 6)], [1, 2 - t, 0, t - 4, 1])]
    a1k, a2k, a3k = SOS.fourierSerieRepræsentation(funktioner)
    eq1 = Eq(a_1k, a1k.doit())
    eq2 = Eq(a_2k, a2k)
    eq3 = Eq(a_3k, a3k)
    
    
    # ? Trekantet signal for at sammenligne mine resultater med en anden, som har lavet en video på trekantede signaler.
    
    funktioner = zip([(2, [(-1, 0), (0, 1)], [t + 1, 1 - t])])
    a_k = symbols("a_k")
    ak = SOS.fourierSerieRepræsentation(funktioner)[0]
    eq = Eq(a_k, ak)
    
    
    # * Videre til signal 4, 5, 6. Impuls, sinus som step, og sawtooth som step, funktioner
    funktioner = zip([(1, [(-1, -1), (0, 0)], [-2, 1]), 
                      (6, [(-3, 2), (-2, -1), (-1, 1), (1, 2), (2, 3)], [0, 1, 0, -1, 0]),
                      (3, [(0, 1), (1, 2), (2, 3)], [2, 1, 0])])
    a_4k, a_5k, a_6k = symbols("a_4:7")
    a4k, a5k, a6k = SOS.fourierSerieRepræsentation(funktioner)
    eq4 = Eq(a_4k, a4k)
    eq5 = Eq(a_5k, a5k)
    eq6 = Eq(a_6k, a6k)
    
    
    # * Opgaveb
    funktion = zip([(2, [(-1, 1)], [exp(-t)])])
    a_k = symbols("a_k")
    ak = SOS.fourierSerieRepræsentation(funktion)[0]
    eq = Eq(a_k, ak)
    
    def printNuværende(self): 
        pprint(nsimplify(self.eq))
        pprint(nsimplify(self.eq.doit()))

class Opgave3_28(Opgave): 
    a, w0 = symbols("a w0", constants = True)
    N, n = symbols("N n", constants = True, integer = True)
    k = symbols("k", variable = True, integer = True)
    ak = (1/N) * (1 - a**(n+1))/(1 - a)
    ligning = Ligning(a, w0, N, n, k)
    ligning.ligning(ligning = ak)
    ak = ligning.ligning
    ak2 = 1/6 * (1 - exp(-4j*k*w0))/(1 - exp(-1j*k*w0))
    ak(ligning = ak2)

class Opgave4_1(Opgave): 
    t, omega = symbols("t omega")
    resultat_frekvens1 = exp(-4)*integrate(exp(t*(2-1j*omega)), (t, -oo, 1))
    resultat_frekvens2 = integrate(exp(2)*exp(t*(-2-1j*omega)), (t, 1, oo))
    # Xjw = frekvens1.doit()
    # resultat_Xjwnum = Xjw

class Opgave4_4(Opgave):
    t, w = symbols("t omega")
    res_x2t = (1/(2*pi)) * ( integrate(-2*exp(1j*w*t), (w, -2, 0), conds="separate") + integrate(2*exp(1j*w*t), (w, 0, 2), conds="separate"))
    pprint(res_x2t)

class Opgave4_5(Opgave): 
    a, w, w0, t = symbols("alpha omega omega0 t")
    Xjw = Function("X")(1j*w)
    Xjw1 = 1/2 * (0 - 1/(- a - 1j*w + 1j*w0) + 0 - 1/(-a -1j*w - 1j*w0))
    Xjw2 = 1/2j * (1/(3 - 1j*w + 2j) - 1/(3-1j*w - 2j) - 1/(-3 - 1j*w + 2j) + 1/(-3 - 1j*w - 2j))
    Xjw2gen = (1/2j) * (1/(a - 1j*w + 1j*w0) - 1/(a - 1j*w - 1j*w0) - 1/(-a -1j*w + 1j*w0) + 1/(-a -1j*w - 1j*w0)) # generalized e^-3|t| * sin(omega0t)
    # Af den har jeg simplificeret den til at være: 
    Xjw2gen = -(4j * a * w * w0)/(a**4 + 2* a**2 * (w0**2 + w**2) + (w**2 - w0**2)**2)
    # Den er testet og giver det samme resultat. 
    Xjw3 = (
        - integrate(exp(-1j*w*t), (t, -2, 1), conds="separate")
        + integrate(t*(exp(-1j*w*t)), (t, -1, 1), conds="separate")
        + integrate(exp(-1j*w*t), (t, 1, 2), conds="separate") )  
    
    eq3 = Eq(Xjw, Xjw3) 
    pprint(simplify(eq3))
    #pprint(expand(simplify(integrate(-t * exp(-1j*w*t), (t, -1, 1), conds = 'separate'))))
    #eq3 = Eq(Xjw, Xjw2gen) 
    # pprint(simplify(eq3.subs([(a, 3), (w0, 2)])))

class Opgave4_22(Opgave):
    t, w = symbols("t omega")
    funktioner = [((-3, -2), (   -1)),
                  ((-2, -1), (t + 1)),
                  (( 1,  2), (t - 1)), 
                  (( 2,  3), (    1))]
    xt = lambda t, w, funktioner : [1/(2*pi) * integrate(Xjw * exp(1j*w*t), (w, g[0], g[1]), conds= "separate") for (g, Xjw) in funktioner]
    
    xt1 = xt(t, w, funktioner)[0]
    pprint(xt1.rewrite(cos))

class Opgave4_26(Opgave):
    w = symbols("w")
    b = 1 
    poler = ((2 + 1j*w)**2) * ((4 + 1j*w) **2)
    poler = collect(expand(poler), w) 
    a = [1, -12, -52, 96, 64]
    pprint(poler)
    
    
    r, p, k = sig.residue(b, a)
    sig.residue
    res_r = r
    res_p = p
    res_k = k

class Eksempel_kapitel4(Opgave):
    t, f = symbols("t f", real = True, variable = True)
    a, b = symbols("a b", real = True, positive = True, constant = True)
    ft = lambda x, t, f: fourier_transform(x, t, f) 
    ift = lambda x, t, f: inverse_fourier_transform(x, f, t, noconds = True)

    # Fourier requires heaviside, not t > 0. 
    xt = exp(-b*t) * Heaviside(t)
    ht = exp(-a*t) * Heaviside(t)
    Yjw = ft(xt, t, f) * ft(ht, t, f)
    A, Yjw = factor_terms(apart(Yjw, f)).args
    
    # Inverse requires t > 0. Doesn't set heaviside itself.    
    t = symbols("t", real = True, variable = True, positive = True)
    yt = A * (ift(Yjw.args[0], t, f) + ift(Yjw.args[1], t, f)) # Has step function onto it, but doesn't show
    pprint(yt)
    
    
    
    
    
    
    
    
    # res_y1t = convolution(xt, ht) # Virker kun for numeriske ligninger 
    """
    res_y2t = inverse_fourier_transform(
        fourier_transform(xt, t, w).doit() * fourier_transform(ht, t, w).doit(), 
        w, t).doit()"""
    
class Opgave5_1(Opgave):
    f = np.linspace(0, 1000, 1000)
    w = 2*np.pi*f
    Xejw_mag = 4/(2 - np.exp(-1j*w)) - 2
    fig, ax = plt.subplots(2)
    ax[0].plot(w, np.abs(Xejw_mag), label = '|Xejwa|')
    Xejwb_mag = 4/(2 - np.exp(-1j*w)) - 2 + 1/(2-np.exp(1j*w)) + 1/2
    ax[1].plot(w, np.abs(Xejwb_mag), label="|Xejwb|", color = "orange")
    fig.legend()
    plt.show()
    
class Opgave5_2(Opgave): 
    fig, ax = plt.subplots(2)
    f = np.linspace(0, 1, 360)
    w = 2*np.pi*f
    Xejwa_mag = np.abs(2*np.cos(w))
    Xejwb_mag = np.abs(2*np.cos(2*w))
    ax[0].plot(w, Xejwa_mag, label = "|Xejwa|")
    ax[1].plot(w, Xejwb_mag, label = "|Xejwb|", color = "orange")
    fig.legend()
    plt.show()

class Opgave5_4(Opgave): 
    n2 = np.linspace(-2*np.pi, -0.2, 50)
    x2n = (2*np.cos(np.pi*n2) - 4)/(np.pi*n2)
    
    n1 = np.linspace(-2*np.pi, 2*np.pi, 100)
    x1n = 4*np.pi * (np.cos(np.pi/4 * n1)**2) 
    fig, ax = plt.subplots(2)
    ax[0].plot(n1, x1n, label = "x1 n", color = "blue")
    ax[1].plot(n2, x2n, color = "orange")
    
    n2 = np.linspace(0.2, 2*np.pi, 50)
    x2n = (2*np.cos(np.pi*n2) - 4)/(np.pi*n2)
    ax[1].plot(n2, x2n, label = "x2 n", color = "orange")
    fig.legend()
    plt.show()
    
class Opgave5_21(Opgave): 
    w = symbols("w", variable = True)
    k = symbols("k", integer = True, variable = True)
    # stepJw = 1/(1 - exp(-1j*w) + Sum(pi*DiracDelta(w - 2*pi*k)))
    timeShiftJw = lambda self, w, n0 : exp(-1j*w*n0)
    Xejw = Ligning(w).ligning
    Xejw(ligning = 1/(1 - exp(-1j*w)))

    Xejw1 = sin(2*w)/(sin(w/2)) * exp(1j*w/2)
    Xejw2 = 0.5/(exp(-1j*w) - 0.5)
    Xejw3 = Ligning(w, k).ligning
    Xejw3sym = 1/(1 - exp(-1j*w)/3) - exp(-1j*w)/3 - 1
    Xejw3num = -1/(3*exp(1 - 9*exp(1j*w)))
    Xejw4 = 1/(2j + exp(1j*w) * 2 * sin(pi/4))
    
    # Symmetri gjorde, at jeg kunne beskrive kompleks konjugerede som en kombination af deres udtryk.
    a = (1-1j)*sqrt(2)/2 * 1/(2*cos(pi/8) - 2j*sin(pi/8) - exp(-1j*w))
    b = (1+1j)*sqrt(2)/2 * 1/(2*cos(pi/8) + 2j*sin(pi/8) - exp(-1j*w))
    f = np.linspace(-1, 1, 100)
    f1 = np.linspace(-1, 0, 50)
    f2 = np.linspace(0, 1, 50)
    w = 2*np.pi*f
    w1 = 2*np.pi*f1
    w2 = 2*np.pi*f2
    Xejw5original= lambdify(symbols("w"), a - b)
    Xejw5konjugeret = lambdify(symbols("w"), b - a)
    # Grundet faseskift medføre det konjugeret symmetri. 
    Xejw5 = np.append(Xejw5original(w1), Xejw5konjugeret(w2))
    magnitude = np.abs(Xejw5)
    angle = np.rad2deg(np.angle(Xejw5))
    fig, ax = plt.subplots(3)
    ax[0].plot(w, Xejw5.imag)
    ax[1].plot(w, magnitude)
    ax[2].plot(w, angle)
    

    
    
    
    
    bodeplot(Xejw4)
    #pprint

class Opgave5_22(Opgave): 
    b = [-1/5, 1]
    a = [1, -1/5]
    r,p,k = sig.residuez(b, a)
    w = symbols("w")
    Xejw = r[0]/(1 - p[0]*exp(-1j*w)) + k[0]
    pprint(Xejw)

class Eksempel6_5(Opgave): 
    w = symbols("w")
    Hejw = (100 * (1 + 1j*w))/((10 + 1j * w)*(100 + 1j*w))
    bodeplot(Hejw, dB=True, wrange = (-1, 2, 1000))

class Opgave6_3(Opgave): 
    w = symbols("w")
    Hejw = (1 - 1j*w)/(1 + 1j*w)
    bodeplot(Hejw, dB = True, wrange = (-3, 1, 250))

class Opgave6_27(Opgave):
    w = symbols("w")
    Hejw = 1/(1j*w + 2)
    bodeplot(Hejw, dB=True, wrange = (-3, 1, 250))

class Opgave6_28(Opgave): 
    w = symbols("w")
    Hejw1 = 1 + (1j*w)/10
    Hejw2 = 1 - (1j*w)/10
    Hejw3 = 16/((1j*w + 2)**4)
    Hejw4 = (1-(1j*w)/10)/(1 + 1j*w)
    bodeplot([Hejw1, Hejw2, Hejw3, Hejw4], dB = True, wrange = (-2, 2, 250))
opg = Opgave5_22()
