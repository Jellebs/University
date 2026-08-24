import numpy as np 
from sympy import *
from Formelsamling.Numerisk_Lineær_Algebra import *

# Opgave 8.1 betragt to vektorer reel^3 

u = np.array([1, -1, 1], dtype= float)
v = np.array([-1, -2, 1], dtype= float)

a = 7*u[0]*v[0] + 2*u[1]*v[1] + 3*u[2]*v[2]; print(a) # = 0. I dette indre produkt er u & v vinkelrette på hinanden.

w = np.array([1, 0, 0])

def projPå(v, u): 
    return np.vdot(v, u) / np.vdot(v, v) * v

# Beregn projektion af w på u og v. 
# Er sådan jeg forstår spørgsmålet

proj_w1 = projPå(u, w); print(proj_w1)
proj_w2 = projPå(v, w); print(proj_w2)

# Skriv formlen på formen x.T*Ay 

A = Matrix([[7, 0, 0],
            [0, 2, 0],
            [0, 0, 3]])

x0, x1, x2 = symbols('x0 x1 x2')
y0, y1, y2 = symbols('y0 y1 y2')

y = Matrix([y0, y1, y2])
x = Matrix([x0, x1, x2])
resultat = x.T @ A @ y; print(resultat)

# Opgave 8.2 Brug rækkeoperationer til at afgøre hvilke af de følgende samlinger vektorer er lineært uafhængig i de givne vektorrum: 
# Note før start. For at samlingerne af vektorer er lineært uafhængige, kræver det, at hver søjle har et pivotelement. 

a = np.array([[1, 0, 0], 
              [1, 1, 0],
              [1, 1, 1]], dtype= float)

b = np.array([[1, 1, 0], 
              [1, 0, 1], 
              [0, 1, 1]], dtype= float)

c = np.array([[1, -1, 0], 
              [-1, 0, 1], 
              [0, 1, -1]], dtype= float)

d = np.array([[1.0        ,       1.0j, 1.0 + 1.0j],
              [       1.0j, 1.0 - 1.0j, 1.0       ],  
              [-1.0 + 1.0j, 1.0       ,       1.0j]])


lægTil(a, 1, -1, 0)
lægTil(a, 2, -1, 0)
lægTil(a, 2, -1, 1); print(a) # Echelon form √

skift(b, 0, 1)
lægTil(b, 1, -1, 0)
lægTil(b, 2, -1, 1)
skaler(b, 1/2, 2); print(b) # Echelon form √

lægTil(c, 1, 1, 2)
lægTil(c, 1, 1, 0); print(c) # Echelon form % 

# Opgave 8.3. Betragt matricerne A & B givet ved 
A = np.array([[6,  0],
              [0, -3]], dtype= float)

B = np.array([[ 1,  2],
              [-1, -2]], dtype= float)


# a. Bestem Frobeniusnormerne ||A||F & ||B||F
#    Angiv værdierne af det indre produkt A & B
#    Bekræft at Cauchy-Schwarz uligheden er opfyldt i dette tilfælde. ||A||**2||B||**2 <= ||A||**2 + ||B||**2, eller også er det omvendt.
#    Beregn vinklen mellem A & B 


#Opgve 8.4. Betragt funktionen 

# f = 4/(4+x**2)

# Beregn tilnærmelse med højre orienteret / venstre orienteret. Et billede af forskellen på disse to er vist som billede.

x, h = np.linspace(-2, 2, 5, retstep= True) 

f = 4/(4+x**2)

def tilnærmelse(f, h, højreorienteret: bool): 
    if højreorienteret: 
        return h * np.sum(f[1:])
    return h * np.sum(f[:-1])

print(tilnærmelse(f, h, højreorienteret=True))
#                   == 
print(tilnærmelse(f, h, højreorienteret=False))