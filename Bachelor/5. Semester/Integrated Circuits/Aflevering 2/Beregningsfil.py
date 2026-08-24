from Formelsamling.StudieHjaelp import Opgave
from sympy import * 
import scipy.signal as sig
Vgs, lamb, Vds = symbols('Vgs lamb Vds')

class Opgave3(Opgave):
    eq = 1/2*110e-6 *(Vgs - 0.73)**2 *(1 + lamb*Vds) - 100e-6
    res_VGS = solve(eq, Vgs)
    
class Opgave4(Opgave):
    VGG, lamb = symbols("V_GG lambda")
    r, p, k = sig.residue([1, -1.46, 0.5329], [1, -11.76, 32.8329])
    resultat_r = r
    resultat_p = p
    resultat_k = k
    resultat_partial_fraction = r[0]/(VGG - p[0]) + r[1]/(VGG - p[1]) + k[0]
    # pprint(resultat_partial_fraction)
    eq = 4.4*(VGG**4) - 58.16803*(VGG**3) + 245.8003 * (VGG**2) - 262.4219*VGG + 57.17884 
    # eq = (VGG + 0.5329 - 1.46 * VGG)*(4.4 + 11*lamb) + 220/9 * (VGG**2 - 1.46*VGG + 0.5329)/(VGG**2 - 11.76 * VGG + 32.8329) - 1
    res_VGS = solve(eq, VGG)
    pprint("="*80)
    pprint("\nSolutions for V_GG:\n")
    for sol in res_VGS: 
        pprint(sol)
    pprint("="*80)