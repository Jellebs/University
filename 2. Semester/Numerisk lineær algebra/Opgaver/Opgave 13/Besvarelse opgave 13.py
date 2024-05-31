import numpy as np 
import sympy as sp 
import matplotlib.pyplot as plt 
from Formelsamling.Numerisk_Lineær_Algebra import * 
np.set_printoptions(precision=2)
# a. Betragt matricen 
A = np.array([
    [-1, 2], 
    [2, -1]]) # y't(Ay)
# Bestem egenværdierne for A og en ortonormal basis af egenvektorer.
eq, (lambda0, lambda1) = findLambda(A)
eq1 = A - float(lambda0)*np.eye(A.shape[0])

lægTil(eq1, 1, -1, 0)
skaler(eq1, 1/2, 0)
# x + y = 0, y = -x
v0 = np.array([1, -1])[:, np.newaxis]

eq2 = A - float(lambda1)*np.eye(A.shape[0])

lægTil(eq2, 1, 1, 0)
skaler(eq2, -1/2, 0)
# x - y = 0, y = x
v1 = np.array([1,  1])[:, np.newaxis]

v = np.hstack([v0, v1])
lambda_mat = np.diag([lambda0, lambda1])
# Test af vektorer
# print(v @ lambda_mat @ np.linalg.inv(v)) == A, så vektorerne passer. 

y0 = np.array([1, 3]) [:, np.newaxis] # y0(0)= 3, y1(0) = 1 

# y(t) = c0*v0*e^(lambda0*t) + c1*v1*e^(lambda1*t) + ...
c0, c1 = np.linalg.solve(v, y0)
t = np.linspace(0, 100, 100)

løsning = (c0 * v0 * np.exp(float(lambda0) * t) # SKAL LAVES TIL FLOAT, igen et sympy format fejl.
           + c1 * v1 * np.exp(float(lambda1) * t))

fig, ax = plt.subplots()
# print(løsning)
ax.plot(*løsning, color = 'b', marker='o', markevery=10, markersize=4)
ax.legend()



# Opgave 13.2. Antag at A = Vdiag(sigma)V^(-1) er en (3 x 3) matrix, som er diagonaliserbar
# med egenværdier lambda0, lambda1, lambda2. Vis at de følgende matricer er diagonaliserbar og bestem deres egenværdier
# a.3A  
# b.2A - I_n3 
# c.A^2
# d. A^4 - 3A^3 + 2A^2 - A + 6I_n3

# Hvis sigma = -1 & mu = 1 er egenværdier for A & A har en basis af vektorer, så er A diagonaliserbar.
# Hvis A opfylder at A = VSigmaV^(-1), hvor Sigma er en diagonal matrix & V er en kvadratisk matrix som er invertibel, 
# så er A diagonaliserbar. 



# Opgave 13.3. Lad 
A = np.array([
    [ 4,  3,  3], 
    [-3, -2, -3], 
    [-3, -3, -2]])
# a. Vis at lambda0 = -2 er en egenværdi for A og find en tilhørende egenvektor v0. 

eq0, (lambda0, lambda1) = findLambda(A) # Har kun 2 rødder
# eq0 = -Lambda**3 + 3*lambda - 2
# En egenværdi kendes til at være 1 

# Lambda(-Lambda**2 + 3) -2 
# 1(-Lambda**2 + 3) -2 
lambda_sym = sp.symbols("Lambda")
coeffs = np.array([-1, 0, 3, -2])



# eq0 = -(-2)^3 - 6 - 2 = 0 == True
# print(lambda0, lambda1)
eq0 = A - lambda0*np.eye(A.shape[0])
lægTil(eq0, 2, -1, 1)
skaler(eq0, 1/6, 0)
skift(eq0, 2, 1)
lægTil(eq0, 2, 3, 0)
lægTil(eq0, 2, 1/2, 1)
skaler(eq0, -1/3, 1)
lægTil(eq0, 0, -1/2, 1)

