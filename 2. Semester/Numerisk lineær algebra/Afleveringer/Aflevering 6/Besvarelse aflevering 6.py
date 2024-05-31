import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Head, NoEscape, Subsubsection
from pylatex.utils import italic
from Formelsamling.Numerisk_Lineær_Algebra import *

geometry_options = {"tmargin": "1cm", "lmargin": "2cm"}
doc = Document(geometry_options=geometry_options)

with doc.create(Section('Aflevering 6', False)): 
    doc.append(italic('Af Jesper Bertelsen'))
    '''
    with doc.create(Subsection('Opgave a. Betragt rummet af differentiable funktioner', False)):
        doc.append(Subsection(NoEscape(r'$$f: [0,\pi] -> \mathbb{R} $$'), False))
        doc.append(Subsection(NoEscape(r'med det $$L^2 \text{indre produkt}$$'), False))
        doc.append(Subsection(NoEscape(r'$$ <f, g> = \[ \int_{0}^{\pi} x^2 \,dx \]$$'), False)):
        doc.append('I python tjekkes det med sympy.')
        doc.append('En arbitrer k værdi vælges til 20')
        doc.append('Integralet af ')
    '''
    #with doc.create(Subsubsection(NoEscape(r'a. Vis at samlingen bestående af funktionerne \n $$ sin(x), sin(2x),...sin((k-1)x)$$ \n defineret for $$ x \in [0,\pi] $$ er ortogonal for dette indre produkt. (Trigonometriske identiter findes i notesættes afsnit 9.6; computeralgebra systemer, kan eventuelt bruges for udregninger.'), False)): 
    
def projektionPå(u, v): 
    return np.vdot(u, v)/np.vdot(v, v) * v

def opgaver(opgave):
    x, k1, k2= sp.symbols("x k1 k2")
    match opgave: 
        case 'a':
            expres = (sp.sin(k1*x)*sp.sin(k2*x)) 
            prikProdukt = sp.integrate(expres, (x, 0, sp.pi), conds= "separate")
            integral = -k1*sp.sin(sp.pi*k2)*sp.cos(sp.pi*k1)/(k1**2 - k2**2) + k2*sp.sin(sp.pi*k1)*sp.cos(sp.pi*k2)/(k1**2 - k2**2)
            print(prikProdukt)
        case 'b': 
            expres = 1 * sp.sin()
            print()
    # Der ses at begge led afhænger af sin. Sin til vilkårligt antal hele pi er 0. 
    




def tjekForOrtogonalitet(k, opgave):
    x, y = sp.symbols('x y')
    for i in range(k-1): 
        match opgave: 
            case 'a': 
                for j in range(k-1): 
                    if i == j: continue; 
                    print(sp.integrate(sp.sin((i+1) * x) * sp.sin((j+1) * x), (x, 0, sp.pi)))
            case 'b':
                print(f"i = {i+1}, resultat = {sp.integrate((1 * sp.sin((i+1)*x)), (x, 0, sp.pi))}")

def indre_produkt(f, g, h): # Integralet af summen af f * g 
    return np.trapz(f*g, dx=h) 

def norm_sq(f, h): 
    return indre_produkt(f, f, h) 

def proj(f, konstantfunktion, k, x, h, gx = False): # k er antal halve udsving per pi.
    out = np.zeros_like(x)
    if gx == False:
        for m in range(1, k+1): 
            out += (indre_produkt(f, np.sin(m*x), h) 
                / norm_sq(np.sin(m*x), h)
                * np.sin(m*x))
    else: 
        g = konstantfunktion + 2/np.pi/2 * np.sin(x) + 4/(3*np.pi) * np.sin(3*x) # 1 + c1sin(x) + c3sin(3x)
        out += (indre_produkt(f, g, h) 
                / norm_sq(g, h)
                * g)
        
    return out


def approksimer(k, opgave): 
    x, h = np.linspace(0, np.pi, 100, retstep=True)
    konstant = np.ones_like(x)
    match opgave: 
        case 'd': 
            f = 1-np.exp(-x)
            konstant = np.ones_like(x)
            fig, ax = plt.subplots()
            ax.plot(x, f, label = "f(x)")
            projektion_samling = proj(f, konstant, 5, x, h, gx = True)
            projektion_samling = proj(f, konstant, 4, x, h)
            ax.plot(x, projektion_samling, label = "Approksimeret funktion")
            ax.legend()
            
opgaver('a')
k = 20
#tjekForOrtogonalitet(k, opgave='a')
#tjekForOrtogonalitet(k, opgave='b')
approksimer(k, opgave='d')


