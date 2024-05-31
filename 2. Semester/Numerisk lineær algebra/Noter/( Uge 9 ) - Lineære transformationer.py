import numpy as np

def L(v):  # Lineær transformation = Ax 
    x = v[0, 0]
    y = v[1, 0]
    return np.array([2*x-y, y+x, y-2*x], dtype= float)[:, np.newaxis]

e0 = np.array([1.0, 0.0])[:, np.newaxis]
e1 = np.array([0.0, 1.0])[:, np.newaxis]

print(L(e0)) # Ae0 = A_0 
print(L(e1)) # Ae1 = A_1

a = np.hstack((L(e0), L(e1)))
print(a)

rng = np.random.default_rng()
v = rng.standard_normal((2,1))
print(v)

print(np.allclose(L(v), a @ v))

