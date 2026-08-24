from sympy import *
from scipy.signal import fftconvolve 
from Uni.Formelsamling.Opgaver import *
from Uni.Vaerktoejer.Plots import * 
'''
class Opgave2(Opgave): 
    t = np.linspace(0, 10, 100)
    ht = t[:, np.newaxis]
    xt = 2*ht
    plots = Plots()
    plots.config.legends = ["x(t)", "h(t)"]
    plots.xy = (t, np.hstack([xt, ht]))

    plots.config.legends = ["x[n]", "h[n]"]
    plots.config.currentPlotFunction = "stairs"
    n = np.arange(0, 10, 1)
    xn = n[:, np.newaxis][: 9]
    hn = np.ones(n.shape)[:, np.newaxis][: 9]
    plots.xy = (n, np.hstack([xn, hn]))
    resultat_xnhn = xn * hn.T
    resultat_yn = np.array([0, 1, 3, 6, 10, 15, 21, 28, 36, 36, 35, 33, 30, 26, 21, 15, 8])
    n = np.arange(0, 18, 1)
    plots.xy = (n, resultat_yn)

t = symbols("t")
ak = lambda k : N(0.5 * integrate(exp(-1j*k*pi*t), (t, 0, 2)), 3)

class Opgave3(Opgave):
    t = np.linspace(-1, 3, 50)
    x = np.array([1 if i >= 0 and i <= 2 else 0 for i in t])
    plots = Plots()
    plots.config.legends = ["x(t)"]
    plots.config.currentPlotFunction = "stairs"
    plots.xy = (t, x[: 49])
    
    
    plots.config.currentPlotFunction = "stem"
    plots.config.legends = ["X(jw)"]
    resultat_ak = np.array([ak(k) for k in range(-5, 6)], dtype=complex)[:, np.newaxis]
    resultat_xjw = sum(np.array([ak(k)*exp(1j*k*pi*t) for k in range(-5, 6)]))
    resultat_absxjw = np.array([np.sqrt((complex(ak(k)).real **2) + (complex(ak(k)).imag ** 2)) for k in range(-5, 6)])[:, np.newaxis]
    plots.xy = (np.arange(-5, 6, 1), resultat_absxjw)
'''

class Opgave4(Opgave): 
    omega = np.linspace(0, 10, 50)
    s = 1j*omega
    Hjw = (np.exp(-s) + 1)/(2*s + 5)
    resultat_absHjwdb = 20*np.log10(abs(Hjw)) [:, np.newaxis]
    plots = Plots() 
    plots.config.legends = ["|H(jw)|dB"]
    
    plots.xy = (omega, resultat_absHjwdb) 


    # ak = 



    
# opg2 = Opgave2()
# opg3 = Opgave3()
opg4 = Opgave4()