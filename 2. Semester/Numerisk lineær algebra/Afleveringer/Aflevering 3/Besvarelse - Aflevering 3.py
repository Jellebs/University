import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 

A = np.array([[2, 35],
              [5, 40], 
              [8, 50], 
              [10, 65], 
              [11, 70]], dtype = float)

fig, ax = plt.subplots()
ax.set_xlabel("Tid")
ax.set_ylabel("Temperatur")
ax.plot(A[:, 0], A[:, 1], 'o', markersize=10)
fig.savefig("Datapunkter.pdf")
# Lav estimations funktion som går gennem de sidste 3 punkter. 
# p(x) = a + bx + cx**2

x = A[:, 0][2:5].T
y = A[:, 1][2:5].T

# Ligning y = a + b*x + c*(x**2)
# Jeg har fundet på en måde at opstille et lineært ligningsystem 

# [ 8**0  8**1  8**2  ]   [ a ]   [ 50 ]
# [ 10**0 10**1 10**2 ] * [ b ] = [ 65 ]
# [ 11**0 11**1 11**2 ]   [ c ]   [ 70 ]

# == 

# [ a 8b   64c  ]   [ 50 ]
# [ a 10b  100c ] = [ 65 ]
# [ a 11b  121c ]   [ 70 ]
def skift(matrix, r1, r2): 
    matrix[[r1, r2], :] = matrix[[r2, r1], :]

def skaler(matrix, s, r): 
    matrix[r, :] *= s

def lægTil(matrix, r1, t, r2):
    matrix[r1, :] += t * matrix[r2, :] 

def erStatVærdier(matrix, søjle_ix, række_ix, y_søjle_ix): 
    # Eks: 
        # 0 b c 2
        # 0 0 c 10
        
        # ==
        # 0 b 0 12
        # 0 0 c 10
    for i in range(0, række_ix): 
        matrix[i, y_søjle_ix] += matrix[i, søjle_ix] * matrix[række_ix, y_søjle_ix]
        matrix[i, søjle_ix] = 0

a = sp.symbols('a')
b = sp.symbols('b')
c = sp.symbols('c')

# A * x = y
# I_n*x = A^-1*y

# Konstanterne trækkes over på den anden side af ligmedstegnet, så skift i fortegn.
A = np.array(
    [[1,  8,  64, 1, 0, 0, 50], 
     [1, 10, 100, 0, 1, 0, 65], 
     [1, 11, 121, 0, 0, 1, 70]], dtype=float)
# lægTil(Matrix, r1, t, r2) 
lægTil(A, 1, -1, 0)
lægTil(A, 2, -1, 0 )
lægTil(A, 2, -3/2, 1)

# Skaler(A, s, r)
skaler(A, 1/3, 2)
skaler(A, 1/2, 1)
lægTil(A, 1, -18, 2)
lægTil(A, 0, -64, 2)
lægTil(A, 0, -8, 1)

A_inv = A[:, 3:6] 
x = A_inv @ y

# Nu er a, b & c fundet i x. 
a = -76.6667 
b = 22.5 
c = -0.83333

ny_x = np.linspace(0, 15, 100)
ny_y = a + b*ny_x + c*(ny_x**2)
#ax.plot(ny_x, ny_y, label="Approksimeret funktion")

# Hvad er den mindste polynomium som opfylder, at den går i gennem hvert punkt? 

# Til at opstille polynomierne, vil jeg lave en funktion. 

def kreerPolynomium(x, n): # Laver en række af ønsket polynomium til x.
    # x = x værdi, n = grad. 
    r = None 
    for i in range(0, n + 1): # n+1 = Til og med n
        if i == 0: 
            r = np.array([x**i])
        else:
            r = np.append(r, [x**i])
    return r

def kreer_A_Matrice(x: list, n: int):
    A = None
    for i in range(0, len(x)):
        if i == 0: 
            A = np.array([kreerPolynomium(x[i], n)])
        else:  
            A = np.append(A, [kreerPolynomium(x[i], n)], axis= 0)
    return A

n = 4
A = kreer_A_Matrice([2, 5, 8, 10, 11], n)

b = np.array([35, 40, 50, 65, 70])
x = np.linalg.inv(A) @ b

# Koeffiecienter fundet

k1 = -1.97530864
k2 = 32.85493827
k3 = -9.09722222
k4 = 1.03395062
k5 = -0.03858025

x_3 = np.linspace(0, 15, 100)
y_3 = k1 + k2*x_3 + k3*(x_3**2) + k4*(x_3**3) + k5*(x_3**4)

#ax.plot(x_3, y_3, label="Fjedre grads pilynomium")

# d. opstil f(x) = p_1(x) for 2<= x <= 8, p2(x) for 8 <= x <= 11
# Hvor p1, p2 er tredjegrads polynomier og p1 indeholder 2, 5, 8 & p2 indeholder 8, 10, 11.

# tredjegradspolynomier kræver 4 variabler. 
# Så systemet medfører 8 ubekendte, 6 ligninger => 2 frie variabler. 

A = np.array([
    [1, 2,  4,   8, 0,  0,   0,    0], 
    [1, 5, 25, 125, 0,  0,   0,    0], 
    [1, 8, 64, 512, 0,  0,   0,    0], 
    [0, 0,  0,   0, 1,  8,  64,  512], 
    [0, 0,  0,   0, 1, 10, 100, 1000], 
    [0, 0,  0,   0, 1, 11, 121, 1331], 
    [0, 1, 16, 192, 0, -1, -16, -192], 
    [0, 1,  4,  12, 0,  0,   0,    0]
    ], dtype=float)

b = np.array([35, 40, 50, 50, 65, 70, 0, 1.5])[:, np.newaxis]

In = np.eye(8, 8)

a = np.linalg.solve(A, b)
print(a)
x_1 = np.linspace(2, 8, 50)
x_2 = np.linspace(8, 11, 50)

y_1 = a[0] + a[1]*x_1 + a[2]*(x_1**2) + a[3]* (x_1**3)
y_2 = a[4] + a[5]*x_2 + a[6]*(x_2**2) + a[7] * (x_2**3)

ax.plot(x_1, y_1, label = "P1(x)")
ax.plot(x_2, y_2, label = "P2(x)")

ax.legend()
fig.savefig("P1 & P2.pdf")