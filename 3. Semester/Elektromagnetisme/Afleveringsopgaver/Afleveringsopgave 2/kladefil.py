from sympy import *




def opgave2(): 
    a, x, e1, e2, e3 = symbols("a x e1 e2 e3") # variabler.
    mu0, I, theta = symbols("mu_0 I theta")
    Bfelt = (mu0*I)/(2* e1)
    flux = integrate(integrate(Bfelt,
                                (e1, x, x + a)),
                      (e3, 0, a))
    pprint(factor(flux))
opgave2()