import sympy as sp 

c, s, r = sp.symbols("c s r")
expres1 = r + 1/(c*s + 1/(2*r + 2/(c*s)))
rational_func = sp.cancel(expres1) # Lav til rational 
rational_func_pol = 2*c**2*r**2*s**2 + 5*c*r*s + 2
nulpunkt = sp.solve(rational_func_pol, s)

expres2 = r + 1/((c*s)/2+ 1/(2*r + 1/(c*s)))
rational_func = sp.cancel(expres2)

sp.pprint(rational_func)
rational_func_nulpunkt = 2*c**2*r*s**2 + 3*c*s

