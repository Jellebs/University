from sympy import * 
import numpy as np
from Uni.Formelsamling.SignalerOgSystemer import kontinuertTidsFourierSerie as ctfs
from Uni.Formelsamling.Elektriske_Kredsløb import filter_bodePlot as bp 

def opgave4():
    def delA():
        f = np.logspace(-1, 1, 100)
        h = 1/(10+5j*f)
        bp(h, "Magnitude", "Frequency", f)
    def delB(): 
        omega = np.logspace(-1, 1, 100) * 2*np.pi
        H = (1+ 0.5 * np.exp(-1j*omega)) / (1 - 0.5 * np.exp(-1j*omega))
        H_mag = np.abs(H)
        H_ang = np.angle(H)
        pprint(H_mag)
        pprint(H_ang)
    delB()

def opgave3(): 
    
opgave3()
    '''def F(eq, t, s): 
        eq_lp = laplace_transform(eq, t, s, noconds = True)
        return eq_lp
    
    def invF(eq, t, s): 
        return inverse_laplace_transform(eq, s, t, noconds = True)
    
    x = Function('x')
    y = Function('y')
    s, t = symbols('s t')
    eq = 5*(y(t).diff(t)) + 10*y(t) - x(t) # = 0 
    eq_lp = F(eq, t, s)
    lptf = lambda v: LaplaceTransform(v, t, s)
    # eq_lph = solve(eq_lp, (lptf(y(t))/lptf(x(t)))) 
    pprint(eq_lp)
    '''


opgave4()