# x + z = 0
# x = -z
# -x = z

# y - z = 0
# y = z

# y = (z), y = -x  
# z er en fri variabel

# print(eq0)
v0 = np.array([1, -1, 1])[:, np.newaxis] # y, -x, z

# b. Bestem de andre egenværdier for A. 
lambda1

# c. Find en basis af egenvektorer for A. 
eq1 = A - lambda1*np.eye(A.shape[0])
skaler(eq1, 1/3, 0)
lægTil(eq1, 1, 3, 0)
lægTil(eq1, 2, 3, 0)
# x + y + z = 0
# y & z er egenværdier
# y = - x - z 
# z = -1, x = -1, y = 2 
v1 = np.array([2, -1, -1])[:, np.newaxis]

v = np.hstack([v0, v1])
lambda_mat = np.diag([lambda0, lambda1])
# print(v.shape, lambda_mat.shape)

# Problematik. 
# Kun to egenværdier medfører udlighed i Matricerne. 
# V er ikke invertibel. 
# Sigma er 2x2

# Der er teknisk set kun 2 rødder. I punktet (0, 1), skifter den retning, hvis vi antager at dette punkt er to egenværdier i sig selv, kan vi finde en løsning
v2 = v1

v = np.hstack([v0, v1, v2])
lambda_mat = np.diag([lambda0, lambda1, lambda1])

# print(v @ lambda_mat @ np.linalg.inv(v)) # => fejl.
# Søjle 1 == søjle 2 => 2 pivotpoints og en fri variabel => ikke invertibel.

# Hvad skal jeg tage med fra det her? 
# Hvis meget i tvivl få et visuelt perspektiv på hvordan ligningen ser ud. 

# Opgave 13.4. Betragt det elektriske kredsløb i figur 1, og lad v_c være spændingsfaldet over kondensatoren C. 
# a. Vis at i og v_c opfylder 

# [ i' ]   [-R/L, -1/L]   [ i ]
# [ v'c] = [ 1/C,    0] = [v_c] 

# y' = Ay

# b. Bestem løsninger til system med i(0) = 0A, v_c(0) = 10V for 
# I: L = 1H, R = 4Ohm & C = (1/3) F

A = np.array([[   -4/1, -1/1], 
              [1/(1/3),    0]])
eq, (lambda0, lambda1) = findLambda(A)
# y'(t) = c * v * e^(lambda_n*t), t = 0 => c*v = y'(0)

eq1 = A - float(lambda0) * np.eye(A.shape[0])
skaler(eq1, -1, 0)
lægTil(eq1, 1, -3, 0)
# x + y = 0 
# y = -x
v0 = np.array([1, -1])[:, np.newaxis]

eq2 = A - float(lambda1) * np.eye(A.shape[0])
skaler(eq2, -1, 0)
lægTil(eq2, 1, -1, 0)
# 3x + y = 0 
# y = -3x 
v1 = np.array([3, -1])[:, np.newaxis]
y0 = np.array([10, 0]) # 10V & 0A
v = np.hstack([v0, v1])
c = np.linalg.solve(v, y0)
print(c)

løsning = (c[0]*v0 * np.exp(float(lambda0) * t)
           + c[1]*v1 * np.exp(float(lambda1) * t)) 
fig, ax = plt.subplots()
ax.plot(*løsning)

A = np.array([[   -4/1, -1/1], 
              [1/(1/104),    0]])

_, (lambda0, lambda1) = findLambda(A)
eq1 = A - lambda0*np.eye(A.shape[0])
eq2 = A - lambda1*np.eye(A.shape[1])

# skaler(eq1, 0, -1/2)
# Komplekse værdier giver rod.

print(eq1)

A = np.array([[1j, 2, -1j,  4],
              [0,  1,  -1,  1j], 
              [0,  0,  1j,  1], 
              [0,  0,   0,  1]])

print(np.linalg.det(A))