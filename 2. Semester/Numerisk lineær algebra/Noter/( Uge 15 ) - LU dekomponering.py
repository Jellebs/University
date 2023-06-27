from Formelsamling.Numerisk_Lineær_Algebra import * 
import matplotlib.pyplot as plt
import numpy as np 
import sympy as sp 

def gaussian_eliminering_uden_ombytning(a):
    n, _ = a.shape
    u = np.copy(a)
    l = np.eye(n)
    for i in range(n-1): 
        l[i+1:, [i]] = u[i+1:, [i]] / u[i, i]
        u[i+1:, i:] -= l[i+1:, [i]] @ u[[i], i:] 
    return l, u

def forward_subs(l, b):
    _, n = l.shape
    y = np.empty((n, 1))
    for j in range(n):
        y[j] = (b[j] - l[[j], :j] @ y[:j] ) / l[j, j]
    return y

a = np.array([[2, 3, 4],
              [4, 3, 2], 
              [2, 4, 3]], dtype = float)
# l, u = gaussian_eliminering_uden_ombytning(a)

# print(l, u)
# print(np.allclose(l @ u, a)) # True

def eksempel_mat(n): 
    a = np.eye(n, dtype= float)
    a -= np.tri(n, k=-1)
    a[:, -1] = 1
    return a

a = eksempel_mat(10)
# print(a)

l, u = gaussian_eliminering_uden_ombytning(a)
print(u)

q, r = householder_qr(a)
print()

def forward_subs(l, b):
    _, n = l.shape
    y = np.empty((n, 1))
    for j in range(n):
        y[j] = (b[j] - l[[j], :j] @ y[:j] ) / l[j, j]
    return y