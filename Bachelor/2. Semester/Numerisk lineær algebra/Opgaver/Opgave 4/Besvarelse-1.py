import os
import numpy as np 
import matplotlib.pyplot as plt

os.system('clear')

# Opgave 4.2 
# Omkostningerne er fundet fra tabel 5.1 om omkostninger 
# Angiv antallet af flops for de følgende matrixberegninger: 
# A = m rækker = 1000 rækker, n søjler = 70.
# B = n rækkker = 70, r søjler = 3000
# C = n rækkker = 70, r søjler = 3000
# D = r rækker = 3000, m søjler = 1000

m = 1000.0
n = 70.0
r = 3000.0

# (a) AB
#   Matrix produkt = 2mnr flops 
def flops(float_tal: float, operation: str): 
    print(f"Flops: {float_tal}, krævet til operationen: {operation}")
    
#flops(2*m*n*r, "AB")

# (b) A(B + C)
# Matrix sum = nr
# Matrixprodukt = 2mnr

#flops(n*r + 2*m*n*r, "A(B+C)")

# (c) (CD)A
# Matrixprodukt = nrm * rmn (CD) * DA 

#flops(n*r*m * r*m*n, "(CD)A")

# (d) C(DA)
# Matrixprodukt nrm(rmn)
# Tror det er forkert den måde jeg regner det på. 
# Ud fra tabellen, ser det dog ud til at være den måde man gør det på. 

#flops(n**2*r**2*m**2, "C(DA)")

# (e) A(BD)
# Samme formel som sidste, måske er der noget jeg misser. Jeg gemmer den her

# (f) 

# (g)
# De sidste 3 opgaver handler om matrix produkter opstillet med forskellige parenteser. 
# Det er tydeligt, at han vil understrege en pointe, men om den pointe er, at det er de samme flops der krævedes
# eller om jeg overser noget, og der er et forskelligt antal flops, ved jeg ikke. 


# Opgave 4.3 
# Brug elementære rækkeoperationer til at løse følgende lineære ligningssystemer: 

# [x, y],
# [x, y]
# variablen som svar kaldes for z
a_z = np.array([7.0, -2.0])[:, np.newaxis] # Søjlevektor
a = np.array([[2.0, -3.0],
              [1.0, 2.0]])
# R_0 = R_0 - 1R_1 
a[0, :] -= 1*a[1, :]
a_z[0] -= a_z[1]

# R_1 = R_1 - R_0
a[1, :] -= a[0, :]
a_z[1] -= a_z[0] 

# R_1/7

a[1, :] /= 7.0
a_z[1] /= 7.0


#y er fundet, -5y reduceres fra x
a[0][1] += 5
a_z[0] += 5*a_z[1]

#Løsning fundet x = 1.14285, y = -1.57142


b = np.array([[2.0, 1.0, -2.0],
              [1.0, -2.0, 1.0 ],
              [2.0, 4.0, 2.0]])

b_z = np.array([1., -1., 0.])[:, np.newaxis] # Søjle

# R_0 = R_0 - R_1 

b[0, :] -= b[1, :]
b_z[0] -= b_z[1]

# Pivot elementet er fundet for første række
# R_1 = R_2
# R_2 = R_1 

b[ [1,2], :] = b[ [2,1], :]
b_z[1], b_z[2] = b_z[2, 0], b_z[1, 0] 

# R_1 = R_1 - 2*R_2 

b[1, :] -= 2*b[2, :]
b_z[1] -= 2*b_z[2]

# Nu kan pivotelementet findes for midten

b[1, :] *= 1./8. 
b_z[1] *= 1./8.

# R_2 += R_0
b[2, :] += b[0, :]
b_z[2] += b_z[0]


# R_2 -= R_1
b[2,:] -= b[1,:]
b_z[2] -= b_z[1]


# R_2 *= 0,5 

b[2,:] *= 0.5
b_z[2] *= 0.5

# R_2 -= R_0 

b[2, :] -= b[0,:]
b_z[2] -= b_z[0]

# R_2 += 3*R_1

b[2, :] += 3*b[1,:]
b_z[2] += 3*b_z[1]

b[2, :] *= 0.5
b_z[2] *= 0.5

# EYYY vi nåede i hus.

# y = 0,25
# z = -0,4375 
# 1x + 3*0,25 - 3*(-0,4375)

b[0, 1] -= 3
b_z[0] -= 3*0.25 

b[0, 2] += 3 
b_z[0] += 3*(-0.4375)

# x = [-0.0625]
# y = [ 0.25  ]
# z = [-0.4375]

c = np.array([[2, -1, 2],
              [1, 1, -1]], dtype=float)

c_z = np.array([0,3], dtype=float)[:, np.newaxis]

# R_0 -= R_1 
c[0, :] -= c[1, :]
c_z[0] -= c_z[1]

# R_1 -= R_0
c[1,:] -= c[0,:]
c_z[1] -= c_z[0]

# R_1 *= 1/3

c[1,:] *= 1./3.
c_z[1] *= 1./3.

# Nu haves x & y som pivotelementer, z er ikke et pivotelement

#  [ 1.         -2.          3.        ] = -3
#  [ 0.          1.         -1.33333333] = 2 

#  [ 1.         -2.          3.        ] = -3
#  [ 0.          1.          0.        ] = 2 + 1.33333333z

#  [ 1.          0           3.        ] = -3 + 2y 
#  [ 0.          1.          0.        ] = 2 + 1.33333333z

#  [ 1.          0           3.        ] = -3 + 4 + 2.66666666z
#  [ 0.          1.          0.        ] = 2 + 1.33333333z

#  [ 1.          0        0.33333333   ] = 1
#  [ 0.          1.      -1.33333333   ] = 2


c[0, 1] += 2
c_z[0] += 2*2

c[0, 2] -= 2*1.33333333

# a*[2,1,2] + b[1, -2, 4] + c[-2, 1, 2]

# a & c er 2x2 matrixer

a_ny = np.zeros((3,3))
a_ny[0,0] = 1.0
a_ny[1,1] = 1.0

a_z_ny = np.zeros((3,1))
a_z_ny[0] = a_z[0]
a_z_ny[1] = a_z[1]

c_ny = np.zeros((3,3))
c_ny[0, :] = c[0,:]
c_ny[1, :] = c[1,:]

c_z_ny = np.zeros((3,3))
c_z_ny[0] = c_z[0]
c_z_ny[1] = c_z[1]

v_1 = [2,1,2]

print(a_z)
