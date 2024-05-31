import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 
from Formelsamling.Numerisk_Lineær_Algebra import * 

# To beholder er forbundne med rør, som i figur 2. 
# A rummer 300L, 90g salt
# B rummer 100L, 30g salt
# a tilføres 30L/min rent vand
# b tilføres 15L/min blanding

# a. Hvor meget blanding skal flyde igennem rær c per minut, hvis væskemængden i beholder A skal være konstant? 
# Hvor meget skal flyde ud igennem rør d, for at væskemængden i B er konstant

# A = 30L/min + 15L/min - c = 0
c = 45 # L/min 

# B = c - b = 0
# B = 45L - 15L - d = 0
d = 30 # L/min


# b. Gør rede for at saltmængderne y0(t) i A og y1(t) i B opfylder systemet

# y'0(t) = -0,15y0(t) + 0,15y1(t)
# y'1(t) = 0,15y0(t) - 0,45y1(t)

A = sp.Matrix([[-0.15,  0.15], 
              [ 0.15, -0.45]])

y0 = np.array([90, 30]) [:, np.newaxis]



# c. I python beregn egenværdier og egenvektorer for koefficientmatricen for systemet.


ligning, (lambda0, lambda1) = findLambda(A)
print(ligning)
print(lambda0)
print(lambda1)

A = np.array([[-0.15,  0.15], 
              [ 0.15, -0.45]])
print(A)


ligning1 = A - lambda0*sp.eye(A.shape[0])
ligning1_np = np.array(ligning1)
skaler(ligning1_np, 1/ligning1_np[0,0], 0)
lægTil(ligning1_np, 1, -ligning1_np[1,0]/1, 0)
# 1x + 0,4142y = 0
# y = (-1/0,4142)x 
print(ligning1_np)

v0 = np.array([1, -1/0.4142]) [:, np.newaxis] # y, x

ligning2 = np.array(A - lambda1*sp.eye(A.shape[0]))

skaler(ligning2, 1/ligning2[0,0], 0)
lægTil(ligning2, 1, -0.15, 0)
print(ligning2)
# 1x + -2,4142y = 0
# y = (1/2,4142)x

v1 = np.array([1, 1/2.4142]) [:, np.newaxis] # y, x
v = np.hstack([v0, v1])

svar = f"Egenværdierne: \nLambda0 = {lambda0}, \nLambda1 = {lambda1}.\n Egenvektorerne: \n v0 =\n{v0}, \nv1 =\n{v1}"
opgaveBesvarelse("Opgave c", svar)


# d. Brug de fundne egenværdier og egenvektorer til at bestemme løsninger y0(t) og y1(t) med det givne startdata.

# y(t) = c*v*e^(lambda*t)
# y(0) = c*v

c0, c1 = np.linalg.solve(v, y0) # ax = b, a^-1b = x 

svar = f"Løsningerne findes til at være \nc0 = {c0}, \nc1 = {c1}" 
opgaveBesvarelse("Opgave 9.d", svar)

# e. Plot funktionerne y0(t) og y1(t) mod t og lav også et plot af y0(t) mod y1(t)
t = np.linspace(0, 100, 100)
løsning = c0*v0*np.exp(float(lambda0)*t) + c1*v1*np.exp(float(lambda1)*t)

plots = ["Løsning på vandbeholder system y0 til t.pdf", "Løsning på vandbeholder system y1 til t.pdf", "Løsning på vandbeholder system y0 mod y1.pdf"]
i = 0
for plot in plots: 
    fig, ax = plt.subplots()
    ax.annotate("", xy= løsning[:, 5], xytext=løsning[:, 4], arrowprops=dict(arrowstyle='->', color='b'))
    if i == 0 or i == 1: 
        ax.plot(t, løsning[i], color='b', marker='o', markevery=10, markersize=4)
        ax.set_xlabel('$t$')
        ax.set_ylabel(f'$y{i}$')            
        
    elif i == 2: 
        ax.plot(*løsning, color='b', marker='o', markevery=10, markersize=4)
        ax.set_xlabel('$y_{0}$')
        ax.set_ylabel('$y_{1}$')
    fig.savefig(plot)
    
    i += 1
t = sp.symbols("t")
y0t = c0 * v0[0]*sp.exp(-0.5*t) + c1*v1[0]*sp.exp(-0.088*t)
y1t = c1 * v1[1]*sp.exp(-0.5*t) + c1*v1[1]*sp.exp(-0.088*t)
print(sp.limit(y1t[0]/y0t[0], t, 0))
print(287127965634281/225000000000000)