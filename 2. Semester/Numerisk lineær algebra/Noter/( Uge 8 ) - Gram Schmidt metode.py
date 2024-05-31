import numpy as np
import matplotlib.pyplot as plt
from Formelsamling.Numerisk_Lineær_Algebra import * 

s = 1e-8 
u0 = np.array([1, s, 0, 0], dtype= float) [:, np.newaxis]
u1 = np.array([1, 0, s, 0], dtype= float) [:, np.newaxis]
u2 = np.array([1, 0, 0, s], dtype= float) [:, np.newaxis]

a = np.hstack([u0, u1, u2])
print(a)

def projPå(v, u):
    return np.vdot(v, u) / np.vdot(v, v) * v 

w0 = u0 
v0 = w0 / np.linalg.norm(w0)
w1 = u1 - projPå(v0, u1)
v1 = w1 / np.linalg.norm(w1)
w2 = u2 - projPå(v0, u2) - projPå(v1, u2)
v2 = w2 / np.linalg.norm(w2)

q = np.hstack([v0, v1, v2])
print(q)

gram = q.T @ q 
print(gram)

# Indre produkt mellem v1 og v2 er langt fra 0. 

print(np.arccos(np.vdot(v1, v2)) * 180 / np.pi) # 60°, langt fra den 90° vinkelrette linje.


# Anden fremgansmåde 
w0 = u0 
v0 = w0 / np.linalg.norm(w0)
w1 = u1 - projPå(v0, u1)
x2 = u2 - projPå(v0, u2)
v1 = w1 / np.linalg.norm(w1)
w2 = x2 - projPå(v1, x2) 
v2 = w2 / np.linalg.norm(w2)

q = np.hstack([v0, v1, v2])
print(q)

gram = q.T @ q 
print(gram)

# Implementer klassisk Gram Schmidt

print(a.shape)

m, n = a.shape
_, k = a.shape # Hvis en af værdierne er uden betydning, bruges _ til den som ikke ønskes.

def klassiskGramSchmidt(a):
    _, k = a.shape 
    q = np.empty_like(a)
    r = np.zeros((k,k))
    for j in range(0, k): 
        r[:j, [j]] = q[:, :j].T @ a[:, [j]]
        w = a[:, [j]] - q[:, :j] @ r[:j, [j]]
        r[j, j] = np.linalg.norm(w)
        q[:, [j]] = w / r[j, j]
    return q,r 

q, r = klassiskGramSchmidt(a)
# print(r)

# Forsøg med den forbedrede gram schmidt
def forbedretGramSchmidt(a):
    _, k = a.shape
    q = np.copy(a)
    r = np.zeros((k,k))
    for i in range( 0, k):
        r[i, i] = np.linalg.norm(q[:, i])
        q[:, i] /= r[i, i]
        r[[i], i+1:] = q[:, [i]].T @ q[:, i+1:]
        q[:, i+1:] -= q[:, [i]] @ r[[i], i+1:]
    return q, r

q, r = forbedretGramSchmidt(a)
# print(q)
# print(np.allclose(q @ r, a) ) # True, så værdien går ikke tabt i beregingen. q @ r == a 

q, r = gramSchmidt(forbedretGramSchmidt=True, a=a) # Formel lavet i min formelsamling
# print(q, r) # Giver det samme resultat som lavet lige før for forbedret gram schmidt.

q, r = gramSchmidt(forbedretGramSchmidt=False, a=a)
# print(q, r) # Giver det samme resultat som lavet lige før for klassisk gram schmidt.



# Eksperiment!

rng = np.random.default_rng()
n = 150

# 2 tilfældige ortogonale matrice
u, _, vt = np.linalg.svd(rng.standard_normal((n,n)))

# dan nogle singulærværdier 
i = np.arange(n)
s = np.array(2.0**(-i))

# ny matrix med disse singulærværdier
a = u @ np.diag(s) @ vt
qk, rk = gramSchmidt(forbedretGramSchmidt=False, a= a)
qf, rf = gramSchmidt(forbedretGramSchmidt=True, a= a)

fig, ax = plt.subplots()
ax.set_yscale('log')
ax.grid()
ax.plot(i, rk[i,i], "o", label="Klassisk Gram Schmidt")
ax.plot(i, rf[i,i], "x", label="Forbedret Gram Schmidt")
ax.plot(i, s[i], "*", label="Singulærværdier")

ax.legend()

fig.savefig("( Uge 8 ) - Effekt af forbedret GS.pdf")


