
import numpy as np 
import matplotlib.pyplot as plt 

A = np.array([[1.0, 2.0],
              [3.0, 2.0]])
B = np.linalg.inv(A)
print(B)
B @ A 
A @ B