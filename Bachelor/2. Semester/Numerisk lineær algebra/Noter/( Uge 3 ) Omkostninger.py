import numpy as np 
for i in range(5): 
    print(i)

# Til at beregne flops, floating point operators 
rng = np.random.default_rng()
a = rng.standard_normal((2000, 100))
b = rng.standard_normal((100, 300))
c = rng.standard_normal((300, 20))
"""
print(f'{a}\n')
print(f'{b}\n')
print(f'{c}\n')
"""

# I interactiv vindue 
# %timeit a @ ( b @ c ) # 7 runs, 1000 loops each, tog 8.1 sek
# %timeit (a @ b) c 7 runs, 100 loops each, tog 6.5 sekunder

# Ligningssystemer 
"""
A = np.array(
    [2, 3, -4], 
    [3,-4,1], 
    [1,1,2]
    )
x = [x, y, z]
b = [7, -2, 3]
A * x = b
"""

# (I) R_i <-> R_j = a[ [i,j], :] = a[ [j,i] :]
# (II) R_i <-> sR_i(s≠0) = a[i, :] = *= s
# (III) R_i <-> R_i + tR_j(j ≠ i) += t * a[j, :]

a = np.array([[2.0, 3.0, -4.0], [3.0, -4.0, 1.0], [1.0, 1.0, 2.0]])
b = np.array([7.0, -2.0, 3.0]) [:,np.newaxis]
aub = np.hstack([a,b])
aub 
aub[ [0,2], :]= aub[ [2, 0], :]
aub
aub[1,:] += (-3)* aub[0, :]
aub[2,:] += (-2)*aub [0, :]
aub
aub[2,:] += 7*aub[1, :]
aub[2, :] *= 1/(-61.0)
aub[1, :] += 8 * aub[2, :]
aub[0, :] += (-2) * aub[2, :]
aub[0, :] += (-1) * aub[1, :]
print(f"aub: {aub}") # Forkert