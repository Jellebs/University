from Formelsamling.StudieHjaelp import Opgave
from sympy import * 
import numpy as np
from sympy import Abs
init_printing()

def printEquation(eqs, navne):
    print("="*80)
    for eq, navn in zip(eqs, navne):
        pprint(Eq(symbols(navn), eq))
    print("="*80)

def parallel(impedances): 
    return 1/(np.sum([1/impedance for impedance in impedances]))
    


class Opgave2(Opgave): 
    rO1, rO2, rO3, rO4 = symbols("r_O1 r_O2 r_O3 rO4")
    gm1, gm2, gm3, gm4 = symbols("g_m1 g_m2 g_m3 g_m4")
    gmb1, gmb2, gmb3, gmb4 = symbols("g_mb1 g_mb2 g_mb3 g_mb4")
    
    iout, iT, VT, Va, Ve, Vc, Vd = symbols("iOut iT VT VA VE VC VD")

    eq1 = iT - gm3*(VT - Ve) - (VT - Ve)/rO3 - gmb3 *(-Ve) 
    eq2 = Ve*(gm1 + 1/rO1)
    eq3 = iout - gm4*(VT - Vd) - (-Vd)/rO4 - gmb4*(-Vd)
    eq4 = iout - gm2*Ve - Vd/rO2

    VD = solve(eq4, Vd)[0]
    VE = solve(eq3.subs(Vd, VD), Ve)[0]
    iOut = solve(eq2.subs(Ve, VE), iout)[0]
    # printEquation([VD, VE, iOut], ["VD", "VE", "iOut"])
    Rin = collect(eq1.subs(Ve, VE).subs(iout, iOut), [iT, VT])
    vt = Rin.coeff(VT)
    it = Rin.coeff(iT)
    Rin = -1/(vt) # aVT + 1*iT => -1/a = VT/IT
    Rin = simplify(Rin)
    # printEquation([Rin], ["Rin"])
    
class Opgave3(Opgave):
    Vthp = -0.88 
    Isd = 100e-6
    k4 = 1e-3/2 * 36 * 1
    lamb = 0.13e-6
    Vsg = symbols("Vsg")
    eq1 = Eq(Abs(Vthp**2) + Isd/k4, Vsg*(Vsg*(1 + lamb*Vsg) - Abs(Vthp**2)))
    res_VSG = solve(eq1, Vsg)[2]
    Vout = symbols("Vout")
    k3 = k4
    res_eq2 = Eq(Isd, k3 * ( (res_VSG - Abs(Vthp))**2 )*( 1 + lamb * (5-Vout)))
    res_Vout = solve(eq2, Vout)
 
    
    
    
    

class Opgave5(Opgave): 
    rO0, rO1, rO2, rO3, RD, gm1, gm2, gmb1, gmb2 = symbols("rO0:4 RD gm1:3 gmb1:3")   
   
    R0 = rO0
    R1 = (1 + rO3/rO1)/(gm1 + gmb1 + 1/rO1)
    
    RT = parallel([
        rO2 * (1 + (parallel([R0, R1])) * (gm2 + gmb2 + 1/rO2)),
        RD])
    GM = gm1/(1 + 1/(rO0*(gm1 + gmb1)))
    Av = GM*RT
    # printEquation([simplify(Av)], ["Av"])
    
    Av = 1e3 * gm1/(2+gm1*2e3)
    Vgs = symbols("VGS")
    res_AV = Av
    res_VGS = Av.subs([(gm1, 0.008*Vgs - 0.0032)])
    
    
    
    
    

class Opgave6(Opgave):
    r2, R1, R2,  Zc1, Zc2, gm0, gm1, gm2 = symbols("r2 R1:3 Zc1:3 gm0:3")
    
    Z1 = Zc1 + R1
    Z2 = Zc2 + R2
    Zp = R2/(gm2 * (R2 + Zc2)) 
    s, C1, C2 = symbols("s C1:3")  
    
    Zout = parallel([Z1, Z2, Zp])
    Gm = gm0/2
    res_Av = -Gm*Zout
    res_Av = expand(res_Av.subs([(Zc1, 1/(s*C1)), (Zc2, 1/(s*C2))]))

    # res_poler = solve(res_Av.as_numer_denom()[1], s) 
    
    # res_poler = solve(res_Av.as_numer_denom()[1])
    
    # res_poler = solve(res_Zout.as_numer_denom()[1], s)
    
    
    # res_Zout = fraction(res_Zout)
    # res_Zout = factor(res_Zout, s)
    








Opgave5()