from sympy import * 
from Uni.Formelsamling.Opgaver import Opgave
from Uni.Formelsamling.Vectoranalyse import beregnFluxAfFirkant
from sympy.core.numbers import Zero as sympyTjekNul
from sympy.core.numbers import One as sympyTjekEt 
from sympy.core import numbers


I = lambda f, g = "(x, 0, 2)" : integrate(f, g)
II = lambda f, g = "[(x, 0, 2), (y, 0, 1)" : I(I(f, g[0]), g[1])
d = lambda f, v : diff(f, v)

class Opgave1(Opgave): 
    # Calculate line integral
    t = symbols("t")
    F = Matrix([[4*cos(t)*(sin(t)**2)],
                [4*(cos(t)**2)*sin(t)],
                [0.5 * (cos(t)**2)*(sin(t)**2)]])
    dr = Matrix([[-sin(t), cos(t), 0]])
    
    resultat_linjeIntegral = I(F.dot(dr), (t, 0, 2*pi))

class Opgave2(Opgave):
    z, t = symbols("z t")
    # Beregn overflade integralet 
    F = Matrix([[3*sqrt(1-z**2) * cos(t)], 
                [2*sqrt(1-z**2) * sin(t)], 
                [                     -z]])
    S = Matrix([[sqrt(1-z**2) * cos(t)],
                [sqrt(1-z**2) * sin(t)], 
                [                    z]])
    St = d(S, t)
    Sz = d(S, z)
    dSvec = St.cross(Sz)
    dSvec[2] = z # sin^2 + cos^2 = 1
    dS = dSvec.dot(dSvec)
    resultat_flux = II(F.dot(dSvec), [(t, 0, 2*pi), (z, -1, 1)])

    # resultat_St = 

class Opgave3(Opgave): 
    x, y, z, t,  R = symbols("x y z t R")
    psi = ln(x**2 + y**2 + z**2)
    resultat_nablaPsi = Matrix([[d(psi, x)],
                                [d(psi, y)], 
                                [d(psi, z)]])
    r = Matrix([[sqrt(R**2 - z**2)*cos(t)],
                [sqrt(R**2 - z**2)*sin(t)], 
                [                       z] ])
    
    nabla_psi = Matrix([[(2*sqrt(R**2 - z**2)*cos(t))/(R**2)],
                        [(2*sqrt(R**2 - z**2)*sin(t))/(R**2)],
                        [                       (2*z)/(R**2)]]) # Simplificeret udtryk 
    
    resultat_flux = II(nabla_psi.dot(d(r, t).cross(d(r, z))), [(t, 0, 2*pi), (z, -R, R)])

class Opgave5(Opgave):
    # Til beregning flux til alle 6 sider. 
    x, y, z = symbols("x y z")     
    F = (1/3) * Matrix([[x**2],
                        [y**2],
                        [z**2]])
    graenser = Matrix([[        0, (y, 0, 1), (z, 0, 1)],
                       [(x, 0, 1),         0, (z, 0, 1)],
                       [        1, (y, 0, 1), (z, 0, 1)],
                       [(x, 0, 1), (y, 0, 1),         0],
                       [(x, 0, 1),         1, (z, 0, 1)], 
                       [(x, 0, 1), (y, 0, 1),         1]])
    n = Matrix([[-1,  0,  0],
                [ 0, -1,  0],
                [ 1,  0,  0],
                [ 0,  0, -1],
                [ 0,  1,  0], 
                [ 0,  0,  1]]) # x y z     
    resultat_Si = beregnFluxAfFirkant(F, n, x, y, z, graenser) # Eget script jeg har lavet til tilfældet.
    resultat_S = sum(resultat_Si)

    
    


    



# opg1 = Opgave1()
# opg2 = Opgave2()
# opg3 = Opgave3()
opg5 = Opgave5()