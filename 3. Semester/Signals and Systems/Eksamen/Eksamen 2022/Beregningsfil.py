from sympy import *
import scipy.signal as sig 
from Uni.Formelsamling.Opgaver import * 
from Uni.Formelsamling.SignalerOgSystemer import diskretTid as DT
from Uni.Vaerktoejer.Plots import * 
import numpy as np

I = lambda f, T : integrate(f, (T))
t = symbols("t")
d = lambda f, x, n : diff(f(x), x, n)
a = lambda k, w: 0.25*(
    I(-t*cos(-k*w*t),    (t, 0, 1)) +
    I(-t*1j*sin(-k*w*t), (t, 0, 1)) + 
    I(cos(-k*w*t),       (t, 1, 2)) + 
    I(1j*sin(-k*w*t),    (t, 1, 2)))


class Opgave2(Opgave): 
    t = symbols('t')
    T = 4
    np.set_printoptions(formatter={'complex_kind': '{:.2f}'.format})
    ak = lambda k, t: I(-t*exp(-1j*k*np.pi/2*t), (t, 0, 1)) + I(*exp(-1j*k*np.pi/2*t), (t, 1, 2))
    resultat_a = np.array([N(I(-t*exp(-1j*k*pi/2*t), (t, 0, 1)) + I(exp(-1j*k*pi/2*t), (t, 1, 2)), 3) for k in np.arange(-3, 4, 1)], dtype = complex)
    resultat_xt = N(sum(resultat_a*np.array([exp(1j*k*2*pi*t) for k in range(-3, 4)])), 2)

class Opgave3(Opgave):
    omega = np.logspace(-1, 1, 50)
    
    s = 1j*omega 
    H = np.abs(1/(s + 3))[:, np.newaxis]
    Hdb = 20*np.log10(H)
    plots = Plots()
    
    plots.config.legends = ["|H(jw)|", "|H(jw)|db"]
    plots.xy = (omega, np.hstack([H, Hdb]))
    
    r, p, k = sig.residue([1], [1, 4, 3]) 
    print(r, p, k)


class Opgave4(Opgave): 
    # Delopgave a 
    plots = Plots()
    plots.config.currentPlotFunction = "stairs"
    plots.config.legends = ["x[n]", "h[n]"]
    n = np.arange(0, 6, 1)
    xn = np.array([1, 1, 1, 0, 0])[:, np.newaxis]
    hn = np.array([2, 2, 2, 2, 2])[:, np.newaxis]
    plots.xy = n, np.hstack([xn, hn])

    resultat_xnhn = xn * hn.T
    n = np.arange(0, 8, 1)
    yn = np.array([2, 4, 6, 6, 6, 4, 2])
    plots.xy = n, yn

    # Delopgave b 
    plots.config.currentPlotFunction = "step"
    plots.config.legends = ["x(t)", "h(t)"]
    t = np.arange(-1, 7, 1)
    xt = np.array([0, 0, 1, 1, 1, 0, 0, 0])[:, np.newaxis]
    ht = np.array([0, 0, 1, 1, 1, 1, 1, 0])[:, np.newaxis]
    plots.xy = t, np.hstack([xt, ht])
    
    t = np.arange(-1, 10, 1)
    yt = lambda t : np.array([
        i     if i >= 0 and i < 3 else 
        3     if i >= 3 and i < 5 else 
        8 - i if i >= 5 and i <= 8 else 
        0 
        for i in t])
    
    plots.config.currentPlotFunction = "plot"
    plots.config.legends = ["y(t)"]
    plots.xy = t, yt(t)

class Opgave5(Opgave):
   DT.zplane([1, -1], [1, -3, 0], r = 5)


    




# opg2 = Opgave2()
opg3 = Opgave3()
# opg4 = Opgave4()
# opg5 = Opgave5()     
