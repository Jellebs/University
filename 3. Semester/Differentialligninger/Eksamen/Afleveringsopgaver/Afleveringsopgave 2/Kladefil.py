import numpy as np 
from sympy import * 
from Formelsamling.Numerisk_Lineær_Algebra import *
init_printing(wrap_line=True)

def customPrint(eq): 
    print("\n")
    pprint(eq)
    print("\n")


def opgave1(): 
    r, x = symbols("r x")
    eq = r**3 + 3*(r**2) - 4
    sol = roots(eq,multiple=True)
    for loesning in sol: 
        pprint(loesning)
    
    Ab = np.array([
        [1,  1,   1, 13/4],
        [1, -2,   1,    2], 
        [1,  4,  -4,    1]])
    A = Ab[:, 0:3]
    b = Ab[:, 3]
    sol = np.linalg.solve(A, b)
    print(sol)
    print("\n")
    y = 160/75*exp(x) + 15/36*exp(-2*x) +7/10*x*exp(-2*x) - x - 1/4
    eq = diff(y, (x, 3)) + 3*diff(y, (x, 2)) - 4*y
    pprint(eq)

# opgave1()

def opgave2(): 
    A, B, t = symbols("A B t")
    x_par = A*cos(t)+B*sin(t)
    def xdiff(order): 
        return diff(x_par, (t, order))

    eq = xdiff(2) + 3 * xdiff(1) + 2 * x_par
    customPrint(simplify(eq))

    
    def testloesning(): 
        x_t = -6/10 * exp(-2*t) + 15/10 * exp(-1*t) + 1/10*cos(t) + 3/10 * sin(t)
        def xdiff(order): 
            return diff(x_t, (t, order))  
        
        iEq = xdiff(2) + 3 * xdiff(1) + 2 * x_t
        customPrint(N(iEq, 4))

    testloesning()

def opgave3(): 
    r = symbols("r")
    eq = r**3 - 3*r**2 + 3*r - 1
    customPrint(roots(eq))
    


    

opgave1()
