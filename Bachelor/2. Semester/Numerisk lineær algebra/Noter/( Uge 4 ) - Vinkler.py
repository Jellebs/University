import numpy as np 
import matplotlib.pyplot as plt 

# Ortogonale vektorer 
# cos(\theta) = (u, v) / (||u||_2 * ||v||_2) 

""" Laver v/||v||_2, men kræver v.

v_normaliseret = np.empty((10,7), dtype= float)
for i in range(0, 10): 
    v[:, [i]] = v[: ,[i]] / np.linalg.norm(v[:, [i]]) 

"""