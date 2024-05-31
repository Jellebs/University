import numpy as np
from Formelsamling.Numerisk_Lineær_Algebra import *

# Eksempel fra forelæsning. Tynd QR data fra Householder
# Beregn Householder v, s for 
# (a) søjle 0 i A.
# (b) søjle 0 i H0 @ A [1:, 1:]
# (c) søjle 0 i H1 @ H0 @ A [2:, 2:] ... 
# gem v data under diagonalen i R 

# A = QR 
# Q = H0 @ H1 @ ... @ Hk-1
# Obs. H0@A = (I_n - svv.T)A = A - (sv)(v.T @ A)

def householder_qr_data(a): # Flops = cirka 2nk^2 - 2/3k^3
    data = np.copy(a)
    _, k = a.shape
    s = np.empty(k)
    for j in range(k): 
        v, s[j] = house(data[j:, [j]])
        data[j:, j:] -= ((s[j] * v)) @ (v.T @ data[j:, j:])
        data[j+1:, [j]] = v[1:]
    return data, s

# Mindste kvadratters metode vha. house
# Q.T @ b = (Hk-1@Hk-2@...@(H0 @ b))[:k]
# Rx = Q.T@b løses vha. back substitution.

def householder_lsq(a, b): 
    data, s = householder_qr_data(a)
    _, k = a.shape
    r = np.triu(data[:k, :k])
    c = np.copy(b) 
    for j in range(k): 
        x = data[j+1:, [j]]
        v = np.vstack([[1], x])
        c[j:] -= (s[j] * np.vdot(v, c[j:])) * v
        back_substitution(r, c[:k])



