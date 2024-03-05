from scipy import signal
from sympy import *

def opgave2_17(): 
    w, n = symbols(('omega n'))
    ts = lambda k : exp(-k*1j*w)
    Yejw = 0.18 + 0.1*ts(1) + 0.3*ts(2) + 0.1*ts(3) + 0.18*ts(4)
    Xejw = 1 + 1.15*ts(1)+ 1.5*ts(2) - 0.7*ts(3) + 0.25*ts(4)
    def findPartialFraction(num, den):
        tri = den.rewrite(cos)
        poler = solve(tri, w)
        pprint(poler)
    # findPartialFraction(Yejw, Xejw)
    

    pprint(Xejw) 
    a, b, c, d = symbols("a b c d")
    eq2 = (a + exp(-1j*w)) * (b + exp(-1j*w)) * (c + exp(-1j*w)) * (d + exp(-1j*w)) 
    
    eq2 = expand(eq2)
    # eq2 = factor(eq2, exp(-1j*w))
    # For simpelhedens skyld, så er der to summer med samme faktor. Jeg dividerer det fra. Jeg tager måske nogle antagelser på vejen, men kan ikke lige huske dem på stående fod.

    eq3 = a+b+c+d - 1 # = 0 
    eq4 = (a*b*c + a*b*d +  a*c*d + b*c*d) - 1.15 # exp(-1jw)
    eq5 = (a*b + a*c + a*d + b*c + b * d + c * d) - 1.5 # exp(-2jw)
    eq6 = (a + b + c + d) - 0.7 # exp(-3jw)
    
    aVal = solve(eq3, a)[0]
    eq4 = eq4.subs(a, aVal)
    # pprint(eq4)
    bVal = solve(eq4, b)[0]
    pprint(bVal)
    eq6 = eq6.subs(b, bVal)
    cVal = solve(eq6, c)
    pprint(cVal)
    # pprint(eq5)
    # bVal = solve(eq5, b) 
    # pprint(bVal)

    # eq5.subs(Symbol("a"), a)
    # pprint(eq5)

    # sol = solve([eq3, eq4, eq5, eq6], [a, b, c, d] dict=True)
    # pprint(sol)


    # a, b, c, d, e, f = symbols("a b c d e f", real = True) 
    # eq = Eq((a + exp(-1j*w)) * (b + exp(-1j*w)) * (c + exp(-1j*w)) * (d + exp(-1j*w)), Xejw)
    # (a*e^-2jw + be^-jw + c) * (de^-2jw + ee^-jw + f )    To kvadratiske funktioner
    #eq = (c + b*exp(-1j*w) + a*exp(-2j*w)) * (f + e*exp(-1j*w) + d * exp(-2j*w)) - Xejw
    #eq = eq.rewrite(cos) # sol = solve(eq, [a, b, c, d])
    # pprint(eq)
    #sol = solve(eq)
    # sol = solve_undetermined_coeffs(eq, [a, b, c, d])
    #pprint(sol)
    # pprint(faktoriser(Xejw, 4))
    # Hejw = Yejw/Xejw
    # hn = inverse_fourier_transform(Hejw, w, n)
    # HejwPart = apart(Hejw, extension=roots(Xejw, w, multiple=True))
    
    # pprint(HejwPart)
    
opgave2_17()