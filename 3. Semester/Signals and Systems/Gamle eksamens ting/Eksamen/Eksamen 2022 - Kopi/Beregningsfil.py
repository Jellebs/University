import numpy as np
from sympy import * 
import matplotlib.pyplot as plt
from Uni.Formelsamling.SignalerOgSystemer import kontinuertTidsFourierSerie as CTFS 
from Uni.Formelsamling.Elektriske_Kredsløb import filter_bodePlot as bp
from Uni.Vaerktoejer import visOpgave
def opgave2(): 
    def ak_fun(k): 
        # Eksempel funktion 
        if (k == 0): return 1
        koeffs = complex(1/(k*np.pi) * sin(k*np.pi/2))
        return koeffs
        # Rigtig funktion
        # if (k == 0): return 0.125
        # if (k % 2 == 0): return np.round(complex((np.cos(k*np.pi/2) - 1)/(9.87*(k**2)) + 1j/(2*np.pi)), 4) # Even
        # if (k % 2 == 1): return np.round(complex(-1/(9.87 * (k**2)) - 1j*(sin(-k*np.pi/2)/(9.87*(k**2)) - 1/(2*np.pi))), 4) # Odd


    ctfs = CTFS()
    T = (0, 4)
    omega0 = (2*np.pi)/(T[1] - T[0]) # = π/2 
    t = np.linspace(-T[1], T[1], 100, dtype= complex)
    antalKoefficienter = [1, 12, 30] 
    koefficienter = ctfs.findKoefficienter(ak_fun, max(antalKoefficienter))
    xt = lambda t, T1, T2: (t < T1).astype(float)*(-t) - (t < 0).astype(float)*(-t) + (T1 < t).astype(float) - (t > T2).astype(float)
    xt = xt(t, 1, 2)
    xhat = ctfs.approksimer(t = t, antalKoefficienter= antalKoefficienter, omega0 = omega0, ak= ak_fun)

    ctfs.plot(ak = koefficienter, x_approksimationer = xhat, tInt=t)

def opgave3(): 
    def delopgaveab(): 
        frekvens = np.logspace(-1, 2, 100)
        h = np.real(1/(1j*frekvens + 3))
        bp(h, "Frequency response", frekvens)
    
    def delopgavec(): 
        def F(eq, t, s): 
            eq_lp = laplace_transform(eq, t, s, noconds = True)
            return eq_lp
        
        def invF(eq, t, s): 
            return inverse_laplace_transform(eq, s, t, noconds = True)
        
        s, t = symbols("s t")
        y = Function('y') 
        eq = y(t).diff(t) + 3*y(t) - exp(-t) # dy/dt + 3y = x
        eq_lp = F(eq, t, s)
        eq_lpy = solve(eq_lp, LaplaceTransform(y(t), t, s)) # lp(y) = ?
        eq_lpy = eq_lpy[0].subs({y(0): 0}) # y(0) = 0
        pprint(eq_lpy)
        eq_pfy = factor(eq_lpy, s).apart() # Partial fraction af laplace(y)
        y = invF(eq_pfy, t, s)
    delopgavec()

def opgave5(): 
    def F(eq, t, s): 
        eq_lp = laplace_transform(eq, t, s, noconds = True)
        return eq_lp
    
    def invF(eq, t, s): 
        return inverse_laplace_transform(eq, s, t, noconds = True)
    
    s, t = symbols("s t")
    y = Function('y') 
    x = Function('x')
    eq = y(t).diff(t, 2) - 3*y(t).diff(t) - 4*y(t) - (x(t).diff(t) - x(t)) # y'' - 3y' - 4y - x' + x = 0
    eq_lp = F(eq, t, s)
    eq_lpy = solve(eq_lp, LaplaceTransform(y(t), t, s))[0] # lp(y) = ...
    eq_lpx = solve(eq_lp, LaplaceTransform(x(t), t, s))[0]
    lpTf = lambda v: LaplaceTransform(v, t, s)
    eq_pfy = ((3*lpTf(x) + 4*y(0) - x(0) -3*y(0) + y.diff(t))/5) * (1/(s-4)) + (2*lpTf(x) + 4*y(0)+x(0)-y.diff(t))*(1/(s+1)) 
    eq_pfx = (((s-2) * lpTf(y)*(s**2 - 3*s-4) - s*y(0)+ x(0) + 3*y(0)-y.diff(t))* (1/(s-2))  + (s+2)*(lpTf(y)*(s**2 - 3*s - 4) - s*y(0) + x(0) + 3*y(0) - y.diff(t)) * (1/(s-1)))
    eq_pfh = eq_pfy/eq_pfx
    pprint(eq_pfh)
    # pprint(factor(eq_lpy))
    # pprint(factor(eq_lpx))
    # eq_lph = expand(eq_lpy/eq_lpx).apart(s)
    # pprint(eq_pfy.apart())
# opgave3()
opgave5()


