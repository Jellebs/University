import numpy as np
from Formelsamling.Numerisk_Lineær_Algebra import * 

def sing_skridt_del(a, v): 
    w = a @ v 
    sigma = np.linalg.norm(w)
    u = w / sigma 
    return sigma, u

rng = np.random.default_rng()
m = 5 
n = 3 
a = rng.normal(0, 5, (m, n))

print(a)
len = 20 
sigma_out = np.zeros(2*len)

v = rng.standard_normal((n, 1))
v /= np.linalg.norm(v)

for k in range(len): 
    sigma_out[2*k], u = sing_skridt_del(a, v)
    sigma_out[2*k+1] , v = sing_skridt_del(a.T, u)

print(sigma_out)

_, s, _ = np.linalg.svd(a, full_matrices=False)
print(s[0]) 
# Nu vides der hvordan man kan finde de singulære værdier, uden numpys svd funktion. 


# Invers potensmetoden: 
def inv_potens_skridt(q, r, mu, w):
    y = q.T @ w
    u = back_substitution(r, y)
    u /= np.linalg.norm(u)
    lambda_ny = np.vdot(u, a @ u) 
    return lambda_ny, u

a = rng.normal(0, 5, (5, 5))
a += a.T

mu = -5.0 
q, r = householder_qr(a- mu*np.eye(a.shape[0]))

n = 20
lambda_out = np.empty(n)

w = rng.standard_normal((5, 1))
w /= np.linalg.norm(w)

for i in reversed(range(n)): 
    lambda_out[i], w = inv_potens_skridt(q, r, mu, w)


print(lambda_out)
print(np.linalg.eigvals(a)) # Egenværdier

# Reduktion til Hessenberg form
# Problem: H_0 = H_0^T = H_0^(-1)

# for k in { , ..., n-3 }: 
#   Beregn Householder H_k for A_[k+1:, k]
#   A = H_k @ AH_k

def hessenberg_data(a): 
    data = np.copy(a)
    n, _ = a.shape
    s = np.empty(n-2)
    for j in range(n-2): 
        v, s[j] = house(data[j+1:, [j]])
        data[j+1:, j:] -= (
            (s[j] * v) @  (v.T @ data[j+1:, j:]))
        data[:, j+1:] -= ( 
            (s[j] * (data[:, j+1:] @ v )) @ v.T)
        data[j+2:, [j]] = v[1:]
    return data, s
def hessenberg(a): 
    data, s = hessenberg_data(a)
    return np.triu(data, -1)

a = rng.normal(0, 5, (5,5))

hesse = hessenberg(a)
print(hesse)
print(hesse[:, 0])
print(hesse[:, 1])
print(hesse[:, 2])


def hessenberg_qh(a): 
    data, s = hessenberg_data(a)
    n, _ = a.shape
    h = np.triu(data, -1)
    q = np.eye(n)
    for j is reversed(range(n-2)):
        x = data[j+2:, [j]]
        v = np.vstack([[1], x])
    q[j+1:, j+1:] -= (s[j] * v ) @ (v.T @ q[j+1:, j+1:])
    return q, h

a = np.round(a)
q, h = hessenberg_qh(a)
print(q.T @ q) # Ortogonale matrice? 

