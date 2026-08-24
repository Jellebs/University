import numpy as np
from Formelsamling.Numerisk_Lineær_Algebra import *
# A^-1Ax = A^-1b
A = np.array([
    [20, 10, 0, 1, 0, 0, 575.0], 
    [0,  10, 5, 0, 1, 0, 587.5], 
    [0,   0, 5, 0, 0, 1, 712.5]], dtype=float)

skaler(A, 1/5, 2)
lægTil(A, 1, -5, 2)
skaler(A, 1/10, 1)
skaler(A, 1/20, 0)

lægTil(A, 0, -0.5, 1)
print(A[:, 0:3])

print(A[:, 3:6], A[:, 6])
x = A[:, 3:6] @ A[:, 6] # A^-1 * b
print(x)
