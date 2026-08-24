import numpy as np
from sympy import * 
from sympy.vector import Del, curl, CoordSys3D
from dataclasses import *
import matplotlib.pyplot as plt
from Uni.Formelsamling.Opgaver import Opgave

# Beregning 
I = lambda f, graenser : integrate(f, graenser) # Integrale
II = lambda f, graenser : integrate(integrate(f, graenser[0]), graenser[1]) #  I(I(f, graenser[0]), graenser[1]) # Dobbelt integrale
d = lambda F, var : diff(F, var)
Greens2D = lambda F, x, y, graenser = "[(x, 0, 1), (y, 0, 2) ]": I(I(d(F[1], x) - d(F[0], y), graenser[0]), graenser[1]) 
Curl = lambda F, x, y, z : Matrix([[d(F[2], y) - d(F[1], z)],  [d(F[0], z) - d(F[2], x)],  [d(F[1], x) - d(F[0], y)]])
Stokes = lambda F, ds, graenser, x, y, z: I(I(    Curl(F, x, y, z).dot(ds),      graenser[0]), graenser[1]) 

@dataclass 
class Opgave():
    __beskrivelse = "" 
    @property
    def beskrivelse(self):
        return self.__beskrivelse
    
    @beskrivelse.setter
    def beskrivelse(self, nyBeskrivelse): 
        print(nyBeskrivelse);  
        self.__beskrivelse += "\n" + nyBeskrivelse
       
    def __init__(self): 
        print("\n\n")
        pprint(type(self).__name__) # Hvad hedder opgaven? 
        vars = [attr for attr in dir(self) if not attr.startswith("__") and attr.startswith("resultat")]
        resultater = {var.split("_")[1]: self.__getattribute__(var) for var in vars} # Hvilke resultater er der? 
        printOpgave(resultater)
        pass

class Opgave1(Opgave):          
    # del 1.
    beskrivelse = "Consider the two lines l and m. \n1. Argue that l and m are NOT parallel, using the cross-product."
    s, t = symbols("s t")
    l = Matrix([[ 1 + 2*t], 
                [-1 + 4*t], 
                [ 2 + 3*t]])
    m = Matrix([[ 1 -   s], 
                [ 1 + 2*s],
                [     4*s]])
    lxm = simplify(l.cross(m))
    
    # del 2. 
    beskrivelse += "\n2. Write down a function of (t,s) that outputs the square distance between a point on l and a point m and use this function to find the minimum distance between the two lines"
    def __f(t = t, s = s):
        return(sqrt(6 + 8*t + 29*(t**2)) + sqrt(2 + 2*s + 21*(s**2))) # distancen mellem de to vektorer.

    f = __f()
    nablaF = Matrix([[diff(f, t)], 
                     [diff(f, s)]])
    resultat_parallel = solve(nablaF)
    resultat_kortesteAfstand = __f(-4/29, -1/21)
    
class Opgave2(Opgave): 
    beskrivelse = "Let F be a vector Field and T be a triangle in R^2. Calculate the line integral of the vector field along the triangle"
    x, y, t= symbols("x y t") 
    F = Matrix([[exp(y)],
                [sin(pi*x)]])
    
    resultat_Sdirekte = I(I(-exp(y) + sin(pi*x), (y, 0, 1)), (x, 1, 0)) + I(I(-exp(y) - sin(pi*x), (y, 1, 0)), (x, 0, -1)) + I(2*exp(y), (x, 0, 2))
    resultat_Sgreens = Greens2D(F, x, y, [(y, 0, 1 - sqrt(x**2)), (x, 1, -1)])
    


class Opgave3(Opgave):
    
    beskrivelse = "Let F be a vector field"
    x, y, z = symbols("x y z")
    F = Matrix([y*z, 2*x*y, exp(x*y)])
    beskrivelse = F
    beskrivelse = "Does a potential function exist such that the gradient of the potential is the vector field?"
    beskrivelse = "Use Stokes theorem to evaluate the surface integral"
    ds = Matrix([0, 0, -pi])
    resultat_StokesTheoremAlgebraisk = simplify(
        Stokes(F = F,
               ds = ds,
               graenser= [(y, -sqrt(x**2 + 1 ), sqrt(x**2 + 1)), (x, -1, 1)],
               x = x, y = y, z = z))
    resultat_StokesTheoremNumerisk = N(resultat_StokesTheoremAlgebraisk.subs(z, 5), 5)  

class Opgave4(Opgave):
    x, theta = symbols("x theta") 
    F = Matrix([3*x*(cos(theta)**2), x*exp(sin(theta)), sin(theta)**3])
    nhat = Matrix([1/x, 1/cos(theta), 1/sin(theta)])
    f = x*exp(sin(theta))*cos(theta) - sin(theta)**4
    resultat_flux = II(f, [(theta, 0, 2*pi), (x, -1, 2)])
# opg1 = Opgave1()
# opg2 = Opgave2()
# opg3 = Opgave3()
opg4 = Opgave4()


