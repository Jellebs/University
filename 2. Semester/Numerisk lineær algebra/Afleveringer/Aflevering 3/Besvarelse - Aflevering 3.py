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
ax.plot(A[:, 0], A[:, 1], marker='o', markersize=10)
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
print(A[:, 0:3])
print(A[:, 3:7])

A_inv = A[:, 3:6] 
x = A_inv @ y

# Nu er a, b & c fundet i x. 
a = -76.6667 
b = 22.5 
c = -0.83333

ny_x = np.linspace(0, 15, 100)
ny_y = a + b*ny_x + c*(ny_x**2)
ax.plot(ny_x, ny_y, label="Approksimeret funktion")
fig.savefig("Datasæt og approksimation af temperatur.pdf")
ax.legend()
