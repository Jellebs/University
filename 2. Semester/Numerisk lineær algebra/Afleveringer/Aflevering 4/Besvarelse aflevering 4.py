import numpy as np 
import matplotlib.pyplot as plt

# a. Dan grammatricen for v0, v1, v2 & bekræft at den er ortogonal 

v0 = np.array([1, -1, 1, -1], dtype = float)[:,np.newaxis]
v1 = np.array([1, 1, -1, -1], dtype = float)[:,np.newaxis]
v2 = np.array([3, 0, 0, 3], dtype= float)[:,np.newaxis]

v = np.hstack([v0, v1, v2])

gram = v.T @ v
print(gram) 

print(np.vdot(v2, v0) + np.vdot(v2, v1) + np.vdot(v1,v0))

x = np.array([3, 2, 1, 0], dtype=float)[:, np.newaxis]

def projektion(v, u): 
    return np.vdot(v, u) / np.vdot(v, v) * v

projektion0 = projektion(v0, x)
projektion1 = projektion(v1, x)
projektion2 = projektion(v2, x)

v3 = x - (projektion0 + projektion1 + projektion2)
print(np.vdot(v3, v0), np.vdot(v3, v1), np.vdot(v3, v2))

def normVektor(v): 
    return v / np.linalg.norm(v) 

V = np.hstack([normVektor(v0), normVektor(v1), normVektor(v2), normVektor(v3)])
print(V)
print(V.T @ V)


