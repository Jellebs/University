import numpy as np 
from sympy import * 
from Formelsamling.Numerisk_Lineær_Algebra import *
np.set_printoptions(precision=3)
a = np.array([[0.98, 0.03],
              [0.02, 0.97]])

w0 = np.array([3.,2.]) [:, np.newaxis]
w1 = np.array([1., -1.]) [:, np.newaxis]
print(a @ w0)
print(a @ w1)

A = Matrix([
    [0.98, 0.03], 
    [0.02, 0.97]])

lmb = symbols("Lambda")

ligning = det(A - lmb*eye(2))
print(ligning)

lmb0, lmb1 = solve(ligning, lmb)

lmb0 = float(lmb0) # Sympy bruger ikke floats her
lmb1 = float(lmb1)
v0 = a - lmb0 * np.eye(2)
lægTil(v0, 1, -2/3, 0)
v0 = v0[0, :][:, np.newaxis] # Egenvektore

v1 = a - lmb1 * np.eye(2)
lægTil(v1, 1, 1, 0)
v1 = v1[0, :][:, np.newaxis] # Egenvektore

# Eksempel fra mentimeter
A = Matrix([[2, 1], 
            [0, -1]])
ligning1 = det(A - lmb*eye(2))
print(ligning1)
print(solve(ligning1, lmb)) # Egenværdier

# Eksempel fra forelæsningen 

print(a @ v0 - lmb0 * v0)
v = np.hstack([v0, v1])

lambda_mat = np.diag([lmb0, lmb1])


# print(v, lambda_mat)
print(v @ lambda_mat @ np.linalg.inv(v)) # Determinanter er dårlige numerisk. 

