from sympy import * 
import numpy as np
from Formelsamling.Numerisk_Lineær_Algebra import *

def opgave1(): 
    def findPlan(p1, p2, p3):
        x, y, z = symbols("x y z")
        p12 = p1-p2
        p13 = p1-p3 
        nP = np.cross(p12, p13) # normal vektor.
        return nP, nP[0]*(x - p1[0]) + nP[1]*(y-p1[1]) + nP[2]*(z - p1[2])

    p1 = np.array([0, 1, 0], dtype= float) 
    p2 = np.array([1, 0, 0], dtype= float) 
    p3 = np.array([1, 1, 1], dtype= float)

    nP1, P1 = findPlan(p1, p2, p3)
    punkter = np.array([[0, 1, 1], 
                        [0, 1, 0], 
                        [0, 0, 1]], dtype = float) 
    # (x, x, x), 
    # (y, y, y), 
    # (z, z, z)
    nP2, P2 = findPlan(punkter[:, 0], punkter[:, 1], punkter[:, 2])
    v = np.degrees(np.arccos(findVinklen(nP1, nP2)[0]))
    print(v)

def opgave2():
    k, t = symbols("k t")
    x = 3*cos(t)
    y = 3*sin(t)
    z = 4*t    
    ds = 5 # dt
    m = k*integrate(z * ds, (t, 0, pi))
    print(m)

    def findMMPTilKomponent(komponentLigning, m):
        ds = 5
        return 1/m* k * integrate(komponentLigning * z * ds, (t, 0, pi))
    x_mmp = findMMPTilKomponent(x, m)
    y_mmp = findMMPTilKomponent(y, m)
    z_mmp = findMMPTilKomponent(z, m)
    print(x_mmp, y_mmp, z_mmp, sep = "\n")

def opgave3(): 
    x, y = symbols("x y")
    T1 = Matrix([1, 0, -x/sqrt(1 - x**2 - y**2)])
    T2 = Matrix([0, 1, -y/sqrt(1 - x**2 - y**2)])
    dA = T1.cross(T2)
    print(dA)

def opgave4():
    

opgave4()