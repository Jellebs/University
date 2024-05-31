import numpy as np 
import sympy as sp
from Formelsamling.Numerisk_Lineær_Algebra import * 

# Efter tjek af A = VLambdaV^-1 
v = np.array([[ 0, 0, 1], 
              [ 1, 1, 0], 
              [-1, 1, 0]])

lambda0, lambda1, lambda2 = 0, 2, 3
Lambda_diag = np.diag([lambda0, lambda1, lambda2])

A = v @ Lambda_diag @ np.linalg.inv(v)
print(A)


A = sp.Matrix([[3, 0, 0], 
               [0, 1, 1], 
               [0, 1, 1]])

A2 = A @ A 

eq, (lambda0, lambda1, lambda2) = findLambda(A2)
Lambda_diag = np.diag([lambda0, lambda1, lambda2])

print(v @ Lambda_diag @ np.linalg.inv(v))